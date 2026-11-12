#!/usr/bin/env python3
"""PF-I16: exact SU(2) one-loop inverse kernel vs independent two-loop comparison."""
from math import sqrt
import numpy as np
import sympy as sp
n=sp.symbols('n',integer=True,positive=True)
S=sp.summation((n+1)**2/(n*n*(n+2)**2),(n,1,sp.oo))
assert sp.simplify(S-(sp.pi**2/12+sp.Rational(1,16)))==0
print('one loop inverse L2 kernel norm (A=4):',float(sp.sqrt(S)))
for N in (4,8,16,32,64,128,256,512):
    r=np.arange(1,N+1,dtype=float)
    one=np.sum((r+1)**2/(r*r*(r+2)**2))
    a=r[:,None];b=r[None,:]
    two=np.sum((a+1)**2*(b+1)**2/(a*(a+2)+b*(b+2))**2)
    assert one<=float(S)+1e-12
    if N>=16: assert two>=N*N/100
    print('N=%d  one_norm=%.9f  two_norm=%.9f'%(N,sqrt(one),sqrt(two)))
for N in (2,4,8,16,32):
    r=np.arange(N,2*N,dtype=float)
    a=r[:,None];b=r[None,:]
    terms=(a+1)**2*(b+1)**2/(a*(a+2)+b*(b+2))**2
    assert np.min(terms)>=1/144
print('PASS symbolic identity, convergent single loop and divergent two-loop shell')
