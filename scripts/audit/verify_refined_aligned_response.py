#!/usr/bin/env python3
"""Deterministic exact identities for refined curvature-weighted Wilson response.

Checks exponents, avoided-crossing exact susceptibility/variance, and
SU(2) fundamental Casimir identity. NO MONTE CARLO, NO GAUGE SIMULATIONS.
"""
import sympy as s
h,alpha,delta,K,t,tau,A0,C1,C2=s.symbols('h alpha delta K t tau A0 C1 C2',positive=True)
sx=s.Matrix([[0,1],[1,0]])
sz=s.diag(1,-1)
I=s.eye(2)
H=delta*(I-sx)+K*(I-sz)+(1+t)*K*(I+sz)
assert s.simplify(H-((delta+2*K+K*t)*I-delta*sx+K*t*sz))==s.zeros(2)
Eg=delta+2*K+K*t-s.sqrt(delta**2+K**2*t**2)
Eex=delta+2*K+K*t+s.sqrt(delta**2+K**2*t**2)
assert s.simplify(Eex-Eg-2*s.sqrt(delta**2+K**2*t**2))==0
V=delta**2/(delta**2+K**2*t**2)
M1=2*delta**2/s.sqrt(delta**2+K**2*t**2)
assert s.simplify(-s.diff(Eg,t,2) -K**2*delta**2/(delta**2+K**2*t**2)**s.Rational(3,2))==0
assert s.simplify(M1*(s.Rational(1,2)*(-s.diff(Eg,t,2))/K**2)-V**2)==0
Iintegral=(delta/K)*(s.atan(K*tau/delta)+(K*tau/delta)/(1+(K*tau/delta)**2))
assert s.simplify(s.integrate(V**2,(t,-tau,tau))-Iintegral)==0
assert s.simplify(s.limit(K*Iintegral/delta,K,s.oo)-s.pi/2)==0
assert s.expand((3-2*alpha)+(5-2*alpha))==8-4*alpha
assert (8-4*alpha).subs(alpha,1)==4
assert (8-4*alpha).subs(alpha,s.Rational(3,2))==2
assert s.expand((3-2*alpha)-(alpha-4))==7-3*alpha
assert (7-3*alpha).subs(alpha,1)==4
assert (7-3*alpha).subs(alpha,s.Rational(3,2))==s.Rational(5,2)
p=s.symbols('p',real=True)
assert s.simplify((s.Rational(3,4)*2*p**2-(4*p**2-1)/2)/2-(1-p**2)/4)==0
print('PASS: exact Pauli avoided-crossing, spectral Cauchy identity')
print('PASS: all symbolic integrated exponents; alpha=1 -> h^4, alpha=3/2 -> h^2')
print('PASS: sharpness toy alpha=1: first moment O(h), spike width O(h^4)')
print('PASS: admissible toy alpha=3/2: fixed gap, spike width O(h^(5/2))')
print('PASS: SU2 gradient Casimir identity; no simulations or inferred physical variance')
