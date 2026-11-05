#!/usr/bin/env python3
"""Actual SU2 one-face positive-frequency FIRST-moment local commutator sum rule.
Numerical regression only; all-N thermodynamic limit proven in P-66 audit.
"""
import numpy as np
from scipy.linalg import eigh
for lam in (.25,1.,2.,4.):
 for d in (16,32,64):
  n=np.arange(d)
  H=np.diag((n*(n+2)).astype(float))
  for k in range(d-1):H[k,k+1]=H[k+1,k]=-lam/2
  E,U=eigh(H);ground=U[:,0];frequencies=E-E[0]
  F=np.diag((n<=2).astype(float));G=np.diag((n%3==0).astype(float))
  fv=U.conj().T@F@ground;gv=U.conj().T@G@ground
  moment=np.vdot(fv,frequencies*gv)
  local=np.vdot(F@ground,(H@G-G@H)@ground)
  assert abs(moment-local)<1e-9
  t=1e-5
  C=lambda z:np.vdot(fv,np.exp(-1j*z*frequencies)*gv)
  assert abs((C(t)-C(-t))/(2*t)+1j*local)<1e-7
  assert frequencies.min()>=-1e-10
  print('PASS actual SU2 local commutator first-frequency identity',lam,d)
print('Thermodynamic theorem uses uniform second moments and trace-norm convergence.')
print('NOT an interacting infinite-volume automorphism or positive mass gap.')
