#!/usr/bin/env python3
"""P-67: dimension-free actual corrected SU2 induced S1 Neumann remainder.
Rigor is analytic; numerical values below are regressions not interval enclosures.
"""
from math import sqrt
import numpy as np
import verify_p2_onehaar_original_link as p
def eta(N,l,interior):
 D=3*(N-1)+l*(l+2)
 if interior:return (3*(N-3)+2*sqrt(3*l*(l+2)))/(2*D)
 return (3*(N-2)+sqrt(3*l*(l+2)))/(2*D)
def rank_cap(N,m,l):return 13*(m+1)*((N+l+1)**2//4)
def total_tail(N,m,q):
 H=2.5*(m+2)*sqrt((m+1)/(N+1));s=0.
 for l in (m-1,m+1):
  D=3*(N-1)+l*(l+2);w=(l+1)**2/(4*(m+1)**3)
  end=eta(N,l,False);inter=eta(N,l,True)
  s+=w*sqrt(rank_cap(N,m,l))*H/D*(2*end**(q+1)/(1-end)+(N-2)*inter**(q+1)/(1-inter))
 return s
for m in (3,4,6,10,20,40,80,160,300,1000):
 N=m*m+m%2
 q=0
 while total_tail(N,m,q)>1e-6:q+=1
 assert q<40 and total_tail(N,m,q)<=1e-6
 print('PASS formula-bound m',m,'N',N,'sufficient q',q)
rng=np.random.default_rng(17)
for l in (1,2,4,8):
 n=l+1;dim=2*n;As=p.spin(l);Bs=p.spin(1)
 factor=sqrt(3*l*(l+2))/2
 for _ in range(16):
  X=rng.normal(size=(dim,dim))+1j*rng.normal(size=(dim,dim))
  B=-2*sum(np.kron(a,np.eye(2))@X@np.kron(np.eye(n),z) for a,z in zip(As,Bs))
  assert np.linalg.norm(B,'nuc')<=factor*np.linalg.norm(X,'nuc')*(1+1e-10)
 print('PASS actual SU2 mixed-bond induced trace norm upper degree',l)
for l in (2,4):
 B=p.block(p.F,3,l);deg=[l,1];D=l*(l+2)+3
 Y=(p.block(p.K(p.F,[1,1]),3,l)+15*B-p.K(B,deg))/2
 d=Y.shape[0]
 km=np.column_stack([p.K(np.eye(d*d)[:,i].reshape(d,d),deg).ravel() for i in range(d*d)])
 actual=np.linalg.solve(km,Y.ravel()).reshape(d,d)
 theta=sqrt(3*l*(l+2))/(2*D)
 step=Y/D;appro=np.zeros_like(Y)
 for q in range(13):
  appro+=step
  upper=np.linalg.norm(Y,'nuc')/D*theta**(q+1)/(1-theta)
  assert np.linalg.norm(actual-appro,'nuc')<=upper*(1+1e-8)+1e-11
  step=-(p.K(step,deg)-D*step)/D
 print('PASS physical Gauss-invariant original-link q=0..12 S1 tail degree',l)
print('Dimension-free induced nuclear contraction proven; full N~m² Schur sums remain uncomputed.')
