#!/usr/bin/env python3
"""Exact canonical Penrose reflection and finite-matrix response verifier.
Reproduces the checks without Monte Carlo.
"""
from itertools import combinations
import sympy as s
seed=[
[[-1,-1,-1,-1,-1],[-1,-1,-1,0,-1],[0,-1,-1,-1,-1],[0,-1,-1,0,-1]],
[[-1,-1,-1,-1,-1],[-1,-1,-1,0,-1],[-1,-1,0,-1,-1],[-1,-1,0,0,-1]],
[[-1,-1,-1,-1,-1],[-1,0,-1,-1,-1],[0,-1,-1,-1,-1],[0,0,-1,-1,-1]]]
F=[frozenset(map(tuple,f)) for f in seed]
perm=(3,2,1,0,4)
def r(z): return tuple(z[perm[i]] for i in range(5))
assert [F.index(frozenset(map(r,f))) for f in F]==[0,2,1]
def edges(f):return {tuple(sorted((a,b))) for a,b in combinations(f,2) if sum(abs(x-y) for x,y in zip(a,b))==1}
E=set().union(*(edges(f) for f in F))
assert len(E)==10 and {tuple(sorted((r(a),r(b)))) for a,b in E}==E
h,t,d=s.symbols("h t d",positive=True)
K=h**(-s.Rational(5,2));I=s.eye(2);sx=s.Matrix([[0,1],[1,0]]);sz=s.diag(1,-1)
H=d*(I-sx)+K*(I+t*sz)
assert sx*H*sx==H.subs(t,-t)
V=d*d/(d*d+K*K*t*t)
assert V.subs(t,0)==1 and s.diff(V,t).subs(t,0)==0
assert s.simplify(s.diff(V,t,2).subs(t,0)+2*K*K/d**2)==0
assert s.simplify((h**s.Rational(5,2)*s.diff(V,t)/2).subs(t,d/K)+1/(4*d))==0
print("PASS: 3 canonical faces, 10 links, exact reflection, zero odd response at t=0; nearby response spike verified; no Monte Carlo")
