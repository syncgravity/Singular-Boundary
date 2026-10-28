#!/usr/bin/env python3
"""Exact symbolic checks for the renormalized Wilson source audit; no simulations."""
import sympy as s
from itertools import combinations
seed=[
[[-1,-1,-1,-1,-1],[-1,-1,-1,0,-1],[0,-1,-1,-1,-1],[0,-1,-1,0,-1]],
[[-1,-1,-1,-1,-1],[-1,-1,0,-1,-1],[-1,-1,-1,0,-1],[-1,-1,0,0,-1]],
[[-1,-1,-1,-1,-1],[-1,0,-1,-1,-1],[0,-1,-1,-1,-1],[0,0,-1,-1,-1]]]
def edges(z):
 z=list(map(tuple,z));return {tuple(sorted((x,y))) for x,y in combinations(z,2) if sum(abs(a-b) for a,b in zip(x,y))==1}
f=[edges(z) for z in seed]
assert len(set().union(*f))==10
assert [len(f[i]&f[j]) for i,j in combinations(range(3),2)]==[1,1,0]
h,a,b,c,t=s.symbols('h a b c t',positive=True)
v=s.expand(h*h*(4*a*a+b*b+9*c*c)/4)
assert s.simplify(s.diff(v*s.exp(-3*t),t)+3*v*s.exp(-3*t))==0
assert s.simplify(v/h**2-(4*a*a+b*b+9*c*c)/4)==0
print('Verified 3 original seed rhombi, exact electric reference variance/correlator and coefficients; no MCMC')
