#!/usr/bin/env python3
"""Exact/symbolic checks for product-link variational curvature bound.
No MCMC, no historical data modifications. Requires sympy.
"""
import json
import sympy as s
from fractions import Fraction as Q
k, A, B, a, b, h, g2 = s.symbols('k A B a b h g2', positive=True)
phi = (s.sqrt(5)+1)/2
sigminus = s.sin(s.pi/5)
sigplus = s.sin(2*s.pi/5)
assert s.simplify(sigplus/sigminus-phi)==0
# Electric trial bound and magnetic trial bound.
F = s.Rational(3,8)*A*k + 3*B/k
kopt=s.sqrt(8*B/A)
assert s.simplify(s.diff(F,k).subs(k,kopt))==0
assert s.simplify(F.subs(k,kopt)-(3/s.sqrt(2))*s.sqrt(A*B))==0
# For uniform a,b and at most 4 edges per face, mean magnetic deficit.
mean_bound = s.simplify((3/s.sqrt(2))*s.sqrt(4*a*b)/b)
assert s.simplify(mean_bound -3*s.sqrt(2)*s.sqrt(a/b))==0
# For the specified physical Penrose coefficient envelope, |E|/|F| <=4.
sm,sp=s.symbols("sigma_minus sigma_plus",positive=True)
Amax=4*g2/sm
Bmax=4/(g2*h**2*sm)
bmin=4/(g2*h**2*sp)
geom = s.simplify((3/s.sqrt(2))*s.sqrt(Amax*Bmax)/bmin)
assert s.simplify(geom-(3/s.sqrt(2))*(sp/sm)*g2*h)==0
assert s.simplify(sigplus/sigminus-phi)==0
# A pointwise counterexample: F-face disk, 2 nonflat based faces, others flat.
# u1=(1,0,0), u2=(0,1,0); v1=v2=1/sqrt(2).
# |SA x SB|^2=1/4 and 64 times this =16.
Fcount = s.symbols('Fcount', positive=True, integer=True)
point_deficit = 2/Fcount
point_torque = s.Integer(16)
assert s.simplify(point_torque/point_deficit - 8*Fcount)==0
# Tiny incidence: 3 seed faces, 10 distinct links, 8 boundary links.
seed=[
[[-1,-1,-1,-1,-1],[-1,-1,-1,0,-1],[0,-1,-1,-1,-1],[0,-1,-1,0,-1]],
[[-1,-1,-1,-1,-1],[-1,-1,-1,0,-1],[-1,-1,0,-1,-1],[-1,-1,0,0,-1]],
[[-1,-1,-1,-1,-1],[-1,0,-1,-1,-1],[0,-1,-1,-1,-1],[0,0,-1,-1,-1]]]
from itertools import combinations
from collections import Counter
def dist(x,y):return sum(abs(a-b) for a,b in zip(x,y))
def edges(face):
    z=[tuple(v) for v in face]
    return {tuple(sorted((u,v))) for u,v in combinations(z,2) if dist(u,v)==1}
faces=[edges(t) for t in seed]
inc=Counter(e for f in faces for e in f)
assert len(inc)==10 and sum(d==1 for d in inc.values())==8
assert all(d<=2 for d in inc.values())
print(json.dumps({
 'product_trial_optimized_energy_bound':'3/sqrt(2) sqrt[(sum a_e)(sum b_f)]',
 'uniform_mean_curvature_bound':'3 sqrt(2) sqrt(a/b)',
 'geometric_mean_curvature_bound':'(3/sqrt(2)) phi g3^2 h',
 'pointwise_obstruction_torque_over_mean_deficit':'8 F',
 'canonical_seed':{'faces':3,'edges':len(inc),'boundary_edges':8},
 'simulations':False,'interacting_gap_proved':False
},indent=2))
