#!/usr/bin/env python3
"""Exact SU2 one-plaquette nonlinear drift verification; no Monte Carlo."""
import sympy as s
p,a,b,E=s.symbols('p a b E',positive=True)
u=s.Function('u')(p)
drift=-3*a*p+2*a*(1-p*p)*u
riccati=(3*a*p*u+b*(1-p)-E)/(a*(1-p*p))-u*u
slope=s.simplify(s.diff(drift,p).subs(s.diff(u,p),riccati))
expect=-3*a+2*a*p*u-2*a*(1-p*p)*u*u+2*b*(1-p)-2*E
assert s.simplify(slope-expect)==0
assert s.simplify(expect.subs({p:-1,u:(2*b-E)/(3*a)})-(-3*a+8*b/3-4*E/3))==0
assert s.simplify(expect.subs({p:1,u:E/(3*a)})-(-3*a-4*E/3))==0
assert s.simplify((-3*a+8*b/3-4*E/3).subs(E,b)-(-3*a+4*b/3))==0
h,y=s.symbols('h y',positive=True)
f=s.Function('f')
assert s.simplify(s.diff(-h*f(1-y/h),y)-s.diff(f(p),p).subs(p,1-y/h))==0
print("PASS SU2 interacting Riccati and force endpoint sign, source scaling; no simulations")
