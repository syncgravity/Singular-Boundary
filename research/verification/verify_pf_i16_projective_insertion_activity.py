#!/usr/bin/env python3
"""Exact rational audit of the PF-I16 projective insertion activity envelope.

This checks only the displayed arithmetic in Section 15. It does not prove
the H^6 regularity constant, the joint WDG estimate, or KP convergence.
"""
from fractions import Fraction as F

x = F(1, 50_000)
delta = F(3, 4)
sqrt_e = F(165, 100)  # exp(1/2) < 1.65
e = F(272, 100)       # exp(1) < 2.72
C6 = F(911, 100)      # Section 15 proves C6 < 9.11

face = 8 * 256 * x * sqrt_e / delta
pair_coeff = 224 * 384 * C6**2 * e / delta
pair = pair_coeff * x**2

assert face == F(11264, 125000)
assert face == F(0.090112)
assert pair_coeff < F(25_890_000, 1)
assert face + pair > face
assert 2 * face > F(1, 8)

print(f"PASS: face-only projective activity = {float(face):.9f}")
print(f"PASS: pair quadratic coefficient < {float(pair_coeff):.9g} * K6^2")
print(f"DIAGNOSTIC: full projective activity <= {float(face + pair):.9g} + pair K6 dependence")
print(f"OBSTRUCTION: even C_st=1 gives 2*kappa_face={float(2*face):.9f} > 1/8")
print("SCOPE: projective majorant cannot verify the recorded x=1/50000 KP target.")
print("SCOPE: this does not refute a direct L-infinity tensorized cumulant proof.")
