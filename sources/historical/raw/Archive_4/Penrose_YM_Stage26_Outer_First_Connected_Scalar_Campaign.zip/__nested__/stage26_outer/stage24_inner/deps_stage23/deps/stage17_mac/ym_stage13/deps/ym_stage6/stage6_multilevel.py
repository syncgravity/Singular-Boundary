"""Stage 6: authentic conditional temporal-slab SU(2) Wilson sampling.

Given fixed spatial links at t % slab_width == 0, the Wilson action factorizes
into independent open temporal slabs. The conditionally averaged values of
spatial O(t) inside different slabs may therefore be multiplied to estimate
an unconnected two-point expectation (Rao-Blackwell estimator). Center/VEV
subtraction and outer-sample uncertainties remain necessary.

This is a *validation* experiment, not a proof that saved finite-ensemble
measurements determine glueball mass or string tension.
"""
from __future__ import annotations
import os,json,time,hashlib,argparse
from pathlib import Path
import numpy as np
from numba import njit
from wilson_torus import mul,face_trace_scalar
from stage5_square_production import setup,AREA,SEEDS
from stage4_smearing_flux import (ape_spatial,measure_scalar_groups,measure_winding,trace_spatial_path)

@njit
def condition_sweeps(links,fi,sg,beta,adj,degree,allowed,nsweeps,angle,seed):
    """Update ONLY non-frozen links using all their incident plaquettes.

    Returns fresh links, number accepted, max plaquette-cache residual. The
    arbitrary distribution of the frozen links is unchanged exactly.
    """
    np.random.seed(seed)
    u=links.copy()
    pf=np.empty(len(fi),dtype=np.float64)
    for f in range(len(fi)):pf[f]=face_trace_scalar(f,u,fi,sg)
    count=0
    cache=np.empty(adj.shape[1],dtype=np.float64)
    for _ in range(nsweeps):
        for i in range(len(allowed)):
            eid=allowed[i]
            axis=np.random.randn(3)
            axis/=np.sqrt(np.dot(axis,axis))
            theta=np.random.random()*angle
            dq=np.array([np.cos(theta),np.sin(theta)*axis[0],np.sin(theta)*axis[1],np.sin(theta)*axis[2]])
            trial=mul(dq,u[eid]);delta=0.
            for j in range(degree[eid]):
                f=adj[eid,j]
                cache[j]=face_trace_scalar(f,u,fi,sg,eid,trial)
                delta+=beta[f]*(cache[j]-pf[f])
            if np.log(np.random.random())<delta:
                u[eid]=trial
                count+=1
                for j in range(degree[eid]):pf[adj[eid,j]]=cache[j]
    err=0.
    for f in range(len(fi)):
        difference=abs(pf[f]-face_trace_scalar(f,u,fi,sg))
        if difference>err:err=difference
    return u,count,err

@njit
def update_sweeps_inplace(u,pf,fi,sg,beta,adj,degree,allowed,nsweeps,angle):
    """Advances ongoing conditional Markov trajectory in place; no reseeding."""
    count=0
    cache=np.empty(adj.shape[1],np.float64)
    for _ in range(nsweeps):
        for k in range(len(allowed)):
            eid=allowed[k]
            axis=np.random.randn(3)
            axis/=np.sqrt(np.dot(axis,axis))
            theta=np.random.random()*angle
            dq=np.array([np.cos(theta),np.sin(theta)*axis[0],np.sin(theta)*axis[1],np.sin(theta)*axis[2]])
            trial=mul(dq,u[eid]);delta=0.
            for j in range(degree[eid]):
                f=adj[eid,j]
                cache[j]=face_trace_scalar(f,u,fi,sg,eid,trial)
                delta+=beta[f]*(cache[j]-pf[f])
            if np.log(np.random.random())<delta:
                u[eid]=trial;count+=1
                for j in range(degree[eid]):pf[adj[eid,j]]=cache[j]
    return count

