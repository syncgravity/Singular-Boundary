#!/usr/bin/env python3
"""Exact finite checks for the global occurrence-level regeneration tree audit.

This is a regression for the finite combinatorial ingredients, not a proof of
the analytic Doeblin decomposition or the full stochastic theorem.
"""
from fractions import Fraction
from itertools import combinations, product
from math import factorial


def partitions(items):
    items = tuple(items)
    if not items:
        yield ()
        return
    first = items[0]
    for tail in partitions(items[1:]):
        yield ((first,),) + tail
        for j in range(len(tail)):
            merged = tuple(sorted(tail[j] + (first,)))
            yield tail[:j] + (merged,) + tail[j + 1:]


def canon(part):
    return tuple(sorted((tuple(sorted(b)) for b in part), key=lambda b: b[0]))


def all_partitions(items):
    return sorted({canon(p) for p in partitions(items)})


def mobius(part):
    k = len(part)
    return (-1) ** (k - 1) * factorial(k - 1)


def restriction(part, component):
    c = set(component)
    return canon([
        tuple(x for x in block if x in c)
        for block in part if any(x in c for x in block)
    ])


def verify_disconnected_partition_cancellation(max_q=5):
    for q in range(2, max_q + 1):
        universe = tuple(range(q))
        global_parts = all_partitions(universe)
        for components in all_partitions(universe):
            if len(components) < 2:
                continue
            local_choices = [all_partitions(c) for c in components]
            for restrictions in product(*local_choices):
                total = 0
                for pi in global_parts:
                    if tuple(restriction(pi, c) for c in components) == restrictions:
                        total += mobius(pi)
                assert total == 0, (q, components, restrictions, total)


def connected(n, edges):
    if n <= 1:
        return True
    seen = {0}
    changed = True
    while changed:
        changed = False
        for i, j in edges:
            if i in seen and j not in seen:
                seen.add(j)
                changed = True
            elif j in seen and i not in seen:
                seen.add(i)
                changed = True
    return len(seen) == n


def verify_independent_edge_tree_union_bound():
    # Exhaust all rational edge probabilities on 3- and 4-vertex graphs.
    for n in (3, 4):
        pairs = list(combinations(range(n), 2))
        for probs in product((Fraction(0), Fraction(1, 3), Fraction(2, 3)), repeat=len(pairs)):
            p = dict(zip(pairs, probs))
            exact_connected = Fraction(0)
            for mask in range(1 << len(pairs)):
                chosen = [pairs[k] for k in range(len(pairs)) if (mask >> k) & 1]
                weight = Fraction(1)
                chosen_set = set(chosen)
                for edge in pairs:
                    weight *= p[edge] if edge in chosen_set else (1 - p[edge])
                if connected(n, chosen):
                    exact_connected += weight
            tree_sum = Fraction(0)
            for tree_edges in combinations(pairs, n - 1):
                if connected(n, tree_edges):
                    term = Fraction(1)
                    for edge in tree_edges:
                        term *= p[edge]
                    tree_sum += term
            assert exact_connected <= tree_sum, (n, p, exact_connected, tree_sum)


def verify_link_incidence_activity_bound():
    # For a fixed pair, at most m shared link-gap indicators, each with
    # activity <= C0*w; R replicas give an OR bound <= m*R*C0*w.
    for m in range(1, 9):
        for replicas in range(1, 7):
            for c0 in (Fraction(1, 4), Fraction(1, 2), Fraction(1)):
                for w in (Fraction(1, 8), Fraction(1, 4), Fraction(1, 2)):
                    activity = min(Fraction(1), c0 * w)
                    exact_or = 1 - (1 - activity) ** (m * replicas)
                    union_bound = m * replicas * c0 * w
                    assert exact_or <= union_bound


def main():
    verify_disconnected_partition_cancellation()
    verify_independent_edge_tree_union_bound()
    verify_link_incidence_activity_bound()
    print("PASS partition-Mobius cancellation for all disconnected restrictions (q<=5)")
    print("PASS exact independent-edge connectivity <= spanning-tree union bound (q=3,4)")
    print("PASS link/replica OR activity <= m*R*C0*temporal weight (m<=8, R<=6)")


if __name__ == "__main__":
    main()
