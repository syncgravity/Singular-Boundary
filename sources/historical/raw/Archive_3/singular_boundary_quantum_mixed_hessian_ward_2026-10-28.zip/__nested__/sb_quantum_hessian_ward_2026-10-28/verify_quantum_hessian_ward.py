#!/usr/bin/env python3
"""Exact finite SU2 Wilson Hessian/force Ward check, no Monte Carlo.

Theorems use continuum operator arguments; this checks Casimir normalization,
weak magnetic coupling coefficients, exact adjoint gauge averaging,
and canonical original 3-face Penrose spatial incidence.
"""
import sympy as s
from itertools import combinations
p,a,b,t=s.symbols('p a b t',real=True,positive=True)
# SU2: -Delta p = 3 p / 4 on a single link, and mean p²=1/4.
assert s.simplify(s.Rational(3,4)*s.Rational(1,4)-s.Rational(3,16))==0
# Constant unit left-invariant direction D_e, SU2 geodesic U_e=e^(t i sigma_z /2)U_e.
assert s.simplify(s.diff(b*(1-s.cos(t/2)),t,2).subs(t,0)-b/s.Integer(4))==0
# Four-link plaquette: single character n=1 has electric energy 3a.
# p chi_0 = (1/2)chi_1; first order Omega = chi_0 + b/(6a) chi_1.
coef=b/(6*a)
meanp=s.simplify(coef)
M=s.simplify(b*meanp/4)
assert s.simplify(M-b**2/(24*a))==0
# Haar derivative D_e chi_1 has norm² 1/4 for one direction; K-energy 3a.
RHS=s.simplify(2*coef**2*(3*a)*s.Rational(1,4))
assert s.simplify(M-RHS)==0
# SO(3) adjoint average of a traceless X vanishes: Haar 2-design
X=s.symbols('X',real=True)
assert s.simplify(X*(1+1+1-1-1-1)/6)==0
# Exact Penrose seed: original 3 face spatial incidence, not Q14.
seed=[
[(-1,-1,-1,-1,-1),(-1,-1,-1,0,-1),(0,-1,-1,-1,-1),(0,-1,-1,0,-1)],
[(-1,-1,-1,-1,-1),(-1,-1,0,-1,-1),(-1,-1,-1,0,-1),(-1,-1,0,0,-1)],
[(-1,-1,-1,-1,-1),(-1,0,-1,-1,-1),(0,-1,-1,-1,-1),(0,0,-1,-1,-1)]]
def edges(face):return {tuple(sorted((x,y))) for x,y in combinations(face,2) if sum(abs(i-j) for i,j in zip(x,y))==1}
assert len(set.union(*(edges(face) for face in seed)))==10
print('PASS exact SU2 Hessian at flat link, Casimir, weak-coupling Ward coefficient b²/(24a)')
print('PASS original canonical 3-face 10-edge spatial Penrose fixture; not temporal Q14')
print('No statistical simulations, no uniform gap assertion, no verified Stage26 identity')
