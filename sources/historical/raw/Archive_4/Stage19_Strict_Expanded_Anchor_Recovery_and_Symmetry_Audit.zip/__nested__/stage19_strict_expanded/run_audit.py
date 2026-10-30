import sys,time,json,hashlib
from pathlib import Path
import numpy as np
from scipy.spatial import cKDTree
base=Path('/mnt/data/stage19_target_first');sys.path.insert(0,str(base))
from stage19_full import setup_geometry
from diagnose_missing import screen
out=Path('/mnt/data/stage19_strict_expanded');out.mkdir(exist_ok=True)
start=time.time(); f=np.load('/mnt/data/stage19_target_diagnostic/variants4_per_anchor.npz');roots=f['anchors'];d=f['minimum_distance'].copy();bs=f['best_size'].copy();bt=f['best_target'].copy();bf=f['best_features'].copy();missing=np.flatnonzero(d>1.5)
sp,_=setup_geometry('penrose',20,3.5)
extra=screen(sp,missing,(2,3,4,5,6,7,8,9,10,12,15),4,(1.5,)); improve=extra['min_distance']<d[missing];ids=missing[improve]
d[ids]=extra['min_distance'][improve];bs[ids]=extra['size'][improve];bt[ids]=extra['target'][improve];bf[ids]=extra['feature'][improve]
covered=d<=1.5
np.savez_compressed(out/'all_anchors_strict_min_distance.npz',anchors=roots,minimum_distance=d,best_size=bs,best_target=bt,best_features=bf,covered=covered,originally_missing=missing)
# Test finite-torus geometric rotations/reflections as actual automorphisms, not merely angular histograms.
xy=np.asarray(sp['xy']); E=np.asarray(sp['edges']); periods=np.asarray(sp['periods']); inv=np.linalg.inv(periods); uv=xy@inv
uv=np.mod(uv,1.0);uv=np.minimum(uv,np.nextafter(1.0,0.0));tree=cKDTree(uv,boxsize=1.0)
edge_set={tuple(sorted(map(int,p))) for p in E}
# candidate D5 rotations and reflections in physical plane; torus period matrix generally breaks them.
angles=[2*np.pi*k/5 for k in range(5)];sym=[]
for typ in ('rotation','reflection'):
 for k,a in enumerate(angles):
  R=np.array([[np.cos(a),-np.sin(a)],[np.sin(a),np.cos(a)]])
  if typ=='reflection':R=R@np.diag([1,-1])
  # a symmetry on periodic torus requires action integral on period lattice
  M=periods@R.T@inv
  lattice_error=float(np.max(np.abs(M-np.rint(M))))
  row={'type':typ,'k':k,'angle_degrees':72*k,'period_lattice_integer_error':lattice_error,'torus_compatible':lattice_error<1e-7,'vertex_edge_automorphism':False}
  if row['torus_compatible']:
   mapped=(uv@M)%1.0;dist,idx=tree.query(mapped,k=1);tol=1e-6
   row['max_fractional_vertex_matching_error']=float(dist.max());row['unique_image_vertices']=int(len(set(map(int,idx))))
   if float(dist.max())<tol and row['unique_image_vertices']==len(uv):
    row['vertex_edge_automorphism']=all(tuple(sorted((int(idx[u]),int(idx[v])))) in edge_set for u,v in E)
  sym.append(row)
rep={'geometry':'penrose_M55','geometry_hash':sp['graph_hash'],'threshold':1.5,'sizes':[2,3,4,5,6,7,8,9,10,12,15],'variants':4,'anchors':len(roots),'previously_missing':len(missing),'recovered_among_previously_missing':int(improve.sum() and np.sum(extra['min_distance']<=1.5)),'now_covered':int(covered.sum()),'now_missing':int((~covered).sum()),'coverage':float(covered.mean()),'original_covered':int(len(roots)-len(missing)),'symmetry_candidates':sym,'time_seconds':time.time()-start,'caveat':'Combines full previous strict scan with exhaustive expanded scan only on previous failures; logically equivalent strict coverage to scanning all anchors with superset. Finite-torus global symmetries only; local approximate shape symmetry not assessed. Full loop catalogues and dynamic gauge measurements not computed.'}
(out/'REPORT.json').write_text(json.dumps(rep,indent=2));print(json.dumps({k:v for k,v in rep.items() if k!='symmetry_candidates'},indent=2));print('SYMMETRIES',[(x['type'],x['k'],x['torus_compatible'],x['vertex_edge_automorphism']) for x in sym]);
