#!/usr/bin/env python3
"""Finite exact-rational regression for the one-link temporal-tree inequality.

Checks the cyclic-run weight recurrence and the leaf-attachment lower bound
for q <= 7 and several gap profiles. The all-orders proof is in the audit.
This does not verify the Markov semigroup or the multi-link support tree.
"""
from fractions import Fraction
from itertools import permutations, product


def cycle_weight(cycle, gaps):
    """Product of exp(-Delta * run spans), with edge weights given by gaps."""
    weight = Fraction(1)
    run_start = cycle[0]
    previous = cycle[0]
    for vertex in cycle[1:]:
        if vertex > previous:
            previous = vertex
        else:
            for k in range(run_start, previous):
                weight *= gaps[k]
            run_start = vertex
            previous = vertex
    for k in range(run_start, previous):
        weight *= gaps[k]
    return weight


def cycle_sum(n, gaps):
    return sum(
        cycle_weight((0,) + tail, gaps)
        for tail in permutations(range(1, n))
    )


def prufer_tree_edges(n, sequence):
    if n == 1:
        return []
    degree = [1] * n
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


def tree_sum(n, gaps):
    if n == 1:
        return Fraction(1)
    total = Fraction(0)
    for sequence in product(range(n), repeat=n - 2):
        weight = Fraction(1)
        for i, j in prufer_tree_edges(n, sequence):
            for k in range(min(i, j), max(i, j)):
                weight *= gaps[k]
        total += weight
    return total


def check_profile(gaps):
    for n in range(2, len(gaps) + 1):
        lhs = cycle_sum(n, gaps[:n - 1])
        rhs = tree_sum(n, gaps[:n - 1])
        assert lhs <= (2 ** (n - 2)) * rhs, (n, gaps, lhs, rhs)

        if n >= 3:
            prev_w = cycle_sum(n - 1, gaps[:n - 2])
            prev_t = tree_sum(n - 1, gaps[:n - 2])
            r = [product(gaps[i:n - 1]) for i in range(n - 1)]
            assert lhs <= 2 * prev_w * sum(r)
            assert rhs >= prev_t * sum(r)


def main():
    profiles = [
        [Fraction(1, 2)] * 6,
        [Fraction(1, 3), Fraction(1, 2), Fraction(1, 4),
         Fraction(1, 2), Fraction(1, 3), Fraction(1, 4)],
        [Fraction(1)] * 6,  # repeated observation times
        [Fraction(1, 100), Fraction(1), Fraction(1, 100),
         Fraction(1), Fraction(1, 100), Fraction(1)],
        [Fraction(1, 5), Fraction(1, 5), Fraction(1),
         Fraction(1, 5), Fraction(1, 5), Fraction(1)],
    ]
    for i, gaps in enumerate(profiles, 1):
        check_profile(gaps)
        print(f"PASS profile {i}: exact cycle/tree inequalities through q={len(gaps)+1}")
    print("LIMIT: finite regression only; no multi-link LS projection bound")


if __name__ == "__main__":
    main()
