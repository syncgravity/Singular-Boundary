#!/usr/bin/env python3
"""P-70 protected spectral second moment = local interacting commutator quadratic form.
Tests include fourth-moment tightness. No infinite-volume automorphism inferred.
"""
import numpy as np
from scipy.linalg import eigh
for lam in (.25,1.,2.,4.):
 for d in (16,32,64,128):
  n=np.arange(d);H=np.diag((n*(n+2)).astype(float))
  for k in range(d-1):H[k,k+1]=H[k+1,k]=-lam/2
  e,U=eigh(H);exc=e-e[0];psi=U[:,0]
  F=np.diag((n<=2).astype(float));G=np.diag((n==2).astype(float))
  f=U.conj().T@F@psi;g=U.conj().T@G@psi
  DF=H@F-F@H;DG=H@G-G@H
  moment=np.vdot(f,(exc**2)*g)
  comm=np.vdot(DF@psi,DG@psi)
  assert abs(moment-comm)<1e-9
  fourth=float(np.dot(np.abs(f)**2,exc**4))
  D2=H@DF-DF@H
  assert abs(fourth-np.linalg.norm(D2@psi)**2)<1e-7
  for cutoff in (2,4,8,16):
   tail=float(np.sum((exc>cutoff)*exc**2*np.abs(f)**2))
   assert tail<=fourth/cutoff**2+1e-8
  t=1e-4;C=lambda z:np.vdot(f,np.exp(-1j*z*exc)*g)
  assert abs((C(t)-2*C(0)+C(-t))/(t*t)+comm)<2e-5
  print('PASS lambda',lam,'size',d,'exact E2 form',comm.real,'E4',fourth)
print('Uniform E4 on finite Casimir core + local kinetic bound, not E2 alone, ensures limiting moment equality.')
print('No claim of interacting infinite-volume group, gap or 4D Yang-Mills mass gap.')
