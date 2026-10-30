#!/usr/bin/env python3
"""Full-lattice Stage 23 pilot: independent OUTER configs, conditional slab benchmark.

Controls: same outer field direct O(t)O(s) and slab product of inner means.
For each outer field and offset the slab chains are started at the outer state;
inner burn must be converged for an unbiased conditional expectation.
No mass or variance-reduction claim from one or a few outer states.
"""
import argparse, hashlib, json, os, sys, time
from pathlib import Path
import numpy as np
from stage22_shifted import slab_masks, shifted_pairs, restricted_sweep, seed_rng, catalogue, measure, setup_geometry, get_plaquettes, sha
from stage22_shifted import DEP
from stage7_checkpointed import sweep

def frozen_snapshot(links, pf, lat, mask_list):
    frozen=np.ones(len(links),dtype=bool)
    for m in mask_list: frozen[m]=False
    return links[frozen].copy(), frozen

def products_by_lag(direct, slabmeans, offset):
    bound,_=slab_masks({'nt':20,'E':1,'V':1,'L':40},offset) if False else ([(offset+5*k)%20 for k in range(4)],None)
    pairs=shifted_pairs(20,bound)
    result=np.zeros((9,4,4)); ctrl=np.zeros_like(result); counts=np.zeros(9,dtype=np.int64)
    for lag,t,s in pairs:
        k=int(lag-2)
        result[k]+=np.outer(slabmeans[t],slabmeans[s]);ctrl[k]+=np.outer(direct[t],direct[s]);counts[k]+=1
    if np.any(counts==0): raise AssertionError('some temporal separations lack cross-slab pairs')
    return result/counts[:,None,None],ctrl/counts[:,None,None],counts

def run(kind,seed,checkpoint,output,cache,outer_n=2,outer_stride=10,inner_depths=(4,12),burn=12,thin=3,offsets=(0,),verify=True):
    if outer_n<1 or outer_stride<1 or burn<0 or thin<1 or min(inner_depths)<1: raise ValueError('Invalid sampling configuration')
    if len(set(inner_depths))!=len(inner_depths):raise ValueError('duplicate depths')
    depths=tuple(sorted(inner_depths)); K=max(depths)
    g,lat=setup_geometry(kind,20,3.5)
    catpath=Path(cache)/('penrose_complete_catalogue.npz' if kind=='penrose' else 'square_strict_catalogue.npz')
    cat,catsha=catalogue(kind,g,catpath,None)
    with np.load(checkpoint,allow_pickle=False) as z:
        links=z['links'].copy(); pf=z['plaquette_trace'].copy(); rng=z['rng'].copy(); start=int(z['sweeps'])
        conf=json.loads(str(z['settings_json'].item())) if 'settings_json' in z.files else {}
    if conf and (conf['kind']!=kind or conf['spatial_geometry_hash']!=g['graph_hash']):raise ValueError('Incompatible geometry')
    if not np.allclose(get_plaquettes(links,lat['fi'],lat['sg']),pf,atol=1e-9,rtol=0):raise ValueError('Invalid starting plaquette cache')
    pairs=[];directs=[];conditionals=[];counts_all=[];accepts=[];elapsed=[];checkerr=[];sweeps=[]
    tic=time.monotonic()
    for outer_i in range(outer_n):
        for _ in range(outer_stride):sweep(links,pf,lat['fi'],lat['sg'],lat['beta'],lat['adj'],lat['degree'],rng,.95)
        sweepn=start+(outer_i+1)*outer_stride
        o,aux=measure(links,g,cat)
        for offset in offsets:
            bound,masks=slab_masks(lat,int(offset))
            work=links.copy();work_pf=pf.copy()
            initial,frozen=frozen_snapshot(links,pf,lat,masks)
            streams=[seed_rng(f'Stage23 outer {kind} {seed} {sweepn} {offset} slab {j}') for j in range(4)]
            samples=np.empty((K,20,4)); aa=[]
            ss=time.monotonic()
            for step in range(burn+K*thin):
                for j,active in enumerate(masks):
                    accept,n=restricted_sweep(work,work_pf,lat['fi'],lat['sg'],lat['beta'],lat['adj'],lat['degree'],streams[j],.95,active)
                    aa.append(accept/n)
                if step>=burn and (step-burn+1)%thin==0:
                    samples[(step-burn+1)//thin-1],_=measure(work,g,cat)
            if not np.array_equal(work[frozen],initial):raise AssertionError('Frozen boundary changed')
            error=float(np.max(np.abs(get_plaquettes(work,lat['fi'],lat['sg'])-work_pf))) if verify else np.nan
            if verify and error>1e-9:raise ValueError(f'bad plaquette cache {error}')
            con=[]; dr=[];ct=[]
            for k in depths:
                cm, dm,c=products_by_lag(o,samples[:k].mean(axis=0),int(offset))
                con.append(cm);dr.append(dm);ct.append(c)
            pairs.append([sweepn,offset]);directs.append(dr);conditionals.append(con);counts_all.append(ct)
            accepts.append(float(np.mean(aa)));elapsed.append(time.monotonic()-ss);checkerr.append(error)
            print(f'{kind} seed{seed} outer_sweep={sweepn} offset={offset} K={K} sec={elapsed[-1]:.1f}',flush=True)
    out=Path(output);out.mkdir(parents=True,exist_ok=True)
    target=out/f'{kind}_seed{seed}_outer{start}_{start+outer_n*outer_stride}_stage23.npz'
    tmp=target.with_suffix('.tmp.npz')
    np.savez_compressed(tmp, keys=np.array(pairs,dtype=np.int64), depths=np.array(depths),
        direct=np.array(directs), conditional=np.array(conditionals),pair_counts=np.array(counts_all),
        acceptance=np.array(accepts),inner_seconds=np.array(elapsed),cache_error=np.array(checkerr),
        catalogue_sha256=np.array(catsha),input_sha256=np.array(sha(checkpoint)),
        inner_burn=np.int64(burn),inner_thin=np.int64(thin),outer_stride=np.int64(outer_stride))
    os.replace(tmp,target)
    meta={'geometry':kind,'seed':seed,'outer_configurations':outer_n,'offsets':list(offsets),'depths':list(depths),
      'final_sweep':start+outer_n*outer_stride,'catalogue_sha256':catsha,
      'output_sha256':sha(target),'elapsed_seconds':time.monotonic()-tic,
      'scientific_gate':'PENDING: inner burn-in, outer autocorrelation, paired unbiasedness, cost-adjusted efficiency'}
    (out/(target.stem+'.json')).write_text(json.dumps(meta,indent=2));return meta

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--kind',choices=['square','penrose'],required=True);p.add_argument('--seed',type=int,required=True)
    p.add_argument('--checkpoint',required=True);p.add_argument('--output',default='stage23_results')
    p.add_argument('--cache',default=str(DEP/'stage19_complete_catalogues'))
    p.add_argument('--outer',type=int,default=2);p.add_argument('--stride',type=int,default=10)
    p.add_argument('--depths',type=int,nargs='+',default=[4,12]);p.add_argument('--burn',type=int,default=12)
    p.add_argument('--thin',type=int,default=3);p.add_argument('--offsets',type=int,nargs='+',default=[0])
    a=p.parse_args();print(json.dumps(run(a.kind,a.seed,a.checkpoint,a.output,a.cache,a.outer,a.stride,a.depths,a.burn,a.thin,a.offsets),indent=2))
if __name__=='__main__':main()
