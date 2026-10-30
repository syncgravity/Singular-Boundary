#!/usr/bin/env python3
"""Exact symbolic validation of source-aligned response and avoided-crossing countertest.
No simulation, no Monte Carlo, and no historical files modified.
"""
import sympy as s
h,delta,t,tau,K=s.symbols('h delta t tau K', positive=True)
I=s.eye(2); sx=s.Matrix([[0,1],[1,0]]); sz=s.diag(1,-1)
He=delta*(I-sx)+K*(I-sz)
D=K*(I+sz)
H=He+(1+t)*D
assert s.simplify(H-((2*K+delta+K*t)*I-delta*sx+K*t*sz))==s.zeros(2)
assert He.is_positive_semidefinite is True
assert D.is_positive_semidefinite is True
E=(2*K+delta+K*t)-s.sqrt(delta**2+(K*t)**2)
Eexc=(2*K+delta+K*t)+s.sqrt(delta**2+(K*t)**2)
assert s.simplify(Eexc-E-2*s.sqrt(delta**2+K**2*t**2))==0
V=delta**2/(delta**2+K**2*t**2)
M1=2*delta**2/s.sqrt(delta**2+K**2*t**2)
chi=delta**2/(delta**2+K**2*t**2)**s.Rational(3,2)
assert s.simplify(M1*chi/2-V**2)==0
assert s.simplify(-s.diff(E,t,2)/K**2-chi)==0
assert s.simplify(V.subs(t,0)-1)==0
assert s.simplify(s.diff(V,t).subs(t,0))==0
# curvature is sharply localized, despite analytic family and gap >= 2delta
R=K*tau/delta
Iexact=delta/K*(s.atan(R)+R/(1+R**2))
assert s.simplify(s.integrate(V**2,(t,-tau,tau))-Iexact)==0
assert s.limit(Iexact*K/delta,K,s.oo)==s.pi/2
# source = -h^3 d_t H, so K=h^-3 gives a bounded field A=-(I+sz)
assert s.simplify((h**3*K).subs(K,h**-3)-1)==0
# in two-parameter result, 1D ray exploits exact alignment of the source
Amax,sigmamax,F,betamax,lam = s.symbols('Amax sigmamax F betamax lam',positive=True)
M1max=4*Amax*sigmamax**2*F*h**2
Emax=6*F*s.sqrt(Amax*betamax)/h
integrated=s.factor(h**6*M1max*Emax/(2*lam))
assert s.simplify(integrated-12*Amax**s.Rational(3,2)*sigmamax**2*s.sqrt(betamax)*(F*h**2)**2*h**3/lam)==0
print('PASS: source-aligned susceptibility identity, dimensionless h^3 integrated bound')
print('PASS: strictly positive avoided crossing with V(0)=1 and gap >=2 delta')
print('PASS: exact integral asymptotic (pi delta/2) h^3 at K=h^-3')
print('PASS: critical response growth order h^-3 is sharp for these abstract data')
print('No Gaussian or nonlinear Penrose spectral gap is inferred.')
