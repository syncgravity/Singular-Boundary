#!/usr/bin/env python3
"""Matching-relative digraph diagnostics for PF-I16 leaf-last transport.

For a left-saturating matching mu, form D on source vertices with x->y
whenever x is adjacent to the target mu(y), x != y. Then for every source
set A, Hall slack equals the number of out-neighbor vertices outside A plus
the number of free target neighbors of A. This script measures the digraph
before attempting a global vertex-connectivity proof.
"""
from collections import Counter
from verify_pf_i16_simultaneous_three_edge_flexibility import build_case, hopcroft_karp


def tarjan_scc(adj, banned=frozenset()):
    n = len(adj)
    index = 0
    stack = []
    onstack = [False] * n
    indices = [-1] * n
    low = [0] * n
    comps = []

    def visit(v):
        nonlocal index
        indices[v] = low[v] = index
        index += 1
        stack.append(v)
        onstack[v] = True
        for w in adj[v]:
            if w in banned:
                continue
            if indices[w] < 0:
                visit(w)
                low[v] = min(low[v], low[w])
            elif onstack[w]:
                low[v] = min(low[v], indices[w])
        if low[v] == indices[v]:
            comp = []
            while True:
                w = stack.pop()
                onstack[w] = False
                comp.append(w)
                if w == v:
                    break
            comps.append(comp)

    for v in range(n):
        if v not in banned and indices[v] < 0:
            visit(v)
    return comps


def run(n):
    rows, _, metadata = build_case(n)
    ml, mr, right = hopcroft_karp(rows)
    assert all(x >= 0 for x in ml)
    owner = {right[j]: i for j, i in enumerate(mr) if i >= 0}
    free = set(right) - set(owner)
    adj = []
    free_neighbors = []
    for x, row in enumerate(rows):
        out = {owner[t] for t in row if t in owner and owner[t] != x}
        adj.append(sorted(out))
        free_neighbors.append({t for t in row if t in free})

    indeg = [0] * len(rows)
    for x in range(len(rows)):
        for y in adj[x]:
            indeg[y] += 1
    outdeg = [len(a) for a in adj]
    print(f"n={n}: sources={len(rows)}, target_union={len(right)}, "
          f"free_targets={len(free)}, digraph_arcs={sum(outdeg)}")
    print(f"  outdegree_min={min(outdeg)}, max={max(outdeg)}, "
          f"indegree_min={min(indeg)}, max={max(indeg)}")
    print(f"  free_neighbor_counts={Counter(map(len, free_neighbors))}")
    comps = tarjan_scc(adj)
    print(f"  scc_count={len(comps)}, largest_scc={max(map(len, comps))}, "
          f"smallest_scc={min(map(len, comps))}")
    if len(comps) > 1:
        print(f"  scc_sizes={sorted(map(len, comps))}")
    # Single-vertex deletion robustness is a necessary first test for
    # 2-vertex-strong connectivity and a useful diagnostic for 3-connectivity.
    failures = []
    for v in range(len(rows)):
        cs = tarjan_scc(adj, frozenset((v,)))
        if len(cs) != 1 and len(rows) - 1 > 0:
            failures.append((v, sorted(map(len, cs))))
    print(f"  single_vertex_deletions_strong={len(failures)}/{len(rows)}")
    if failures[:20]:
        print(f"  single_deletion_failures={failures[:20]}")


if __name__ == "__main__":
    run(6)
    run(8)
