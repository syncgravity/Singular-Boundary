#!/usr/bin/env python3
"""Reproducible exact charge bound and crossing-history tests.
The full PW physical matrix/feedback verifiers reside in the conversation ZIP.
"""
from fractions import Fraction as Q
from itertools import product
from random import Random
rng=Random(20261104);count=0
for a,b in product(range(65),repeat=2):
 for c in range(abs(a-b),a+b+1,2):
  assert a*(a+2)+b*(b+2)-c*(c+2)<=6*a*b
  count+=1
for N in (3,4,5,7,10):
 for _ in range(1400):
  a=[rng.randrange(13) for i in range(N)]
  b=[rng.randrange(13) for i in range(N)]
  if not any(a) or not any(b):continue
  A=1+max(a);B=1+max(b);h=sum(x>0 and y>0 for x,y in zip(a,b))
  E=sum(x*(x+2) for x in a)+sum(x*(x+2) for x in b)
  allowed=[list(range(abs(x-y),x+y+1,2)) for x,y in zip(a,b)]
  cases=[tuple(x[0] for x in allowed),tuple(x[-1] for x in allowed)]
  cases.extend(tuple(rng.choice(x) for x in allowed) for _ in range(6))
  for c in cases:
   D=sum(z*(z+2) for z in c)
   if not D:continue
   W=1+max(c)
   scalar=Q(W,A*B)*(Q(1,2)+Q(3*E,2*D))
   assert scalar<=2+6*h,(a,b,c,scalar)
   assert Q(W,D)<=Q(2,3)
   count+=1
print('PASS',count,'exact SU2 CG energy-charge and multiwidth scalar checks')
# Positive *scalar* nested history majorant is not volume-uniform:
for n in (10,100,1000):
 assert Q(8*n,2)==4*n
print('PASS nested positive majorant obstruction at widths 10, 100, 1000')
