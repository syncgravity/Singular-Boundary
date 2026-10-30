#!/usr/bin/env python3
"""Full-size conditional temporal-slab SU(2) scalar benchmark; no mass inference.

Boundary spatial links at t=0,5,10,15 are frozen. The interiors of four
non-overlapping temporal slabs are conditionally independent GIVEN these links.
For t=2 and t=7, E[O2 O7|B]=E[O2|B]E[O7|B], assuming equilibrium outer fields.
Inner measurements form one estimator per OUTER configuration, never K samples.
"""
import argparse,hashlib,json,os,sys,time
from pathlib import Path
import numpy as np
from numba import njit
HERE=Path(__file__).resolve().parent
sys.path[:0]=[str(HERE),str(HERE/'stage18'),str(HERE/'stage18'/'stage17_mac'),str(HERE/'stage18'/'stage17_mac'/'ym_stage13'/'deps'/'ym_stage7'),str(HERE/'stage18'/'stage17_mac'/'ym_stage13'/'deps'/'ym_stage6'/'source_stage5'),str(HERE/'stage19')]
from stage7_checkpointed import sweep, get_plaquettes,setup_geometry,rand
from stage19_mc import catalogue, measure,sha
from wilson_torus import mul,face_trace_scalar

@njit
def restricted_sweep(links,pf,fi,sg,beta,adj,degree,st,angle,active):
    """Identical exact local Metropolis acceptance to Stage 9, with frozen links.
    Returns (accepted, proposed). Uses an independent RNG stream from outer MCMC.
    """
    accepted=0;proposal=0
    proposed=np.empty(adj.shape[1],np.float64)
    for eid in range(len(links)):
        if not active[eid]:continue
        proposal+=1
        z=2*rand(st)-1;phase=2*np.pi*rand(st)
        r=np.sqrt(max(0.,1-z*z));theta=rand(st)*angle;ss=np.sin(theta)
        dq=np.array([np.cos(theta),ss*r*np.cos(phase),ss*r*np.sin(phase),ss*z])
        trial=mul(dq,links[eid]);delta=0.
        for k in range(degree[eid]):
            p=adj[eid,k];proposed[k]=face_trace_scalar(p,links,fi,sg,eid,trial)
            delta+=beta[p]*(proposed[k]-pf[p])
        if np.log(max(1e-300,rand(st)))<delta:
            links[eid]=trial;accepted+=1
            for k in range(degree[eid]):pf[adj[eid,k]]=proposed[k]
    return accepted,proposal

def boundary_mask(lat,boundaries=(0,5,10,15)):
    """Link layout: spatial (nt,E), then temporal (nt,V)."""
    nt,E,V=int(lat['nt']),int(lat['E']),int(lat['V'])
    assert nt==20 and set(boundaries)=={0,5,10,15}
    mask=np.ones(int(lat['L']),np.bool_)
    for t in boundaries:mask[t*E:(t+1)*E]=False
    assert mask.sum()==lat['L']-len(boundaries)*E
    return mask

def conditional_pair(x, y, slabs=((2,7),(2,12),(2,17),(7,12),(7,17),(12,17))):
    """x: (K,20,4) inner measurements; returns pair-products (6,4,4)."""
    return np.stack([x[:,t,:].mean(axis=0)[:,None]*x[:,s,:].mean(axis=0)[None,:]
                     for t,s in slabs])

def seed_rng(label):
    h=hashlib.sha256(label.encode()).digest();st=np.frombuffer(h[:16],dtype='<u8').copy()
    if not np.any(st):st[0]=1
    return st

