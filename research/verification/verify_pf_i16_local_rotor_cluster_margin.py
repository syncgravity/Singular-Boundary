#!/usr/bin/env python3
"""Exact arithmetic checks for the candidate PF-I16 local-rotor cluster margin.

This verifies the stated norm arithmetic only. It does NOT verify a quantum
Kotecky-Preiss or linked-cluster theorem.
"""
from fractions import Fraction

x = Fraction(1, 50_000)
z_over_gap = Fraction(128, 3) * x + Fraction(57_344, 3) * x * x
degree_weighted = 28 * z_over_gap
e_upper = Fraction(68, 25)  # 2.72 > e
e_weighted = e_upper * degree_weighted

assert z_over_gap < Fraction(861, 1_000_000)  # 8.61e-4
assert degree_weighted < Fraction(2411, 100_000)  # 2.411e-2
assert e_weighted < Fraction(6558, 100_000)  # 6.558e-2

print(f"PASS: z_face/gap = {float(z_over_gap):.12g} < 8.61e-4")
print(f"PASS: 28*z_face/gap = {float(degree_weighted):.12g} < 2.411e-2")
print(f"PASS: e*28*z_face/gap < {float(e_weighted):.12g} < 6.554e-2")
print("NOTE: no quantum cluster-expansion criterion is asserted or verified.")
