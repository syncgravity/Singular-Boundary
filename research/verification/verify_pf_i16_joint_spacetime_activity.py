#!/usr/bin/env python3
"""Exact-rational check of PF-I16 local activity and centering thresholds."""
from fractions import Fraction as Q

x = Q(1, 50_000)
e_half = Q(165, 100)
e_upper = Q(272, 100)
delta0 = Q(3, 4)

face = 8 * (64 * x + 64 * x * x) * e_half / delta0
pair = 224 * (512 * x * x) * e_upper / delta0
kappa_h = face + pair

# The published uncentered arithmetic and its conditional centered variants.
assert kappa_h < Q(22695, 1_000_000)
assert 4 * kappa_h < Q(1, 8)
assert 8 * kappa_h > Q(1, 8)

# A centered norm estimate ||v-Ev|| <= c ||v|| must have this c or better.
c_max = Q(1, 32) / kappa_h
assert Q(1, 1) < c_max < Q(2, 1)

# The projective-norm face contribution alone at x=1/50000.
projective_face = Q(45056, 500_000)  # 4505.6 * x = 0.090112
assert projective_face == Q(90112, 1_000_000)
assert 4 * projective_face > Q(1, 8)

print(f"PASS: exact uncentered kappa_H={float(kappa_h):.12f} < 0.022695")
print(f"PASS: 4*kappa_H={float(4*kappa_h):.12f} < 1/8")
print(f"LIMIT: generic centering gives 8*kappa_H={float(8*kappa_h):.12f} > 1/8")
print(f"TARGET: centered-norm ratio c must be <= {float(c_max):.6f}")
print("LIMIT: projective face majorant alone exceeds the proposed KP threshold")
print("No KP convergence or physical-vacuum result is certified.")
