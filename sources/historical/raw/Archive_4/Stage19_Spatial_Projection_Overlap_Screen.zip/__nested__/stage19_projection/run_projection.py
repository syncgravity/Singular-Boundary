#!/usr/bin/env python3
"""Stage19 deterministic spatial projection convergence and same-field overlap screen.
Measurements are spatial averages of closed cluster traces, not glueball correlators.
"""
import argparse, sys, json, time
from pathlib import Path
import numpy as np
ROOT=Path(__file__).resolve().parent
PILOT=ROOT.parent/'stage19_operator_pilot'
sys.path.insert(0,str(PILOT))
from stage19_pilot import catalogue, measurement, gauge_test
from stage7_checkpointed import setup_geometry

def rank_stats(X):
    X=np.asarray(X,float); X=X-X.mean(axis=0)
    v=np.linalg.svd(X,compute_uv=False)
    return {'singular_values':v.tolist(), 'effective_rank':float(np.exp(-(p:=v*v/(np.sum(v*v)+1e-300))@np.log(p+1e-300)))}

def main(args):
    out=Path(args.output);out.mkdir(parents=True,exist_ok=True)
    reports=[]
    for kind in args.kinds:
        start=time.monotonic()
        sp,lat=setup_geometry(kind,20,3.5)
        c=catalogue(sp,per_size=args.loops,seed=args.seed)
        # spatial centering by all sampled source cluster locations (a controlled proxy)
        # no false assertion of full exact zero momentum: the sampled clusters are not a translation orbit.
        kinds=c['kind']; ar=c['areas']; lengths=c['length']
        stats={}
        for i,n in enumerate(c['sizes']):
            x=ar[kinds==i]; l=lengths[kinds==i]
            stats[str(n)]={'n':len(x),'area_min':float(x.min()),'area_median':float(np.median(x)),
                           'area_max':float(x.max()),'area_cv':float(x.std()/x.mean()),
                           'boundary_length_min':int(l.min()),'boundary_length_max':int(l.max())}
        observations=[]
        for seed in args.seeds:
            src=Path(args.inputs)/f'{kind}_nt20_seed{seed}.npz'
            with np.load(src,allow_pickle=False) as f: links=f['links']
            # repeat groups at 96, 192, 384, ... for deterministic coverage/convergence
            obs_levels=[]
            for nn in args.steps:
                if nn>args.loops:continue
                # stratified clusters: deterministic prefix within each geometric group
                indices=np.concatenate([np.flatnonzero(kinds==i)[:nn] for i in range(3)])
                ids=c['idx'][indices];sign=c['sign'][indices];length=c['length'][indices];ki=kinds[indices]
                from stage4_smearing_flux import measure_scalar_groups
                obs=measure_scalar_groups(links,20,int(sp['E']),ids,sign,length,ki,nkind=3)
                obs_levels.append(obs)
            observations.append(np.stack(obs_levels))
        A=np.stack(observations) # [seed, step, time, operator]
        # std of difference between coarser/finer spatial projections across times and seeds
        comparison={}
        for j,nn in enumerate([x for x in args.steps if x<=args.loops]):
            if j==len(args.steps)-1:continue
            diff=A[:,j]-A[:,-1]
            comparison[str(nn)]={'rms_difference_to_largest':np.sqrt(np.mean(diff*diff,axis=(0,1))).tolist(),
                                'average_signal':A[:,j].mean(axis=(0,1)).tolist()}
        # the 20 timeslices per snapshot are strongly correlated; descriptive same-field covariance ONLY
        final=A[:,-1,:,:].reshape(-1,3)
        cov=np.corrcoef(final,rowvar=False)
        report={'geometry':kind,'geometry_hash':sp['graph_hash'],'seeds':args.seeds,
                'sampling': 'deterministic spatial cluster subset, not full lattice zero-momentum sum',
                'cluster_area_boundary_summary':stats,'nested_spatial_coverage':comparison,
                'same_field_channel_correlations':cov.tolist(), 'same_field_rank':rank_stats(final),
                'elapsed_seconds':time.monotonic()-start,'mass_fit_admitted':False}
        np.savez_compressed(out/f'{kind}_projection_pilot.npz',observables=A,steps=np.array([x for x in args.steps if x<=args.loops]),seeds=np.array(args.seeds),areas=ar,kind=kinds,lengths=lengths)
        (out/f'{kind}_projection_report.json').write_text(json.dumps(report,indent=2))
        reports.append(report)
        print(kind,'finished in',round(report['elapsed_seconds'],1),'seconds',flush=True)
    (out/'summary.json').write_text(json.dumps(reports,indent=2))

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--inputs',default='/mnt/data');p.add_argument('--output',default=str(ROOT/'results'));p.add_argument('--kinds',nargs='+',default=['square','penrose']);p.add_argument('--seeds',nargs='+',type=int,default=[101,211,307,419]);p.add_argument('--loops',type=int,default=384);p.add_argument('--steps',nargs='+',type=int,default=[96,192,384]);p.add_argument('--seed',type=int,default=19)
 main(p.parse_args())
