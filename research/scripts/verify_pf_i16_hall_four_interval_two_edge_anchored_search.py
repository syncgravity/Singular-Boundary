#!/usr/bin/env python3
"""Search all third-edge replacements while anchoring the first two motif edges.

This is a target-only, necessary-condition search for a four-interval extension.
It fixes the first two matched edges of the demand-independent alternative
triple, varies the third matched edge over the complete Ngrid=12 inventory,
and preserves the complete one-to-three-rhombus support families.

For each candidate triangle parent support triple, it asks whether the same
fourth matched edge can realize both decisive order-eight attachments:
  graph 5: interval 4 meets interval 1 only;
  graph 12: interval 4 meets intervals 2 and 3 only.

The fourth support options are deliberately over-enumerated: they need only
belong to the connected simple-boundary inventory and have the required
two-sided open-arc footprints. We do not require fourth-support collapse or
four-support L6c/L7b conditions. Therefore an empty common-edge set is a
strong necessary-condition obstruction, not a positive lift certificate.

No Hall demands, loads, deficiencies, matching outcomes, or flows are read.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from collections import defaultdict
from pathlib import Path

import verify_pf_i16_hall_four_interval_parent_compatibility as geom


def edge_key(row):
    return (tuple(row["lower"]), tuple(row["upper"]))


def sha_edges(edges):
    rows = [
        ",".join(map(str, a)) + "->" + ",".join(map(str, b))
        for a, b in sorted(edges)
    ]
    return hashlib.sha256(("\n".join(rows) + "\n").encode()).hexdigest()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--inventory", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    inv = json.loads(args.inventory.read_text())

    face_vertices, face_edges, options, _ = geom.build_target(inv)
    cells, union, intersection, collapse, point_contractible, edge_contractible, footprint = (
        geom.make_geometry(face_vertices, face_edges)
    )

    edge_rows = {edge_key(row["edge"]): row for row in inv["edge_support_options"]}
    fixed = [edge_key(row) for row in inv["fixed_triple_edges"]]
    e1, e2 = fixed[:2]
    fixed_endpoints = set(e1) | set(e2)
    if len(options[e1]) != 28 or len(options[e2]) != 26:
        raise AssertionError("anchored first-two edge support family changed")

    # Index every support option by its matched edge and by each vertex in its
    # support. This makes the fourth-edge mask query exact and inexpensive.
    all_options = []
    by_edge = defaultdict(list)
    vertex_to_options = defaultdict(set)
    for edge in sorted(options):
        for support in options[edge]:
            oid = len(all_options)
            all_options.append((edge, frozenset(support)))
            by_edge[edge].append(oid)
            support_vertices = cells(tuple(sorted(support)))[2]
            for vertex in support_vertices:
                vertex_to_options[vertex].add(oid)

    def options_touching(vertices):
        result = set()
        for vertex in vertices:
            result.update(vertex_to_options[vertex])
        return result

    first_pair_count = 0
    triple_assignment_count = 0
    by_third = defaultdict(lambda: {"graph5": set(), "graph12": set()})

    for s1 in options[e1]:
        if not edge_contractible(s1):
            continue
        c1 = cells(tuple(sorted(s1)))
        for s2 in options[e2]:
            if not edge_contractible(s2):
                continue
            c2 = cells(tuple(sorted(s2)))
            common12 = intersection([s1, s2])
            if not common12[2] or not point_contractible(common12):
                continue
            if not footprint(s1, s2, e1) or not footprint(s2, s1, e2):
                continue
            first_pair_count += 1

            # Any third edge whose support meets both first supports can be
            # found by intersecting the support-option vertex indexes.
            possible_s3 = options_touching(c1[2]) & options_touching(c2[2])
            for s3_oid in possible_s3:
                e3, s3 = all_options[s3_oid]
                if e3 in (e1, e2) or (set(e3) & fixed_endpoints):
                    continue
                if not edge_contractible(s3):
                    continue

                common13 = intersection([s1, s3])
                common23 = intersection([s2, s3])
                if not common13[2] or not common23[2]:
                    continue
                if not point_contractible(common13) or not point_contractible(common23):
                    continue
                if not footprint(s1, s3, e1) or not footprint(s3, s1, e3):
                    continue
                if not footprint(s2, s3, e2) or not footprint(s3, s2, e3):
                    continue

                triple_union = union([s1, s2, s3])
                if not point_contractible(triple_union):
                    continue
                # Star-parent interval 1 and interval 2 are the two eligible
                # non-root leaves. The root deletion is not imposed.
                if not collapse(triple_union, union([s1, s3])):
                    continue
                if not collapse(triple_union, union([s1, s2])):
                    continue

                triple_assignment_count += 1
                c3 = cells(tuple(sorted(s3)))

                # Graph 5 requires support 4 to meet S1 and avoid S2,S3.
                # Graph 12 requires support 4 to meet S2,S3 and avoid S1.
                hit_graph5 = (
                    options_touching(c1[2])
                    - options_touching(c2[2])
                    - options_touching(c3[2])
                )
                hit_graph12 = (
                    options_touching(c2[2])
                    & options_touching(c3[2])
                    - options_touching(c1[2])
                )

                endpoints123 = fixed_endpoints | set(e3)
                for qid in hit_graph5:
                    e4, s4 = all_options[qid]
                    if e4 in (e1, e2, e3) or (set(e4) & endpoints123):
                        continue
                    if footprint(s1, s4, e1) and footprint(s4, s1, e4):
                        by_third[e3]["graph5"].add(e4)

                for qid in hit_graph12:
                    e4, s4 = all_options[qid]
                    if e4 in (e1, e2, e3) or (set(e4) & endpoints123):
                        continue
                    if (
                        footprint(s2, s4, e2)
                        and footprint(s4, s2, e4)
                        and footprint(s3, s4, e3)
                        and footprint(s4, s3, e4)
                    ):
                        by_third[e3]["graph12"].add(e4)

    rows = []
    common_third_edges = []
    for e3 in sorted(by_third):
        g5 = by_third[e3]["graph5"]
        g12 = by_third[e3]["graph12"]
        common = g5 & g12
        if common:
            common_third_edges.append(e3)
        rows.append({
            "third_edge": {"lower": list(e3[0]), "upper": list(e3[1])},
            "graph5_fourth_edge_count": len(g5),
            "graph5_fourth_edge_sha256": sha_edges(g5),
            "graph12_fourth_edge_count": len(g12),
            "graph12_fourth_edge_sha256": sha_edges(g12),
            "common_fourth_edge_count": len(common),
            "common_fourth_edge_sha256": sha_edges(common),
        })

    result = {
        "schema": "PF-I16-HALL-FOUR-INTERVAL-TWO-EDGE-ANCHORED-SEARCH-v1",
        "target": inv["target"],
        "fixed_first_two_edges": [
            {"lower": list(e1[0]), "upper": list(e1[1])},
            {"lower": list(e2[0]), "upper": list(e2[1])},
        ],
        "inventory_edge_count": len(options),
        "first_two_support_pair_assignments_passing_triangle_parent_tests": first_pair_count,
        "triangle_parent_support_assignments": triple_assignment_count,
        "distinct_third_matched_edges_with_valid_triangle_supports": len(by_third),
        "third_edges_with_a_common_fourth_edge_for_graphs_5_and_12": len(common_third_edges),
        "common_third_edge_sha256": sha_edges(common_third_edges),
        "third_edge_candidate_sets": rows,
        "filters": [
            "The first two matched edges are fixed to the first two edges of the demand-independent alternative triple.",
            "Every one-to-three-rhombus support option for those two edges and every eligible third edge is enumerated.",
            "The first-three supports each collapse to their matched edge; their pairwise intersections are nonempty and collapse to a vertex; all three pair footprints are single boundary cells on both open complementary arcs.",
            "The first-three union collapses to a vertex and admits relative deletion collapses for the two non-root leaves of the star parent tree.",
            "For graph 5, a fourth support must intersect support 1 only; for graph 12 it must intersect supports 2 and 3 only. Footprints are checked in both directions.",
            "Fourth-support collapse and four-support L6c/L7b conditions are intentionally not imposed, so the candidate sets are relaxed supersets.",
        ],
        "nonclaims": [
            "The first two matched edges remain fixed; this is not a search over all first-three-edge motifs.",
            "The fourth support is only tested against necessary footprint and adjacency conditions, not the full L4/L6c/L7b requirements.",
            "The result does not exclude supports larger than three rhombi or a different target complex.",
            "The result does not establish L8 or the all-orders Hall inequality.",
        ],
    }
    payload = json.dumps(result, sort_keys=True, indent=2) + "\n"
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(payload)
    print(payload, end="")


if __name__ == "__main__":
    main()
