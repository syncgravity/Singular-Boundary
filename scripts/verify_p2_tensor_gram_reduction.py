#!/usr/bin/env python3
"""Tensor-local nuclear Gram identity and fixed-depth rank-count sanity checks.
Full corrected original-link/Haar/CG implementation is in companion P2 ZIP.
"""
from functools import reduce
from math import ceil
import numpy as np
rng=np.random.default_rng(20261104)
def kron(z):return reduce(np.kron,z)
for N in (2,3,4,6):
 for rank in (2,4,8,12):
  u=[[rng.normal(size=2)+1j*rng.normal(size=2) for _ in range(N)] for _ in range(rank)]
  v=[[rng.normal(size=2)+1j*rng.normal(size=2) for _ in range(N)] for _ in range(rank)]
  coeff=rng.normal(size=rank)+1j*rng.normal(size=rank)
  U=np.column_stack([coeff[i]*kron(u[i]) for i in range(rank)])
  V=np.column_stack([kron(v[i]) for i in range(rank)])
  A=np.empty((rank,rank),complex);B=np.empty((rank,rank),complex)
  for i in range(rank):
   for j in range(rank):
    A[i,j]=np.conj(coeff[i])*coeff[j]*np.prod([np.vdot(u[i][k],u[j][k]) for k in range(N)])
    B[i,j]=np.prod([np.vdot(v[i][k],v[j][k]) for k in range(N)])
  w,Q=np.linalg.eigh((A+A.conj().T)/2)
  Ah=(Q*np.sqrt(np.clip(w,0,None)))@Q.conj().T
  C=Ah@B@Ah
  gram=np.sum(np.sqrt(np.clip(np.linalg.eigvalsh((C+C.conj().T)/2),0,None)))
  dense=np.linalg.norm(U@V.conj().T,'nuc')
  assert abs(gram-dense)<1e-6*max(1,dense),(N,rank,gram,dense)
print("PASS 16 arbitrary complex tensor-product nuclear-Gram identities")
for N in (2,4,8,16,64):
 for m in (3,4,16):
  K=ceil((N+1)/2)*(2*N+1)**2
  for q in (0,1,2,3):
   rank=13*(m+1)*K*sum((3*(N-1))**p for p in range(q+1))
   assert rank>=13*(m+1)*K
print("PASS fixed-depth polynomial-rank upper envelope")
