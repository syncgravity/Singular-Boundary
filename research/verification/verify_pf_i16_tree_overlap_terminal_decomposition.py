#!/usr/bin/env python3
"""Test whether tree-overlap sources form a recursively separable terminal block.

For a source (M,tau), the candidate terminal class K_n is defined by
|E(H_M)|=s-1. Since source generation already requires H_M connected, this
is equivalent to H_M being a tree, and tau is then forced.

The test splits the bipartite graph into:
  K_n -> N(K_n), and
  the complement of K_n -> the complement of N(K_n).
If both pieces have saturating matchings, their union makes K_n closed in
the matching-relative exchange digraph. We then check that K_n is strongly
connected and that the full exchange digraph has no other sink SCC.
This is finite evidence for a structural induction, not an all-orders proof.
"""
from array import array
from collections import Counter

from verify_pf_i16_n10_multivalued_pi_exchange_scc import build_rows
from verify_pf_i16_global_alternating_reroute import hopcroft_karp
from verify_pf_i16_source_dependent_leaf_peeling import sources
from verify_pf_i16_local_switch_fractional_transport import overlap_edges


def scc_census(rows, assignment):
    all_targets = sorted({t for row in rows for t in row})
    owner = {t: x for x, t in assignment.items()}
    free = set(all_targets) - set(owner)
    n = len(rows)
    adj = [array("I") for _ in range(n)]
    rev = [array("I") for _ in range(n)]
    for x, row in enumerate(rows):
        for t in row:
            y = owner.get(t)
            if y is not None and y != x:
                adj[x].append(y)
                rev[y].append(x)
    seen = bytearray(n)
    order = []
    for root in range(n):
        if seen[root]:
            continue
        seen[root] = 1
        stack = [(root, 0)]
        while stack:
            v, k = stack[-1]
            if k < len(adj[v]):
                w = adj[v][k]
                stack[-1] = (v, k + 1)
                if not seen[w]:
                    seen[w] = 1
                    stack.append((w, 0))
            else:
                order.append(v)
                stack.pop()
    comp = [-1] * n
    groups = []
    for root in reversed(order):
        if comp[root] >= 0:
            continue
        cid = len(groups)
        group = []
        comp[root] = cid
        stack = [root]
        while stack:
            v = stack.pop()
            group.append(v)
            for w in rev[v]:
                if comp[w] < 0:
                    comp[w] = cid
                    stack.append(w)
        groups.append(group)
    outgoing = [set() for _ in groups]
    free_count = [set() for _ in groups]
    for x, row in enumerate(rows):
        cx = comp[x]
        for t in row:
            y = owner.get(t)
            if y is None:
                free_count[cx].add(t)
            elif comp[y] != cx:
                outgoing[cx].add(comp[y])
    sinks = [i for i, out in enumerate(outgoing) if not out]
    return comp, groups, sinks, [len(free_count[i]) for i in sinks]


def run(n):
    rows, _, _ = build_rows(n)
    src = list(sources(n))
    assert len(rows) == len(src)
    s = n // 2
    K = [i for i, (intervals, tau) in enumerate(src)
         if len(overlap_edges(intervals)) == s - 1]
    outside = [i for i in range(len(rows)) if i not in set(K)]
    assert len(K) == 2 ** (s - 1), (n, len(K), 2 ** (s - 1))
    assert all(len(overlap_edges(src[i][0])) == s - 1 for i in K)

    K_targets = set().union(*(rows[i] for i in K))
    all_targets = set().union(*rows)
    k_rows = [rows[i] for i in K]
    o_rows = [rows[i] - K_targets for i in outside]
    mk, rk, right_k = hopcroft_karp(k_rows)
    mo, ro, right_o = hopcroft_karp(o_rows)
    k_size = sum(v >= 0 for v in mk)
    o_size = sum(v >= 0 for v in mo)
    print(f"n={n}: sources={len(rows)} K_tree_overlap={len(K)} "
          f"targets={len(all_targets)} K_target_union={len(K_targets)}")
    print(f"  K_matching={k_size}/{len(K)} "
          f"outside_avoiding_K_neighborhood={o_size}/{len(outside)}")
    if k_size != len(K) or o_size != len(outside):
        print("  RESULT: separable matching decomposition failed at this order")
        return False

    assignment = {}
    for j, x in enumerate(K):
        assignment[x] = right_k[mk[j]]
    for j, x in enumerate(outside):
        assignment[x] = right_o[mo[j]]
    assert len(set(assignment.values())) == len(rows)
    assert all(assignment[x] in rows[x] for x in range(len(rows)))
    assert all(assignment[x] not in K_targets for x in outside)
    comp, groups, sinks, sink_free = scc_census(rows, assignment)
    k_components = {comp[x] for x in K}
    sink_sizes = [len(groups[i]) for i in sinks]
    print(f"  full_scc_count={len(groups)} sink_sizes={sink_sizes} "
          f"sink_free_target_counts={sink_free}")
    print(f"  K_scc_count={len(k_components)} "
          f"K_is_unique_sink={len(sinks)==1 and set(groups[sinks[0]])==set(K)}")
    assert len(k_components) == 1
    assert len(sinks) == 1 and set(groups[sinks[0]]) == set(K)
    assert sink_free[0] > 0
    print("  RESULT: tree-overlap class is a closed, strongly connected, "
          "free-target terminal SCC under the constructed finite matching")
    return True


if __name__ == "__main__":
    for order in (4, 6, 8):
        assert run(order)
