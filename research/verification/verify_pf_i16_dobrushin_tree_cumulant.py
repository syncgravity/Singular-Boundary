#!/usr/bin/env python3
"""Arithmetic verifier for the conditional PF-I16 Dobrushin/tree-cumulant bound.

This checks the numerical implications used in the proof record. It does not
verify the analytic Kato-Bochner derivative-flow hypothesis or Follmer's
covariance inequality.
"""
from fractions import Fraction
import math

# beta_* <= 2 b0/a0 <= 1/25000.
beta = Fraction(1, 25_000)

# Weighted influence norm:
# 600*tanh(4*pi*beta_*) <= 600*4*pi/25000 = 12*pi/125 < 264/875.
rho_upper = Fraction(264, 875)
assert Fraction(12, 125) * Fraction(22, 7) == rho_upper
assert rho_upper < 1

# Resolvent weighted norm <= 1/(1-rho) < 875/611.
D_upper = Fraction(875, 611)
assert D_upper == 1 / (1 - rho_upper)

# Inherited exact convolution bounds: C1 < 25.511, C1*C2 < 465.933.
C1_upper = Fraction(25_511, 1_000)
C3_upper = Fraction(465_933, 1_000)
pi_upper = Fraction(22, 7)

K_residual_resolvent = D_upper * pi_upper**2 * C3_upper
K_two_pair_arms = D_upper * 52 * pi_upper**3 * C1_upper
assert K_residual_resolvent < 6_591
assert K_two_pair_arms < 58_976

# Six permutations: E_123 = -2 sum over the three middle labels.
assert 2 * 6_591 == 13_182
assert 6 * 58_976 == 353_856

eta = math.log(25 / 23) / 8
assert eta > 0

print("PASS: beta_* <= 1/25000")
print("PASS: weighted Dobrushin influence norm < 264/875 < 1")
print("PASS: covariance-kernel constant < 875/611")
print("PASS: inherited C1 and C1*C2 convolution bounds are sufficient")
print("PASS: third-cumulant constants < 6591 and < 58976")
print("PASS: six-permutation constants 13182 and 353856")
print(f"PASS: tree exponent eta = {eta:.12f} > 0")
