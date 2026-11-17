#!/usr/bin/env python3
"""Test a pi-stable intermediate parent relation for PF-I16.

For each n=8 parent pi=(M',tau'), take the UNION of its leaf-last
neighborhoods over every non-root leaf of tau', rather than selecting only
the canonical leaf. Retain an n=10 child target iff its inverse final-switch
projection lies in this union. Then test exact Hall saturation.
"""
from collections import Counter, defaultdict, deque
from verify_pf_i16_source_dependent_leaf_peeling import (
    sources, canonical_leaf, parent_data, inverse_last_switch, compress_tree,
)
from verify_pf_i16_local_switch_fractional_transport import candidate_outputs
from verify_pf_i16_full_leaf_last_graph_n10 import encode_tree
from verify_pf_i16_global_alternating_reroute import hopcroft_karp


def nonroot_leaves(intervals, tau):
    degree = [0] * len(intervals)
    for a, b in tau:
        degree[a] += 1
        degree[b] += 1
    root = next(i for i, I in enumerate(intervals) if I[0] == 1)
    return [i for i, d in enumerate(degree) if d == 1 and i != root]


def run():
    parent_targets = {}
    canonical_targets = {}
    parent_leaf_counts = {}
    rows = []
    parent_of = []
    degrees = []
    total = rejected = 0
    fibers = defaultdict(list)

    for idx, (intervals, tau) in enumerate(sources(10)):
        leaf = canonical_leaf(intervals, tau)
        parent = parent_data(intervals, tau, leaf)
        parent_of.append(parent)
        fibers[parent].append(idx)
        if parent not in parent_targets:
            pi, pt = parent
            canonical_leaf_index = canonical_leaf(pi, pt)
            canonical_targets[parent] = candidate_outputs(
                pi, pt, forced_last=canonical_leaf_index
            )
            leaves = nonroot_leaves(pi, pt)
            assert leaves
            parent_leaf_counts[parent] = len(leaves)
            union = set()
            for ell in leaves:
                union.update(candidate_outputs(pi, pt, forced_last=ell))
            parent_targets[parent] = union

    for idx, (intervals, tau) in enumerate(sources(10)):
        leaf = canonical_leaf(intervals, tau)
        J = intervals[leaf]
        parent = parent_of[idx]
        allowed = parent_targets[parent]
        kept = set()
        outputs = candidate_outputs(intervals, tau, forced_last=leaf)
        total += len(outputs)
        for T in outputs:
            inv = inverse_last_switch(T, J, 10)
            assert len(inv) == 1, (idx, T, inv)
            P = compress_tree(next(iter(inv)), set(J), 10)
            if P in allowed:
                kept.add(encode_tree(T))
            else:
                rejected += 1
        rows.append(kept)
        degrees.append(len(kept))
        if (idx + 1) % 2000 == 0:
            print(f"  child_sources={idx+1} total={total} retained={sum(degrees)}", flush=True)

    ml, mr, right = hopcroft_karp(rows)
    matching = sum(v >= 0 for v in ml)

    right_index = {t: j for j, t in enumerate(right)}
    adj = [[right_index[t] for t in sorted(row)] for row in rows]
    reachable_left = {i for i, v in enumerate(ml) if v < 0}
    reachable_right = set()
    queue = deque(("L", i) for i in sorted(reachable_left))
    while queue:
        side, v = queue.popleft()
        if side == "L":
            for w in adj[v]:
                if ml[v] == w:
                    continue
                if w not in reachable_right:
                    reachable_right.add(w)
                    queue.append(("R", w))
        else:
            u = mr[v]
            if u >= 0 and u not in reachable_left:
                reachable_left.add(u)
                queue.append(("L", u))
    hall_neighbors = {w for u in reachable_left for w in adj[u]}
    assert hall_neighbors == reachable_right
    deficiency = len(reachable_left) - len(hall_neighbors)
    assert deficiency == len(rows) - matching

    witness_fibers = Counter(parent_of[u] for u in reachable_left)
    print("n10_child_graph_restricted_to_pi_union_of_parent_leaf_last_neighborhoods")
    print(f"  child_sources={len(rows)} parent_sources={len(fibers)}")
    print(f"  parent_nonroot_leaf_count_range=[{min(parent_leaf_counts.values())},{max(parent_leaf_counts.values())}]")
    print(f"  canonical_parent_target_count_range=[{min(map(len, canonical_targets.values()))},{max(map(len, canonical_targets.values()))}]")
    print(f"  pi_union_parent_target_count_range=[{min(map(len, parent_targets.values()))},{max(map(len, parent_targets.values()))}]")
    print(f"  original_child_incidences={total}")
    print(f"  retained_incidences={sum(degrees)} rejected_incidences={rejected}")
    print(f"  retained_degree_range=[{min(degrees)},{max(degrees)}]")
    print(f"  retained_degree_zero_sources={sum(d == 0 for d in degrees)}")
    print(f"  retained_target_trees={len(right)}")
    print(f"  maximum_matching={matching}/{len(rows)}")
    print(f"  deficiency={len(rows)-matching}")
    print(f"  alternating_hall_witness_sources={len(reachable_left)}")
    print(f"  alternating_hall_witness_neighbors={len(hall_neighbors)}")
    print(f"  alternating_hall_witness_deficiency={deficiency}")
    print(f"  witness_parent_fibers={len(witness_fibers)}")
    if witness_fibers:
        print(f"  witness_fiber_source_count_range=[{min(witness_fibers.values())},{max(witness_fibers.values())}]")
        print(f"  witness_fiber_histogram={dict(sorted(Counter(witness_fibers.values()).items()))}")
    else:
        print("  witness_fiber_source_count_range=empty (no Hall witness; graph is saturated)")
    if matching == len(rows):
        print("PASS: every child source can be matched while its pi-projection is leaf-last for some non-root parent leaf.")
    else:
        print("RESULT: union over all non-root parent leaves is still not Hall-saturating.")


if __name__ == "__main__":
    run()
