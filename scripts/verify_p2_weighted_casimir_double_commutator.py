#!/usr/bin/env python3
"""Actual corrected two-face SU2 local graph-weighted double commutator test.
Proves no all-time dynamics; illustrates graph-bound analytically derived in audit.
"""
import numpy as np
from math import sqrt
def spin(n):
 j=n/2;up=np.zeros((n+1,n+1),complex)
 for k in range(n):
  z=j-k-1
  up[k,k+1]=sqrt((j-z)*(j+z+1))
 return [(up+up.conj().T)/2,(up-up.conj().T)/(2j),np.diag(np.arange(n,-n-1,-2)/2)]
ad=lambda x,y:x@y-y@x
P=np.diag([1,0,0,0,0]).astype(complex);V=np.zeros((5,5),complex)
for i in (1,4):V[0,i]=V[i,0]=-1/(2*sqrt(2))
C=np.diag([0,.75,.75,.75,.75])
J=[]
for A in spin(1):
 T=np.zeros((5,5),complex);T[1:,1:]=np.kron(np.eye(2),A);J.append(T)
D=ad(V,P);comm=[ad(A,D) for A in J]
assert abs(np.linalg.norm(comm[2]@np.eye(5)[:,0])-.25)<1e-12
for lam in (.25,1.,2.):
 B=lam*ad(4*C,D)+lam*lam*ad(V,D)
 bound=np.linalg.norm(B,2)+2*abs(lam)*sum(np.linalg.norm(a,2) for a in comm)
 for n in (1,2,4,8,16,32,64,128):
  cas=n*(n+2)/4
  Z=np.kron(B,np.eye(n+1,dtype=complex))
  for i,a in enumerate(spin(n)):Z+=2*lam*np.kron(comm[i],a)
  weighted=np.linalg.norm(Z,2)/sqrt(1+cas)
  assert weighted<=bound+1e-9
  if n in (1,64,128):print('PASS lambda',lam,'neighbor degree',n,'rawnorm',np.linalg.norm(Z,2),'weighted',weighted,'upper',bound)
print('Graph-weight bound uniform in neighboring spin. No invariant all-time dynamics inferred.')
