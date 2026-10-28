#!/usr/bin/env python3
"""Read-only exact source-response energy-window checks. No simulation."""
from fractions import Fraction as F
import sympy as s
alpha,delta,h=s.symbols("alpha delta h",positive=True)
assert s.expand(3-3*alpha+2*(1+delta))==5-3*alpha+2*delta
assert s.simplify((5-3*alpha+2*delta).subs(alpha,s.Rational(3,2))-(s.Rational(1,2)+2*delta))==0
assert s.simplify((3*alpha-4).subs(alpha,s.Rational(3,2))-s.Rational(1,2))==0
a=s.symbols("a",positive=True)
assert s.simplify(8*a*s.Rational(1,16)-a/2)==0
energies=[F(1),F(3),F(7),F(11)]
x=[F(1),F(-2),F(4),F(3)];y=[F(2),F(1),F(-1),F(5)]
for cutoff in [F(2),F(4),F(8)]:
 r=sum((x[i]*y[i]/energies[i] for i in range(4) if energies[i]>cutoff),F(0))
 mx=sum((energies[i]*x[i]**2 for i in range(4)),F(0))
 my=sum((energies[i]*y[i]**2 for i in range(4)),F(0))
 assert r*r <= mx*my/cutoff**4
print("PASS: exact spectral high-energy Cauchy and regulator exponents. No simulation.")
