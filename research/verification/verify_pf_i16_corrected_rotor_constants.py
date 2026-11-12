#!/usr/bin/env python3
"""Exact rational regression checks for the corrected PF-I16 rotor constants."""
from fractions import Fraction as F

# Corrected pullback blocks under ||s'|| <= 2 beta and
# ||Hess s|| <= 4 beta/3 + 80 beta^2/3.
hd_linear = F(32, 3)
ho_linear = F(56, 3)
h_quadratic = F(1280, 3)
assert ho_linear - hd_linear == 8
assert h_quadratic == F(8) * F(80, 3) * 2  # 8 A_f and A_f >= a0/2

# Unweighted curvature row and mu=log(25) weighted derivative-flow row.
kappa_linear = F(16) * (hd_linear + 3 * ho_linear)
kappa_quadratic = F(16) * (4 * h_quadratic)
flow_linear = F(16) * hd_linear + F(1200) * ho_linear
flow_quadratic = F(16) * h_quadratic + F(1200) * h_quadratic
assert (kappa_linear, kappa_quadratic) == (F(3200, 3), F(81920, 3))
assert (flow_linear, flow_quadratic) == (F(67712, 3), F(1556480, 3))

r = F(1, 50000)
kappa_margin = F(1, 2) - kappa_linear*r - kappa_quadratic*r*r
flow_margin = F(1, 2) - flow_linear*r - flow_quadratic*r*r
assert kappa_margin > F(4786, 10000)
assert flow_margin > F(483, 10000)

# Residual derivative constants from the corrected 2 beta gradient bound.
h_star_ratio = ho_linear + h_quadratic*r
component = 1152*h_star_ratio
assert component < 21514
assert 5*component < 107570
assert 25*component < 537850

# The radial linear response coefficient is fixed by the ODE.
# q_1 = -(4/3) sin(theta), so its sup norm coefficient is 4/3 > 1.
assert F(4, 3) > 1

print("PASS: corrected diagonal/off-diagonal face-block coefficients")
print("PASS: corrected curvature and weighted-flow row coefficients")
print(f"PASS: kappa margin > {float(kappa_margin):.8f} a0")
print(f"PASS: weighted derivative-flow margin > {float(flow_margin):.8f} a0")
print("PASS: corrected shared-link residual derivative ceilings")
print("PASS: linear response coefficient 4/3 rules out the old unit constant")
print("LIMIT: arithmetic regression only; analytic lemmas and continuum gates remain separate")
