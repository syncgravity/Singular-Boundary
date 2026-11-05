#!/usr/bin/env python3
"""Actual signed SU2 character score recursion, NOT scalar nonnegative majorant."""
from fractions import Fraction as F
from collections import defaultdict
def e(k):return k*(k+2)
def B(f,g):
 out=defaultdict(F)
 for a,x in f.items():
  for b,y in g.items():
   for c in range(abs(a-b),a+b+1,2):
    if c:out[c]+=x*y*F(e(a)+e(b)-e(c),2*e(c))
 return {c:v for c,v in out.items() if v}
S={1:{1:F(1,6)}}
for n in range(2,25):
 d=defaultdict(F)
 for j in range(1,n):
  for k,v in B(S[j],S[n-j]).items():d[k]+=v
 S[n]={k:v for k,v in d.items() if v}
 assert all(k<=n and (n-k)%2==0 for k in S[n])
assert S[2]=={2:-F(1,288)}
assert S[3]=={1:-F(1,648),3:F(1,6480)}
print('PASS 24 exact-rational actual sign-sensitive one-face SU2 score orders')
print('No inference about infinite-volume Borel continuation follows.')
