#!/usr/bin/env python3
"""P-74: critical neighboring half-Casimir weight for genuine corrected SU2
gauge-invariant spin-zero projection second Hamiltonian commutator.
Finite spin checks illustrate analytic row/column Cauchy-Schwarz bound; no dynamics inferred.
"""
from math import sqrt
import numpy as np
def spin(n):
 j=n/2;up=np.zeros((n+1,n+1),complex)
 for k in range(n):
  z=j-k-1;up[k,k+1]=sqrt((j-z)*(j+z+1))
 return ((up+up.conj().T)/2,(up-up.conj().T)/(2j),np.diag(np.arange(n,-n-1,-2)/2))
P=np.diag([1,0,0,0,0]).astype(complex)
V=np.zeros((5,5),complex)
for k in (1,4):V[0,k]=V[k,0]=-1/(2*sqrt(2))
C=np.diag([0,.75,.75,.75,.75]).astype(complex)
J=[]
for A in spin(1):
 M=np.zeros((5,5),complex);M[1:,1:]=np.kron(np.eye(2),A);J.append(M)
ad=lambda A,B:A@B-B@A
D=ad(V,P);A=[ad(Z,D) for Z in J]
assert abs(np.linalg.norm(A[2]@np.eye(5)[:,0])-.25)<1e-12
for lam in (.5,1.,2.):
 B0=lam*(4*ad(C,D)+lam*ad(V,D))
 upper=np.linalg.norm(B0,2)+2*abs(lam)*sqrt(sum(np.linalg.norm(z,2)**2 for z in A))
 values={}
 for beta in (.25,.5,.75):
  data=[]
  for n in (8,16,32,64):
   JJ=spin(n);cas=n*(n+2)/4
   operator=np.kron(B0,np.eye(n+1,dtype=complex))
   for a in range(3):operator+=2*lam*np.kron(A[a],JJ[a])
   weighted=np.linalg.norm(operator,2)*(1+cas)**(-beta)
   if beta==.5:assert weighted<=upper+1e-9
   data.append(weighted)
  values[beta]=data
 assert values[.25][-1]>values[.25][0]*1.7
 assert values[.5][-1]<values[.5][0]*1.01
 print('PASS lambda',lam,'critical beta=1/2 bounded, beta<1/2 diverges',values)
print('Analytic bound at beta=1/2 by spin-generator row/column inequality;')
print('higher-spin compression makes beta<1/2 diverge. This is at time t=0 only.')
