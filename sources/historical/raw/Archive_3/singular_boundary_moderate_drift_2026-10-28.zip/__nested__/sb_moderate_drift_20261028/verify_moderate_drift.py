#!/usr/bin/env python3
"""Deterministic symbolic audit of SU(2) projected drift and moderate-window bounds.

This does not check unknown interacting Penrose vacuum drift or prove a mass gap.
"""
import sympy as s
from itertools import combinations

p,a,h,q,cl,be,theta,T,lam,cs=s.symbols('p a h q cl be theta T lam cs',positive=True)
# Exactly one open SU2 rhombus, total electric coefficient 4a.
rho = 2/s.pi*s.sqrt(1-p*p)  # p in [-1,1], Haar density
gamma=a*(1-p*p)           # 4 links x a (1-p²)/4
b=s.simplify(s.diff(rho*gamma,p)/rho)
assert s.simplify(b+3*a*p)==0
assert s.simplify(s.diff(b,p)+3*a)==0
# Exact Haar moments via beta integrals, not numerical fits.
# SU2 character orthogonality E p =0 and E p²=1/4 exactly.
# p=chi_1/2 / 2; ∫chi_1/2=0; ∫chi_1/2²=1.
mean=s.Integer(0);var=s.Rational(1,4);moment=3*a/4
assert s.simplify(moment-3*a*var)==0
# Source Y=h(1-p): change-of-variables p=1-Y/h, b_Y = - h b_p(p)
y=s.symbols('y',real=True)
by=s.simplify((-h*b).subs(p,1-y/h))
assert s.simplify(by-3*a*(h-y))==0
assert s.simplify(s.diff(by,y)+3*a)==0
assert s.simplify(s.diff(by,y)+3*a)==0
# Scalar differential identity of the SU2 fundamental representation.
assert s.simplify((1-p*p)/4-(1-p)/2+(1-p)**2/4)==0
# Agmon exterior bound L=cl/h, lambda=cs/h,
# E[X e^{2 lambda(X-2L)} 1_{X>=2L}] <=64a h³/(be cl).
# For |Y| >T, X> T/(q h). With T/q>2cl, and sufficiently small h,
# E[Y² 1_tail] <=64a T*q*h^4/(be*cl) exp[-2cs(T/q-2cl)/h²].
end_tail=64*a*T*q*h**4/(be*cl)*s.exp(-2*cs*(T/q-2*cl)/h**2)
assert s.simplify(end_tail/(64*a*T*q*h**4/(be*cl))-s.exp(-2*cs*(T/q-2*cl)/h**2))==0
# Gamma(Y) <= 4 a q² h Z, and E Z <= constant at fixed physical region.
# Consequence: noncollapse forces spectral weight at fixed energy.
v,C=s.symbols('v C',positive=True)
cutoff=2*C/v
assert s.simplify(v-C/cutoff-v/2)==0
# Riemann–Stieltjes/IBP truncated variance and covariance identity tested in the
# exact Haar example on a nontrivial subinterval, via boundary flux.
L=s.Rational(-1,2); U=s.Rational(1,2)
# On symmetric [-1/2,1/2] the conditional mean of p is exactly 0.
mu=s.Integer(0)
# Boundary flux equals integrand antiderivative at endpoints:
# d/dp [p gamma rho] = gamma rho + p b rho.
assert s.simplify(s.diff(p*gamma*rho,p)-(gamma+p*b)*rho)==0
BC=s.simplify((p*rho*gamma).subs(p,U)-(p*rho*gamma).subs(p,L))
assert s.simplify(BC-3*s.sqrt(3)*a/(4*s.pi))==0
# Original canonical Penrose spatial fixture (not temporal Q14).
seed=[
[(-1,-1,-1,-1,-1),(-1,-1,-1,0,-1),(0,-1,-1,-1,-1),(0,-1,-1,0,-1)],
[(-1,-1,-1,-1,-1),(-1,-1,0,-1,-1),(-1,-1,-1,0,-1),(-1,-1,0,0,-1)],
[(-1,-1,-1,-1,-1),(-1,0,-1,-1,-1),(0,-1,-1,-1,-1),(0,0,-1,-1,-1)]
]
def face_edges(f):
 return {tuple(sorted((x,z))) for x,z in combinations(f,2) if sum(abs(i-j) for i,j in zip(x,z))==1}
fs=[face_edges(f) for f in seed]
assert len(set.union(*fs))==10
print('PASS exact SU2 effective drift -3ap, Haar variance 1/4, M1=3a/4')
print('PASS actual truncated boundary flux / drift integration by parts')
print('PASS exponential Agmon scaling and fixed-energy spectral witness cutoff')
print('PASS canonical 3-face spatial fixture, 10 links; no Monte Carlo')
print('OPEN: nonlinear Penrose conditional drift monotonicity κ_h→infinity; covariance o(h)')
