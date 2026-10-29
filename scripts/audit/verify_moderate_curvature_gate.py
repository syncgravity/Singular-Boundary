#!/usr/bin/env python3
"""Exact SU2 Haar / moderate-curvature mixture algebra. No Monte Carlo."""
import sympy as s
from itertools import combinations
k=s.symbols('k',positive=True)
Z=s.besseli(1,2*k)/k
r=s.besseli(0,2*k)/s.besseli(1,2*k)-1/k
assert s.simplify(s.diff(Z,k)-2*r*Z)==0
assert s.simplify(s.diff(Z,k,2)/(4*Z)-r**2-s.diff(r,k)/2)==0
h,c1,c2,I,eps=s.symbols('h c1 c2 I eps',positive=True)
dm=s.Rational(3,4)*I*(1/c2-1/c1)/s.sqrt(h)
mix=s.expand(eps*(1-eps)*dm**2)
assert s.simplify(mix.subs({eps:h,c1:1,c2:2,I:1})-s.Rational(9,64)*(1-h))==0
assert s.simplify(mix.subs({eps:s.Rational(1,2),c1:1,c2:2,I:1})-s.Rational(9,256)/h)==0
factor=(2*s.sqrt(c1*c2)/(c1+c2))**s.Rational(3,2)
assert 0<float(factor.subs({c1:1,c2:2}))<1
cl,beta,a,theta=s.symbols('cl beta a theta',positive=True)
L=cl/h
agmon_tail=s.exp(2*theta*h*L)*64*a*h*h/(beta*L)/(2*L)
assert s.simplify(agmon_tail-32*a*s.exp(2*theta*cl)*h**4/(beta*cl**2))==0
seed=[
[(-1,-1,-1,-1,-1),(-1,-1,-1,0,-1),(0,-1,-1,-1,-1),(0,-1,-1,0,-1)],
[(-1,-1,-1,-1,-1),(-1,-1,0,-1,-1),(-1,-1,-1,0,-1),(-1,-1,0,0,-1)],
[(-1,-1,-1,-1,-1),(-1,0,-1,-1,-1),(0,-1,-1,-1,-1),(0,0,-1,-1,-1)]]
def edges(face):
 return {tuple(sorted((x,y))) for x,y in combinations(face,2) if sum(abs(t-u) for t,u in zip(x,y))==1}
assert len(set.union(*(edges(face) for face in seed)))==10
print("PASS: SU2 Bessel/Haar, moderate two-branch variance, Agmon mgf, Penrose fixture")
print("Actual ground-state covariance rate o(h) is OPEN; no stochastic simulations")
