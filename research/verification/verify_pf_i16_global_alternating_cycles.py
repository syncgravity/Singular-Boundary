#!/usr/bin/env python3
"""Global alternating-cycle diagnostic for PF-I16 leaf-last source matching.

Build the exact leaf-last child-source -> port-tree relation and a deterministic
maximum matching. Contract each matched right vertex to its owner. Every
unmatched source->target edge then gives a directed arc from that source to
the source currently occupying the target. Directed cycles are precisely
alternating cycles along which the matching can be rerouted without losing
saturation.

The test asks whether same-parent-fiber collision pairs that are disconnected
inside their own parent neighborhood nevertheless lie in a common alternating
strongly connected component, and whether that component uses other parent
fibers. This is a diagnostic of one global rerouting mechanism, not a Hall
proof.
"""
from collections import defaultdict, deque
from verify_pf_i16_source_dependent_leaf_peeling import (
    canonical_leaf, parent_data, inverse_last_switch, compress_tree, sources,
)
from verify_pf_i16_local_switch_fractional_transport import candidate_outputs


def hopcroft_karp(rows):
    right = {t: i for i, t in enumerate(sorted({t for row in rows for t in row}))}
    adj = [[right[t] for t in sorted(row)] for row in rows]
    nl, nr = len(adj), len(right)
    ml, mr = [-1] * nl, [-1] * nr
    dist = [0] * nl
    inf = nl + nr + 1

    def bfs():
        q = deque()
        found = inf
        for u in range(nl):
            if ml[u] < 0:
                dist[u] = 0
                q.append(u)
            else:
                dist[u] = inf
        while q:
            u = q.popleft()
            if dist[u] >= found:
                continue
            for v in adj[u]:
                w = mr[v]
                if w < 0:
                    found = dist[u] + 1
                elif dist[w] == inf:
                    dist[w] = dist[u] + 1
                    q.append(w)
        return found < inf

    def dfs(u):
        for v in adj[u]:
            w = mr[v]
            if w < 0 or (dist[w] == dist[u] + 1 and dfs(w)):
                ml[u], mr[v] = v, u
                return True
        dist[u] = inf
        return False

    while bfs():
        for u in range(nl):
            if ml[u] < 0:
                dfs(u)
    return ml, mr, right


def strongly_connected_components(graph):
    n = len(graph)
    index = 0
    stack, on_stack = [], set()
    indices, low = [-1] * n, [0] * n
    components = []

    def visit(v):
        nonlocal index
        indices[v] = low[v] = index
        index += 1
        stack.append(v)
        on_stack.add(v)
        for w in graph[v]:
            if indices[w] < 0:
                visit(w)
                low[v] = min(low[v], low[w])
            elif w in on_stack:
                low[v] = min(low[v], indices[w])
        if low[v] == indices[v]:
            comp = []
            while True:
                w = stack.pop()
                on_stack.remove(w)
                comp.append(w)
                if w == v:
                    break
            components.append(comp)

    for v in range(n):
        if indices[v] < 0:
            visit(v)
    labels = [-1] * n
    for c, members in enumerate(components):
        for v in members:
            labels[v] = c
    return labels, components


def run(n, expected):
    children, rows, parents, projections = [], [], [], []
    fibers = defaultdict(list)
    for intervals, tau in sources(n):
        leaf = canonical_leaf(intervals, tau)
        J = intervals[leaf]
        parent = parent_data(intervals, tau, leaf)
        out = candidate_outputs(intervals, tau, forced_last=leaf)
        projection = {}
        for T in out:
            inv = inverse_last_switch(T, J, n)
            assert len(inv) == 1
            projection[T] = compress_tree(next(iter(inv)), set(J), n)
        i = len(children)
        child = (intervals, tau)
        children.append(child)
        rows.append(out)
        parents.append(parent)
        projections.append(projection)
        fibers[parent].append(i)

    assert len(children) == expected, (n, len(children), expected)
    ml, mr, right_ids = hopcroft_karp(rows)
    matched = sum(v >= 0 for v in ml)
    assert matched == expected, (n, matched, expected)
    right_values = [None] * len(right_ids)
    for tree, idx in right_ids.items():
        right_values[idx] = tree

    # Directed source graph: i -> owner(t) for every non-matching candidate t.
    graph = [set() for _ in children]
    for i, row in enumerate(rows):
        for tree in row:
            v = right_ids[tree]
            owner = mr[v]
            assert owner >= 0
            if owner != i:
                graph[i].add(owner)
    graph = [sorted(x) for x in graph]
    labels, comps = strongly_connected_components(graph)
    comp_fibers = {
        c: {parents[i] for i in members}
        for c, members in enumerate(comps)
    }
    cyclic_cross = {
        c for c, members in enumerate(comps)
        if (len(members) > 1 or any(i in graph[i] for i in members))
        and len(comp_fibers[c]) > 1
    }

    # Same-fiber shared-target collisions and their alternating SCC status.
    collision_pairs = 0
    same_scc = 0
    cross_fiber_cycle = 0
    local_disconnected_pairs = 0
    collision_examples = []
    for parent, members in fibers.items():
        owners = defaultdict(list)
        for i in members:
            for tree in rows[i]:
                owners[tree].append(i)
        for tree, who in owners.items():
            if len(who) < 2:
                continue
            for a_pos in range(len(who)):
                for b_pos in range(a_pos + 1, len(who)):
                    a, b = who[a_pos], who[b_pos]
                    collision_pairs += 1
                    if labels[a] == labels[b]:
                        same_scc += 1
                        if labels[a] in cyclic_cross:
                            cross_fiber_cycle += 1
                    if projections[a][tree] != projections[b][tree]:
                        local_disconnected_pairs += 1
                        if len(collision_examples) < 3:
                            collision_examples.append(
                                (parent, tree, a, b,
                                 projections[a][tree], projections[b][tree],
                                 labels[a] == labels[b],
                                 labels[a] in cyclic_cross if labels[a] == labels[b] else False)
                            )

    multi = [members for members in comps if len(members) > 1]
    cross_components = [members for c, members in enumerate(comps)
                        if c in cyclic_cross]
    max_scc = max(map(len, comps), default=0)
    print(
        f"n={n}: sources={expected}, target_union={len(right_ids)}, "
        f"matching={matched}/{expected}, alternating_arcs={sum(map(len, graph))}"
    )
    print(
        f"  nontrivial_sccs={len(multi)}, cross_parent_fiber_sccs={len(cross_components)}, "
        f"largest_scc={max_scc}, sources_in_cross_fiber_sccs="
        f"{sum(map(len, cross_components))}"
    )
    print(
        f"  same_fiber_collision_pairs={collision_pairs}, "
        f"collision_pairs_in_same_alternating_scc={same_scc}, "
        f"collision_pairs_in_cross_fiber_scc={cross_fiber_cycle}, "
        f"distinct_parent_projection_collision_pairs={local_disconnected_pairs}"
    )
    if collision_examples:
        print("  sample_projection_collisions=", collision_examples)
    return {
        "sources": expected, "matching": matched,
        "collision_pairs": collision_pairs, "same_scc": same_scc,
        "cross_fiber_cycle": cross_fiber_cycle,
        "local_disconnected": local_disconnected_pairs,
    }


def main():
    results = [run(4, 2), run(6, 22), run(8, 608)]
    print("Global alternating-cycle diagnostic complete; no all-orders Hall claim.")
    assert all(r["matching"] == r["sources"] for r in results)


if __name__ == "__main__":
    main()
