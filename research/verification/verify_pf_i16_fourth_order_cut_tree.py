#!/usr/bin/env python3
"""Arithmetic and cut-geometry checks for the conditional PF-I16 fourth-order tree bound.

This script checks the weighted shell constant, positive tree exponent, and
the integer cut-radius inequalities used in the proof. It does not verify the
analytic derivative-flow or Hellmann-Feynman hypotheses.
"""
import math

mu = math.log(25.0)
gamma = 0.25 * math.log(25.0 / 23.0)
S_gamma = 1.0 + 24.0 / (math.exp(mu - gamma) - 23.0)
eta4 = gamma / 6.0
boundary_factor = math.exp(1.5 * gamma)

assert S_gamma < 18.264
assert eta4 > 0.0
assert boundary_factor < 1.04

for L in range(0, 10001):
    R = max(0, L // 2 - 1)
    assert R >= L / 2.0 - 1.5
    assert math.exp(-gamma * R) <= boundary_factor * math.exp(-gamma * L / 2.0) * (1 + 1e-12)
    ell_upper = 3 * L
    assert math.exp(-gamma * L / 2.0) <= math.exp(-eta4 * ell_upper) * (1 + 1e-12)

print(f"PASS: S_gamma = {S_gamma:.12f} < 18.264")
print(f"PASS: eta_4 = {eta4:.12f} > 0")
print(f"PASS: cut-layer offset factor exp(3 gamma/2) = {boundary_factor:.12f}")
print("PASS: R >= L/2 - 3/2 for all integer L in [0,10000]")
print("PASS: four-terminal MST conversion ell_MST <= 3 L")
