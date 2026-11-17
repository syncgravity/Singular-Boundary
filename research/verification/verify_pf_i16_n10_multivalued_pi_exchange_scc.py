#!/usr/bin/env python3
"""Matching-relative SCC test for global edge flexibility in the n=10 multivalued-pi graph.

Given a left-saturating matching mu, form D on left sources:
x -> y iff x has a graph-neighbor equal to mu(y), x != y.
A sink SCC with no neighbor among unmatched right targets is a tight Hall
block. If every sink SCC has a genuinely free right neighbor, every vertex
of D can reach a free target; consequently every nonmatching edge can be
forced into some left-saturating matching by an alternating reroute (unless
the route reaches the challenger's matched target first, giving a cycle).
"""
from collections import Counter, defaultdict
from array import array

from verify_pf_i16_source_dependent_leaf_peeling import (
    sources, parent_data, inverse_last_switch, compress_tree,
)
from verify_pf_i16_local_switch_fractional_transport import candidate_outputs
from verify_pf_i16_global_alternating_reroute import hopcroft_karp
from verify_pf_i16_full_leaf_last_graph_n10 import encode_tree, sink_scc_census


def nonroot_leaves(intervals, tau):
    degree = [0] * len(intervals)
    for a, b in tau:
        degree[a] += 1
        degree[b] += 1
    root = next(i for i, I in enumerate(intervals) if I[0] == 1)
    return [i for i, d in enumerate(degree) if d == 1 and i != root]


def build_rows(n=10):
    parent_targets = {}
    rows = []
    total_leaf_outputs = 0
    for idx, (intervals, tau) in enumerate(sources(n)):
        retained = set()
        for leaf in nonroot_leaves(intervals, tau):
            J = intervals[leaf]
            parent = parent_data(intervals, tau, leaf)
            if parent not in parent_targets:
                pi, pt = parent
                # Canonical parent leaf; the one-interval parent is the base case.
                if len(pi) == 1:
                    parent_targets[parent] = {((1, 2),)}
                else:
                    from verify_pf_i16_source_dependent_leaf_peeling import canonical_leaf
                    pl = canonical_leaf(pi, pt)
                    parent_targets[parent] = candidate_outputs(pi, pt, forced_last=pl)
            allowed = parent_targets[parent]
            outputs = candidate_outputs(intervals, tau, forced_last=leaf)
            total_leaf_outputs += len(outputs)
            for T in outputs:
                inv = inverse_last_switch(T, J, n)
                assert len(inv) == 1
                P = compress_tree(next(iter(inv)), set(J), n)
                if P in allowed:
                    retained.add(encode_tree(T))
        rows.append(retained)
        if (idx + 1) % 2000 == 0:
            print(f"  prepared_sources={idx+1} distinct_parent_sources={len(parent_targets)}",
                  flush=True)
    return rows, total_leaf_outputs, len(parent_targets)


def main():
    rows, raw_leaf_outputs, parent_count = build_rows(10)
    ml, mr, right = hopcroft_karp(rows)
    matching = sum(v >= 0 for v in ml)
    assert matching == len(rows), (matching, len(rows))
    print("n10_multivalued_pi_matching_relative_exchange_scc")
    print(f"  sources={len(rows)}")
    print(f"  parent_sources={parent_count}")
    print(f"  raw_leaf_outputs={raw_leaf_outputs}")
    print(f"  unique_incidences={sum(map(len, rows))}")
    print(f"  target_union={len(right)}")
    print(f"  matching={matching}/{len(rows)}")

    census = sink_scc_census(rows, ml, mr, right)
    zero_free = [item for item in census if item[1] == 0]
    print(f"  zero_free_sink_scc_count={len(zero_free)}")
    print(f"  all_sink_sccs_reach_free_target={not zero_free}")
    if not zero_free:
        print("RESULT: every vertex reaches a free right target; every nonmatching")
        print("        incidence is individually admissible by an alternating reroute.")
    else:
        print("RESULT: at least one closed tight Hall block remains; inspect its incoming edges.")
        raise SystemExit(1)


if __name__ == "__main__":
    main()
