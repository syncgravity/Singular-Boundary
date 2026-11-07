#!/usr/bin/env python3
"""Source-inspired Z5 -> 3+2 orthogonal candidate, finite cubical skeleton.
NOT the dissertation's authenticated regulator; all physical 3D/PF YM gates OPEN.
"""
import itertools
from collections import Counter,defaultdict
import numpy as np
from math import pi

def orthogonal_basis():
 j=np.arange(5,dtype=float)
 B=np.stack([np.ones(5)/np.sqrt(5),np.sqrt(2/5)*np.cos(2*pi*j/5),np.sqrt(2/5)*np.sin(2*pi*j/5),np.sqrt(2/5)*np.cos(4*pi*j/5),np.sqrt(2/5)*np.sin(4*pi*j/5)])
 assert np.max(np.abs(B@B.T-np.eye(5)))<1e-13
 return B

def patch(Bound=6,Rz=2.5,Rxy=3.0,Rwin=1.5):
 B=orthogonal_basis()
 points=np.array(list(itertools.product(range(-Bound,Bound+1),repeat=5)),dtype=np.int16)
 coords=points@B.T
 phys,internal=coords[:,:3],coords[:,3:]
 normals=np.array([(np.cos(2*pi*j/10),np.sin(2*pi*j/10)) for j in range(10)])
 accept=(np.abs(phys[:,0])<=Rz)&(np.linalg.norm(phys[:,1:3],axis=1)<=Rxy)&(np.max(internal@normals.T,axis=1)<=Rwin*np.cos(pi/10))
 V={tuple(map(int,a)) for a in points[accept]}
 def shift(x,i):
  y=list(x);y[i]+=1;return tuple(y)
 edges=set();faces=set();cubes=set()
 for v in V:
  for i in range(5):
   if shift(v,i) in V:edges.add((v,i))
  for i,j in itertools.combinations(range(5),2):
   if all(tuple(v[k]+int(k in sub) for k in range(5)) in V for sub in ((),(i,),(j,),(i,j))):
    faces.add((v,i,j))
  for i,j,k in itertools.combinations(range(5),3):
   if all(tuple(v[kk]+int(kk in sub) for kk in range(5)) in V for n in range(4) for sub in itertools.combinations((i,j,k),n)):
    cubes.add((v,i,j,k))
 # Verify boundary of every cube has six faces, and ∂² zero by edge cancellation.
 def square_bd(v,i,j):
  return [( (shift(v,i),j),+1),((v,j),-1),((shift(v,j),i),-1),((v,i),+1)]
 cube_inc=Counter()
 for v,i,j,k in cubes:
  boundary=[((shift(v,i),j,k),+1),((v,j,k),-1),((shift(v,j),i,k),-1),((v,i,k),+1),((shift(v,k),i,j),+1),((v,i,j),-1)]
  eb=Counter()
  for face,sign in boundary:
   assert face in faces
   cube_inc[face]+=1
   fv,a,b=face
   for edge,eps in square_bd(fv,a,b):eb[edge]+=sign*eps
  assert not any(eb.values())
 inc=Counter()
 for v,i,j in faces:
  for x in (i,j):
   for b in (v,shift(v,j if x==i else i)):
    inc[(b,x)]+=1
 max_inc=max(inc.values(),default=0)
 max_cube_inc=max(cube_inc.values(),default=0)
 # Physical dimension and orientation of projected cubes, all determinant nonzero.
 phys_basis=B[:3,:]
 dets=[abs(np.linalg.det(phys_basis[:,list(cols)])) for cols in itertools.combinations(range(5),3)]
 assert min(dets)>0.08
 # C5 rotates physical XY; Z5 cyclic permutation preserves the projected action.
 q=np.roll(np.eye(5),1,axis=0)
 mat=B@q@B.T
 assert np.max(np.abs(mat[0,1:]))<1e-12
 assert np.max(np.abs(mat[3:, :3]))<1e-12
 assert np.max(np.abs(mat[:3,3:]))<1e-12
 return {'vertices':len(V),'links':len(edges),'faces':len(faces),'cubes':len(cubes),'max_faces_per_edge':max_inc,'max_cubes_per_face':max_cube_inc,'faces_over_two_cubes':sum(c>2 for c in cube_inc.values()),'cube_incidence_histogram':dict(sorted(Counter(cube_inc.values()).items())),'triple_proj_det_range':(round(min(dets),6),round(max(dets),6))}
if __name__=='__main__':
 for B in (4,5,6):print('box_bound',B,patch(Bound=B))
 print('PASS finite 3+2 orthogonal projection and cubical incidence/∂² tests; NOT source fidelity or 3D manifold certification')