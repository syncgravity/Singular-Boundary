#!/usr/bin/env python3
"""Portable exact Casimir Neumann and local Borel certificates (full physical test in companion ZIP)."""
from math import sqrt,comb,factorial
from fractions import Fraction as F
for n in (2,4,8,16,64,256):
 for m in (3,4,8,16,32,64):
  Dmin=3*n+m*m-4
  assert Dmin>0
  for j in range(n):
   for l in (m-1,m+1):
    degrees=[1]*n; degrees[j]=l
    e=[x*(x+2) for x in degrees];D=sum(e)
    alpha=sum(sqrt(e[i]*e[i+1]) for i in range(n-1))/(2*D)
    assert alpha<=0.5+1e-12 and D>=Dmin
    for q in (0,1,2,4,8):
     adaptive=9*n*m/(2*Dmin)*alpha**(q+1)/(1-alpha)
     uniform=9*n*m/Dmin*2**(-q-1)
     assert adaptive<=uniform*(1+1e-12)
print('PASS certified sectorwise original-link Neumann tail and uniform bound')
for L in range(1,101):
 C=2+6*L;M=F(4*L,3); B=4*C*M; lam=F(1,2*B)
 for n in range(1,101):
  cat=F(comb(2*n-2,n-1),n)
  assert cat*C**(n-1)*M**n<=M*B**(n-1)
 for p in (1,3,8,16):
  partial=sum(F(comb(2*n-2,n-1),n)*C**(n-1)*M**n*lam**n for n in range(p+1,p+35))
  assert partial<M*lam*(B*lam)**p/(1-B*lam)
print('PASS 10000 exact Catalan checks and 400 Laplace truncation tests')
