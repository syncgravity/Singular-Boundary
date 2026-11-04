#!/usr/bin/env python3
from fractions import Fraction as F
from math import factorial
def ratio(n,m,r):
 return F(m+2,2*(m+1))**(r+1)*(F(3*m*(n-2),7*n-1+2*m*m+10*m)+F(5*m,7*n-1+2*m*m+9*m))
for r in range(5):
 for m in range(1,151):
  q=ratio(m*m+2,m,r)
  assert q>0
  if m>=100: assert q>F(m,12*(6*2**r))
t=F(1,4); c=F(88,3); d=c/2+48*t; k=4*d; M=F(16,3)
assert k==F(320,3) and 1/(M*k)==F(9,5120)
a=[F(0),M]
for n in range(2,121):
 a.append((c+24*t*(n+2))*sum(a[i]*a[n-i] for i in range(1,n)))
 assert a[n]<=M**n*k**(n-1)*factorial(n-1)
 assert n*sum(factorial(i-1)*factorial(n-i-1) for i in range(1,n))<=4*factorial(n-1)
print("PASS exact extremal ratio and Borel majorant checks")
