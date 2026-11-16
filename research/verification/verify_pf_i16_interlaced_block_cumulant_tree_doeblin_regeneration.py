#!/usr/bin/env python3
"""Exact finite regressions for the Doeblin-regeneration block-cumulant proof.

The analytic theorem is in the companion audit. This script checks:
(1) the partition-lattice/chromatic-polynomial cancellation identity;
(2) the conditional replica cancellation for an interlaced A={0,2}, B={1},
    C={3} port pattern in a finite refresh chain, for every +/-1 row
    function and several nontrivial reset probabilities.
"""
from fractions import Fraction
from itertools import product
import math


def partitions(items):
    items = tuple(items)
    if not items:
        yield tuple()
        return
    first = items[0]
    for tail in partitions(items[1:]):
        yield ((first,),) + tail
        for j in range(len(tail)):
            merged = tuple(sorted(tail[j] + (first,)))
            yield tail[:j] + (merged,) + tail[j + 1:]


def canon(part):
    return tuple(sorted((tuple(sorted(block)) for block in part), key=lambda b: b[0]))


def all_partitions(items):
    seen = set()
    for part in partitions(items):
        normalized = canon(part)
        if normalized not in seen:
            seen.add(normalized)
            yield normalized


def mobius(part):
    k = len(part)
    return (-1) ** (k - 1) * math.factorial(k - 1)


def verify_partition_mobius_identity(max_q=5):
    for q in range(2, max_q + 1):
        universe = tuple(range(q))
        global_parts = list(all_partitions(universe))
        for components in all_partitions(universe):
            if len(components) == 1:
                continue
            choices = [list(all_partitions(component)) for component in components]
            for restrictions in product(*choices):
                total = Fraction(0)
                for pi in global_parts:
                    induced = []
                    for component in components:
                        cset = set(component)
                        induced.append(canon([
                            tuple(x for x in block if x in cset)
                            for block in pi
                            if any(x in cset for x in block)
                        ]))
                    if tuple(induced) == tuple(restrictions):
                        total += mobius(pi)
                assert total == 0, (q, components, restrictions, total)


def moment_for_pattern(pattern, subset_mask, labels, funcs):
    n = len(labels)
    parent = list(range(n))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for k, active in enumerate(pattern):
        if active:
            a, b = find(k), find(k + 1)
            if a != b:
                parent[a] = b

    positions = {
        i: [k for k, label in enumerate(labels) if label == i]
        for i in range(len(funcs))
    }
    subset = [i for i in range(len(funcs)) if (subset_mask >> i) & 1]
    roots = sorted({find(k) for i in subset for k in positions[i]})
    total = Fraction(0)
    for spins in product((-1, 1), repeat=len(roots)):
        assignment = dict(zip(roots, spins))
        value = 1
        for i in subset:
            row_spins = [assignment[find(k)] for k in positions[i]]
            index = 0
            for spin in row_spins:
                index = 2 * index + ((spin + 1) // 2)
            value *= funcs[i][index]
        total += Fraction(value, 2 ** len(roots))
    return total


def verify_replica_cancellation():
    # Interlaced disjoint ports: A={0,2}, B={1}, C={3}.
    labels = (0, 1, 0, 2)
    q = 3
    function_tables = [
        list(product((-1, 1), repeat=4)),
        list(product((-1, 1), repeat=2)),
        list(product((-1, 1), repeat=2)),
    ]
    parts = list(all_partitions(range(q)))
    patterns = list(product((False, True), repeat=len(labels) - 1))

    for f_a in function_tables[0]:
        for f_b in function_tables[1]:
            for f_c in function_tables[2]:
                funcs = (f_a, f_b, f_c)
                moments = {
                    pattern: {
                        mask: moment_for_pattern(pattern, mask, labels, funcs)
                        for mask in range(1, 1 << q)
                    }
                    for pattern in patterns
                }

                for activity in (Fraction(1, 3), Fraction(1, 2), Fraction(2, 3)):
                    grouped_signed = {}
                    for pattern_tuple in product(patterns, repeat=q):
                        union_edges = set()
                        active_count = 0
                        for pattern in pattern_tuple:
                            active_count += sum(pattern)
                            for k, active in enumerate(pattern):
                                if active and labels[k] != labels[k + 1]:
                                    union_edges.add(tuple(sorted((labels[k], labels[k + 1]))))
                        graph = tuple(sorted(union_edges))
                        probability = (
                            activity ** active_count
                            * (1 - activity) ** (q * (len(labels) - 1) - active_count)
                        )

                        signed_partition_sum = Fraction(0)
                        for pi in parts:
                            term = Fraction(1)
                            for replica_slot, block in enumerate(pi):
                                mask = sum(1 << i for i in block)
                                term *= moments[pattern_tuple[replica_slot]][mask]
                            signed_partition_sum += mobius(pi) * term

                        grouped_signed[graph] = (
                            grouped_signed.get(graph, Fraction(0))
                            + probability * signed_partition_sum
                        )

                    for graph, signed_sum in grouped_signed.items():
                        # The only possible row edges are AB and AC.
                        connected = (0, 1) in graph and (0, 2) in graph
                        if not connected:
                            assert signed_sum == 0, (
                                funcs, activity, graph, signed_sum
                            )


def main():
    verify_partition_mobius_identity()
    verify_replica_cancellation()
    print("PASS partition-lattice chromatic derivative cancellation (q<=5)")
    print("PASS exact interlaced replica cancellation for all 256 +/-1 block-function triples")
    print("PASS reset activities 1/3, 1/2, 2/3; overlapping hulls and two-port row")


if __name__ == "__main__":
    main()
