#!/usr/bin/env python3
"""Exact-rational checks for the PF-I16 character-tail/projective-norm audit.

This verifies the fixed-point constants, weighted gradient-character tail
constant, Casimir norm bounds, and activity arithmetic. The analytic proof
and its stated Markov/rotor hypotheses are recorded in the companion audit.
"""
from fractions import Fraction as F

beta_max = F(1, 25_000)
x_max = F(1, 50_000)

# Character Banach-algebra and parity-tail constants at weight s=4.
M4 = F(3 + 3**4, 4)
K4 = F(8)
nonlinear_constant = K4 * M4
assert M4 == 21
assert nonlinear_constant == 168

# On ||R||_{4,chi} <= 2 beta:
# T(R) <= 4 beta/3 + 672 beta^2, and Lip(T) <= 672 beta.
ball_radius = 2 * beta_max
map_bound = F(4, 3) * beta_max + nonlinear_constant * ball_radius**2
lipschitz = 2 * nonlinear_constant * ball_radius
assert map_bound < ball_radius
assert lipschitz == F(672) * beta_max
assert lipschitz < 1

# The nonlinear correction to the exact source (4 beta/3) chi_0.
delta = nonlinear_constant * ball_radius**2
assert delta == 672 * beta_max**2

# Weighted gradient-character coefficient bound:
# The nonlinear remainder is K((1-p^2)R^2), so its entire nonconstant
# character tail is <= 672 beta^2 (not 2 beta/3 + 672 beta^2).
# Thus C5 <= (64/3) beta + (1299/64)*672 beta^2.
c5_ratio = F(64, 3) + F(1299, 64) * 672 * beta_max
assert c5_ratio == F(3281837, 150000)
assert c5_ratio < F(21879, 1000)

# Exact SU(2) Casimir contraction:
# ||Omega_{j,k}|| = min(j,k)(max(j,k)+1)
# <= (n+1)(m+1)/4 for j=n/2, k=m/2.
for n in range(0, 20):
    for m in range(0, 20):
        exact = F(min(n, m) * (max(n, m) + 2), 4)
        upper = F((n + 1) * (m + 1), 4)
        assert exact <= upper

# Face/pair projective norms and support-weighted per-link activity.
face_norm_coeff = F(256)
pair_norm_coeff = 32 * c5_ratio**2
assert face_norm_coeff == 32 * 8
assert pair_norm_coeff == F(10770454094569, 703125000)
assert pair_norm_coeff < 15_318

sqrt_e_upper = F(165, 100)
e_upper = F(272, 100)
delta0_ratio = F(3, 4)

face_activity = F(8) * face_norm_coeff * x_max * sqrt_e_upper / delta0_ratio
pair_activity = F(224) * pair_norm_coeff * x_max**2 * e_upper / delta0_ratio
kappa = face_activity + pair_activity

assert face_activity == F(1408, 15_625)
assert pair_activity == F(1281684037253711, 257492065429687500)
assert kappa == F(24484809037253711, 257492065429687500)
assert 2 * kappa > F(1, 8)

print("PASS: weighted character Banach algebra and parity-tail constants M4=21, K4<=8")
print("PASS: PF-I16 weighted character fixed point maps the 2 beta ball into itself")
print("PASS: contraction constant 672 beta <= 0.02688")
print(f"PASS: weighted gradient-character coefficient ratio = {float(c5_ratio):.9f} < 21.879")
print("PASS: exact shared-link Casimir norm is bounded by (n+1)(m+1)/4")
print("PASS: face projective norm <= 256 b0")
print(f"PASS: corrected pair projective norm <= {float(pair_norm_coeff):.6f} b0^2/a0")
print(f"DIAGNOSTIC: face activity = {float(face_activity):.9f}")
print(f"DIAGNOSTIC: corrected pair activity = {float(pair_activity):.9f}")
print(f"DIAGNOSTIC: corrected kappa_pi <= {float(kappa):.9f}; 2*kappa_pi = {float(2*kappa):.9f} > 1/8")
print("SCOPE: improved sufficient projective majorant still does not certify the 1/8 criterion.")
print("SCOPE: this verifier does not prove the analytic fixed-point theorem, joint support tree, KP convergence, or mass gap.")
