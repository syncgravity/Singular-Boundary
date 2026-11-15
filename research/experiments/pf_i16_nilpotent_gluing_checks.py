#!/usr/bin/env python3
"""Exact finite checks for PF-I16 nilpotent row projection examples.

No external dependencies. Run:
    python research/experiments/pf_i16_nilpotent_gluing_checks.py
These tests validate finite moment/cumulant identities only; they do not
establish a weighted all-orders estimate.
"""
from math import factorial


def partitions(items):
    """Yield each set partition exactly once as a tuple of tuple blocks."""
    items = tuple(items)
    if not items:
        yield ()
        return
    first, *rest = items
    for p in partitions(rest):
        yield ((first,),) + p
        for j in range(len(p)):
            yield p[:j] + (tuple(sorted((first,) + p[j])),) + p[j + 1:]


def cumulant(moment, rows):
    """Moment-cumulant formula on a finite row set."""
    rows = tuple(rows)
    total = 0
    for p in partitions(rows):
        k = len(p)
        coefficient = (-1) ** (k - 1) * factorial(k - 1)
        product = 1
        for block in p:
            product *= moment(frozenset(block))
        total += coefficient * product
    return total


def product_link_moment(subset, incidences, link_moments):
    """Independent-link row moment after all-or-none row projection."""
    value = 1
    for link, incident_rows in incidences.items():
        active = frozenset(subset & incident_rows)
        value *= link_moments[link](active)
    return value


def rademacher_moment(subset):
    return 1 if len(subset) % 2 == 0 else 0


def test_two_row_two_link_gluing():
    # Link-e moments: means (2,3), joint moment 11 -> covariance 5.
    # Link-f moments: means (5,7), joint moment 41 -> covariance 6.
    me = {frozenset(): 1, frozenset({1}): 2, frozenset({2}): 3,
          frozenset({1, 2}): 11}
    mf = {frozenset(): 1, frozenset({1}): 5, frozenset({2}): 7,
          frozenset({1, 2}): 41}
    moment = lambda s: me[s] * mf[s]
    kappa = cumulant(moment, (1, 2))
    ce, cf = 11 - 2 * 3, 41 - 5 * 7
    rhs = ce * cf + ce * 5 * 7 + 2 * 3 * cf
    assert kappa == rhs == 11 * 41 - (2 * 5) * (3 * 7)


def test_centered_three_row_path():
    def link_pair(c):
        return lambda s: 1 if not s else (0 if len(s) == 1 else c)
    incidences = {"e": frozenset({1, 2}), "f": frozenset({2, 3})}
    lm = {"e": link_pair(2), "f": link_pair(3)}
    moment = lambda s: product_link_moment(s, incidences, lm)
    assert cumulant(moment, (1, 2, 3)) == 6


def test_centered_four_row_path():
    incidences = {
        "e12": frozenset({1, 2}),
        "e23": frozenset({2, 3}),
        "e34": frozenset({3, 4}),
    }
    lm = {link: link_pair(c) for link, c in (
        ("e12", 2), ("e23", 3), ("e34", 5)
    )}
    moment = lambda s: product_link_moment(s, incidences, lm)
    assert cumulant(moment, (1, 2, 3, 4)) == 2 * 3 * 5


def link_pair(c):
    return lambda s: 1 if not s else (0 if len(s) == 1 else c)


def test_degree_eight_rademacher_witness():
    value = cumulant(rademacher_moment, tuple(range(1, 9)))
    assert value == -272


def main():
    test_two_row_two_link_gluing()
    test_centered_three_row_path()
    test_centered_four_row_path()
    test_degree_eight_rademacher_witness()
    print("PASS: two-link gluing, 3-row path, 4-row path, and Rademacher kappa_8=-272")


if __name__ == "__main__":
    main()
