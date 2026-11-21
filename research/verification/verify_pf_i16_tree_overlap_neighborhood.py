#!/usr/bin/env python3
"""K-only neighborhood census for the tree-overlap terminal-class conjecture.

Unlike build_rows, this verifier constructs only rows belonging to K_n, so it
can test the conjectural |N(K_n)|=3^(s-1) pattern at n=10 without building the
full 31,744-source graph.
"""
from verify_pf_i16_source_dependent_leaf_peeling import (
    sources, canonical_leaf, parent_data, inverse_last_switch, compress_tree,
)
from verify_pf_i16_n10_multivalued_pi_exchange_scc import nonroot_leaves
from verify_pf_i16_local_switch_fractional_transport import (
    overlap_edges, candidate_outputs,
)
from verify_pf_i16_full_leaf_last_graph_n10 import encode_tree
from verify_pf_i16_global_alternating_reroute import hopcroft_karp


def build_k_rows(n):
    s = n // 2
    parent_targets = {}
    selected_sources = []
    rows = []
    for intervals, tau in sources(n):
        if len(overlap_edges(intervals)) != s - 1:
            continue
        leaves = nonroot_leaves(intervals, tau)
        retained = set()
        for leaf in leaves:
            J = intervals[leaf]
            parent = parent_data(intervals, tau, leaf)
            if parent not in parent_targets:
                pi, pt = parent
                if len(pi) == 1:
                    parent_targets[parent] = {((1, 2),)}
                else:
                    pl = canonical_leaf(pi, pt)
                    parent_targets[parent] = candidate_outputs(
                        pi, pt, forced_last=pl
                    )
            outputs = candidate_outputs(intervals, tau, forced_last=leaf)
            for T in outputs:
                inv = inverse_last_switch(T, J, n)
                assert len(inv) == 1
                P = compress_tree(next(iter(inv)), set(J), n)
                if P in parent_targets[parent]:
                    retained.add(encode_tree(T))
        selected_sources.append((intervals, tau))
        rows.append(retained)
    return selected_sources, rows


def run(n):
    selected, rows = build_k_rows(n)
    ml, mr, right = hopcroft_karp(rows)
    matching = sum(v >= 0 for v in ml)
    s = n // 2
    print(f"n={n}: K_sources={len(rows)} expected={2**(s-1)} "
          f"target_union={len(right)} expected_3pow={3**(s-1)} "
          f"incidences={sum(map(len, rows))}")
    print(f"  degree_range=[{min(map(len, rows))},{max(map(len, rows))}] "
          f"K_matching={matching}/{len(rows)}")
    assert len(rows) == 2 ** (s - 1)
    assert matching == len(rows)
    if n <= 8:
        assert len(right) == 3 ** (s - 1)
    print("  RESULT: K_n is saturable within its own target neighborhood")


if __name__ == "__main__":
    for order in (4, 6, 8, 10):
        run(order)