@njit
def plaquettes(links,fi,sg):
    pf=np.empty(len(fi),np.float64)
    for f in range(len(fi)):pf[f]=face_trace_scalar(f,links,fi,sg)
    return pf

def slab_partition(nt,E,V,width):
    if width<3 or nt%width:raise ValueError('slab width >=3 must divide nt')
    L=nt*(E+V)
    boundaries=list(range(0,nt,width))
    locked=np.zeros(L,np.bool_)
    for t in boundaries:locked[t*E:(t+1)*E]=True
    allowed=np.flatnonzero(~locked).astype(np.int64)
    assert len(allowed)==L-len(boundaries)*E
    # Every non-frozen link is assigned to exactly one slab, no plaquette
    # contains updatable links from distinct slabs.
    group=np.full(L,-1,np.int64)
    for t in range(nt):
        g=t//width
        if t not in boundaries:group[t*E:(t+1)*E]=g
        group[nt*E+t*V:nt*E+(t+1)*V]=g
    return locked,allowed,group,boundaries

def assert_slab_factorization(lat,group,locked,nt,E,V,width):
    for edges in lat['fi']:
        g={group[e] for e in edges if not locked[e]}
        if len(g)>1:raise AssertionError('a plaquette couples separate live slabs')
    return True

def local_observables(u,nt,E,staple,scalar,flux,levels=(2,)):
    # conditional operators at all time slices; spatial smearing does not
    # introduce dependence on neighboring time slices.
    out_s=[];out_f=[]
    for level in levels:
        v=u if level==0 else ape_spatial(u,nt,E,*staple,.4,level)
        out_s.append(measure_scalar_groups(v,nt,E,scalar['idx'],scalar['sign'],scalar['length'],scalar['kind']))
        out_f.append(measure_winding(v,nt,E,flux['idx'],flux['sign'],flux['length'],flux['direction']))
    return np.concatenate(out_s,axis=1),np.concatenate(out_f,axis=1)

@njit
def _selected_ape_measure(links,E,staple_ids,staple_signs,weights,nst,
                          scalar_ids,scalar_sign,scalar_len,scalar_kind,
                          flux_ids,flux_sign,flux_len,flux_dir,centers,alpha,levels):
    """APE only the four probed times; all other link/times remain unchanged."""
    cur=links.copy()
    for _ in range(levels):
        nxt=cur.copy()
        for z in range(len(centers)):
            t=centers[z]
            for e in range(E):
                acc=(1-alpha)*cur[t*E+e].copy()
                ws=0.
                for k in range(nst[e]):ws+=weights[e,k]
                for k in range(nst[e]):
                    q=np.array([1.,0.,0.,0.])
                    for j in range(3):
                        zz=cur[t*E+staple_ids[e,k,j]]
                        if staple_signs[e,k,j]==-1:
                            zz=np.array([zz[0],-zz[1],-zz[2],-zz[3]])
                        q=mul(q,zz)
                    acc+=alpha*(weights[e,k]/ws)*q
                norm=np.sqrt(np.dot(acc,acc))
                if norm<1e-13:raise ValueError('smearing projection singular')
                nxt[t*E+e]=acc/norm
        cur=nxt
    so=np.zeros((len(centers),3),np.float64);fo=np.zeros((len(centers),2),np.float64)
    cs=np.zeros(3,np.float64);cf=np.zeros(2,np.float64)
    for j in range(len(scalar_len)):cs[scalar_kind[j]]+=1
    for j in range(len(flux_len)):cf[flux_dir[j]]+=1
    for a in range(len(centers)):
        t=centers[a]
        for j in range(len(scalar_len)):
            v=trace_spatial_path(cur,len(centers),E,t,scalar_ids[j],scalar_sign[j],scalar_len[j])
            so[a,scalar_kind[j]]+=1.-v
        for j in range(len(flux_len)):
            v=trace_spatial_path(cur,len(centers),E,t,flux_ids[j],flux_sign[j],flux_len[j])
            fo[a,flux_dir[j]]+=v
        for j in range(3):so[a,j]/=cs[j]
        for j in range(2):fo[a,j]/=cf[j]
    return so,fo

