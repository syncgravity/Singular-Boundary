#!/usr/bin/env python3
"""Exact finite obstruction check for L6 under the frozen rank-indexed edge map.

The frozen L1-L3 rule maps sorted child interval I_i to motif edge e_i.
For each eligible non-root leaf deletion, this script compares the inherited
edge identity of every retained interval with the rank-indexed edge identity
assigned to that interval in the compressed parent.

No target geometry, Hall loads, deficiencies, flows, or observer data are used.
"""
from __future__ import annotations
import json
from collections import defaultdict
from pathlib import Path
import argparse
import export_pf_i16_hall_source_records as hall

def parent_key(record, parent):
    return (
        tuple(tuple(x) for x in parent["parent_intervals"]),
        tuple(tuple(x) for x in parent["parent_tree_edges"]),
    )

def check_order_six():
    rows = hall.source_records(6)
    if len(rows) != 22:
        raise AssertionError(("expected 22 order-six sources", len(rows)))

    marks = 0
    rank_shift_marks = 0
    parent_origins = defaultdict(list)
    first_obstruction = None

    for row in rows:
        intervals = [tuple(x) for x in row["intervals"]]
        for parent in row["parents"]:
            marks += 1
            deleted = int(parent["deleted_interval_index"])
            retained_old = [i for i in range(len(intervals)) if i != deleted]
            inherited = []
            conflicts = []
            for new_index, old_index in enumerate(retained_old):
                child_edge = old_index + 1
                parent_edge = new_index + 1
                inherited.append({
                    "parent_interval_index": new_index,
                    "child_interval_index": old_index,
                    "inherited_edge": child_edge,
                    "rank_assigned_parent_edge": parent_edge,
                    "commutes": child_edge == parent_edge,
                })
                if child_edge != parent_edge:
                    conflicts.append((new_index, child_edge, parent_edge))
            if conflicts:
                rank_shift_marks += 1
                if first_obstruction is None:
                    first_obstruction = {
                        "child_intervals": [list(x) for x in intervals],
                        "child_tree_edges": row["tree_edges"],
                        "deleted_interval_index": deleted,
                        "deleted_interval": parent["deleted_interval"],
                        "parent_intervals": parent["parent_intervals"],
                        "parent_tree_edges": parent["parent_tree_edges"],
                        "inherited_edge_comparison": inherited,
                    }
            parent_origins[parent_key(row, parent)].append({
                "child_intervals": [list(x) for x in intervals],
                "child_tree_edges": row["tree_edges"],
                "deleted_interval_index": deleted,
                "inherited_edge_map": [x["inherited_edge"] for x in inherited],
            })

    ambiguous = {}
    for key, origins in sorted(parent_origins.items()):
        maps = sorted({tuple(x["inherited_edge_map"]) for x in origins})
        if len(maps) > 1:
            ambiguous[str(key)] = {
                "distinct_inherited_edge_maps": [list(x) for x in maps],
                "origin_count": len(origins),
            }

    if marks != 30:
        raise AssertionError(("expected 30 eligible marks", marks))
    if rank_shift_marks != 14:
        raise AssertionError(("unexpected rank-shift count", rank_shift_marks))
    if len(ambiguous) != 2:
        raise AssertionError(("expected two ambiguous parent structures", ambiguous))

    # Canonical explicit witness: the same parent is reached by deleting I2
    # or I3 from the same child source, but I2 of the parent inherits e3 or e2.
    witness_child = ((1, 4), (2, 5), (3, 6))
    witness_tree = ((0, 1), (0, 2))
    witness_origins = []
    for row in rows:
        if tuple(tuple(x) for x in row["intervals"]) != witness_child:
            continue
        if tuple(tuple(x) for x in row["tree_edges"]) != witness_tree:
            continue
        for parent in row["parents"]:
            if parent["deleted_interval_index"] in (1, 2):
                retained_old = [i for i in range(3)
                                if i != parent["deleted_interval_index"]]
                witness_origins.append({
                    "deleted_interval_index": parent["deleted_interval_index"],
                    "deleted_interval": parent["deleted_interval"],
                    "parent_intervals": parent["parent_intervals"],
                    "parent_tree_edges": parent["parent_tree_edges"],
                    "parent_interval_2_inherited_edge":
                        retained_old[1] + 1,
                })
    if len(witness_origins) != 2:
        raise AssertionError(("explicit two-mark witness missing", witness_origins))
    if {x["parent_interval_2_inherited_edge"] for x in witness_origins} != {2, 3}:
        raise AssertionError(("explicit witness does not force e2/e3 conflict",
                              witness_origins))

    return {
        "schema": "PF-I16-HALL-L6-RANK-MAP-OBSTRUCTION-v1",
        "scope": "all n=6 Hall sources and eligible non-root leaf marks",
        "source_count": len(rows),
        "eligible_mark_count": marks,
        "rank_shift_mark_count": rank_shift_marks,
        "rank_shift_mark_fraction": rank_shift_marks / marks,
        "distinct_parent_structures": len(parent_origins),
        "parent_structures_with_conflicting_inherited_maps": len(ambiguous),
        "ambiguous_parent_structures": ambiguous,
        "first_rank_shift_obstruction": first_obstruction,
        "same_child_two_mark_witness": {
            "child_intervals": [list(x) for x in witness_child],
            "child_tree_edges_zero_based": [list(x) for x in witness_tree],
            "parent_intervals": [[1, 3], [2, 4]],
            "parent_tree_edges_zero_based": [[0, 1]],
            "eligible_deletions": witness_origins,
            "conclusion": "the same parent second interval is forced to inherit e2 and e3",
        },
        "verdict": "L6 FAILS for the frozen rank-indexed port/edge map",
        "nonclaims": [
            "not a Hall counterexample",
            "does not test free-edge collapses because port/edge naturality already fails",
            "does not rule out a redesigned parent-compatible lift",
            "does not establish L7, L8, or the Hall theorem",
        ],
    }

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=None)
    args = parser.parse_args()
    result = check_order_six()
    payload = json.dumps(result, sort_keys=True, indent=2) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(payload)
    print(payload, end="")

if __name__ == "__main__":
    main()
