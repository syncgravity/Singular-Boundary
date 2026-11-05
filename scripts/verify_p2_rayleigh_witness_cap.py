#!/usr/bin/env python3
"""Exact all-width cap on specific Gauss-invariant Rayleigh LOWER witness.
Not a trace-norm upper bound on the physical response.
"""
from fractions import Fraction as F
from math import ceil
def bound(N,m):
 assert N>=4 and N%2==0 and m>=3
 return F(5*N*(m+2)**4,(m+1)**3*(N-2)*(3*N+m*m-4))
for m in range(3,10000):
 for l in (m-1,m+1):
  beta=F(3+m*(m+2)-l*(l+2),2)
  assert abs(beta)+F(3,2)*(l+1)<=F(5,2)*(m+2)
for m in (3,4,6,10,16,32,64,128,256,512,1024):
 N=2*ceil(m*m/2)
 assert bound(N,m)>0
 print('m',m,'N',N,'m times dual-cap',float(m*bound(N,m)))
assert abs(float(1024*bound(1024**2,1024))-1.25)<.02
print('PASS 19994 exact local collar source bounds; cap=5/(4m)(1+o(1))')
print('WARNING: this upper cap applies only to the LOWER Rayleigh certificate, not the true Schatten response.')
