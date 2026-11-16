#!/usr/bin/env python3
"""Exact chromatic interval-overlap resummation for a symmetric binary chain.

Checks the perfect-matching reindexing of the cumulant, the interval-graph
chromatic coefficient, the chordal/PEO spanning-tree bound, and the temporal
path-tree majorant. This is a special-case verifier, not a general Markov proof.
"""
from fractions import Fraction as F
from itertools import combinations
from math import factorial


def partitions(items):
    items = tuple(items)
    if not items:
        yield ()
        return
    first, *rest = items
    for tail in partitions(rest):
        yield ((first,),) + tail
        for j in range(len(tail)):
            yield tail[:j] + (tuple(sorted(tail[j] + (first,))),) + tail[j + 1:]


def canon(part):
    return tuple(sorted((tuple(sorted(b)) for b in part), key=lambda b: b[0]))


def all_partitions(n):
    return sorted({canon(p) for p in partitions(range(n))})


def perfect_matchings(items):
    items = tuple(items)
    if not items:
        yield ()
        return
    first = items[0]
    for j in range(1, len(items)):
        second = items[j]
        rest = items[1:j] + items[j + 1:]
        for tail in perfect_matchings(rest):
            yield ((first, second),) + tail


def overlap_graph(matching):
    intervals = tuple(sorted((min(a, b), max(a, b)) for a, b in matching))
    edges = set()
    for i, (a, b) in enumerate(intervals):
        for j in range(i + 1, len(intervals)):
            c, d = intervals[j]
            if max(a, c) < min(b, d):
                edges.add((i, j))
    return intervals, edges


def chromatic_linear_coefficient(vertex_count, edges):
    total = 0
    for part in all_partitions(vertex_count):
        if any(any(u in block and v in block for u, v in edges)
               for block in part):
            continue
        k = len(part)
        total += (-1) ** (k - 1) * factorial(k - 1)
    return total


def peo_later_degrees(intervals, edges):
    # Nondecreasing right endpoints is a perfect-elimination ordering.
    order = sorted(range(len(intervals)), key=lambda i: (intervals[i][1], intervals[i][0]))
    position = {v: i for i, v in enumerate(order)}
    degrees = []
    for v in order[:-1]:
        degrees.append(sum(1 for a, b in edges
                           if (a == v and position[b] > position[v])
                           or (b == v and position[a] > position[v])))
    return degrees


def interval_weight(pair, edge_weights):
    a, b = pair
    out = F(1)
    for j in range(a, b):
        out *= edge_weights[j]
    return out


def block_moment(block, edge_weights):
    block = tuple(sorted(block))
    if len(block) % 2:
        return F(0)
    out = F(1)
    for j in range(0, len(block), 2):
        out *= interval_weight((block[j], block[j + 1]), edge_weights)
    return out


def exact_cumulant(n, edge_weights):
    total = F(0)
    for part in all_partitions(n):
        k = len(part)
        product = F(1)
        for block in part:
            product *= block_moment(block, edge_weights)
        total += (-1) ** (k - 1) * factorial(k - 1) * product
    return total


def matching_resummation(n, edge_weights):
    total = F(0)
    coefficients = {}
    for matching in perfect_matchings(range(n)):
        intervals, edges = overlap_graph(matching)
        coefficient = chromatic_linear_coefficient(len(intervals), edges)
        product = F(1)
        for pair in matching:
            product *= interval_weight(pair, edge_weights)
        coefficients[matching] = (coefficient, product)
        total += coefficient * product
    return total, coefficients


def verify_exact_resummation():
    for n in (2, 4, 6, 8):
        weights = [F(2 + (j % 3), 5 + (j % 3)) for j in range(n - 1)]
        direct = exact_cumulant(n, weights)
        resummed, coefficients = matching_resummation(n, weights)
        assert direct == resummed, (n, direct, resummed)

        for matching, (coefficient, _product) in coefficients.items():
            intervals, edges = overlap_graph(matching)
            degrees = peo_later_degrees(intervals, edges)
            peo_coefficient = (-1) ** (len(intervals) - 1)
            for degree in degrees:
                peo_coefficient *= degree
            assert coefficient == peo_coefficient, (n, matching, coefficient, peo_coefficient)


def verify_four_port_formula():
    r1, r2, r3 = F(2, 5), F(3, 7), F(4, 9)
    weights = [r1, r2, r3]
    direct = exact_cumulant(4, weights)
    assert direct == -2 * r1 * r2**2 * r3

    resummed, coeffs = matching_resummation(4, weights)
    assert resummed == direct
    connected = [(m, c) for m, (c, _w) in coeffs.items() if c]
    assert len(connected) == 2
    assert all(c == -1 for _m, c in connected)
    assert coeffs[((0, 1), (2, 3))][0] == 0


def verify_connected_weight_and_global_coefficient_bound():
    for n in (2, 4, 6, 8, 10):
        weights = [F(1, j + 2) for j in range(n - 1)]
        path_weight = F(1)
        for w in weights:
            path_weight *= w

        coefficient_sum = 0
        for matching in perfect_matchings(range(n)):
            intervals, edges = overlap_graph(matching)
            coefficient = chromatic_linear_coefficient(len(intervals), edges)
            if coefficient:
                interval_product = F(1)
                covered = set()
                for a, b in matching:
                    interval_product *= interval_weight((a, b), weights)
                    covered.update(range(a, b))
                assert covered == set(range(n - 1))
                assert interval_product <= path_weight
                coefficient_sum += abs(coefficient)

        assert coefficient_sum <= 4**n * n**(n - 2), (n, coefficient_sum)


def main():
    verify_exact_resummation()
    verify_four_port_formula()
    verify_connected_weight_and_global_coefficient_bound()
    print("PASS exact matching/chromatic resummation (R=2,4,6,8)")
    print("PASS four-port overlapping/nested interval coefficients")
    print("PASS connected interval coverage and temporal path majorant (R<=10)")
    print("PASS coefficient sum <= 4^R R^(R-2) on tested even arities")


if __name__ == "__main__":
    main()
