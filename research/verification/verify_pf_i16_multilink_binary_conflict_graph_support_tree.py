#!/usr/bin/env python3
"""Exact multi-link matching/conflict-graph expansion for binary Markov rows."""
from fractions import Fraction as F
from itertools import combinations, product
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


def perfect_matchings(items):
    items = tuple(items)
    if not items:
        yield ()
        return
    a = items[0]
    for j in range(1, len(items)):
        b = items[j]
        for tail in perfect_matchings(items[1:j] + items[j + 1:]):
            yield ((a, b),) + tail


def components(n, edges):
    adj = [set() for _ in range(n)]
    for a, b, _e in edges:
        adj[a].add(b)
        adj[b].add(a)
    seen = set()
    out = []
    for v in range(n):
        if v in seen:
            continue
        stack = [v]
        seen.add(v)
        block = []
        while stack:
            x = stack.pop()
            block.append(x)
            for y in adj[x] - seen:
                seen.add(y)
                stack.append(y)
        out.append(tuple(sorted(block)))
    return tuple(out)


def intervals_overlap(a, b):
    return max(a[0], b[0]) < min(a[1], b[1])


def chromatic_linear_coefficient(n, edges, loops=False):
    if loops:
        return 0
    total = 0
    for p in all_parts(n):
        if any(u in b and v in b for b in p for u, v in edges):
            continue
        k = len(p)
        total += (-1) ** (k - 1) * factorial(k - 1)
    return total


def conflict_data(n, match_family):
    row_edges = []
    for e, matching in enumerate(match_family):
        row_edges.extend((a, b, e) for a, b in matching)
    comps = components(n, row_edges)
    comp_of = {v: i for i, c in enumerate(comps) for v in c}
    conflict_edges = set()
    loops = False
    all_intervals = []
    for e, matching in enumerate(match_family):
        ints = [(min(a, b), max(a, b), comp_of[a]) for a, b in matching]
        all_intervals.append(ints)
        for i, (a, b, ca) in enumerate(ints):
            for c, d, cb in ints[i + 1:]:
                if intervals_overlap((a, b), (c, d)):
                    if ca == cb:
                        loops = True
                    else:
                        conflict_edges.add(tuple(sorted((ca, cb))))
    return comps, conflict_edges, loops, all_intervals


def block_link_moment(block, ports, r):
    selected = sorted(set(block) & set(ports))
    if len(selected) % 2:
        return F(0)
    out = F(1)
    for k in range(0, len(selected), 2):
        a, b = selected[k], selected[k + 1]
        for j in range(a, b):
            out *= r[j]
    return out


def direct_cumulant(n, link_ports, link_r):
    total = F(0)
    for p in all_parts(n):
        k = len(p)
        term = F((-1) ** (k - 1) * factorial(k - 1))
        for block in p:
            for ports, r in zip(link_ports, link_r):
                term *= block_link_moment(block, ports, r)
        total += term
    return total


def expansion_cumulant(n, link_ports, link_r):
    match_lists = []
    for ports in link_ports:
        match_lists.append(list(perfect_matchings(ports)))
    total = F(0)
    configs = []
    for family in product(*match_lists):
        comps, hedges, loops, all_intervals = conflict_data(n, family)
        coeff = chromatic_linear_coefficient(len(comps), hedges, loops)
        weight = F(1)
        for matching, r in zip(family, link_r):
            for a, b in matching:
                for j in range(a, b):
                    weight *= r[j]
        total += coeff * weight
        configs.append((family, comps, hedges, loops, coeff, weight, all_intervals))
    return total, configs


def support_tree_from_config(n, family, all_intervals, link_ports):
    # For each connected interval-overlap component on each link, connect
    # consecutive endpoint rows. Their union is the per-configuration support graph.
    graph_edges = set()
    total_path_length = F(0)
    total_interval_length = F(0)
    for e, intervals in enumerate(all_intervals):
        # Build overlap components of matched intervals on this link.
        adj = [set() for _ in intervals]
        for i in range(len(intervals)):
            for j in range(i + 1, len(intervals)):
                if intervals_overlap(intervals[i][:2], intervals[j][:2]):
                    adj[i].add(j)
                    adj[j].add(i)
        seen = set()
        for i in range(len(intervals)):
            a, b, _ = intervals[i]
            total_interval_length += b - a
            if i in seen:
                continue
            stack = [i]
            seen.add(i)
            idxs = []
            while stack:
                x = stack.pop()
                idxs.append(x)
                for y in adj[x] - seen:
                    seen.add(y)
                    stack.append(y)
            vertices = sorted({z for x in idxs for z in intervals[x][:2]})
            for u, v in zip(vertices, vertices[1:]):
                graph_edges.add((u, v, e))
                total_path_length += v - u
    return graph_edges, total_path_length, total_interval_length


def connected(n, edges):
    return len(components(n, [(a, b, e) for a, b, e in edges])) == 1


def verify_patterns():
    patterns = [
        (3, [(0, 1), (1, 2)]),
        (4, [(0, 1, 2, 3), (0, 1, 2, 3)]),
        (4, [(0, 1, 2, 3), (0, 2)]),
        (5, [(0, 1, 2, 3), (1, 2, 3, 4)]),
    ]
    for n, ports in patterns:
        if any(len(p) % 2 for p in ports):
            continue
        link_r = [[F(1, 2) for _ in range(n - 1)] for _ in ports]
        direct = direct_cumulant(n, ports, link_r)
        expanded, configs = expansion_cumulant(n, ports, link_r)
        assert direct == expanded, (n, ports, direct, expanded)
        for family, comps, hedges, loops, coeff, weight, intervals in configs:
            if coeff:
                assert not loops
                assert connected(len(comps), [(a, b, 0) for a, b in hedges])
                graph_edges, path_len, interval_len = support_tree_from_config(
                    n, family, intervals, ports)
                assert connected(n, graph_edges), (n, ports, family, comps, hedges)
                assert path_len <= interval_len
                # Since all edge correlations are 1/2 per unit time, a spanning
                # tree extracted from this connected graph has weight >= config weight.
                assert weight <= F(1, 2) ** path_len


def main():
    verify_patterns()
    print("PASS exact multi-link matching/conflict-graph cumulant identity")
    print("PASS nonzero conflict coefficients imply connected row support")
    print("PASS interval-component path domination in tested incidence patterns")


if __name__ == "__main__":
    main()
