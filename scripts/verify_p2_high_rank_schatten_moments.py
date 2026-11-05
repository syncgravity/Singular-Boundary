#!/usr/bin/env python3
"""Schatten moment certificate from tensor-local Gram matrices; no large Fourier matrix."""
from functools import reduce
import numpy as np
rng=np.random.default_rng(20261104)
def kron(z):return reduce(np.kron,z)
for nfaces in (2,3,4,5):
 for rank in (2,3,5,8,12):
  u=[[rng.normal(size=2)+1j*rng.normal(size=2) for _ in range(nfaces)] for _ in range(rank)]
  v=[[rng.normal(size=2)+1j*rng.normal(size=2) for _ in range(nfaces)] for _ in range(rank)]
  c=rng.normal(size=rank)+1j*rng.normal(size=rank)
  U=np.column_stack([c[i]*kron(u[i]) for i in range(rank)])
  V=np.column_stack([kron(v[i]) for i in range(rank)])
  A=np.array([[np.conj(c[i])*c[j]*np.prod([np.vdot(u[i][k],u[j][k]) for k in range(nfaces)]) for j in range(rank)] for i in range(rank)])
  B=np.array([[np.prod([np.vdot(v[i][k],v[j][k]) for k in range(nfaces)]) for j in range(rank)] for i in range(rank)])
  T2=np.trace(A@B).real
  T4=np.trace(A@B@A@B).real
  X=U@V.conj().T
  exact=np.linalg.norm(X,'nuc')
  lower=T2**1.5/np.sqrt(T4)
  assert abs(T2-np.linalg.norm(X,'fro')**2)<1e-7*max(1,T2)
  assert abs(T4-np.linalg.norm(X.conj().T@X,'fro')**2)<1e-7*max(1,T4)
  assert lower<=exact*(1+1e-8),(nfaces,rank,lower,exact)
print('PASS 20 complex tensor-Gram Schatten 2/4 moment certificates')
print('Full corrected original-link Gauss-invariant small matrices: companion ZIP')
print('No large N~m² asymptotic certified')
