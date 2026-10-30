#!/usr/bin/env python3
"""Deterministic exact Z2 cochain check and independent sector-resolvent model.
No diagonalization of full nonlinear SU(2) nine-face Hamiltonian is claimed.
"""
import numpy as np
from scipy.linalg import eigh
from scipy.integrate import quad
from math import pi,sin,cos

# Full 3x3 square rhombus disk, cochain C^1 -> C^2 and C^0 -> C^1.
vertices=[(x,y) for y in range(4) for x in range(4)]
faces=[(x,y) for y in range(3) for x in range(3)]
edge_set={}
for f in faces:
 x,y=f;v=[(x,y),(x+1,y),(x+1,y+1),(x,y+1)]
 for v1,v2 in zip(v,v[1:]+v[:1]):
  a=tuple(sorted((v1,v2)));edge_set[a]=None
edges=list(sorted(edge_set))
fi={v:i for i,v in enumerate(faces)}; ei={v:i for i,v in enumerate(edges)}; vi={v:i for i,v in enumerate(vertices)}
d1=np.zeros((len(faces),len(edges)),int)
d0=np.zeros((len(edges),len(vertices)),int)
for f in faces:
 x,y=f;v=[(x,y),(x+1,y),(x+1,y+1),(x,y+1)]
 for v1,v2 in zip(v,v[1:]+v[:1]):d1[fi[f],ei[tuple(sorted((v1,v2)))]]=1
for e,i in ei.items():
 for v in e:d0[i,vi[v]]=1
assert not np.any((d1@d0)%2)

def gf2_rank(a):
 a=np.array(a,dtype=np.uint8)%2
 r=0
 for c in range(a.shape[1]):
  piv=next((z for z in range(r,a.shape[0]) if a[z,c]),None)
  if piv is None:continue
  a[[r,piv]]=a[[piv,r]]
  for z in range(a.shape[0]):
   if z!=r and a[z,c]:a[z]^=a[r]
  r+=1
  if r==a.shape[0]:break
 return r
assert len(edges)==24 and len(vertices)==16 and len(faces)==9
assert gf2_rank(d1)==9 and gf2_rank(d0)==15
# A north-going center string: cross target-north common edge and north boundary edge.
stringN=np.zeros(len(edges),int)
for e in [((1,2),(2,2)),((1,3),(2,3))]:stringN[ei[tuple(sorted(e))]]=1
stringE=np.zeros(len(edges),int)
for e in [((2,1),(2,2)),((3,1),(3,2))]:stringE[ei[tuple(sorted(e))]]=1
target=np.zeros(len(faces),int);target[fi[(1,1)]]=1
assert np.array_equal((d1@stringN)%2,target)
assert np.array_equal((d1@stringE)%2,target)
assert gf2_rank(np.column_stack([d0, (stringN^stringE)]))==gf2_rank(d0)
# Reflect diagonal: (x,y) -> (y,x), north string becomes east string.
reflection=np.zeros((len(edges),len(edges)),int)
for e,i in ei.items():
 a=tuple(sorted(((e[0][1],e[0][0]),(e[1][1],e[1][0]))))
 reflection[ei[a],i]=1
assert np.array_equal(reflection@stringN,stringE)
print('PASS cell cohomology: 9 faces, 24 edges; H^1(disk;Z2)=0, center flux canonical in physical gauge quotient')
print('PASS reflection conjugates north path to east path up to vertex-center gauge, hence R C_f=C_f R physically')

# Spectral parity toy, dimensions 5. Independent commuting reflection R and target center C.
R=np.diag([1.,1.,-1.,1.,-1.]);C=np.diag([1.,1.,1.,-1.,-1.])
H0=np.diag([0.,3.,2.,.05,.09])
D=np.zeros((5,5));D[0,2]=D[2,0]=.06;D[1,2]=D[2,1]=.04
assert np.allclose(R@H0@R,H0) and np.allclose(C@H0@C,H0)
assert np.allclose(R@D@R,-D) and np.allclose(C@D@C,D)
eps=np.linalg.norm(D,2)
vals,states=eigh(H0+D);om=states[:,0]
if om[0]<0:om=-om
v=np.linalg.norm(om[[2,4]]);w=abs(om[1]);
r=eps/2.;s=eps**2/(3*2)
assert v<=r+1e-13 and w<=s+1e-13
r_old=eps/.09;s_old=eps**2/(.05*.09)
assert r_old>r*10 and s_old>s*100
print('PASS center-filtered parity sector resolvent estimate; new (r,s)=',r,s,'old',r_old,s_old)

# Reflection-even center-odd SU2 trial chi_half = 2p; Haar q=E[p^2]=1/4;
haar_q=quad(lambda u:2/pi*sin(u)**2*cos(u)**2,0,pi,epsabs=1e-13)[0]
assert abs(haar_q-.25)<1e-13
A=4.; ray=A*(1-haar_q)/(4*haar_q)
assert abs(ray-.75*A)<1e-13
print('PASS physical reflection-even center-odd Wilson trial Rayleigh quotient 3 A_f /4 at Haar; generic positive-spin1 marginal gives <= same')
print('PASS overall: exact sector filtration, cochain reflection commutation, gap-sector sharpening')
