#!/usr/bin/env python3
"""Exhaustive exact check of the quotient-tree injection for graphs through n=5."""
from itertools import combinations


def partitions(items):
    items = tuple(items)
    if not items:
        yield ()
        return
    x, *rest = items
    for p in partitions(rest):
        yield ((x,),) + p
        for j in range(len(p)):
            yield p[:j] + (tuple(sorted(p[j] + (x,))),) + p[j + 1:]


def canon(p):
    return tuple(sorted((tuple(sorted(b)) for b in p), key=lambda b: b[0]))


def all_partitions(n):
    return sorted({canon(p) for p in partitions(range(n))})


def connected(vertices, edges):
    vertices = set(vertices)
    if not vertices:
        return True
    adj = {v: set() for v in vertices}
    for a, b in edges:
        if a in vertices and b in vertices:
            adj[a].add(b)
            adj[b].add(a)
    seen = {next(iter(vertices))}
    stack = list(seen)
    while stack:
        x = stack.pop()
        for y in adj[x] - seen:
            seen.add(y)
            stack.append(y)
    return seen == vertices


def tree_count(vertices, edges):
    vertices = tuple(vertices)
    if len(vertices) <= 1:
        return 1
    total = 0
    for chosen in combinations(edges, len(vertices) - 1):
        if connected(vertices, chosen):
            total += 1
    return total


def connected_partitions(n, graph_edges):
    for p in all_partitions(n):
        if all(connected(B, graph_edges) for B in p):
            yield p


def quotient_graph(partition, graph_edges):
    owner = {v: i for i, B in enumerate(partition) for v in B}
    qedges = set()
    for a, b in graph_edges:
        x, y = owner[a], owner[b]
        if x != y:
            qedges.add(tuple(sorted((x, y))))
    return tuple(range(len(partition))), tuple(sorted(qedges))


def check_one_graph(n, graph_edges):
    tau_g = tree_count(range(n), graph_edges)
    lhs = 0
    pairs = []
    for p in connected_partitions(n, graph_edges):
        qv, qe = quotient_graph(p, graph_edges)
        tau_q = tree_count(qv, qe)
        lhs += tau_q
        pairs.append((p, qv, qe))
    rhs = (2 ** (n - 1)) * tau_g
    assert lhs <= rhs, (n, graph_edges, lhs, rhs)

    # Explicitly build the injection (P, quotient tree) -> (T, marked cross edges).
    # Canonical internal trees and canonical cross edges make it deterministic.
    encodings = set()
    for p, qv, qe in pairs:
        for qtree in combinations(qe, max(0, len(qv) - 1)):
            if not connected(qv, qtree):
                continue
            owner = {v: i for i, B in enumerate(p) for v in B}
            chosen = []
            for B in p:
                internal = [(a, b) for a, b in graph_edges if a in B and b in B]
                # Deterministic spanning tree: greedily add lexicographic edges.
                parent = {v: v for v in B}
                def find(x):
                    while parent[x] != x:
                        parent[x] = parent[parent[x]]
                        x = parent[x]
                    return x
                for a, b in sorted(internal):
                    ra, rb = find(a), find(b)
                    if ra != rb:
                        parent[ra] = rb
                        chosen.append((a, b))
            cross = []
            for x, y in qtree:
                B, C = p[x], p[y]
                candidates = [(a, b) for a, b in graph_edges
                              if (a in B and b in C) or (a in C and b in B)]
                edge = min(candidates)
                cross.append(edge)
                chosen.append(edge)
            T = tuple(sorted(chosen))
            F = tuple(sorted(cross))
            assert len(T) == n - 1 and connected(range(n), T)
            key = (T, F)
            assert key not in encodings, (n, graph_edges, p, qtree, key)
            encodings.add(key)
    assert len(encodings) == lhs


def main():
    for n in range(1, 6):
        all_edges = list(combinations(range(n), 2))
        for mask in range(1 << len(all_edges)):
            graph = tuple(all_edges[i] for i in range(len(all_edges))
                          if (mask >> i) & 1)
            check_one_graph(n, graph)
    print("PASS quotient-tree injection for every simple graph with 1<=n<=5")
    print("PASS sum_P tau(G/P) <= 2^(n-1) tau(G) on exhaustive graph family")


if __name__ == "__main__":
    main()
