#!/usr/bin/env python3
"""Exact n=10 child / n=8 parent projection comparison.

Builds the complete n=10 leaf-last graph, obtains a left-saturating matching,
then projects each matched child tree through the unique inverse final switch.
It compares parent-source fibers, parent target neighborhoods, and the
multiplicity with which the child matching uses each (parent source,parent
target) pair. This is a diagnostic comparison, not a recursive Hall proof.
"""
from collections import Counter, defaultdict
from verify_pf_i16_source_dependent_leaf_peeling import (
    sources, canonical_leaf, parent_data, inverse_last_switch, compress_tree,
)
from verify_pf_i16_local_switch_fractional_transport import candidate_outputs
from verify_pf_i16_full_leaf_last_graph_n10 import encode_tree
from verify_pf_i16_global_alternating_reroute import hopcroft_karp


def run():
    rows = []
    tree_by_mask = []
    child_sources = []
    parent_of = []
    parent_cache = {}
    fibers = defaultdict(list)

    for idx, (intervals, tau) in enumerate(sources(10)):
        leaf = canonical_leaf(intervals, tau)
        J = intervals[leaf]
        parent = parent_data(intervals, tau, leaf)
        parent_of.append(parent)
        parent_cache.setdefault(parent, None)
        child_sources.append((intervals, tau, J))
        fibers[parent].append(idx)

        trees = candidate_outputs(intervals, tau, forced_last=leaf)
        encoded = {encode_tree(T): T for T in trees}
        assert len(encoded) == len(trees)
        rows.append(set(encoded))
        tree_by_mask.append(encoded)
        if (idx + 1) % 2000 == 0:
            print(f"  built_child_sources={idx+1}", flush=True)

    for parent in parent_cache:
        pi, pt = parent
        parent_cache[parent] = candidate_outputs(pi, pt)

    ml, mr, right = hopcroft_karp(rows)
    assert all(v >= 0 for v in ml), "n=10 child graph not left-saturated"
    right_masks = right
    assert len(right_masks) == len(set(right_masks))

    projected_load = Counter()
    projected_by_fiber = defaultdict(set)
    invalid_projection = []
    child_projection_degree = Counter()
    for i, j in enumerate(ml):
        mask = right_masks[j]
        T = tree_by_mask[i][mask]
        intervals, tau, J = child_sources[i]
        projections = inverse_last_switch(T, J, 10)
        assert len(projections) == 1, (i, T, projections)
        P = next(iter(projections))
        pT = compress_tree(P, set(J), 10)
        parent = parent_of[i]
        if pT not in parent_cache[parent]:
            invalid_projection.append((i, parent, pT))
        projected_load[(parent, pT)] += 1
        projected_by_fiber[parent].add(pT)
        child_projection_degree[len(parent_cache[parent]) - len(parent_cache[parent] - {pT})] += 1

    fiber_sizes = [len(v) for v in fibers.values()]
    parent_degrees = [len(parent_cache[p]) for p in fibers]
    used_parent_targets = [len(projected_by_fiber[p]) for p in fibers]
    pair_loads = list(projected_load.values())

    # The parent graph is the exact n=8 source-to-port-tree relation.
    parent_rows = [parent_cache[p] for p in fibers]
    pm, pmr, pright = hopcroft_karp(parent_rows)
    parent_match_size = sum(v >= 0 for v in pm)

    print("n10_child_to_n8_parent_comparison")
    print(f"  child_sources={len(rows)} parent_sources={len(fibers)}")
    print(f"  parent_fiber_size_range=[{min(fiber_sizes)},{max(fiber_sizes)}]")
    print(f"  parent_neighborhood_degree_range=[{min(parent_degrees)},{max(parent_degrees)}]")
    print(f"  parent_graph_targets={len(pright)} parent_graph_incidences={sum(map(len,parent_rows))}")
    print(f"  parent_graph_matching={parent_match_size}/{len(parent_rows)}")
    print(f"  child_graph_matching={sum(v>=0 for v in ml)}/{len(rows)}")
    print(f"  matched_child_projection_failures={len(invalid_projection)}")
    print(f"  parent_targets_used_per_fiber_range=[{min(used_parent_targets)},{max(used_parent_targets)}]")
    print(f"  fibers_using_every_parent_target={sum(used==deg for used,deg in zip(used_parent_targets,parent_degrees))}")
    print(f"  distinct_parent_source_target_pairs_used={len(projected_load)}")
    print(f"  child_matching_parent_pair_multiplicity_range=[{min(pair_loads)},{max(pair_loads)}]")
    print(f"  parent_pair_load_histogram={dict(sorted(Counter(pair_loads).items()))}")
    print(f"  fibers_with_repeated_parent_target_projection={sum(1 for p in fibers if any(k[0]==p and v>1 for k,v in projected_load.items()))}")
    print(f"  max_parent_target_reuse_in_one_fiber={max(pair_loads)}")
    assert not invalid_projection
    assert parent_match_size == len(parent_rows)
    print("PASS: every matched child tree projects to an admissible n=8 parent tree.")


if __name__ == "__main__":
    run()
