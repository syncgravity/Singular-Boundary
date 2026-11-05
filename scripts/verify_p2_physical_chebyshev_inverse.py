#!/usr/bin/env python3
"""Chebyshev q-inverse error on ACTUAL corrected original-link SU2 N=2,m=3 source.
Depends only on repository's preexisting verified q0 physical source code.
"""
from math import sqrt
import numpy as np
import verify_p2_onehaar_original_link as p
for l in (2,4):
 deg=[l,1];D=l*(l+2)+3
 B=p.block(p.F,3,l)
 Y=(p.block(p.K(p.F,[1,1]),3,l)+15*B-p.K(B,deg))/2
 d=Y.shape[0]
 Kmat=np.column_stack([p.K(np.eye(d*d)[:,k].reshape(d,d),deg).reshape(-1)
                       for k in range(d*d)])
 actual=np.linalg.solve(Kmat,Y.reshape(-1)).reshape(d,d)
 theta=sqrt(3*l*(l+2))/(2*D)
 rho=theta/(1+sqrt(1-theta*theta))
 def T(X):return (p.K(X,deg)-D*X)/(D*theta)
 prev=Y;cur=T(Y)
 approx=Y/(D*sqrt(1-theta*theta))
 neumann=np.zeros_like(Y);step=Y/D
 for q in range(13):
  if q:approx+=2*(-rho)**q*cur/(D*sqrt(1-theta*theta))
  neumann+=step
  err=np.linalg.norm(actual-approx,'nuc')
  bound=2*sqrt(d)*np.linalg.norm(Y,'fro')*rho**(q+1)/(D*sqrt(1-theta*theta)*(1-rho))
  assert err<=bound*(1+1e-7)+1e-11,(l,q,err,bound)
  if q in (0,1,4,8,12):
   print('PASS physical corrected SU2 l',l,'q',q,
         'Cheb S1 error',err,'Neumann S1 error',np.linalg.norm(actual-neumann,'nuc'),
         'certified-in-formula tail',bound)
  step=-(p.K(step,deg)-D*step)/D
  if q>=1:prev,cur=cur,2*T(cur)-prev
print('PASS actual corrected original-link physical Chebyshev CG-source tests')
