#!/usr/bin/env python3
"""Exact SU2 Wigner coefficient projector: mixed magnetic weights, no full multiplicity basis.
The larger independently verified test suite is in the Library companion archive.
"""
import numpy as np
from math import sqrt, comb
from functools import reduce
from numpy.polynomial.legendre import leggauss
from scipy.linalg import eigh

def rep(n,g):
 out=np.zeros((n+1,n+1),complex)
 for k in range(n+1):
  for l in range(n+1):
   for s in range(max(0,l-k),min(l,n-k)+1):
    out[l,k]+=sqrt(comb(n,k)/comb(n,l))*comb(n-k,s)*comb(k,l-s)*g[1,0]**s*g[0,0]**(n-k-s)*g[0,1]**(k-l+s)*g[1,1]**(l-s)
 return out

def wigner_gram(degrees,a,b,L):
 S=sum(degrees);ma=sum(n-2*k for n,k in zip(degrees,a));mb=sum(n-2*k for n,k in zip(degrees,b))
 if abs(ma)>L or abs(mb)>L or (L-ma)%2 or (L-mb)%2:return 0j
 M=Q=S+L+3
 t,w=leggauss(Q);t=(t+1)/2;w=w/2
 phases=np.exp(2j*np.pi*np.arange(M)/M)
 acc=0j
 for x,wx in zip(t,w):
  for p in phases:
   for q in phases:
    z=sqrt(x)*p;v=sqrt(1-x)*q
    g=np.array([[z,v],[-v.conjugate(),z.conjugate()]])
    y=np.conj(rep(L,g)[(L-ma)//2,(L-mb)//2])
    for n,i,j in zip(degrees,a,b):y*=rep(n,g)[i,j]
    acc+=wx*y/M**2
 return (L+1)*acc

# Two fundamental spins: explicit CG singlet/triplet projections.
assert abs(wigner_gram([1,1],[0,1],[1,0],0)+.5)<1e-10
assert abs(wigner_gram([1,1],[0,1],[1,0],2)-.5)<1e-10
# Cross-weight, mixed spin: these values separately checked via total Casimir.
assert abs(wigner_gram([1,2,1],[0,1,0],[1,0,0],2)+1/sqrt(8))<1e-10
assert abs(wigner_gram([1,3,1],[0,1,1],[1,0,0],3)+.4)<1e-10
print('PASS exact Haar Wigner coefficients, mixed weights and mixed-spin tensors')
print('Quadrature complexity polynomial in total degree, at fixed rank / inverse depth')
print('NO large-N physical Fourier inverse tail or high-spin asymptotic certified')
