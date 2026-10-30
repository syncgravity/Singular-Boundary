#!/usr/bin/env python3
"""Full-lattice shifted-slab scalar measurement engineering benchmark.

Inner sweeps are independent by slab, conditional on frozen spatial boundary
links. These are finite-MCMC estimates; equality with exact conditional means
requires inner equilibration and autocorrelation control. Never count inner
samples as independent outer gauge configurations.
"""
import argparse, hashlib, json, sys, time
from pathlib import Path
import numpy as np
HERE=Path(__file__).resolve().parent
DEP=HERE/'deps'/'stage19_complete'
sys.path.insert(0,str(DEP))
from stage21_scalar_multilevel import restricted_sweep,seed_rng
from stage19_mc import catalogue,measure,sha
from stage7_checkpointed import setup_geometry,get_plaquettes

def slab_masks(lat, offset=0, width=5):
    nt,E,V=int(lat['nt']),int(lat['E']),int(lat['V'])
    if nt%width or not 0<=offset<width: raise ValueError('Invalid slab width or offset')
    bound={(offset+j*width)%nt for j in range(nt//width)}
    masks=[]
    for start in sorted(bound):
        mask=np.zeros(int(lat['L']),dtype=np.bool_)
        for j in range(width):
            t=(start+j)%nt
            mask[nt*E+t*V:nt*E+(t+1)*V]=True # temporal edges belong to exactly one slab
            if j:
                mask[t*E:(t+1)*E]=True # non-boundary spatial edges
        masks.append(mask)
    union=np.zeros(int(lat['L']),dtype=np.int8)
    for mask in masks: union+=mask.astype(np.int8)
    assert np.max(union)==1
    assert sum(np.count_nonzero(m) for m in masks)==lat['L']-len(bound)*E
    return sorted(bound),masks

def shifted_pairs(nt, boundaries, min_lag=2,max_lag=10):
    # For a nonzero offset, sorted boundaries[0] is NOT the cyclic slab origin.
    # Determine slab by walking forward from the preceding boundary mod nt.
    boundary_set=set(int(x) for x in boundaries)
    def membership(t):
        for d in range(nt):
            u=(int(t)-d)%nt
            if u in boundary_set:
                return u
        raise AssertionError("No preceding slab boundary")
    pairs=[]
    for lag in range(min_lag,max_lag+1):
        for t in range(nt):
            s=(t+lag)%nt
            if t in boundaries or s in boundaries:continue
            if membership(t)!=membership(s):pairs.append((lag,t,s))
    return np.asarray(pairs,dtype=np.int64).reshape(-1,3)

def run(kind,seed,checkpoint,cache,output,K=4,burn=2,thin=2,offsets=(0,1,2,3,4),verify=True):
    start=time.monotonic();g,lat=setup_geometry(kind,20,3.5)
    catfile=Path(cache)/('penrose_complete_catalogue.npz' if kind=='penrose' else 'square_strict_catalogue.npz')
    cat,catsha=catalogue(kind,g,catfile,None)
    with np.load(checkpoint,allow_pickle=False) as z:
        original=z['links'].copy();pf=z['plaquette_trace'].copy();sweep=int(z['sweeps'])
        if 'settings_json' in z:
            settings=json.loads(str(z['settings_json'].item()))
            assert settings['kind']==kind and settings['spatial_geometry_hash']==g['graph_hash']
    if not np.allclose(get_plaquettes(original,lat['fi'],lat['sg']),pf,atol=1e-9,rtol=0):raise ValueError('Initial cache')
    direct,_=measure(original,g,cat)
    records=[];statistics=[]
    for offset in offsets:
        bound,masks=slab_masks(lat,int(offset)); rng=[seed_rng(f'Stage22 {kind} {seed} {sweep} {offset} {i}') for i in range(len(masks))]
        links=original.copy(); cachepf=pf.copy()
        samples=np.zeros((K,20,4),dtype=np.float64)
        acc=[]
        for step in range(burn+K*thin):
            for i,m in enumerate(masks):
                accepted,n=restricted_sweep(links,cachepf,lat['fi'],lat['sg'],lat['beta'],lat['adj'],lat['degree'],rng[i],.95,m)
                acc.append(accepted/n)
            if step>=burn and (step-burn+1)%thin==0:
                j=(step-burn+1)//thin-1
                samples[j],_=measure(links,g,cat)
        frozen=np.ones(len(original),dtype=bool)
        for mask in masks:frozen[mask]=False
        if not np.array_equal(links[frozen],original[frozen]):raise AssertionError('Frozen links modified')
        err=float(np.max(np.abs(get_plaquettes(links,lat['fi'],lat['sg'])-cachepf))) if verify else None
        if err is not None and err>1e-9:raise AssertionError('Plaquette cache mismatch')
        pairs=shifted_pairs(20,bound)
        for lag,t,s in pairs:
            # Different slab processes have independent RNG streams;
            # conditional-product estimate is still subject to finite MCMC burn/mixing.
            conditional=np.outer(samples[:,t,:].mean(axis=0),samples[:,s,:].mean(axis=0))
            direct_product=np.outer(direct[t],direct[s])
            records.append((int(offset),int(lag),int(t),int(s),conditional,direct_product))
        statistics.append({'offset':int(offset),'boundaries':bound,'pair_count':len(pairs),'acceptance':float(np.mean(acc)),'plaquette_cache_error':err,'elapsed':time.monotonic()-start})
    out=Path(output);out.mkdir(parents=True,exist_ok=True)
    path=out/f'{kind}_seed{seed}_outer{sweep}_shifted_K{K}.npz'
    np.savez_compressed(path,offset=np.array([r[0] for r in records]),lag=np.array([r[1] for r in records]),t=np.array([r[2] for r in records]),s=np.array([r[3] for r in records]),conditional=np.stack([r[4] for r in records]),direct=np.stack([r[5] for r in records]),outer_operators=direct,catalogue_sha=np.array(catsha),source_sha=np.array(sha(checkpoint)),K=np.int64(K),burn=np.int64(burn),thin=np.int64(thin))
    meta={'geometry':kind,'seed':seed,'source_sweep':sweep,'n_outer':1,'n_inner':K,'disclaimer':'One outer field: engineering only, no unbiasedness or variance claims','statistics':statistics,'output':str(path)}
    (out/(path.stem+'.json')).write_text(json.dumps(meta,indent=2));print(json.dumps(meta,indent=2));return meta

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--kind',choices=['square','penrose'],required=True);p.add_argument('--seed',type=int,default=101)
    p.add_argument('--checkpoint',required=True);p.add_argument('--cache',default=str(DEP/'stage19_complete_catalogues'));p.add_argument('--output',default='stage22_results');p.add_argument('--inner',type=int,default=4);p.add_argument('--burn',type=int,default=2);p.add_argument('--thin',type=int,default=2);p.add_argument('--offsets',type=int,nargs='+',default=[0,1,2,3,4]);a=p.parse_args()
    if a.inner<1 or a.burn<0 or a.thin<1:raise ValueError('Invalid inner parameters')
    run(a.kind,a.seed,a.checkpoint,a.cache,a.output,a.inner,a.burn,a.thin,a.offsets)
