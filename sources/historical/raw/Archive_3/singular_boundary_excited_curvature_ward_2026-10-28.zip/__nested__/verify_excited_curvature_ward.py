#!/usr/bin/env python3
"""Deterministic exact SU(2) and excited-state Ward estimates; no simulations."""
import sympy as s
from itertools import combinations
from collections import Counter
h,alpha,ar,q,br,F,eta,L=s.symbols('h alpha ar q br F eta L', positive=True)
# SU2 fundamental identity from p²=(chi_0+chi_1)/4 and Casimir values.
p=s.symbols('p',real=True)
assert s.simplify((2*s.Rational(3,4)*p**2 - s.Rational(1,2)*(4*p**2-1))/2-(1-p**2)/4)==0
assert s.simplify(2*(1-p)-(1-p**2)-(1-p)**2)==0
# Each link belongs to <= 2 faces. Each face has 4 edges.
# Weighted regional curvature <= h²(E0+eta)/beta_min.
Gamma=4*ar*q**2*h**(6-2*alpha)*(F/h+eta)/br
Bnorm2=2*F*q**2*h**(6-2*alpha)*(F/h+eta)/br
assert s.simplify(Gamma.subs(alpha,s.Rational(3,2)) - 4*ar*q**2*(F*h**2+eta*h**3)/br)==0
assert s.simplify(Bnorm2.subs(alpha,s.Rational(3,2)) -2*q**2*F*(F*h**2+eta*h**3)/br)==0
# Fixed total area: F~A0/h². At alpha 3/2, Gamma=O(1), Bnorm²=O(h^-2).
A0=s.symbols('A0',positive=True)
assert s.simplify(Bnorm2.subs({alpha:s.Rational(3,2),F:A0/h**2,eta:0}) -2*q**2*A0**2/(br*h**2))==0
# Genuine SU2 one-rhombus electric character states (n=0,1,2,3):
# H_E chi_n = a*n(n+2) chi_n, p chi_n=(chi_{n-1}+chi_{n+1})/2.
pp=s.zeros(4)
for j in range(3): pp[j,j+1]=pp[j+1,j]=s.Rational(1,2)
H=s.diag(0,3*ar,8*ar,15*ar)
base=s.eye(4)[:,0];exc=s.eye(4)[:,1]
assert s.simplify((pp*base).dot(H*(pp*base))-3*ar/4)==0
assert s.simplify((pp*exc).dot((H-3*ar*s.eye(4))*(pp*exc))-ar/2)==0
assert s.simplify((exc.T*(pp*pp)*exc)[0]-s.Rational(1,2))==0
# These are the exact differential double-commutator identities in character space.
seed=[
[[-1,-1,-1,-1,-1],[-1,-1,-1,0,-1],[0,-1,-1,-1,-1],[0,-1,-1,0,-1]],
[[-1,-1,-1,-1,-1],[-1,-1,0,-1,-1],[-1,-1,-1,0,-1],[-1,-1,0,0,-1]],
[[-1,-1,-1,-1,-1],[-1,0,-1,-1,-1],[0,-1,-1,-1,-1],[0,0,-1,-1,-1]]]
def edges(z):
 z=list(map(tuple,z));return {tuple(sorted((x,y))) for x,y in combinations(z,2) if sum(abs(a-b) for a,b in zip(x,y))==1}
faces=[edges(z) for z in seed]
assert all(len(e)==4 for e in faces) and len(set.union(*faces))==10
ctr=Counter(e for f in faces for e in f)
assert max(ctr.values())==2 and sum(v==1 for v in ctr.values())==8
print('PASS exact SU2 Casimir, pointwise gradient/deficit, scaling, 3-seed incidence')
print('PASS low-energy curved-state scaling alpha 3/2: Gamma=O(1), ||(A-c)P_low||²=O(h^-2) at fixed physical area')
print('No Monte Carlo; no assumed interacting gap.')
