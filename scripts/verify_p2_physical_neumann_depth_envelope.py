#!/usr/bin/env python3
"""Sufficient corrected SU2 physical Neumann depth, not necessary depth or proof of easy inversion."""
from math import sqrt,log2,ceil
def theta(N,l,interior):
 D=3*(N-1)+l*(l+2)
 p=3*(N-3)+2*sqrt(3*l*(l+2)) if interior else 3*(N-2)+sqrt(3*l*(l+2))
 return p/(2*D)
def bound(N,m,eps):
 assert N>=4 and N%2==0 and m>=3 and eps>0
 a=max(theta(N,l,interior) for l in (m-1,m+1) for interior in (False,True))
 D=3*N+m*m-4
 B=(2.5*N*(m+2)/D*sqrt((m+1)/(N+1))
    *(m**2.5+(m+2)**2.5)/(4*(m+1)**3))
 logC=(N-1)/2+log2(B)-log2(1-a)
 q=max(0,ceil((log2(eps)-logC)/log2(a)-1))
 assert logC+(q+1)*log2(a)<=log2(eps)+1e-9
 return q,a
for m in (3,4,6,10,20,40,80,160):
 N=m*m+m%2
 q,a=bound(N,m,1e-6)
 print('PASS m',m,'N',N,'theta',round(a,8),'sufficient q',q)
for m in (100,1000):
 N=m*m;q,a=bound(N,m,1e-6)
 assert abs(q/N-1/(2*log2(8/3)))<.01
print('Conservative sufficient q ~ 0.3533475263N at N~m², fixed tolerance')
print('NOT a lower bound on actual q; actual high-spin physical Schur overlaps uncomputed')
