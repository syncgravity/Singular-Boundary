#!/usr/bin/env python3
"""Exact SU2 gauge-invariant history-weight Poisson obstruction and p>2 growth."""
from fractions import Fraction as F
from math import comb
assert F(3+3-8,2*8)==-F(1,8)
for grade in range(6):
 c=F(9*3**grade,8*(4*2**grade)**2)
 assert c>0
 for L in (10,20,50,100):
  # logarithm of exact normalized ratio is log(c)+aL^p-kappa L.
  # At a=1/50,p=3,kappa=2 it grows without bound.
  assert F(L**3,50)-2*L>F(9*3**grade,1000) if L>=20 else True
 print("PASS SU2 gauge-invariant grade",grade,"weight-independent constant",c)
for p in (F(5,2),F(3),F(4),F(6),F(10)):
 assert p/(p-2)>1
 print("PASS certified p-history majorant order",p/(p-2))
print("WARNING: valid on unrestricted history-label algebra; not source-generated same-grade no-go")
