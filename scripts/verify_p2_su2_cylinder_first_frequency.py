#!/usr/bin/env python3
"""P-78: actual SU2 Gauss-invariant one-face Jacobi χ1 cylinder first frequency:
Ground-state kinetic Dirichlet Γ(χ1,χ1)=4−χ1²; no continuum gap claim.
"""
import numpy as np
from scipy.linalg import eigh
for lam in (0.,.25,1.,2.,4.,10.):
 for d in (12,24,48,96):
  n=np.arange(d,dtype=float)
  K=np.diag(n*(n+2))
  f=np.zeros((d,d))
  for i in range(d-1):f[i,i+1]=f[i+1,i]=1.
  H=K-lam*f/2
  E,U=eigh(H)
  psi=U[:,0];v=f@psi
  excitation=np.vdot(v,(H-E[0]*np.eye(d))@v).real
  dirichlet=4-np.linalg.norm(f@psi)**2
  assert abs(excitation-dirichlet)<1e-8,(lam,d,excitation,dirichlet)
  assert 0<=excitation<=4+1e-8
  spectral=U.conj().T@v;freq=E-E[0]
  moment1=np.dot(np.abs(spectral)**2,freq)
  moment2=np.dot(np.abs(spectral)**2,freq**2)
  comm=(H@f-f@H)@psi
  assert abs(moment1-excitation)<1e-8
  assert abs(moment2-np.linalg.norm(comm)**2)<1e-7
  if lam==0:assert abs(moment1-3)<1e-9
 if True:print('PASS corrected oneface SU2 lambda',lam,'Dirichlet first moment',excitation)
print('These finite tests support the local identity, not an infinite-volume all-time dynamics or gap.')
