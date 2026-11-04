#!/usr/bin/env python3
"""Exact-rational regression for P2 Gauss-twirl spectrum and local Borel bounds.
The companion archive independently tests dense physical matrices N=2,4,6.
"""
from fractions import Fraction as F
from math import comb, factorial
for k in range(1,101):
 N=2*k; C=comb(N,k); s=[]
 for j in range(k+1):
  mu=comb(N,k-j)-(comb(N,k-j-1) if k-j>0 else 0)
  q=F(mu,(2*j+1)*C)
  assert q==F(comb(N,k-j),(k+j+1)*C)
  s.extend([q]*(2*j+1))
 assert len(s)==(k+1)**2
 assert sum(s)==1
 assert sum(x*x for x in s)==F(1,N+1)
 assert max(s)==F(1,k+1)
print("PASS 100 exact rational even-width Gauss-twirl spectra")
for L in range(1,101):
 C=2+6*L;M=F(4*L,3)
 assert F(1,4*C*M)==F(3,16*L*(2+6*L))
 for n in range(1,51):
  cat=F(comb(2*n-2,n-1),n)
  assert cat<=4**(n-1)
  assert cat*C**(n-1)*M**n/factorial(n)<=M*(4*C*M)**(n-1)/factorial(n)
print("PASS 5000 exact fixed-history Catalan/Borel bounds")
print("NOTE: componentwise entire does NOT establish global anchored continuation.")
