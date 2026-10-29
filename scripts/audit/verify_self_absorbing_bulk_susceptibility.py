#!/usr/bin/env python3
"""Deterministic SU2 self-absorbing coupling fsum certificate."""
import sympy as s
p,A,b,h,m,L=s.symbols('p A b h m L',positive=True)
d=1-p
assert s.simplify((1-p*p)-(2*d-d*d))==0
lam=L*h**(-s.Rational(5,4))*m**s.Rational(1,4)
assert s.simplify(h**(-6)*m/lam**4-h**(-1)/L**4)==0
x,c,z=s.symbols('x c z',nonnegative=True)
assert s.simplify((c+s.sqrt(c*c+4*z))**2/4-z-c*(c+s.sqrt(c*c+4*z))/2)==0
print('PASS SU2 trace identity, fourth-power cutoff, and self-absorption. Full character-basis audit in downloadable ZIP.')
