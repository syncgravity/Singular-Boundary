"""Validate lifted M5 ten-face dual cycle winding about face 0."""
import numpy as np
from penrose_causal_study import Approximant
from wilson_torus import penrose_faces
a=Approximant(M=5); fi,sg,E=penrose_faces(a)
cycle=[1,3,2,4,154,150,11,10,7,8,1]
edge_ids=[3,2,5,19,296,17,18,12,8,14]
for (f,g),e in zip(zip(cycle,cycle[1:]),edge_ids):
    assert int(sg[f,list(fi[f]).index(e)])==-int(sg[g,list(fi[g]).index(e)])
eye=np.eye(5)
centers=np.array([a.Qpar@(np.asarray(a.nodes[u],float)+(eye[i]+eye[j])/2) for u,ua,uab,ub,i,j in a.faces])
period=np.array([a.Qpar@a.t1,a.Qpar@a.t2])
points=[centers[cycle[0]]];shifts=[]
for f in cycle[1:]:
    candidates=[(np.linalg.norm(centers[f]+m*period[0]+n*period[1]-points[-1]),m,n,centers[f]+m*period[0]+n*period[1]) for m in range(-2,3) for n in range(-2,3)]
    d,m,n,p=min(candidates,key=lambda z:z[0]);assert d<1.0
    shifts.append((f,m,n));points.append(p)
assert [(f,m,n) for f,m,n in shifts if m or n]==[(154,-1,0),(150,-1,0)]
p=np.array(points);assert np.linalg.norm(p[-1]-p[0])<1e-10
area=np.sum(p[:-1,0]*p[1:,1]-p[1:,0]*p[:-1,1])/2
u=p[:-1]-centers[0];v=p[1:]-centers[0]
winding=np.sum(np.arctan2(u[:,0]*v[:,1]-u[:,1]*v[:,0],np.sum(u*v,axis=1)))/(2*np.pi)
assert 1.80<area<1.82 and abs(winding-1)<1e-10
print("PASS M5 dual cycle contractible winding +1; area",area)
