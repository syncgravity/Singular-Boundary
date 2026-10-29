#!/usr/bin/env python3
"""Exact deterministic SU2 coherent wavefunction checks. No MCMC."""
import sympy as s
from itertools import combinations
k=s.symbols("k",positive=True)
z=s.besseli(1,2*k)/k
r=s.besseli(0,2*k)/s.besseli(1,2*k)-1/k
assert s.simplify(s.diff(z,k)-2*r*z)==0
e,s0,m,v,vH=s.symbols("eps overlap m v vH",positive=True)
norm=1+2*s.sqrt(e*(1-e))*s0
mean=(1-2*e)*m/norm
second=(m*m+v+2*s.sqrt(e*(1-e))*s0*vH)/norm
assert s.simplify((second-mean**2).subs(s0,0)-(v+4*e*(1-e)*m*m))==0
h,I,p=s.symbols("h I p",positive=True)
variance=s.simplify((4*e*(1-e)*m*m).subs({e:h**p,m:I*h**s.Rational(-3,2)}))
assert s.simplify(variance-4*I*I*h**(p-3)*(1-h**p))==0
assert s.simplify(variance.subs(p,3)-4*I*I*(1-h**3))==0
seed=[
[(-1,-1,-1,-1,-1),(-1,-1,-1,0,-1),(0,-1,-1,-1,-1),(0,-1,-1,0,-1)],
[(-1,-1,-1,-1,-1),(-1,-1,0,-1,-1),(-1,-1,-1,0,-1),(-1,-1,0,0,-1)],
[(-1,-1,-1,-1,-1),(-1,0,-1,-1,-1),(0,-1,-1,-1,-1),(0,0,-1,-1,-1)]]
def edges(face):return {tuple(sorted((x,y))) for x,y in combinations(face,2) if sum(abs(a-b) for a,b in zip(x,y))==1}
assert len(set.union(*(edges(face) for face in seed)))==10
print("PASS exact Bessel Haar normalization, superposition variance, Penrose seed; no simulation")
