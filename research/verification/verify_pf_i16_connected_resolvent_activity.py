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
