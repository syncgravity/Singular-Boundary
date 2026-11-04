#!/usr/bin/env python3
"""Schatten full-inverse Rayleigh dual: actual corrected SU(2) link superoperators.
The complete Gauss-twirled summed response regression and exact one-Haar
tensor module are in the independently executed companion audit ZIP.
"""
import numpy as np
from functools import reduce
from math import sqrt
rng=np.random.default_rng(20261104)
def spin(n):
 j=n/2;m=np.arange(j,-j-1,-1);up=np.zeros((n+1,n+1),complex)
 for k in range(n):
  a=m[k+1];up[k,k+1]=sqrt((j-a)*(j+a+1))
 return ((up+up.conj().T)/2,(up-up.conj().T)/(2j),np.diag(m).astype(complex))
def kron(z):return reduce(np.kron,z)
for degrees in ((1,1),(1,2,1),(1,3,1,1),(1,4,1)):
 J=[[kron([a if i==j else np.eye(degrees[i]+1) for i in range(len(degrees))]) for a in spin(degrees[j])] for j in range(len(degrees))]
 D=sum(n*(n+2) for n in degrees)
 e=[n*(n+2) for n in degrees]
 alpha=sum(sqrt(e[i]*e[i+1]) for i in range(len(e)-1))/(2*D)
 assert alpha<=.5
 def H(Y):
  return -2*sum((J[i][a]@Y@J[i+1][a] for i in range(len(J)-1) for a in range(3)),np.zeros_like(Y))
 dim=J[0][0].shape[0]
 Y=rng.normal(size=(dim,dim))+1j*rng.normal(size=(dim,dim))
 X=np.zeros_like(Y);step=Y/D
 for _ in range(120):
  X+=step;step=-H(step)/D
  if np.linalg.norm(step,'fro')<1e-13:break
 assert np.linalg.norm(D*X+H(X)-Y,'fro')<1e-10
 z=np.linalg.norm(Y,2)
 dual=np.vdot(Y,X).real/z
 lower=np.linalg.norm(Y,'fro')**2/(D*(1+alpha)*z)
 assert lower<=dual*(1+1e-9)<=np.linalg.norm(X,'nuc')*(1+1e-9)
 print("PASS full physical K inverse Rayleigh nuclear dual",degrees,"lower",round(lower,8))
print("NOTE: actual Gauss-twirled full extensive source regression in companion ZIP.")
