#!/usr/bin/env python3
"""Exact-rational check of the PF-I16 degree-eight order-four LS envelope.

This verifies only the finite combinatorial coefficient and its numerical
upper bound. It does not establish the all-orders product-cumulant estimate,
the actual insertion projective norms, or a quantum cluster theorem.
"""
from fractions import Fraction as F
from math import factorial

# A(z)=exp(z/(1-z)) satisfies A'(z)=A(z)/(1-z)^2.
# If A(z)=sum a_n z^n, then n*a_n=sum_{j=0}^{n-1}(n-j)*a_j.
a = [F(1)]
for n in range(1, 33):
    a.append(sum((n-j)*a[j] for j in range(n)) / n)

assert all(a[n+1] >= a[n] for n in range(32))
assert a[32] == F(
    8128355160734725467847349684342205601,
    7973661725263440308097515520000000,
)
assert a[32] < 1020

# e=sum 1/k!. The tail from k=9 is bounded by a geometric series
# with ratio 1/10, since every subsequent factorial ratio is <=1/10.
e_partial = sum((F(1, factorial(k)) for k in range(9)), F(0))
e_tail = F(10, 9 * factorial(9))
e_upper = e_partial + e_tail
assert e_upper < F(2719, 1000)

D_upper = (2 * F(2719, 1000))**32 * factorial(32) * 1020
assert D_upper < F(92, 10) * 10**61

print(f"PASS: [z^32] exp(z/(1-z)) = {float(a[32]):.12f} < 1020")
print("PASS: exact rational tail estimate gives e < 2.719")
print(f"PASS: D_8,4 < {float(D_upper / 10**61):.12f}e61 < 9.2e61")
print("LIMIT: fixed order-four elementary-tensor envelope only.")
