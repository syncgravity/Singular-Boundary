#!/usr/bin/env python3
"""Exact finite checks for the L2-gap/interlaced-block obstruction.

The infinite LPS family and its Ramanujan/girth properties are cited in the
companion audit. This script checks the graph-decoding identity on Petersen's
graph and verifies the asymptotic ratio from the LPS parameter inequalities.
It does not numerically construct LPS graphs.
"""
from itertools import combinations


def is_prime(n):
    if n < 2:
        return False
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True


def petersen_graph():
    # Outer 5-cycle 0..4, inner star 5..9, spokes i--i+5.
    edges = set()
    for i in range(5):
        edges.add(tuple(sorted((i, (i + 1) % 5))))
        edges.add(tuple(sorted((i + 5, ((i + 2) % 5) + 5)))
        edges.add((i, i + 5))
    adj = [set() for _ in range(10)]
    for a, b in edges:
        adj[a].add(b)
        adj[b].add(a)
    return adj


def connected(adj):
    seen = {0}
    stack = [0]
    while stack:
        u = stack.pop()
        for v in adj[u] - seen:
            seen.add(v)
            stack.append(v)
    return len(seen) == len(adj)


def has_odd_cycle(adj):
    color = {}
    for root in range(len(adj)):
        if root in color:
            continue
        color[root] = 0
        stack = [root]
        while stack:
            u = stack.pop()
            for v in adj[u]:
                if v not in color:
                    color[v] = 1 - color[u]
                    stack.append(v)
                elif color[v] == color[u]:
                    return True
    return False


def check_no_four_cycles(adj):
    # In particular, any two distinct neighbors of x have x as
    # their unique common neighbor.
    for u, v in combinations(range(len(adj)), 2):
        common = adj[u] & adj[v]
        assert len(common) <= 1, (u, v, common)


def check_decoding_identity(adj):
    d = len(adj[0])
    n = len(adj)
    assert all(len(row) == d for row in adj)
    assert connected(adj)
    assert has_odd_cycle(adj)
    check_no_four_cycles(adj)

    # Any balanced +/-1 labeling is admissible. For every middle vertex x,
    # ordered independent neighbors Y,Z satisfy:
    # E[h(Y,Z)|X_1=x] = (1 - 1/d) g(x).
    g = [1 if i < n // 2 else -1 for i in range(n)]
    assert sum(g) == 0
    for x in range(n):
        total = 0
        for y in adj[x]:
            for z in adj[x]:
                if y != z:
                    common = adj[y] & adj[z]
                    assert common == {x}
                    total += g[next(iter(common))]
        conditional_mean = total / (d * d)
        assert abs(conditional_mean - (1 - 1 / d) * g[x]) < 1e-12

    covariance = 1 - 1 / d
    assert abs(covariance - (d - 1) / d) < 1e-15
    return covariance


def check_lps_parameter_fixtures():
    # p,q are distinct primes, both 1 mod 4; q>p^2; (p/q)=1.
    fixtures = [(5, 29), (13, 173), (17, 293), (29, 857), (37, 1373), (41, 1697)]
    ratios = []
    for p, q in fixtures:
        assert is_prime(p) and is_prime(q)
        assert p % 4 == 1 and q % 4 == 1 and p != q
        assert q > p * p
        assert pow(p, (q - 1) // 2, q) == 1
        d = p + 1
        theta_upper = 2 * (p ** 0.5) / d
        covariance = p / d
        ratio_lower = covariance / (2 * theta_upper)
        assert abs(ratio_lower - (p ** 0.5) / 4) < 1e-12
        ratios.append(ratio_lower)
    assert all(ratios[i] < ratios[i + 1] for i in range(len(ratios) - 1))


def main():
    adj = petersen_graph()
    covariance = check_decoding_identity(adj)
    check_lps_parameter_fixtures()
    print(f"PASS Petersen no-four-cycle decoding identity: covariance={covariance:.6f}")
    print("PASS LPS parameter conditions and divergent covariance/port-weight ratio")
    print("LIMIT: L2-gap obstruction only; uniform bridge-Doeblin heat-kernel case remains open")


if __name__ == "__main__":
    main()
