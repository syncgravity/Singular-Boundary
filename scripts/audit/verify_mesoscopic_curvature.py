#!/usr/bin/env python3
"""Read-only exact checks for MI-1/MI-3. No Monte Carlo."""
import sympy as s
from itertools import combinations
k,A,B=s.symbols('k A B',positive=True)
F=3*A*k/8+3*B/k
assert s.simplify(s.diff(F,k).subs(k,s.sqrt(8*B/A)))==0
assert s.simplify(F.subs(k,s.sqrt(8*B/A))-3*s.sqrt(A*B)/s.sqrt(2))==0
sm=s.sin(s.pi/5);sp=s.sin(2*s.pi/5);phi=(1+s.sqrt(5))/2
assert s.simplify(sp/sm-phi)==0
h,g=s.symbols('h g',positive=True)
am=g/sm;bm=4/(g*h*h*sm);bn=4/(g*h*h*sp)
lhs=3*s.sqrt(2)*s.sqrt(am*bm)/bn
rhs=3*phi*g*h/s.sqrt(2)
assert s.simplify(s.trigsimp(lhs**2-rhs**2))==0
seed=[
[[-1,-1,-1,-1,-1],[-1,-1,-1,0,-1],[0,-1,-1,-1,-1],[0,-1,-1,0,-1]],
[[-1,-1,-1,-1,-1],[-1,-1,0,-1,-1],[-1,-1,-1,0,-1],[-1,-1,0,0,-1]],
[[-1,-1,-1,-1,-1],[-1,0,-1,-1,-1],[0,-1,-1,-1,-1],[0,0,-1,-1,-1]]]
def edges(z):
 z=list(map(tuple,z));return {tuple(sorted((x,y))) for x,y in combinations(z,2) if sum(abs(i-j) for i,j in zip(x,y))==1}
fs=[edges(z) for z in seed]
assert len(set().union(*fs))==10
for m in range(1,8):
 D={i for i in range(3) if m>>i&1}
 S=set().union(*(fs[i] for i in D))
 C={j for j in range(3) if j not in D and fs[j]&S}
 assert len(S)<=4*len(D) and D.isdisjoint(C)
print("Exact MI regional coefficient and 7 canonical subset checks passed; no simulation.")
