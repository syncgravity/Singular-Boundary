#!/usr/bin/env python3
"""Exact reciprocal reverse-mark degree diagnostic for PF-I16 cut blocks.

For each fiber F=(parent source, deleted interval), construct its complete
same-first-overcrowded-cut retained row N_k(F). For each target T, count
r_k(T) across ALL fibers in that block, including crossing and noncrossing
deleted intervals. Then compute q(F)=sum_{T in N_k(F)}1/r_k(T) and compare
against exact split demand delta(F).
"""
from collections import defaultdict, Counter
from fractions import Fraction
from verify_pf_i16_source_dependent_leaf_peeling import (
    sources, parent_data, inverse_last_switch, compress_tree, canonical_leaf,
)
from verify_pf_i16_local_switch_fractional_transport import candidate_outputs


def nonroot_leaves(intervals, tau):
    degree = [0] * len(intervals)
    for a, b in tau:
        degree[a] += 1
        degree[b] += 1
    root = next(i for i, I in enumerate(intervals) if I[0] == 1)
    return [i for i, d in enumerate(degree) if d == 1 and i != root]


def first_source_cut(intervals, n):
    loads = [sum(a <= k < b for a, b in intervals) for k in range(1, n)]
    return next((k for k in range(1, n, 2) if loads[k-1] >= 3), None)


def first_target_cut(tree, n):
    loads = [sum(a <= k < b for a, b in tree) for k in range(1, n)]
    return next((k for k in range(1, n, 2) if loads[k-1] >= 2), None)


def run(n, expected_sources):
    fibers = {}
    source_classes = Counter()
    source_count = 0
    for intervals, tau in sources(n):
        source_count += 1
        k = first_source_cut(intervals, n)
        source_classes[k] += 1
        if k is None:
            continue
        leaves = nonroot_leaves(intervals, tau)
        assert leaves
        d = len(leaves)
        for leaf in leaves:
            J = intervals[leaf]
            parent = parent_data(intervals, tau, leaf)
            key = (parent, J, k)
            if key not in fibers:
                fibers[key] = {
                    "representative": (intervals, tau, leaf),
                    "demand": Fraction(0),
                    "children": 0,
                }
            item = fibers[key]
            item["demand"] += Fraction(1, d)
            item["children"] += 1
        if source_count % 5000 == 0:
            print(f"n={n} enumerated_sources={source_count} fibers={len(fibers)}",
                  flush=True)

    assert source_count == expected_sources, (n, source_count, expected_sources)
    parent_target_cache = {}
    rows = {}
    target_reverse_degree = Counter()
    cut_fiber_counts = Counter()
    cut_incidence_counts = Counter()
    empty_rows = []

    for idx, (key, item) in enumerate(fibers.items(), 1):
        parent, J, k = key
        if parent not in parent_target_cache:
            pi, pt = parent
            if len(pi) == 1:
                parent_target_cache[parent] = {((1, 2),)}
            else:
                pl = canonical_leaf(pi, pt)
                parent_target_cache[parent] = candidate_outputs(
                    pi, pt, forced_last=pl
                )
        allowed_parent_targets = parent_target_cache[parent]
        intervals, tau, leaf = item["representative"]
        raw = candidate_outputs(intervals, tau, forced_last=leaf)
        row = set()
        for T in raw:
            if first_target_cut(T, n) != k:
                continue
            inv = inverse_last_switch(T, J, n)
            assert len(inv) == 1, (n, key, T, inv)
            P = compress_tree(next(iter(inv)), set(J), n)
            if P in allowed_parent_targets:
                row.add(T)
        assert row, (n, "empty retained same-cut fiber", key,
                     item["children"], len(raw))
        rows[key] = row
        cut_fiber_counts[k] += 1
        cut_incidence_counts[k] += len(row)
        for T in row:
            target_reverse_degree[(k, T)] += 1
        if idx % 2000 == 0:
            print(f"n={n} processed_fibers={idx}/{len(fibers)} "
                  f"target_keys={len(target_reverse_degree)}", flush=True)

    # Reciprocal-degree allocation. Degrees include every eligible fiber in
    # the cut block; no crossing/noncrossing subfamily restriction is used.
    q_values = {}
    deficits = []
    cut_min_slack = {}
    cut_negative = Counter()
    cut_sums = defaultdict(Fraction)
    for key, row in rows.items():
        k = key[2]
        q = sum((Fraction(1, target_reverse_degree[(k, T)]) for T in row),
                Fraction(0))
        delta = fibers[key]["demand"]
        slack = q - delta
        q_values[key] = q
        cut_sums[k] += slack
        cut_min_slack[k] = min(cut_min_slack.get(k, slack), slack)
        if slack < 0:
            cut_negative[k] += 1
            deficits.append((slack, key, q, delta, len(row),
                             min(target_reverse_degree[(k, T)] for T in row),
                             max(target_reverse_degree[(k, T)] for T in row)))

    print(f"RECIPROCAL_DEGREE_RESULT n={n}")
    print(f"  source_count={source_count}")
    print(f"  source_classes={sorted(source_classes.items(), key=lambda z: (-1 if z[0] is None else z[0]))}")
    print(f"  cut_fibers={dict(sorted(cut_fiber_counts.items()))}")
    print(f"  cut_target_incidences={dict(sorted(cut_incidence_counts.items()))}")
    print(f"  cut_target_counts={dict(sorted(Counter(k for k, _ in target_reverse_degree).items()))}")
    print(f"  cut_negative_fibers={dict(sorted(cut_negative.items()))}")
    print(f"  cut_minimum_q_minus_delta={dict(sorted(cut_min_slack.items()))}")
    print(f"  cut_sum_q_minus_delta={dict(sorted(cut_sums.items()))}")
    print(f"  negative_fiber_total={len(deficits)}")
    if deficits:
        deficits.sort(key=lambda x: x[0])
        for slack, key, q, delta, degree, rmin, rmax in deficits[:20]:
            parent, J, k = key
            print(f"  NEGATIVE cut={k} J={J} children={fibers[key]['children']} "
                  f"row={degree} reverse_degree_range=[{rmin},{rmax}] "
                  f"q={q} delta={delta} slack={slack} parent={parent}")
    else:
        print("  RESULT: reciprocal-degree sufficient condition PASSES this finite order")
    return not deficits


if __name__ == "__main__":
    assert run(8, 608)
    assert run(10, 31744)
