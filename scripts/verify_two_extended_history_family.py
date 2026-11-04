#!/usr/bin/env python3
"""Finite exact character and conservative scalar checks for the two-extended
history original-link SU(2) family theorem. Requires sympy. Independent
quaternion PDE and full Fourier Schatten superoperator checks are in the
companion ZIP, with SHA256 hashes. Finite tests are not the all-spin proof.
"""
from itertools import product
from math import sqrt
import sympy as S
x=S.Symbol("x")
def channels(q,r):return range(abs(q-r),q+r+1,2)
def co(q,r,l):
 Q=q*(q+2);R=r*(r+2);L=l*(l+2)
 return (S.Rational(Q+R-L,2), S.Rational(L+R-Q,2*L) if l else S.S(0),
         S.Rational(L+Q-R,2*L) if l else S.S(0))
for q,r in product(range(1,8),repeat=2):
 U=lambda i:S.chebyshevu(i,x)
 assert S.expand(U(q)*U(r)-sum((U(l) for l in channels(q,r)),S.S(0)))==0
 assert S.expand((1-x*x)*S.diff(U(q),x)*S.diff(U(r),x)-sum((co(q,r,l)[0]*U(l) for l in channels(q,r)),S.S(0)))==0
 assert S.expand(U(q)*S.diff(U(r),x)-sum((co(q,r,l)[1]*S.diff(U(l),x) for l in channels(q,r) if l),S.S(0)))==0
 assert S.expand(S.diff(U(q),x)*U(r)-sum((co(q,r,l)[2]*S.diff(U(l),x) for l in channels(q,r) if l),S.S(0)))==0
print("PASS 49 exact SU(2) four-identity character tests")
for p,q,r,s in product(range(1,13),repeat=4):
 P=p*(p+2);T=s*(s+2);a=q+1;b=r+1;N=a+b
 ratio=0.
 for l in channels(q,r):
  L=l*(l+2);base=P+L+T
  a0,t,u=co(q,r,l)
  S12=sqrt(P*L)/4;S23=sqrt(T*L)/4
  X=(abs(float(a0))+abs(float(t))*S12+abs(float(u))*S23)/(base-2*(S12+S23))
  assert X<=3*N*N/((l+1)**2)+1e-10
  moment=(1+max(p,l,s))/((1+max(p,q))*(1+max(r,s)))
  ratio+=((l+1)**2/(a*a*b*b))*moment*X
 assert ratio<=24/(1+min(q,r))**2+1e-10,(p,q,r,s,ratio)
print("PASS 20736 conservative all-four-spin scalar ratio checks")
