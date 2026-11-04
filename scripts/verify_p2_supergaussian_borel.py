#!/usr/bin/env python3
"""Exact fixed-window Catalan coefficients and cubic history-majorant checks."""
from fractions import Fraction as F
from math import comb,exp,log
for L in range(1,101):
 C=2+6*L;M=F(4*L,3);B=4*C*M
 for n in range(1,51):
  cat=F(comb(2*n-2,n-1),n)
  assert cat*C**(n-1)*M**n <= M*B**(n-1)
print("PASS 5000 exact finite-window Catalan coefficients")
b=128/3
for a in (.1,1.,4.):
 for R in (0.,.25,1.,2.):
  for L in (1,2,3,4,7,12,20,40,80,160,1000):
   lhs=b*R*L*L-a*L**3
   rhs=-a*L**3/2+16*b**3*R**3/(27*a*a)
   assert lhs<=rhs+1e-8*max(1,abs(lhs),abs(rhs))
print("PASS cubic history-weight entire-growth bound checks")
print("CAUTION: weaker topology; no anchored Borel summability follows")
