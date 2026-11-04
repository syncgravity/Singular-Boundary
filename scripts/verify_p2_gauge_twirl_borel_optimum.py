#!/usr/bin/env python3
"""Exact SU(2) two-face gauge twirl and certified Borel radius optimization."""
import itertools
import sympy as s
A=s.symbols('a1:4'); B=s.symbols('b1:4'); avg=0
for p in itertools.permutations(range(3)):
 parity=(-1)**sum(p[i]>p[j] for i in range(3) for j in range(i+1,3))
 for signs in itertools.product((-1,1),repeat=3):
  if parity*s.prod(signs)!=1: continue
  a=[signs[i]*A[p[i]] for i in range(3)]
  b=[signs[i]*B[p[i]] for i in range(3)]
  avg+=(s.I*a[0]-a[1])*(s.I*b[0]+b[1])
assert s.expand(avg/24+s.Rational(2,3)*sum(x*y for x,y in zip(A,B)))==0
t=s.symbols('t',positive=True)
K=16/(1-t)+48*t/(1-t)**2+256*t
rad=s.factor(3*t/(4*K))
d=s.factor(s.diff(rad,t))
assert s.factor(d-3*(t-1)*(t+1)*(4*t-1)/(64*(16*t**3-32*t**2+18*t+1)**2))==0
assert rad.subs(t,s.Rational(1,4))==s.Rational(9,5120)
for m in range(1,1001): assert s.Rational(2+6*m,2**m)<=4
print('PASS exact two-face physical gauge twirl and global majorant radius optimum')
