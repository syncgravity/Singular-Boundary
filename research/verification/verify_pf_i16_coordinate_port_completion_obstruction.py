#!/usr/bin/env python3
"""Exact finite incidence witness: global port subdivision can leave support."""
from itertools import combinations

supports = {
    1: frozenset({"e"}),
    2: frozenset({"f"}),
    3: frozenset({"e", "g"}),
    4: frozenset({"f", "g"}),
}

def supported(i, j):
    return bool(supports[i] & supports[j])

# One link-labelled path for each non-singleton block.
labelled_edges = {
    (1, 3): "e",
    (2, 4): "f",
    (3, 4): "g",
}
assert all(label in supports[i] & supports[j]
           for (i, j), label in labelled_edges.items())

# The union is exactly the connected support path 1--3--4--2.
vertices = set(supports)
assert len(labelled_edges) == len(vertices) - 1
adj = {v: set() for v in vertices}
for i, j in labelled_edges:
    adj[i].add(j)
    adj[j].add(i)
seen = set()
stack = [1]
while stack:
    v = stack.pop()
    if v not in seen:
        seen.add(v)
        stack.extend(adj[v] - seen)
assert seen == vertices
assert {tuple(sorted(e)) for e in labelled_edges} == {(1, 3), (2, 4), (3, 4)}

# Port-completing connector 2 into parent edge (1,3) creates unsupported (1,2).
assert 1 < 2 < 3
assert not supported(1, 2)
assert supported(1, 3)
assert supported(2, 4)

# All row supports have size <= 2, hence satisfy the degree-eight cap.
assert max(map(len, supports.values())) <= 8

print("PASS: connected link-labelled support tree; naive interval port subdivision creates a non-support edge")
