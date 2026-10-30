#!/usr/bin/env python3
"""Geometry-only diagnosis of missing target-matched anchors; never silently impute."""
import argparse,json,time,hashlib,sys
from pathlib import Path
import numpy as np
from stage19_full import setup_geometry,neighbors,boundary
from target_first import grow
from full_anchor_targets import TARGETS,SCALE,THRESHOLD

def screen(sp, roots, sizes, variants, thresholds):
 adj=neighbors(sp); areas=np.asarray(sp['face_areas']); vec=np.asarray(sp['edge_vectors']); tar=np.array([[np.log(a),np.log(p),4*np.pi*a/p**2] for a,p in TARGETS]); out=np.full((len(roots),),np.inf); bestsize=np.full(len(roots),-1); besttarget=np.full(len(roots),-1); bestfeature=np.full((len(roots),3),np.nan); total=0; invalid=0; no_cluster=0; count=np.zeros(len(roots),np.int32); admissible=np.zeros((len(roots),len(thresholds)),np.int32)
 for j,root in enumerate(roots):
  seen=set()
  for size in sizes:
   for variant in range(variants):
    fs=grow(adj,int(root),size,variant)
    if fs is None: no_cluster+=1;continue
    if fs in seen:continue
    seen.add(fs)
    path=boundary(sp,fs)
    if path is None: invalid+=1;continue
    total+=1;ids=np.asarray([e for e,s in path],int);per=np.linalg.norm(vec[ids],axis=1).sum();ar=areas[list(fs)].sum();f=np.array([np.log(ar),np.log(per),4*np.pi*ar/per**2]); d=np.linalg.norm((tar-f)/SCALE,axis=1); k=int(np.argmin(d)); v=d[k]
    if v<out[j]:out[j]=v;bestsize[j]=size;besttarget[j]=k;bestfeature[j]=f
    count[j]+=1
  admissible[j]=np.asarray([int(out[j]<=t) for t in thresholds])
 return {'min_distance':out,'size':bestsize,'target':besttarget,'feature':bestfeature,'candidate_counts':count,'admissible':admissible,'candidate_total':total,'invalid_boundaries':invalid,'no_clusters':no_cluster}

def summary(data,thresholds):
 d=data['min_distance'];good=np.isfinite(d);return {'candidate_total':int(data['candidate_total']),'invalid_boundaries':int(data['invalid_boundaries']),'no_clusters':int(data['no_clusters']),'roots_without_valid_boundary':int(np.sum(~good)),'min_distance_quantiles':np.quantile(d[good],[0,.25,.5,.75,.9,.95,.99,1]).tolist(),'coverage_by_threshold':{str(t):{'covered':int(np.sum(d<=t)),'missing':int(np.sum(d>t)),'fraction':float(np.mean(d<=t))} for t in thresholds},'missing_by_nearest_target_at_1p5':np.bincount(data['target'][d>1.5],minlength=len(TARGETS)).tolist(),'missing_by_best_face_count_at_1p5':{str(k):int(np.sum((d>1.5)&(data['size']==k))) for k in sorted(set(data['size']))}}

def main():
 p=argparse.ArgumentParser();p.add_argument('--roots',type=int,default=0);p.add_argument('--variants',type=int,default=4);p.add_argument('--output',default='/mnt/data/stage19_target_diagnostic');a=p.parse_args();t=time.perf_counter();sp,_=setup_geometry('penrose',20,3.5);F=int(sp['F']);roots=np.arange(F,dtype=np.int64) if not a.roots else np.unique(np.linspace(0,F-1,a.roots,dtype=np.int64));thresholds=(1.5,1.65,1.8,2.0,2.25,2.5)
 variants=a.variants
 base=screen(sp,roots,(3,5,8,10),2,thresholds);print('base',summary(base,thresholds),flush=True)
 configs=[('variants4',(3,5,8,10),variants),('sizes_extended',(2,3,4,5,6,7,8,9,10,12,15),2),('sizes_and_variants',(2,3,4,5,6,7,8,9,10,12,15),variants)]
 results={'geometry':'penrose','roots_tested':int(len(roots)),'total_roots':F,'geometry_hash':sp['graph_hash'],'thresholds':thresholds,'baseline':summary(base,thresholds)}
 out=Path(a.output);out.mkdir(parents=True,exist_ok=True)
 for name,sizes,nvar in configs:
  t0=time.perf_counter();data=screen(sp,roots,sizes,nvar,thresholds);results[name]=summary(data,thresholds);results[name]['seconds']=time.perf_counter()-t0
  b=(base['min_distance']>1.5);v=(data['min_distance']<=1.5);results[name]['baseline_missing_recovered_at_1p5']=int(np.sum(b&v));results[name]['baseline_missing_still_missing_at_1p5']=int(np.sum(b&~v));
  print(name,results[name],flush=True)
  np.savez_compressed(out/f'{name}_per_anchor.npz',anchors=roots,minimum_distance=data['min_distance'],best_size=data['size'],best_target=data['target'],best_features=data['feature'],candidate_counts=data['candidate_counts'])
 results['total_seconds']=time.perf_counter()-t
 (out/'DIAGNOSTIC_REPORT.json').write_text(json.dumps(results,indent=2,allow_nan=False));print('saved',out,flush=True)
if __name__=='__main__':main()
