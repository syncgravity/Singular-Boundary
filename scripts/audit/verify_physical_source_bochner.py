#!/usr/bin/env python3
"""Exact SU(2) full mixed-link Bochner identity and interacting one-face benchmark."""
import sympy as s
import numpy as np
from scipy.linalg import eigh_tridiagonal
p=s.symbols('p',real=True)
assert s.simplify(4*s.Rational(3,16)*p*p+12*(p*p+2)/16+s.Rational(1,2)*(1-p*p)-(2+p*p))==0
for N in (24,36,48):
 n=np.arange(N,dtype=float); E,vs=eigh_tridiagonal(n*(n+2)+5,np.full(N-1,-2.5),select='i',select_range=(0,0)); c=vs[:,0]
 k=np.arange(1,1201); x=np.cos(np.pi*k/1201);wt=2/1201*np.sin(np.pi*k/1201)**2
 U=np.zeros((N,len(x)));P=np.zeros_like(U);Q=np.zeros_like(U)
 U[0]=1;U[1]=2*x;P[1]=2
 for j in range(2,N):
  U[j]=2*x*U[j-1]-U[j-2];P[j]=2*U[j-1]+2*x*P[j-1]-P[j-2];Q[j]=4*P[j-1]+2*x*Q[j-1]-Q[j-2]
 o=c@U;v=(c@P)/o;v2=(c@Q)/o-v*v
 average=lambda z:float(np.dot(o*o*wt,z))
 lhs=average((.1*(3*x-2*(1-x*x)*v))**2)
 geom=average(.01*(2+x*x))
 curv=average(-.02*((1-x*x)**2*v2-x*(1-x*x)*v))
 assert abs(lhs-geom-curv)<1e-12
 print(N,lhs,geom,curv)
print("PASS; no Monte Carlo")