def run(kind,seed,checkpoint,cache,output,K=4,skip=1,angle=.95,verify=True):
    start=time.monotonic();g,lat=setup_geometry(kind,20,3.5)
    catname='penrose_complete_catalogue.npz' if kind=='penrose' else 'square_strict_catalogue.npz'
    cat,catsha=catalogue(kind,g,Path(cache)/catname,None)
    with np.load(checkpoint,allow_pickle=False) as z:
        outer=z['links'].copy();pf0=z['plaquette_trace'].copy();sweepn=int(z['sweeps'])
        if 'settings_json' in z.files:
            settings=json.loads(str(z['settings_json'].item()))
            if settings['kind']!=kind or settings['spatial_geometry_hash']!=g['graph_hash']:
                raise ValueError('incompatible checkpoint geometry')
    assert len(outer)==lat['L']
    if not np.allclose(get_plaquettes(outer,lat['fi'],lat['sg']),pf0,atol=1e-9,rtol=0):raise ValueError('initial plaquette cache mismatch')
    active=boundary_mask(lat)
    base,aux=measure(outer,g,cat)
    links=outer.copy();pf=pf0.copy();rng=seed_rng(f'Stage21 {kind} {seed} sweep{sweepn} inner')
    inner=[];accept=[]
    for j in range(K):
        for _ in range(skip):
            a,n=restricted_sweep(links,pf,lat['fi'],lat['sg'],lat['beta'],lat['adj'],lat['degree'],rng,angle,active)
            accept.append(a/n)
        measured,_=measure(links,g,cat)
        inner.append(measured)
    inner=np.asarray(inner)
    E=int(lat['E']); boundaries=(0,5,10,15)
    for t in boundaries:
        if not np.array_equal(outer[t*E:(t+1)*E],links[t*E:(t+1)*E]):raise ValueError('frozen boundary changed')
    err=float(np.max(np.abs(get_plaquettes(links,lat['fi'],lat['sg'])-pf))) if verify else None
    if err is not None and err>1e-9:raise ValueError('inner plaquette cache mismatch')
    pairs=((2,7),(2,12),(2,17),(7,12),(7,17),(12,17))
    direct=np.stack([base[t,:,None]*base[s,None,:] for t,s in pairs])
    improved=conditional_pair(inner,inner,pairs)
    output=Path(output);output.mkdir(parents=True,exist_ok=True)
    dest=output/f'{kind}_seed{seed}_outer{sweepn}_K{K}_scalar_slab.npz'
    # Do NOT store raw full links or modify source checkpoint
    with open(dest,'wb') as f:
        np.savez_compressed(f, direct=direct,conditional=improved,outer_operator=base,
            conditional_means=inner.mean(axis=0),inner_samples=inner,
            pair_times=np.array(pairs),boundary_times=np.array(boundaries),
            n_outer=np.int64(1),n_inner=np.int64(K),sweep=np.int64(sweepn),
            catalogue_sha256=np.array(catsha),input_sha256=np.array(sha(checkpoint)))
    rep={'geometry':kind,'seed':seed,'source_sweep':sweepn,'n_outer':1,'n_inner':K,
         'inner_skip_sweeps':skip,'K_inner_not_independent_outer':True,
         'frozen_boundaries':list(boundaries),'active_links':int(active.sum()),
         'cache_error':err,'acceptance_mean':float(np.mean(accept)),
         'elapsed_seconds':time.monotonic()-start,'catalogue_sha256':catsha,
         'outcome':'Estimator engineering snapshot only; no variance reduction or mass claim',
         'file':str(dest)}
    (output/(dest.stem+'.json')).write_text(json.dumps(rep,indent=2))
    print(json.dumps(rep,indent=2),flush=True)
    return rep

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--kind',choices=['square','penrose'],required=True)
    p.add_argument('--seed',type=int,default=101)
    p.add_argument('--checkpoint',required=True)
    p.add_argument('--cache',default='stage19_complete_catalogues')
    p.add_argument('--output',default='stage21_smoke')
    p.add_argument('--inner',type=int,default=4)
    p.add_argument('--inner-sweeps',type=int,default=1)
    a=p.parse_args()
    if a.inner<1 or a.inner_sweeps<1:raise ValueError('positive inner and inner-sweeps required')
    run(a.kind,a.seed,a.checkpoint,a.cache,a.output,a.inner,a.inner_sweeps)
if __name__=='__main__':main()
