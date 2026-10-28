#!/usr/bin/env python3
"""Exact algebra fixtures for coupling-averaged variance; no Monte Carlo."""
import sympy as s
z,h,F,a,beta,sm,sp,bm,bp=s.symbols("z h F a beta sm sp bm bp",positive=True)
E=(z-s.sqrt(z*z+4))/2
assert s.simplify(s.diff(E,z,2)+2/(z*z+4)**s.Rational(3,2))==0
M1=4*a*sp**2*F*h**2
Ecap=6*F*s.sqrt(a*beta)/h
chi_integral=2*h**2*(sm**2/(bm/h**2)**2+sp**2/(bp/h**2)**2)*Ecap
result=s.factor(M1*chi_integral/2)
assert s.simplify(result-24*a**s.Rational(3,2)*s.sqrt(beta)*sp**2*(sm**2/bm**2+sp**2/bp**2)*(F*h**2)**2*h**3)==0
print("PASS: Kato spectral curvature, Cauchy and h^3 integrated variance algebra.")
print("No fixed-coupling variance result; no simulation.")
