#!/usr/bin/env python3
"""Exact SU2 one-rhombus vacuum neck check, no Monte Carlo."""
import sympy as s
import mpmath as m
from itertools import combinations
p=s.symbols('p',real=True)
assert s.simplify((1-p*p)/4-(1-p)/2+(1-p)**2/4)==0
m.mp.dps=45
rho=lambda x:2/m.pi*m.sqrt(1-x*x)
pm=m.quad(rho,[m.mpf('0.5'),1])
pp=m.quad(rho,[-1,-m.mpf('0.5')])
pb=m.quad(rho,[-m.mpf('0.5'),m.mpf('0.5')])
assert abs(pm-pp)<m.mpf('1e-40')
assert abs(pm+pp+pb-1)<m.mpf('1e-40')
variance=(pm+pp)/4+m.quad(lambda x:x*x*rho(x),[-m.mpf('0.5'),m.mpf('0.5')])
energy=m.quad(lambda x:(1-x*x)*rho(x),[-m.mpf('0.5'),m.mpf('0.5')])
rayleigh=energy/variance
coarse=6*pb/(pm*pp)
assert 3<rayleigh<coarse
assert abs(float(pm)-(1/3-3**.5/(4*m.pi)))<1e-12
seed=[
[(-1,-1,-1,-1,-1),(-1,-1,-1,0,-1),(0,-1,-1,-1,-1),(0,-1,-1,0,-1)],
[(-1,-1,-1,-1,-1),(-1,-1,0,-1,-1),(-1,-1,-1,0,-1),(-1,-1,0,0,-1)],
[(-1,-1,-1,-1,-1),(-1,0,-1,-1,-1),(0,-1,-1,-1,-1),(0,0,-1,-1,-1)]]
def edges(f):return {tuple(sorted((x,y))) for x,y in combinations(f,2) if sum(abs(a-b) for a,b in zip(x,y))==1}
assert len(set.union(*(edges(f) for f in seed)))==10
print("PASS SU2 Haar, ground-state Dirichlet/Rayleigh, original 3-face fixture. No simulations.")
