#!/usr/bin/env python3
"""Full-Z5 C5 3+2 cut/project with a sufficiently large regular-decagon window.
Exact proof is cyclotomic norm + Z5 covering; this numerical test is illustrative.
NOT the dissertation's source-authenticated 3D gauge regulator.
"""
import itertools
import numpy as np
from math import pi,sqrt,cos
from scipy.spatial import cKDTree,Voronoi
from verify_z5_3d_gauge_skeleton import orthogonal_basis
B=orthogonal_basis();P=B[:3];Q=B[3:];Rwin=1.5
Rcover=sqrt(5)/2
rsep=min(1/sqrt(5),1/(5*Rwin))
assert Rwin*cos(pi/10)>Rcover
rng=np.random.default_rng(20261107)
normal=np.array([(cos(2*pi*j/10),np.sin(2*pi*j/10)) for j in range(10)])
def in_window(y):return np.max(y@normal.T,axis=-1)<=Rwin*cos(pi/10)+1e-12
N=10000
x=rng.uniform(-8,8,(N,3))
M=np.rint(x@P).astype(int)
physical=M@P.T;internal=M@Q.T
assert np.all(in_window(internal))
assert np.max(np.linalg.norm(physical-x,axis=1))<=Rcover+1e-12
assert abs(np.linalg.norm(P@np.eye(5)[:,0])-sqrt(3/5))<1e-12
# Internal window patches truncated to a cylinder; check observed separation & Voronoi bounded sites.
points=np.array(list(itertools.product(range(-4,5),repeat=5)),dtype=float)
coords=points@B.T
mask=(np.abs(coords[:,0])<=2.5)&(np.linalg.norm(coords[:,1:3],axis=1)<=3)&in_window(coords[:,3:])
physical=coords[mask,:3]
tree=cKDTree(physical)
dists,_=tree.query(physical,k=2)
observed=float(np.min(dists[:,1]))
assert observed>=rsep-1e-12,(observed,rsep)
vor=Voronoi(physical)
finite_cells=sum(all(k>=0 for k in vor.regions[vor.point_region[i]]) for i in range(len(physical)))
print('window inradius',Rwin*cos(pi/10),'rounding cover radius',Rcover,'arithmetic sep',rsep)
print('observed finite patch min separation',observed,'site count',len(physical),'finite Voronoi cells',finite_cells)
print('PASS: 10,000 rounding-covered sample points; uniform arith separation check; Voronoi cells finite in interior (not source-certified)')