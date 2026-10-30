#!/usr/bin/env python3
"""Stage 19 target-first *anchor-complete* geometry-only loop screening.

Does not imply point-group orbit completeness or scalar mass admission.
"""
import argparse, json, time, hashlib
from pathlib import Path
import numpy as np
from target_first import rooted_candidates, pack
from stage19_full import setup_geometry, full_catalogue
from matched_basis import weighted_observe

# Target physical shapes fixed a priori; area/perimeter Stage7 units.
TARGETS=((1.4,5.5),(1.9,6.5),(2.5,8.0),(3.2,9.5),(4.0,11.5))
# Standardized log(A), log(P), compactness matching. No face-count constraint.
SCALE=np.array([.25,.25,.12]); THRESHOLD=1.5

def assign(rows, roots, kmax=2, threshold=THRESHOLD):
    """For each root choose up to kmax distinct rooted loops, target nearest first.
    Missing eligible loops are counted and are NOT silently imputed.
    """
    rootmap={int(x):[] for x in roots}
    for i,r in enumerate(rows):rootmap[r[0]].append(i)
    target=np.array([[np.log(a),np.log(p),4*np.pi*a/p**2] for a,p in TARGETS])
    selected=[]; distance=[]; target_idx=[]; availability={};anchor_counts=[]
    for root in roots:
        root=int(root); inds=rootmap[root]
        scored=[]
        for i in inds:
            r=rows[i]; f=np.array([np.log(r[3]),np.log(r[4]),r[5]])
            ds=np.linalg.norm((target-f)/SCALE,axis=1)
            for t in np.where(ds<=threshold)[0]: scored.append((float(ds[t]),int(t),i))
        scored.sort();chosen=[];used=set();used_target=set()
        for d,t,i in scored:
            if i in used or t in used_target: continue
            chosen.append((i,d,t));used.add(i);used_target.add(t)
            if len(chosen)>=kmax:break
        selected.extend(x[0] for x in chosen);distance.extend(x[1] for x in chosen);target_idx.extend(x[2] for x in chosen)
        anchor_counts.append(len(chosen))
    return np.asarray(selected,dtype=int),np.asarray(distance),np.asarray(target_idx,dtype=int),np.asarray(anchor_counts,dtype=int)

def orientations(rows, sel, sp, bins=8):
    vv=np.asarray(sp['edge_vectors']); angles=[]; moduli=[]
    for i in sel:
        r=rows[int(i)]; ids=np.array([e for e,s in r[8]],dtype=np.int64)
        v=vv[ids]; ll=np.linalg.norm(v,axis=1); phi=np.arctan2(v[:,1],v[:,0]); z=(ll*np.exp(2j*phi)).sum()
        # magnitude close to zero => orientation undefined; not treated as balanced
        moduli.append(float(abs(z)/ll.sum()));angles.append(float((np.angle(z)/2)%np.pi))
    angles=np.asarray(angles);moduli=np.asarray(moduli)
    valid=moduli>1e-8
    hist=np.histogram(angles[valid],bins=bins,range=(0,np.pi))[0]
    return hist, int((~valid).sum()), angles, moduli

