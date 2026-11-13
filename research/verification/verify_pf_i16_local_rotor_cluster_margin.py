#!/usr/bin/env python3
"""Exact arithmetic checks for candidate PF-I16 local-rotor activity margins.

This verifies the stated norm arithmetic only. It does NOT verify a quantum
Kotecky-Preiss or linked-cluster theorem.
"""
from fractions import Fraction

x = Fraction(1, 50_000)
e_upper = Fraction(68, 25)  # 2.72 > e

# Original conjugated interaction: one-face term plus adjacent-face pairs.
z_face_over_gap = Fraction(128, 3) * x + Fraction(57_344, 3) * x * x
face_degree_weighted = 28 * z_face_over_gap
assert z_face_over_gap < Fraction(861, 1_000_000)  # 8.61e-4
assert face_degree_weighted < Fraction(2411, 100_000)  # 2.411e-2
assert e_upper * face_degree_weighted < Fraction(6558, 100_000)  # 6.558e-2

# Derivative insertion for a multi-cut parameter in the conjugated picture.
z_cut_over_gap = Fraction(256, 3) * x + Fraction(115_712, 3) * x * x
cut_degree_weighted = 28 * z_cut_over_gap
assert z_cut_over_gap < Fraction(1723, 1_000_000)  # 1.723e-3
assert cut_degree_weighted < Fraction(4822, 100_000)  # 4.822e-2
assert e_upper * cut_degree_weighted < Fraction(1312, 10_000)  # 0.1312

print(f"PASS: z_face/gap = {float(z_face_over_gap):.12g} < 8.61e-4")
print(f"PASS: 28*z_face/gap = {float(face_degree_weighted):.12g} < 2.411e-2")
print(f"PASS: e*28*z_face/gap < {float(e_upper*face_degree_weighted):.12g} < 6.558e-2")
print(f"PASS: z_cut/gap = {float(z_cut_over_gap):.12g} < 1.723e-3")
print(f"PASS: 28*z_cut/gap = {float(cut_degree_weighted):.12g} < 4.822e-2")
print(f"PASS: e*28*z_cut/gap < {float(e_upper*cut_degree_weighted):.12g} < 0.1312")
print("NOTE: no quantum cluster-expansion criterion is asserted or verified.")
