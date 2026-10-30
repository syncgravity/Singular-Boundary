"""Checkpointed interacting SU(2) Wilson runs on geometrically paired Stage 7 tori.

Purpose: reproducible continuation, exact local-action Metropolis updates, no inference
from unequilibrated hot starts. Every measurement is tagged burn-in/production.
Custom stored-state xorshift128+ generator (not cryptographic); production should
add independent PRNG robustness checks. Checkpoints use atomic os.replace.
"""
from __future__ import annotations
import argparse,hashlib,json,os,time
from pathlib import Path
import numpy as np
from numba import njit
from stage7_large_torus import assemble_vectorized,pair
from wilson_torus import mul,face_trace_scalar

@njit
def next_uint64(st):
    x=st[0];y=st[1]
    st[0]=y
    x^=x<<np.uint64(23)
    x^=x>>np.uint64(17)
    x^=y
    x^=y>>np.uint64(26)
    st[1]=x
    return x+y

@njit
def rand(st):
    return float(next_uint64(st)>>np.uint64(11))*(1.0/9007199254740992.0)

@njit
def gaussian_pair(st):
    """Box-Muller normals from independent high-53-bit PRNG uniforms."""
    v=max(rand(st),1e-300)
    phi=2*np.pi*rand(st)
    radius=np.sqrt(-2*np.log(v))
    return radius*np.cos(phi),radius*np.sin(phi)

@njit
def initialize(L,st):
    """Four independent standard normals / norm = exact Haar measure on SU(2)."""
    links=np.empty((L,4),np.float64)
    for i in range(L):
        a,b=gaussian_pair(st)
        c,d=gaussian_pair(st)
        links[i,0]=a;links[i,1]=b;links[i,2]=c;links[i,3]=d
        links[i]/=np.sqrt(np.dot(links[i],links[i]))
    return links

@njit
def get_plaquettes(links,fi,sg):
    pf=np.empty(len(fi),np.float64)
    for f in range(len(fi)):pf[f]=face_trace_scalar(f,links,fi,sg)
    return pf

@njit
def sweep(links,pf,fi,sg,beta,adj,degree,st,angle):
    accepted=0
    proposed=np.empty(adj.shape[1],np.float64)
    for eid in range(len(links)):
        z=2*rand(st)-1
        phase=2*np.pi*rand(st)
        r=np.sqrt(max(0.,1-z*z))
        theta=rand(st)*angle
        ss=np.sin(theta)
        dq=np.array([np.cos(theta),ss*r*np.cos(phase),ss*r*np.sin(phase),ss*z])
        trial=mul(dq,links[eid])
        delta=0.
        for k in range(degree[eid]):
            p=adj[eid,k]
            proposed[k]=face_trace_scalar(p,links,fi,sg,eid,trial)
            delta+=beta[p]*(proposed[k]-pf[p])
        u=max(1e-300,rand(st))
        if np.log(u)<delta:
            links[eid]=trial
            accepted+=1
            for k in range(degree[eid]):pf[adj[eid,k]]=proposed[k]
    return accepted

def rng_state(kind,seed):
    digest=hashlib.sha256(f'Stage7 {kind} seed {seed}'.encode()).digest()
    st=np.frombuffer(digest[:16],dtype='<u8').copy()
    if not np.any(st):st[0]=1
    return st

def setup_geometry(kind,nt,beta):
    pen,square=pair()
    g=pen if kind=='penrose' else square
    a=(pen['physical_area']/pen['F'])**.5
    return g,assemble_vectorized(g,nt,beta,a)

