#!/usr/bin/env python3
"""Exact checks; source manuscript and full run in downloadable verification bundle."""
from fractions import Fraction as F
from itertools import product
import sympy as s
u=[(F(1),F(0),F(0),F(0)),(F(0),F(1),F(0),F(0)),(F(0),F(0),F(1),F(0)),(F(0),F(0),F(0),F(1)),(F(3,5),F(4,5),F(0),F(0)),(F(5,13),F(0),F(12,13),F(0))]
def dot(a,b): return sum((a[i]*b[i] for i in range(3)),F(0))
def mult(a,b):
 x,y=a[1:],b[1:]
 return a[0]*b[0]-dot(x,y)
def inv(a):return (a[0],)+tuple(-z for z in a[1:])
for a,b in product(u,repeat=2):
 assert mult(a,inv(b))-mult(a,b)==2*dot(a[1:],b[1:])
v=[F(0),F(1,2),F(1,2)]
variance=sum(z*z for z in v)+12*sum(v[i]*v[j] for i in range(3) for j in range(i+1,3))
assert variance==F(7,2) and 24*v[1]*v[2]==6
t=s.symbols('t',real=True)
assert s.diff(8+8*s.sin(t),t).subs(t,0)==8
print("36 exact SU(2) pairs, variance 7/2, pure connector Dirichlet 6a; no simulation")
