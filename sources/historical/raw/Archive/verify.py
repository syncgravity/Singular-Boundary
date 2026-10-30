import numpy as np,json
# Explicit combinatorial extrusion of a single oriented quadrilateral; not an extraction of the supplied Penrose mesh.
V=[(i,t) for t in (0,1) for i in range(4)]
E=[]
for t in (0,1):
 for i in range(4): E.append(((i,t),((i+1)%4,t)))
for i in range(4):E.append(((i,0),(i,1)))
F=[[(i,0) for i in range(4)],[(i,1) for i in range(3,-1,-1)]]
for i in range(4):F.append([(i,0),(i,1),((i+1)%4,1),((i+1)%4,0)])
# Initial bottom orientation positive and top negative; side orientation chosen to cancel boundary.
# Check/correct orientation of face lists by computing kernel relation of face-edge matrix.
def incidence_faces(F):
 B=np.zeros((len(E),len(F)),dtype=int)
 for j,face in enumerate(F):
  for k,u in enumerate(face):
   v=face[(k+1)%len(face)]
   if (u,v) in E:B[E.index((u,v)),j]+=1
   elif (v,u) in E:B[E.index((v,u)),j]-=1
   else:raise ValueError((u,v))
 return B
B1=np.zeros((len(V),len(E)),dtype=int)
for j,(u,v) in enumerate(E):B1[V.index(u),j]=-1;B1[V.index(v),j]=1
B2=incidence_faces(F)
# orientations above boundary: bottom needs negative; top positive, sides as written each needs check
print('raw B2*1', B2@np.ones(6,dtype=int))
# solved cellular boundary signs, brute force six faces
import itertools
sol=[np.array(s) for s in itertools.product((-1,1),repeat=6) if not np.any(B2@np.array(s))]
assert sol
sign=next(s for s in sol if s[0]==1)
B3=sign[:,None]
assert not np.any(B1@B2)
assert not np.any(B2@B3)
np.savez('/mnt/data/R3_prism_incidence_verified_2026_10_27/prism_incidence.npz',d1=B1,d2=B2,d3=B3,vertices=np.array(V),edges=np.array([[V.index(u),V.index(v)] for u,v in E]),faces=np.array([[V.index(v) for v in face] for face in F]))
print(json.dumps({'vertices':len(V),'edges':len(E),'faces':len(F),'cells':1,'rank_d1':int(np.linalg.matrix_rank(B1)),'rank_d2':int(np.linalg.matrix_rank(B2)),'d1_d2_zero':bool(not np.any(B1@B2)),'d2_d3_zero':bool(not np.any(B2@B3)),'cell_orientations':sign.tolist(),'face_edge_incidence_nonzeros':int(np.count_nonzero(B2))},indent=2))
