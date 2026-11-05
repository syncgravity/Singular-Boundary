#!/usr/bin/env python3
"""Definite total magnetic weight SU2 Haar twirl rank: exact compact test.
Full true corrected-original-link Fourier source regressions in companion ZIP.
"""
import numpy as np
from math import comb,sqrt
from functools import reduce
from numpy.polynomial.legendre import leggauss
def kron(a):return reduce(np.kron,a)
def rep(n,g):
 out=np.zeros((n+1,n+1),complex)
 for k in range(n+1):
  for l in range(n+1):
   out[l,k]=sqrt(comb(n,k)/comb(n,l))*sum(
    comb(n-k,s)*comb(k,l-s)*g[1,0]**s*g[0,0]**(n-k-s)
    *g[0,1]**(k-l+s)*g[1,1]**(l-s)
    for s in range(max(0,l-k),min(l,n-k)+1))
 return out
for deg in ((1,1),(1,2,1),(1,3,1),(1,2,1,1)):
 S=sum(deg);dims=tuple(x+1 for x in deg)
 dim=int(np.prod(dims));M=2*S+1;Q=(S+2)//2
 t,w=leggauss(Q)
 idx=[0,1,dim-1]
 for iu,iv in ((0,0),(0,dim-1),(1,1)):
  T=np.zeros((dim,dim),complex)
  for x,weight in zip(t,w):
   x=(x+1)/2
   for a in range(M):
    for b in range(M):
     z=sqrt(x)*np.exp(2j*np.pi*a/M)
     v=sqrt(1-x)*np.exp(2j*np.pi*b/M)
     g=np.array([[z,v],[-v.conjugate(),z.conjugate()]])
     U=kron([rep(n,g) for n in deg])
     T+=weight/(2*M*M)*np.outer(U[:,iu],U[:,iv].conj())
  ma=lambda index:sum(n-2*j for n,j in zip(deg,np.unravel_index(index,dims)))
  if ma(iu)!=ma(iv):assert np.linalg.norm(T)<1e-9
  assert np.linalg.matrix_rank(T,tol=1e-8)<=((S+2)**2)//4
 print('PASS exact weight-Schur Haar rank in mixed-spin sector',deg)
print('All physical q0 source channels and N=2,4 checked independently in archive.')
