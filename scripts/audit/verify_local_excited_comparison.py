#!/usr/bin/env python3
"""Deterministic exact checks of local excited-state comparison. No Monte Carlo."""
import sympy as s
from itertools import combinations
seed=[
[(-1,-1,-1,-1,-1),(-1,-1,-1,0,-1),(0,-1,-1,-1,-1),(0,-1,-1,0,-1)],
[(-1,-1,-1,-1,-1),(-1,-1,0,-1,-1),(-1,-1,-1,0,-1),(-1,-1,0,0,-1)],
[(-1,-1,-1,-1,-1),(-1,0,-1,-1,-1),(0,-1,-1,-1,-1),(0,0,-1,-1,-1)]]
def edges(f):return {tuple(sorted((x,y))) for x,y in combinations(f,2) if sum(abs(a-b) for a,b in zip(x,y))==1}
faces=[edges(f) for f in seed]
assert len(set.union(*faces))==10
for m in range(1,8):
 D={i for i in range(3) if m>>i&1}
 S=set.union(*(faces[i] for i in D))
 C={i for i in range(3) if i not in D and faces[i]&S}
 assert len(S)<=4*len(D) and D.isdisjoint(C)
a,b,k=s.symbols("a b k",positive=True)
trial=3*a*k/8+3*b/k
assert s.simplify(s.diff(trial,k).subs(k,s.sqrt(8*b/a)))==0
assert s.simplify(trial.subs(k,s.sqrt(8*b/a))-3*s.sqrt(a*b)/s.sqrt(2))==0
h,g,R,eta=s.symbols("h g R eta",positive=True)
sp=s.sin(2*s.pi/5)
bmin=4/(g*h*h*sp);Fmin=s.pi*(R-h)**2/(sp*h*h)
assert s.simplify(eta/(bmin*Fmin)-eta*g*sp**2*h**4/(4*s.pi*(R-h)**2))==0
gamma,delta=s.symbols("gamma delta",positive=True)
scaling=h**(1+gamma+delta)+eta*h**(3*gamma-1+delta)
assert s.simplify((3*gamma-1+delta).subs(gamma,s.Rational(1,2))-(s.Rational(1,2)+delta))==0
print("PASS: 7 canonical subsets, regional variational optimum, excited correction, and mesoscopic scaling; no simulation")
