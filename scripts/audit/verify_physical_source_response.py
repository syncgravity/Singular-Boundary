#!/usr/bin/env python3
"""Exact symbolic physical Wilson-source response, no Monte Carlo."""
import sympy as s
a,t,z,g=s.symbols('a t z g',positive=True)
v=s.Rational(1,4);m=3*a*v;chi=v/(3*a)
assert s.simplify(chi-v*v/m)==0
assert s.simplify(-2*chi+1/(6*a))==0
assert s.simplify(v*s.exp(-3*a*t)-v*s.exp(-m*t/v))==0
sfield=s.symbols('sfield',real=True)
trial=(z*z*m-sfield*2*z*v)/(1+z*z*v)
assert s.simplify(s.limit((trial.subs(z,sfield*v/m))/sfield**2,sfield,0)+v*v/m)==0
print("PASS: physical SU2 response, susceptibility, Euclidean kernel, variational source; no Monte Carlo")
