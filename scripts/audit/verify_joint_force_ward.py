#!/usr/bin/env python3
"""Deterministic interacting SU2 physical Wilson joint-force Ward check."""
import numpy as np
from scipy.linalg import eigh_tridiagonal
from numpy.polynomial.chebyshev import chebgauss
a,b,h,N=1.,5.,.1,36
n=np.arange(N,dtype=float)
E,c=eigh_tridiagonal(a*n*(n+2)+b,np.full(N-1,-b/2),select='i',select_range=(0,0))
c=c[:,0]
k=np.arange(1,601)
p=np.cos(np.pi*k/601)
wt=2/601*np.sin(np.pi*k/601)**2
U=np.zeros((N,len(p)));Up=np.zeros_like(U);U[0]=1;U[1]=2*p;Up[1]=2
for j in range(2,N):
 U[j]=2*p*U[j-1]-U[j-2]
 Up[j]=2*U[j-1]+2*p*Up[j-1]-Up[j-2]
O=c@U;dO=c@Up;prob=O*O*wt
avg=lambda x:np.dot(prob,x)
D=3*a*h*p
F=-2*a*h*(1-p*p)*dO/O
grad=-3*a*a*h*h*(1-p*p)
L=D+F
assert abs(avg(L))<1e-10
assert abs(avg(D*F)+avg(D*D)+avg(grad))<1e-10
assert abs((avg(L*L)-avg(F*F)+avg(D*D)+2*avg(grad))/h)<1e-10
print("PASS SU2 interacting Haar-character joint-force Ward identity; no Monte Carlo")
