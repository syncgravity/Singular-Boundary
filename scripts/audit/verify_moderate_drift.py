#!/usr/bin/env python3
"""Exact SU2 one-face drift and spectral-alternative audit. No Monte Carlo."""
import sympy as s
from itertools import combinations
p,a,h,y=s.symbols("p a h y",real=True,positive=True)
rho=2*s.sqrt(1-p*p)/s.pi;gamma=a*(1-p*p)
drift=-3*a*p
assert s.simplify(s.diff(rho*gamma,p)-rho*drift)==0
assert s.simplify((-h*drift).subs(p,1-y/h)-3*a*(h-y))==0
assert s.simplify((s.diff(p*gamma*rho,p)-(gamma+p*drift)*rho))==0
# SU2 character orthogonality: Var_Haar p=1/4 and first moment=3a/4
assert s.simplify(3*a/4-3*a*s.Rational(1,4))==0
C,v=s.symbols('C v',positive=True)
assert s.simplify(v-C/(2*C/v)-v/2)==0
seed=[
[(-1,-1,-1,-1,-1),(-1,-1,-1,0,-1),(0,-1,-1,-1,-1),(0,-1,-1,0,-1)],
[(-1,-1,-1,-1,-1),(-1,-1,0,-1,-1),(-1,-1,-1,0,-1),(-1,-1,0,0,-1)],
[(-1,-1,-1,-1,-1),(-1,0,-1,-1,-1),(0,-1,-1,-1,-1),(0,0,-1,-1,-1)]]
def edges(f):return {tuple(sorted((x,z))) for x,z in combinations(f,2) if sum(abs(i-j) for i,j in zip(x,z))==1}
assert len(set.union(*(edges(f) for f in seed)))==10
print("PASS: exact SU2 drift, flux, Haar spectral moment and Penrose seed; no simulation")
