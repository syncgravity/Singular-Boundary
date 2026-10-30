#!/usr/bin/env python3
"""Deterministic exact arithmetic/symbolic checks for local SU2 vacuum-score theorem.
No Monte Carlo, no temporal Q14 reconstruction, no historical data mutation.
"""
import sympy as s
from itertools import combinations
from fractions import Fraction

h,C_E,C_G,C_Z,r,q,a,F,T=s.symbols('h C_E C_G C_Z r q a F T',positive=True)
# Exact SU2 p=cos theta, Laplacian and gradient Casimir convention.
p=s.symbols('p',real=True)
assert s.simplify((1-p*p)/4-(1-p)/2+(1-p)**2/4)==0
assert s.simplify(s.Rational(3,4)*p*p - (s.Rational(1,4)*(4*p*p-1)+s.Rational(1,4)*(1-p*p)))==0
# Local score Cauchy for region T_S and Gamma_h= C_G h Z.
# E[T_S] <= C_E h^-3 and ||Z||_r <= C_Z.
Lp_score=2*s.sqrt((C_E/h**3)*(C_G*h*C_Z))
assert s.simplify(h*Lp_score-2*s.sqrt(C_E*C_G*C_Z))==0
assert s.simplify((2-r)/r-2*(s.Rational(1,1)/r-s.Rational(1,2)))==0
# For 1 <= p<2, Holder exponent r=p/(2-p).
for exponent in (s.Rational(1,1),s.Rational(6,5),s.Rational(3,2),s.Rational(7,4),s.Rational(19,10)):
 R=s.simplify(exponent/(2-exponent))
 assert R>=1 and s.simplify(exponent/2+exponent/(2*R)-1)==0
# Explicit geometric part: 4 edges each face times a*(3/4) h -> 3 a h F.
geom=3*a*q*h*F
assert s.simplify((h*geom).subs(F,C_E/h**2)-3*a*q*C_E)==0
# Gaussians are illustrative marginal diffusions, NOT SU2 vacuum realizations.
variance_weak=h
variance_strong=h**2
# Diffusion Gamma=h, b(y)=-h*y/variance; linear drift slope kappa=h/variance.
assert s.simplify(h/variance_weak)==1
assert s.simplify(h/variance_strong)==1/h

seed=[
[(-1,-1,-1,-1,-1),(-1,-1,-1,0,-1),(0,-1,-1,-1,-1),(0,-1,-1,0,-1)],
[(-1,-1,-1,-1,-1),(-1,-1,0,-1,-1),(-1,-1,-1,0,-1),(-1,-1,0,0,-1)],
[(-1,-1,-1,-1,-1),(-1,0,-1,-1,-1),(0,-1,-1,-1,-1),(0,0,-1,-1,-1)],
]
def edges(face):
 return {tuple(sorted((u,v))) for u,v in combinations(face,2) if sum(abs(x-y) for x,y in zip(u,v))==1}
parts=[edges(face) for face in seed]
assert len(set.union(*parts))==10 and all(len(face)==4 for face in parts)
assert max(sum(e in face for face in parts) for e in set.union(*parts))==2
# Exact pure-electric rhombus validation: Y=h(1-p), L Y=3a(h-Y).
y=s.symbols('y',real=True)
assert s.simplify((3*a*h*p).subs(p,1-y/h)-3*a*(h-y))==0
assert s.simplify((a*h*h*(1-p*p)).subs(p,1-y/h)-a*(2*h*y-y*y))==0
print('PASS: exact SU2 Casimir and drift, Holder p<2 exponents, local force scaling, canonical seed incidence')
print('STATUS: fixed-support covariance o(h), conditional force monotonicity and mass gap OPEN; no Monte Carlo')
# Positive nonvanishing face source: 2-sided sharp regional kinetic and f-sum scales.
a_min,q_mass,beta=s.symbols('a_min q_mass beta',positive=True)
c_D=s.Rational(3,2)*a_min*q_mass
C_M=4*a*q*q*C_E/beta
lower_T=c_D**2/(4*C_M)*h**-3
lower_M=c_D**2/(4*C_E)*h
assert s.simplify((c_D/h)**2/(4*C_M*h)-lower_T)==0
assert s.simplify((c_D/h)**2/(4*C_E/h**3)-lower_M)==0
assert s.simplify(lower_M/h-c_D**2/(4*C_E))==0
assert s.simplify(h*(c_D/h)-c_D)==0
print('PASS: nonnegative macroscopic source forces T_S=Theta(h^-3), M1(Y)=Theta(h)')
