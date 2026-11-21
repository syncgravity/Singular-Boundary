#!/usr/bin/env python3
"""Exact regression for the endpoint rooted-forest recurrence for cut-bounded trees."""
from __future__ import annotations

from itertools import combinations, product


def prufer_trees(n: int):
    """Yield edge sets of all labeled trees on 1,...,n."""
    if n == 2:
        yield frozenset({(1, 2)})
        return
    for code in product(range(1, n + 1), repeat=n - 2):
        degree = [0] + [1] * n
        for x in code:
            degree[x] += 1
        edges = []
        for x in code:
            leaf = next(i for i in range(1, n + 1) if degree[i] == 1)
            edges.append((min(leaf, x), max(leaf, x)))
            degree[leaf] -= 1
            degree[x] -= 1
        a = next(i for i in range(1, n + 1) if degree[i] == 1)
        b = next(i for i in range(a + 1, n + 1) if degree[i] == 1)
        edges.append((a, b))
        yield frozenset(edges)


def cut_loads(edges, n):
    return tuple(sum(a <= k < b for a, b in edges) for k in range(1, n))


def direct_tree_count(n, caps):
    return sum(all(x <= y for x, y in zip(cut_loads(t, n), caps))
               for t in prufer_trees(n))


def forest_count(vertices, roots, caps):
    """Forests with one designated root per component and bounded ordered cuts."""
    vertices = tuple(vertices)
    roots = frozenset(roots)
    m = len(vertices)
    all_edges = tuple(combinations(vertices, 2))
    need_edges = m - len(roots)
    total = 0
    for chosen in combinations(all_edges, need_edges):
        parent = {v: v for v in vertices}

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        acyclic = True
        for a, b in chosen:
            ra, rb = find(a), find(b)
            if ra == rb:
                acyclic = False
                break
            parent[ra] = rb
        if not acyclic:
            continue
        components = {}
        for v in vertices:
            components.setdefault(find(v), []).append(v)
        if len(components) != len(roots):
            continue
        if any(sum(v in roots for v in comp) != 1 for comp in components.values()):
            continue
        loads = tuple(sum(a <= k < b for a, b in chosen)
                      for k in range(vertices[0], vertices[-1]))
        if all(x <= y for x, y in zip(loads, caps)):
            total += 1
    return total


def rooted_forest_rhs(n, caps):
    vertices = tuple(range(2, n + 1))
    total = 0
    for d in range(1, min(caps[0], n - 1) + 1):
        for roots in combinations(vertices, d):
            residual = tuple(caps[k - 1] -
                             sum(v > k for v in roots)
                             for k in range(2, n))
            if min(residual, default=0) < 0:
                continue
            total += forest_count(vertices, roots, residual)
    return total


def main():
    checks = 0
    for n in range(3, 7):
        for caps in product((1, 2), repeat=n - 1):
            lhs = direct_tree_count(n, caps)
            rhs = rooted_forest_rhs(n, caps)
            assert lhs == rhs, (n, caps, lhs, rhs)
            checks += 1
    print(f"PASS: rooted-forest endpoint recurrence; {checks} capacity vectors, n=3..6")


if __name__ == "__main__":
    main()
