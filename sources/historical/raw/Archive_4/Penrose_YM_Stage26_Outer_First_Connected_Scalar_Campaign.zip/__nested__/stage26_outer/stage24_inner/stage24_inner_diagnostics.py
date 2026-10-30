#!/usr/bin/env python3
"""Independent conditional replicas at fixed full-size outer configurations.
No estimate of effective outer sample size is implied by inner replica counts.
"""
import argparse, hashlib, json, os, sys, time
from pathlib import Path
import numpy as np
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE/'deps_stage23'))
from stage23_outer_benchmark import frozen_snapshot, products_by_lag
from stage22_shifted import slab_masks, restricted_sweep, seed_rng, catalogue, measure, setup_geometry, get_plaquettes, sha, DEP
from stage7_checkpointed import sweep

def compute(kind,seed,checkpoint,output,cache,outer=1,stride=10,burns=(12,48),depths=(4,12),reps=2,thin=3,offsets=(0,)):
    burns=tuple(sorted(set(int(x) for x in burns)));depths=tuple(sorted(set(int(x) for x in depths)))
    offsets=tuple(sorted(set(int(x) for x in offsets)))
    if outer<1 or stride<1 or reps<2 or min(burns)<0 or min(depths)<1 or thin<1 or any(not 0<=q<5 for q in offsets):raise ValueError('invalid sampling parameters')
    graph,lat=setup_geometry(kind,20,3.5)
    catfile=Path(cache)/('penrose_complete_catalogue.npz' if kind=='penrose' else 'square_strict_catalogue.npz')
    cat,catsha=catalogue(kind,graph,catfile,None)
    with np.load(checkpoint,allow_pickle=False) as z:
        links=z['links'].copy();pf=z['plaquette_trace'].copy();rng=z['rng'].copy();start=int(z['sweeps'])
        if 'settings_json' in z:
            settings=json.loads(str(z['settings_json'].item()))
            if settings['kind']!=kind or settings['spatial_geometry_hash']!=graph['graph_hash']:raise ValueError('checkpoint geometry mismatch')
    if not np.allclose(get_plaquettes(links,lat['fi'],lat['sg']),pf,atol=1e-9,rtol=0):raise ValueError('initial plaquette mismatch')
    # Dimensions outer, offset, burn, replicate, depth, lag, channel, channel
    shape=(outer,len(offsets),len(burns),reps,len(depths))
    con=np.empty(shape+(9,4,4)); one=np.empty(shape+(20,4)); direct=np.empty((outer,20,4))
    directpair=np.empty((outer,len(offsets),9,4,4));pairs=np.empty((len(offsets),9),dtype=np.int64)
    seconds=np.empty(shape[:4]);errors=np.empty(shape[:4]); acceptance=np.empty(shape[:4])
    starts=time.monotonic()
    for i in range(outer):
        for _ in range(stride):sweep(links,pf,lat['fi'],lat['sg'],lat['beta'],lat['adj'],lat['degree'],rng,.95)
        direct[i],_=measure(links,graph,cat)
        for oi,offset in enumerate(offsets):
            bound,masks=slab_masks(lat,offset)
            for bi,burn in enumerate(burns):
                for rep in range(reps):
                    work=links.copy();wpf=pf.copy();frozen_links,frozen=frozen_snapshot(links,pf,lat,masks)
                    streams=[seed_rng(f'Stage24 {kind} {seed} {start+i*stride+stride} offset{offset} burn{burn} rep{rep} slab{j}') for j in range(4)]
                    samples=np.empty((max(depths),20,4));accepts=[]; t0=time.monotonic()
                    for step in range(burn+max(depths)*thin):
                        for j,mask in enumerate(masks):
                            a,n=restricted_sweep(work,wpf,lat['fi'],lat['sg'],lat['beta'],lat['adj'],lat['degree'],streams[j],.95,mask)
                            accepts.append(a/n)
                        if step>=burn and (step-burn+1)%thin==0:
                            samples[(step-burn+1)//thin-1],_=measure(work,graph,cat)
                    if not np.array_equal(work[frozen],frozen_links):raise ValueError('boundary altered')
                    err=float(np.max(np.abs(get_plaquettes(work,lat['fi'],lat['sg'])-wpf)))
                    if err>1e-9:raise ValueError(f'plaquette mismatch {err}')
                    seconds[i,oi,bi,rep]=time.monotonic()-t0; errors[i,oi,bi,rep]=err;acceptance[i,oi,bi,rep]=np.mean(accepts)
                    for ki,k in enumerate(depths):
                        means=samples[:k].mean(axis=0)
                        one[i,oi,bi,rep,ki]=means
                        prod,dp,count=products_by_lag(direct[i],means,offset)
                        con[i,oi,bi,rep,ki]=prod
                        directpair[i,oi]=dp
                        pairs[oi]=count
                    print(f'{kind} seed{seed} outer={i+1}/{outer} offset={offset} burn={burn} replica={rep+1}/{reps} sec={seconds[i,oi,bi,rep]:.1f}',flush=True)
    out=Path(output);out.mkdir(parents=True,exist_ok=True)
    path=out/f'{kind}_seed{seed}_stage24_from{start}_outer{outer}.npz'
    temp=path.with_suffix('.tmp.npz')
    np.savez_compressed(temp,onepoint=one,conditional=con,direct_timeslice=direct,direct_product=directpair,
        pair_counts=pairs,seconds=seconds,acceptance=acceptance,cache_error=errors,
        sweeps=start+stride*np.arange(1,outer+1),offsets=np.asarray(offsets),burns=np.asarray(burns),depths=np.asarray(depths),
        inner_thin=np.int64(thin),catalogue_sha256=np.array(catsha),source_sha256=np.array(sha(checkpoint)),
        scientific_gate=np.array('PENDING: no physical signal or unbiasedness admission from this diagnostic'))
    os.replace(temp,path)
    result=dict(kind=kind,seed=seed,outer=outer,offsets=offsets,burns=burns,depths=depths,reps=reps,
        source_sha256=sha(checkpoint),catalogue_sha256=catsha,output_sha256=sha(path),output=path.name,
        seconds=float(time.monotonic()-starts),max_cache_error=float(errors.max()))
    path.with_suffix('.json').write_text(json.dumps(result,indent=2))
    return result

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--kind',choices=['square','penrose'],required=True);p.add_argument('--seed',type=int,required=True)
    p.add_argument('--checkpoint',required=True);p.add_argument('--output',default='stage24_results')
    p.add_argument('--cache',default=str(DEP/'stage19_complete_catalogues'))
    p.add_argument('--outer',type=int,default=1);p.add_argument('--stride',type=int,default=10)
    p.add_argument('--burns',type=int,nargs='+',default=[12,48]);p.add_argument('--depths',type=int,nargs='+',default=[4,12]);p.add_argument('--reps',type=int,default=2)
    p.add_argument('--thin',type=int,default=3);p.add_argument('--offsets',type=int,nargs='+',default=[0])
    a=p.parse_args();print(json.dumps(compute(a.kind,a.seed,a.checkpoint,a.output,a.cache,a.outer,a.stride,a.burns,a.depths,a.reps,a.thin,a.offsets),indent=2))
if __name__=='__main__':main()
