#!/usr/bin/env python3
"""Exact seven-original-link SU(2) theta-graph electric spectrum and inverse trace."""
from fractions import Fraction
from math import pi,sqrt

def labels(n,m):
    return range(abs(n-m),n+m+1,2)
def energy(n,m,l,A=3,B=3,s=1):
    return Fraction(A*n*(n+2)+B*m*(m+2)+s*l*(l+2),4)
assert all(len(list(labels(n,m)))==min(n,m)+1 for n in range(16) for m in range(16))
assert energy(1,0,1)==energy(0,1,1)==3
assert energy(1,1,0)==Fraction(9,2) and energy(1,1,2)==Fraction(13,2)
def trace(N,A=3,B=3,s=1):
    out=0.
    for n in range(N+1):
        for m in range(N+1):
            if not n and not m:continue
            for l in labels(n,m):
                out+=float(energy(n,m,l,A,B,s))**-2
    return out
upper=8*pi*pi/27-1/3
for N in (4,8,16,32,64,128,256):
    t=trace(N)
    assert t<=upper
    print(f'N={N}: Tr inverse squared={t:.12f}, HS={sqrt(t):.12f}, tail bound={32/(9*N):.12f}')
assert trace(8,3.7,5.2,1.1)<trace(8)
print(f'PASS exact spectrum and HS upper bound {sqrt(upper):.12f}')
