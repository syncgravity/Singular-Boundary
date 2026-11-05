#!/usr/bin/env python3
"""P-77: positive local nuclear-transfer upper on an operator MPS, plus actual
corrected original-link SU2 q0 residual S1 enclosure (dense used as oracle).
Complete product-tensor residual and Haar-HS transfer tests are in Library ZIP.
"""
import numpy as np
from math import sqrt
import verify_p2_onehaar_original_link as p
rng=np.random.default_rng(771)
def kron(xs):
 from functools import reduce
 return reduce(np.kron,xs)
def transfer_pi(A):
 v=np.ones(1)
 for T in A:
  l,r,d,_=T.shape;W=np.zeros((l,r))
  for i in range(l):
   for j in range(r):
    W[i,j]=np.linalg.norm(T[i,j],'nuc')
  v=v@W
 return float(v[0])
def mps_rank_terms(terms):
 R=len(terms);n=len(terms[0][1]);out=[]
 for i in range(n):
  d=len(terms[0][1][i])
  T=np.zeros((1 if i==0 else R,1 if i==n-1 else R,d,d),complex)
  for a,(c,u,v) in enumerate(terms):
   T[0 if i==0 else a,0 if i==n-1 else a]+=(c if i==0 else 1)*np.outer(u[i],v[i].conj())
  out.append(T)
 return out
for degrees in ([1,1],[2,1,1],[1,3,1,1]):
 terms=[]
 for r in range(5):
  ket=[rng.normal(size=n+1)+1j*rng.normal(size=n+1) for n in degrees]
  bra=[rng.normal(size=n+1)+1j*rng.normal(size=n+1) for n in degrees]
  terms.append((rng.normal()+1j*rng.normal(),ket,bra))
 X=sum((c*np.outer(kron(u),kron(v).conj()) for c,u,v in terms))
 bound=transfer_pi(mps_rank_terms(terms))
 assert np.linalg.norm(X,'nuc')<=bound+1e-8
 print('PASS operator MPS transfer Pi bound for local degrees',degrees)
for ell in (2,4):
 deg=[ell,1];D=ell*(ell+2)+3
 B=p.block(p.F,3,ell)
 Y=(p.block(p.K(p.F,[1,1]),3,ell)+15*B-p.K(B,deg))/2
 q0=Y/D
 residual=Y-p.K(q0,deg)
 theta=sqrt(3*ell*(ell+2))/(2*D)
 cap=np.linalg.norm(residual,'nuc')/(D*(1-theta))
 dim=Y.shape[0];KM=np.column_stack([p.K(np.eye(dim*dim)[:,k].reshape(dim,dim),deg).ravel() for k in range(dim*dim)])
 full=np.linalg.solve(KM,Y.ravel()).reshape(dim,dim)
 assert np.linalg.norm(full-q0,'nuc')<=cap+1e-10
 print('PASS TRUE physical corrected N2,m3,ell',ell,'a posteriori S1 error cap',cap,'measured',np.linalg.norm(full-q0,'nuc'))
print('Unrestricted nuclear norm of a large MPO is not shown polynomial-time computable.')
