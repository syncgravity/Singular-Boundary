#!/usr/bin/env python3
"""Exact SU2 local curvature, spectral scaling and 3-seed checks. No simulations."""
import sympy as s
from itertools import combinations
from collections import Counter
p,h,alpha,a,q,b,F,eta,A0=s.symbols("p h alpha a q b F eta A0",positive=True)
assert s.simplify((s.Rational(3,2)*p**2-s.Rational(1,2)*(4*p**2-1))/2-(1-p**2)/4)==0
assert s.simplify(2*(1-p)-(1-p*p)-(1-p)**2)==0
bound=2*q*q*h**(6-2*alpha)*(F/h+eta)*(2*a+eta*F)/(b*h**(-1-s.Rational(1,2)))
special=s.simplify(bound.subs({alpha:s.Rational(3,2),F:A0/h**2,eta:h}))
assert s.limit(special,h,0)==0
P=s.zeros(4)
for j in range(3):P[j,j+1]=P[j+1,j]=s.Rational(1,2)
H=s.diag(0,3*a,8*a,15*a)
vac=s.eye(4)[:,0];exc=s.eye(4)[:,1]
assert s.simplify((P*vac).dot(H*(P*vac))-3*a/4)==0
assert s.simplify((P*exc).dot((H-3*a*s.eye(4))*(P*exc))-a/2)==0
seed=[
[[-1,-1,-1,-1,-1],[-1,-1,-1,0,-1],[0,-1,-1,-1,-1],[0,-1,-1,0,-1]],
[[-1,-1,-1,-1,-1],[-1,-1,0,-1,-1],[-1,-1,-1,0,-1],[-1,-1,0,0,-1]],
[[-1,-1,-1,-1,-1],[-1,0,-1,-1,-1],[0,-1,-1,-1,-1],[0,0,-1,-1,-1]]]
def edges(f):
 v=list(map(tuple,f))
 return {tuple(sorted((x,y))) for x,y in combinations(v,2) if sum(abs(i-j) for i,j in zip(x,y))==1}
faces=[edges(z) for z in seed]
counts=Counter(e for f in faces for e in f)
assert len(counts)==10 and max(counts.values())==2 and sum(x==1 for x in counts.values())==8
print("PASS SU2 Casimir, character excitation, scaling and Penrose local incidence; no Monte Carlo.")
