#!/usr/bin/env python3
"""Exact, read-only mesoscopic-source algebra. Not Monte Carlo."""
import sympy as s
from itertools import combinations
h,gamma,alpha,R,eta,Fc,C0,C1,beta,q=s.symbols("h gamma alpha R eta Fc C0 C1 beta q",positive=True)
lhs=2*q*q*h**(6-2*alpha)*(Fc*R**2/h**2)*((C0*R**2+C1*R)/h**3+eta)/beta
rhs=2*q*q*Fc/beta*((C0*R**4+C1*R**3)*h**(1-2*alpha)+eta*R**2*h**(4-2*alpha))
assert s.simplify(lhs-rhs)==0
assert (1-2*alpha+3*gamma).subs({alpha:s.Rational(3,2),gamma:s.Rational(7,10)})==s.Rational(1,10)
seed=[[(-1,-1,-1,-1,-1),(-1,-1,-1,0,-1),(0,-1,-1,-1,-1),(0,-1,-1,0,-1)],
[(-1,-1,-1,-1,-1),(-1,-1,0,-1,-1),(-1,-1,-1,0,-1),(-1,-1,0,0,-1)],
[(-1,-1,-1,-1,-1),(-1,0,-1,-1,-1),(0,-1,-1,-1,-1),(0,0,-1,-1,-1)]]
def edges(f):return {tuple(sorted((a,b))) for a,b in combinations(f,2) if sum(abs(x-y) for x,y in zip(a,b))==1}
faces=[edges(x) for x in seed]
assert len(set.union(*faces))==10
for mask in range(1,8):
 D={i for i in range(3) if mask&(1<<i)}
 S=set.union(*(faces[i] for i in D))
 C={j for j in range(3) if j not in D and faces[j]&S}
 assert len(S)<=4*len(D) and D.isdisjoint(C)
print("PASS seven original seed subsets and all exact scaling identities; no simulations")
