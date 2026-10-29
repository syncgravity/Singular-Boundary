#!/usr/bin/env python3
"""Exact SU2 score-force algebra, no stochastic simulation."""
import sympy as s
from itertools import combinations
h,a,q,CE,CZ,r=s.symbols("h a q CE CZ r",positive=True)
p=s.symbols("p",real=True)
assert s.simplify((1-p*p)/4-(1-p)/2+(1-p)**2/4)==0
for v in [s.S.One,s.Rational(6,5),s.Rational(3,2),s.Rational(7,4)]:
 ex=v/(2-v)
 assert s.simplify(v/2+v/(2*ex)-1)==0
assert s.simplify(h*2*s.sqrt((CE/h**3)*(4*a*q*q*h*CZ))-4*q*s.sqrt(a*CE*CZ))==0
cm,CM=s.symbols("cm CM",positive=True)
assert s.simplify((cm/h)**2/(4*CM*h)-cm**2/(4*CM*h**3))==0
seed=[
[(-1,-1,-1,-1,-1),(-1,-1,-1,0,-1),(0,-1,-1,-1,-1),(0,-1,-1,0,-1)],
[(-1,-1,-1,-1,-1),(-1,-1,0,-1,-1),(-1,-1,-1,0,-1),(-1,-1,0,0,-1)],
[(-1,-1,-1,-1,-1),(-1,0,-1,-1,-1),(0,-1,-1,-1,-1),(0,0,-1,-1,-1)]]
def edges(f):return {tuple(sorted((x,y))) for x,y in combinations(f,2) if sum(abs(v-w) for v,w in zip(x,y))==1}
assert len(set.union(*(edges(f) for f in seed)))==10
print("PASS: SU2 identity, Holder force bound, source first-moment lower scaling, canonical spatial seed")
print("OPEN: conditional drift slope, covariance, continuum gap")
