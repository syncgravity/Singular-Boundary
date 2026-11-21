#!/usr/bin/env python3
"""Finite regression for decorated-tree transport through LS partitions.

Checks only the finite graph statement: LS-connected current clusters plus
one internal tree per cluster produce a spanning tree on original labels.
It does not verify any analytic cumulant, semigroup, or projective estimate.
"""
from fractions import Fraction
from itertools import product


def partitions(items):
    items = tuple(items)
    if not items:
        yield ()
        return
    first, *rest = items
    for p in partitions(rest):
        yield (frozenset((first,)),) + p
        for j, block in enumerate(p):
            q = list(p)
            q[j] = block | {first}
            yield tuple(q)


def canonical_partitions(items):
    unique = set()
    for p in partitions(items):
        unique.add(tuple(sorted(tuple(sorted(b)) for b in p)))
    return [tuple(frozenset(b) for b in p) for p in sorted(unique)]


def find(parent, x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x


def union(parent, a, b):
    a, b = find(parent, a), find(parent, b)
    if a != b:
        parent[b] = a
        return True
    return False


def connected(parent):
    return len({find(parent, x) for x in range(len(parent))}) <= 1


def run_fixture(name, clusters, internal_edges, slots_by_link, ratio=Fraction(1, 2)):
    # Original label -> current cluster.
    label_to_cluster = {}
    for c, labels in enumerate(clusters):
        for label in labels:
            assert label not in label_to_cluster
            label_to_cluster[label] = c
    labels = sorted(label_to_cluster)
    assert labels == list(range(len(labels)))

    # Internal decorations must be trees on their respective clusters.
    internal_parent = list(range(len(labels)))
    for u, v, _link, _tu, _tv in internal_edges:
        assert label_to_cluster[u] == label_to_cluster[v]
        assert union(internal_parent, u, v)
    for c, members in enumerate(clusters):
        assert len(members) == 1 or len({find(internal_parent, x) for x in members}) == 1
    assert len(internal_edges) == len(labels) - len(clusters)

    links = sorted(slots_by_link)
    choices = [canonical_partitions(range(len(slots_by_link[e]))) for e in links]
    checked = connected_cases = 0

    for local_parts in product(*choices):
        checked += 1
        # LS join condition on current cluster labels.
        cluster_parent = list(range(len(clusters)))
        block_paths = []
        for e, parts in zip(links, local_parts):
            slots = slots_by_link[e]
            for block in parts:
                ordered = sorted(block, key=lambda j: (slots[j][1], slots[j][0]))
                path = []
                for j in range(len(ordered) - 1):
                    a, b = ordered[j], ordered[j + 1]
                    la, ta = slots[a]
                    lb, tb = slots[b]
                    ca, cb = label_to_cluster[la], label_to_cluster[lb]
                    if ca != cb:
                        union(cluster_parent, ca, cb)
                    path.append((la, lb, ratio ** abs(ta - tb)))
                block_paths.extend(path)

        if len({find(cluster_parent, c) for c in range(len(clusters))}) != 1:
            continue
        connected_cases += 1

        # Select a spanning tree in the projected graph on current clusters.
        outer_parent = list(range(len(clusters)))
        outer_edges = []
        for u, v, weight in sorted(block_paths, key=lambda x: x[2], reverse=True):
            cu, cv = label_to_cluster[u], label_to_cluster[v]
            if cu != cv and union(outer_parent, cu, cv):
                outer_edges.append((u, v, weight))
        assert len(outer_edges) == len(clusters) - 1
        assert connected(outer_parent)

        # Internal trees + selected outer edges must be a tree on original labels.
        full_parent = list(range(len(labels)))
        all_edges = list(internal_edges) + [
            (u, v, "outer", None, None) for u, v, _w in outer_edges
        ]
        for u, v, *_ in all_edges:
            assert union(full_parent, u, v), (name, "cycle", all_edges)
        assert len(all_edges) == len(labels) - 1
        assert connected(full_parent)

        # Every selected outer edge is a real cross-cluster common-link port pair.
        for u, v, _w in outer_edges:
            assert label_to_cluster[u] != label_to_cluster[v]
            assert any(
                any(slot_u[0] == u for slot_u in slots)
                and any(slot_v[0] == v for slot_v in slots)
                for slots in slots_by_link.values()
            )

    assert connected_cases > 0
    print(
        f"PASS {name}: {checked} partition combinations, "
        f"{connected_cases} LS-connected; decorated union is a spanning tree"
    )


def main():
    run_fixture(
        "three-cluster-interlaced",
        clusters=[(0, 1), (2,), (3, 4)],
        internal_edges=[
            (0, 1, "old-a", 0, 3),
            (3, 4, "old-b", 2, 5),
        ],
        slots_by_link={
            "a": [(0, 0), (2, 4), (3, 1)],
            "b": [(1, 6), (2, 2), (4, 7)],
        },
    )
    run_fixture(
        "four-cluster-cycle",
        clusters=[(0,), (1, 2), (3,), (4, 5)],
        internal_edges=[
            (1, 2, "old-c", 0, 4),
            (4, 5, "old-d", 1, 6),
        ],
        slots_by_link={
            "a": [(0, 0), (1, 5), (3, 2)],
            "b": [(2, 1), (3, 7), (4, 3)],
            "c": [(0, 6), (4, 0), (5, 4)],
        },
    )
    print("LIMIT: finite decorated-connectivity regression only")


if __name__ == "__main__":
    main()
