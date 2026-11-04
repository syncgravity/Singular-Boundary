#!/usr/bin/env python3
"""Exact arithmetic sanity checks for a conditional formal Borel majorant.

Does not verify original-link SU(2) PW recoupling or the infinite theorem.
"""
from fractions import Fraction
from math import comb, factorial

def verify(N=80):
    M = Fraction(1)
    cross = Fraction(2)
    nest = Fraction(3)
    D = 3*cross + 12*nest
    coeff = [Fraction(0), M]
    for n in range(2, N+1):
        reciprocal = sum((Fraction(1, comb(n-2,k)) for k in range(n-1)), Fraction(0))
        assert reciprocal <= 3, (n,reciprocal)
        assert n+2 <= 4*(n-1)
        actual = (cross + nest*(n+2))*sum(
            (coeff[i]*coeff[n-i] for i in range(1,n)), Fraction(0))
        coeff.append(actual)
        assert actual <= M**n*D**(n-1)*factorial(n-1), n
    for n in range(1,N+1):
        assert coeff[n]/factorial(n) <= (M*D)**n/(D*n)
    print(f"PASS: orders 1..{N}; formal Gevrey-1 and local Borel coefficient bounds. Not a SU(2) theorem verification.")

if __name__ == "__main__":
    verify()
