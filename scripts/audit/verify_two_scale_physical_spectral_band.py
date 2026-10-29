#!/usr/bin/env python3
"""Exact rational source spectral band and boundary layer. No Monte Carlo."""
from fractions import Fraction as Q
from math import exp
for n in (5,10,25,100,500):
 h=Q(1,n);c=Q(1);V=Q(1);M3=Q(1);d=c/(4*V);R=Q(2)
 for E in (h**-1,Q(1),h):
  w=1/E
  assert E*w==1 and E**3*w<=M3/h**2 and w<=V/h
  low=E*w if E<d*h else Q(0)
  high=E*w if E>R/h else Q(0)
  assert low<=c/4 and high<=c/4 and 1-low-high>=c/2
  xi=h*E
  assert h*(E*w)/xi==w
 for E in (float(h)**-.5,):
  assert E**2<=float(h)**-2 and 1/E<=1/float(h)
for t in (.1,1.,3.):
 spec=[(.25,.4),(2.,.1),(10.,.03)]
 m=sum(E*w for E,w in spec)
 Ct=sum(exp(-t*E)*w for E,w in spec)
 for L in (.5,3,12):
  low=sum(w for E,w in spec if E<=L)
  assert exp(-t*L)*low<=Ct+1e-12
  assert Ct<=low+m/L*exp(-t*L)+1e-12
print("PASS spectral shell and boundary layer rational identities, finite time test")
