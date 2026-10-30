#!/usr/bin/env python3
"""Stage 26 outer-first, restartable, full-lattice scalar multilevel measurement.
Measurement is not a certified mass extraction; independent OUTER fields count as samples.
"""
import argparse, hashlib, json, os, sys, time
from pathlib import Path
import numpy as np
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'stage24_inner'))
from stage24_inner_diagnostics import frozen_snapshot, products_by_lag
from stage22_shifted import slab_masks, restricted_sweep, seed_rng, catalogue, measure, setup_geometry, get_plaquettes, sha
from stage7_checkpointed import sweep

def atomic_npz(path, **a):
    path=Path(path);path.parent.mkdir(parents=True,exist_ok=True)
    tmp=path.with_name(path.name+'.tmp.npz');np.savez_compressed(tmp,**a);os.replace(tmp,path)
def atomic_json(path, o):
    path=Path(path);tmp=path.with_name(path.name+'.tmp');tmp.write_text(json.dumps(o,indent=2));os.replace(tmp,path)
def config(a):
    return {'kind':a.kind,'seed':a.seed,'stride':a.stride,'burn':a.burn,'depth':a.depth,'thin':a.thin,'reps':a.reps,'offset_policy':'cyclic 0..4','beta_ref':3.5,'nt':20}
def run(a):
    if a.target_sweeps<10000 or a.stride<1 or a.burn<0 or a.depth<1 or a.thin<1 or a.reps<1:raise ValueError('invalid controls')
    g,lat=setup_geometry(a.kind,20,3.5)
    catpath=Path(a.cache)/('penrose_complete_catalogue.npz' if a.kind=='penrose' else 'square_strict_catalogue.npz')
    cat,catsha=catalogue(a.kind,g,catpath,None)
    directory=Path(a.output)/f'{a.kind}_seed{a.seed}'; directory.mkdir(parents=True,exist_ok=True)
    restart=directory/'restart.npz';cfg=config(a)
    if restart.exists():
        with np.load(restart,allow_pickle=False) as z:
            links=z['links'].copy();pf=z['plaquette_trace'].copy();rng=z['rng'].copy();n=int(z['sweeps']);base=int(z['initial_sweep']);saved_cfg=json.loads(str(z['configuration'].item()));sourcehash=str(z['source_sha256'].item())
        if saved_cfg!=cfg:raise ValueError('restart settings differ; use a new output directory')
    else:
        with np.load(a.checkpoint,allow_pickle=False) as z:
            links=z['links'].copy();pf=z['plaquette_trace'].copy();rng=z['rng'].copy();n=int(z['sweeps']);base=n
            if 'settings_json' in z:
                settings=json.loads(str(z['settings_json'].item()))
                if settings['kind']!=a.kind or settings['spatial_geometry_hash']!=g['graph_hash']:raise ValueError('mismatched input geometry')
        sourcehash=sha(a.checkpoint)
    if (n-base)%a.stride:raise ValueError('non-aligned restart')
    if np.max(np.abs(get_plaquettes(links,lat['fi'],lat['sg'])-pf))>1e-9:raise ValueError('initial plaquette cache invalid')
    tic=time.monotonic();made=0
    while n+a.stride<=a.target_sweeps:
        for _ in range(a.stride):sweep(links,pf,lat['fi'],lat['sg'],lat['beta'],lat['adj'],lat['degree'],rng,.95)
        n+=a.stride;outer_index=(n-base)//a.stride-1; offset=int(outer_index%5)
        direct,_=measure(links,g,cat)
        bound,masks=slab_masks(lat,offset)
        fp,frozen=frozen_snapshot(links,pf,lat,masks)
        con=np.empty((a.reps,9,4,4));ones=np.empty((a.reps,20,4));times=np.empty(a.reps);errors=np.empty(a.reps)
        for rep in range(a.reps):
            work=links.copy();wp=pf.copy()
            rngs=[seed_rng(f'Stage26 {a.kind} seed{a.seed} sweep{n} offset{offset} replica{rep} slab{j}') for j in range(4)]
            obs=np.zeros((20,4));t0=time.monotonic()
            nstep=a.burn+a.depth*a.thin
            for step in range(nstep):
                for j,m in enumerate(masks): restricted_sweep(work,wp,lat['fi'],lat['sg'],lat['beta'],lat['adj'],lat['degree'],rngs[j],.95,m)
                if step>=a.burn and (step-a.burn+1)%a.thin==0:
                    x,_=measure(work,g,cat);obs+=x/a.depth
            if not np.array_equal(work[frozen],fp):raise ValueError('boundary changed')
            err=float(np.max(np.abs(get_plaquettes(work,lat['fi'],lat['sg'])-wp)))
            if err>1e-9:raise ValueError(f'cache error {err}')
            cp,dp,pc=products_by_lag(direct,obs,offset)
            con[rep]=cp;ones[rep]=obs;times[rep]=time.monotonic()-t0;errors[rep]=err
        record=directory/f'outer_{n:08d}.npz'
        atomic_npz(record,sweep=np.int64(n),chain_seed=np.int64(a.seed),offset=np.int64(offset),
            direct_timeslice=direct,direct_product=dp,conditional=con,conditional_onepoint=ones,
            pair_counts=pc,inner_seconds=times,cache_error=errors,inner_burn=np.int64(a.burn),
            inner_depth=np.int64(a.depth),inner_thin=np.int64(a.thin),catalogue_sha256=np.array(catsha),source_sha256=np.array(sourcehash))
        # Record is committed first; deterministic replay overwrites it if process stops before checkpoint.
        atomic_npz(restart,links=links,plaquette_trace=pf,rng=rng,sweeps=np.int64(n),initial_sweep=np.int64(base),configuration=np.array(json.dumps(cfg,sort_keys=True)),source_sha256=np.array(sourcehash))
        atomic_json(directory/'latest.json',dict(**cfg,sweep=n,initial_sweep=base,observations=(n-base)//a.stride,offset=offset,record=record.name,record_sha256=sha(record),catalogue_sha256=catsha,source_sha256=sourcehash,elapsed_seconds=time.monotonic()-tic))
        made+=1;print(f'{a.kind} seed{a.seed} sweep={n} offset={offset} replicas={a.reps} inner_sec={times.sum():.1f}',flush=True)
        if a.max_outer and made>=a.max_outer:break
    print(json.dumps({'kind':a.kind,'seed':a.seed,'sweep':n,'new_outer_records':made,'output':str(directory)},indent=2))

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--kind',required=True,choices=['square','penrose']);p.add_argument('--seed',type=int,required=True)
    p.add_argument('--checkpoint',required=True);p.add_argument('--cache',default='stage24_inner/deps_stage23/deps/stage19_complete');p.add_argument('--output',default='stage26_results')
    p.add_argument('--target-sweeps',type=int,default=11000);p.add_argument('--stride',type=int,default=20)
    p.add_argument('--burn',type=int,default=96);p.add_argument('--depth',type=int,default=32);p.add_argument('--thin',type=int,default=3);p.add_argument('--reps',type=int,default=2);p.add_argument('--max-outer',type=int,default=0)
    run(p.parse_args())
if __name__=='__main__':main()
