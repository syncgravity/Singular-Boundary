#!/usr/bin/env python3
"""Exact rational SU(2) Pauli-quaternion identities; no sampling."""
from fractions import Fraction as Q
from itertools import product
import json
Z=Q(0)
def dot(a,b): return sum((x*y for x,y in zip(a,b)),Z)
def cross(a,b): return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def mul(a,b):
 x,u=a[0],a[1:]; y,v=b[0],b[1:]; c=cross(u,v)
 return (x*y-dot(u,v),)+tuple(x*w+y*z-t for z,w,t in zip(u,v,c))
def inv(q):return (q[0],)+tuple(-v for v in q[1:])
def tr(q):return 2*q[0]
I=(Q(1),Z,Z,Z);X=(Z,Q(1),Z,Z);Y=(Z,Z,Q(1),Z);V=(Z,Z,Z,Q(1))
S=[I,X,Y,V,inv(V),(Q(3,5),Q(4,5),Z,Z),(Q(5,13),Z,Q(12,13),Z)]
S.append(inv(S[-2]))
assert all(sum(t*t for t in s)==1 for s in S)
for a,b in product(S,repeat=2):
 assert tr(a)*tr(b)==tr(mul(a,b))+tr(mul(a,inv(b)))
 assert mul(a,inv(a))==I
for a,b,c in product(S,repeat=3):
 sa,sb,sc=a[0],b[0],c[0];u,v,w=a[1:],b[1:],c[1:]
 expected=2*(sa*sb*sc-sa*dot(v,w)-sb*dot(u,w)-sc*dot(u,v)+dot(cross(u,v),w))
 assert tr(mul(mul(a,b),c))==expected
assert tr(mul(mul(X,Y),V))==2
assert tr(mul(mul(X,Y),inv(V)))==-2
assert tr(V)==tr(X)==0
assert tr(mul(V,V))==-2 and tr(mul(V,X))==0
print(json.dumps({"two_word_checks":64,"three_word_checks":512,"triple_orientation":[2,-2],"mixed_two_loop":[-2,0],"simulations":False},indent=2))
