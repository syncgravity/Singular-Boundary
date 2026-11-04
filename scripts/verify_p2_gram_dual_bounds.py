#!/usr/bin/env python3
"""Gram-only Schatten dual certificate checks; no Fourier-sized matrices needed."""
import numpy as np
from functools import reduce
from math import sqrt
rng=np.random.default_rng(20261104)
def kron(a):return reduce(np.kron,a)
for N in (2,3,4,5):
 for rank in (2,3,5,8,12):
  u=[[rng.normal(size=2)+1j*rng.normal(size=2) for _ in range(N)] for _ in range(rank)]
  v=[[rng.normal(size=2)+1j*rng.normal(size=2) for _ in range(N)] for _ in range(rank)]
  c=rng.normal(size=rank)+1j*rng.normal(size=rank)
  U=np.column_stack([c[i]*kron(u[i]) for i in range(rank)])
  V=np.column_stack([kron(v[i]) for i in range(rank)])
  A=np.array([[np.conj(c[i])*c[j]*np.prod([np.vdot(u[i][k],u[j][k]) for k in range(N)]) for j in range(rank)] for i in range(rank)])
  B=np.array([[np.prod([np.vdot(v[i][k],v[j][k]) for k in range(N)]) for j in range(rank)] for i in range(rank)])
  T=np.trace(A@B).real
  bound=sqrt(np.linalg.eigvalsh(A)[-1]*np.linalg.eigvalsh(B)[-1])
  lo=T/bound;hi=sqrt(rank*T)
  X=U@V.conj().T
  exact=np.linalg.norm(X,'nuc')
  assert lo<=exact*(1+1e-9)<=hi*(1+1e-9)
print("PASS 20 arbitrary complex Gram trace-norm dual lower and rank upper bounds")
print("Use certified inverse error Delta_q to bracket full physical response.")
