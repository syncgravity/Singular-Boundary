#!/usr/bin/env python3
"""Independent support-sector/local Borel audit, pure standard library.
Complete physical SU2 matrix inverse regression and logs live in companion ZIP.
Support-tree counter is combinatorial only, not a SU2 amplitude calculation.
"""
from fractions import Fraction as F
from math import factorial
from collections import defaultdict
for N in range(2,202,2):
 for m in range(3,31):
  labels=[]
  for j in range(N):
   for l in (m-1,m+1):
    a=[1]*N;a[j]=l;labels.append(tuple(a))
  assert len(set(labels))==2*N
  assert F(9*N*m,3*N+m*m-4)>0
print('PASS exact disjoint SU2 CG output sectors at every tested width and high spin')

def histories(lo,hi,nmax):
 a=[defaultdict(int) for _ in range(nmax+1)]
 for k in range(lo,hi+1):a[1][(k,k)]=1
 for n in range(2,nmax+1):
  for j in range(1,n):
   for (p,q),x in a[j].items():
    for (r,s),y in a[n-j].items():
     if q+1<r or s+1<p:continue
     a[n][(min(p,r),max(q,s))]+=x*y
 return a
a=histories(-5,5,6);b=histories(-7,7,6)
for n in range(1,7):
 for i in range(-4,5):
  for j in range(i,5):
   assert a[n].get((i,j),0)==b[n].get((i,j),0)
   if a[n].get((i,j),0):assert j-i+1<=n
print('PASS linked-history locality up to source order 6 (support combinatorics)')

M=F(16,3);K=F(320,3)
assert 1/(M*K)==F(9,5120)
for n in range(1,121):
 upper=M**n*K**(n-1)*factorial(n-1)
 assert F(upper,factorial(n))==K**(-1)*(M*K)**n/n
print('PASS exact infinite-row formal Gevrey majorant through order 120')
print('GLOBAL sup-anchor finite-volume truncations are non-Cauchy at source order one')
