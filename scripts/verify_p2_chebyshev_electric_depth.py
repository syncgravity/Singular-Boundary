#!/usr/bin/env python3
"""Sufficient q for actual corrected SU2 electric inverse: Chebyshev vs Neumann.
Actual physical source benchmark is in companion Library ZIP.
"""
from math import sqrt, log, log1p, ceil
def one(N,m,eps):
 assert N>=4 and N%2==0 and m>=3
 t=[]
 for l in (m-1,m+1):
  D=3*(N-1)+l*(l+2)
  t.extend([(3*(N-3)+2*sqrt(3*l*(l+2)))/(2*D),
            (3*(N-2)+sqrt(3*l*(l+2)))/(2*D)])
 theta=max(t)
 rho=theta/(1+sqrt(1-theta*theta))
 B=(2.5*N*(m+2)/(3*N+m*m-4)*sqrt((m+1)/(N+1))
     *(m**2.5+(m+2)**2.5)/(4*(m+1)**3))
 LC=(N-1)*log(2)/2+log(B)+log(2)-.5*log1p(-theta*theta)-log1p(-rho)
 LN=(N-1)*log(2)/2+log(B)-log1p(-theta)
 qc=max(0,ceil((log(eps)-LC)/log(rho)-1))
 qn=max(0,ceil((log(eps)-LN)/log(theta)-1))
 assert LC+(qc+1)*log(rho)<=log(eps)+1e-8
 assert LN+(qn+1)*log(theta)<=log(eps)+1e-8
 assert qc<=qn
 return theta,rho,qc,qn
for m in (3,4,6,10,20,40,80,160):
 N=m*m+m%2
 theta,rho,qc,qn=one(N,m,1e-6)
 print('PASS m',m,'N',N,'Chebyshev',qc,'Neumann',qn,'theta',theta)
for m in (300,1000):
 N=m*m;theta,rho,qc,qn=one(N,m,1e-6)
 asym=log(2)/(2*log((8+sqrt(55))/3))
 assert abs(qc/N-asym)<.003
print('PASS asymptotic sufficient Chebyshev q/N=',asym)
print('NOT proof of necessary q or practical N~m² nuclear norm')
