#!/usr/bin/env python3
"""Exact SU2 magnetic core algebra and Penrose seed. No Monte Carlo."""
import sympy as s
from itertools import combinations
h,gamma,theta,delta,CL,al,bet,CE,CF,bmax=s.symbols("h gamma theta delta CL al bet CE CF bmax",positive=True)
assert s.simplify((h/h**gamma)*h*h**gamma-h*h)==0
assert s.simplify(theta*delta*h**gamma/h-theta*delta*h**(gamma-1))==0
assert s.simplify((bmax*h**-2)*(CE/(bet*h))/(bet*CF*h**-4)-bmax*CE*h/(bet**2*CF))==0
assert s.simplify(32*al*h*h/(bet*(CL/h)**2)-32*al*h**4/(bet*CL**2))==0
t,u,b=s.symbols("t u b",real=True)
f=b*(1-s.cos((t+u)/2))
M=s.hessian(f,(t,u)).subs({t:0,u:0})
assert M==s.Matrix([[b/4,b/4],[b/4,b/4]]) and M.det()==0
assert M*s.Matrix([1,-1])==s.zeros(2,1)
assert s.simplify(s.diff(b*(1-s.cos(t/2)),t,2)-b*s.cos(t/2)/4)==0
seed=[
[(-1,-1,-1,-1,-1),(-1,-1,-1,0,-1),(0,-1,-1,-1,-1),(0,-1,-1,0,-1)],
[(-1,-1,-1,-1,-1),(-1,-1,0,-1,-1),(-1,-1,-1,0,-1),(-1,-1,0,0,-1)],
[(-1,-1,-1,-1,-1),(-1,0,-1,-1,-1),(0,-1,-1,-1,-1),(0,0,-1,-1,-1)]]
def edges(face):return {tuple(sorted((x,y))) for x,y in combinations(face,2) if sum(abs(a-b) for a,b in zip(x,y))==1}
assert len(set.union(*(edges(f) for f in seed)))==10
print("PASS exact SU2 geometric Hessian, zero mode, bad-area moment scalings, 3-face spatial seed")
