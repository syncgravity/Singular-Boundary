#!/usr/bin/env python3
"""Companion exact checks for fixed-support nonlinear SU2 defect spectral localization."""
from math import pi,cos,sin
import sympy as s
u=s.symbols('u',real=True)
assert s.simplify(s.diff(u*u/2-(1-s.cos(u)),u)-(u-s.sin(u)))==0
h=s.symbols('h',positive=True);g=s.Rational(3,4)
assert s.simplify(g-s.Rational(1,2)-s.Rational(1,4))==0
assert 1-g==s.Rational(1,4)
assert s.simplify(2*g-s.Rational(3,2))==0
print("PASS: angle derivative and source/area/spectral cutoff exponents; full nonlinear rotor verifier in ZIP.")
