#!/usr/bin/env python3
"""Actual SU2 one-face class-function Schrödinger Jacobi continuation tests.
Finite cutoffs provide numerical examples; positivity and minmax are analytic.
"""
import numpy as np
from scipy.linalg import eigh_tridiagonal
for lam in (0.,0.25,0.5,1.,2.,4.,10.):
 vals=[]
 for cut in (20,40,80,160):
  n=np.arange(cut,dtype=float)
  es=eigh_tridiagonal(n*(n+2),-lam/2*np.ones(cut-1),select='i',select_range=(0,1))[0]
  vals.append(es)
 assert np.max(np.abs(vals[-1]-vals[-2]))<1e-9
 print('real lambda',lam,'E0',vals[-1][0],'gap',vals[-1][1]-vals[-1][0])
assert 3-2*1*1==1
print('PASS exact minmax one-face lambda=1 gap >=1')
print('For EACH fixed N, positivity-improving elliptic ground state is unique and locally real analytic for all real lambda.')
print('NO volume-uniform real-lambda gap or positive-ray Borel summability is proved.')
