#!/usr/bin/env python3
"""Exact rational regression for centered connected pair/triple hyperedges."""
from fractions import Fraction
from itertools import combinations, product as cartesian_product
from math import prod
from math import factorial


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
    total = Fraction(0)
    for part in partitions(tuple(indices)):
        term = Fraction((-1) ** (len(part) - 1) * factorial(len(part) - 1))
        for block in part:
            term *= moment(frozenset(block))
        total += term
    return total


def local_law(q, seed):
    # A rational positive tilt of a product Rademacher law:
    # p(x) proportional to prod_i(1+a_i*x_i) * (1+theta*prod_i x_i).
    aa = [Fraction(1, 5 + seed + i) for i in range(q)]
    theta = Fraction(1, 7 + seed)
    norm = 1 + theta * prod(aa)
    law = {}
    for x in cartesian_product((-1, 1), repeat=q):
        p = prod((1 + aa[i]*x[i]) / 2 for i in range(q))
        p *= (1 + theta * prod(x)) / norm
        assert p > 0
        law[x] = p
    means = [
        sum(p*x[i] for x, p in law.items())
        for i in range(q)
    ]

    def centered_moment(indices):
        out = Fraction(0)
        for x, p in law.items():
            term = p
            for i in indices:
                term *= x[i] - means[i]
            out += term
        return out

    def raw_moment(indices):
        return sum(
            p * prod(x[i] for i in indices)
            for x, p in law.items()
        )

    return means, centered_moment, raw_moment


def connected(n, selected):
    adjacency = [set() for _ in range(n)]
    for edge in selected:
        for i, j in combinations(edge, 2):
            adjacency[i].add(j)
            adjacency[j].add(i)
    seen = {0}
    stack = [0]
    while stack:
        i = stack.pop()
        for j in adjacency[i] - seen:
            seen.add(j)
            stack.append(j)
    return len(seen) == n


def check(n, hyperedges, tag):
    data = [local_law(len(e), k + 1) for k, e in enumerate(hyperedges)]
    index_maps = [{row: i for i, row in enumerate(edge)} for edge in hyperedges]

    def moment(rows):
        value = Fraction(1)
        for edge, mapping, (_, _, raw) in zip(hyperedges, index_maps, data):
            local = [mapping[i] for i in rows if i in mapping]
            value *= raw(local)
        return value

    lhs = cumulant(range(n), moment)

    choices = []
    for edge in hyperedges:
        local = [()]
        local.extend(combinations(edge, 2))
        if len(edge) == 3:
            local.append(tuple(edge))
        choices.append(local)

    rhs = Fraction(0)
    for selection in product(*choices):
        active = [tuple(s) for s in selection if s]
        if not active or not connected(n, active):
            continue
        term = Fraction(1)
        for edge, selected, mapping, (means, centered, _) in zip(
            hyperedges, selection, index_maps, data
        ):
            if selected:
                local = [mapping[i] for i in selected]
                term *= centered(local)
            for row in edge:
                if row not in selected:
                    term *= means[mapping[row]]
        rhs += term

    assert lhs == rhs, (tag, lhs, rhs)
    print(f"PASS {tag}: rows={n}, links={len(hyperedges)}, exact rational identity")


def main():
    fixtures = [
        (3, [(0,1,2)], "single-triple"),
        (4, [(0,1,2),(1,2,3)], "overlapping-triples"),
        (6, [(0,1,2),(2,3,4),(4,5,0)], "cyclic-triples"),
        (4, [(0,1,2),(1,2,3),(0,2,3)], "dense-triple-cycle"),
        (5, [(0,1,2),(2,3),(3,4,0)], "mixed-pair-triple-cycle"),
        (3, [(0,1,2),(0,1,2)], "parallel-triples"),
        (4, [(0,1,2),(0,1,2),(2,3)], "parallel-and-bridge"),
        (6, [(0,1,2),(2,3,4),(4,5,0),(1,3,5)], "four-triple-cycle"),
    ]
    for fixture in fixtures:
        check(*fixture)
    print("LIMIT: exact arity<=3 algebra only; arity>=4 remains open")


if __name__ == "__main__":
    main()
