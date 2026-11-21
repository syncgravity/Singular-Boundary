#!/usr/bin/env python3
"""Exact regression for the proper-down-set endpoint-leaf decomposition.

Checks the identity
 N_n(D) = sum_{p,q=2}^{n-1} N_{n-2}(B_{p,q}(D))
for every down-set D of primitive Dyck paths at n=4,6,8.
All counts are exact integers from Prüfer-code enumeration.
"""
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


def tree_loads(n):
    counts = {}
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
        counts[load] = counts.get(load, 0) + 1
    return counts


def dominated_by_any(load, capacities):
    return any(
        all(x <= y for x, y in zip(load, bound))
        for bound in capacities
    )


def downsets(paths):
    paths = tuple(paths)
    for mask in range(1 << len(paths)):
        chosen = {paths[i] for i in range(len(paths)) if mask & (1 << i)}
        if all(
            g in chosen
            for h in chosen
            for g in paths
            if all(x <= y for x, y in zip(g, h))
        ):
            yield chosen


def maximal_elements(chosen):
    return tuple(
        h for h in chosen
        if not any(h != g and all(x <= y for x, y in zip(h, g))
                   for g in chosen)
    )


def residual(h, p, q):
    # Interior vertices are old labels 2,...,n-1; j-th new cut
    # is old cut k=j+1.
    return tuple(
        h[k - 1] - int(p > k) - int(q <= k)
        for k in range(2, len(h))
    )


def count_union(load_counts, capacities):
    return sum(
        count for load, count in load_counts.items()
        if dominated_by_any(load, capacities)
    )


def check(n):
    paths = primitive_paths(n)
    full = tree_loads(n)
    interior = tree_loads(n - 2)
    tested = 0
    for D in downsets(paths):
        if not D:
            continue
        H = maximal_elements(D)
        direct = count_union(full, H)
        decomposed = 0
        for p in range(2, n):
            for q in range(2, n):
                B = tuple(residual(h, p, q) for h in H)
                decomposed += count_union(interior, B)
        assert direct == decomposed, (n, sorted(D), direct, decomposed)
        tested += 1
    print(
        f"PASS n={n}: primitive_paths={len(paths)}, "
        f"nonempty_downsets={tested}, labeled_trees={sum(full.values())}"
    )


def main():
    for n in (4, 6, 8):
        check(n)
    print("PASS proper-down-set endpoint-leaf decomposition through eight ports")
    print("NOTE exact right-supply identity only; no Hall inequality is claimed")


if __name__ == "__main__":
    main()
