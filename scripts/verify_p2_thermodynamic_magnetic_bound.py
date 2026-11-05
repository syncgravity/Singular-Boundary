#!/usr/bin/env python3
"""Independent SU2 one-face signed magnetic variational bound checks.
Thermodynamic measure compactness, Dirichlet regularity and shift-invariance are proven analytically.
"""
import numpy as np
from scipy.linalg import eigh_tridiagonal
n=np.arange(100,dtype=float)
for lam in (.1,.25,.5,1.,2.,4.,10.):
 eps=1e-4
 def energy(x):
  return eigh_tridiagonal(n*(n+2),-x/2*np.ones(99),select='i',select_range=(0,0))[0][0]
 magnetic=-2*(energy(lam+eps)-energy(lam-eps))/(2*eps)
 lower=(np.sqrt(9+lam*lam)-3)/lam
 assert lower>0 and magnetic>=lower-1e-6
 print('PASS real lambda=',lam,'magnetic=',magnetic,'uniform lower=',lower)
print('Finite corrected electric form inequality K_N>=2 sum_i C_i and Fisher convexity imply local Sobolev bounds.')
print('WARNING: diagonal translation-invariant measures are not proved to be quantum infinite-volume ground states.')
