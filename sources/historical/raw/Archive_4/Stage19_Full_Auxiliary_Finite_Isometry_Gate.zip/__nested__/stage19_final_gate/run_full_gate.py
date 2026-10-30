import os,sys,time,json,hashlib
from pathlib import Path
import numpy as np
from scipy.spatial import cKDTree
BASE=Path('/mnt/data/stage19_target_first');sys.path.insert(0,str(BASE))
from stage19_full import setup_geometry,neighbors,boundary,full_catalogue
from target_first import grow
from full_anchor_targets import TARGETS,SCALE,THRESHOLD
from matched_basis import weighted_observe
OUT=Path('/mnt/data/stage19_final_gate');OUT.mkdir(exist_ok=True)
SIZESET=(2,3,4,5,6,7,8,9,10,12,15)
prior=np.load('/mnt/data/stage19_strict_expanded/all_anchors_strict_min_distance.npz')
def do(kind):
 t=time.perf_counter();sp,_=setup_geometry(kind,20,3.5);F=int(sp['F']);adj=neighbors(sp);areas=np.asarray(sp['face_areas']);vv=np.asarray(sp['edge_vectors']);targets=np.array([[np.log(a),np.log(p),4*np.pi*a/p**2] for a,p in TARGETS]);
 src=Path('/mnt/data')/f'{kind}_nt20_seed101.npz'
 with np.load(src,allow_pickle=False) as z:
  links=z['links'];ss=json.loads(str(z['settings_json'].item()));assert ss['spatial_geometry_hash']==sp['graph_hash']
 paths=[]; roots=[];dists=[];tids=[];sizes=[];area_used=[];per_used=[];angle_used=[];miss=[];scanned=0
 for root in range(F):
  # Reconstruct the certified winning size before performing an expanded fallback.
  requested=(int(prior['best_size'][root]),) if kind=='penrose' and int(prior['best_size'][root]) in SIZESET else (3,5,8,10)
  best=(float('inf'),None)
  for sizes_to_try in (requested,SIZESET):
   seen=set()
   for nf in sizes_to_try:
    for v in range(4):
     fs=grow(adj,root,nf,v)
     if fs is None or fs in seen:continue
     seen.add(fs);path=boundary(sp,fs)
     if path is None:continue
     ai=np.array([e for e,s in path],int); ll=np.linalg.norm(vv[ai],axis=1)
     ar=float(areas[list(fs)].sum());pe=float(ll.sum())
     f=np.array([np.log(ar),np.log(pe),4*np.pi*ar/pe**2]);dis=np.linalg.norm((targets-f)/SCALE,axis=1);j=int(np.argmin(dis));d=float(dis[j]);scanned+=1
     if d<best[0]:
      phi=np.arctan2(vv[ai,1],vv[ai,0]);z=np.sum(ll*np.exp(2j*phi));ang=float((np.angle(z)/2)%np.pi) if abs(z)>1e-10 else float('nan')
      best=(d,(path,j,nf,ar,pe,ang))
   if best[0]<=THRESHOLD:break
  if best[0]<=THRESHOLD:
   path,j,nf,ar,pe,ang=best[1];paths.append(path);roots.append(root);dists.append(best[0]);tids.append(j);sizes.append(nf);area_used.append(ar);per_used.append(pe);angle_used.append(ang)
  else:miss.append(root)
  if root%5000==0:print(kind,'root',root,'covered',len(roots),'elapsed',round(time.perf_counter()-t,1),flush=True)
 print(kind,'CAT DONE',len(roots),'missing',len(miss),'s',round(time.perf_counter()-t,1),flush=True)
 maxlen=max(map(len,paths));idx=np.full((len(paths),maxlen),-1,np.int64);sign=np.zeros_like(idx)
 for i,p in enumerate(paths):
  for j,(e,s) in enumerate(p):idx[i,j]=e;sign[i,j]=s
 weights=np.full(len(paths),1.0/F)
 start=time.perf_counter();obs=weighted_observe(links,20,int(sp['E']),idx,sign,np.array(list(map(len,paths)),np.int64),weights,np.zeros(len(paths),np.int64),1);mtime=time.perf_counter()-start
 start=time.perf_counter();cat=full_catalogue(sp);ct=weighted_observe(links,20,int(sp['E']),cat['idx'].astype(np.int64),cat['sign'].astype(np.int64),cat['length'],np.ones(len(cat['kind']))/F,cat['kind'],3);ctime=time.perf_counter()-start
 # Note missing anchors contribute literal zero in auxiliary; also report conditional matched-root normalized mean separately
 obs_cond=obs*F/len(paths)
 ori=np.array(angle_used);valid=np.isfinite(ori);hist=np.histogram(ori[valid],bins=12,range=(0,np.pi))[0]
 np.savez_compressed(OUT/f'{kind}_full_auxiliary_seed101.npz',aux_unconditional=obs,aux_conditional=obs_cond,control=ct,roots=np.array(roots),unmatched=np.array(miss),distance=np.array(dists),targets=np.array(tids),faces=np.array(sizes),area=np.array(area_used),perimeter=np.array(per_used),orientation=ori)
 report={'geometry':kind,'F':F,'covered':len(paths),'missing':len(miss),'fraction':len(paths)/F,'threshold':THRESHOLD,'scan_seconds':time.perf_counter()-t,'aux_seconds':mtime,'control_seconds_including_catalogue':ctime,'orientation_hist_12':hist.tolist(),'undefined_orientation':int((~valid).sum()),'target_counts':np.bincount(tids,minlength=len(TARGETS)).tolist(),'face_counts':{str(k):int(np.sum(np.asarray(sizes)==k)) for k in sorted(set(sizes))},'max_distance':max(dists),'aux_means_unconditional':float(obs.mean()),'aux_means_conditional':float(obs_cond.mean()),'control_means':ct.mean(axis=0).tolist(),'graph_hash':sp['graph_hash'],'source':str(src),'scanned_valid_candidates':scanned}
 return report,sp
if __name__=='__main__':
 reports={};sps={}
 for kind in ('square','penrose'):
  reports[kind],sps[kind]=do(kind)
  (OUT/'RESULTS_PARTIAL.json').write_text(json.dumps(reports,indent=2))
 (OUT/'RESULTS.json').write_text(json.dumps(reports,indent=2))
 print('COMPLETE',flush=True)
