#!/usr/bin/env python3
"""Exact n=10 child / n=8 parent projection comparison.

Build the complete n=10 leaf-last graph and a saturating matching. Project
matched child trees through the unique inverse final switch. Compare each
projection against BOTH the full all-orders parent neighborhood and the
parent's own canonical leaf-last neighborhood. These are distinct relations.
"""
from collections import Counter, defaultdict
from verify_pf_i16_source_dependent_leaf_peeling import (
    sources, canonical_leaf, parent_data, inverse_last_switch, compress_tree,
)
from verify_pf_i16_local_switch_fractional_transport import candidate_outputs
from verify_pf_i16_full_leaf_last_graph_n10 import encode_tree
from verify_pf_i16_global_alternating_reroute import hopcroft_karp


def run():
    rows, tree_by_mask, child_sources, parent_of = [], [], [], []
    parent_full, parent_leaf_last = {}, {}
    fibers = defaultdict(list)

    for idx, (intervals, tau) in enumerate(sources(10)):
        leaf = canonical_leaf(intervals, tau)
        J = intervals[leaf]
        parent = parent_data(intervals, tau, leaf)
        parent_of.append(parent)
        fibers[parent].append(idx)
        child_sources.append((intervals, tau, J))
        trees = candidate_outputs(intervals, tau, forced_last=leaf)
        encoded = {encode_tree(T): T for T in trees}
        assert len(encoded) == len(trees)
        rows.append(set(encoded))
        tree_by_mask.append(encoded)
        if (idx + 1) % 2000 == 0:
            print(f"  built_child_sources={idx+1}", flush=True)

    for parent in fibers:
        pi, pt = parent
        parent_full[parent] = candidate_outputs(pi, pt)
        parent_leaf = canonical_leaf(pi, pt)
        parent_leaf_last[parent] = candidate_outputs(pi, pt, forced_last=parent_leaf)

    ml, mr, right = hopcroft_karp(rows)
    assert all(v >= 0 for v in ml), "n=10 child graph not left-saturated"
    assert len(right) == len(set(right))

    projected_load = Counter()
    projected_by_fiber = defaultdict(set)
    invalid_full, invalid_leaf_last = [], []
    for i, j in enumerate(ml):
        T = tree_by_mask[i][right[j]]
        intervals, tau, J = child_sources[i]
        projections = inverse_last_switch(T, J, 10)
        assert len(projections) == 1, (i, T, projections)
        P = next(iter(projections))
        pT = compress_tree(P, set(J), 10)
        parent = parent_of[i]
        if pT not in parent_full[parent]:
            invalid_full.append((i, parent, pT))
        if pT not in parent_leaf_last[parent]:
            invalid_leaf_last.append((i, parent, pT))
        projected_load[(parent, pT)] += 1
        projected_by_fiber[parent].add(pT)

    fiber_sizes = [len(v) for v in fibers.values()]
    pair_loads = list(projected_load.values())

    def summarize(label, neighborhoods):
        degrees = [len(neighborhoods[p]) for p in fibers]
        used = [len(projected_by_fiber[p] & neighborhoods[p]) for p in fibers]
        graph_rows = [neighborhoods[p] for p in fibers]
        pm, pmr, pright = hopcroft_karp(graph_rows)
        matching = sum(v >= 0 for v in pm)
        print(f"  {label}_degree_range=[{min(degrees)},{max(degrees)}]")
        print(f"  {label}_targets={len(pright)} {label}_incidences={sum(map(len,graph_rows))}")
        print(f"  {label}_matching={matching}/{len(graph_rows)}")
        print(f"  {label}_fiber_projected_target_count_range=[{min(used)},{max(used)}]")
        print(f"  {label}_fibers_using_every_target={sum(u==d for u,d in zip(used,degrees))}")
        return matching

    print("n10_child_to_n8_parent_comparison")
    print(f"  child_sources={len(rows)} parent_sources={len(fibers)}")
    print(f"  parent_fiber_size_range=[{min(fiber_sizes)},{max(fiber_sizes)}]")
    print(f"  child_graph_matching={sum(v>=0 for v in ml)}/{len(rows)}")
    print(f"  matched_child_projection_failures_full={len(invalid_full)}")
    print(f"  matched_child_projection_failures_parent_leaf_last={len(invalid_leaf_last)}")
    full_matching = summarize("parent_full_all_orders", parent_full)
    leaf_matching = summarize("parent_canonical_leaf_last", parent_leaf_last)
    print(f"  distinct_parent_source_target_pairs_used={len(projected_load)}")
    print(f"  child_matching_parent_pair_multiplicity_range=[{min(pair_loads)},{max(pair_loads)}]")
    print(f"  parent_pair_load_histogram={dict(sorted(Counter(pair_loads).items()))}")
    print(f"  fibers_with_repeated_parent_target_projection={sum(1 for p in fibers if any(k[0]==p and v>1 for k,v in projected_load.items()))}")
    print(f"  max_parent_target_reuse_in_one_fiber={max(pair_loads)}")
    assert not invalid_full
    assert full_matching == len(fibers)
    assert sum(v >= 0 for v in ml) == len(rows)
    print("PASS: every matched child tree projects to the full admissible parent neighborhood.")
    if invalid_leaf_last:
        print("NOTE: some projections are outside the restricted parent leaf-last neighborhoods; this is not a contradiction.")
    else:
        print("PASS: every matched child tree also projects to the restricted parent leaf-last neighborhood.")
    print(f"  parent_leaf_last_matching_saturates={leaf_matching == len(fibers)}")


if __name__ == "__main__":
    run()
