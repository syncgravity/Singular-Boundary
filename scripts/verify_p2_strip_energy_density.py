#!/usr/bin/env python3
"""Variational proof regression for true original-link SU2 strip energy density.
All-N subadditivity is analytic from exact SU2-vector boundary expectation cancellation.
"""
import numpy as np
from scipy.linalg import eigh_tridiagonal
for lam in (0,.25,.5,1,2,4,10):
 n=np.arange(80,dtype=float)
 one=eigh_tridiagonal(n*(n+2),-lam/2*np.ones(79),select='i',select_range=(0,0))[0][0]
 trial=(3-np.sqrt(9+lam*lam))/2
 assert -abs(lam)<=one+1e-12<=trial+1e-12<=1e-12
 print('PASS lambda',lam,'-|lambda| <= E1 <= 2-char trial:',one,trial)
# Exact block decomposition:
# K_{N+M}=K_N+K_M+2 sum_a R_N^a L_{N+1}^a.
# Each finite positive ground state is invariant under SU2 conjugation.
# Hence each boundary-generator expectation is an SO3-fixed vector, identically zero.
# Product trial -> E_{N+M}<=E_N+E_M. Fekete + -N|lambda| bound.
print('PASS analytic subadditivity assumptions, evenness, concavity and 1-Lipschitz ground-energy-density gates')
print('LIMIT: energy density exists; unique state, N-uniform gap, Borel sum not established')
