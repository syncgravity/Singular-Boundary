#!/usr/bin/env python3
"""P-75: explicit actual corrected SU2 collar S1 source / all-sector full inverse certificates.
Formula-only at large N; no giant Fourier matrices are constructed.
"""
from math import sqrt
def eta(N,l,interior):
 D=3*(N-1)+l*(l+2)
 return (3*(N-3)+2*sqrt(3*l*(l+2)))/(2*D) if interior else (3*(N-2)+sqrt(3*l*(l+2)))/(2*D)
def cap(N,m,q=-1):
 A=2.5*(m+1)*(m+2);z=0.
 for l in (m-1,m+1):
  D=3*(N-1)+l*(l+2);w=(l+1)**2/(4*(m+1)**3)
  a=eta(N,l,False);c=eta(N,l,True)
  assert 0<a<.5 and 0<c<.5
  p=0 if q==-1 else q+1
  z+=A*w/D*(2*a**p/(1-a)+(N-2)*c**p/(1-c))
 return z
for m in (3,4,6,10,20,40,80,160,300,1000):
 N=m*m+(m%2);q=0
 while cap(N,m,q)>1e-6:q+=1
 assert cap(N,m,q)<=1e-6
 print('PASS physical q0 S1 source collar',m,'N',N,'upper full response',cap(N,m),'upper/m',cap(N,m)/m,'sufficient q',q)
assert abs(cap(1000000,1000)/1000-.5)<.01
print('P-75: O(m), NOT O(1), conservative actual physical upper at N=m²; source rank independent of N.')
