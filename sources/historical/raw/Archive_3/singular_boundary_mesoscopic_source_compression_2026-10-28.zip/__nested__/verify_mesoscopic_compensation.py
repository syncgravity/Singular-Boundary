#!/usr/bin/env python3
"""Deterministic exact regional source norm and coherent-witness checks.

No Monte Carlo and no reconstructed historical samples.
"""
from fractions import Fraction as Q
from itertools import combinations
import sympy as s

seed = [
 [(-1,-1,-1,-1,-1),(-1,-1,-1,0,-1),(0,-1,-1,-1,-1),(0,-1,-1,0,-1)],
 [(-1,-1,-1,-1,-1),(-1,-1,0,-1,-1),(-1,-1,-1,0,-1),(-1,-1,0,0,-1)],
 [(-1,-1,-1,-1,-1),(-1,0,-1,-1,-1),(0,-1,-1,-1,-1),(0,0,-1,-1,-1)]
]
def face_edges(face):
 return {tuple(sorted((a,b))) for a,b in combinations(face,2) if sum(abs(x-y) for x,y in zip(a,b))==1}
faces = [face_edges(z) for z in seed]
assert len(set.union(*faces))==10
for mask in range(1,8):
 D={i for i in range(3) if mask & (1<<i)}
 S=set.union(*(faces[i] for i in D))
 C={j for j in range(3) if j not in D and faces[j]&S}
 assert len(S)<=4*len(D) and len(C)<=2*len(D)

h,gamma,alpha,R,eta,a,b,F,bc,q=s.symbols('h gamma alpha R eta a b F bc q',positive=True)
# E_D <= C0 R^2 h^-3 + C1 R h^-3, F <= Fc R^2 h^-2.
Fc,C0,C1,beta=s.symbols('Fc C0 C1 beta',positive=True)
raw=2*q**2*h**(6-2*alpha)* (Fc*R**2/h**2) * ((C0*R**2+C1*R)/h**3+eta)/beta
expected=(2*q**2*Fc/beta)*((C0*R**4+C1*R**3)*h**(1-2*alpha)+eta*R**2*h**(4-2*alpha))
assert s.simplify(raw-expected)==0
crit=s.expand((1-2*alpha+3*gamma).subs(alpha,s.Rational(3,2)))
assert crit==3*gamma-2
assert crit.subs(gamma,s.Rational(7,10))==s.Rational(1,10)
assert (2*gamma-s.Rational(3,2)).subs(gamma,s.Rational(7,10))==-s.Rational(1,10)
# For gamma=7/10, operator norm diverges while low-energy norm tends to zero.
# Coherent rank-one face probability witness: d_f=Z in {0,1}, with P(Z=1)=h/R.
for m in (100,10000):
 hh=Q(1,m);rr=Q(1,10) if m==100 else Q(1,100)
 ff=round(float(rr**2/hh**2))
 prob=hh/rr
 var=hh*ff**2*prob*(1-prob)
 assert var>0 and prob<1
 # Holder deficit comparison: Var <= E(B^2) <= h F^2 (h/R).
 assert var <= hh*ff**2*prob
print('PASS exact: 7 seed subregions; full low-energy source norm exponents; coherent covariance witness')
print('NO MONTE CARLO. The coherent witness is not an SU(2) Wilson ground state.')
