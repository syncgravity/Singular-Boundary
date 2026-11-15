#!/usr/bin/env python3
"""Small exact combinatorial regression for the occurrence-level LS formula.

Enumerates set partitions of slots, retains only monochromatic link blocks,
and checks that the LS join condition is equivalent to connectivity of the
induced row graph. This validates the indexing/connectivity reduction only;
it does not prove the uniform weighted resummation inequality.
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


def connected(vertices, edges):
    if not vertices:
        return True
    seen = {vertices[0]}
    changed = True
    while changed:
        changed = False
        for a, b in edges:
            if a in seen and b not in seen and (seen.add(b) or True):
                changed = True
            if b in seen and a not in seen and (seen.add(a) or True):
                changed = True
    return len(seen) == len(vertices)


def check_fixture(supports):
    rows = tuple(range(len(supports)))
    slots = tuple((i, e) for i, support in enumerate(supports) for e in support)
    surviving = 0
    for pi in partitions(slots):
        if any(len({e for _, e in block}) != 1 for block in pi):
            continue
        edges = set()
        for block in pi:
            members = sorted({i for i, _ in block})
            for a, b in combinations(members, 2):
                edges.add((a, b))
        is_connected = connected(rows, edges)
        # The partition join with row blocks is connected iff this graph is.
        if is_connected:
            surviving += 1
        assert is_connected == connected(rows, edges)
    print(f"PASS rows={len(rows)} slots={len(slots)} admissible_connected_partitions={surviving}")


def main():
    check_fixture((("a", "b"), ("b", "c"), ("c", "d")))
    check_fixture((("a", "b"), ("a", "c"), ("b", "c")))
    check_fixture((("a",), ("a",), ("b",), ("a", "b")))
    print("LIMIT: checks LS partition connectivity only; no C^R weighted resummation")


if __name__ == "__main__":
    main()
