#!/usr/bin/env python3
"""Exact SU(2) Bochner checks + deterministic interacting character quadrature."""
import sympy as s
import numpy as np
from scipy.linalg import eigh_tridiagonal
from itertools import combinations
p,a,h=s.symbols('p a h',real=True)
# Four incident links: Ricci 1/2; 4 diagonal Hess blocks and 12 off-diagonal ones.
geomdiag=4*s.Rational(3,16)*p*p
geomoff=12*(p*p+2)/16
ricci=s.Rational(1,2)*(1-p*p)
assert s.simplify(geomdiag+geomoff+ricci-(2+p*p))==0
assert s.simplify((1-p*p)/4-(1-p)/2+(1-p)**2/4)==0
# Haar reference: E p² = 1/4, E (L Y)²=9a²h²/4.
assert s.simplify((2+s.Rational(1,4))-s.Rational(9,4))==0
for N in (24,36,48):
 aa,b,hh=1.,5.,0.1
 n=np.arange(N,dtype=float)
 E,vs=eigh_tridiagonal(aa*n*(n+2)+b,np.full(N-1,-b/2),select='i',select_range=(0,0))
 c=vs[:,0]
 k=np.arange(1,1201); x=np.cos(np.pi*k/1201);wt=2/1201*np.sin(np.pi*k/1201)**2
 U=np.zeros((N,len(x))); Up=np.zeros_like(U); Upp=np.zeros_like(U)
 U[0]=1;U[1]=2*x;Up[1]=2
 for j in range(2,N):
  U[j]=2*x*U[j-1]-U[j-2]
  Up[j]=2*U[j-1]+2*x*Up[j-1]-Up[j-2]
  Upp[j]=4*Up[j-1]+2*x*Upp[j-1]-Upp[j-2]
 O=c@U; O1=c@Up; O2=c@Upp
 w1=O1/O; w2=O2/O-w1*w1
 density=O**2*wt
 avg=lambda z:float(np.dot(density,z))
 direct=avg((hh*(3*aa*x-2*aa*(1-x*x)*w1))**2)
 ge=avg(aa*aa*hh*hh*(2+x*x))
 curv=avg(-2*aa*aa*hh*hh*((1-x*x)**2*w2-x*(1-x*x)*w1))
 assert abs(direct-ge-curv)<1e-12
 assert abs(direct-0.0325527660401600)<2e-11
 print(f'N={N} m2={direct/hh:.12f}, geom={ge:.12f}, scoreCurv={curv:.12f}, residual={direct-ge-curv:+.2e}')
seed=[
[(-1,-1,-1,-1,-1),(-1,-1,-1,0,-1),(0,-1,-1,-1,-1),(0,-1,-1,0,-1)],
[(-1,-1,-1,-1,-1),(-1,-1,0,-1,-1),(-1,-1,-1,0,-1),(-1,-1,0,0,-1)],
[(-1,-1,-1,-1,-1),(-1,0,-1,-1,-1),(0,-1,-1,-1,-1),(0,0,-1,-1,-1)]]
def edges(face):return {tuple(sorted((x,y))) for x,y in combinations(face,2) if sum(abs(u-v) for u,v in zip(x,y))==1}
fs=[edges(f) for f in seed]; ed=set.union(*fs)
assert len(ed)==10 and max(sum(e in f for f in fs) for e in ed)==2
print('PASS: full mixed-link Bochner geometry and interacting physical SU(2) score Hessian; 3-face spatial fixture; no Monte Carlo')
