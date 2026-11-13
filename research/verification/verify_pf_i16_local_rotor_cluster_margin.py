#!/usr/bin/env python3
"""Exact arithmetic checks for the candidate PF-I16 local-rotor cluster margin.

This verifies the stated norm arithmetic only. It does NOT verify a quantum
Kotecky-Preiss or linked-cluster theorem.
"""
from fractions import Fraction

x = Fraction(1, 50_000)
z_over_gap = Fraction(4, 3) * x + Fraction(57_344, 3) * x * x
degree_weighted = 28 * z_over_gap
e_upper = Fraction(68, 25)  # 2.72 > e
e_weighted = e_upper * degree_weighted

assert z_over_gap < Fraction(3432, 100_000_000)  # 3.432e-5
assert degree_weighted < Fraction(961, 1_000_000)  # 9.61e-4
assert e_weighted < Fraction(262, 100_000)  # 2.62e-3

print(f"PASS: z_face/gap = {float(z_over_gap):.12g} < 3.432e-5")
print(f"PASS: 28*z_face/gap = {float(degree_weighted):.12g} < 9.61e-4")
print(f"PASS: e*28*z_face/gap < {float(e_weighted):.12g} < 2.62e-3")
print("NOTE: no quantum cluster-expansion criterion is asserted or verified.")
