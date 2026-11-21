#!/usr/bin/env python3
"""Exact two-endpoint rooted-forest recurrence for left interval demand."""
from collections import Counter


def matchings(items):
    items = tuple(items)
    if not items:
        yield ()
        return
    a = items[0]
    for j in range(1, len(items)):
        b = items[j]
        rest = items[1:j] + items[j + 1:]
        for tail in matchings(rest):
            yield ((a, b),) + tail


def overlap_edges(intervals):
    return tuple(
        (i, j)
        for i in range(len(intervals))
        for j in range(i + 1, len(intervals))
        if max(intervals[i][0], intervals[j][0])
        < min(intervals[i][1], intervals[j][1])
    )


def forest_components(vertex_count, edges, mask):
    parent = list(range(vertex_count))
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    selected = []
    for bit, (u, v) in enumerate(edges):
        if not (mask >> bit) & 1:
            continue
        ru, rv = find(u), find(v)
        if ru == rv:
            return None
        parent[ru] = rv
        selected.append((u, v))
    groups = {}
    for v in range(vertex_count):
        groups.setdefault(find(v), []).append(v)
    return tuple(tuple(group) for group in groups.values())


def two_root_forest_weight(intervals, p, q, cone=False):
    """Count augmented-graph spanning trees by deleting its endpoint roots.

    cone=True is the single interval [1,n] case: one universal root.
    Otherwise the roots are [1,p] and [q,n].
    """
    v = len(intervals)
    edges = overlap_edges(intervals)
    total = 0
    for mask in range(1 << len(edges)):
        components = forest_components(v, edges, mask)
        if components is None:
            continue
        if cone:
            weight = 1
            for C in components:
                weight *= len(C)
        else:
            a = [sum(intervals[i][0] < p for i in C) for C in components]
            b = [sum(intervals[i][1] > q for i in C) for C in components]
            factors = [x + y for x, y in zip(a, b)]
            # A spanning tree may use the A-B edge (if available),
            # or omit it and use exactly one forest component as the bridge.
            weight = 0
            if q < p:
                product = 1
                for f in factors:
                    product *= f
                weight += product
            for j in range(len(components)):
                term = a[j] * b[j]
                for i, f in enumerate(factors):
                    if i != j:
                        term *= f
                weight += term
        total += weight
    return total


def direct_left(n):
    out = Counter()
    for M in matchings(range(1, n + 1)):
        intervals = tuple(sorted(tuple(sorted(e)) for e in M))
        edges = overlap_edges(intervals)
        # Count spanning trees by edge-subset enumeration, independent of
        # the forest decomposition being tested.
        tau = 0
        for mask in range(1 << len(edges)):
            if mask.bit_count() != len(intervals) - 1:
                continue
            comps = forest_components(len(intervals), edges, mask)
            if comps is not None and len(comps) == 1:
                tau += 1
        if tau:
            load = tuple(sum(a <= k < b for a, b in intervals)
                         for k in range(1, n))
            out[load] += tau
    return out


def endpoint_recurrence(n):
    out = Counter()
    # Exceptional single interval [1,n].
    for M0 in matchings(range(2, n)):
        intervals = tuple(sorted(tuple(sorted(e)) for e in M0))
        weight = two_root_forest_weight(intervals, None, None, cone=True)
        load0 = tuple(sum(a <= k < b for a, b in intervals)
                      for k in range(1, n))
        load = tuple(x + 1 for x in load0)
        out[load] += weight

    # Distinct endpoint intervals [1,p] and [q,n].
    for p in range(2, n):
        for q in range(2, n):
            if p == q:
                continue
            remaining = tuple(x for x in range(2, n) if x not in (p, q))
            for M0 in matchings(remaining):
                intervals = tuple(sorted(tuple(sorted(e)) for e in M0))
                weight = two_root_forest_weight(intervals, p, q)
                load0 = tuple(sum(a <= k < b for a, b in intervals)
                              for k in range(1, n))
                load = tuple(
                    load0[k - 1] + int(k < p) + int(k >= q)
                    for k in range(1, n)
                )
                out[load] += weight
    return out


def main():
    for n in (4, 6, 8):
        direct = direct_left(n)
        rec = endpoint_recurrence(n)
        assert direct == rec, (n, direct, rec)
        print(
            f"PASS n={n}: load_types={len(direct)}, "
            f"left_copies={sum(direct.values())}"
        )
    print("PASS exact two-endpoint rooted-forest recurrence through eight ports")


if __name__ == "__main__":
    main()
