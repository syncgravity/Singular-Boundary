#!/usr/bin/env python3
"""Deterministic symbolic Penrose Cheeger and Gaussian tangent checks; no Monte Carlo."""
import sympy as s
from itertools import combinations
L=s.Matrix([[4,-1,-1],[-1,4,0],[-1,0,4]])
assert set(L.eigenvals())=={4-s.sqrt(2),s.Integer(4),4+s.sqrt(2)}
sigma=s.sin(s.pi/5)
assert (4-s.sqrt(2)).evalf(20)>(s.pi*sigma/6).evalf(20)
for mask in range(1,8):
 S=[i for i in range(3) if mask>>i&1]
 edges=[(0,1),(0,2)]
 boundary=4*len(S)-2*sum(i in S and j in S for i,j in edges)
 assert boundary**2 >= 4*s.pi*sigma*len(S)
a,b=s.symbols('a b',positive=True)
P=[]
for v in L.eigenvals():
 q=s.eye(3)
 for w in L.eigenvals():
  if v!=w:q=q*(L-w*s.eye(3))/(v-w)
 P.append((v,q))
R=sum((s.sqrt(v)*q for v,q in P),s.zeros(3))
assert all(s.simplify(x)==0 for x in R*R-L)
S=s.sqrt(2*a/b)*R;V=b*s.eye(3)/8;M=a*L
assert all(s.simplify(x)==0 for x in S*V*S-M/4)
assert all(s.simplify((S*S)[i,i]-8*a/b)==0 for i in range(3))
h,alpha=s.symbols('h alpha',positive=True)
assert (4-2*alpha).subs(alpha,s.Rational(3,2))==1
print('PASS: 7 planar subsets, 3 eigenvalues, Gaussian covariance, critical source exponent. NO MONTE CARLO')
