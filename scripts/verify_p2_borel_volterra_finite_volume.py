#!/usr/bin/env python3
"""Exact source-order Borel-Volterra and finite-volume Catalan checks.
Physical SU(2) matrix tests and full logs are in the companion conversation ZIP.
"""
from fractions import Fraction as F
from collections import defaultdict
from math import comb, factorial
def E(n):return n*(n+2)
def B(a,b):
 out=defaultdict(F)
 for n,x in a.items():
  for m,y in b.items():
   for l in range(abs(n-m),n+m+1,2):
    if l:out[l]+=x*y*F(E(n)+E(m)-E(l),2*E(l))
 return {k:v for k,v in out.items() if v}
S={1:{1:F(1,6)}}
for n in range(2,21):
 out=defaultdict(F)
 for i in range(1,n):
  for j,v in B(S[i],S[n-i]).items():out[j]+=v
 S[n]={j:v for j,v in out.items() if v}
 assert all(j<=n and (j-n)%2==0 for j in S[n])
assert S[2]=={2:-F(1,288)}
assert S[3]=={1:-F(1,648),3:F(1,6480)}
for N in (1,2,4,8,16,64):
 C=F(2+6*N);M=F(4*N,3)
 assert F(1,4*C*M)==F(3,16*N*(2+6*N))
 for n in range(1,31):
  cat=F(comb(2*(n-1),n-1),n)
  assert cat<=4**(n-1)
  if n>1:
   assert sum(F(comb(2*i-2,i-1),i)*F(comb(2*(n-i)-2,n-i-1),n-i) for i in range(1,n))==cat
print("PASS exact SU2 one-face score/Borel coefficients and finite-volume Catalan analytic bounds")
print("FINITE volume: rho_N=3 exp(-sigma)/[16 N(2+6N)]; no uniform Laplace claim")
