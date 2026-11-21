#!/usr/bin/env python3
"""Exact rational regression for the interval-gap cyclic tree inequality."""
from fractions import Fraction
from itertools import combinations, permutations, product


def edge_weight(i, j, intervals, rho):
    if i < j:
        return rho ** (intervals[j][0] - intervals[i][1])
    return Fraction(1)


def cycle_sum(intervals, rho):
    q = len(intervals)
    total = Fraction(0)
    for tail in permutations(range(1, q)):
        cycle = (0,) + tail
        weight = Fraction(1)
        for k in range(q):
            a, b = cycle[k], cycle[(k + 1) % q]
            if a < b:
                weight *= edge_weight(a, b, intervals, rho)
        total += weight
    return total


def prufer_tree(sequence, q):
    degree = [1] * q
    for x in sequence:
        degree[x] += 1
    edges = []
    for x in sequence:
        leaf = next(i for i, d in enumerate(degree) if d == 1)
        edges.append((leaf, x))
        degree[leaf] -= 1
        degree[x] -= 1
    leaves = [i for i, d in enumerate(degree) if d == 1]
    edges.append((leaves[0], leaves[1]))
    return edges


def tree_sum(intervals, rho):
    q = len(intervals)
    if q == 2:
        return edge_weight(0, 1, intervals, rho)
    total = Fraction(0)
    for code in product(range(q), repeat=q - 2):
        tree = prufer_tree(code, q)
        weight = Fraction(1)
        for i, j in tree:
            weight *= edge_weight(min(i, j), max(i, j), intervals, rho)
        total += weight
    return total


def check(intervals, rho, tag):
    q = len(intervals)
    assert q >= 2
    assert all(intervals[i][1] < intervals[i + 1][0] for i in range(q - 1))
    wq = cycle_sum(intervals, rho)
    tq = tree_sum(intervals, rho)
    assert wq <= (2 ** (q - 2)) * tq, (tag, wq, tq)

    if q >= 3:
        previous = cycle_sum(intervals[:-1], rho)
        leaf_weights = sum(
            edge_weight(i, q - 1, intervals, rho)
            for i in range(q - 1)
        )
        assert wq <= 2 * previous * leaf_weights, (tag, "cycle insertion")
        previous_tree = tree_sum(intervals[:-1], rho)
        assert tq >= previous_tree * leaf_weights, (tag, "tree leaf attachment")
    print(f"PASS {tag}: q={q}, exact interval-gap tree inequality")


def main():
    rho = Fraction(2, 3)
    fixtures = [
        [(0,1),(3,4)],
        [(0,0),(2,5),(8,9)],
        [(0,2),(4,4),(7,10),(14,15)],
        [(0,1),(3,6),(8,8),(10,13),(17,19)],
        [(0,3),(5,5),(7,9),(12,15),(18,18),(21,24)],
        [(0,0),(2,4),(7,8),(10,12),(15,17),(20,20),(22,25)],
    ]
    for k, intervals in enumerate(fixtures, start=2):
        check(intervals, rho, f"interval-fixture-{k}")
    print("LIMIT: exact cycle/tree combinatorics; transfer-operator identity is analytic")


if __name__ == "__main__":
    main()
