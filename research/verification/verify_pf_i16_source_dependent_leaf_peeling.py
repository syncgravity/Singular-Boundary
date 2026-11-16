#!/usr/bin/env python3
"""Leaf-peeling / source-dependent insertion audit for PF-I16.

Each source (M,tau) chooses its lexicographically first leaf interval J.
Delete J to obtain a parent source on n-2 ordered ports. Child switch
histories are then restricted to orders in which J is inserted last.

For every final tree, invert the last local switch in all possible ways:
the four vertices are J's endpoints plus a candidate old-edge endpoint pair;
the induced four-vertex tree must be one of the three guarded local patterns.
After reversing that switch and deleting J, compress labels to obtain a
parent port tree.

The verifier checks:
  (1) every leaf-last child output projects to an output of its parent source;
  (2) for each parent source and each parent target, whether all children in
      that parent fiber can be lifted injectively above that one parent target.

This tests a concrete recursive strengthening. It is not itself a proof of
global Hall: different parent fibers may still produce the same child tree
under different source-dependent deletions.
"""
from collections import defaultdict
from verify_pf_i16_local_switch_fractional_transport import (
    LOCAL_TREES, candidate_outputs, matchings, overlap_edges, spanning_trees,
)


def parent_data(intervals, tau, leaf):
    n = 2 * len(intervals)
    keep = [i for i in range(len(intervals)) if i != leaf]
    remaining_ports = sorted(x for i in keep for x in intervals[i])
    rank = {x: i + 1 for i, x in enumerate(remaining_ports)}
    p_intervals = tuple(sorted(
        tuple(sorted((rank[intervals[i][0]], rank[intervals[i][1]])))
        for i in keep
    ))
    old_to_new = {old: new for new, old in enumerate(keep)}
    p_tau = tuple(sorted(
        tuple(sorted((old_to_new[a], old_to_new[b])))
        for a, b in tau if a != leaf and b != leaf
    ))
    assert len(p_intervals) == n // 2 - 1
    assert len(p_tau) == len(p_intervals) - 1
    return p_intervals, p_tau


def canonical_leaf(intervals, tau):
    degree = [0] * len(intervals)
    for a, b in tau:
        degree[a] += 1
        degree[b] += 1
    leaves = [i for i, d in enumerate(degree) if d == 1]
    return min(leaves, key=lambda i: intervals[i])


def compress_tree(tree, removed):
    remaining = [x for x in range(1, 2 * (len(tree) + 1) + 1)
                 if x not in removed]
    rank = {x: i + 1 for i, x in enumerate(remaining)}
    return tuple(sorted(tuple(sorted((rank[a], rank[b])))
                        for a, b in tree
                        if a not in removed and b not in removed))


def inverse_last_switch(tree, J, n):
    a, b = J
    result = set()
    for u in range(1, n + 1):
        if u in J:
            continue
        for v in range(u + 1, n + 1):
            if v in J:
                continue
            xs = sorted((a, b, u, v))
            induced = tuple(sorted(e for e in tree
                                   if e[0] in xs and e[1] in xs))
            for local in LOCAL_TREES:
                mapped = tuple(sorted(
                    tuple(sorted((xs[i], xs[j]))) for i, j in local
                ))
                if induced != mapped:
                    continue
                parent = set(tree) - set(mapped)
                parent.add(tuple(sorted((u, v))))
                if len(parent) != n - 1:
                    continue
                if any(x in J for edge in parent for x in edge):
                    continue
                result.add(tuple(sorted(parent)))
    return result


def hopcroft_karp_size(rows):
    right = {t: i for i, t in enumerate(sorted({x for row in rows for x in row}))}
    adj = [[right[x] for x in row] for row in rows]
    nl, nr = len(adj), len(right)
    ml, mr = [-1] * nl, [-1] * nr
    from collections import deque
    inf = nl + nr + 1
    dist = [inf] * nl

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
    return sum(v >= 0 for v in ml), len(right)


def sources(n):
    for matching in matchings(range(1, n + 1)):
        intervals = tuple(sorted(tuple(sorted(e)) for e in matching))
        ov = overlap_edges(intervals)
        for tau in spanning_trees(len(intervals), ov):
            yield intervals, tau


def run(n, expected):
    parent_cache = {}
    fibers = defaultdict(list)
    child_rows = {}
    projection_rows = {}
    child_count = 0
    inverse_count = 0

    for intervals, tau in sources(n):
        leaf = canonical_leaf(intervals, tau)
        J = intervals[leaf]
        p = parent_data(intervals, tau, leaf)
        parent_cache.setdefault(p, None)
        outputs = candidate_outputs(intervals, tau, forced_last=leaf)
        assert outputs, (n, intervals, tau, leaf)
        projections = {}
        for T in outputs:
            inv = inverse_last_switch(T, J, n)
            assert inv, ("no inverse for leaf-last output", n, intervals, tau, J, T)
            compressed = set()
            for P in inv:
                compressed.add(compress_tree(P, set(J)))
            projections[T] = compressed
            inverse_count += len(compressed)
        child = (intervals, tau)
        fibers[p].append(child)
        child_rows[child] = outputs
        projection_rows[child] = projections
        child_count += 1

    # Enumerate parent neighborhoods once, then verify exact projection closure.
    for p in list(parent_cache):
        pi, pt = p
        parent_cache[p] = candidate_outputs(pi, pt)
    closure_failures = []
    for p, children in fibers.items():
        parent_targets = parent_cache[p]
        for child in children:
            for T, projected in projection_rows[child].items():
                if not projected.intersection(parent_targets):
                    closure_failures.append((p, child, T, projected))
                    break

    robust_total = 0
    parent_summary = []
    worst = None
    for p, children in fibers.items():
        robust = 0
        for parent_T in parent_cache[p]:
            rows = [
                {T for T, projections in projection_rows[ch].items()
                 if parent_T in projections}
                for ch in children
            ]
            size, union = hopcroft_karp_size(rows)
            if size == len(children):
                robust += 1
        robust_total += robust
        parent_summary.append((len(children), robust, len(parent_cache[p])))
        if robust == 0 and (worst is None or len(children) > worst[0]):
            worst = (len(children), p, len(parent_cache[p]))

    print(f"n={n}: child_sources={child_count}, parent_fibers={len(fibers)}, "
          f"leaf_last_inverse_candidates={inverse_count}, "
          f"projection_closure_failures={len(closure_failures)}")
    print(f"  fiber_size_range=[{min(x[0] for x in parent_summary)},"
          f"{max(x[0] for x in parent_summary)}], "
          f"parent_targets_with_full_fiber_lift={robust_total}")
    zero = sum(1 for x in parent_summary if x[1] == 0)
    print(f"  fibers_with_no_single_parent_target_supporting_all_children={zero}")
    if worst:
        print(f"  largest_zero_robust_fiber_size={worst[0]}, parent={worst[1]}")
    assert child_count == expected
    if closure_failures:
        print(f"  first_projection_failure={closure_failures[0]}")
        raise SystemExit("Leaf-last projection closure failed.")


def main():
    run(4, 2)
    run(6, 22)
    run(8, 608)
    print("Leaf-peeling recursive diagnostic complete; no global Hall theorem claimed.")


if __name__ == "__main__":
    main()
