#!/usr/bin/env python3
"""Deterministic exact SU2 Wilson-angle inequalities and physical spectral-band audit."""
import math
import numpy as np
import sympy as s
from scipy.linalg import eigh_tridiagonal
c=math.pi**2/4-1
for x in np.linspace(0,math.pi,2001):
 d=1-math.cos(x);r=x*x/2-d
 assert -1e-11<=r<=c*d+1e-11
 assert r<=math.pi**4*d*d/96+1e-11
h,R,eta,beta,cf,ce=s.symbols('h R eta beta cf ce',positive=True)
assert s.simplify((2*c*c/beta)*(cf*R**2/h**2)*h**3*(ce*(R**2+R)/h**3+eta)-(2*c*c*cf/beta)*(ce*(R**4+R**3)/h**2+eta*R**2*h))==0
for h0 in (.2,.1,.05):
 b=h0**-2;n=70
 en,U=eigh_tridiagonal(np.arange(n)*(np.arange(n)+2)+b,np.full(n-1,-b/2))
 P=U[:,:3];eta0=en[2]-en[0]
 j=np.arange(1,1602);p=np.cos(np.pi*j/1602);w=2/1602*np.sin(np.pi*j/1602)**2
 C=np.zeros((n,len(p)));C[0]=1;C[1]=2*p
 for k in range(2,n):C[k]=2*p*C[k-1]-C[k-2]
 r=np.arccos(p)**2/2-(1-p)
 V=C.T@P
 val=np.linalg.eigvalsh((V.T*(w*h0*r*r))@V)[-1]
 assert val<=2*c*c*h0**3*(en[0]+eta0+1e-7)
print("PASS: global angle bounds and interacting physical SU2 spectral-band tests")
