#!/usr/bin/env python3
"""Exact finite-state regression checks for the three-row path-support lemma.

The proof is analytic and appears in the companion audit. This script checks the
conditional-expectation identity and its L2-gap bound on independent two-state
stationary Markov paths, using exact rational arithmetic.
"""
from fractions import Fraction
from itertools import product


def transition(q, steps):
    one = (1 + q ** steps) / 2
    zero = (1 - q ** steps) / 2
    return ((one, zero), (zero, one))


def path_joint(q, steps):
    p = transition(q, steps)
    # Joint law of (X_0, X_steps), with stationary uniform initial state.
    return tuple(
        (x, y, Fraction(1, 2) * p[x][y])
        for x in range(2) for y in range(2)
    )


def centered_mean(values):
    return sum(values, Fraction(0)) / len(values)


def check_case(q, d1, d3):
    p1 = path_joint(q, d1)
    p3 = path_joint(q, d3)
    signs1 = list(product((-1, 1), repeat=2))
    signs3 = list(product((-1, 1), repeat=2))
    signs2 = list(product((-1, 1), repeat=4))

    for f1 in signs1:
        mu1 = centered_mean(f1)
        for f3 in signs3:
            mu3 = centered_mean(f3)
            for f2 in signs2:
                mu2 = centered_mean(f2)
                cumulant = Fraction(0)
                rhs_identity = Fraction(0)
                for a0, a2, wa in p1:
                    for b2, b3, wb in p3:
                        weight = wa * wb
                        cumulant += weight * (
                            (f1[a0] - mu1)
                            * (f2[2 * a2 + b2] - mu2)
                            * (f3[b3] - mu3)
                        )
                        # Conditional expectations given the middle states.
                        alpha = (q ** d1) * (f1[a2] - mu1)
                        beta = (q ** d3) * (f3[b2] - mu3)
                        rhs_identity += weight * alpha * f2[2 * a2 + b2] * beta

                assert cumulant == rhs_identity, (q, d1, d3, f1, f2, f3)
                bound = q ** (d1 + d3)
                assert abs(cumulant) <= bound, (
                    q, d1, d3, f1, f2, f3, cumulant, bound
                )


cases = 0
for q in (Fraction(1, 2), Fraction(2, 3), Fraction(3, 4)):
    for d1, d3 in ((1, 1), (1, 2), (2, 1), (2, 3)):
        check_case(q, d1, d3)
        cases += 1

print(f"PASS: exact path cumulant identity and temporal product bound in {cases} parameter cases")
print("PASS: exhaustive sign-valued f1, f2, f3 on each two-state product-path model")
print("SCOPE: finite-state regression only; analytic proof and general all-orders theorem are in the audit")
