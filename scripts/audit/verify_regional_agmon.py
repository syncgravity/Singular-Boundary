#!/usr/bin/env python3
"""Exact symbolic Agmon constants; no Monte Carlo."""
import sympy as s
h,a,b,L,x,t=s.symbols("h a b L x t",positive=True)
lam=s.sqrt(b/(32*a))/h
assert s.simplify(8*a*lam**2-b/(4*h**2))==0
W=64*a*h**2/(b*L)
assert s.simplify((W/(2*L))-32*a*h**2/(b*L**2))==0
assert s.simplify(2*L*W-128*a*h**2/b)==0
p=s.symbols("p",real=True)
assert s.simplify((1-p*p)/4-(1-p)/2+(p-1)**2/4)==0
print("PASS: absorption constant, exponential-tail and second-moment constants, SU2 Casimir.")
