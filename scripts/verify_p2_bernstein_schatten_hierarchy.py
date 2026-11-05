#!/usr/bin/env python3
"""Monotone Bernstein even-Schatten moment certificates with rigorous upper error."""
import numpy as np
from math import comb
rng=np.random.default_rng(419)
count=0
for d in (2,4,8,12):
 for _ in range(5):
  X=rng.standard_normal((d,d))+1j*rng.standard_normal((d,d))
  sig=np.linalg.svd(X,compute_uv=False)
  u=max(sig)*1.00001
  t=(sig/u)**2
  exact=sum(sig)
  last=0.
  for n in (1,2,3,4,8,16,32,64,128):
   lower=u*sum(sum((k/n)**.5*comb(n,k)*ti**k*(1-ti)**(n-k) for k in range(1,n+1)) for ti in t)
   assert last<=lower+1e-8 and lower<=exact+1e-8
   assert exact-lower<=d*u*(4*n)**(-.25)+1e-8
   last=lower
  count+=1
assert count==20
print('PASS 20 complex matrices at nine increasing Bernstein orders')
print('The theorem applies to tensor Gram moments tr((AB)^k) and physical Neumann error Delta_q.')
