#!/usr/bin/env python3
"""Simultaneous two-edge flexibility test for PF-I16 leaf-last transport.

A requirement is a challenger edge (source, tree) already certified by the
single-edge alternating-reroute test. For two requirements with distinct
sources and distinct trees, force both edges, delete their endpoints, and
compute an exact maximum matching on the residual bipartite graph.

All pairs are checked at n=4 and n=6. At n=8 the pair universe is too large
for exhaustive CI; a deterministic, evenly spread set of pair ranks is
checked and the exact scope is printed. This is a finite diagnostic only.
"""
from collections import defaultdict
from verify_pf_i16_global_alternating_reroute import hopcroft_karp
from verify_pf_i16_source_dependent_leaf_peeling import (
    canonical_leaf, sources, candidate_outputs,
)


def saturated_after_forcing(rows, x, T, y, U):
    if x == y or T == U or T not in rows[x] or U not in rows[y]:
        return False
    residual = []
    for i, row in enumerate(rows):
        if i in (x, y):
            continue
        residual.append(set(row) - {T, U})
    ml, _, _ = hopcroft_karp(residual)
    return sum(v >= 0 for v in ml) == len(residual)


def build_case(n):
    rows = []
    target_sources = defaultdict(list)
    for intervals, tau in sources(n):
        leaf = canonical_leaf(intervals, tau)
        row = candidate_outputs(intervals, tau, forced_last=leaf)
        rows.append(row)
        for T in row:
            target_sources[T].append(len(rows) - 1)
    ml, mr, right = hopcroft_karp(rows)
    assert all(v >= 0 for v in ml), (n, "base matching not left-saturating")
    matched = {i: right[ml[i]] for i in range(len(rows))}
    owner = {right[j]: i for j, i in enumerate(mr) if i >= 0}
    requirements = sorted(
        (x, T)
        for T, xs in target_sources.items()
        for x in xs if owner.get(T) != x
    )
    return rows, requirements


def unrank_pair(rank, n):
    # Lexicographic unranking of 0 <= i < j < n.
    lo, hi = 0, n - 1
    while lo < hi:
        mid = (lo + hi + 1) // 2
        before = mid * (2 * n - mid - 1) // 2
        if before <= rank:
            lo = mid
        else:
            hi = mid - 1
    i = lo
    before = i * (2 * n - i - 1) // 2
    return i, i + 1 + (rank - before)


def selected_pair_ranks(total, cap):
    if total <= cap:
        return range(total)
    # Midpoint-spaced deterministic ranks cover the full lexicographic range.
    return sorted({((2*k + 1) * total) // (2 * cap) for k in range(cap)})


def run(n, cap):
    rows, req = build_case(n)
    total = len(req) * (len(req) - 1) // 2
    ranks = selected_pair_ranks(total, cap)
    tested = admissible = saturated = 0
    same_fiber_not_available = 0
    first_failure = None
    for rank in ranks:
        i, j = unrank_pair(rank, len(req))
        x, T = req[i]
        y, U = req[j]
        if x == y or T == U:
            continue
        tested += 1
        ok = saturated_after_forcing(rows, x, T, y, U)
        if ok:
            saturated += 1
        elif first_failure is None:
            first_failure = (x, T, y, U)
    scope = "exhaustive" if len(ranks) == total else "deterministic-spread"
    print(f"n={n}: sources={len(rows)}, single_edge_requirements={len(req)}, "
          f"pair_universe={total}, pair_tests={tested}, scope={scope}")
    print(f"  two_edge_constraints_satisfied={saturated}/{tested}, "
          f"failures={tested-saturated}")
    if first_failure:
        x, T, y, U = first_failure
        print(f"  first_failure=(source {x}, tree {T}) + (source {y}, tree {U})")
    return saturated == tested


def main():
    ok = True
    ok &= run(4, 10**9)
    ok &= run(6, 10**9)
    ok &= run(8, 4096)
    print("Simultaneous two-edge flexibility:", "PASS" if ok else "FAIL")
    if not ok:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
