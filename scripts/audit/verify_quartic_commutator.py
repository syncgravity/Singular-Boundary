#!/usr/bin/env python3
"""Exact finite-dimensional parity-resolvent certificate; no stochastic work."""
import sympy as s
from itertools import combinations
n=s.symbols('n',positive=True)
K=s.diag(0,1/n,n)
A=s.Matrix([[0,1/n,0],[1/n,0,1],[0,1,0]])
G=s.diag(0,n,1/n);vac=s.Matrix([1,0,0]);R=s.diag(1,-1,1)
assert R*A*R==-A and R*K==K*R
X=A*vac;Y=G*X;v=(X.T*X)[0];S=A*A*vac-v*vac
t1=s.simplify(4*(S.T*G*A*Y)[0])
t2=s.simplify(2*(Y.T*(A*A-v*s.eye(3))*Y)[0])
t3=s.simplify(-8*(X.T*Y)[0]**2)
assert (t1,t2,t3)==(4/n**2,2,-8/n**2)
assert s.simplify((X.T*K*X)[0]-1/n**3)==0
assert s.simplify((K*A-A*K)[2,1]-(n-1/n))==0
seed=[
[[-1,-1,-1,-1,-1],[-1,-1,-1,0,-1],[0,-1,-1,-1,-1],[0,-1,-1,0,-1]],
[[-1,-1,-1,-1,-1],[-1,-1,0,-1,-1],[-1,-1,-1,0,-1],[-1,-1,0,0,-1]],
[[-1,-1,-1,-1,-1],[-1,0,-1,-1,-1],[0,-1,-1,-1,-1],[0,0,-1,-1,-1]]]
faces=[frozenset(map(tuple,f)) for f in seed]
p=(3,2,1,0,4)
def refl(x):return tuple(x[i] for i in p)
assert [faces.index(frozenset(map(refl,f))) for f in faces]==[0,2,1]
def edges(f):return {tuple(sorted((x,y))) for x,y in combinations(f,2) if sum(abs(a-b) for a,b in zip(x,y))==1}
assert len(set().union(*(edges(f) for f in faces)))==10
print('PASS: parity, quartic response terms, exact commutator, canonical 3-face fixture. No simulations.')
