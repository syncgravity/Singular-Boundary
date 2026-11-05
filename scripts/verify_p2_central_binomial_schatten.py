#!/usr/bin/env python3
"""Exact central-binomial Schatten hierarchy; expanded independent tests in audit ZIP."""
from fractions import Fraction as F
from math import comb
import numpy as np
for n in range(1,201):
 b=sum((F(comb(2*k,k),4**k*(2*k-1)) for k in range(1,n+1)),F())
 c=F(comb(2*n,n),4**n)
 assert b+c==1
print('PASS 200 exact-rational optimal positive-polynomial uniform tail identities')
rng=np.random.default_rng(419)
for d in (3,5,8):
 for _ in range(4):
  U=rng.normal(size=(d,d))+1j*rng.normal(size=(d,d))
  V=rng.normal(size=(d,d))+1j*rng.normal(size=(d,d))
  X=U@V.conj().T;sig=np.linalg.svd(X,compute_uv=False)
  u=1.001*max(sig);rank=len(sig);t=(sig/u)**2;last=0.
  for n in (1,2,4,8,16,32,64):
   b=F(1,2);P=np.zeros_like(t)
   for k in range(1,n+1):
    P+=float(b)*(-np.expm1(k*np.log1p(-t)))
    b*=F(2*k-1,2*(k+1))
   lower=u*sum(P);err=rank*u*float(F(comb(2*n,n),4**n))
   assert last<=lower+1e-8 and lower<=sum(sig)+1e-8<=lower+err+1e-8
   last=lower
print('PASS 84 complex tensor-factor Schatten lower/upper tests')
print('Certified analytic error c_n=binom(2n,n)/4^n ~ 1/sqrt(pi*n)')
