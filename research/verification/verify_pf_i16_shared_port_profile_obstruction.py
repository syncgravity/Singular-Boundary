#!/usr/bin/env python3
"""Finite audit of the PF-I16 shared-port exact-profile obstruction.

The theorem-level contradiction is in Section 11.2 of
PF_I16_JOINT_SPACETIME_CLUSTER_TREE_OPEN_GATE_2026_11_13.md.
This script independently enumerates all labeled spanning trees on the
five-vertex example and checks that none both contains the required
non-endpoint spatial witness edge and preserves the temporal cut profile.
"""
from itertools import combinations

LABELS = (0, 1, 2, 4, 7)
VERTICES = range(len(LABELS))
ALL_EDGES = tuple(combinations(VERTICES, 2))
TEMPORAL_FOREST = {(0, 2), (1, 3), (3, 4)}
SPATIAL_WITNESS = (2, 4)  # label edge (2, 7)


def cut_profile(edges):
    return tuple(
        sum(LABELS[a] <= q < LABELS[b] for a, b in edges)
        for q in range(LABELS[-1])
    )


def is_spanning_tree(edges):
    if len(edges) != len(LABELS) - 1:
        return False
    adjacency = [[] for _ in LABELS]
    for a, b in edges:
        adjacency[a].append(b)
        adjacency[b].append(a)
    seen = {0}
    stack = [0]
    while stack:
        v = stack.pop()
        for w in adjacency[v]:
            if w not in seen:
                seen.add(w)
                stack.append(w)
    return len(seen) == len(LABELS)


def main():
    target = cut_profile(TEMPORAL_FOREST)
    assert target == (1, 2, 1, 1, 1, 1, 1)

    trees = [
        set(candidate)
        for candidate in combinations(ALL_EDGES, len(LABELS) - 1)
        if is_spanning_tree(candidate)
    ]
    assert len(trees) == 125

    candidates_with_witness = [
        tree for tree in trees if SPATIAL_WITNESS in tree
    ]
    profile_preserving = [
        tree for tree in candidates_with_witness
        if cut_profile(tree) == target
    ]
    assert not profile_preserving

    # The proof-level obstruction: witness (2,7) crosses cuts 2 and 4.
    # Both target cut counts equal one, so it would be the unique crossing
    # edge at both cuts. Those cuts induce different bipartitions.
    assert target[2] == target[4] == 1
    print({
        "vertices": LABELS,
        "spanning_trees_enumerated": len(trees),
        "trees_containing_spatial_witness": len(candidates_with_witness),
        "profile_preserving_trees_with_witness": len(profile_preserving),
        "temporal_cut_profile": target,
        "result": "PASS: exact-profile shared-port completion is impossible",
    })


if __name__ == "__main__":
    main()
