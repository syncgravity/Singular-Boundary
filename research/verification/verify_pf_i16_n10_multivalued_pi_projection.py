#!/usr/bin/env python3
"""Test a multivalued pi-parent intermediate relation at n=10.

For a child source x=(M,tau), allow every non-root leaf ell of tau as the
peeled interval. For each ell, form pi_ell(x) by deleting that interval.
A child output T is retained if it is realizable with ell inserted last and
its inverse final-switch projection lies in the CANONICAL leaf-last
neighborhood of pi_ell(x). Thus pi is a relation, not one canonical map.
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
    child_data = []
    parent_targets = {}
    parent_set_by_child_leaf = []
    leaf_counts = []
    fibers = defaultdict(set)

    for idx, (intervals, tau) in enumerate(sources(10)):
        leaves = nonroot_leaves(intervals, tau)
        assert leaves
        child_data.append((intervals, tau, leaves))
        leaf_counts.append(len(leaves))
        per_leaf = []
        for ell in leaves:
            parent = parent_data(intervals, tau, ell)
            per_leaf.append((ell, parent))
            fibers[parent].add(idx)
            if parent not in parent_targets:
                pi, pt = parent
                pl = canonical_leaf(pi, pt)
                parent_targets[parent] = candidate_outputs(pi, pt, forced_last=pl)
        parent_set_by_child_leaf.append(per_leaf)
        if (idx + 1) % 2000 == 0:
            print(f"  prepared_child_sources={idx+1} distinct_pi_parents={len(parent_targets)}", flush=True)

    rows = []
    total = retained_incidence_pairs = 0
    for idx, (intervals, tau, leaves) in enumerate(child_data):
        retained = set()
        for ell, parent in parent_set_by_child_leaf[idx]:
            J = intervals[ell]
            allowed = parent_targets[parent]
            outputs = candidate_outputs(intervals, tau, forced_last=ell)
            total += len(outputs)
            for T in outputs:
                inv = inverse_last_switch(T, J, 10)
                assert len(inv) == 1, (idx, ell, T, inv)
                P = compress_tree(next(iter(inv)), set(J), 10)
                if P in allowed:
                    retained.add(encode_tree(T))
        retained_incidence_pairs += len(retained)
        rows.append(retained)
        if (idx + 1) % 2000 == 0:
            print(f"  child_sources={idx+1} raw_leaf_incidences={total} retained_unique={retained_incidence_pairs}", flush=True)

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
    witness_fibers = Counter()
    for u in reachable_left:
        witness_fibers.update(parent for _, parent in parent_set_by_child_leaf[u])

    print("n10_child_graph_with_multivalued_pi_parent_projection")
    print(f"  child_sources={len(rows)} distinct_pi_parent_sources={len(parent_targets)}")
    print(f"  nonroot_leaf_count_range=[{min(leaf_counts)},{max(leaf_counts)}]")
    print(f"  pi_fiber_size_range=[{min(map(len, fibers.values()))},{max(map(len, fibers.values()))}]")
    print(f"  pi_parent_target_count_range=[{min(map(len, parent_targets.values()))},{max(map(len, parent_targets.values()))}]")
    print(f"  raw_child_leaf_incidences={total}")
    print(f"  retained_unique_child_source_target_incidences={retained_incidence_pairs}")
    print(f"  retained_degree_range=[{min(map(len, rows))},{max(map(len, rows))}]")
    print(f"  retained_degree_zero_sources={sum(not row for row in rows)}")
    print(f"  retained_target_trees={len(right)}")
    print(f"  maximum_matching={matching}/{len(rows)}")
    print(f"  deficiency={len(rows)-matching}")
    print(f"  alternating_hall_witness_sources={len(reachable_left)}")
    print(f"  alternating_hall_witness_neighbors={len(hall_neighbors)}")
    print(f"  alternating_hall_witness_deficiency={deficiency}")
    print("RESULT: multivalued pi-parent relation is Hall-saturating." if matching == len(rows)
          else "RESULT: multivalued pi-parent relation is not Hall-saturating.")


if __name__ == "__main__":
    run()
