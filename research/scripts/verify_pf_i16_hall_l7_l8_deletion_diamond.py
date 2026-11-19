#!/usr/bin/env python3
"""Exact source-level deletion-diamond verifier for the PF-I16 Hall lift.

This verifies only the combinatorial source deletion system at n=8. It does
not inspect target supports, L6c, L7b, or Hall demands/flows.
"""
from __future__ import annotations
import argparse
import json
from collections import Counter
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import export_pf_i16_hall_source_records as hall


def delete_one(intervals, tree_edges, index):
    gone = set(intervals[index])
    ports = range(1, 2 * len(intervals) + 1)
    retained_ports = [p for p in ports if p not in gone]
    compression = {p: i + 1 for i, p in enumerate(retained_ports)}
    new_intervals = tuple(sorted(
        (compression[a], compression[b])
        for i, (a, b) in enumerate(intervals) if i != index
    ))
    retained_indices = [i for i in range(len(intervals)) if i != index]
    reindex = {old: new for new, old in enumerate(retained_indices)}
    new_tree = tuple(sorted(
        (reindex[a], reindex[b])
        for a, b in tree_edges if a != index and b != index
    ))
    return new_intervals, new_tree


def direct_double_delete(intervals, tree_edges, i, j):
    deleted_ports = set(intervals[i]) | set(intervals[j])
    retained_ports = [p for p in range(1, 2 * len(intervals) + 1)
                      if p not in deleted_ports]
    compression = {p: k + 1 for k, p in enumerate(retained_ports)}
    retained_indices = [k for k in range(len(intervals)) if k not in (i, j)]
    new_intervals = tuple(sorted(
        (compression[intervals[k][0]], compression[intervals[k][1]])
        for k in retained_indices
    ))
    reindex = {old: new for new, old in enumerate(retained_indices)}
    new_tree = tuple(sorted(
        (reindex[a], reindex[b])
        for a, b in tree_edges if a in reindex and b in reindex
    ))
    return new_intervals, new_tree


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=None)
    args = parser.parse_args()

    rows = hall.source_records(8)
    if len(rows) != 608:
        raise AssertionError(("unexpected n=8 source count", len(rows)))

    graph_counts = Counter()
    mark_histogram = Counter()
    diamond_count = 0
    path_mismatches = []
    by_graph_diamonds = Counter()
    max_marks = 0

    for row in rows:
        intervals = tuple(tuple(x) for x in row["intervals"])
        tree = tuple(tuple(x) for x in row["tree_edges"])
        graph = tuple(tuple(x) for x in row["full_overlap_edges"])
        marks = tuple(int(x) for x in row["eligible_reverse_marks"])
        graph_counts[graph] += 1
        mark_histogram[len(marks)] += 1
        max_marks = max(max_marks, len(marks))

        parent_by_mark = {
            int(p["deleted_interval_index"]): p for p in row["parents"]
        }
        if set(parent_by_mark) != set(marks):
            raise AssertionError(("parent records do not match eligible marks", row))

        for pos, i in enumerate(marks):
            for j in marks[pos + 1:]:
                # Path i then j.
                p_i = parent_by_mark[i]
                ints_i = tuple(tuple(x) for x in p_i["parent_intervals"])
                tree_i = tuple(tuple(x) for x in p_i["parent_tree_edges"])
                remaining_after_i = [k for k in range(len(intervals)) if k != i]
                j_after_i = remaining_after_i.index(j)
                path_ij = delete_one(ints_i, tree_i, j_after_i)

                # Path j then i.
                p_j = parent_by_mark[j]
                ints_j = tuple(tuple(x) for x in p_j["parent_intervals"])
                tree_j = tuple(tuple(x) for x in p_j["parent_tree_edges"])
                remaining_after_j = [k for k in range(len(intervals)) if k != j]
                i_after_j = remaining_after_j.index(i)
                path_ji = delete_one(ints_j, tree_j, i_after_j)

                direct = direct_double_delete(intervals, tree, i, j)
                if path_ij != path_ji or path_ij != direct:
                    path_mismatches.append({
                        "intervals": intervals, "tree": tree,
                        "marks": [i, j], "path_ij": path_ij,
                        "path_ji": path_ji, "direct": direct,
                    })
                else:
                    diamond_count += 1
                    by_graph_diamonds[graph] += 1

    if path_mismatches:
        raise AssertionError(("deletion diamond failures", path_mismatches[:3]))
    if diamond_count != 490:
        raise AssertionError(("unexpected deletion diamond count", diamond_count))
    if len(graph_counts) != 13:
        raise AssertionError(("unexpected overlap graph type count", len(graph_counts)))

    result = {
        "schema": "PF-I16-HALL-SOURCE-DELETION-DIAMOND-v1",
        "scope": "all n=8 Hall sources and pairs of simultaneously eligible reverse-leaf marks",
        "source_count": len(rows),
        "eligible_mark_count": sum(k * v for k, v in mark_histogram.items()),
        "eligible_mark_histogram": {str(k): v for k, v in sorted(mark_histogram.items())},
        "distinct_full_overlap_graphs": len(graph_counts),
        "overlap_graph_source_counts": [
            {"edges": [list(e) for e in graph], "sources": count}
            for graph, count in sorted(graph_counts.items())
        ],
        "simultaneous_deletion_pairs": diamond_count,
        "deletion_diamonds_verified": diamond_count,
        "deletion_diamond_failures": len(path_mismatches),
        "max_simultaneously_eligible_marks": max_marks,
        "proof_boundary": [
            "This is source-level confluence only.",
            "No target support, intersection diagram, L6c collapse, or L7b boundary data are tested.",
            "No all-orders induction is established by the n=8 finite enumeration.",
            "No Hall demand, load, deficiency, matching, or flow data are read."
        ]
    }
    payload = json.dumps(result, sort_keys=True, indent=2) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(payload)
    print(payload, end="")


if __name__ == "__main__":
    main()
