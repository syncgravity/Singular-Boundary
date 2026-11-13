#!/usr/bin/env python3
"""Exact arithmetic checks for the PF-I16 two-point resolvent-decay constants."""
from fractions import Fraction

r = Fraction(1, 50_000)
kappa = Fraction(1, 2) - Fraction(3200, 3) * r - Fraction(81920, 3) * r * r
lam = Fraction(1, 2) - Fraction(67712, 3) * r - Fraction(1556480, 3) * r * r
assert kappa == Fraction(1_869_749, 3_906_250)
assert lam == Fraction(188_981, 3_906_250)

# For mu=log(25), gamma=0.5*log(25/23),
# C = 1 + 24/(5*sqrt(23)-23). Prove C < 25.511 exactly.
# This is equivalent to 5*sqrt(23) > 587753/24511.
assert 25 * 23 * 24_511**2 > 587_753**2
C_upper = Fraction(25_511, 1_000)

# Insert the corrected residual derivative envelope
# M_i <= 537850*b0^2/sqrt(a0).
pair_constant = 2 * C_upper * Fraction(537_850**2, 1) / (lam**2)
assert pair_constant < Fraction(6_307, 1) * 10**12

print("PASS: corrected curvature margin", kappa)
print("PASS: corrected weighted derivative-flow margin", lam)
print("PASS: shell-convolution constant C < 25.511")
print("PASS: residual pair coefficient < 6.307e15 * b0^4/a0^3")
