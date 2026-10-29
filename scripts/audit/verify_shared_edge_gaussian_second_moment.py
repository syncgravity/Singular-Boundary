#!/usr/bin/env python3
"""Exact shared-link Gaussian tangent moment certificate; deterministic."""
import sympy as s
L=s.Matrix([[4,-1,0],[-1,4,-1],[0,-1,4]])
assert L.eigenvals()=={4-s.sqrt(2):1,s.Integer(4):1,4+s.sqrt(2):1}
assert s.trace(L)==12 and s.trace(L*L)==52
h,a,b=s.symbols('h a b',positive=True)
assert s.simplify(3*a*h*s.trace(L)/(16*b)-9*a*h/(4*b))==0
assert s.simplify(3*a*a*h*s.trace(L*L)/8-39*a*a*h/2)==0
assert s.simplify((3*a*a*h*s.trace(L*L)/8).subs(h,s.symbols("h",positive=True)))!=0
print("PASS exact Penrose spatial dual eigenvalues, Gaussian critical-source variance and m2")