def make(kind,nroots=0,variants=2,sizes=(3,5,8,10),kmax=2,measure=False,seed=101,inputs='/mnt/data'):
    begin=time.perf_counter();sp,_=setup_geometry(kind,20,3.5);geometry_time=time.perf_counter()-begin
    F=int(sp['F']);roots=np.arange(F,dtype=np.int64) if nroots==0 else np.unique(np.linspace(0,F-1,nroots,dtype=np.int64))
    begin=time.perf_counter();rows=rooted_candidates(sp,roots,sizes=sizes,variants=variants);build_time=time.perf_counter()-begin
    begin=time.perf_counter();sel,d,targets,counts=assign(rows,roots,kmax=kmax);select_time=time.perf_counter()-begin
    hist,undefined,ang,anis=orientations(rows,sel,sp)
    bytarget=np.bincount(targets,minlength=len(TARGETS)).tolist()
    report={'geometry':kind,'face_anchors':F,'roots_evaluated':len(roots),'all_anchors_tested':len(roots)==F,
      'candidate_loops':len(rows),'selected_loops':len(sel),'anchors_with_no_match':int((counts==0).sum()),
      'anchors_with_one_match':int((counts==1).sum()),'anchors_with_multiple_matches':int((counts>=2).sum()),
      'anchor_coverage':float(np.mean(counts>0)),'selected_face_counts':{str(s):int(sum(rows[int(i)][1]==s for i in sel)) for s in sizes},
      'target_counts':bytarget,'target_definitions':TARGETS,'matching_threshold':float(THRESHOLD),
      'distance_quantiles':np.quantile(d,[0,.5,.9,.99,1]).tolist() if len(d) else [],
      'orientation_second_moment_bincount':hist.tolist(),'orientation_undefined':undefined,
      'rotation_reflection_orbits_completed':False,
      'geometry_seconds':geometry_time,'construction_seconds':build_time,'matching_seconds':select_time,
      'warning':'Anchored deterministic sample, not all loops or full point-group averaging; restricted matched subset NOT full-volume zero-momentum projector.'}
    if measure:
        if not len(sel):raise ValueError('no matches')
        paths=pack(rows,sel);w=1.0/np.maximum(counts,1);w=w[np.searchsorted(roots,paths['anchor'])];w/=w.sum()
        src=Path(inputs)/f'{kind}_nt20_seed{seed}.npz'
        with np.load(src,allow_pickle=False) as f:
            settings=json.loads(str(f['settings_json'].item())); assert settings['spatial_geometry_hash']==sp['graph_hash']; links=f['links']
        begin=time.perf_counter();obs=weighted_observe(links,20,int(sp['E']),paths['idx'].astype(np.int64),paths['sign'].astype(np.int64),paths['length'],w,np.zeros(len(sel),dtype=np.int64),1);report['matched_measure_seconds']=time.perf_counter()-begin
        # Original unrestricted full-volume operator stays separate and is never reweighted.
        begin=time.perf_counter();original=full_catalogue(sp,sizes=(3,5,8))
        cw=np.ones(len(original['length']))/len(original['length'])
        ctrl=weighted_observe(links,20,int(sp['E']),original['idx'].astype(np.int64),original['sign'].astype(np.int64),original['length'],cw,original['kind'],3)
        report['control_measure_seconds_including_catalogue']=time.perf_counter()-begin
        report['matched_timeslice_mean']=float(obs.mean());report['control_timeslice_means']=ctrl.mean(axis=0).tolist();report['control_full_face_coverage']=all(int((original['kind']==i).sum())==F for i in range(3))
    return report

def main():
    p=argparse.ArgumentParser();p.add_argument('--roots',type=int,default=0,help='0 means all face anchors');p.add_argument('--variants',type=int,default=2);p.add_argument('--max-per-anchor',type=int,default=2);p.add_argument('--measure',action='store_true');p.add_argument('--seed',type=int,default=101);p.add_argument('--inputs',default='/mnt/data');p.add_argument('--output',default='stage19_full_anchor_results');a=p.parse_args()
    out=Path(a.output);out.mkdir(parents=True,exist_ok=True)
    report={'configuration':vars(a),'geometries':{},'scientific_admission':False}
    for g in ('square','penrose'):
        report['geometries'][g]=make(g,a.roots,a.variants,kmax=a.max_per_anchor,measure=a.measure,seed=a.seed,inputs=a.inputs)
        print(g,report['geometries'][g],flush=True)
    (out/'STAGE19_FULL_ANCHOR_REPORT.json').write_text(json.dumps(report,indent=2,allow_nan=False))
if __name__=='__main__':main()
