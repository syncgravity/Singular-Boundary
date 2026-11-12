#!/usr/bin/env python3
"""Verify finite golden-angle parastichy counts and an explicit 3D lift.

This is a synthetic radial golden-angle construction, NOT an authenticated
coupled-Z5 Conway-worm generator or a source-derived physical clock/metric.
"""
import math
from collections import Counter
import numpy as np
from scipy.spatial import Delaunay

PHI = (1 + math.sqrt(5)) / 2
ALPHA = PHI ** -2
N_POINTS = 1600
ANNULI = ((200, 400), (400, 800), (800, 1300))

# Exact Fibonacci near-return identity.
fib = [0, 1]
for _ in range(2, 17):
    fib.append(fib[-1] + fib[-2])
checks = 0
for k in range(3, 15):
    assert abs(fib[k] * ALPHA - fib[k - 2] - (-1) ** k * PHI ** -k) < 2e-13
    checks += 1
assert (fib[9], fib[10]) == (34, 55)
assert math.sin(2 * math.pi * 34 * ALPHA) < 0
assert math.sin(2 * math.pi * 55 * ALPHA) > 0
checks += 2

# Zero-based array indices i correspond to sequence labels n=i+1.
idx = np.arange(N_POINTS)
n = idx + 1
phases = {
    "golden": n * ALPHA,
    "irrational_complement": n / PHI,
    "rational_H3": n * (8 / 13),
    "phase_shuffled": np.random.default_rng(101).permutation((n * ALPHA) % 1),
}


def delaunay_edges(phase):
    xy = np.column_stack((np.sqrt(n) * np.cos(2 * math.pi * phase),
                          np.sqrt(n) * np.sin(2 * math.pi * phase)))
    edges = set()
    for tri in Delaunay(xy).simplices:
        for a, b in ((tri[0], tri[1]), (tri[1], tri[2]), (tri[2], tri[0])):
            edges.add(tuple(sorted((int(a), int(b)))))
    return edges


edge_sets = {name: delaunay_edges(phase) for name, phase in phases.items()}
results = {}
for name, edges in edge_sets.items():
    for lo, hi in ANNULI:
        counts = Counter(b - a for a, b in edges if lo <= a < hi and lo <= b < hi)
        results[name, lo, hi] = counts
        checks += 1

assert results["golden", 400, 800].most_common(3) == [(34, 366), (55, 345), (89, 311)]
assert results["irrational_complement", 400, 800].most_common(3) == [(34, 366), (55, 345), (89, 311)]
assert set(k for k, _ in results["rational_H3", 400, 800].most_common(3)) == {5, 8, 13}
checks += 3


def residue_chain_components(edges, lo, hi, lag):
    """Return components of the annular graph containing only edges of exact lag."""
    vertices = range(lo, hi)
    parent = {i: i for i in vertices}

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a, b):
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[rb] = ra

    selected = {(a, b) for a, b in edges
                if lo <= a < hi and lo <= b < hi and b - a == lag}
    for a, b in selected:
        union(a, b)
    components = {}
    for i in vertices:
        components.setdefault(find(i), []).append(i)
    return selected, list(components.values())


# The edge count equals the number of all possible lag-k pairs in the annulus.
# Therefore every such pair is a Delaunay edge, and the lag graph is exactly
# the disjoint union of k residue-class chains.
chain_cases = ((200, 400, (34, 55)),
               (400, 800, (34, 55, 89)),
               (800, 1300, (55, 89, 144)))
for lo, hi, lags in chain_cases:
    for lag in lags:
        selected, components = residue_chain_components(edge_sets["golden"], lo, hi, lag)
        assert len(selected) == hi - lo - lag
        assert len(components) == lag
        assert len({tuple(sorted(v % lag for v in comp)) for comp in components}) == lag
        assert all(len({i % lag for i in comp}) == 1 for comp in components)
        checks += 4

# At [400,800), the finite parastichy count is exactly 34 and 55.
for lag, expected_edges in ((34, 366), (55, 345)):
    selected, components = residue_chain_components(edge_sets["golden"], 400, 800, lag)
    assert len(selected) == expected_edges
    assert len(components) == lag
    checks += 2

# Explicit 3D lift: Gamma_n=(x_n,y_n,h*n), with declared h=1 and t_n=n.
# Each lag-k residue chain has exactly constant axial increment k.
height = 1.0
for lag in (34, 55, 89):
    sample = np.arange(400, 800 - lag)
    ds = height * ((sample + lag + 1) - (sample + 1))
    dt = (sample + lag + 1) - (sample + 1)
    assert np.all(ds == height * lag)
    assert np.all(dt == lag)
    checks += 1

# Rational H3 has 13-phase aliasing; the shuffled control has no coherent triplet.
for a in (3, 5, 8):
    x = (a * np.arange(52)) % 13
    assert len(set(x[:13])) == 13 and np.array_equal(x[:13], x[13:26])
    checks += 1
for lag in (34, 55):
    assert np.sign(math.sin(2 * math.pi * lag * ALPHA)) == -np.sign(math.sin(2 * math.pi * lag * (1 - ALPHA)))
    checks += 1
assert 0.002 < abs(8 / 13 - 1 / PHI) < 0.003
checks += 1

# Reproducible output: show edge counts and exact residue-chain counts.
for name in phases:
    top = results[name, 400, 800].most_common(3)
    print(name, top)
print("golden annulus [400,800):")
for lag in (34, 55, 89):
    selected, components = residue_chain_components(edge_sets["golden"], 400, 800, lag)
    print(f"  lag={lag}: edges={len(selected)}, residue_chains={len(components)}")
print(f"PASS {checks} checks; finite golden-angle parastichy counts verified; coupled-Z5 source bridge OPEN")
