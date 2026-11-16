#!/usr/bin/env python3
"""Canonical-order guarded-switch subrelation and exact source matching.

For each source (M,tau), test a small fixed family of parent-before-child
orders (BFS ascending, BFS descending, DFS ascending). At each insertion take
the first admissible edge on the connected-tree witness path and branch over
all guarded local patterns for that edge. The union is a deliberately small
subrelation of the full guarded switch relation.

Trees are encoded as integer edge bitmasks. A deterministic lexicographic
augmenting-path assignment is computed, and a failed run reports an
alternating-reachability Hall witness. This is finite diagnostic evidence,
not an all-orders theorem.
"""
from collections import deque
from heapq import heappop, heappush
from verify_pf_i16_local_switch_fractional_transport import (
    LOCAL_TREES, load, matchings, overlap_edges, overlaps, spanning_trees,
    tree_path,
)


def edge_ids(n):
    pairs = ((a, b) for a in range(1, n + 1) for b in range(a + 1, n + 1))
    return {(a, b): i for i, (a, b) in enumerate(pairs)}


def encode_tree(edges, ids):
    return sum(1 << ids[tuple(sorted(e))] for e in edges)


def decode_tree(mask, n):
    pairs = [(a, b) for a in range(1, n + 1) for b in range(a + 1, n + 1)]
    return tuple(pairs[i] for i in range(len(pairs)) if (mask >> i) & 1)


def canonical_order(intervals, tau, strategy):
    root = next(i for i, I in enumerate(intervals) if I[0] == 1)
    adj = [[] for _ in intervals]
    for a, b in tau:
        adj[a].append(b)
        adj[b].append(a)
    for row in adj:
        row.sort(key=lambda v: intervals[v],
                 reverse=(strategy.endswith("desc")))

    parent = {root: None}
    order = []
    if strategy.startswith("kahn"):
        def priority(v):
            a, b = intervals[v]
            if strategy == "kahn-interval-asc":
                return (a, b, v)
            if strategy == "kahn-interval-desc":
                return (-a, -b, v)
            if strategy == "kahn-span-asc":
                return (b - a, a, b, v)
            return (-(b - a), a, b, v)
        heap = []
        for v in adj[root]:
            parent[v] = root
            heappush(heap, (priority(v), v))
        while heap:
            _, u = heappop(heap)
            order.append(u)
            for v in adj[u]:
                if v not in parent:
                    parent[v] = u
                    heappush(heap, (priority(v), v))
    elif strategy.startswith("bfs"):
        queue = deque([root])
        while queue:
            u = queue.popleft()
            for v in adj[u]:
                if v not in parent:
                    parent[v] = u
                    order.append(v)
                    queue.append(v)
    else:
        stack = [root]
        while stack:
            u = stack.pop()
            children = [v for v in adj[u] if v not in parent]
            for v in reversed(children):
                parent[v] = u
                order.append(v)
                stack.append(v)
    assert len(parent) == len(intervals)
    return root, parent, tuple(order)


def fixed_order_outputs(intervals, tau, n, ids, strategy):
    root, parent, order = canonical_order(intervals, tau, strategy)
    states = {frozenset({tuple(sorted(intervals[root]))})}
    for child in order:
        J = intervals[child]
        next_states = set()
        for tree_edges in states:
            inside = sorted({x for a, b in tree_edges for x in (a, b)
                             if J[0] < x < J[1]})
            if inside:
                start, end = inside[0], 1
            else:
                start, end = intervals[parent[child]]
            path = tree_path(tree_edges, start, end)
            eligible = [
                e for e in zip(path, path[1:])
                if overlaps(e, J)
                and not (J[0] < min(e) < max(e) < J[1])
            ]
            assert eligible, (intervals, tau, strategy, child, J, path)
            old_edge = tuple(sorted(eligible[0]))
            a, b = old_edge
            xs = sorted((a, b, J[0], J[1]))
            valid = 0
            for local in LOCAL_TREES:
                mapped = tuple(tuple(sorted((xs[i], xs[j])))
                               for i, j in local)
                if old_edge in mapped:
                    continue
                valid += 1
                next_states.add(
                    frozenset((set(tree_edges) - {old_edge}) | set(mapped))
                )
            assert valid >= 2, (intervals, tau, strategy, child, old_edge, valid)
        assert len(next_states) >= 2 * len(states)
        states = next_states
    encoded = {encode_tree(T, ids) for T in states}
    assert len(encoded) == len(states)
    return encoded


