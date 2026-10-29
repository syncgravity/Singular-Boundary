#!/usr/bin/env python3
"""Deterministic exact algebra and nonlinear physical SU2 rotor, no Monte Carlo."""
import sympy as s
import numpy as np
from scipy.linalg import eigh_tridiagonal
p,a,b=s.symbols("p a b",positive=True)
C={1:2*a*(1-p*p),0:-3*a*p}
T={2:-a*(1-p*p),1:3*a*p}
def prod(A,B):
 r={}
 for i,x in A.items():
  for j,y in B.items():
   for k in range(i+1):
    key=i+j-k;r[key]=r.get(key,0)+x*s.binomial(i,k)*s.diff(y,p,k)
 return r
def comm(A,B):
 x,y=prod(A,B),prod(B,A)
 return {k:s.factor(x.get(k,0)-y.get(k,0)) for k in set(x)|set(y) if s.simplify(x.get(k,0)-y.get(k,0))!=0}
m=comm(C,comm(T,C))
assert s.simplify(m[0]+6*a**3*(5*p*p+1))==0
assert s.simplify(m[2]-8*a**3*(1-p**4))==0
assert s.simplify(m[1]-s.diff(m[2],p)+p/(1-p*p)*m[2])==0
assert s.simplify(comm(C,comm({0:b*(1-p)},C))[0]+8*a*a*b*p*(1-p*p))==0
for h in (.2,.1,.05,.025):
 B=4/h**2;N=120;j=np.arange(N)
 evals,vec=eigh_tridiagonal(j*(j+2)+B,np.full(N-1,-B/2),select='i',select_range=(0,0))
 o=vec[:,0];P=np.diag(np.full(N-1,.5),1)+np.diag(np.full(N-1,.5),-1);d=np.eye(N)-P
 mu=o@d@o;var=o@d@d@o-mu**2
 assert mu<=3*np.sqrt(2/B)+1e-8 and var<=18.5/B+1e-8
 assert var>9/(512*626)/B
 print("h",h,"variance(d)/h²",var/h**2)
print("PASS exact interacting SU2 commutator and physical rotor moment bounds")
