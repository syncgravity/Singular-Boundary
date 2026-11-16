#!/usr/bin/env python3
"""Global alternating-path diagnostic for PF-I16 leaf-last source matching.

Build the exact leaf-last child-source -> port-tree relation and a deterministic
maximum matching. Contract each occupied right vertex to its matched owner.
An unmatched candidate tree is a free endpoint. For a same-parent-fiber
collision at T, let x be the non-owner and y the owner of T. If y has an
alternating path to a free tree, shift the owners along that path, freeing T,
then assign T to x. The test records whether such a path exists and whether
it passes through another parent fiber.

This is a finite rerouting diagnostic, not an all-orders Hall proof.
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


def alternating_path_to_free(start, graph, free_exit):
    """Return source path ending at a source with a free candidate, or None."""
    q = deque([start])
    pred = {start: None}
    end = None
    while q:
        u = q.popleft()
        if free_exit[u]:
            end = u
            break
        for v in graph[u]:
            if v not in pred:
                pred[v] = u
                q.append(v)
    if end is None:
        return None
    path = []
    cur = end
    while cur is not None:
        path.append(cur)
        cur = pred[cur]
    return list(reversed(path))


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

    graph = [set() for _ in children]
    free_exit = [False] * len(children)
    for i, row in enumerate(rows):
        for tree in row:
            owner = mr[right_ids[tree]]
            if owner < 0:
                free_exit[i] = True
            elif owner != i:
                graph[i].add(owner)
    graph = [sorted(x) for x in graph]

    path_cache = {}
    def path_from(owner):
        if owner not in path_cache:
            path_cache[owner] = alternating_path_to_free(owner, graph, free_exit)
        return path_cache[owner]

    all_reachable = sum(path_from(i) is not None for i in range(len(children)))
    collision_pairs = 0
    distinct_projection_pairs = 0
    reroutable_pairs = 0
    cross_fiber_reroutes = 0
    external_owners = 0
    max_path_length = 0
    first_failure = None
    first_cross_path = None

    for parent, members in fibers.items():
        owners = defaultdict(list)
        for i in members:
            for tree in rows[i]:
                owners[tree].append(i)
        for tree, who in owners.items():
            for ai in range(len(who)):
                for bi in range(ai + 1, len(who)):
                    a, b = who[ai], who[bi]
                    collision_pairs += 1
                    if projections[a][tree] == projections[b][tree]:
                        continue
                    distinct_projection_pairs += 1
                    owner = mr[right_ids[tree]]
                    assert owner >= 0
                    if owner not in (a, b):
                        external_owners += 1
                    path = path_from(owner)
                    if path is None:
                        if first_failure is None:
                            first_failure = (parent, tree, a, b, owner)
                        continue
                    reroutable_pairs += 1
                    max_path_length = max(max_path_length, len(path) - 1)
                    crosses = any(parents[v] != parent for v in path)
                    if crosses:
                        cross_fiber_reroutes += 1
                        if first_cross_path is None:
                            first_cross_path = (parent, tree, a, b, path,
                                                [parents[v] for v in path])

    print(
        f"n={n}: sources={expected}, target_union={len(right_ids)}, "
        f"matching={matched}/{expected}, alternating_arcs={sum(map(len, graph))}, "
        f"sources_reaching_free_tree={all_reachable}/{expected}"
    )
    print(
        f"  same_fiber_collision_pairs={collision_pairs}, "
        f"distinct_parent_projection_pairs={distinct_projection_pairs}, "
        f"reroutable_by_alternating_path={reroutable_pairs}, "
        f"reroutes_crossing_parent_fibers={cross_fiber_reroutes}, "
        f"collisions_owned_outside_pair={external_owners}, "
        f"max_reroute_path_length={max_path_length}"
    )
    if first_failure:
        print("  first_unresolved_collision=", first_failure)
    if first_cross_path:
        print("  sample_cross_fiber_reroute=", first_cross_path)
    return {
        "sources": expected, "matching": matched,
        "collision_pairs": collision_pairs,
        "distinct_projection_pairs": distinct_projection_pairs,
        "reroutable": reroutable_pairs,
        "cross_fiber": cross_fiber_reroutes, "external_owners": external_owners,
    }


def main():
    results = [run(4, 2), run(6, 22), run(8, 608)]
    print("Global alternating-path diagnostic complete; no all-orders Hall claim.")
    assert all(r["matching"] == r["sources"] for r in results)


if __name__ == "__main__":
    main()
