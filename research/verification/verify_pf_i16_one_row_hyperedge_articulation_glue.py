#!/usr/bin/env python3
"""Exact rational regression for one-row-intersection cumulant gluing."""
from fractions import Fraction
from itertools import product


def partitions(items):
    items = tuple(items)
    if not items:
        yield ()
        return
    first, *rest = items
    for p in partitions(rest):
        yield ((first,),) + p
        for k in range(len(p)):
            yield p[:k] + (p[k] + (first,),) + p[k + 1:]


def cumulant(indices, moment):
    indices = tuple(indices)
    total = Fraction(0)
    for part in partitions(indices):
        coefficient = (-1) ** (len(part) - 1)
        coefficient *= factorial(len(part) - 1)
        term = Fraction(coefficient)
        for block in part:
            term *= moment(frozenset(block))
        total += term
    return total


def factorial(n):
    out = 1
    for k in range(2, n + 1):
        out *= k
    return out


def sample_moments(q, family):
    weights = [Fraction(1, 15), Fraction(2, 15), Fraction(3, 15),
               Fraction(4, 15), Fraction(5, 15)]
    rows = []
    for state in range(5):
        values = []
        for i in range(q):
            if family == "X":
                numerator = (state + 1) * (i + 2) + (-1) ** (state + i)
                values.append(Fraction(numerator, 3))
            else:
                numerator = (state + 2) * (i + 1) - (-1) ** (state * (i + 1))
                values.append(Fraction(numerator, 4))
        rows.append(values)

    def moment(subset):
        return sum(
            weights[state] * prod(rows[state][i] for i in subset)
            for state in range(5)
        )
    return moment


def check(qx, qy):
    # The unique shared row is 0. H1={0,...,qx-1}; H2={0,qx,...,qx+qy-2}.
    r = qx + qy - 1
    mx = sample_moments(qx, "X")
    my = sample_moments(qy, "Y")
    h1 = set(range(qx))
    h2 = {0} | set(range(qx, r))

    def row_moment(subset):
        ix = frozenset(i for i in subset if i in h1)
        iy = frozenset(0 if i == 0 else i - qx + 1
                       for i in subset if i in h2)
        return mx(ix) * my(iy)

    lhs = cumulant(range(r), row_moment)
    rhs = cumulant(range(qx), mx) * cumulant(range(qy), my)
    assert lhs == rhs, (qx, qy, lhs, rhs)

    # Ensure the regression includes genuinely nonzero one-point means.
    assert mx(frozenset({0})) != 0
    assert my(frozenset({0})) != 0
    print(f"PASS |H1|={qx}, |H2|={qy}, R={r}, exact cumulant identity")


def main():
    for qx, qy in product(range(1, 5), repeat=2):
        check(qx, qy)
    print("LIMIT: exact finite algebra only; no multi-overlap or multi-link bound")


if __name__ == "__main__":
    main()
