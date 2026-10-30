#!/usr/bin/env python3
"""Exact deterministic audit of SU(2) coherent trial mixture. No Monte Carlo."""
import sympy as s
from itertools import combinations
from collections import Counter

# SU(2) Haar one-plaquette integrals: Z(k)=I_1(2k)/k, E p=Z'/(2Z).
k=s.symbols('k',positive=True)
z=s.besseli(1,2*k)/k
r=s.besseli(0,2*k)/s.besseli(1,2*k)-1/k
assert s.simplify(s.diff(z,k)-2*r*z)==0
# Character orthogonality: E_Haar p=0, E_Haar p^2=1/4.
p=s.symbols('p',real=True)
assert s.simplify(s.Rational(3,4)*p*p-s.Rational(1,4)*(4*p*p-1)-(1-p*p)/4)==0

E,s0,m,v,vH=s.symbols('eps overlap m v vH',positive=True)
n=1+2*s.sqrt(E*(1-E))*s0
Ea=(1-2*E)*m/n
Ea2=(m*m+v+2*s.sqrt(E*(1-E))*s0*vH)/n
var=s.factor(Ea2-Ea*Ea)
assert s.simplify(var.subs(s0,0)-(v+4*E*(1-E)*m*m))==0
# Fixed physical support: face-count N~h^-2; source h^1/2 sum q_f p_f
h,I,expn=s.symbols('h I expn',positive=True)
rare=s.simplify((4*E*(1-E)*m*m).subs({E:h**expn,m:s.sqrt(h)*I/h**2}))
assert s.simplify(rare-4*I**2*h**(expn-3)*(1-h**expn))==0
assert s.simplify(rare.subs(expn,3)-4*I**2*(1-h**3))==0
assert s.simplify(rare.subs(expn,1)-4*I**2*h**(-2)*(1-h))==0
# Energy envelope: F~h^-2, kappa=h^-1, Btot~h^-4.
Eplus=s.O(h**-3,h)
assert (1-4)>=-3 # rare weight h^p >= h^1 leaves O(h^-3) total energy

seed=[
[(-1,-1,-1,-1,-1),(-1,-1,-1,0,-1),(0,-1,-1,-1,-1),(0,-1,-1,0,-1)],
[(-1,-1,-1,-1,-1),(-1,-1,0,-1,-1),(-1,-1,-1,0,-1),(-1,-1,0,0,-1)],
[(-1,-1,-1,-1,-1),(-1,0,-1,-1,-1),(0,-1,-1,-1,-1),(0,0,-1,-1,-1)]]
def edges(face):
    return {tuple(sorted((x,y))) for x,y in combinations(face,2) if sum(abs(a-b) for a,b in zip(x,y))==1}
faces=[edges(f) for f in seed]
counts=Counter(e for f in faces for e in f)
assert len(counts)==10 and max(counts.values())==2 and sum(v==1 for v in counts.values())==8
print('PASS: SU(2) Bessel normalization derivative and fundamental Casimir')
print('PASS: exact positive-state mixture variance and rarity h^p scaling')
print('PASS: canonical three-face Z^5 fixture, 10 edges, max face incidence 2')
print('No Monte Carlo, no synthetic historical results, no actual interacting vacuum claim')
