import numpy as np, json
from collections import defaultdict
polygons=[(0,1,2,3),(2,1,4,5),(5,4,6,7)]
vertices=[(v,t) for t in (0,1) for v in range(8)]
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
assert len(seams)==2 and all(list(B3[s]) in ([1,-1,0],[-1,1,0],[0,1,-1],[0,-1,1]) for s in seams)
# Different seam boundaries on middle prism share no edges
seam_edge_sets=[set(np.flatnonzero(B2[:,s])) for s in seams]
assert not (seam_edge_sets[0]&seam_edge_sets[1])
# rank-1, PSD fundamental-sector coefficient for K(x,y)=chi_1/2(x^{-1} y).
d=2; omega=np.zeros(d*d)
for i in range(d):omega[i*d+i]=1
M=np.outer(omega,omega)
assert np.allclose(np.linalg.eigvalsh(M),[0,0,0,2])
report={'source':'constructed three-rhombus strip, not provenance-certified Penrose tiles','vertices':len(vertices),'edges':len(edges),'faces':len(faces),'cells':3,'shared_faces':seams.tolist(),'shared_coefficients':[B3[s].tolist() for s in seams],'shared_face_edge_disjoint':True,'rank_d1':int(np.linalg.matrix_rank(B1)),'rank_d2':int(np.linalg.matrix_rank(B2)),'rank_d3':int(np.linalg.matrix_rank(B3)),'d1d2_zero':True,'d2d3_zero':True,'middle_prism_other_faces':4,'fundamental_multiport_fourier_block_eigenvalues':np.linalg.eigvalsh(M).tolist(),'analytical_scope':'left/right five-face disk kernels, middle four-face annulus cylinder kernel; does not include external glued plaquettes'}
np.savez('/mnt/data/R3_three_prism_multiport_2026_10_27/incidence.npz',d1=B1,d2=B2,d3=B3)
with open('/mnt/data/R3_three_prism_multiport_2026_10_27/certificate.json','w') as f:json.dump(report,f,indent=2)
print(json.dumps(report,indent=2))