def local_observables_selected(u,E,staple,scalar,flux,centers,level=2):
    return _selected_ape_measure(u,E,*staple,scalar['idx'],scalar['sign'],scalar['length'],scalar['kind'],
                    flux['idx'],flux['sign'],flux['length'],flux['direction'],
                    np.asarray(centers,dtype=np.int64),.4,int(level))

def conditioned_snapshot(outer,lat,sp,staple,scalar,flux,width=5,warm=8,inner=16,spacing=2,seed=123,levels=(2,)):
    """Use the *same frozen spatial boundaries* throughout an inner trajectory."""
    nt=lat['nt'];E=sp['E'];V=sp['V']
    locked,allowed,group,boundaries=slab_partition(nt,E,V,width)
    assert_slab_factorization(lat,group,locked,nt,E,V,width)
    original=outer[locked].copy()
    u=outer.copy()
    # Seed RNG once; every subsequent sweep advances a continuous chain.
    u,accepted,err=condition_sweeps(u,lat['fi'],lat['sg'],lat['beta'],lat['adj'],lat['degree'],
                                      allowed,warm,.95,int(seed))
    pf=plaquettes(u,lat['fi'],lat['sg'])
    centers=np.asarray([t+width//2 for t in range(0,nt,width)],np.int64)
    ss=[];ff=[]
    if len(levels)!=1:raise ValueError('targeted slab pilot requires one fixed smearing level')
    for k in range(inner):
        accepted+=update_sweeps_inplace(u,pf,lat['fi'],lat['sg'],lat['beta'],lat['adj'],lat['degree'],allowed,spacing,.95)
        s,f=local_observables_selected(u,E,staple,scalar,flux,centers,levels[0])
        ss.append(s);ff.append(f)
    if not np.array_equal(u[locked],original):raise AssertionError('frozen links changed')
    direct_s,direct_f=local_observables_selected(outer,E,staple,scalar,flux,centers,levels[0])
    err2=np.max(np.abs(plaquettes(u,lat['fi'],lat['sg'])-pf))
    if max(err,err2)>1e-9:raise AssertionError('plaquette cache mismatch')
    ss=np.asarray(ss);ff=np.asarray(ff)
    # use times 2,7,12,17 for separation 5; within distinct slabs.
    sc=ss.mean(axis=0)
    fc=ff.mean(axis=0)
    raw_s=np.mean(direct_s*np.roll(direct_s,-1,axis=0),axis=0)
    raw_f=np.mean(direct_f*np.roll(direct_f,-1,axis=0),axis=0)
    cond_s=np.mean(sc*np.roll(sc,-1,axis=0),axis=0)
    cond_f=np.mean(fc*np.roll(fc,-1,axis=0),axis=0)
    return {'direct_scalar_raw':raw_s,'conditional_scalar_raw':cond_s,
            'direct_flux_raw':raw_f,'conditional_flux_raw':cond_f,
            'direct_scalar_means':direct_s.mean(axis=0), 'conditional_scalar_means':ss.mean(axis=(0,1)),
            'direct_flux_means':direct_f.mean(axis=0),'conditional_flux_means':ff.mean(axis=(0,1)),
            'outer_locked_sha256':hashlib.sha256(original.tobytes()).hexdigest(),
            'conditional_cache_residual':float(max(err,err2)),
            'inner_acceptance':accepted/(len(allowed)*(warm+inner*spacing))}

def run(output,src,nouter=4,warm=8,inner=16,spacing=2,width=5,levels=(2,),seed=8022):
    output=Path(output);output.mkdir(parents=True,exist_ok=True)
    src=Path(src)
    meta=json.loads((src/'settings.json').read_text())
    if meta['nt']!=20 or meta['nx']!=13 or meta['ny']!=14:raise ValueError('Stage 5 20-slice square expected')
    sp,lat,cal,paths,flux,scalar,staple=setup(meta['nt'],meta['beta_ref'])
    if sp['graph_hash']!=meta['graph_hash']:raise AssertionError('spatial geometry hash mismatch')
    locked,allowed,group,boundaries=slab_partition(lat['nt'],sp['E'],sp['V'],width)
    assert_slab_factorization(lat,group,locked,lat['nt'],sp['E'],sp['V'],width)
    # One-time costly JIT compilation before timing production.
    results=[];t0=time.monotonic()
    for c,seed0 in enumerate(meta['seeds']):
        z=np.load(src/f'configs_seed{seed0}.npz');links=z['links'];actions=z['actions']
        if len(links)!=meta['n_saved_per_chain']:raise ValueError('incorrect archive')
        # Pick deliberately separated configurations, for a *pilot* only.
        locs=np.linspace(30,len(links)-30,nouter).round().astype(int)
        for i,ind in enumerate(locs):
            item=conditioned_snapshot(links[ind],lat,sp,staple,scalar,flux,
                    width,warm,inner,spacing,seed+c*1000+i,levels)
            item.update({'chain':int(seed0),'index':int(ind),'action':float(actions[ind])})
            results.append(item)
            print('Stage6 outer',len(results),'/',len(meta['seeds'])*nouter,'chain',seed0,'frame',ind,flush=True)
    np.savez_compressed(output/'conditional_observables.npz',
       **{key:np.stack([r[key] for r in results]) for key in ['direct_scalar_raw','conditional_scalar_raw',
          'direct_flux_raw','conditional_flux_raw','direct_scalar_means','conditional_scalar_means',
          'direct_flux_means','conditional_flux_means']},
       chain=np.array([r['chain'] for r in results]),index=np.array([r['index'] for r in results]))
    out={'status':'VALIDATION_ONLY','geometry':'13x14 square torus','nt':meta['nt'],'beta_ref':meta['beta_ref'],
       'chains':len(meta['seeds']),'outer_per_chain':nouter,'outer_count':len(results),
       'slab_width':width,'frozen_spatial_times':boundaries,
       'warmup_sweeps':warm,'inner_saved':inner,'inner_spacing_sweeps':spacing,
       'inner_proposals_per_outer':len(allowed)*(warm+inner*spacing),
       'n_scalar_ops':3*len(levels),'n_flux_ops':2*len(levels),'ape_levels':list(levels),
       'all_frozen_checks_pass':True,'all_cache_checks_pass':all(x['conditional_cache_residual']<1e-9 for x in results),
       'acceptance_mean':float(np.mean([x['inner_acceptance'] for x in results])),
       'runtime_seconds':time.monotonic()-t0,
       'scientific_gate':'FAIL: Stage5 outer ESS <400 for many monitored channels; inner conditional efficiency and 3+ time fit unverified',
       'physical_mass':None,'string_tension':None,'continuum_ratio':None,'penrose_production':False}
    (output/'stage6_validation.json').write_text(json.dumps(out,indent=2))
    return out

if __name__=='__main__':
    pa=argparse.ArgumentParser()
    pa.add_argument('--out',default='stage6_outputs');pa.add_argument('--source',default='/mnt/data/ym_stage5/outputs')
    pa.add_argument('--outer-per-chain',type=int,default=4)
    pa.add_argument('--warm',type=int,default=8);pa.add_argument('--inner',type=int,default=16)
    pa.add_argument('--spacing',type=int,default=2)
    args=pa.parse_args()
    print(json.dumps(run(args.out,args.source,args.outer_per_chain,args.warm,args.inner,args.spacing),indent=2))
