import sys,json,itertools,time
from pathlib import Path
import numpy as np
from scipy.spatial import cKDTree
sys.path.insert(0,'/mnt/data/stage19_target_first')
from stage19_full import setup_geometry
out={}
for kind in ('square','penrose'):
 sp,_=setup_geometry(kind,20,3.5);p=np.asarray(sp['periods']);ip=np.linalg.inv(p);xy=np.asarray(sp['xy']);E=np.asarray(sp['edges']); V=len(xy)
 # Candidate Euclidean isometries that are also torus lattice automorphisms:
 # A in GL(2,Z) with bounded entries and A's induced physical transform orthogonal.
 # Orthogonality constraint bounds entries; for this period basis use [-3,3] as a screen,
 # not as a proof of completeness without an explicit bound.
 good=[]
 for abcd in itertools.product(range(-3,4),repeat=4):
  a,b,c,d=abcd
  if abs(a*d-b*c)!=1:continue
  A=np.array([[a,b],[c,d]],float);Q=p.T@A@np.linalg.inv(p.T)
  if np.max(np.abs(Q.T@Q-np.eye(2)))<1e-7:
   good.append({'integer_matrix':list(abcd),'det':int(round(np.linalg.det(Q))),'physical_Q':Q.tolist()})
 # shift candidate exhaustive for a chosen vertex v0: any affine isometry must map it onto a vertex.
 # First reject candidate using sorted pairwise distance fingerprints for fixed 6 probe vertices,
 # sampled possible translations; full permutation validation only when probes match.
 x0=xy[0]; uv=np.mod(xy@ip,1);uv=np.minimum(uv,np.nextafter(1.,0.));tree=cKDTree(uv,boxsize=1.0)
 degrees=np.bincount(E.flatten(),minlength=V)
 allowed=np.flatnonzero(degrees==degrees[0]);results=[]
 probe=np.array([0,1,2,3,4,5,11,19,23,37,47,97,191,307,401,701,1103,2021,4001,7001,11011,17011],dtype=int);probe=probe[probe<V]
 edgeset={tuple(sorted(map(int,x))) for x in E}
 for item in good:
  Q=np.array(item['physical_Q']);rq=xy@Q.T
  # Each candidate image for vertex 0 generates one possible translation modulo period lattice.
  offsets=np.mod((xy[allowed]-rq[0])@ip,1)
  # Compare degree of mapped probes before expensive full-bijection test.
  pass_probe=0;valid=[]
  for i,offset in zip(allowed,offsets):
   uvp=np.mod(rq[probe]@ip+offset,1)
   ds,inds=tree.query(uvp,distance_upper_bound=1e-7)
   if not np.isfinite(ds).all() or not np.array_equal(degrees[probe],degrees[inds]):continue
   pass_probe+=1
   uvfull=np.mod(rq@ip+offset,1)
   ds2,inds2=tree.query(uvfull,distance_upper_bound=1e-7)
   if not np.isfinite(ds2).all() or len(set(inds2))!=V:continue
   if not np.array_equal(degrees,degrees[inds2]):continue
   if all(tuple(sorted((int(inds2[u]),int(inds2[v])))) in edgeset for u,v in E):valid.append(int(i))
  item['translation_candidates_with_reference_degree']=int(len(allowed));item['probe_passes']=pass_probe;item['verified_affine_automorphisms_reference_images']=valid[:30];item['verified_count']=len(valid)
  results.append(item)
 out[kind]={'vertex_count':V,'period_basis':p.tolist(),'integer_matrix_screen':'entries -3..3, unimodular and physically orthogonal','candidate_linear_actions':results,'scope':'For each screened linear action, translations exhaust possible images of one reference vertex. Does not classify non-Euclidean graph automorphisms; integer matrix cutoff not analytically certified.'}
 print(kind,'actions',len(good),'counts',[v['verified_count'] for v in results],flush=True)
Path('/mnt/data/stage19_final_gate/SYMMETRY_SCREEN.json').write_text(json.dumps(out,indent=2))
