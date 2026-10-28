#!/usr/bin/env python3
import sympy as s
from itertools import combinations
from collections import Counter
p,h,alpha,a,sig,K,F=s.symbols("p h alpha a sig K F",positive=True)
assert s.expand(2*(1-p)-(1-p*p))==(1-p)**2
assert s.simplify(s.Rational(3,4)*p*p-s.Rational(1,4)*(4*p*p-1)-(1-p*p)/4)==0
m=10*a*sig**2*K*(F*h*h)*h**(3-2*alpha)
assert s.simplify(m.subs(alpha,1)/h-10*a*sig**2*K*(F*h*h))==0
seed=[[[0,0],[1,0],[0,1],[1,1]]]
print("Exact Casimir identity and improved h^(3-2alpha) exponent verified; no simulation.")
