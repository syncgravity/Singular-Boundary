#!/usr/bin/env python3
"""Test whether n=10 child matching can be restricted to leaf-last parent projections.

For each child source, enumerate its complete leaf-last target neighborhood.
Keep a child target only when its unique inverse final switch belongs to the
canonical leaf-last neighborhood of that child's n=8 parent. Then test Hall
saturation of this stricter child graph exactly.
"""
from collections import defaultdict
from verify_pf_i16_source_dependent_leaf_peeling import (
    sources, canonical_leaf, parent_data, inverse_last_switch, compress_tree,
)
from verify_pf_i16_local_switch_fractional_transport import candidate_outputs
from verify_pf_i16_full_leaf_last_graph_n10 import encode_tree
from verify_pf_i16_global_alternating_reroute import hopcroft_karp


def run():
    parents = {}
    rows = []
    parent_of = []
    kept_degrees = []
    rejected = 0
    total = 0
    child_count = 0
    fibers = defaultdict(list)

    # Cache each parent's canonical leaf-last neighborhood.
    for intervals, tau in sources(10):
        leaf = canonical_leaf(intervals, tau)
        parent = parent_data(intervals, tau, leaf)
        parent_of.append(parent)
        fibers[parent].append(child_count)
        child_count += 1
        if parent not in parents:
            pi, pt = parent
            pl = canonical_leaf(pi, pt)
            parents[parent] = candidate_outputs(pi, pt, forced_last=pl)

    # Re-enumerate in the same deterministic source order and filter every
    # child incidence by its inverse projection.
    for idx, (intervals, tau) in enumerate(sources(10)):
        leaf = canonical_leaf(intervals, tau)
        J = intervals[leaf]
        parent = parent_of[idx]
        parent_targets = parents[parent]
        kept = set()
        outputs = candidate_outputs(intervals, tau, forced_last=leaf)
        total += len(outputs)
        for T in outputs:
            inv = inverse_last_switch(T, J, 10)
            assert len(inv) == 1, (idx, T, inv)
            P = compress_tree(next(iter(inv)), set(J), 10)
            if P in parent_targets:
                kept.add(encode_tree(T))
            else:
                rejected += 1
        rows.append(kept)
        kept_degrees.append(len(kept))
        if (idx + 1) % 2000 == 0:
            print(f"  filtered_child_sources={idx+1} incidences={total} kept={sum(kept_degrees)}", flush=True)

    ml, mr, right = hopcroft_karp(rows)
    matching = sum(v >= 0 for v in ml)
    print("n10_child_graph_restricted_to_canonical_n8_parent_leaf_last")
    print(f"  child_sources={len(rows)} parent_sources={len(fibers)}")
    print(f"  original_child_incidences={total}")
    print(f"  retained_incidences={sum(kept_degrees)} rejected_incidences={rejected}")
    print(f"  retained_degree_range=[{min(kept_degrees)},{max(kept_degrees)}]")
    print(f"  retained_degree_zero_sources={sum(d==0 for d in kept_degrees)}")
    print(f"  retained_target_trees={len(right)}")
    print(f"  maximum_matching={matching}/{len(rows)}")
    print(f"  deficiency={len(rows)-matching}")
    if matching == len(rows):
        print("PASS: a child matching exists with every projection in the canonical parent leaf-last graph.")
    else:
        print("RESULT: canonical leaf-last projection restriction is not Hall-saturating.")

if __name__ == "__main__":
    run()
