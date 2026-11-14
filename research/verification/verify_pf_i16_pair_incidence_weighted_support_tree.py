#!/usr/bin/env python3
"""Exact finite-state regression for pair-incidence weighted tree cumulants.

Each link is a stationary two-state reset chain shared by exactly two rows.
Rows are arbitrary sign-valued functions of their incident link states.
The analytic deletion-contraction proof is in the companion audit.
"""
from fractions import Fraction
from itertools import product
from math import factorial


def partitions(items):
    if not items:
        yield []
        return
    first = items[0]
    for p in partitions(items[1:]):
        yield [[first]] + [b[:] for b in p]
        for j in range(len(p)):
            q = [b[:] for b in p]
            q[j] = [first] + q[j]
            yield q


def transition(q, d, x, y):
    return Fraction(1, 2) * (1 + (q ** d if x == y else -q ** d))


def graph_data(edges, times, q):
    n = len(times)
    incident = [[] for _ in range(n)]
    for e, (u, v) in enumerate(edges):
        incident[u].append((e, 0))
        incident[v].append((e, 1))
    local_index = {
        (v, e): k for v, row in enumerate(incident)
        for k, (e, _) in enumerate(row)
    }
    assignments = list(product(range(2), repeat=2 * len(edges)))
    weighted = []
    masks = []
    for state in assignments:
        w = Fraction(1)
        row_masks = [0] * n
        for e, (u, v) in enumerate(edges):
            xu, xv = state[2 * e], state[2 * e + 1]
            w *= transition(q, abs(times[u] - times[v]), xu, xv)
            if xu:
                row_masks[u] |= 1 << local_index[(u, e)]
            if xv:
                row_masks[v] |= 1 << local_index[(v, e)]
        weighted.append(w)
        masks.append(row_masks)
    return incident, weighted, masks


def tree_polynomial(edges, times, q):
    n = len(times)
    total = Fraction(0)
    for chosen in __import__("itertools").combinations(edges, n - 1):
        parent = list(range(n))

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        w = Fraction(1)
        good = True
        for u, v in chosen:
            a, b = find(u), find(v)
            if a == b:
                good = False
                break
            parent[a] = b
            w *= q ** abs(times[u] - times[v])
        if good and len({find(i) for i in range(n)}) == 1:
            total += w
    return total


def cumulant(values_by_assignment, weights, n):
    moments = {}
    for mask in range(1, 1 << n):
        moments[mask] = sum(
            (w * __import__("math").prod(
                values[i] for i in range(n) if mask & (1 << i)
            ) for w, values in zip(weights, values_by_assignment)),
            Fraction(0)
        )
    answer = Fraction(0)
    for part in partitions(list(range(n))):
        term = (-1) ** (len(part) - 1) * factorial(len(part) - 1)
        for block in part:
            mask = sum(1 << i for i in block)
            term *= moments[mask]
        answer += term
    return answer


def check_graph(edges, times, q, exhaustive=False):
    n = len(times)
    incident, weights, masks = graph_data(edges, times, q)
    function_lists = [list(product((-1, 1), repeat=1 << len(row)))
                      for row in incident]
    choices = product(*function_lists)
    checked = 0
    target = tree_polynomial(edges, times, q)
    for funcs in choices:
        values = [
            [funcs[i][masks[k][i]] for i in range(n)]
            for k in range(len(weights))
        ]
        kappa = cumulant(values, weights, n)
        assert abs(kappa) <= target, (edges, times, q, funcs, kappa, target)
        checked += 1
        if not exhaustive and checked >= 512:
            break
    return checked


def main():
    q = Fraction(1, 2)
    triangle = [(0, 1), (1, 2), (2, 0)]
    cycle4 = [(0, 1), (1, 2), (2, 3), (3, 0)]
    star4 = [(0, 1), (0, 2), (0, 3)]
    c3 = check_graph(triangle, [0, 2, 1], q, exhaustive=True)
    c4 = check_graph(cycle4, [0, 2, 1, 3], q, exhaustive=False)
    s4 = check_graph(star4, [0, 1, 2, 4], q, exhaustive=False)
    print(f"PASS: exhaustive triangle sign-functions: {c3}")
    print(f"PASS: deterministic cycle-four cases: {c4}")
    print(f"PASS: deterministic star-four cases: {s4}")
    print("SCOPE: pair-incidence two-state Markov models only; general proof is in the audit")


if __name__ == "__main__":
    main()
