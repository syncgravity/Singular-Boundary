#!/usr/bin/env python3
"""Independently replay the explicit n=10 multivalued-pi matching certificate."""
import json
from pathlib import Path

from verify_pf_i16_source_dependent_leaf_peeling import (
    sources, canonical_leaf, parent_data, inverse_last_switch, compress_tree,
)
from verify_pf_i16_local_switch_fractional_transport import candidate_outputs
from verify_pf_i16_full_leaf_last_graph_n10 import encode_tree


def decode_tree(mask, n=10):
    edges = []
    bit = 0
    for a in range(1, n + 1):
        for b in range(a + 1, n + 1):
            if (mask >> bit) & 1:
                edges.append((a, b))
            bit += 1
    return tuple(edges)


def main():
    path = Path("n10_multivalued_pi_matching.json")
    cert = json.loads(path.read_text(encoding="utf-8"))
    assert cert["schema"] == "pf-i16-multivalued-pi-matching-v1"
    assert cert["n"] == 10
    assert cert["source_count"] == cert["matching_size"] == 31744
    rows = cert["rows"]
    assert len(rows) == 31744

    seen_targets = set()
    checked = 0
    parent_cache = {}
    for index, (expected_intervals, expected_tau) in enumerate(sources(10)):
        row = rows[index]
        intervals = tuple(tuple(e) for e in row["source_intervals"])
        tau = tuple(tuple(e) for e in row["source_overlap_tree"])
        assert intervals == expected_intervals, ("source intervals", index)
        assert tau == expected_tau, ("source overlap tree", index)

        leaf_interval = tuple(row["leaf_interval"])
        assert leaf_interval in intervals
        leaf = intervals.index(leaf_interval)
        assert leaf != next(i for i, I in enumerate(intervals) if I[0] == 1)
        degree = [0] * len(intervals)
        for a, b in tau:
            degree[a] += 1
            degree[b] += 1
        assert degree[leaf] == 1, ("not a non-root leaf", index, leaf)

        parent = parent_data(intervals, tau, leaf)
        stored_parent = (
            tuple(tuple(e) for e in row["parent_intervals"]),
            tuple(tuple(e) for e in row["parent_overlap_tree"]),
        )
        assert parent == stored_parent, ("parent projection", index)

        target = decode_tree(row["target_mask"])
        assert len(target) == 9
        assert row["target_mask"] not in seen_targets, ("duplicate target", index)
        seen_targets.add(row["target_mask"])

        child_outputs = candidate_outputs(intervals, tau, forced_last=leaf)
        assert target in child_outputs, ("matched edge not in child leaf-last row", index)

        projected_candidates = inverse_last_switch(target, leaf_interval, 10)
        assert len(projected_candidates) == 1
        projected = compress_tree(next(iter(projected_candidates)),
                                  set(leaf_interval), 10)
        stored_projected = tuple(sorted(tuple(sorted(e))
                                        for e in row["projected_parent_tree"]))
        assert projected == stored_projected, ("inverse projection", index)

        if parent not in parent_cache:
            pi, pt = parent
            parent_leaf = canonical_leaf(pi, pt)
            parent_cache[parent] = candidate_outputs(pi, pt,
                                                     forced_last=parent_leaf)
        assert projected in parent_cache[parent], (
            "parent target not in canonical parent neighborhood", index
        )
        assert encode_tree(target) == row["target_mask"]
        checked += 1

    assert len(seen_targets) == checked == 31744
    print("PASS: explicit n=10 multivalued-pi matching certificate")
    print(f"  matched_sources={checked}")
    print(f"  distinct_assigned_child_targets={len(seen_targets)}")
    print(f"  distinct_parent_sources_used={len(parent_cache)}")
    print("  every child edge replayed from its selected leaf")
    print("  every projected parent edge replayed in its canonical parent row")


if __name__ == "__main__":
    main()
