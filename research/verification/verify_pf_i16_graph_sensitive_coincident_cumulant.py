#!/usr/bin/env python3
"""Exhaustive finite-graph checks for the support-sensitive coincident cumulant identity."""
from itertools import combinations
from math import factorial, prod


def partitions(items):
    if not items:
        yield []
        return
    first = items[0]
    for p in partitions(items[1:]):
        yield [[first]] + [block[:] for block in p]
        for j in range(len(p)):
            q = [block[:] for block in p]
            q[j] = [first] + q[j]
            yield q


def components(vertices, adj):
    unseen = set(vertices)
    result = []
    while unseen:
        root = unseen.pop()
        block = {root}
        stack = [root]
        while stack:
            v = stack.pop()
            for w in tuple(unseen):
                if adj[v][w]:
                    unseen.remove(w)
                    block.add(w)
                    stack.append(w)
        result.append(frozenset(block))
    return result


def connected(vertices, adj):
    return len(components(vertices, adj)) == 1


def spanning_tree_count(vertices, adj):
    vertices = list(vertices)
    n = len(vertices)
    if n == 1:
        return 1
    edges = [(i, j) for i in range(n) for j in range(i + 1, n)
             if adj[vertices[i]][vertices[j]]]
    count = 0
    for chosen in combinations(edges, n - 1):
        parent = list(range(n))

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        acyclic = True
        for i, j in chosen:
            a, b = find(i), find(j)
            if a == b:
                acyclic = False
                break
            parent[a] = b
        if acyclic and len({find(i) for i in range(n)}) == 1:
            count += 1
    return count


def chromatic_linear_coefficient(adj):
    n = len(adj)
    coefficient = 0
    for partition in partitions(list(range(n))):
        proper = all(not adj[i][j]
                     for block in partition
                     for i, j in combinations(block, 2))
        if proper:
            k = len(partition)
            coefficient += (-1) ** (k - 1) * factorial(k - 1)
    return coefficient


def quotient_graph(sigma, adj):
    k = len(sigma)
    qadj = [[False] * k for _ in range(k)]
    for i, j in combinations(range(k), 2):
        qadj[i][j] = qadj[j][i] = any(
            adj[a][b] for a in sigma[i] for b in sigma[j]
        )
    return qadj


def check_graph(adj):
    n = len(adj)
    vertices = list(range(n))
    all_partitions = list(partitions(vertices))
    connected_partitions = [
        p for p in all_partitions
        if all(connected(block, adj) for block in p)
    ]

    connected_sets = [
        frozenset(s)
        for size in range(1, n + 1)
        for s in combinations(vertices, size)
        if connected(s, adj)
    ]
    # Deterministic bounded "connected moments"; only the algebraic identity matters.
    mu = {s: ((sum((i + 1) * (i + 3) for i in s) % 7) - 3)
          for s in connected_sets}

    def block_moment(block):
        return prod(mu[c] for c in components(block, adj))

    cumulant = sum(
        (-1) ** (len(p) - 1) * factorial(len(p) - 1)
        * prod(block_moment(block) for block in p)
        for p in all_partitions
    )

    regrouped = 0
    quotient_tree_sum = 0
    for sigma in connected_partitions:
        qadj = quotient_graph(sigma, adj)
        c_q = chromatic_linear_coefficient(qadj)
        tau_q = spanning_tree_count(range(len(sigma)), qadj)
        assert abs(c_q) <= tau_q
        if not connected(range(len(sigma)), qadj):
            assert c_q == 0
        regrouped += c_q * prod(mu[frozenset(block)] for block in sigma)
        if connected(range(len(sigma)), qadj):
            quotient_tree_sum += tau_q

    assert cumulant == regrouped, (cumulant, regrouped, adj)
    tau_g = spanning_tree_count(vertices, adj)
    assert quotient_tree_sum <= (2 ** (n - 1)) * tau_g, (
        quotient_tree_sum, tau_g, adj
    )
    if not connected(vertices, adj):
        assert cumulant == 0
        assert tau_g == 0


graphs_checked = 0
for n in range(1, 6):
    possible_edges = list(combinations(range(n), 2))
    for mask in range(1 << len(possible_edges)):
        adjacency = [[False] * n for _ in range(n)]
        for bit, (i, j) in enumerate(possible_edges):
            if mask & (1 << bit):
                adjacency[i][j] = adjacency[j][i] = True
        check_graph(adjacency)
        graphs_checked += 1

print(f"PASS: exact cumulant regrouping and quotient-tree bound on {graphs_checked} graphs (n<=5)")
print("PASS: |[q] chi_Q(q)| <= tau(Q) for every quotient graph tested")
print("PASS: sum_sigma tau(Q_sigma) <= 2^(r-1) tau(G) for every graph tested")
print("SCOPE: exhaustive checks support the proof; they do not replace the general deletion-contraction and cut-bijection arguments")
print("SCOPE: coincident-time independent-coordinate result only; temporal weighted extension remains open")
