#!/usr/bin/env python3
"""Exact multi-link matching/conflict-graph expansion for binary Markov rows."""
from fractions import Fraction as F
from itertools import product
from math import factorial


def partitions(items):
    items = tuple(items)
    if not items:
        yield ()
        return
    x, *rest = items
    for p in partitions(rest):
        yield ((x,),) + p
        for j in range(len(p)):
            yield p[:j] + (tuple(sorted(p[j] + (x,))),) + p[j + 1:]


def canon(p):
    return tuple(sorted((tuple(sorted(b)) for b in p), key=lambda b: b[0]))


def all_parts(n):
    return sorted({canon(p) for p in partitions(range(n))})


def matchings(items):
    items = tuple(items)
    if not items:
        yield ()
        return
    a = items[0]
    for j in range(1, len(items)):
        b = items[j]
        for tail in matchings(items[1:j] + items[j + 1:]):
            yield ((a, b),) + tail


def components(n, edges):
    adj = [set() for _ in range(n)]
    for a, b, _e in edges:
        adj[a].add(b); adj[b].add(a)
    seen, out = set(), []
    for v in range(n):
        if v in seen: continue
        stack, block = [v], []
        seen.add(v)
        while stack:
            x = stack.pop(); block.append(x)
            for y in adj[x] - seen:
                seen.add(y); stack.append(y)
        out.append(tuple(sorted(block)))
    return tuple(out)


def chromatic_linear_coefficient(n, edges, loops=False):
    if loops: return 0
    total = 0
    for p in all_parts(n):
        if any(u in b and v in b for b in p for u, v in edges):
            continue
        k = len(p)
        total += (-1) ** (k - 1) * factorial(k - 1)
    return total


def conflict_data(n, family):
    row_edges = [(a, b, e) for e, M in enumerate(family) for a, b in M]
    comps = components(n, row_edges)
    comp_of = {v: i for i, C in enumerate(comps) for v in C}
    hedges, loops, intervals_all = set(), False, []
    for e, M in enumerate(family):
        ints = [(a, b, comp_of[a]) for a, b in M]
        intervals_all.append(ints)
        for k, (a, b, ca) in enumerate(ints):
            for c, d, cb in ints[k + 1:]:
                if max(a, c) < min(b, d):
                    if ca == cb: loops = True
                    else: hedges.add(tuple(sorted((ca, cb))))
    return comps, hedges, loops, intervals_all


def link_moment(block, ports, r):
    S = sorted(set(block) & set(ports))
    if len(S) % 2: return F(0)
    z = F(1)
    for k in range(0, len(S), 2):
        for j in range(S[k], S[k + 1]): z *= r[j]
    return z


def direct_cumulant(n, ports_by_link, r_by_link):
    total = F(0)
    for p in all_parts(n):
        k = len(p)
        term = F((-1) ** (k - 1) * factorial(k - 1))
        for B in p:
            for ports, r in zip(ports_by_link, r_by_link):
                term *= link_moment(B, ports, r)
        total += term
    return total


def expansion(n, ports_by_link, r_by_link):
    families = [list(matchings(P)) for P in ports_by_link]
    total, records = F(0), []
    for family in product(*families):
        comps, hedges, loops, ints = conflict_data(n, family)
        c = chromatic_linear_coefficient(len(comps), hedges, loops)
        w = F(1)
        for M, r in zip(family, r_by_link):
            for a, b in M:
                for j in range(a, b): w *= r[j]
        total += c * w
        records.append((family, comps, hedges, loops, c, w, ints))
    return total, records


def interval_path_graph(intervals_all):
    edges, total_path_cost, total_interval_cost = set(), 0, 0
    for e, ints in enumerate(intervals_all):
        adj = [set() for _ in ints]
        for i in range(len(ints)):
            for j in range(i + 1, len(ints)):
                a, b, _ = ints[i]; c, d, _ = ints[j]
                if max(a, c) < min(b, d):
                    adj[i].add(j); adj[j].add(i)
        seen = set()
        for i in range(len(ints)):
            a, b, _ = ints[i]
            total_interval_cost += b - a
            if i in seen: continue
            stack, ids = [i], []
            seen.add(i)
            while stack:
                x = stack.pop(); ids.append(x)
                for y in adj[x] - seen:
                    seen.add(y); stack.append(y)
            V = sorted({z for x in ids for z in ints[x][:2]})
            for u, v in zip(V, V[1:]):
                edges.add((u, v, e))
                total_path_cost += v - u
    return edges, total_path_cost, total_interval_cost


def is_connected(n, edges):
    return len(components(n, edges)) == 1


def verify():
    patterns = [
        (3, [(0, 1), (1, 2)]),
        (4, [(0, 1, 2, 3), (0, 1, 2, 3)]),
        (4, [(0, 1, 2, 3), (0, 2)]),
        (5, [(0, 1, 2, 3), (1, 2, 3, 4)]),
    ]
    for n, ports in patterns:
        rs = [[F(1, 2) for _ in range(n - 1)] for _ in ports]
        direct = direct_cumulant(n, ports, rs)
        expanded, records = expansion(n, ports, rs)
        assert direct == expanded, (n, ports, direct, expanded)
        for family, comps, hedges, loops, c, weight, ints in records:
            if c == 0: continue
            assert not loops
            assert is_connected(len(comps), [(a, b, 0) for a, b in hedges])
            graph, path_cost, interval_cost = interval_path_graph(ints)
            assert is_connected(n, graph), (n, ports, family, comps, hedges)
            assert path_cost <= interval_cost
            assert weight <= F(1, 2) ** path_cost


def main():
    verify()
    print("PASS exact multi-link matching/conflict-graph cumulant identity")
    print("PASS nonzero conflict coefficients imply connected row support")
    print("PASS interval-component path domination in tested incidence patterns")


if __name__ == "__main__":
    main()
