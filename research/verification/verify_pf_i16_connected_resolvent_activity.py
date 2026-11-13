#!/usr/bin/env python3
"""Exact rational checks for PF-I16 two-cut local activity bounds.

The verifier checks the incidence and arithmetic bounds only. It does not
prove the quantum connected-resolvent/tree lemma or a polymer theorem.
"""
from fractions import Fraction

x = Fraction(1, 50_000)
delta = Fraction(3, 4)
sqrt_e_upper = Fraction(165, 100)  # exp(1/2) < 1.65
e_upper = Fraction(272, 100)       # exp(1) < 2.72
a = Fraction(1, 8)

# Per-face local operator bounds divided by a0.
h_one = 64*x + 64*x*x
h_pair = 512*x*x
cut_one = 64*x + 256*x*x
cut_pair = 1024*x*x
cut2_one = 64*x + 768*x*x
cut2_pair = 2048*x*x

# At most eight incident faces and 8*28 pair supports per link.
def weighted(one, pair):
    return (8*one*sqrt_e_upper + 224*pair*e_upper) / delta

kappa_h = weighted(h_one, h_pair)
kappa_cut = weighted(cut_one, cut_pair)
kappa_cut2 = weighted(cut2_one, cut2_pair)

assert kappa_h == Fraction(16622186, 732421875)
assert kappa_cut == Fraction(16745032, 732421875)
assert kappa_cut2 == Fraction(16991384, 732421875)

assert kappa_h < Fraction(22695, 1_000_000)
assert kappa_cut < Fraction(22863, 1_000_000)
assert kappa_cut2 < Fraction(23199, 1_000_000)

q_path = 8 * e_upper * kappa_h
assert q_path < Fraction(494, 1000)

print(f"PASS: kappa_H < {float(kappa_h):.12g} < 0.022695")
print(f"PASS: kappa_cut < {float(kappa_cut):.12g} < 0.022863")
print(f"PASS: kappa_cut2 < {float(kappa_cut2):.12g} < 0.023199")
print(f"PASS: q_path < {float(q_path):.12g} < 0.494")
print("NOTE: no quantum time-ordered resolvent or cluster theorem is asserted.")


# Follow-up arithmetic after the exact temporal port-injection (2026-11-13)
# These are candidate arithmetic checks only. They are NOT a Kotecky-Preiss
# criterion until the joint space-time tree expansion is proved.
C_time = 2
proposed_kp = 2 * C_time * kappa_h
q_path_with_time = C_time * q_path
assert proposed_kp < Fraction(1, 8)
assert q_path_with_time < 1

# The direct temporal-tree integral contributes a further factor 2 per
# integrated edge; Stirling on m^(m-2)/m! contributes e^m.
temporal_base = 2 * C_time * e_upper
per_link_overlap_base = temporal_base * 8 * Fraction(22695, 1_000_000)

# Face/pair grouping gives a much smaller candidate local activity.
z_face = 32*x + 14336*x*x
z_face_ratio = z_face / delta
q_face = 58 * z_face_ratio
q_joint_candidate = temporal_base * e_upper * q_face / e_upper
# The last expression is written this way to keep the single e-factor explicit:
# q_joint_candidate = (2*C_time) * e * (2) * q_face = 4*e*q_face.
q_joint_candidate = 4 * e_upper * q_face

assert z_face_ratio < Fraction(8610, 10_000_000)
assert q_face < Fraction(49937, 1_000_000)
assert q_joint_candidate < Fraction(544, 1000)

print(f"PASS: arithmetic candidate 2*C_time*kappa_H = {float(proposed_kp):.12g} < 1/8")
print(f"PASS: arithmetic candidate C_time*q_path = {float(q_path_with_time):.12g} < 1")
print(f"DIAGNOSTIC: temporal-integrated base 2*C_time*e <= {float(temporal_base):.6g}")
print(f"DIAGNOSTIC: crude per-link overlap continuation <= {float(per_link_overlap_base):.6g} (not < 1)")
print(f"PASS: face activity z_face/Delta_0 < {float(z_face_ratio):.12g}")
print(f"PASS: 58-face-neighborhood q_face < {float(q_face):.12g}")
print(f"PASS: conditional single-tree candidate 4*e*q_face < {float(q_joint_candidate):.12g} < 1")
print("SCOPE: all values above are arithmetic only. The joint support-sensitive space-time tree lemma and the actual KP criterion remain OPEN.")
