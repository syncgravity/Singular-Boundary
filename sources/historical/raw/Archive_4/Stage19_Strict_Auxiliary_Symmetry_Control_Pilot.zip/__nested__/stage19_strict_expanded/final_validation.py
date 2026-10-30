import sys,json,time,hashlib
from pathlib import Path
import numpy as np
from scipy.spatial import cKDTree
base=Path('/mnt/data/stage19_target_first');sys.path.insert(0,str(base))
from stage19_full import setup_geometry,neighbors,boundary,full_catalogue
from target_first import grow
from full_anchor_targets import TARGETS,SCALE,THRESHOLD
from matched_basis import weighted_observe
out=Path('/mnt/data/stage19_final_validation');out.mkdir(exist_ok=True)
prior=np.load('/mnt/data/stage19_strict_expanded/all_anchors_strict_min_distance.npz')
results={'strict_threshold':1.5,'scan_anchors':22808,'certified_penrose_covered':int(prior['covered'].sum()),'certified_penrose_uncovered':int((~prior['covered']).sum()),'scope':'Target-matched auxiliary measured on sampled spatial anchors, full-volume scalar controls on all anchors; NOT a full matched production operator. Symmetry screen of origin-fixed D4/D5 candidates and a finite set of centers, not an exhaustive graph automorphism classification.'}
for kind in ('square','penrose'):
 t0=time.perf_counter();sp,_=setup_geometry(kind,20,3.5)
 xy=np.asarray(sp['xy']);period=np.asarray(sp['periods']);inv=np.linalg.inv(period);uv=np.mod(xy@inv,1.);uv=np.minimum(uv,np.nextafter(1.,0.));tree=cKDTree(uv,boxsize=1.)
 edges=np.asarray(sp['edges']);edge_set={tuple(sorted(map(int,x))) for x in edges}
 # Standard Euclidean candidate point maps, and candidate center offsets at the first 8 vertex positions.
 candidates=[]
 for family, angles in [('D4',[np.pi*k/2 for k in range(4)]),('D5',[np.pi*k/5 for k in range(10)])]:
  for k,a in enumerate(angles):
   R=np.array([[np.cos(a),-np.sin(a)],[np.sin(a),np.cos(a)]])
   for refl in (False,True):
    Q=R@(np.diag([1.,-1.]) if refl else np.eye(2)); M=period@Q.T@inv
    err=float(abs(M-np.rint(M)).max());item={'family':family,'k':k,'reflection':refl,'period_integer_error':err,'torus_compatible':err<1e-7,'automorphism_found':False}
    if err<1e-7:
     for cent in np.vstack([np.zeros(2),xy[:8]]):
      # row points transform about a candidate center
      transformed=np.mod((xy-cent)@Q.T+cent,period @ np.eye(2) if False else 1.) if False else np.mod(((xy-cent)@Q.T+cent)@inv,1.)
      dist,ind=tree.query(transformed)
      if dist.max()>1e-6 or len(np.unique(ind))!=len(xy):continue
      if all(tuple(sorted((int(ind[u]),int(ind[v])))) in edge_set for u,v in edges):
       item['automorphism_found']=True;item['center']=cent.tolist();break
    candidates.append(item)
 # sample 256 roots spanning all ranges. Strictly matching only selected roots with re-screening.
 anchors=np.unique(np.linspace(0,int(sp['F'])-1,256,dtype=np.int64));adj=neighbors(sp);areas=np.asarray(sp['face_areas']);vec=np.asarray(sp['edge_vectors'])
 target=np.array([[np.log(a),np.log(p),4*np.pi*a/p**2] for a,p in TARGETS]);rows=[];roots_covered=[]
 tb=time.perf_counter()
 for root in anchors:
  best=(np.inf,None)
  seen=set()
  for nf in (2,3,4,5,6,7,8,9,10,12,15):
   for v in range(4):
    fs=grow(adj,int(root),nf,v)
    if fs is None or fs in seen:continue
    seen.add(fs);path=boundary(sp,fs)
    if path is None:continue
    ar=float(areas[list(fs)].sum());per=float(np.linalg.norm(vec[[e for e,s in path]],axis=1).sum());feature=np.array([np.log(ar),np.log(per),4*np.pi*ar/per**2]);ds=np.linalg.norm((target-feature)/SCALE,axis=1);d=float(ds.min())
    if d<best[0]:best=(d,(path,nf,int(np.argmin(ds))))
  if best[0]<=THRESHOLD:
   rows.append((int(root),best[0],*best[1]));roots_covered.append(int(root))
 search_seconds=time.perf_counter()-tb
 if not rows:raise RuntimeError('no paths')
 length=np.array([len(x[2]) for x in rows],np.int64);W=int(length.max());idx=np.full((len(rows),W),-1,np.int64);sg=np.zeros((len(rows),W),np.int64)
 for j,r in enumerate(rows):
  for h,(eid,s) in enumerate(r[2]):idx[j,h]=eid;sg[j,h]=s
 fn=Path('/mnt/data')/f'{kind}_nt20_seed101.npz'
 with np.load(fn,allow_pickle=False) as z:
  links=z['links'];settings=json.loads(str(z['settings_json'].item()));sweep=int(z['sweeps'])
 assert settings['spatial_geometry_hash']==sp['graph_hash'] and sweep>=10000
 w=np.ones(len(rows))/len(rows)
 t=time.perf_counter();aux=weighted_observe(links,20,int(sp['E']),idx,sg,length,w,np.zeros(len(rows),np.int64),1);aux_time=time.perf_counter()-t
 t=time.perf_counter();control=full_catalogue(sp,(3,5,8));control_build=time.perf_counter()-t
 t=time.perf_counter();ctrl=weighted_observe(links,20,int(sp['E']),control['idx'].astype(np.int64),control['sign'].astype(np.int64),control['length'],np.ones(len(control['length']))/len(control['length']),control['kind'],3);ctrl_time=time.perf_counter()-t
 assert all(int((control['kind']==i).sum())==int(sp['F']) for i in range(3))
 assert np.isfinite(aux).all() and np.isfinite(ctrl).all()
 np.savez_compressed(out/f'{kind}_seed101_validation.npz',aux_sample=aux,full_control=ctrl,aux_anchors=np.array(roots_covered),aux_target=np.array([r[4] for r in rows]),aux_match_distance=np.array([r[1] for r in rows]))
 results[kind]={'graph_hash':sp['graph_hash'],'vertices':len(xy),'sample_anchors':len(anchors),'sample_covered':len(rows),'sample_coverage':len(rows)/len(anchors),'auxiliary_path_count':len(rows),'full_control_paths':len(control['length']),'full_control_counts':[int((control['kind']==i).sum()) for i in range(3)],'gauge_snapshot_sweep':sweep,'symmetry_candidates':candidates,'confirmed_candidate_symmetries':[(x['family'],x['k'],x['reflection']) for x in candidates if x['automorphism_found']],'search_seconds':search_seconds,'aux_measure_seconds':aux_time,'control_catalogue_seconds':control_build,'control_measure_seconds':ctrl_time,'aux_timeslice_mean':float(aux.mean()),'control_timeslice_mean':ctrl.mean(axis=0).tolist()}
 print(kind,'sample',len(rows), '/',len(anchors),'sym',results[kind]['confirmed_candidate_symmetries'],'seconds',results[kind]['aux_measure_seconds'],results[kind]['control_measure_seconds'],flush=True)
(out/'REPORT.json').write_text(json.dumps(results,indent=2));print('REPORT COMPLETE')
