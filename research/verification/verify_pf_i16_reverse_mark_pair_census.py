#!/usr/bin/env python3
"""Exhaust small port trees for guarded reverse-mark pairs.

This is a finite diagnostic for target-side local geometry only. It does not
construct matching sources, overlap trees, canonical parent neighborhoods,
fiber demands, or Hall witnesses.
"""
from itertools import combinations, product

# Zero-based ranks x1 < x2 < x3 < x4.
LOCAL = {
    "S0": frozenset({(0, 1), (1, 2), (1, 3)}),
    "S1": frozenset({(0, 1), (1, 2), (2, 3)}),
    "S2": frozenset({(0, 2), (1, 2), (2, 3)}),
}
EXPECTED_RANK_MARKS = {
    (0, 2): ("S1", "S2"),
    (1, 2): ("S0", "S1", "S2"),
    (1, 3): ("S0", "S1"),
}


def edge(a, b):
    return tuple(sorted((a, b)))


def prufer_tree(code, n):
    degree = [1] * n
    for v in code:
        degree[v] += 1
    result = []
    for v in code:
        leaf = next(i for i, d in enumerate(degree) if d == 1)
        result.append(edge(leaf, v))
        degree[leaf] -= 1
        degree[v] -= 1
    leaves = [i for i, d in enumerate(degree) if d == 1]
    result.append(edge(*leaves))
    return frozenset(result)


def overlap(e, mark):
    u, v = e
    a, b = mark
    return max(u, a) < min(v, b)


def local_records(tree, n, mark):
    """All exact guarded inverse records for fixed mark in this port tree."""
    records = []
    outside = [v for v in range(n) if v not in mark]
    for old in combinations(outside, 2):
        ports = tuple(sorted((*mark, *old)))
        mapped = {
            name: frozenset(edge(ports[i], ports[j]) for i, j in pattern)
            for name, pattern in LOCAL.items()
        }
        for name, target_pattern in mapped.items():
            incident_target = frozenset(
                e for e in tree if e[0] in mark or e[1] in mark
            )
            incident_local = frozenset(
                e for e in target_pattern if e[0] in mark or e[1] in mark
            )
            induced = frozenset(
                e for e in tree if e[0] in ports and e[1] in ports
            )
            old_edge = edge(*old)
            if (
                induced == target_pattern
                and incident_target == incident_local
                and old_edge not in target_pattern
                and overlap(old_edge, mark)
            ):
                records.append((old, name, ports))
    return records


def all_marks(tree, n):
    answer = {}
    for mark in combinations(range(n), 2):
        records = local_records(tree, n, mark)
        assert len(records) <= 1, (tree, mark, records)
        if records:
            answer[mark] = records[0]
    return answer


def inverse(tree, mark, record):
    old, _name, _ports = record
    return frozenset(
        e for e in tree if e[0] not in mark and e[1] not in mark
    ) | {edge(*old)}


def relabel_tree(tree, old_vertices):
    relabel = {v: i for i, v in enumerate(old_vertices)}
    return frozenset(edge(relabel[a], relabel[b]) for a, b in tree)


def relabel_record(record, old_vertices):
    relabel = {v: i for i, v in enumerate(old_vertices)}
    old, name, ports = record
    return (
        tuple(relabel[v] for v in old),
        name,
        tuple(relabel[v] for v in ports),
    )


def lift_record(record, new_to_old):
    old, name, ports = record
    return (
        tuple(new_to_old[v] for v in old),
        name,
        tuple(new_to_old[v] for v in ports),
    )


