#!/usr/bin/env python3
"""Deterministic SU2 deleted-fiber exact identities; full rotor tests in companion ZIP."""
import sympy as s
from math import acos,sqrt,pi
p,A,h,e,q=s.symbols("p A h e q",positive=True)
rho=2*s.sqrt(1-p*p)/s.pi
g=A*(1-p*p)/4
drift=-3*A*p/4
assert s.simplify(s.diff(rho*g,p)-rho*drift)==0
phi=(1+e*p*p*q)/s.sqrt(1+e*e*p**4/4)
def haar_q(z):
  z=s.expand(z)
  for power in range(8,1,-1):
    if power%2: z=z.subs(q**power,0)
  z=z.subs(q**4,s.Rational(1,8)).subs(q**3,0)
  return s.simplify(s.expand(z).subs(q**2,s.Rational(1,4)).subs(q,0))
assert haar_q(phi*phi)==1
assert haar_q(phi*s.diff(phi,p))==0
c=(s.acos(1-h)-(1-h)*s.sqrt(2*h-h*h))/s.pi
assert s.simplify(s.limit(c/h**s.Rational(3,2),h,0)-4*s.sqrt(2)/(3*s.pi))==0
print("PASS Haar radial divergence, nonconstant conditional-state kinetic cross cancellation, center cap exponent")
print("OPEN full nonlinear deleted-face fiber potential monotonicity; no mass gap claim")
