#!/usr/bin/env python3
"""3D physical Delaunay geometric mesh on UNAUTHENTICATED full Z5 3+2 patch.
Finite test only. QJ triangulation can break exact 5-fold symmetry and no uniform
shape regularity, h/R refinement or source-Gauss model is claimed.
"""
import itertools
from collections import Counter
import numpy as np
from scipy.spatial import Delaunay
from verify_z5_3d_gauge_skeleton import orthogonal_basis
B=orthogonal_basis()
Rz=2.5;Rxy=3.;Rwin=1.5
points=np.array(list(itertools.product(range(-4,5),repeat=5)),dtype=np.int16)
coords=points@B.T;phys=coords[:,:3];internal=coords[:,3:]
normals=np.array([(np.cos(2*np.pi*j/10),np.sin(2*np.pi*j/10)) for j in range(10)])
mask=(abs(phys[:,0])<=Rz)&(np.linalg.norm(phys[:,1:],axis=1)<=Rxy)&(np.max(internal@normals.T,axis=1)<=Rwin*np.cos(np.pi/10))
X=phys[mask]
assert len(X)==903
tri=Delaunay(X,qhull_options='QJ Qbb Qc')
tets=tri.simplices
assert len(set(map(tuple,map(sorted,tets))))==len(tets)
face_counts=Counter(tuple(sorted((t[i],t[j],t[k]))) for t in tets for i,j,k in ((0,1,2),(0,1,3),(0,2,3),(1,2,3)))
assert max(face_counts.values())==2 and min(face_counts.values())==1
v=np.array([abs(np.linalg.det(np.stack([X[t[1]]-X[t[0]],X[t[2]]-X[t[0]],X[t[3]]-X[t[0]]],axis=1)))/6 for t in tets])
print('vertices',len(X),'tetrahedra',len(tets),'faces',len(face_counts),'boundary faces',sum(y==1 for y in face_counts.values()))
print('volumes min/median/max',np.min(v),np.median(v),np.max(v),'nearzero',np.sum(v<1e-10))
edge_lengths=[]
for t in tets:
 ds=[np.linalg.norm(X[a]-X[b]) for a,b in itertools.combinations(t,2)]
 edge_lengths.append((min(ds),max(ds)))
ratios=np.array([b/a if a>0 else np.inf for a,b in edge_lengths])
print('edge max/min ratio quantiles',np.quantile(ratios,[0,.5,.9,1]))
print('PASS geometric 3D Delaunay incidence≤2; physical-source and uniform-mesh claims OPEN')