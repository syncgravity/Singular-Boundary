#!/usr/bin/env python3
"""Fixed-order guarded-switch subrelation and exact source matching.

For each source (M,tau), use one canonical parent-before-child order of the
rooted overlap tree. At each insertion choose the first admissible edge on
the connected-tree witness path and branch over every guarded local pattern
for that edge. This deliberately keeps a small, canonical sub-neighborhood:
it tests whether the all-orders proof can be reduced to one fixed insertion
order plus the two/three local choices supplied by the witness lemma.

Trees are encoded as integer edge bitmasks to keep the n=10 exact test small.
A deterministic lexicographic augmenting-path assignment is then computed.
This is a finite diagnostic, not an all-orders theorem.
"""
from verify_pf_i16_local_switch_fractional_transport import (
    LOCAL_TREES, load, matchings, overlap_edges, overlaps, spanning_trees,
    tree_path,
)
from verify_pf_i16_guarded_switch_injective_assignment import hopcroft_karp


def edge_ids(n):
    return {(a, b): i for i, (a, b) in enumerate(
        ( (a, b) for a in range(1, n + 1) for b in range(a + 1, n + 1) )
    )}


def encode_tree(edges, ids):
    return sum(1 << ids[tuple(sorted(e))] for e in edges)


def decode_tree(mask, n):
    pairs = [(a, b) for a in range(1, n + 1) for b in range(a + 1, n + 1)]
    return tuple(pairs[i] for i in range(len(pairs)) if (mask >> i) & 1)


def canonical_order(intervals, tau):
    root = next(i for i, I in enumerate(intervals) if I[0] == 1)
    adj = [[] for _ in intervals]
    for a, b in tau:
        adj[a].append(b)
        adj[b].append(a)
    parent = {root: None}
    order = []
    queue = [root]
    while queue:
        u = queue.pop(0)
        children = sorted((v for v in adj[u] if v not in parent),
                          key=lambda v: intervals[v])
        for v in children:
            parent[v] = u
            order.append(v)
            queue.append(v)
    assert len(parent) == len(intervals)
    return root, parent, tuple(order)


def fixed_order_outputs(intervals, tau, n, ids):
    root, parent, order = canonical_order(intervals, tau)
    root_edge = tuple(sorted(intervals[root]))
    states = {frozenset({root_edge})}
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
            assert eligible, (intervals, tau, child, J, path)
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
            assert valid >= 2, (intervals, tau, child, old_edge, valid)
        assert len(next_states) >= 2 * len(states)
        states = next_states
    encoded = {encode_tree(T, ids) for T in states}
    assert len(encoded) == len(states)
    for mask in encoded:
        T = decode_tree(mask, n)
        assert len(T) == n - 1
    return encoded


def enumerate_rows(n):
    ids = edge_ids(n)
    rows, labels = [], []
    for matching in matchings(range(1, n + 1)):
        intervals = tuple(sorted(tuple(sorted(e)) for e in matching))
        overlap = overlap_edges(intervals)
        source_load = load(intervals, n)
        for tau in spanning_trees(len(intervals), overlap):
            outputs = fixed_order_outputs(intervals, tau, n, ids)
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
    return targets, chosen, failures, max_depth


def run(n, expected_sources):
    rows, labels = enumerate_rows(n)
    assert len(rows) == expected_sources, (n, len(rows), expected_sources)
    targets, chosen, failures, depth = lexicographic_assignment(rows)
    matched = sum(v >= 0 for v in chosen)
    min_degree = min(map(len, rows))
    max_degree = max(map(len, rows))
    print(f"n={n}: sources={len(rows)}, target_union={len(targets)}, "
          f"degree_range=[{min_degree},{max_degree}], matched={matched}, "
          f"failures={len(failures)}, max_augmenting_depth={depth}")
    if failures:
        witness = failures[0]
        print(f"  FIRST_DEFICIT_SOURCE={labels[witness]}")
        raise SystemExit("Fixed-order canonical subrelation is not source-saturating.")
    assignment = [targets[v] for v in chosen]
    assert len(set(assignment)) == len(rows)
    print("  PASS: fixed-order canonical subrelation has a lexicographic injection")
    print(f"  first_assignments={[decode_tree(x, n) for x in assignment[:3]]}")


def main():
    run(4, 2)
    run(6, 22)
    run(8, 608)
    run(10, 31744)
    print("Fixed-order finite tests complete; no all-orders claim is made.")


if __name__ == "__main__":
    main()
