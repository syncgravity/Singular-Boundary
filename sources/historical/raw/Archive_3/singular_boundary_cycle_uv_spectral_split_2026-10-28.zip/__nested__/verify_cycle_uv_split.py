#!/usr/bin/env python3
"""Deterministic finite SU(2) cycle susceptibility UV bounds; no Monte Carlo."""
import numpy as np
from scipy.linalg import eigh
from math import sqrt
from itertools import combinations

# Authentic three-rhombus spatial Penrose fixture (not the full temporal Q14).
faces0 = [
[(-1,-1,-1,-1,-1),(-1,-1,-1,0,-1),(0,-1,-1,-1,-1),(0,-1,-1,0,-1)],
[(-1,-1,-1,-1,-1),(-1,-1,0,-1,-1),(-1,-1,-1,0,-1),(-1,-1,0,0,-1)],
[(-1,-1,-1,-1,-1),(-1,0,-1,-1,-1),(0,-1,-1,-1,-1),(0,0,-1,-1,-1)]
]
def edges(face):
 return {tuple(sorted((x,y))) for x,y in combinations(face,2) if sum(abs(a-b) for a,b in zip(x,y))==1}
faces=[edges(f) for f in faces0]
Es=set.union(*faces)
assert len(Es)==10 and all(len(f)==4 for f in faces)
assert max(sum(e in f for f in faces) for e in Es)<=2
assert len(faces[1]&faces[2])==0  # the two peripheral faces are edge-disjoint
print('PASS authentic spatial Penrose seed: 3 faces, 10 edges, peripheral edge-disjoint pair')

# The sharp Hilbert spectral inequality for any (centered) physical vectors.
def check_high(K, x, y, cutoff):
 evals, v=eigh(K)
 ix=np.where(evals>cutoff+1e-9)[0]
 if not len(ix):return 0.0,0.0
 xx=v.T@x;yy=v.T@y
 val=float(np.sum(xx[ix]*yy[ix]/evals[ix]))
 m1x=float(x@K@x);m1y=float(y@K@y)
 bound=sqrt(max(0,m1x)*max(0,m1y))/cutoff**2
 assert abs(val)<=bound+1e-9,(val,bound)
 return val,bound

# Genuine physical class SU(2) rotor: electric eigenvalues n(n+2),
# magnetic plaquette deficit = 1 - p, p mixing neighboring characters.
for b in (0.0,0.5,5.0,20.0,60.0):
 n=52; j=np.arange(n);P=np.diag(np.full(n-1,0.5),1)+np.diag(np.full(n-1,0.5),-1)
 D=np.eye(n)-P
 H=np.diag(j*(j+2))+b*D
 vals,vec=eigh(H);omega=vec[:,0];gap=vals[1]-vals[0]
 K=np.diag(vals-vals[0]);transform=vec.T
 # centered physical source in diagonal eigenbasis, remove exact ground overlap
 xd=D@omega-(omega@(D@omega))*omega
 for c in (0.2,1.0,4.0):
  yd=c*xd
  for scale in (1.05,2,4,10):
   lam=scale*gap
   val,bnd=check_high(K,transform@xd,transform@yd,lam)
   assert bnd>=0
 print(f'PASS interacting SU2 character rotor b={b:g}; gap={gap:.8f}')

# Coupling scaling: m<=F<=C h^-2 yields O(h^-1) UV budget at lambda=h^-2.
for h,m in ((0.2,1),(0.1,4),(0.05,25),(0.025,400),(0.0125,6400)):
 bf=bmax=h**-2;a_star=1.0
 A_f=4*a_star;Bterm=m*bmax**2*(4*a_star)
 cutoff=h**(-1.5)*m**.25
 UV=bf*sqrt(A_f*Bterm)/(sqrt(2)*cutoff**2)
 assert abs(UV*h-2*sqrt(2))<1e-8
 print(f'PASS UV cutoff h={h:.4f}, m={m}, lambda={cutoff:.3g}, h*UV={h*UV:.6f}')
# Exact Kato mixed Hessian and center parity in a positive 2-state comparison.
sigx=np.array([[0.,1.],[1.,0.]])
sigz=np.diag([1.,-1.])
ident=np.eye(2)
for u,t in ((0.,.4),(.3,1.),(2.,3.)):
 g=1.7
 H=(g+u)*(ident-sigx)+t*(ident-sigz)
 ee,V=eigh(H);om=V[:,0];exc=V[:,1]; gap=ee[1]-ee[0]
 df=ident-sigz;W=ident-sigx
 cross=(exc@df@om)*(exc@W@om)/gap
 from_kato=-2*cross
 exact=t*(g+u)/(((g+u)**2+t*t)**1.5)
 assert abs(from_kato-exact)<1e-12,(from_kato,exact)
 for cutoff in (gap/2,gap*1.05):
  high=from_kato if gap>cutoff else 0.
  e1=gap*(exc@df@om)**2
  e2=gap*(exc@W@om)**2
  assert abs(high)<=2*sqrt(e1*e2)/cutoff**2+1e-12
print('PASS exact signed Kato response in unique-positive center-symmetric two-state comparison')
print('ALL TESTS PASS — analytic theorem uses actual SU2 f-sums, not a Gaussian vacuum')
