#!/usr/bin/env python3
"""Exhaust the four-port guarded reverse-mark rank patterns.

A reverse mark J and old edge e use four distinct ordered ports.  The local
target must be one of S0, S1, S2; every target edge incident to J must be
exactly the corresponding local edge set; e must overlap J in positive
interval length; and e must not be reinserted by the local pattern.

This verifier checks the complete six-pair rank census, not source/fiber
canonical eligibility or any Hall condition.
"""
from itertools import combinations

VERTICES = (1, 2, 3, 4)
LOCAL_TREES = {
    "S0": frozenset({(1, 2), (2, 3), (2, 4)}),
    "S1": frozenset({(1, 2), (2, 3), (3, 4)}),
    "S2": frozenset({(1, 3), (2, 3), (3, 4)}),
}
EXPECTED = {
    (1, 3): ("S1", "S2"),
    (2, 3): ("S0", "S1", "S2"),
    (2, 4): ("S0", "S1"),
}


def overlaps(edge, mark):
    u, v = edge
    a, b = mark
    return max(u, a) < min(v, b)


def incident_edges(edges, mark):
    return frozenset(
        edge for edge in edges
        if edge[0] in mark or edge[1] in mark
    )


def enumerate_valid_marks():
    found = {}
    for mark in combinations(VERTICES, 2):
        old_edge = tuple(v for v in VERTICES if v not in mark)
        for name, local_tree in LOCAL_TREES.items():
            # In the four-port local target, exact incidence equality is
            # delta_T(J) == delta_{S_j}(J) == S_j.
            exact_incidence = incident_edges(local_tree, mark) == local_tree
            no_reinsertion = old_edge not in local_tree
            positive_overlap = overlaps(old_edge, mark)
            if exact_incidence and no_reinsertion and positive_overlap:
                found.setdefault(mark, []).append(name)
    return {mark: tuple(names) for mark, names in found.items()}


def main():
    found = enumerate_valid_marks()
    assert found == EXPECTED, (found, EXPECTED)

    # The outer pair would reinsert the middle edge in every pattern.
    outer = (1, 4)
    middle_edge = (2, 3)
    assert all(middle_edge in tree for tree in LOCAL_TREES.values())

    # The two extreme adjacent pairs have disjoint intervals from their
    # complementary old edge and therefore fail positive overlap.
    assert not overlaps((3, 4), (1, 2))
    assert not overlaps((1, 2), (3, 4))

    print("PASS exact guarded four-port reverse-mark rank census")
    for mark, names in sorted(found.items()):
        old_edge = tuple(v for v in VERTICES if v not in mark)
        print(f"  J={mark}, e={old_edge}, patterns={','.join(names)}")
    print("PASS excluded outer mark by no-reinsertion")
    print("PASS excluded extreme adjacent marks by disjoint intervals")


if __name__ == "__main__":
    main()
