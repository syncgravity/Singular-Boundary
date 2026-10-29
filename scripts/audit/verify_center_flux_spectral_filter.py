#!/usr/bin/env python3
"""SU2 target center-flux spectral filter: cochain audit + five-state parity comparator.
Not a full Penrose physical Hamiltonian diagonalization.
"""
import numpy as np
from scipy.linalg import eigh
from scipy.integrate import quad
from math import pi, sin, cos
faces=[(x,y) for y in range(3) for x in range(3)]
vertices=[(x,y) for y in range(4) for x in range(4)]
edges=set()
for x,y in faces:
 v=[(x,y),(x+1,y),(x+1,y+1),(x,y+1)]
 for a,b in zip(v,v[1:]+v[:1]):edges.add(tuple(sorted((a,b))))
edges=sorted(edges);ei={e:i for i,e in enumerate(edges)}
F=np.zeros((9,24),dtype=int);V=np.zeros((24,16),dtype=int)
for i,(x,y) in enumerate(faces):
 v=[(x,y),(x+1,y),(x+1,y+1),(x,y+1)]
 for a,b in zip(v,v[1:]+v[:1]):F[i,ei[tuple(sorted((a,b)))]]=1
for i,(a,b) in enumerate(edges):
 V[i,vertices.index(a)]=1;V[i,vertices.index(b)]=1
assert np.all((F@V)%2==0)
def rank2(a):
 a=a.copy()%2;r=0
 for j in range(a.shape[1]):
  p=next((k for k in range(r,a.shape[0]) if a[k,j]),None)
  if p is None:continue
  a[[r,p]]=a[[p,r]]
  for k in range(a.shape[0]):
   if k!=r and a[k,j]:a[k]^=a[r]
  r+=1
  if r==a.shape[0]:break
 return r
assert rank2(F)==9 and rank2(V)==15
north=np.zeros(24,dtype=int);east=north.copy()
for edge in [((1,2),(2,2)),((1,3),(2,3))]:north[ei[tuple(sorted(edge))]]=1
for edge in [((2,1),(2,2)),((3,1),(3,2))]:east[ei[tuple(sorted(edge))]]=1
target=np.zeros(9,int);target[faces.index((1,1))]=1
assert np.array_equal(F@north%2,target) and np.array_equal(F@east%2,target)
assert rank2(np.column_stack([V,north^east]))==rank2(V)
R=np.diag([1.,1.,-1.,1.,-1.]);C=np.diag([1.,1.,1.,-1.,-1.])
H0=np.diag([0.,3.,2.,.05,.09]);D=np.zeros((5,5))
D[0,2]=D[2,0]=.06;D[1,2]=D[2,1]=.04
assert np.allclose(R@D@R,-D) and np.allclose(C@D@C,D)
vals,U=eigh(H0+D);omega=U[:,0]
odd=(omega-R@omega)/2;even=(omega+R@omega)/2
eps=np.linalg.norm(D,2)
assert np.linalg.norm(odd)<=eps/2+1e-12
assert np.linalg.norm(even-(even[0]*np.array([1.,0.,0.,0.,0.])))<=eps**2/6+1e-12
q=quad(lambda u:2/pi*sin(u)**2*cos(u)**2,0,pi)[0]
assert abs(q-.25)<1e-12
print('PASS exact disk cochains, target-center spectral parity and physical SU2 Haar energy coefficient')
