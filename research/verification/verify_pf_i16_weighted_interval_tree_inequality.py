#!/usr/bin/env python3
"""Exact finite checks for the one-link weighted interval-tree conjecture.

For n ordered ports, enumerate perfect matchings M whose interval-overlap graph
H_M is connected. Check
    sum_M tau(H_M) prod_(a,b in M) r_ab
        <= sum_T prod_(i,j in T) r_ij,
where r_ij is the product of rational adjacent-gap factors q_k in (0,1].
This is a regression experiment, not a proof of the conjectured inequality.
"""
from fractions import Fraction
from itertools import combinations


def perfect_matchings(items):
    items = tuple(items)
    if not items:
        yield ()
        return
    a = items[0]
    for j in range(1, len(items)):
        b = items[j]
        rest = items[1:j] + items[j + 1:]
        for tail in perfect_matchings(rest):
            yield ((a, b),) + tail


def intervals_overlap(I, J):
    a, b = I
    c, d = J
    return max(a, c) < min(b, d)


def connected(n, edges):
    if n <= 1:
        return True
    adj = [set() for _ in range(n)]
    for a, b in edges:
        adj[a].add(b)
        adj[b].add(a)
    seen = {0}
    stack = [0]
    while stack:
        v = stack.pop()
        for w in adj[v] - seen:
            seen.add(w)
            stack.append(w)
    return len(seen) == n


def tree_count(n, edges):
    if n <= 1:
        return 1
    total = 0
    for chosen in combinations(edges, n - 1):
        if connected(n, chosen):
            total += 1
    return total


def determinant(A):
    A = [[Fraction(x) for x in row] for row in A]
    n = len(A)
    if n == 0:
        return Fraction(1)
    sign = 1
    result = Fraction(1)
    for k in range(n):
        pivot_row = next((i for i in range(k, n) if A[i][k]), None)
        if pivot_row is None:
            return Fraction(0)
        if pivot_row != k:
            A[k], A[pivot_row] = A[pivot_row], A[k]
            sign = -sign
        pivot = A[k][k]
        result *= pivot
        for i in range(k + 1, n):
            factor = A[i][k] / pivot
            for j in range(k + 1, n):
                A[i][j] -= factor * A[k][j]
            A[i][k] = 0
    return sign * result


def weighted_tree_sum(weights):
    n = len(weights)
    laplacian = [[Fraction(0) for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            w = weights[i][j]
            laplacian[i][i] += w
            laplacian[j][j] += w
            laplacian[i][j] -= w
            laplacian[j][i] -= w
    return determinant([row[:-1] for row in laplacian[:-1]])


def check(n, gap_factors):
    weights = [[Fraction(1) for _ in range(n)] for _ in range(n)]
    for i in range(n):
        product = Fraction(1)
        for j in range(i + 1, n):
            product *= gap_factors[j - 1]
            weights[i][j] = weights[j][i] = product

    lhs = Fraction(0)
    connected_matchings = 0
    for matching in perfect_matchings(range(n)):
        intervals = tuple(tuple(sorted(pair)) for pair in matching)
        overlap_edges = tuple(
            (i, j)
            for i in range(len(intervals))
            for j in range(i + 1, len(intervals))
            if intervals_overlap(intervals[i], intervals[j])
        )
        multiplicity = tree_count(len(intervals), overlap_edges)
        if multiplicity == 0:
            continue
        connected_matchings += 1
        matching_weight = Fraction(1)
        for a, b in intervals:
            matching_weight *= weights[a][b]
        lhs += multiplicity * matching_weight

    rhs = weighted_tree_sum(weights)
    assert lhs <= rhs, (n, gap_factors, lhs, rhs)
    return connected_matchings


def main():
    for n in (4, 6, 8, 10):
        patterns = (
            (Fraction(1, 2),) * (n - 1),
            (Fraction(1, 3),) * (n - 1),
            (Fraction(3, 4),) * (n - 1),
            tuple(Fraction(i + 1, i + 3) for i in range(n - 1)),
        )
        for factors in patterns:
            count = check(n, factors)
            print(f"PASS n={n}, connected interval matchings={count}, gaps={factors}")
    print("PASS exact rational checks of the tau(H)-weighted one-link inequality")
    print("NOTE finite regression only; no general weighted inequality is proved")


if __name__ == "__main__":
    main()
