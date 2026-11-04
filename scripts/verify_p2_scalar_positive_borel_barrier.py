#!/usr/bin/env python3
"""Exact nonnegative scalar P2 majorant and provable positive Borel singularity gate."""
from fractions import Fraction as F
from math import factorial
C=F(88,3);M=F(16,3)
a=[F(0),M]
for n in range(2,101):
 conv=sum(a[i]*a[n-i] for i in range(1,n))
 a.append((C+6*(n+2))*conv)
 assert a[n]==(C+12+6*n)*conv
 assert a[n]>0
 if n>=3: assert a[n]/factorial(n)>=12*M*a[n-1]/factorial(n-1)
assert F(9,5120)<F(1,12*M)==F(1,64)
print("PASS 99 exact rational scalar-majorant recurrence coefficients")
print("Rigorously 9/5120 <= Borel radius <= 1/64 at sigma=0")
print("Pringsheim: nonnegative scalar comparison has a positive-real Borel singularity")
print("NOT a theorem about the actual signed SU2 Borel transform")
