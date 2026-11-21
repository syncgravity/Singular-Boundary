#!/usr/bin/env python3
"""Verify the all-orders local-switch witness construction at small orders.

For each matching M and each spanning tree tau of its interval-overlap graph,
construct a port tree by rooting tau at the interval containing port 1 and
inserting child intervals along monotone parent paths. Every switch replaces
one tree edge by the increasing path through the four endpoints.
The verifier checks that the result is a tree and c(T) <= m(M).
It deliberately does not claim injectivity.
"""
from collections import Counter
from itertools import combinations


def matchings(items):
    items = tuple(items)
    if not items:
        yield ()
        return
    a = items[0]
    for j in range(1, len(items)):
        b = items[j]
        for tail in matchings(items[1:j] + items[j + 1:]):
            yield ((a, b),) + tail


def overlap_edges(intervals):
    return tuple(
        (i, j)
        for i in range(len(intervals))
        for j in range(i + 1, len(intervals))
        if max(intervals[i][0], intervals[j][0])
        < min(intervals[i][1], intervals[j][1])
    )


def components(v, edges, mask):
    parent = list(range(v))
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    for bit, (a, b) in enumerate(edges):
        if (mask >> bit) & 1:
            x, y = find(a), find(b)
            if x == y:
                return None
            parent[x] = y
    return {find(i) for i in range(v)}


def spanning_trees(v, edges):
    if v == 1:
        yield ()
        return
    for mask in range(1 << len(edges)):
        if mask.bit_count() != v - 1:
            continue
        c = components(v, edges, mask)
        if c is not None and len(c) == 1:
            yield tuple(edges[i] for i in range(len(edges))
                        if (mask >> i) & 1)


def construct(intervals, tau, n):
    v = len(intervals)
    root = next(i for i, I in enumerate(intervals) if I[0] == 1)
    adj = [[] for _ in intervals]
    for a, b in tau:
        adj[a].append(b)
        adj[b].append(a)

    parent = {root: None}
    order = [root]
    for u in order:
        for w in sorted(adj[u], key=lambda z: intervals[z]):
            if w not in parent:
                parent[w] = u
                order.append(w)
    assert len(order) == v

    paths = {root: [intervals[root][0], intervals[root][1]]}
    edges = {tuple(sorted(intervals[root]))}
    for child in order[1:]:
        J = intervals[child]
        P = paths[parent[child]]
        selected = next(
            ((u, w) for u, w in zip(P, P[1:])
             if max(u, J[0]) < min(w, J[1])),
            None,
        )
        assert selected is not None, (intervals, tau, child, P)
        u, w = selected
        xs = sorted((u, w, J[0], J[1]))
        old_edge = tuple(sorted((u, w)))
        assert old_edge in edges
        edges.remove(old_edge)
        edges.update((a, b) for a, b in zip(xs, xs[1:]))

        # The new path between the old edge endpoints is a monotone
        # subpath of x1-x2-x3-x4. Update every maintained interval path
        # that used the replaced edge.
        replacement = xs[xs.index(u):xs.index(w) + 1]
        new_paths = {}
        for key, old_path in paths.items():
            new_path = []
            i = 0
            while i < len(old_path):
                if (i + 1 < len(old_path)
                        and old_path[i] == u and old_path[i + 1] == w):
                    new_path.extend(replacement)
                    i += 2
                else:
                    new_path.append(old_path[i])
                    i += 1
            new_paths[key] = new_path

        lo, hi = xs.index(J[0]), xs.index(J[1])
        new_paths[child] = xs[lo:hi + 1]
        paths = new_paths

    assert len(edges) == n - 1, (intervals, tau, edges)
    parent_port = list(range(n + 1))
    def find(x):
        while parent_port[x] != x:
            parent_port[x] = parent_port[parent_port[x]]
            x = parent_port[x]
        return x
    for a, b in edges:
        x, y = find(a), find(b)
        assert x != y, (intervals, tau, edges)
        parent_port[x] = y
    assert len({find(i) for i in range(1, n + 1)}) == 1

    tree_load = tuple(
        sum(a <= k < b for a, b in edges) for k in range(1, n)
    )
    matching_load = tuple(
        sum(a <= k < b for a, b in intervals) for k in range(1, n)
    )
    assert all(x <= y for x, y in zip(tree_load, matching_load)), (
        intervals, tau, tree_load, matching_load
    )
    return tuple(sorted(edges))


def check(n):
    source_count = 0
    images = set()
    for matching in matchings(range(1, n + 1)):
        intervals = tuple(sorted(tuple(sorted(e)) for e in matching))
        overlap = overlap_edges(intervals)
        for tau in spanning_trees(len(intervals), overlap):
            image = construct(intervals, tau, n)
            images.add(image)
            source_count += 1
    print(
        f"PASS n={n}: left_objects={source_count}, "
        f"distinct_deterministic_witnesses={len(images)}"
    )
    if n == 8:
        assert source_count == 608
        assert len(images) == 62


def main():
    for n in (4, 6, 8):
        check(n)
    print("PASS local-switch cut-load witness construction through eight ports")
    print("NOTE witness map is many-to-one; no Hall injection is claimed")


if __name__ == "__main__":
    main()
