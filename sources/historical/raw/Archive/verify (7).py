import numpy as np, json
from collections import defaultdict
polygons=[(0,1,4,3),(1,2,5,4),(3,4,7,6),(4,5,8,7)]
vertices=[(v,t) for t in (0,1) for v in range(9)]
vid={x:i for i,x in enumerate(vertices)}
edges=[]; emap={}; faces=[]; fmap={}; cellcols=[]
def edge(u,v):
 key=tuple(sorted((u,v)))
 if key not in emap: emap[key]=len(edges);edges.append((u,v))
 i=emap[key];return i,1 if edges[i]==(u,v) else -1
def face_cycle(p):
 col=defaultdict(int)
 for u,v in zip(p,p[1:]+p[:1]):
  i,s=edge(u,v);col[i]+=s
 return dict(col)
def add_face(p):
 key=tuple(sorted(p)); col=face_cycle(p)
 if key not in fmap: fmap[key]=len(faces);faces.append((p,col))
 i=fmap[key];old=faces[i][1]
 if col==old:s=1
 elif len(col)==len(old) and all(col.get(e,0)==-v for e,v in old.items()):s=-1
 else:raise RuntimeError('orientation inconsistency')
 return i,s
for poly in polygons:
 col=defaultdict(int)
 bottom=[vid[v,0] for v in poly];top=[vid[v,1] for v in poly]
 for cyc,coeff in [(bottom,-1),(top,1)]:
  i,s=add_face(cyc);col[i]+=coeff*s
 for a,b in zip(poly,poly[1:]+poly[:1]):
  i,s=add_face([vid[a,0],vid[b,0],vid[b,1],vid[a,1]]);col[i]+=s
 cellcols.append(dict(col))
B1=np.zeros((len(vertices),len(edges)),dtype=np.int64)
for i,(u,v) in enumerate(edges):B1[u,i]-=1;B1[v,i]+=1
B2=np.zeros((len(edges),len(faces)),dtype=np.int64)
for i,(_,col) in enumerate(faces):
 for e,s in col.items():B2[e,i]=s
B3=np.zeros((len(faces),len(polygons)),dtype=np.int64)
for j,col in enumerate(cellcols):
 for i,s in col.items():B3[i,j]=s
assert not (B1@B2).any() and not (B2@B3).any()
seams=np.flatnonzero(np.count_nonzero(B3,axis=1)==2)
assert len(seams)==4
assert all(sorted(abs(int(z)) for z in B3[s] if z)!=[] for s in seams)
assert np.all(np.sum(B3[seams]!=0,axis=0)==2)
assert np.all((B1@B2)==0) and np.all((B2@B3)==0)
from itertools import combinations
face_edges=[set(np.flatnonzero(B2[:,s])) for s in seams]
intersection_matrix=np.array([[len(face_edges[i]&face_edges[j]) for j in range(4)] for i in range(4)])
assert np.all(np.diag(intersection_matrix)==4)
rank=lambda m: int(np.linalg.matrix_rank(m, tol=1e-9))
report={'origin':'constructed 2x2 quadrilateral patch, combinatorially admissible, not provenance-certified from a Penrose tiling', 'vertices':len(vertices),'edges':len(edges),'faces':len(faces),'prisms':len(polygons),'interior_seam_faces':seams.tolist(), 'rank_d1':rank(B1),'rank_d2':rank(B2),'rank_d3':rank(B3),'chain_d1d2_zero':bool(not (B1@B2).any()),'chain_d2d3_zero':bool(not (B2@B3).any()),'seam_pair_shared_edges':intersection_matrix.tolist(),'face_cell_incidence':B3[seams].tolist()}
np.savez('/mnt/data/R3_looped_four_prism_2026_10_27/incidence.npz',d1=B1,d2=B2,d3=B3,seam_face_ids=seams)
with open('/mnt/data/R3_looped_four_prism_2026_10_27/certificate.json','w') as f:json.dump(report,f,indent=2)
print(json.dumps(report,indent=2))
# A three-port ordered SU(2) word is not positive-definite on SU(2)^3.
# Its fundamental Fourier tensor is a cyclic permutation (non-Hermitian).
d=2
P=np.zeros((d**3,d**3))
for a in range(d):
 for b in range(d):
  for c in range(d):
   def ix(i,j,k):return i*d*d+j*d+k
   P[ix(a,b,c),ix(b,c,a)]=1
assert np.allclose(P@P@P,np.eye(8))
H=(P+P.T)/2
spec=np.linalg.eigvalsh(H)
assert np.allclose(spec,[-.5]*4+[1.]*4)
print('cyclic fundamental block Hermitian part eigenvalues:',spec.tolist())
