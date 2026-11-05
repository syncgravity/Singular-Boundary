#!/usr/bin/env python3
"""P-68: twice differentiable protected positive-energy time kernel and Taylor envelope.
Finite SU2 class-character Jacobi regression; thermodynamic claim is analytic.
"""
import numpy as np
from scipy.linalg import eigh
for lam in (.25,1.,2.,4.):
 for dim in (20,40,80):
  n=np.arange(dim);H=np.diag((n*(n+2)).astype(float))
  for j in range(dim-1):H[j,j+1]=H[j+1,j]=-lam/2
  E,U=eigh(H);w=E-E[0];psi=U[:,0]
  F=np.diag((n<=3).astype(float))
  G=np.diag((n%3==0).astype(float))
  f=U.conj().T@F@psi;g=U.conj().T@G@psi
  m1=np.vdot(f,w*g);m2=np.vdot(f,w*w*g)
  LF=np.linalg.norm((H@F-F@H)@psi)
  LG=np.linalg.norm((H@G-G@H)@psi)
  assert LF<=2*lam+1e-9 and LG<=2*lam+1e-9
  assert abs(m2)<=LF*LG+1e-9
  def C(t):return np.vdot(f,np.exp(-1j*t*w)*g)
  for t in (.001,.025,.1,.5,1.):
   assert abs(C(t)-C(0)+1j*t*m1)<=t*t*LF*LG/2+1e-9
 print('PASS corrected SU2 oneface protected C2 kernels lambda=',lam)
print('Second derivative exists from positive spectral second moment, not identified with local delta^2.')
print('No common infinite-volume interacting dynamics or gap asserted.')
