#!/usr/bin/env python3
"""Exact rational arithmetic for centered PF-I16 face/pair activities.

The matching Observatory graph verifier treats the alternate per-link centering
inventory separately; this script only certifies the exact conjugated face/pair route.

The Haar-centering identities are proved in the companion audit; this script
checks the displayed activity constants and the conditional q_joint margin.
It does not verify the all-orders quasi-factorization or KP theorem.
"""
from fractions import Fraction as Q

x = Q(1, 50_000)
delta0_over_a0 = Q(3, 4)

# Face term: 32 b0. Pair term per neighboring face: 512 b0^2/a0.
z_over_delta = (Q(32) * x + Q(14_336) * x * x) / delta0_over_a0
assert z_over_delta == Q(53_811_200, 62_500_000_000)
assert z_over_delta == Q(1_076_224, 1_250_000_000)
assert z_over_delta < Q(861, 1_000_000)

q_face = 58 * z_over_delta
assert q_face == Q(31_210_496, 625_000_000)
assert q_face < Q(49_937, 1_000_000)

# e < 2.7183, so the conditional candidate q_joint=4 e q_face is <0.543.
e_upper = Q(27_183, 10_000)
q_joint_upper = 4 * e_upper * q_face
assert q_joint_upper < Q(543, 1_000)
assert q_joint_upper < 1

# The generic factor-two centering loss is not used for these insertions:
# both local Haar means vanish by the conditional-Haar argument.
print(f"PASS: z_f/Delta_0 = {float(z_over_delta):.10f} < 0.000861")
print(f"PASS: q_face = {float(q_face):.10f} < 0.049937")
print(f"PASS: 4*(2.7183)*q_face = {float(q_joint_upper):.10f} < 0.543")
print("NOTE: q_joint is conditional on the unproved all-orders joint tree/KP counting.")
