#!/usr/bin/env python3
"""Exact rational/symbolic checks for the variance and spectral tightness note. No Monte Carlo."""
from fractions import Fraction as Q
import sympy as s
import json
w=s.symbols('w',positive=True)
ex2=3/(2*w);ex4=15/(4*w*w)
variance=s.simplify((ex4-ex2*ex2)/4)
assert variance==3/(8*w*w)
assert s.simplify(variance.subs(w,1/s.sqrt(2))-s.Rational(3,4))==0
assert s.simplify((ex2/2).subs(w,1/s.sqrt(2))-3/(2*s.sqrt(2)))==0
assert s.simplify(4*(1/s.sqrt(2))-2*s.sqrt(2))==0
measure=[(Q(1,2),Q(1,3)),(Q(3,2),Q(2,3))]
V=sum((weight for E,weight in measure),Q(0))
M=sum((E*weight for E,weight in measure),Q(0))
assert V==1 and M==Q(7,6)
assert sum((weight for E,weight in measure if E<=2*M/V),Q(0))>=V/2
print(json.dumps({'one_face_strong_field_variance_over_a_div_b':'3/4','one_face_gap_over_sqrt_ab':'2*sqrt(2)','spectral_fixture_first_moment':str(M),'spectral_fixture_variance':str(V),'monte_carlo':False,'interacting_variance_proved':False},indent=2))
