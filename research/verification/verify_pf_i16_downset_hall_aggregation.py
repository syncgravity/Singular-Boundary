#!/usr/bin/env python3
"""Exact proper-downset Hall aggregation and endpoint-state obstruction.

Enumerates every primitive-path down-set, all perfect matchings and their
interval-overlap spanning trees, and all labeled port trees for n=4,6,8.
Also records a concrete failure of endpoint-statewise Hall domination.
"""
from collections import Counter
from itertools import product


def primitive_paths(n):
    out = []
    def visit(k, height, path):
        if k == n - 1:
            if height == 1:
                out.append(tuple(path))
            return
        visit(k + 1, height + 1, path + [height + 1])
        if height > 1:
            visit(k + 1, height - 1, path + [height - 1])
    visit(0, 0, [])
    return tuple(out)


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
        (i, j) for i in range(len(intervals))
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


def spanning_tree_count(v, edges):
    if v == 1:
        return 1
    total = 0
    for mask in range(1 << len(edges)):
        if mask.bit_count() == v - 1:
            c = components(v, edges, mask)
            if c is not None and len(c) == 1:
                total += 1
    return total


def left_loads(n, retain_states=False):
    out = Counter()
    states = Counter()
    for matching in matchings(range(1, n + 1)):
        intervals = tuple(sorted(tuple(sorted(e)) for e in matching))
        tau = spanning_tree_count(len(intervals), overlap_edges(intervals))
        if not tau:
            continue
        load = tuple(sum(a <= k < b for a, b in intervals)
                     for k in range(1, n))
        out[load] += tau
        if retain_states:
            partner = {}
            for a, b in matching:
                partner[a] = b
                partner[b] = a
            states[(partner[1], partner[n], load)] += tau
    return (out, states) if retain_states else out


def port_tree_loads(n, retain_states=False):
    out = Counter()
    states = Counter()
    for code in product(range(n), repeat=n - 2):
        degree = [1] * n
        for v in code:
            degree[v] += 1
        edges = []
        for v in code:
            leaf = next(i for i, d in enumerate(degree) if d == 1)
            edges.append((leaf, v))
            degree[leaf] -= 1
            degree[v] -= 1
        leaves = [i for i, d in enumerate(degree) if d == 1]
        edges.append((leaves[0], leaves[1]))
        adj = [[] for _ in range(n)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        load = tuple(sum(min(a, b) <= k < max(a, b) for a, b in edges)
                     for k in range(1, n))
        out[load] += 1
        if retain_states and len(adj[0]) == len(adj[n - 1]) == 1:
            states[(adj[0][0] + 1, adj[n - 1][0] + 1, load)] += 1
    return (out, states) if retain_states else out


def leq(a, b):
    return all(x <= y for x, y in zip(a, b))


def downsets(paths):
    for mask in range(1 << len(paths)):
        chosen = {paths[i] for i in range(len(paths)) if mask & (1 << i)}
        if all(g in chosen for h in chosen for g in paths
               if leq(g, h)):
            yield chosen


def maximal(chosen):
    return tuple(h for h in chosen if not any(
        h != g and leq(h, g) for g in chosen
    ))


def check_order(n):
    paths = primitive_paths(n)
    left = left_loads(n)
    right = port_tree_loads(n)
    slacks = []
    for D in downsets(paths):
        H = maximal(D)
        demand = sum(left[h] for h in D)
        supply = sum(c for load, c in right.items()
                     if any(leq(load, h) for h in H))
        slack = supply - demand
        assert slack >= 0, (n, sorted(D), demand, supply)
        slacks.append((slack, demand, supply, len(D)))
    nonempty = [x for x in slacks if x[3]]
    print(
        f"PASS n={n}: paths={len(paths)}, downsets={len(slacks)}, "
        f"min_nonempty_slack={min(x[0] for x in nonempty)}, "
        f"full_slack={next(x[0] for x in slacks if x[3] == len(paths))}"
    )


def check_statewise_obstruction():
    n = 8
    h = (1, 2, 1, 2, 1, 2, 1)
    left, left_states = left_loads(n, True)
    right, right_states = port_tree_loads(n, True)
    demand = sum(left[g] for g in primitive_paths(n) if leq(g, h))
    supply = sum(c for load, c in right.items() if leq(load, h))
    local_demand = sum(c for (p, q, load), c in left_states.items()
                       if (p, q) == (3, 6) and leq(load, h))
    local_supply = sum(c for (p, q, load), c in right_states.items()
                       if (p, q) == (3, 6) and leq(load, h))
    assert (local_demand, local_supply) == (2, 0)
    assert (demand, supply) == (8, 36)
    print(
        "PASS statewise obstruction: D=down(h), state=(3,6) "
        "has demand=2, supply=0; aggregate demand=8, supply=36"
    )


def main():
    for n in (4, 6, 8):
        check_order(n)
    check_statewise_obstruction()
    print("NOTE finite aggregate Hall checks only; no all-orders proof claimed")


if __name__ == "__main__":
    main()
