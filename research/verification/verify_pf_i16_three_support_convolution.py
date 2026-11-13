#!/usr/bin/env python3
"""Exact arithmetic checks for the PF-I16 three-kernel spatial convolution."""
from fractions import Fraction

# C1 = 1 + 24/(5*sqrt(23)-23) < 25.511.
# Equivalent to 5*sqrt(23) > 587753/24511.
assert 25 * 23 * 24_511**2 > 587_753**2

# For gamma = (1/4)log(25/23),
# x2 = exp(-(log(25)-gamma)) = (1/25)*(25/23)**(1/4).
# Prove x2 < 41/1000 by taking fourth powers.
assert Fraction(25, 23 * 25**4) < Fraction(41, 1000)**4

# Shell-sum bound C2 < 1 + 24*(41/1000)/(1-23*(41/1000))
# = 347/19 < 18.264.
c2_bound = Fraction(347, 19)
assert c2_bound < Fraction(18_264, 1000)

# Consequently C1*C2 < 25.511*18.264 = 465.932904 < 465.933.
c3_bound = Fraction(25_511, 1000) * Fraction(18_264, 1000)
assert c3_bound == Fraction(58_241_613, 125_000)
assert c3_bound < Fraction(465_933, 1000)

# gamma = 1/4 log(25/23) is positive and below nu = 1/2 log(25/23).
# The shell sum for mu-gamma converges because
# exp(-(mu-gamma)) < 41/1000 < 1/23.
assert Fraction(41, 1000) < Fraction(1, 23)

print("PASS: C1 < 25.511")
print("PASS: C2 < 18.264")
print("PASS: C1*C2 < 465.933")
print("PASS: second convolution shell sum is finite")
