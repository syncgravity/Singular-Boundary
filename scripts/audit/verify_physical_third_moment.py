#!/usr/bin/env python3
"""Exact deterministic SU(2) physical third-spectral-moment commutator checker."""
import sympy as s
import numpy as np
from scipy.linalg import eigh_tridiagonal
for N in [24,48]:
 n=np.arange(N,dtype=float); P=np.diag(np.full(N-1,.5),1)+np.diag(np.full(N-1,.5),-1)
 for b in [0.,.5,5.,20.]:
  H=np.diag(n*(n+2)+b)-b*P; E,V=eigh_tridiagonal(np.diag(H),np.diag(H,1),select='i',select_range=(0,0));omega=V[:,0]
  Y=.1*(np.eye(N)-P);K=H-E[0]*np.eye(N);Z=Y@omega-(omega@Y@omega)*omega
  C=H@Y-Y@H
  m3=Z@K@K@K@Z
  via=-.5*omega@(C@(H@C-C@H)-(H@C-C@H)@C)@omega
  m3V=-.5*omega@(C@((b*(np.eye(N)-P))@C-C@(b*(np.eye(N)-P)))-((b*(np.eye(N)-P))@C-C@(b*(np.eye(N)-P)))@C)@omega
  expected=4*b*.1**2*(omega@P@omega-omega@P@P@P@omega)
  assert abs(m3-via)<1e-8 and abs(expected-m3V)<1e-8
  m1=Z@K@Z;m2=Z@K@K@Z
  assert m2*m2<=m1*m3+1e-8
print("PASS exact interacting physical SU2 third fsum, magnetic separation, Cauchy; no Monte Carlo.")
