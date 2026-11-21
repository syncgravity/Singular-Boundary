#!/usr/bin/env python3
"""Expose the actual terminal exchange-class sources at n=4,6,8.

This is a structural diagnostic: unlike the aggregate SCC census, it prints
which (matching, overlap-tree) sources occupy the unique sink SCC.  The aim is
to identify a recursive description of the conjectural terminal class.
"""
from collections import Counter, defaultdict
from array import array

from verify_pf_i16_n10_multivalued_pi_exchange_scc import build_rows
from verify_pf_i16_global_alternating_reroute import hopcroft_karp
from verify_pf_i16_source_dependent_leaf_peeling import sources


def terminal_members(rows, ml, mr, right):
    n = len(rows)
    owner = {right[j]: i for j, i in enumerate(mr) if i >= 0}
    adj = [array("I") for _ in range(n)]
    rev = [array("I") for _ in range(n)]
    free = {right[j] for j, i in enumerate(mr) if i < 0}
    for x, row in enumerate(rows):
        for t in row:
            y = owner.get(t)
            if y is not None and y != x:
                adj[x].append(y)
                rev[y].append(x)
    seen = bytearray(n)
    order = []
    for root in range(n):
        if seen[root]:
            continue
        seen[root] = 1
        stack = [(root, 0)]
        while stack:
            v, k = stack[-1]
            if k < len(adj[v]):
                w = adj[v][k]
                stack[-1] = (v, k + 1)
                if not seen[w]:
                    seen[w] = 1
                    stack.append((w, 0))
            else:
                order.append(v)
                stack.pop()
    comp = [-1] * n
    members = []
    for root in reversed(order):
        if comp[root] >= 0:
            continue
        cid = len(members)
        group = []
        comp[root] = cid
        stack = [root]
        while stack:
            v = stack.pop()
            group.append(v)
            for w in rev[v]:
                if comp[w] < 0:
                    comp[w] = cid
                    stack.append(w)
        members.append(group)
    outgoing = [set() for _ in members]
    for x in range(n):
        for y in adj[x]:
            if comp[x] != comp[y]:
                outgoing[comp[x]].add(comp[y])
    sinks = [i for i, out in enumerate(outgoing) if not out]
    assert len(sinks) == 1, (len(sinks), [len(members[i]) for i in sinks])
    sid = sinks[0]
    free_neighbors = {t for x in members[sid] for t in rows[x] if t in free}
    assert free_neighbors
    return sorted(members[sid]), len(members), len(free_neighbors)


def run(n):
    rows, _, _ = build_rows(n)
    ml, mr, right = hopcroft_karp(rows)
    assert sum(v >= 0 for v in ml) == len(rows)
    terminal, scc_count, free_count = terminal_members(rows, ml, mr, right)
    src = list(sources(n))
    assert len(src) == len(rows)
    selected = [src[i] for i in terminal]
    matching_hist = Counter(intervals for intervals, tau in selected)
    tau_hist = Counter(tau for intervals, tau in selected)
    print(f"n={n} sources={len(rows)} scc_count={scc_count} "
          f"terminal_size={len(terminal)} free_targets={free_count}")
    print(f"  terminal_matching_count={len(matching_hist)} "
          f"terminal_overlap_tree_count={len(tau_hist)}")
    print(f"  terminal_sources_per_matching={dict(sorted(Counter(matching_hist.values()).items()))}")
    for intervals, tau in selected:
        print(f"  source matching={intervals} overlap_tree={tau}")


if __name__ == "__main__":
    for order in (4, 6, 8):
        run(order)
