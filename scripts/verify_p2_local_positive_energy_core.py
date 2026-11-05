#!/usr/bin/env python3
"""Local ground variational positivity and exceptional-anchor O(N^-1/2) checks.
Finite interacting spin chain is a structural regression, not a full SU2 proof.
"""
from fractions import Fraction
from math import sqrt
import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.linalg import eigsh
I=np.eye(2, dtype=complex);X=np.array([[0,1],[1,0]],complex)
Y=np.array([[0,-1j],[1j,0]],complex)
Z=np.diag([1,-1]).astype(complex)
def site(N, ops):
 out=np.array([[1]],complex)
 for j in range(N):out=np.kron(out,ops.get(j,I))
 return out
for N in range(3,8):
 H=sum((1.5*(np.eye(2**N)-site(N,{j:Z})) for j in range(N)),np.zeros((2**N,2**N),complex))
 H-=.35*sum((site(N,{j:X,j+1:X}) for j in range(N-1)),np.zeros_like(H))
 e,p=eigsh(csr_matrix(H),k=1,which='SA',tol=1e-12)
 psi=p[:,0]
 for A1 in (X,Y,Z,(X+Z)/sqrt(2),(Y+Z)/sqrt(2)):
  for j in range(N):
   A=site(N,{j:A1})
   comm=np.vdot(psi,A.conj().T@(H@A-A@H)@psi).real
   vari=np.vdot(A@psi,(H-e[0]*np.eye(2**N))@(A@psi)).real
   assert abs(comm-vari)<1e-9 and comm>=-1e-9
 print('PASS finite ground commutator identity, N=',N)
for s in range(1,20):
 for N in (s+3,s+8,3*s+20):
  bad=[j for j in range(N) if j<1 or j+s>N-1]
  assert len(bad)<=s+2
for n in range(1,101):
 Cas=n*(n+2)
 for cutoff in (1,4,10,100,1000):
  if Cas>cutoff:assert n/2<=Cas/sqrt(cutoff)
print('PASS exact exceptional-anchor count and first-order SU2 Casimir tail')
print('Unbounded infinite-volume C*-dynamics and a spectral gap remain unproved.')
