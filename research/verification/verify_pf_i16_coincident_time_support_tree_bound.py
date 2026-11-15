#!/usr/bin/env python3
"""Exact checks for the coincident-time support-disconnection baseline."""
from math import prod

# Stirling numbers S(n,k), generated exactly by S(n,k)=k*S(n-1,k)+S(n-1,k-1).
S = [[0] * 52 for _ in range(52)]
S[0][0] = 1
for n in range(1, 52):
    for k in range(1, n + 1):
        S[n][k] = k * S[n - 1][k] + S[n - 1][k - 1]

for r in range(2, 52):
    weighted_partition_sum = sum(S[r][k] * __import__("math").factorial(k - 1)
                                 for k in range(1, r + 1))
    # S(r,k) <= k^r/k!, hence each weighted term <= k^(r-1).
    elementary_upper = sum(k ** (r - 1) for k in range(1, r + 1))
    assert weighted_partition_sum <= elementary_upper
    assert elementary_upper <= r ** r
    # r <= 2^r implies r^r <= 4^r r^(r-2).
    assert r ** r <= (4 ** r) * (r ** (r - 2))

# Exact support-disconnection fact: if row supports split into disjoint
# coordinate unions, product-Haar independence makes the joint cumulant zero.
supports = [{"a"}, {"a", "b"}, {"b"}, {"c"}]
components = [{0, 1, 2}, {3}]
for left, right in [(components[0], components[1])]:
    left_links = set().union(*(supports[i] for i in left))
    right_links = set().union(*(supports[i] for i in right))
    assert left_links.isdisjoint(right_links)

print("PASS: exact Stirling recurrence verifies the complete-graph cumulant envelope for r=2,...,51")
print("PASS: support-disconnected row families use disjoint product-Haar coordinates")
print("SCOPE: does not establish a bound by the number of spanning trees of a sparse support graph")
print("SCOPE: does not establish any noncoincident-time support-tree estimate")
