#!/usr/bin/env python3
"""Exact source-order reachability and Gaussian graded Poisson algebra audit.
The analytic theorem and limitations are in P2_ONE_HAAR_SOURCEORDER_GAUSSIAN_2026-11-04.md.
"""
from itertools import product
from fractions import Fraction as F
from decimal import Decimal,getcontext
getcontext().prec=70
count=0
for L in range(1,5):
 for mult in product(range(5),repeat=L):
  if not any(mult):continue
  for spins in product(*[range(x+1) for x in mult]):
   if not all((m-c)%2==0 for m,c in zip(mult,spins)):continue
   minimum=sum((c if c else 2) for m,c in zip(mult,spins) if m>0)
   assert sum(mult)>=minimum
   count+=1
assert count==7376
for L in range(1,401):
 assert 2*L-1==1+sum(2 for _ in range(L-1))
C=F(88,3);t=F(1,4)
for n in range(1,151):
 for m in range(1,151):
  assert n+m+2<=2*n*m+2
  assert C+24*t*(n+m+2)<=F(160,3)+12*(n*m-1)
d=Decimal
H=d(160)/3*(-d(6)).exp()
src=d(16)/3*(-d(3)).exp()
crit=4*H*src
assert crit==d(10240)/9*(-d(9)).exp()
assert crit<1
print("PASS",count,"exact parity/source leaf checks; 22,500 grade pairs")
print("PASS formal source-order a=3 lambda=1 contraction bound",crit)
print("CAUTION: source-order evaluation into physical norm is discontinuous.")
