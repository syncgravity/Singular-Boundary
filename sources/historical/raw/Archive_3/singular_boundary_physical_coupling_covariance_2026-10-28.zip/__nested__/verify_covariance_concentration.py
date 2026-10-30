#!/usr/bin/env python3
"""Read-only rational and symbolic audit of finite-coupling covariance arguments.

This script neither simulates a Yang-Mills chain nor substitutes historical data.
It checks the algebraic consequences of the rigorous regional curvature estimate.
"""
from fractions import Fraction as Q
from itertools import product
from math import pi
import json

# Exact covariance for a three-source fully correlated two-point field.
q=Q(1,16)
varp=4*q*(1-q)
h=Q(1,4)
w=(Q(1),Q(2),Q(3))
values=[]
for signs in product((-1,1), repeat=3):
    v=h*h*varp*sum((weights*sign for weights,sign in zip(w,signs)),Q(0))**2
    values.append(v)
assert sum(values,Q(0))/len(values)==h*h*varp*sum((weights**2 for weights in w),Q(0))
assert len(values)==8

# Exact rank-one coherent counterexample: F=m^2, h=1/m, rare all-face flip q=h^2.
coherent=[]
for m in (2,3,4,8,16,64):
    hh=Q(1,m); count=m*m; prob=hh*hh
    mean_deficit=2*prob
    collective_var=4*hh*hh*count*count*prob*(1-prob)
    signed_average=4*hh*hh*count*prob*(1-prob)
    assert collective_var==4*(1-hh*hh)
    assert signed_average==4*hh*hh*(1-hh*hh)
    assert mean_deficit <= 2*hh
    coherent.append({'h':str(hh),'mean_deficit':str(mean_deficit),
                     'smooth_variance':str(collective_var),
                     'random_sign_mean_variance':str(signed_average)})

# Deterministic PSD trace/rank and near-pair inequalities on a rational fixture.
# A rank-one plus diagonal positive covariance matrix: no probabilistic samples.
base=Q(1,8)
C=[[base+ (Q(1,4) if i==j else Q(0)) for j in range(3)] for i in range(3)]
trace=sum(C[i][i] for i in range(3))
for mask in range(8):
    src=[Q(1 if mask>>i&1 else -1) for i in range(3)]
    energy=sum((src[i]*C[i][j]*src[j] for i in range(3) for j in range(3)),Q(0))
    assert energy>=0
assert sum((C[i][j] for i in range(3) for j in range(3) if i==j),Q(0))==trace
# For all PSD covariances, |C_ij| <= (C_ii+C_jj)/2, and the fixture satisfies it.
for i in range(3):
    for j in range(3):
        assert abs(C[i][j])<=(C[i][i]+C[j][j])/2

print(json.dumps({
  'exact_rademacher_sign_patterns':len(values),
  'rademacher_identity':'passed',
  'coherent_example':coherent,
  'positive_covariance_fixture':'passed',
  'physical_penrose_variance_established':False,
  'physical_mass_gap_established':False,
  'simulations_performed':False},indent=2))
