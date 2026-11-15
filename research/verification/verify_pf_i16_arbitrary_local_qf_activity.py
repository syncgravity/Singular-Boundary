#!/usr/bin/env python3
"""Exact-rational activity checks for the arbitrary-local-QF/pair-contraction audit.

The analytic interpolation, radial endpoint inequality, and SU(2) gradient
identity are proved in the companion audit. This verifier checks only the
rational activity arithmetic after the factor-four pair-bound improvement.
It does not prove the all-orders support-sensitive tree or KP convergence.
"""
from fractions import Fraction as F

x = F(1, 50_000)
delta0 = F(3, 4)

# Face activity 32 b0; pair activity per neighboring face 128 b0^2/a0.
z_over_delta = (32*x + 3_584*x*x) / delta0
q_face = 58 * z_over_delta
e_upper = F(27_183, 10_000)
q_joint_candidate = 4 * e_upper * q_face

assert z_over_delta == F(8_352, 9_765_625)
assert q_face == F(484_416, 9_765_625)
assert q_joint_candidate < F(540, 1_000)
assert q_joint_candidate < 1

print(f"PASS: z_f/Delta_0 = {float(z_over_delta):.10f}")
print(f"PASS: 58 z_f/Delta_0 = {float(q_face):.10f}")
print(f"DIAGNOSTIC: 4*2.7183*58 z_f/Delta_0 = {float(q_joint_candidate):.10f} < 0.540")
print("SCOPE: QF is proved for arbitrary bounded local observables under the stated link-Markov hypotheses.")
print("SCOPE: the support-sensitive all-orders cumulant tree and quantum KP application remain OPEN.")
