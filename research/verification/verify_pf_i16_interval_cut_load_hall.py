#!/usr/bin/env python3
"""Exact Hall-coupling regression for the weighted interval-tree conjecture.

For even n <= 8, form the left multiset consisting of tau(H_M) copies of
m(M) for every perfect matching M whose interval-overlap graph H_M is
connected. Form the right multiset from all labeled spanning trees T of K_n,
with one copy of c(T). Verify Hall's condition for c <= m coordinatewise.

This is a finite sufficient-coupling test only. It is not a proof of the
weighted inequality for arbitrary n, and failure would not refute that
inequality (the coupling is only sufficient).
"""
from collections import Counter
from itertools import product


def perfect_matchings(items):
    items = tuple(items)
    if not items:
        yield ()
        return
    a = items[0]
    for j in range(1, len(items)):
        b = items[j]
        rest = items[1:j] + items[j + 1:]
        for tail in perfect_matchings(rest):
            yield ((a, b),) + tail


def connected_graph(vertex_count, edges):
    if vertex_count <= 1:
        return True
    adj = [set() for _ in range(vertex_count)]
    for a, b in edges:
        adj[a].add(b)
        adj[b].add(a)
    seen = {0}
    stack = [0]
    while stack:
        v = stack.pop()
        for w in adj[v] - seen:
            seen.add(w)
            stack.append(w)
    return len(seen) == vertex_count


def bareiss_det(matrix):
    """Integer determinant by fraction-free Bareiss elimination."""
    a = [list(map(int, row)) for row in matrix]
    n = len(a)
    if n == 0:
        return 1
    sign = 1
    previous_pivot = 1
    for k in range(n - 1):
        if a[k][k] == 0:
            pivot_row = next((i for i in range(k + 1, n) if a[i][k]), None)
            if pivot_row is None:
                return 0
            a[k], a[pivot_row] = a[pivot_row], a[k]
            sign = -sign
        pivot = a[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                numerator = a[i][j] * pivot - a[i][k] * a[k][j]
                assert numerator % previous_pivot == 0
                a[i][j] = numerator // previous_pivot
        for i in range(k + 1, n):
            a[i][k] = 0
        previous_pivot = pivot
    return sign * a[-1][-1]


def spanning_tree_count(vertex_count, edges):
    if vertex_count == 1:
        return 1
    laplacian = [[0] * vertex_count for _ in range(vertex_count)]
    for a, b in edges:
        laplacian[a][a] += 1
        laplacian[b][b] += 1
        laplacian[a][b] -= 1
        laplacian[b][a] -= 1
    return bareiss_det([row[:-1] for row in laplacian[:-1]])


def left_load_multiplicities(n):
    left = Counter()
    connected_matchings = 0
    for matching in perfect_matchings(range(n)):
        intervals = tuple(tuple(sorted(pair)) for pair in matching)
        overlap_edges = tuple(
            (i, j)
            for i in range(len(intervals))
            for j in range(i + 1, len(intervals))
            if max(intervals[i][0], intervals[j][0])
            < min(intervals[i][1], intervals[j][1])
        )
        tau = spanning_tree_count(len(intervals), overlap_edges)
        if tau == 0:
            continue
        connected_matchings += 1
        load = tuple(
            sum(a <= k < b for a, b in intervals)
            for k in range(n - 1)
        )
        left[load] += tau
    return left, connected_matchings


def prufer_tree_loads(n):
    """Count c(T) over all n^(n-2) labeled trees using Prüfer codes."""
    counts = Counter()
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
        load = tuple(
            sum(min(a, b) <= k < max(a, b) for a, b in edges)
            for k in range(n - 1)
        )
        counts[load] += 1
    assert sum(counts.values()) == n ** (n - 2)
    return counts


def hall_minimum_slack(left, right):
    """Return minimum Hall slack and its witnessing nonempty left subset."""
    types = tuple(left)
    best_slack = None
    best_subset = None
    best_demand = best_supply = None
    for mask in range(1, 1 << len(types)):
        subset = tuple(types[i] for i in range(len(types)) if mask & (1 << i))
        demand = sum(left[v] for v in subset)
        neighborhood = {
            u for u in right
            if any(all(x <= y for x, y in zip(u, v)) for v in subset)
        }
        supply = sum(right[u] for u in neighborhood)
        slack = supply - demand
        if best_slack is None or slack < best_slack:
            best_slack = slack
            best_subset = subset
            best_demand = demand
            best_supply = supply
    return best_slack, best_subset, best_demand, best_supply



def least_primitive_majorant(load, primitive_paths):
    """Least primitive Dyck path h satisfying load <= h coordinatewise.

    Primitive Dyck paths form a meet-semilattice under coordinatewise min:
    the minimum of two such paths is again a primitive Dyck path. Therefore
    the coordinatewise minimum of all majorants is the unique least one.
    """
    candidates = [
        h for h in primitive_paths
        if all(x <= y for x, y in zip(load, h))
    ]
    if not candidates:
        return None
    least = tuple(min(h[k] for h in candidates) for k in range(len(load)))
    assert least in primitive_paths
    assert all(x <= y for x, y in zip(load, least))
    assert all(
        all(least[k] <= h[k] for k in range(len(load)))
        for h in candidates
    )
    return least


def right_ceiling_multiplicities(right, primitive_paths):
    """Partition all relevant trees by their least primitive Dyck majorant.

    Trees whose cut-load vector is not dominated by the maximal primitive
    Dyck path cannot neighbor any left type and are omitted.
    """
    ceilings = Counter()
    excluded = 0
    for load, count in right.items():
        ceiling = least_primitive_majorant(load, primitive_paths)
        if ceiling is None:
            excluded += count
        else:
            ceilings[ceiling] += count
    return ceilings, excluded


def check(n, expected_left, expected_types, expected_right_types):
    left, connected_matchings = left_load_multiplicities(n)
    right = prufer_tree_loads(n)
    assert sum(left.values()) == expected_left, (n, left)
    assert len(left) == expected_types, (n, left)
    assert len(right) == expected_right_types, (n, len(right))
    slack, subset, demand, supply = hall_minimum_slack(left, right)
    assert slack >= 0, (n, slack, subset, demand, supply)

    # A stronger sufficient condition: classify each relevant tree by its
    # least primitive-Dyck majorant. If each class has at least as many trees
    # as left copies at that exact load, a within-class injection proves Hall.
    ceilings, excluded = right_ceiling_multiplicities(right, tuple(left))
    for load, multiplicity in left.items():
        assert ceilings[load] >= multiplicity, (
            n, load, multiplicity, ceilings[load]
        )

    print(
        f"PASS n={n}: connected_matchings={connected_matchings}, "
        f"left_copies={sum(left.values())}, left_load_types={len(left)}, "
        f"trees={sum(right.values())}, right_load_types={len(right)}, "
        f"minimum_Hall_slack={slack}, "
        f"relevant_trees={sum(ceilings.values())}, excluded_trees={excluded}"
    )
    for load, multiplicity in sorted(left.items()):
        print(
            f"  load {load}: left={multiplicity}, "
            f"same-ceiling trees={ceilings[load]}"
        )


def main():
    check(4, expected_left=2, expected_types=1, expected_right_types=13)
    check(6, expected_left=22, expected_types=2, expected_right_types=383)
    check(8, expected_left=608, expected_types=5, expected_right_types=15165)
    print("PASS exact capacitated Hall and pointwise ceiling tests through eight ports")
    print("NOTE finite sufficient-coupling regression only; no all-n theorem")


if __name__ == "__main__":
    main()
