#!/usr/bin/env python3
"""Exact rational counterexample to a coefficient-one interlaced-time mixing bound."""
from fractions import Fraction
from itertools import product


def path_law(q, last_time):
    for xs in product((-1, 1), repeat=last_time + 1):
        p = Fraction(1, 2)
        for x, y in zip(xs, xs[1:]):
            p *= (1 + q * x * y) / 2
        yield xs, p


def table_value(table, xs, times):
    index = sum((1 << j) for j, t in enumerate(times) if xs[t] == 1)
    return table[index]


def main():
    q = Fraction(1, 2)
    S, T = (0, 2, 4), (1, 3)
    f = (-1, -1, -1, 1, -1, -1, 1, 1)
    g = (-1, -1, -1, 1)
    ef = eg = efg = Fraction(0)
    for xs, p in path_law(q, 4):
        fv = table_value(f, xs, S)
        gv = table_value(g, xs, T)
        ef += p * fv
        eg += p * gv
        efg += p * fv * gv
    covariance = efg - ef * eg
    assert ef == Fraction(-9, 64)
    assert eg == Fraction(-3, 8)
    assert efg == Fraction(73, 128)
    assert covariance == Fraction(265, 512)
    assert covariance > q
    print("PASS: exact interlaced-time covariance counterexample")
    print(f"E[F]={ef}; E[G]={eg}; E[FG]={efg}")
    print(f"Cov(F,G)={covariance} > q={q}; minimum cross-set gap is one")
    print("SCOPE: refutes only the coefficient-one min-distance lemma")


if __name__ == "__main__":
    main()
