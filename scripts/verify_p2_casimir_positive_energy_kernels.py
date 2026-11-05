#!/usr/bin/env python3
"""Actual one-face SU2 Casimir-regular positive energy spectral correlation checks.
Finite numerical tests do not prove an interacting infinite-volume automorphism or gap.
"""
import numpy as np
from scipy.linalg import eigh
for lam in (.25,1.,2.,4.):
 for dim in (12,24,48):
  n=np.arange(dim)
  H=np.diag((n*(n+2)).astype(float))
  for k in range(dim-1):H[k,k+1]=H[k+1,k]=-lam/2
  e,U=eigh(H);psi=U[:,0];w=e-e[0]
  F=[np.diag((n<=k).astype(float)) for k in (0,1,3,6)]
  V=np.column_stack([U.conj().T@f@psi for f in F])
  assert min(w)>-1e-8
  for j,f in enumerate(F):
   com=H@f-f@H
   assert abs(np.dot(w*w,np.abs(V[:,j])**2)-np.linalg.norm(com@psi)**2)<1e-8
   assert np.linalg.norm(com@psi)<=2*lam+1e-10
  for t in (.001,.02,.5,1.5):
   C=(V.conj().T*np.exp(-1j*w*t))@V
   C0=V.conj().T@V
   assert np.max(abs(C-C0))<=2*lam*t+1e-8
   for k in range(dim):
    B=np.outer(V[k,:].conj(),V[k,:])
    assert np.linalg.eigvalsh(B).min()>-1e-8
 print('PASS actual SU2 oneface positive-energy Casimir spectral kernels lambda',lam)
print('Nonzero uniform gap, interacting infinite-volume dynamics and generator core remain open.')
