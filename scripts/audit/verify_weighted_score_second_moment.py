#!/usr/bin/env python3
"""Deterministic algebraic checks for SU2 weighted vacuum-score and second spectral moment."""
import sympy as s
from itertools import combinations
h,t,a,CE,M1,M2,mstar,C=s.symbols("h t a CE M1 M2 mstar C",positive=True)
p=s.symbols("p",real=True)
assert s.simplify((1-p*p)/4-(1-p)/2+(1-p)**2/4)==0
z=s.symbols("z",positive=True)
assert s.simplify(s.diff(s.exp(t*z/2),z)**2*(4*a*h*z)-a*t*t*h*z*s.exp(t*z))==0
x,y=s.symbols("x y",real=True)
assert s.simplify(2*(x+y)**2+2*y*y-x*x-(x+2*y)**2)==0
rhs=2*CE*h**-3*M1+4*a*h*M2
assert s.simplify(h**3*rhs-(2*CE*M1+4*a*h**4*M2))==0
cut=2*C*h**-3/mstar
assert s.simplify(C*h**-3/cut-mstar/2)==0
assert s.simplify(mstar**2/(C*h**-3)-mstar**2*h**3/C)==0
seed=[
[(-1,-1,-1,-1,-1),(-1,-1,-1,0,-1),(0,-1,-1,-1,-1),(0,-1,-1,0,-1)],
[(-1,-1,-1,-1,-1),(-1,-1,0,-1,-1),(-1,-1,-1,0,-1),(-1,-1,0,0,-1)],
[(-1,-1,-1,-1,-1),(-1,0,-1,-1,-1),(0,-1,-1,-1,-1),(0,0,-1,-1,-1)]]
def edges(f):return {tuple(sorted((x,y))) for x,y in combinations(f,2) if sum(abs(i-j) for i,j in zip(x,y))==1}
fs=[edges(f) for f in seed]; ee=set.union(*fs)
assert len(ee)==10 and max(sum(e in f for f in fs) for e in ee)==2
print("PASS SU2 gradient, weighted IMS, h scaling, spectral moments, authentic 3-face spatial fixture")
