#!/usr/bin/env python3
"""Finite exact arithmetic diagnostics for the *combinatorial* formal majorant.
Does not verify SU(2) tame estimates or prove the infinite-order theorem.
"""
from fractions import Fraction
from math import factorial, comb

def run(limit=40):
    assert limit >= 2
    for n in range(2, limit+1):
        m = n-2
        reciprocal_binomial_sum = sum((Fraction(1,comb(m,k)) for k in range(m+1)),Fraction(0))
        assert reciprocal_binomial_sum <= 3, (n,reciprocal_binomial_sum)
        assert n+2 <= 4*(n-1)
    # For illustrative positive constants Ccross=2, Cnest=3 and M=1,
    # check the exact scalar equality recurrence against the analytical
    # Gevrey-1 bound. This tests arithmetic only.
    Ccross,Cnest=2,3
    D=3*Ccross+12*Cnest
    values=[0,1]
    for n in range(2,limit+1):
        an=(Ccross+Cnest*(n+2))*sum(values[i]*values[n-i] for i in range(1,n))
        values.append(an)
        assert an<=D**(n-1)*factorial(n-1),(n,an)
    print(f"PASS: {limit-1} exact reciprocal-binomial bounds and {limit-1} positive recurrence bounds; constants {Ccross=}, {Cnest=}, {D=}")
if __name__=='__main__':
    run()
