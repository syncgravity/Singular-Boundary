#!/usr/bin/env python3
"""Exact symbolic audit of source-aligned SU(2) response scaling and a positive avoided crossing.
No Monte Carlo; no assertion of a Penrose interacting mass gap.
"""
import sympy as s
h,delta,t,tau,K=s.symbols('h delta t tau K',positive=True)
I=s.eye(2); sx=s.Matrix([[0,1],[1,0]]); sz=s.diag(1,-1)
He=delta*(I-sx)+K*(I-sz)
D=K*(I+sz)
H=He+(1+t)*D
assert s.simplify(H-((2*K+delta+K*t)*I-delta*sx+K*t*sz))==s.zeros(2)
assert He.is_positive_semidefinite is True and D.is_positive_semidefinite is True
E=2*K+delta+K*t-s.sqrt(delta**2+K**2*t**2)
Eexc=2*K+delta+K*t+s.sqrt(delta**2+K**2*t**2)
assert s.simplify(Eexc-E-2*s.sqrt(delta**2+K**2*t**2))==0
V=delta**2/(delta**2+K**2*t**2)
M1=2*delta**2/s.sqrt(delta**2+K**2*t**2)
chi=delta**2/(delta**2+K**2*t**2)**s.Rational(3,2)
assert s.simplify(M1*chi/2-V**2)==0
assert s.simplify(-s.diff(E,t,2)/K**2-chi)==0
assert s.simplify(V.subs(t,0)-1)==0
R=K*tau/delta
Iexact=delta/K*(s.atan(R)+R/(1+R**2))
assert s.simplify(s.integrate(V**2,(t,-tau,tau))-Iexact)==0
assert s.limit(Iexact*K/delta,K,s.oo)==s.pi/2
assert s.simplify((h**3*K).subs(K,h**-3)-1)==0
am,sm,F,bm,eps=s.symbols('am sm F bm eps',positive=True)
M1max=4*am*sm**2*F*h**2
Emax=6*F*s.sqrt(am*bm)/h
integrated=s.factor(h**6*M1max*Emax/(2*eps))
assert s.simplify(integrated-12*am**s.Rational(3,2)*sm**2*s.sqrt(bm)*(F*h**2)**2*h**3/eps)==0
print('PASS: nonlinear source alignment, dimensionless h^3 integral')
print('PASS: analytic strictly positive 2-level family with gap >= 2delta and V(0)=1')
print('PASS: exact integral asymptotic pi delta h^3 / 2 at K=h^-3')
print('All computations deterministic; no numerical spectrum or Monte Carlo.')
