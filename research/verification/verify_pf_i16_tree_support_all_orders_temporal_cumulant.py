#!/usr/bin/env python3
"""Exact finite-state regression for the all-orders tree-support cumulant bound.

Tests arbitrary sign-valued row functions on small tree support graphs for
independent two-state stationary reset chains. The general result is proved
analytically in the companion audit; this finite check is supplementary.
"""
from fractions import Fraction
from itertools import product
from math import prod


def partitions(items):
    if not items:
        yield []
        return
    first = items[0]
    for p in partitions(items[1:]):
        yield [[first]] + [block[:] for block in p]
        for j in range(len(p)):
            q = [block[:] for block in p]
            q[j] = [first] + q[j]
            yield q


def transition(q, distance, x, y):
    return (1 + q ** distance) / 2 if x == y else (1 - q ** distance) / 2


def check_tree(edges, times, q):
    n = len(times)
    incident = [[] for _ in range(n)]
    for e, (u, v) in enumerate(edges):
        incident[u].append((e, 0))
        incident[v].append((e, 1))
    local_index = {}
    for vertex, inc in enumerate(incident):
        for position, (edge, endpoint) in enumerate(inc):
            local_index[(vertex, edge)] = position
    row_sizes = [1 << len(inc) for inc in incident]
    row_functions = [list(product((-1, 1), repeat=size))
                     for size in row_sizes]

    # Each edge contributes its two endpoint states, independently of other edges.
    edge_assignments = list(product(range(2), repeat=2 * len(edges)))
    weighted_assignments = []
    row_masks = []
    for states in edge_assignments:
        weight = Fraction(1)
        masks = [0] * n
        for e, (u, v) in enumerate(edges):
            xu, xv = states[2 * e], states[2 * e + 1]
            distance = abs(times[u] - times[v])
            weight *= Fraction(1, 2) * transition(q, distance, xu, xv)
            for vertex, endpoint in ((u, 0), (v, 1)):
                if states[2 * e + endpoint]:
                    masks[vertex] |= 1 << local_index[(vertex, e)]
        weighted_assignments.append(weight)
        row_masks.append(masks)

    all_parts = list(partitions(list(range(n))))
    target = prod(q ** abs(times[u] - times[v]) for u, v in edges)
    checked = 0

    # Exhaustive sign-valued functions for the tested small trees.
    for funcs in product(*row_functions):
        moments = [Fraction(1)] * (1 << n)
        for mask in range(1, 1 << n):
            total = Fraction(0)
            for weight, states in zip(weighted_assignments, row_masks):
                value = 1
                for i in range(n):
                    if mask & (1 << i):
                        value *= funcs[i][states[i]]
                total += weight * value
            moments[mask] = total

        cumulant = Fraction(0)
        for part in all_parts:
            term = (-1) ** (len(part) - 1)
            term *= __import__("math").factorial(len(part) - 1)
            for block in part:
                mask = sum(1 << i for i in block)
                term *= moments[mask]
            cumulant += term
        assert abs(cumulant) <= target, (edges, times, q, funcs, cumulant, target)
        checked += 1
    return checked


tests = 0
tests += check_tree([(0, 1)], [0, 2], Fraction(1, 2))
tests += check_tree([(0, 1), (1, 2)], [0, 1, 3], Fraction(1, 2))
tests += check_tree([(0, 1), (1, 2), (2, 3)], [0, 1, 3, 4], Fraction(1, 2))
tests += check_tree([(0, 1), (0, 2), (0, 3)], [0, 1, 2, 4], Fraction(1, 2))

print(f"PASS: exact cumulant tree bound for {tests} exhaustive sign-valued row-function choices")
print("PASS: tested one-edge, path, and star support trees with nonuniform time gaps")
print("SCOPE: finite two-state models only; the general all-orders leaf-contraction proof is in the audit")
