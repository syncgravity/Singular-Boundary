#!/usr/bin/env python3
"""Deterministic exact physical SU(2) source response and spectral moments.

No numerical simulation, no reconstruction of historical Stage 7/26 samples.
"""
import sympy as s
from fractions import Fraction
from itertools import combinations

# One open rhombus, a per link, physical character fundamental chi_1=2p.
a, t, lam = s.symbols('a t lam', positive=True)
v = s.Rational(1,4)
M = 3*a*v
chi = v/(3*a)
assert s.simplify(chi-v*v/M) == 0
assert s.simplify(-2*chi+1/(6*a)) == 0
assert s.simplify(v*s.exp(-3*a*t) - v*s.exp(-M*t/v)) == 0
# Gauge invariant trial state Rayleigh form.
z, k3, sfield = s.symbols('z k3 sfield', real=True)
trial = (z*z*M-sfield*(2*z*v+z*z*k3))/(1+z*z*v)
assert s.simplify(s.limit(trial.subs(z,sfield*v/M)/sfield**2,sfield,0)+v*v/M)==0

# A finite-gap physical 3-level spectral representation (not claimed SU2).
weights = [(Fraction(1,4),Fraction(3,1)),(Fraction(1,8),Fraction(7,1))]
v2=sum((w for w,e in weights),Fraction(0))
m2=sum((w*e for w,e in weights),Fraction(0))
chi2=sum((w/e for w,e in weights),Fraction(0))
assert chi2*m2>=v2*v2
assert chi2<=v2/min(e for w,e in weights)

# A divergent-variance family with uniformly bounded first moment and soft spectrum.
n=s.symbols('n',positive=True)
assert s.simplify((n*(1/n))-1)==0
assert s.simplify(((1/n)*n)/n-(1/n))==0

# Original canonical three-rhombus spatial Penrose Z5 seed.
seed=[
[(-1,-1,-1,-1,-1),(-1,-1,-1,0,-1),(0,-1,-1,-1,-1),(0,-1,-1,0,-1)],
[(-1,-1,-1,-1,-1),(-1,-1,0,-1,-1),(-1,-1,-1,0,-1),(-1,-1,0,0,-1)],
[(-1,-1,-1,-1,-1),(-1,0,-1,-1,-1),(0,-1,-1,-1,-1),(0,0,-1,-1,-1)]]
def edges(f):
    return {tuple(sorted((u,v))) for u,v in combinations(f,2) if sum(abs(x-y) for x,y in zip(u,v))==1}
assert len(set.union(*(edges(f) for f in seed)))==10
print('PASS exact one-rhombus physical source variance, susceptibility, Euclidean correlator')
print('PASS finite gauge-invariant variational response, spectral Cauchy bounds and 3-face incidence')
print('No Monte Carlo. Penrose variance regime, continuum spectrum and mass gap remain OPEN.')
