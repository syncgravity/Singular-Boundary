#!/usr/bin/env python3
"""Exact rational tests of cumulant factorization on incidence trees."""
from fractions import Fraction
from itertools import product
from math import prod


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


def factorial(n):
    out = 1
    for k in range(2, n + 1):
        out *= k
    return out


def cumulant(indices, moment):
    total = Fraction(0)
    for part in partitions(tuple(indices)):
        term = Fraction((-1) ** (len(part) - 1) * factorial(len(part) - 1))
        for block in part:
            term *= moment(frozenset(block))
        total += term
    return total


def link_moments(q, seed):
    weights = [Fraction(1, 15), Fraction(2, 15), Fraction(3, 15),
               Fraction(4, 15), Fraction(5, 15)]
    samples = []
    for state in range(5):
        values = []
        for i in range(q):
            sign = (-1) ** (state + i + seed)
            numerator = (state + 1 + seed) * (i + 2) + sign
            values.append(Fraction(numerator, 3 + seed))
        samples.append(values)

    def moment(subset):
        return sum(weights[s] * prod(samples[s][i] for i in subset)
                   for s in range(5))
    return moment


def check(hyperedges):
    # The test fixtures are grown by one-row attachments; their incidence
    # bipartite graph is therefore a tree by construction.
    rows = sorted(set().union(*(set(h) for h in hyperedges)))
    assert rows == list(range(len(rows)))
    local_maps = []
    local_moments = []
    for e, h in enumerate(hyperedges):
        ordered = tuple(h)
        local_maps.append({row: i for i, row in enumerate(ordered)})
        local_moments.append(link_moments(len(ordered), e + 1))

    def row_moment(subset):
        value = Fraction(1)
        for h, index, moment in zip(hyperedges, local_maps, local_moments):
            local_subset = frozenset(index[i] for i in subset if i in index)
            value *= moment(local_subset)
        return value

    lhs = cumulant(rows, row_moment)
    rhs = Fraction(1)
    for h, moment in zip(hyperedges, local_moments):
        rhs *= cumulant(range(len(h)), moment)
        assert moment(frozenset({0})) != 0  # nonzero means
    assert lhs == rhs, (hyperedges, lhs, rhs)
    print(f"PASS incidence tree {hyperedges}: exact factorization")


def main():
    fixtures = [
        [[0, 1, 2]],
        [[0, 1], [1, 2, 3]],
        [[0, 1, 2], [2, 3, 4], [0, 5, 6]],
        [[0, 1], [1, 2, 3], [3, 4], [0, 5, 6]],
        [[0, 1, 2, 3], [0, 4], [2, 5, 6], [4, 7]],
        [[0], [0, 1], [0, 2], [1, 3]],
        [[0, 1], [0, 2], [0, 3], [0, 4]],
    ]
    for fixture in fixtures:
        check(fixture)
    print("LIMIT: exact finite algebra only; cyclic incidence remains open")


if __name__ == "__main__":
    main()
