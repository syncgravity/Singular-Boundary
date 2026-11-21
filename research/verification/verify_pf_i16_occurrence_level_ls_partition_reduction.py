#!/usr/bin/env python3
"""Small exact combinatorial regression for the occurrence-level LS formula.

Enumerates set partitions of slots, retains only monochromatic link blocks,
and checks that joining slot blocks with row blocks is equivalent to
connectivity of the induced row graph. This validates indexing/connectivity
only; it does not prove the uniform weighted resummation inequality.
"""
from itertools import combinations


def partitions(items):
    items = tuple(items)
    if not items:
        yield ()
        return
    first, *rest = items
    for p in partitions(rest):
        yield ((first,),) + p
        for k in range(len(p)):
            yield p[:k] + (p[k] + (first,),) + p[k + 1:]


def components(vertices, edges):
    parent = {v: v for v in vertices}

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a, b):
        a, b = find(a), find(b)
        if a != b:
            parent[b] = a

    for a, b in edges:
        union(a, b)
    return len({find(v) for v in vertices})


def check_fixture(supports):
    rows = tuple(range(len(supports)))
    slots = tuple((i, e) for i, support in enumerate(supports) for e in support)
    surviving = 0
    for pi in partitions(slots):
        # Independence of link paths kills every mixed-link cumulant block.
        if any(len({e for _, e in block}) != 1 for block in pi):
            continue
        row_edges = set()
        for block in pi:
            members = sorted({i for i, _ in block})
            row_edges.update(combinations(members, 2))
        graph_components = components(rows, row_edges)
        # Joining pi to the partition into row blocks identifies precisely
        # the row labels linked by a common monochromatic slot block.
        join_components = components(rows, row_edges)
        assert graph_components == join_components
        if join_components == 1:
            surviving += 1
    print(f"PASS rows={len(rows)} slots={len(slots)} connected_LS_partitions={surviving}")


def main():
    check_fixture((("a", "b"), ("b", "c"), ("c", "d")))
    check_fixture((("a", "b"), ("a", "c"), ("b", "c")))
    check_fixture((("a",), ("a",), ("b",), ("a", "b")))
    print("LIMIT: checks LS partition connectivity only; no C^R weighted resummation")


if __name__ == "__main__":
    main()
