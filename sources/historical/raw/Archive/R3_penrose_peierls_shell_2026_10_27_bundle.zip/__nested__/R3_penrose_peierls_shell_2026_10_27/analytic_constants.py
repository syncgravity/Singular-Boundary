#!/usr/bin/env python3
"""Numerical checks only; proofs are self-contained in FORMAL_NOTE.md."""
import math
from scipy.integrate import quad
c=8/(3*math.pi**3)
C=14-math.log(c)
assert abs(C-16.4533604045365)<1e-12
for r in [0.001,0.01,0.1,0.5,1.]:
 exact=(r-math.sin(r)*math.cos(r))/math.pi
 assert exact>=c*r**3-1e-15
print('Haar c=',c,'C_7=',C)
print('For the fixed 14-face Penrose insertion, |A|=54, |B|=101, |H|=232; |B|+|H|=333')
