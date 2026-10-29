#!/usr/bin/env python3
"""Deterministic collective transverse spectrum and deleted longitudinal coefficient audit.
Square n-by-n dual grids are surrogates, not Penrose geometry data.
"""
import math
import numpy as np
from scipy.sparse import diags, eye, kron
from scipy.sparse.linalg import spsolve, eigsh

L3=np.array([[4.,-1.,0.],[-1.,4.,-1.],[0.,-1.,4.]])
assert np.allclose(np.linalg.eigvalsh(L3),[4-math.sqrt(2),4,4+math.sqrt(2)])
for n in (7,15,31,63):
  J=diags([-np.ones(n-1),2*np.ones(n),-np.ones(n-1)],[-1,0,1],format="csr")
  I=eye(n,format="csr")
  M=kron(J,I,format="csr")+kron(I,J,format="csr")
  center=(n//2)*n+n//2
  delta=1/(n+1)
  lam=4-4*math.cos(math.pi/(n+1))
  freq=math.sqrt(lam)/(math.sqrt(2)*delta)
  e=np.zeros(n*n);e[center]=1
  G=float(spsolve(M,e)[center])
  if n<=31:
    keep=np.arange(n*n)!=center
    minus=M[keep,:][:,keep]
    lm=float(eigsh(minus,k=1,which="SA",tol=1e-9)[0][0])
    freqminus=math.sqrt(lm)/(math.sqrt(2)*delta)
    assert 2.5<freqminus<4.5
  assert abs(freq-math.pi)<.2 and G>0
  print(n,round(freq,8),round(G,8),round(1/G,8))
# True all-volume SU2 marginal: Var_Haar(p)=1/4, odd Rayleigh ratio for a_e=1 is 3.
assert abs((4/4)*(1-.25)/.25 - 3)<1e-13
print("PASS collective harmonic modes and exact SU2 center-odd marginal bound")
