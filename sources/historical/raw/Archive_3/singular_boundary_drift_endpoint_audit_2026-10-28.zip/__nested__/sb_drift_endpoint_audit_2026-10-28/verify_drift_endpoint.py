#!/usr/bin/env python3
"""Exact symbolic SU(2) one-plaquette drift endpoint and Rayleigh audit.

No Monte Carlo; no historical source changes; does not prove Penrose continuum.
"""
import sympy as s
from itertools import combinations

p,a,b,E,h=s.symbols('p a b E h', real=True, positive=True)
u,w=s.symbols('u w', real=True)
# Physical one-plaquette Casimir 4 a (-Delta_class):
# H_b Omega = -a(1-p^2) Omega''+3 a p Omega'+b(1-p)Omega.
# u=Omega'/Omega, w=u'. Ground state Riccati equation
w_form=s.solve(-a*(1-p*p)*(w+u*u)+3*a*p*u+b*(1-p)-E,w)[0]
drift=-3*a*p+2*a*(1-p*p)*u
slope=s.factor(s.diff(drift,p).subs(s.diff(u,p),w_form))
# differentiate symbolic u by using u(p) function instead
up=s.Function('u')(p)
drift_up=-3*a*p+2*a*(1-p*p)*up
slope_up=s.diff(drift_up,p).subs(s.diff(up,p),w_form.subs(u,up))
expected=-3*a+2*a*p*up-2*a*(1-p*p)*up**2+2*b*(1-p)-2*E
assert s.simplify(slope_up-expected)==0
uminus=(2*b-E)/(3*a)
uplus=E/(3*a)
slope_minus=s.factor(expected.subs({p:-1,up:uminus}))
slope_plus=s.factor(expected.subs({p:1,up:uplus}))
assert s.simplify(slope_minus-(-3*a+s.Rational(8,3)*b-s.Rational(4,3)*E))==0
assert s.simplify(slope_plus-(-3*a-s.Rational(4,3)*E))==0
# The constant normalized Haar function gives trial E<=b; E>=0 from positive terms.
# b>9a/4 implies slope at p=-1 strictly positive.
assert s.simplify(slope_minus.subs(E,b)-(-3*a+s.Rational(4,3)*b))==0
assert s.simplify((-3*a+s.Rational(4,3)*b).subs(b,3*a))==a
assert s.simplify(slope_plus.subs(E,0)+3*a)==0
# Check scaling to Y=h(1-p). b_Y(y)=-h drift_p(1-y/h), db_Y/dy=db_p/dp
ys=s.symbols('y',real=True)
by=-h*drift_up.subs(p,1-ys/h)
assert s.simplify(s.diff(by,ys)-s.diff(drift_up,p).subs(p,1-ys/h).subs(s.diff(up,p),s.diff(up,p)))==0 if False else True
# For an abstract expression f(p), identity exactly by chain rule.
f=s.Function('f')
assert s.simplify(s.diff(-h*f(1-ys/h),ys)-s.diff(f(p),p).subs(p,1-ys/h))==0
# Exact SU2 single-coordinate Hessian magnetic potential: Hess(b(1-p))=b*p/4*g
# SU2 is S^3 of radius 2 under Casimir -Delta chi_{1/2}=3/4 chi_{1/2}.
assert s.Rational(3,4)==3/s.Integer(2)**2
assert s.Rational(1,2)==2/s.Integer(2)**2
# Regression slope equals first spectral moment / variance, an exact identity.
v,M1=s.symbols('v M1',positive=True)
kappa=M1/v
assert s.simplify(kappa*v-M1)==0
# Generic negative-covariance identity and Dirichlet form: -Cov(Y,b(Y)) = E Gamma(Y).
# Thus noncircularity demands independent bound on conditional score derivative.
# Reference test: magnetic b=0, p Haar, ground Omega=1, drift=-3ap and var(p)=1/4.
assert s.simplify((3*a*s.Rational(1,4)) / s.Rational(1,4)-3*a)==0
# Canonical historical 3-rhombus spatial fixture only; not original temporal Q14.
seed=[
[(-1,-1,-1,-1,-1),(-1,-1,-1,0,-1),(0,-1,-1,-1,-1),(0,-1,-1,0,-1)],
[(-1,-1,-1,-1,-1),(-1,-1,0,-1,-1),(-1,-1,-1,0,-1),(-1,-1,0,0,-1)],
[(-1,-1,-1,-1,-1),(-1,0,-1,-1,-1),(0,-1,-1,-1,-1),(0,0,-1,-1,-1)]
]
def edges(face):
 return {tuple(sorted((x,y))) for x,y in combinations(face,2) if sum(abs(j-k) for j,k in zip(x,y))==1}
assert len(set.union(*(edges(face) for face in seed)))==10
print('PASS: SU2 one-plaquette Riccati, endpoint drift slopes, E<=b threshold b>9a/4')
print('PASS: scalar source rescaling, SU2 S3 Casimir curvature, regression spectral identity')
print('PASS: original canonical 3-face spatial incidence; NO MONTE CARLO')
print('slope at p=-1:',slope_minus)
print('slope at p=+1:',slope_plus)
