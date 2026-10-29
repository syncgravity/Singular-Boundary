#!/usr/bin/env python3
"""Exact deterministic SU2 vacuum mixed-Hessian checks; no Monte Carlo."""
import sympy as s
from itertools import combinations
a,b,t=s.symbols('a b t',positive=True)
assert s.simplify(s.diff(b*(1-s.cos(t/2)),t,2).subs(t,0)-b/4)==0
coef=b/(6*a)
assert s.simplify(b*coef/4-2*coef**2*(3*a)*s.Rational(1,4))==0
seed=[
[(-1,-1,-1,-1,-1),(-1,-1,-1,0,-1),(0,-1,-1,-1,-1),(0,-1,-1,0,-1)],
[(-1,-1,-1,-1,-1),(-1,-1,0,-1,-1),(-1,-1,-1,0,-1),(-1,-1,0,0,-1)],
[(-1,-1,-1,-1,-1),(-1,0,-1,-1,-1),(0,-1,-1,-1,-1),(0,0,-1,-1,-1)]]
def edges(face):return {tuple(sorted((x,y))) for x,y in combinations(face,2) if sum(abs(i-j) for i,j in zip(x,y))==1}
assert len(set.union(*(edges(f) for f in seed)))==10
print("PASS SU2 Casimir perturbative Hessian/susceptibility; 3-face spatial seed; no simulation")
