#!/usr/bin/env python3
"""P-76: actual two-face corrected K energy dominance and all-time form propagation,
using a finite compression (vacuum+fundamental first face, neighbor spin n).
"""
import numpy as np
from scipy.linalg import eigh
from math import sqrt
def spin(n):
 j=n/2;up=np.zeros((n+1,n+1),complex)
 for k in range(n):
  z=j-k-1;up[k,k+1]=sqrt((j-z)*(j+z+1))
 return [(up+up.conj().T)/2,(up-up.conj().T)/(2j),np.diag(np.arange(n,-n-1,-2)/2)]
C=np.diag([0,.75,.75,.75,.75]);R=[]
for A in spin(1):
 J=np.zeros((5,5),complex);J[1:,1:]=np.kron(np.eye(2),A);R.append(J)
V=np.zeros((5,5),complex)
for k in (1,4):V[0,k]=V[k,0]=-1/(2*sqrt(2))
rng=np.random.default_rng(76)
for n in (1,2,4,8):
 d=n+1;cas=n*(n+2)/4;I=np.eye(d)
 Csum=np.kron(C,I)+cas*np.eye(5*d)
 K=4*Csum+2*sum(np.kron(R[a],spin(n)[a]) for a in range(3))
 assert min(np.linalg.eigvalsh(K-2*Csum))>-1e-10
 e,U=eigh(K);W=U@np.diag(np.sqrt(np.maximum(e,0)+1))@U.conj().T
 for lam in (.25,1.,2.):
  H=K+lam*np.kron(V,I);tval,X=eigh(H)
  for t in (.17,1.1,4.):
   psi=rng.normal(size=5*d)+1j*rng.normal(size=5*d)
   psi/=np.linalg.norm(psi)
   orbit=X@(np.exp(-1j*t*tval)*(X.conj().T@psi))
   assert np.linalg.norm(W@orbit)<=sqrt(1+4*lam)*np.linalg.norm(W@psi)+1e-10
  print('PASS finite original-link energy graph propagation neighbor n',n,'lambda',lam)
print('Bound sqrt(1+2|lambda|N) is uniform in time, NOT in strip length N.')
