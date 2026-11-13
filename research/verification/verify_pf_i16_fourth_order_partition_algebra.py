#!/usr/bin/env python3
"""Finite-dimensional regression checks for the PF-I16 fourth-order algebra.

The proof itself is the self-adjoint reduced-resolvent calculation in the
accompanying theorem record. This script checks the 36-term partition counts
and compares the recursion formula with the three-pair-channel formula on
random finite reversible generators.
"""
from itertools import combinations
import numpy as np

LABELS = ("i", "j", "k", "l")
PARTITIONS = (
    (("i", "j"), ("k", "l")),
    (("i", "k"), ("j", "l")),
    (("i", "l"), ("j", "k")),
)

def canonical_pair_partition(pair1, pair2):
    a, b = tuple(sorted(pair1)), tuple(sorted(pair2))
    return tuple(sorted((a, b)))

nested_counts = {canonical_pair_partition(*p): 0 for p in PARTITIONS}
for m in LABELS:
    for a in LABELS:
        if a == m:
            continue
        c, d = [x for x in LABELS if x not in (m, a)]
        part = canonical_pair_partition((m, a), (c, d))
        nested_counts[part] += 2

energy_counts = {canonical_pair_partition(*p): 0 for p in PARTITIONS}
for m in LABELS:
    remaining = [x for x in LABELS if x != m]
    for a, b in combinations(remaining, 2):
        c = next(x for x in remaining if x not in (a, b))
        part = canonical_pair_partition((a, b), (m, c))
        energy_counts[part] += 1

assert len(nested_counts) == 3
assert set(nested_counts.values()) == {8}
assert sum(nested_counts.values()) == 24
assert set(energy_counts.values()) == {4}
assert sum(energy_counts.values()) == 12
assert sum(nested_counts.values()) + sum(energy_counts.values()) == 36

def laplacian(n, rng):
    w = rng.uniform(0.2, 1.4, size=(n, n))
    w = np.triu(w, 1)
    w = w + w.T
    return np.diag(w.sum(axis=1)) - w

def centered(x):
    return x - np.mean(x)

def check_random_generator(seed):
    rng = np.random.default_rng(seed)
    n = 7
    L = laplacian(n, rng)
    G = np.linalg.pinv(L, rcond=1e-12)
    rs = {x: centered(rng.normal(size=n)) for x in LABELS}
    A = {x: G @ rs[x] for x in LABELS}

    def mean(x):
        return float(np.mean(x))

    def B(pair):
        a, b = pair
        return G @ (rs[a] * A[b] + rs[b] * A[a])

    E2 = {}
    for a, b in combinations(LABELS, 2):
        E2[(a, b)] = -mean(rs[a] * A[b] + rs[b] * A[a])

    def e2(a, b):
        return E2[tuple(sorted((a, b)))]

    def b2(a, b):
        return B(tuple(sorted((a, b))))

    E4_rec = 0.0
    for m in LABELS:
        others = [x for x in LABELS if x != m]
        a, b, c = others
        rhs = (
            rs[a] * b2(b, c) + rs[b] * b2(a, c) + rs[c] * b2(a, b)
            + e2(a, b) * A[c] + e2(a, c) * A[b] + e2(b, c) * A[a]
        )
        u3 = G @ rhs
        E4_rec -= mean(rs[m] * u3)

    E4_pair = 0.0
    for (a, b), (c, d) in PARTITIONS:
        Qab = rs[a] * A[b] + rs[b] * A[a]
        Qcd = rs[c] * A[d] + rs[d] * A[c]
        GQcd = G @ Qcd
        channel = (
            mean(Qab * GQcd)
            + e2(a, b) * mean(A[c] * A[d])
            + e2(c, d) * mean(A[a] * A[b])
        )
        E4_pair -= 2.0 * channel

    assert abs(E4_rec - E4_pair) < 2e-9, (seed, E4_rec, E4_pair)

for seed in range(25):
    check_random_generator(seed)

print("PASS: 24 nested-resolvent monomials split 8 per pair partition")
print("PASS: 12 pair-energy monomials split 4 per pair partition")
print("PASS: total fourth-order expansion contains exactly 36 monomials")
print("PASS: recursion and three-channel formula agree on 25 random finite reversible generators")
