#!/usr/bin/env python3
"""Simultaneous three-edge flexibility test for PF-I16 leaf-last transport.

For a triple of individually flexible source-tree requirements with distinct
sources and distinct target trees, force all three edges and ask whether the
remaining bipartite graph still has a matching saturating every remaining
source. This is an exact residual matching test for each tested triple.

The n=4 universe is exhaustive; n=6 and n=8 use deterministic spread samples.
This is diagnostic evidence only, not an all-orders exchange theorem.
"""
from collections import defaultdict
from verify_pf_i16_global_alternating_reroute import hopcroft_karp
from verify_pf_i16_source_dependent_leaf_peeling import (
    canonical_leaf, sources, candidate_outputs,
)


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
    owner = {right[j]: i for j, i in enumerate(mr) if i >= 0}
    requirements = sorted(
        (x, T)
        for T, xs in target_sources.items()
        for x in xs if owner.get(T) != x
    )
    return rows, requirements


def unrank_combination(rank, n, k):
    """Lexicographic unranking among k-subsets of range(n)."""
    result, lower = [], 0
    for remaining in range(k, 0, -1):
        for value in range(lower, n - remaining + 1):
            block = comb(n - value - 1, remaining - 1)
            if rank < block:
                result.append(value)
                lower = value + 1
                break
            rank -= block
    return tuple(result)


def comb(n, k):
    if k < 0 or k > n:
        return 0
    k = min(k, n-k)
    value = 1
    for i in range(1, k+1):
        value = value * (n-k+i) // i
    return value


def selected_ranks(total, cap):
    if total <= cap:
        return range(total)
    return sorted({((2*i + 1) * total) // (2*cap) for i in range(cap)})


def saturated_after_forcing(rows, forced):
    sources = [x for x, _ in forced]
    targets = [T for _, T in forced]
    if len(set(sources)) != len(sources) or len(set(targets)) != len(targets):
        return None
    residual = [
        set(row) - set(targets)
        for i, row in enumerate(rows) if i not in set(sources)
    ]
    ml, _, _ = hopcroft_karp(residual)
    return sum(v >= 0 for v in ml) == len(residual)


def run(n, cap):
    rows, req = build_case(n)
    total = comb(len(req), 3)
    tested = satisfied = 0
    first_failure = None
    for rank in selected_ranks(total, cap):
        idx = unrank_combination(rank, len(req), 3)
        forced = [req[i] for i in idx]
        if len({x for x, _ in forced}) != 3 or len({T for _, T in forced}) != 3:
            continue
        tested += 1
        if saturated_after_forcing(rows, forced):
            satisfied += 1
        elif first_failure is None:
            first_failure = forced
    scope = "exhaustive" if total <= cap else "deterministic-spread"
    print(f"n={n}: sources={len(rows)}, single_edge_requirements={len(req)}, "
          f"triple_universe={total}, triple_tests={tested}, scope={scope}")
    print(f"  three_edge_constraints_satisfied={satisfied}/{tested}, "
          f"failures={tested-satisfied}")
    if first_failure:
        print(f"  first_failure={first_failure}")
    return satisfied == tested


def main():
    ok = True
    ok &= run(4, 10**9)
    ok &= run(6, 4096)
    ok &= run(8, 4096)
    print("Simultaneous three-edge flexibility:", "PASS" if ok else "FAIL")
    if not ok:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