def enumerate_rows(n):
    ids = edge_ids(n)
    rows, labels = [], []
    strategies = (
        "bfs-asc", "bfs-desc", "dfs-asc", "dfs-desc",
        "kahn-interval-asc", "kahn-interval-desc",
        "kahn-span-asc", "kahn-span-desc",
    )
    for matching in matchings(range(1, n + 1)):
        intervals = tuple(sorted(tuple(sorted(e)) for e in matching))
        overlap = overlap_edges(intervals)
        source_load = load(intervals, n)
        for tau in spanning_trees(len(intervals), overlap):
            outputs = set()
            for strategy in strategies:
                outputs.update(fixed_order_outputs(
                    intervals, tau, n, ids, strategy
                ))
            for mask in outputs:
                T = decode_tree(mask, n)
                assert all(x <= y for x, y in zip(load(T, n), source_load))
            rows.append(outputs)
            labels.append((intervals, tau))
    return rows, labels


def lexicographic_assignment(rows):
    targets = sorted({t for row in rows for t in row})
    target_id = {t: i for i, t in enumerate(targets)}
    adjacency = [sorted(target_id[t] for t in row) for row in rows]
    owner = [-1] * len(targets)
    chosen = [-1] * len(rows)
    max_depth = 0

    def augment(source, seen, depth):
        nonlocal max_depth
        max_depth = max(max_depth, depth)
        for v in adjacency[source]:
            if v in seen:
                continue
            seen.add(v)
            previous = owner[v]
            if previous == -1 or augment(previous, seen, depth + 1):
                owner[v] = source
                chosen[source] = v
                return True
        return False

    failures = []
    for source in range(len(rows)):
        if not augment(source, set(), 1):
            failures.append(source)

    # Alternating-reachability Hall witness from all unmatched left vertices.
    seen_left = set(failures)
    seen_right = set()
    queue = deque(failures)
    while queue:
        u = queue.popleft()
        for v in adjacency[u]:
            if chosen[u] == v or v in seen_right:
                continue
            seen_right.add(v)
            mate = owner[v]
            if mate != -1 and mate not in seen_left:
                seen_left.add(mate)
                queue.append(mate)
    return targets, chosen, failures, max_depth, seen_left, seen_right


def run(n, expected_sources):
    rows, labels = enumerate_rows(n)
    assert len(rows) == expected_sources, (n, len(rows), expected_sources)
    targets, chosen, failures, depth, hall_left, hall_right = (
        lexicographic_assignment(rows)
    )
    matched = sum(v >= 0 for v in chosen)
    min_degree = min(map(len, rows))
    max_degree = max(map(len, rows))
    print(f"n={n}: sources={len(rows)}, target_union={len(targets)}, "
          f"degree_range=[{min_degree},{max_degree}], matched={matched}, "
          f"failures={len(failures)}, max_augmenting_depth={depth}")
    if failures:
        print(f"  HALL_WITNESS: |S|={len(hall_left)}, "
              f"|N(S)|={len(hall_right)}, deficit={len(hall_left)-len(hall_right)}")
        witness = min(hall_left)
        print(f"  FIRST_WITNESS_SOURCE={labels[witness]}")
        raise SystemExit("Eight-order canonical subrelation is not source-saturating.")
    assignment = [targets[v] for v in chosen]
    assert len(set(assignment)) == len(rows)
    print("  PASS: eight-order canonical subrelation has a lexicographic injection")
    print(f"  first_assignments={[decode_tree(x, n) for x in assignment[:3]]}")


def main():
    run(4, 2)
    run(6, 22)
    run(8, 608)
    print("Canonical-order finite tests complete; no all-orders claim is made.")


if __name__ == "__main__":
    main()