def pair_census(n):
    tree_count = 0
    mark_histogram = {}
    max_marks = 0
    pair_count = 0
    disjoint_mark_pairs = 0
    second_survives = 0
    both_survive = 0
    commuting_survivors = 0
    survivor_support_types = {}

    for code in product(range(n), repeat=n - 2):
        tree = prufer_tree(code, n)
        marks = all_marks(tree, n)
        tree_count += 1
        count = len(marks)
        max_marks = max(max_marks, count)
        mark_histogram[count] = mark_histogram.get(count, 0) + 1

        for (j, rj), (k, rk) in combinations(marks.items(), 2):
            pair_count += 1
            if set(j) & set(k):
                continue
            disjoint_mark_pairs += 1

            # Project J first, then test whether K is a valid reverse mark
            # in the smaller parent target. The second witness may change.
            parent_j = inverse(tree, j, rj)
            remaining_j = sorted(set(range(n)) - set(j))
            parent_j_small = relabel_tree(parent_j, remaining_j)
            k_small = tuple(sorted(remaining_j.index(v) for v in k))
            k_records = local_records(parent_j_small, n - 2, k_small)

            # Symmetric test: K first, then J.
            parent_k = inverse(tree, k, rk)
            remaining_k = sorted(set(range(n)) - set(k))
            parent_k_small = relabel_tree(parent_k, remaining_k)
            j_small = tuple(sorted(remaining_k.index(v) for v in j))
            j_records = local_records(parent_k_small, n - 2, j_small)

            if k_records:
                second_survives += 1
            if not (k_records and j_records):
                continue
            both_survive += 1

            # Lift the newly validated second witnesses back to original
            # labels and compare the two double inverses.
            k_after_j = lift_record(
                k_records[0], {i: v for i, v in enumerate(remaining_j)}
            )
            j_after_k = lift_record(
                j_records[0], {i: v for i, v in enumerate(remaining_k)}
            )
            j_then_k = inverse(parent_j, k, k_after_j)
            k_then_j = inverse(parent_k, j, j_after_k)
            remaining = sorted(set(range(n)) - set(j) - set(k))
            j_then_k = relabel_tree(j_then_k, remaining)
            k_then_j = relabel_tree(k_then_j, remaining)
            assert j_then_k == k_then_j, (
                tree, j, rj, k, rk, k_records, j_records,
                j_then_k, k_then_j,
            )
            commuting_survivors += 1

            support_j = set(j) | set(rj[0])
            support_k = set(k) | set(rk[0])
            key = (
                len(support_j & support_k),
                len(set(rj[0]) & set(k)),
                len(set(rk[0]) & set(j)),
            )
            survivor_support_types[key] = (
                survivor_support_types.get(key, 0) + 1
            )

    return {
        "n": n,
        "trees": tree_count,
        "mark_histogram": dict(sorted(mark_histogram.items())),
        "max_marks": max_marks,
        "unordered_mark_pairs": pair_count,
        "disjoint_mark_pairs": disjoint_mark_pairs,
        "second_survives_after_first": second_survives,
        "both_directions_survive": both_survive,
        "commuting_double_inverses": commuting_survivors,
        "survivor_support_types": survivor_support_types,
    }


EXPECTED_CENSUS = {
    5: {
        "trees": 125, "mark_histogram": {0: 86, 1: 14, 2: 22, 4: 3},
        "max_marks": 4, "unordered_mark_pairs": 40,
        "disjoint_mark_pairs": 10, "second_survives_after_first": 0,
        "both_directions_survive": 0, "commuting_double_inverses": 0,
        "survivor_support_types": {},
    },
    6: {
        "trees": 1296, "mark_histogram": {0: 777, 1: 267, 2: 210, 3: 20, 4: 19, 5: 1, 6: 2},
        "max_marks": 6, "unordered_mark_pairs": 424,
        "disjoint_mark_pairs": 118, "second_survives_after_first": 58,
        "both_directions_survive": 58, "commuting_double_inverses": 58,
        "survivor_support_types": {(2, 1, 1): 58},
    },
    7: {
        "trees": 16807, "mark_histogram": {0: 9249, 1: 4088, 2: 2632, 3: 510, 4: 290, 5: 24, 6: 11, 7: 2, 8: 1},
        "max_marks": 8, "unordered_mark_pairs": 6377,
        "disjoint_mark_pairs": 2331, "second_survives_after_first": 1701,
        "both_directions_survive": 1701, "commuting_double_inverses": 1701,
        "survivor_support_types": {(2, 1, 1): 812, (1, 0, 0): 889},
    },
}


def main():
    # Exhaust all six possible mark ranks on a four-port support.
    rank_records = {}
    for mark in combinations(range(4), 2):
        old = tuple(v for v in range(4) if v not in mark)
        for name, pattern in LOCAL.items():
            incident = frozenset(
                e for e in pattern if e[0] in mark or e[1] in mark
            )
            if (
                incident == pattern
                and edge(*old) not in pattern
                and overlap(edge(*old), mark)
            ):
                rank_records.setdefault(mark, []).append(name)
    rank_records = {k: tuple(v) for k, v in rank_records.items()}
    assert rank_records == EXPECTED_RANK_MARKS, rank_records

    print("PASS four-port rank census:", rank_records)
    for n in (5, 6, 7):
        result = pair_census(n)
        assert result["second_survives_after_first"] == result["both_directions_survive"]
        assert result["both_directions_survive"] == result["commuting_double_inverses"]
        assert {k: v for k, v in result.items() if k != "n"} == EXPECTED_CENSUS[n]
        print("PASS exhaustive pair census:", result)


if __name__ == "__main__":
    main()
