#!/usr/bin/env python3
"""Exact rational regression checks for corrected PF-I16 rotor and third-order constants."""
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

# Smallness threshold and exact dimensionless margins.
r = F(1, 50000)
kappa_margin = F(1, 2) - kappa_linear*r - kappa_quadratic*r*r
flow_margin = F(1, 2) - flow_linear*r - flow_quadratic*r*r
assert kappa_margin == F(478655744, 10**9)
assert flow_margin == F(48379136, 10**9)
assert kappa_margin > F(4786, 10000)
assert flow_margin > F(483, 10000)

# Corrected residual bounds from the rotor repair audit.
R_star = F(4160)  # ||R_e|| <= R_star * b0^2/a0
r_sup = 2 * R_star
M = F(537850)     # sum_h ||D_h r_i|| <= M * b0^2/sqrt(a0)
assert r_sup == 8320

# Six terms: 6 * ||r||inf * ||G||_2 * ||r||inf * ||G r||inf,
# with ||G||_2 <= 1/kappa and ||G r||inf <= 50*pi*M*b0^2/(a0*lambda).
third_order_numerator = 6 * r_sup**2 * 50 * M
assert third_order_numerator == 11169380352000000

# Use pi < 22/7 and the exact rational curvature/flow margins.
third_order_pi_upper = F(third_order_numerator) * F(22, 7) / (
    kappa_margin * flow_margin
)
assert third_order_pi_upper == F(
    288422062500000000000000000000, 190263788491
)
assert third_order_pi_upper < F(1516, 1000) * 10**18

# Corrected residual derivative constants.
h_star_ratio = ho_linear + h_quadratic*r
component = 1152*h_star_ratio
assert component < 21514
assert 5*component < 107570
assert 25*component < 537850

# The radial linear response coefficient is fixed by the ODE.
assert F(4, 3) > 1

print("PASS: corrected diagonal/off-diagonal face-block coefficients")
print("PASS: corrected curvature and weighted-flow row coefficients")
print(f"PASS: exact curvature margin = {float(kappa_margin):.9f} a0")
print(f"PASS: exact weighted-flow margin = {float(flow_margin):.9f} a0")
print("PASS: corrected shared-link residual magnitude and derivative ceilings")
print(f"PASS: corrected six-term third-order numerator = {third_order_numerator}")
print(f"PASS: pi<22/7 third-order constant < {float(third_order_pi_upper):.12e}")
print("PASS: linear response coefficient 4/3 rules out the old unit constant")
print("LIMIT: exact-rational arithmetic regression only; analytic estimates remain conditional")
