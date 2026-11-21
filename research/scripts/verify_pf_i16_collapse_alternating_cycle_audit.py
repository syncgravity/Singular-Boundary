#!/usr/bin/env python3
"""Audit symmetric differences of PF-I16 elementary collapse pairings.

Input is the gzip JSON emitted by verify_pf_i16_four_support_relative_collapse_diamonds.py.
For every critical pair whose two deterministic collapse paths use different elementary
free-pair sets, this verifier checks that the symmetric difference is one connected,
even, alternating cycle in the typed cell-incidence graph.
"""
from __future__ import annotations

import argparse
import collections
import gzip
import hashlib
import json
from pathlib import Path
from typing import Any


def cell_key(value: Any) -> tuple:
    """Return a typed, hashable cell identity from the collapse certificate schema."""
    if isinstance(value, int):
        return ("F", value)
    if not isinstance(value, list):
        raise AssertionError(("unrecognized cell encoding", value))
    if value and isinstance(value[0], list):
        return ("E", tuple(sorted(tuple(int(c) for c in v) for v in value)))
    return ("V", tuple(int(c) for c in value))


def path_pairs(path: dict) -> set[tuple]:
    pairs: set[tuple] = set()
    for stage_name in ("first_relative_collapse", "second_relative_collapse"):
        stage = path[stage_name]
        for item in stage["face_edge_pairs"]:
            pair = (cell_key(item["free_edge"]), cell_key(item["removed_face"]))
            if pair in pairs:
                raise AssertionError(("duplicate elementary pair in one path", pair))
            pairs.add(pair)
        for item in stage["edge_vertex_pairs"]:
            pair = (cell_key(item["free_vertex"]), cell_key(item["removed_edge"]))
            if pair in pairs:
                raise AssertionError(("duplicate elementary pair in one path", pair))
            pairs.add(pair)
    return pairs


def audit_cycle(left: set[tuple], right: set[tuple]) -> dict:
    left_only, right_only = left - right, right - left
    if not left_only or len(left_only) != len(right_only):
        raise AssertionError(("unbalanced symmetric difference", len(left_only), len(right_only)))

    adjacency: dict[tuple, list[tuple[tuple, str]]] = collections.defaultdict(list)
    for tag, pairs in (("L", left_only), ("R", right_only)):
        used = set()
        for a, b in pairs:
            if a in used or b in used:
                raise AssertionError(("one path is not a cell matching on symmetric difference", tag, a, b))
            used.add(a)
            used.add(b)
            adjacency[a].append((b, tag))
            adjacency[b].append((a, tag))

    degrees = {node: len(edges) for node, edges in adjacency.items()}
    if any(degree != 2 for degree in degrees.values()):
        raise AssertionError(("symmetric-difference graph is not 2-regular", collections.Counter(degrees.values())))
    if any({tag for _, tag in adjacency[node]} != {"L", "R"} for node in adjacency):
        raise AssertionError("alternation fails at a cell")

    start = min(adjacency, key=repr)
    stack, seen = [start], {start}
    while stack:
        node = stack.pop()
        for neighbor, _ in adjacency[node]:
            if neighbor not in seen:
                seen.add(neighbor)
                stack.append(neighbor)
    if len(seen) != len(adjacency):
        raise AssertionError(("symmetric difference has multiple components", len(seen), len(adjacency)))

    types = collections.Counter(node[0] for node in adjacency)
    cycle_nodes = len(adjacency)
    if cycle_nodes % 2 or cycle_nodes != 2 * len(left_only):
        raise AssertionError(("cycle parity/size mismatch", cycle_nodes, len(left_only)))
    return {
        "cycle_cell_count": cycle_nodes,
        "pairs_per_path_in_symmetric_difference": len(left_only),
        "face_cells": types["F"],
        "edge_cells": types["E"],
        "vertex_cells": types["V"],
        "connected_components": 1,
        "all_cells_have_one_left_and_one_right_pair": True,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--collapse", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()

    raw = args.collapse.read_bytes()
    payload = json.loads(gzip.decompress(raw))
    families_out = {}
    total_different = total_same = 0

    for family, family_data in sorted(payload["families"].items()):
        histogram: collections.Counter = collections.Counter()
        mark_pair_counts: collections.Counter = collections.Counter()
        different = same = 0
        for witness in family_data["witness_results"]:
            for permutation in witness["permutation_results"]:
                for certificate in permutation["diamond_certificates"]:
                    left = path_pairs(certificate["path_delete_m_then_n"])
                    right = path_pairs(certificate["path_delete_n_then_m"])
                    recorded_same = bool(certificate["same_elementary_pair_set"])
                    computed_same = left == right
                    if recorded_same != computed_same:
                        raise AssertionError(("recorded pair-set verdict mismatch", family, witness["witness_id"], certificate["source_mark_pair"]))
                    if computed_same:
                        same += 1
                        continue
                    different += 1
                    result = audit_cycle(left, right)
                    key = (
                        result["cycle_cell_count"],
                        result["face_cells"],
                        result["edge_cells"],
                        result["vertex_cells"],
                        result["pairs_per_path_in_symmetric_difference"],
                    )
                    histogram[key] += 1
                    mark_pair_counts[tuple(certificate["source_mark_pair"])] += 1

        if different != family_data["different_elementary_pair_set_tests"]:
            raise AssertionError(("different-pair test count mismatch", family, different, family_data["different_elementary_pair_set_tests"]))
        if same != family_data["same_elementary_pair_set_tests"]:
            raise AssertionError(("same-pair test count mismatch", family, same, family_data["same_elementary_pair_set_tests"]))
        total_different += different
        total_same += same
        families_out[family] = {
            "same_pair_set_tests": same,
            "different_pair_set_tests": different,
            "every_different_pair_set_is_one_alternating_cycle": True,
            "cycle_signature_histogram": [
                {"cycle_cells": k[0], "faces": k[1], "edges": k[2], "vertices": k[3],
                 "pairs_per_path_in_symmetric_difference": k[4], "count": v}
                for k, v in sorted(histogram.items())
            ],
            "source_mark_pair_test_counts": [
                {"marks": list(k), "count": v} for k, v in sorted(mark_pair_counts.items())
            ],
        }

    expected_total = sum(x["different_elementary_pair_set_tests"] for x in payload["families"].values())
    if total_different != expected_total or total_different != 1788:
        raise AssertionError(("global different-pair count mismatch", total_different, expected_total))

    output = {
        "schema": "PF-I16-COLLAPSE-ALTERNATING-CYCLE-AUDIT-v1",
        "collapse_input_sha256": hashlib.sha256(raw).hexdigest(),
        "total_same_pair_set_tests": total_same,
        "total_different_pair_set_tests": total_different,
        "conclusions": {
            "every_different_pair_set_symmetric_difference_is_one_connected_alternating_cycle": True,
            "no_open_alternating_paths_or_multiple_components_found": True,
            "this_is_a_matching_difference_classification_not_a_collapse_map_homotopy_proof": True,
            "geometric_L8_closed": False,
        },
        "families": families_out,
        "scope": "Finite Ngrid=12 graph-5/graph-12 four-support collapse certificates only.",
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"same": total_same, "different": total_different, "families": families_out}, sort_keys=True))


if __name__ == "__main__":
    main()
