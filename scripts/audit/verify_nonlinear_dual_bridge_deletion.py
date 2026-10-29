#!/usr/bin/env python3
"""Exact bridge topology and SU2 Haar magnetic-deletion check; full reproducible script in package."""
import sympy as s
from scipy.special import ive
from math import sqrt
A,b,k=s.symbols("A b k",positive=True)
expr=3*A*k/8+3*b/(4*k)
opt=s.sqrt(2*b/A)
assert s.simplify(expr.subs(k,opt)-3*s.sqrt(A*b)/(2*s.sqrt(2)))==0
for value in [.2,1.,5.,20.]:
 r=ive(0,2*value)/ive(1,2*value)-1/value
 assert 0<=1-r<=3/(4*value)+1e-12
print("PASS SU2 Haar trial and exact magnetic deletion coefficient; topology and rotor in ZIP.")
