#!/usr/bin/env python3
"""Test canonical lexicographic augmenting-path rules for guarded source matching.

This is deliberately a diagnostic, not a claimed theorem. Sources are ordered
lexicographically by (matching, overlap-tree); each neighborhood is sorted by
its labeled edge tuple. The recursive augmenting search is deterministic.
We record whether this simple canonical rule saturates the source set and the
maximum recursion depth needed for a successful reassignment.
"""
from verify_pf_i16_local_switch_fractional_transport import (
    candidate_outputs, matchings, overlap_edges, spanning_trees,
)


def lexicographic_augmenting_assignment(rows):
    targets = sorted({t for row in rows for t in row})
    target_id = {t: i for i, t in enumerate(targets)}
    adjacency = [sorted((target_id[t] for t in row)) for row in rows]
    owner = [-1] * len(targets)
    chosen = [-1] * len(rows)
    max_depth = 0
    reassignment_lengths = []

    def augment(source, seen, depth):
        nonlocal max_depth
        max_depth = max(max_depth, depth)
        for target in adjacency[source]:
            if target in seen:
                continue
            seen.add(target)
            previous = owner[target]
            if previous == -1 or augment(previous, seen, depth + 1):
                owner[target] = source
                chosen[source] = target
                return True
        return False

    failures = []
    for source in range(len(rows)):
        before = sum(x != -1 for x in owner)
        if not augment(source, set(), 1):
            failures.append(source)
        else:
            after = sum(x != -1 for x in owner)
            assert after == before + 1
    assignment = [
        (i, targets[chosen[i]]) for i in range(len(rows)) if chosen[i] != -1
    ]
    assert len({t for _, t in assignment}) == len(assignment)
    return assignment, failures, max_depth


def enumerate_sources(n):
    rows = []
    labels = []
    for matching in matchings(range(1, n + 1)):
        intervals = tuple(sorted(tuple(sorted(e)) for e in matching))
        overlap = overlap_edges(intervals)
        for tau in spanning_trees(len(intervals), overlap):
            rows.append(candidate_outputs(intervals, tau))
            labels.append((intervals, tau))
    order = sorted(range(len(rows)), key=lambda i: labels[i])
    return [rows[i] for i in order], [labels[i] for i in order]


def run(n, expected):
    rows, labels = enumerate_sources(n)
    assert len(rows) == expected
    assignment, failures, depth = lexicographic_augmenting_assignment(rows)
    print(
        f"n={n}: sources={len(rows)}, matched={len(assignment)}, "
        f"failures={len(failures)}, max_augmenting_depth={depth}"
    )
    if failures:
        print(f"  first_failed_sources={[labels[i] for i in failures[:5]]}")
    else:
        print("  PASS: deterministic lexicographic augmenting rule saturates all sources")
        print(f"  first_assignments={assignment[:5]}")
    return not failures


def main():
    results = [run(4, 2), run(6, 22), run(8, 608)]
    if not all(results):
        raise SystemExit("Lexicographic augmenting rule failed at a tested order.")
    print("All tested orders saturated by the deterministic lexicographic rule.")


if __name__ == "__main__":
    main()
