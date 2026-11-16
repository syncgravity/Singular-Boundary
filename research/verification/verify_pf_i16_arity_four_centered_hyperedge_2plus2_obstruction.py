#!/usr/bin/env python3
"""Exact rational check of the four-slot 2+2 partition obstruction."""
from fractions import Fraction
from itertools import product


def main():
    states = list(product((-1, 1), repeat=2))
    probability = Fraction(1, 4)
    # Y1=Y2=U and Y3=Y4=V.
    def expectation(fn):
        return sum(probability * fn(u, v) for u, v in states)

    means = [
        expectation(lambda u, v: u),
        expectation(lambda u, v: u),
        expectation(lambda u, v: v),
        expectation(lambda u, v: v),
    ]
    assert means == [0, 0, 0, 0]

    pair = {}
    for i, j in product(range(4), repeat=2):
        if i < j:
            pair[(i, j)] = expectation(
                lambda u, v, i=i, j=j:
                    ([u, u, v, v][i]) * ([u, u, v, v][j])
            )
    fourth_moment = expectation(lambda u, v: u*u*v*v)
    fourth_cumulant = fourth_moment - (
        pair[(0,1)]*pair[(2,3)]
        + pair[(0,2)]*pair[(1,3)]
        + pair[(0,3)]*pair[(1,2)]
    )
    assert fourth_moment == 1
    assert pair[(0,1)] == 1 and pair[(2,3)] == 1
    assert all(pair[p] == 0 for p in ((0,2),(0,3),(1,2),(1,3)))
    assert fourth_cumulant == 0
    print("PASS: centered fourth moment=1, pair-pair contribution=1, kappa_4=0")
    print("LIMIT: obstruction to naive arity-four centering only")


if __name__ == "__main__":
    main()