def process(checkpoint,kind='penrose',seed=101,nt=20,beta=3.5,total_sweeps=2,
            burn=1000,thin=10,limit=2,verify=True,measure=False,initial_state='haar'):
    if initial_state not in ('haar','cold'):
        raise ValueError('initial_state must be haar or cold')
    cp=Path(checkpoint);cp.parent.mkdir(parents=True,exist_ok=True)
    geom,lat=setup_geometry(kind,nt,beta)
    settings={'kind':kind,'seed':seed,'nt':nt,'beta':beta,'burn':burn,'thin':thin,
              'spatial_geometry_hash':geom['graph_hash'],'L':lat['L'],'P':lat['P'],
              'rng_scheme':'xorshift128plus-high-53-v1','initial_state':('Haar_SU2_normalized_four_Gaussians' if initial_state=='haar' else 'cold_identity_SU2')}
    if cp.exists():
        with np.load(cp,allow_pickle=False) as z:
            old=json.loads(str(z['settings_json'].item()))
            if old!=settings:raise ValueError('checkpoint parameter or graph mismatch')
            links=z['links'].copy();pf=z['plaquette_trace'].copy();st=z['rng'].copy()
            completed=int(z['sweeps'].item())
            history=json.loads(str(z['history_json'].item()))
            saved_obs=list(z['observables_scalar']) if 'observables_scalar' in z.files else []
            saved_flux=list(z['observables_flux']) if 'observables_flux' in z.files else []
            saved_wilson=list(z['observables_wilson']) if 'observables_wilson' in z.files else []
            measured_sweeps=list(z['measured_sweeps']) if 'measured_sweeps' in z.files else []
    else:
        st=rng_state(kind if initial_state=='haar' else kind+'_cold',seed)
        if initial_state=='haar':
            links=initialize(lat['L'],st)
        else:
            links=np.zeros((lat['L'],4),np.float64)
            links[:,0]=1.0
        pf=get_plaquettes(links,lat['fi'],lat['sg'])
        completed=0;history=[];saved_obs=[];saved_flux=[];saved_wilson=[];measured_sweeps=[]
    upto=min(total_sweeps,completed+limit)
    start=time.monotonic()
    # Geometry, smear loops and winding paths are constructed only when a
    # production sample is actually scheduled. No measured gauges discarded.
    has_measures=any((k+1)>burn and ((k+1-burn)%thin==0) for k in range(completed,upto))
    if has_measures and not measure:
        raise ValueError('production samples would be lost: resume with --measure')
    plan=None
    if has_measures:
        from stage7_measurement import build_measurement_plan,measure_configuration
        plan=build_measurement_plan(geom)
    for it in range(completed,upto):
        accepted=sweep(links,pf,lat['fi'],lat['sg'],lat['beta'],lat['adj'],lat['degree'],st,.95)
        means=pf.reshape(nt,geom['F']+geom['E'])
        history.append({'sweep':it+1,'acceptance':accepted/lat['L'],
          'spatial_plaquette':float(means[:,:geom['F']].mean()),
          'temporal_plaquette':float(means[:,geom['F']:].mean()),
          'status':'burn_in' if it+1<=burn else 'production'})
        if plan is not None and it+1>burn and ((it+1-burn)%thin==0):
            obs,flux,rect=measure_configuration(links,nt,geom,plan)
            saved_obs.append(obs);saved_flux.append(flux)
            saved_wilson.append(rect);measured_sweeps.append(it+1)
    err=float(np.max(np.abs(get_plaquettes(links,lat['fi'],lat['sg'])-pf))) if verify else None
    if err is not None and err>=1e-9:raise AssertionError('cache mismatch')
    tmp=cp.with_name(cp.stem+'.partial.npz')
    np.savez_compressed(tmp,links=links,plaquette_trace=pf,rng=st,sweeps=np.int64(upto),
         settings_json=json.dumps(settings),history_json=json.dumps(history),
         measured_sweeps=np.asarray(measured_sweeps,dtype=np.int64),
         observables_scalar=np.asarray(saved_obs,dtype=np.float64).reshape((-1,nt,9)),
         observables_flux=np.asarray(saved_flux,dtype=np.float64).reshape((-1,nt,6)),
         observables_wilson=np.asarray(saved_wilson,dtype=np.float64).reshape((-1,3,100,nt//2)))
    os.replace(tmp,cp)
    digest=hashlib.sha256(cp.read_bytes()).hexdigest()
    result={'settings':settings,'completed_sweeps':upto,'required_sweeps':total_sweeps,
       'elapsed_seconds':time.monotonic()-start,'cache_error':err,
       'n_postburn_samples':len(measured_sweeps),
       'checkpoint_sha256':digest,'checkpoint':str(cp),'history':history,
       'physical_fit_admitted':False}
    (cp.parent/(cp.stem+'_progress.json')).write_text(json.dumps(result,indent=2))
    return result

if __name__=='__main__':
    ap=argparse.ArgumentParser()
    ap.add_argument('--kind',choices=['penrose','square'],default='penrose')
    ap.add_argument('--seed',type=int,default=101);ap.add_argument('--nt',type=int,default=20)
    ap.add_argument('--beta',type=float,default=3.5);ap.add_argument('--burn',type=int,default=1000)
    ap.add_argument('--total-sweeps',type=int,default=10000);ap.add_argument('--thin',type=int,default=10)
    ap.add_argument('--max-sweeps-this-run',type=int,default=2)
    ap.add_argument('--checkpoint-root',default='checkpoints')
    ap.add_argument('--initial-state',choices=('haar','cold'),default='haar')
    ap.add_argument('--measure',action='store_true',help='required when crossing scheduled production sample sweeps')
    args=ap.parse_args()
    cp=Path(args.checkpoint_root)/f'{args.kind}_nt{args.nt}_seed{args.seed}.npz'
    result=process(cp,args.kind,args.seed,args.nt,args.beta,args.total_sweeps,args.burn,args.thin,args.max_sweeps_this_run,measure=args.measure,initial_state=args.initial_state)
    print('checkpointed:',cp,'completed',result['completed_sweeps'],'required',result['required_sweeps'],'no physical fit',flush=True)
