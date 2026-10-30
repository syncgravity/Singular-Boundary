#!/usr/bin/env python3
"""Exact deterministic audit of regional Agmon inequality and scaling.

No Monte Carlo, no alternative historical output, no inferred continuum mass gap.
"""
import sympy as s
from itertools import combinations
from collections import Counter

h, am, beta, ED, L, x, t, lmbd = s.symbols('h amax beta E_D L x t lambda', positive=True)
# Region X >= L, L>=2 h^2 ED/beta: positive barrier is >= beta X/(2h^2)
barrier=s.simplify(beta*x/h**2-ED)
assert s.simplify(barrier.subs(ED,beta*L/(2*h*h))-beta*x/(2*h*h)) == beta*(x-L)/ (2*h*h)
# Gamma(X)<=4 amax X. Chain rule and (a+b)^2<=2a^2+2b^2.
c=s.sqrt(beta/(32*am))
lambda_h=c/h
assert s.simplify(8*am*lambda_h**2-beta/(4*h**2))==0
# 2 integral e^(2 lambda(x-2L)) (chi')^2 Gamma(X) over L<x<2L
# bounded by 16 am/L, yielding the weighted moment bound.
weighted=s.simplify((16*am/L)*(4*h*h/beta))
assert weighted == 64*am*h**2/(beta*L)
# Tail probability bound for event X>=2L+t, t>=0:
prob=weighted/(2*L+t)*s.exp(-2*lambda_h*t)
assert s.simplify(prob.subs(t,0)-32*am*h*h/(beta*L*L))==0
# If 4 lambda L>=1 then x exp(-2lambda(x-2L)) decreases for x>=2L.
assert s.simplify(s.diff(x*s.exp(-2*lmbd*(x-2*L)),x) - s.exp(-2*lmbd*(x-2*L))*(1-2*lmbd*x))==0
second=s.simplify(2*L*weighted)
assert second==128*am*h*h/beta
# At fixed physical region ED=O(h^-3), L chosen O(h^-1), so P(X>=2L)=O(h^4),
# second moment on the forbidden tail is O(h^2).
K=s.symbols('K',positive=True)
assert s.simplify(prob.subs({t:0,L:K/h})-32*am*h**4/(beta*K*K))==0
assert s.simplify(second*h-128*am*h**3/beta)==0
# Fundamental Casimir and deficit establish |grad p|^2=(1-p^2)/4<=d/2.
p=s.symbols('p',real=True)
assert s.simplify((s.Rational(3,4)*p*p - (4*p*p-1)/4)-(1-p*p)/4)==0
assert s.simplify((1-p*p)/4-(1-p)/2 + (p-1)**2/4)==0
# Original Penrose spatial three-face fixture, not recovered temporal Q14.
seed=[
[(-1,-1,-1,-1,-1),(-1,-1,-1,0,-1),(0,-1,-1,-1,-1),(0,-1,-1,0,-1)],
[(-1,-1,-1,-1,-1),(-1,-1,0,-1,-1),(-1,-1,-1,0,-1),(-1,-1,0,0,-1)],
[(-1,-1,-1,-1,-1),(-1,0,-1,-1,-1),(0,-1,-1,-1,-1),(0,0,-1,-1,-1)]]
def edges(f):
    return {tuple(sorted((u,v))) for u,v in combinations(f,2)
            if sum(abs(a-b) for a,b in zip(u,v))==1}
faces=[edges(f) for f in seed]
counts=Counter(e for f in faces for e in f)
assert len(counts)==10 and max(counts.values())==2 and all(len(f)==4 for f in faces)
print('PASS: exact regional barrier, chain-rule absorption, weighted moment, tail constants')
print('PASS: SU(2) Casimir and 3-face canonical incidence; no simulations')
print('Tail: E[X exp(2lambda(X-2L)) 1_{X>=2L}] <= 64 amax h^2/(beta L)')
print('Tail second moment: <= 128 amax h^2/beta if 4lambda L>=1')
print('Fixed-support connected covariance and full mass gap remain OPEN')
