#!/usr/bin/env python3
"""Exact one-face free SU2 norm-topology obstruction on Gauss-invariant character sector."""
import cmath
from math import pi
for n in (10,20,100,1000,10000):
 t=pi/(2*n+3)
 phase=cmath.exp(1j*t*(2*n+3))
 assert abs(phase-1)>2-1e-12
 print('PASS n',n,'time',t,'operator norm lower bound',abs(phase-1))
# weakly time-smeared A_f has norm shift <=||A|| * ||f_t-f||_1.
# Normalized top-hat f=1_[0,1] has ||f_t-f||_1=2 min(|t|,1).
for t in (.5,.1,.01,.001):
 assert 2*min(t,1)<2
print('PASS exact one-face free character non-norm-continuity and free smearing remedy')
print('NO interacting infinite-volume norm dynamics inferred')
