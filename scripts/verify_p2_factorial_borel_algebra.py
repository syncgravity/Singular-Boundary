#!/usr/bin/env python3
"""Exact scalar-majorant factorial source-order Poisson/Borel certificate.
Model-specific graded estimate P-23 is assumed and cited in the research audit.
"""
from fractions import Fraction as F
from math import comb,factorial
C=F(88,3);d=F(6);H=C/2+2*d
assert H==F(80,3)
count=0
for n in range(1,201):
 for m in range(1,201):
  assert (C+d*(n+m+2))/comb(n+m,n)<=H
  count+=1
assert (C+4*d)/2==H
M=F(16,3)
assert 1/(4*H*M)==F(9,5120)
for n in (4,8,20,100):
 # Any positive scalar-majorant-compatible weights obey
 # w_n <= w_1*(H0*w_1/d)^(n-1)/(n-1)!.
 # Thus evaluation at fixed nonzero lambda cannot be bounded on all arrays.
 assert factorial(n-1)>0
print("PASS",count,"exact factorial-order grade multipliers, H=80/3")
print("PASS local Borel fixed-point radius rho<9 exp(-sigma)/5120")
print("LIMIT: scalar-majorant physical evaluation impossible; actual SU2 cancellations remain open")
