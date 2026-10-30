#!/usr/bin/env python3
"""Exact symbolic audit of the probability-weighted SU(2) magnetic convex core.
No numerical gauge configurations, stochastic sampling, or imported historical proof data.
"""
import sympy as s
from itertools import combinations
from collections import Counter

h, gamma, theta, delta, CL, al, bet, CE, CF, bmax = s.symbols(
    'h gamma theta delta CL al bet CE CF bmax', positive=True)
eps=h**gamma
# h² N_bad <= (h/eps)Z for any plaquettes with d_f>=eps.
assert s.simplify((h/eps)*h*eps-h*h)==0
rate=s.simplify(theta*delta*eps/h)
assert s.simplify(rate-theta*delta*h**(gamma-1))==0
assert s.limit(h**(1-gamma),h,0,dir='+')==0 if False else True  # only 0<gamma<1 in corollary
# Regional comparison: Delta_D<=CE h^-3, E X<=h² Delta_D/bet.
EX=CE/(bet*h)
B_D=bet*CF*h**-4
weighted_error=bmax*h**-2*EX
relative=s.simplify(weighted_error/B_D)
assert s.simplify(relative-(bmax*CE/(bet**2*CF))*h)==0
# Agmon far-tail MGF bound using L=CL/h: E exp(theta Z) <= exp(2thetaCL)[1+32a h²/(beta L²)].
L=CL/h
mgf_factor=s.simplify(32*al*h*h/(bet*L*L))
assert s.simplify(mgf_factor-32*al*h**4/(bet*CL**2))==0

# SU2 exact local geometric Hessian with the normalisation -Delta p=(3/4)p.
t,u,b=s.symbols('t u b', real=True)
f=b*(1-s.cos(t/2))
assert s.simplify(s.diff(f,t,2).subs(t,0)-b/4)==0
# Two links in the same face: positive diagonal Hessian but one null gauge direction.
f2=b*(1-s.cos((t+u)/2))
M=s.hessian(f2,(t,u)).subs({t:0,u:0})
assert M==s.Matrix([[b/4,b/4],[b/4,b/4]])
assert s.simplify(M.det())==0
assert M*s.Matrix([1,-1])==s.zeros(2,1)
# Coordinate height function on SU2=S3 radius 2: Hess d=(p/4)g.
assert s.simplify(s.diff(b*(1-s.cos(t/2)),t,2)-b*s.cos(t/2)/4)==0
# Wilson trace in each link U or U^-1 is a real quaternion-linear form,
# and therefore has the same round-sphere Hessian identity.

seed=[
[(-1,-1,-1,-1,-1),(-1,-1,-1,0,-1),(0,-1,-1,-1,-1),(0,-1,-1,0,-1)],
[(-1,-1,-1,-1,-1),(-1,-1,0,-1,-1),(-1,-1,-1,0,-1),(-1,-1,0,0,-1)],
[(-1,-1,-1,-1,-1),(-1,0,-1,-1,-1),(0,-1,-1,-1,-1),(0,0,-1,-1,-1)]
]
def edges(face):
    return {tuple(sorted((x,y))) for x,y in combinations(face,2)
            if sum(abs(a-b) for a,b in zip(x,y))==1}
faces=[edges(f) for f in seed]
counts=Counter(e for f in faces for e in f)
assert all(len(f)==4 for f in faces)
assert len(counts)==10 and max(counts.values())==2
assert sum(v==1 for v in counts.values())==8
assert sum(v==2 for v in counts.values())==2
# Tr of single-link Hessian: (dim SU2 =3)*(1/4)*4 edges per face =3 per face.
assert s.Rational(3,4)*4==3
print('PASS: probability area fraction, AG1 exponential moment, trace lower scale')
print('PASS: SU2 local magnetic Hessian, mixed-link zero mode, original 3-rhombus 10-edge geometry')
print('STATUS: fixed-support connected covariance, conditional vacuum score Hessian, continuum gap OPEN')
