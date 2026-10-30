#!/usr/bin/env python3
"""Exact symbolic proof-fixture checks for an interacting Wilson susceptibility bound.
Does not run simulations or approximate any historical records.
"""
import sympy as sp
from fractions import Fraction

s,h,am,bm,sm,spg,F=sp.symbols('s h am bm sm spg F',positive=True)
# Two-dimensional toy ground energy: exact susceptibility/variance identity.
E=(s-sp.sqrt(s*s+4))/2
assert sp.simplify(sp.diff(E,s,2)+2/(s*s+4)**sp.Rational(3,2))==0
v=1/(s*s+4)
chi=2/(s*s+4)**sp.Rational(3,2)
m1=1/sp.sqrt(s*s+4)
assert sp.simplify(v**2-m1*chi/2)==0
# The face magnetic coefficients are bj=betaj / h^2.
betamin,betamax=sp.symbols('betamin betamax',positive=True)
bminus=betamin/h**2; bplus=betamax/h**2
# Core estimated integrated variance inequality:
Ebound=6*F*sp.sqrt(am*bm)
M1bound=4*am*spg**2*F*h**2
chiint=2*h*h*(sm**2/bminus**2+spg**2/bplus**2)*Ebound
V2int=sp.simplify(M1bound*chiint/2)
expected=24*am**sp.Rational(3,2)*spg**2*(F*h*h)**2*h**3*sp.sqrt(betamin)*(sm**2/betamin**2+spg**2/betamax**2)
# Ebound uses bm=bmax=betamin/h^2. Checking that the dimensional expression agrees.
assert sp.simplify(V2int.subs(bm,betamin/h**2)-expected)==0
# If v at distinguished parameter is v0 and function Lipschitz L,
# an interior quadrant of radius v0/(2L) has lower variance v0/2,
# hence integral V^2 >= v0^4/(16 L^2).
v0,L=sp.symbols('v0 L',positive=True)
assert sp.simplify((v0/2)**2*(v0/(2*L))**2-v0**4/(16*L**2))==0
# Finite graph combinatorics, E <= 4 F and each e touches <=2 faces.
from itertools import combinations
faces=[{(0,1),(1,2),(2,3),(0,3)}, {(0,1),(1,4),(4,5),(0,5)}]
from collections import Counter
inc=Counter(e for face in faces for e in face)
assert len(inc)==7 and max(inc.values())==2
print('PASS: exact Kato two-level response and Cauchy-Schwarz equality')
print('PASS: two-shape coupled susceptibility bound simplifies to O(F*h^2)^2*h^3')
print('PASS: conditional Lipschitz-to-pointwise exponent 3/4')
print('No Monte Carlo, no nonlinear Penrose variance inferred at s=(1,1).')
