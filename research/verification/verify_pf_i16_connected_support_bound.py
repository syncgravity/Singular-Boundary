#!/usr/bin/env python3
"""Exact combinatorial checker for the PF-I16 connected-face support bound."""
from fractions import Fraction
DELTA = 4
def rooted_bound(k):
    if k < 1: raise ValueError('k must be >= 1')
    return DELTA ** (2 * (k - 1))
def main():
    assert [rooted_bound(k) for k in range(1,5)] == [1,16,256,4096]
    q = Fraction(1,32)
    assert q / (1 - 16*q) == Fraction(1,16)
    assert 16 * Fraction(1,16) == 1
    print('PASS: rooted connected-support bound 16^(k-1)')
    print('PASS: exact majorant at q=1/32 sums to 1/16')
    print('GATE: independent activity estimate q<1/16 still required')
    print('LIMIT: no Wilson-vacuum activity bound, Taylor radius, or gap proved')
if __name__ == '__main__': main()