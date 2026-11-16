#!/usr/bin/env python3
"""Exact root-interval / rooted-overlap-forest decomposition of L(h)."""
from __future__ import annotations

from itertools import combinations


def matchings(vertices):
    vertices = tuple(vertices)
    if not vertices:
        yield ()
        return
    a = vertices[0]
    for j in range(1, len(vertices)):
        b = vertices[j]
        rest = vertices[1:j] + vertices[j + 1:]
        for tail in matchings(rest):
            yield ((a, b),) + tail


def load(matching, n):
    return tuple(sum(a <= k < b for a, b in matching)
                 for k in range(1, n))


def overlap_graph(intervals):
    edges = []
    for i, (a, b) in enumerate(intervals):
        for j in range(i + 1, len(intervals)):
            c, d = intervals[j]
            if max(a, c) < min(b, d):
                edges.append((i, j))
    return tuple(edges)


def component_roots(vertex_count, chosen_edges, roots):
    parent = list(range(vertex_count))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for a, b in chosen_edges:
        ra, rb = find(a), find(b)
        if ra == rb:
            return None
        parent[ra] = rb
    comps = {}
    for v in range(vertex_count):
        comps.setdefault(find(v), []).append(v)
    if any(sum(v in roots for v in comp) != 1 for comp in comps.values()):
        return None
    return comps


def tree_count(graph_edges, vertex_count):
    if vertex_count == 1:
        return 1
    total = 0
    for chosen in combinations(graph_edges, vertex_count - 1):
        if component_roots(vertex_count, chosen, {0}) is not None:
            # With a single distinguished vertex, this test means connected tree.
            total += 1
    return total


def rooted_forest_count(graph_edges, vertex_count, roots):
    roots = frozenset(roots)
    if not roots or len(roots) > vertex_count:
        return 0
    total = 0
    for chosen in combinations(graph_edges, vertex_count - len(roots)):
        if component_roots(vertex_count, chosen, roots) is not None:
            total += 1
    return total


def left_direct(n, h):
    total = 0
    for M in matchings(tuple(range(1, n + 1))):
        if load(M, n) != h:
            continue
        H = overlap_graph(M)
        total += tree_count(H, len(M))
    return total


def left_rooted_decomposition(n, h):
    total = 0
    for p in range(2, n + 1):
        remaining_vertices = tuple(v for v in range(2, n + 1) if v != p)
        for M0 in matchings(remaining_vertices):
            residual = tuple(h[k - 1] - int(k < p)
                             for k in range(1, n))
            if load(M0, n) != residual:
                continue
            # M0 intervals are indexed in their tuple order.
            candidate_roots = {
                i for i, (a, b) in enumerate(M0) if a < p
            }
            H0 = overlap_graph(M0)
            ordered_roots = sorted(candidate_roots)
            # The actual neighbors of [1,p] in the overlap tree form an
            # arbitrary nonempty subset R of all possible overlapping
            # intervals. Each component of the deleted forest has exactly
            # one root from this selected R.
            for mask in range(1, 1 << len(ordered_roots)):
                roots = {
                    ordered_roots[j] for j in range(len(ordered_roots))
                    if mask & (1 << j)
                }
                total += rooted_forest_count(H0, len(M0), roots)
    return total


def primitive_dyck_paths(n):
    # Enumerate up/down words and retain positive interior heights.
    paths = []

    def rec(pos, height, word, heights):
        if pos == n:
            if height == 0:
                paths.append(tuple(heights))
            return
        remaining = n - pos
        if height + 1 <= remaining - 1:
            rec(pos + 1, height + 1, word + "U", heights + [height + 1])
        if height > 1 or (height == 1 and pos == n - 1):
            rec(pos + 1, height - 1, word + "D", heights + [height - 1])

    # Force first U, last D; strict positive interior heights.
    def walk(pos, height, heights):
        if pos == n - 1:
            if height == 1:
                paths.append(tuple(heights))
            return
        if height + 1 <= n - pos - 1:
            walk(pos + 1, height + 1, heights + [height + 1])
        if height > 1:
            walk(pos + 1, height - 1, heights + [height - 1])

    walk(1, 1, [1])
    return paths


def main():
    checks = 0
    for n in (4, 6, 8, 10):
        for h in primitive_dyck_paths(n):
            direct = left_direct(n, h)
            decomposed = left_rooted_decomposition(n, h)
            assert direct == decomposed, (n, h, direct, decomposed)
            checks += 1
    print(f"PASS: root-interval rooted-forest identity; {checks} primitive loads, n=4,6,8,10")


if __name__ == "__main__":
    main()
