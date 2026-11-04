#!/usr/bin/env python3
"""Independent finite regressions for the exact restricted three-spin family theorem.
The full original-link quaternion and Fourier matrix-superoperator verifiers,
logs and SHA-256 manifest are in the companion conversation ZIP.
Not a proof of unrestricted tame closure or Yang–Mills mass gap.
"""
from itertools import product
from math import sqrt
import sympy as sp
x=sp.symbols('x')
def channel(q,r):return range(abs(q-r),q+r+1,2)
def alpha_t(q,r,l):
 Q=q*(q+2);R=r*(r+2);L=l*(l+2)
 return sp.Rational(Q+R-L,2),(sp.Rational(L+R-Q,2*L) if l else sp.S(0))
for q,r in product(range(1,11),repeat=2):
 U=lambda k:sp.chebyshevu(k,x)
 assert sp.expand(U(q)*U(r)-sum((U(l) for l in channel(q,r)),sp.S(0)))==0
 assert sp.expand(U(q)*sp.diff(U(r),x)-sum((alpha_t(q,r,l)[1]*sp.diff(U(l),x) for l in channel(q,r) if l),sp.S(0)))==0
 assert sp.expand((1-x*x)*sp.diff(U(q),x)*sp.diff(U(r),x)-sum((alpha_t(q,r,l)[0]*U(l) for l in channel(q,r)),sp.S(0)))==0
print("PASS: 100 exact SU(2) character product, derivative and carré-du-champ identities")
for p,q,r in product(range(1,21),repeat=3):
 P=p*(p+2);ans=0.
 for l in channel(q,r):
  L=l*(l+2);b=P+L+3;S=(sqrt(P*L)+sqrt(3*L))/4
  alpha,t=alpha_t(q,r,l)
  X=(abs(float(alpha))+abs(float(t))*S)/(b-2*S)
  ans+=((l+1)/(q+1))**2*((1+max(p,l))/(1+max(p,q)))*X
 ans/=(r+1)**3
 assert ans<=16/(1+min(q,r))**2+1e-10,(p,q,r,ans)
print("PASS: 8000 three-spin scalar trace-norm majorant regressions")
print("All-degree claim requires the analytic proof in the corresponding audit, not finite checks.")
