#!/usr/bin/env python3
"""Deterministic proof-constant/SU(2) incidence and spectral algebra audit. No Monte Carlo.

Checks are algebraic necessary conditions, not a computer proof of all form-domain steps.
"""
import sympy as s
from fractions import Fraction
from itertools import combinations

h,theta,a,CE,CF,q,M1,M2,mstar=s.symbols('h theta a CE CF q M1 M2 mstar',positive=True)
Z, beta, dd=s.symbols('Z beta dd',positive=True)
p=s.symbols('p',real=True)
# SU2 normalized class function gradient and curvature inequality
assert s.simplify((1-p*p)/4 - (1-p)/2 + (1-p)**2/4)==0
# For f=exp(theta Z), Gamma(f)<= 4 a theta^2 h Z exp(2theta Z)
GammaZ=4*a*h*Z
f=s.exp(theta*Z)
assert s.simplify(s.diff(f,Z)**2*GammaZ - 4*a*h*theta**2*Z*s.exp(2*theta*Z))==0
# IMS: ||f grad Omega||^2 <= 2 ||grad(fOmega)||^2 +2 ||Omega grad f||^2
x,y=s.symbols('x y',real=True)
assert s.simplify(2*(x+y)**2+2*y**2-x**2-(x+2*y)**2)==0
# Exp(sZ) weighted-score estimate with s=1 gives 2 Delta M1 +4a h M2
slope=s.symbols('slope',positive=True)
scorerhs=2*CE*h**(-3)*M1 + 4*a*h*M2
normalized=s.simplify(h**3*scorerhs)
assert normalized==2*CE*M1+4*a*M2*h**4
# second moment M2(A) = (1/h^3) E[(h L Y)^2]
LY=s.symbols('LY',real=True)
assert s.simplify((LY/s.sqrt(h))**2 - (h*LY)**2/h**3)==0
# moment lower bounds and spectral cutoff
C=s.symbols('C',positive=True)
Lambda=2*C*h**(-3)/mstar
assert s.simplify(C*h**(-3)/Lambda-mstar/2)==0
assert s.simplify((mstar/2)/Lambda-mstar**2*h**3/(4*C))==0
# exact 3-rhombus spatial incidence, not temporal Q14
seed=[
[(-1,-1,-1,-1,-1),(-1,-1,-1,0,-1),(0,-1,-1,-1,-1),(0,-1,-1,0,-1)],
[(-1,-1,-1,-1,-1),(-1,-1,0,-1,-1),(-1,-1,-1,0,-1),(-1,-1,0,0,-1)],
[(-1,-1,-1,-1,-1),(-1,0,-1,-1,-1),(0,-1,-1,-1,-1),(0,0,-1,-1,-1)]]
def edges(face):
    return {tuple(sorted((x,y))) for x,y in combinations(face,2) if sum(abs(a-b) for a,b in zip(x,y))==1}
faces=[edges(f) for f in seed]
S=set.union(*faces)
assert len(S)==10 and all(len(f)==4 for f in faces)
assert max(sum(e in f for f in faces) for e in S)==2
print('PASS: SU2 Casimir, exponential chain rule, weighted IMS square, h scaling, spectral Chebyshev, 3-face seed')
print('No Monte Carlo and no numerical vacuum or mass gap claim')
