#!/usr/bin/env python3
"""Proposed directed Z5-family event word reflection test; not source band generator."""
import numpy as np
rng=np.random.default_rng(20261107)
K=np.sin(2*np.pi*(np.arange(5)[None,:]-np.arange(5)[:,None])/5)
assert np.allclose(K,-K.T)
def chi(b):
 return np.einsum('tj,jk,tk->',b,K,np.roll(b,-1,axis=0))/len(b)
checks=1
for _ in range(1000):
 b=rng.integers(0,2,(13,5))
 mir=b[:,(-np.arange(5))%5]
 rev=b[(-np.arange(13))%13]
 assert abs(chi(b)+chi(mir))<1e-12;checks+=1
 assert abs(chi(b)+chi(rev))<1e-12;checks+=1
 assert abs((chi(b)+chi(mir))/2)<1e-12;checks+=1
 assert abs((chi(b)-chi(mir))/2-chi(b))<1e-12;checks+=1
assert checks==4001
print("PASS",checks,"symbolic five-family encounter parity checks; authentic Z5 paths not recovered")
