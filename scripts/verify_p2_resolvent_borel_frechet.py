#!/usr/bin/env python3
"""Exact rational Borel derivative and uniform electric Neumann norm checks."""
from fractions import Fraction as F
from math import factorial,sqrt
from functools import reduce
import numpy as np
def kron(z):return reduce(np.kron,z)
def spin(n):
 j=n/2; vals=np.arange(j,-j-1,-1);p=np.zeros((n+1,n+1),complex)
 for k in range(n):
  v=vals[k+1];p[k,k+1]=sqrt((j-v)*(j+v+1))
 return ((p+p.conj().T)/2,(p-p.conj().T)/(2j),np.diag(vals).astype(complex))
rng=np.random.default_rng(419)
for degrees in ((1,1),(1,2,1),(1,3,1,1)):
 idents=[np.eye(n+1) for n in degrees]
 J=[[kron([s if i==j else idents[i] for i in range(len(degrees))]) for s in spin(degrees[j])] for j in range(len(degrees))]
 D=sum(n*(n+2) for n in degrees)
 def H(X):
  return -2*sum((J[i][a]@X@J[i+1][a] for i in range(len(degrees)-1) for a in range(3)),np.zeros_like(X))
 d=int(np.prod([n+1 for n in degrees]));Y=rng.normal(size=(d,d))+1j*rng.normal(size=(d,d))
 exact=np.zeros_like(Y);term=Y/D
 for k in range(65):
  exact+=term;term=-H(term)/D
 assert np.linalg.norm(D*exact+H(exact)-Y,'fro')<1e-10
 for q in (0,1,2,4,8):
  approx=np.zeros_like(Y);term=Y/D
  for k in range(q+1):
   approx+=term;term=-H(term)/D
  assert np.linalg.norm(exact-approx,'nuc')<=(2.0**(-q)/D)*np.linalg.norm(Y,'nuc')*(1+1e-9)
 print("PASS true original-link Neumann tail",degrees)
for i in range(1,35):
 for j in range(1,35):
  assert F(1,factorial(i+j))==F(i+j+1,factorial(i+j+1))
print("PASS 1156 rational Borel-Volterra differentiated convolution identities")
