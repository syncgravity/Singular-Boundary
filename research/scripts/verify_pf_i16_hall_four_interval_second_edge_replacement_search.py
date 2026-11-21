#!/usr/bin/env python3
"""Search second-edge replacements with the first motif edge anchored.

This is a target-only necessary-condition search for the order-eight
four-interval extension. It consumes the complete Ngrid=12 support inventory
and the first-edge-anchored second-edge frontier. For each surviving second
edge it varies the third edge and aggregates graph-5 / graph-12 fourth-edge
candidate sets over every compatible first-three support assignment.

A fourth support is deliberately over-enumerated: it need only be an inventory
support with the required exact incidence mask and two-sided open-arc
footprints. We do not require fourth-support collapse or the full four-support
L6c/L7b diagram. Thus an empty common-fourth-edge result is only a necessary-
condition obstruction within this bounded target/support family.

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
    parser.add_argument("--frontier", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    inv = json.loads(args.inventory.read_text())
    frontier = json.loads(args.frontier.read_text())
    fv, fe, options, _ = geom.build_target(inv)
    cells, union, intersection, collapse, point_contractible, edge_contractible, footprint = (
        geom.make_geometry(fv, fe)
    )

    e1 = edge_key(inv["fixed_triple_edges"][0])
    frontier_rows = {
        edge_key(row["second_edge"]): row
        for row in frontier["candidate_second_edges"]
    }
    second_edges = sorted(frontier_rows)
    if len(second_edges) != frontier["second_edges_with_parent_compatible_support_pair"]:
        raise AssertionError("frontier candidate edge count mismatch")
    if sha_edges(second_edges) != frontier["candidate_second_edge_sha256"]:
        raise AssertionError("frontier candidate edge SHA-256 mismatch")
    if any(e not in options for e in second_edges):
        raise AssertionError("frontier contains an edge absent from support inventory")

    # Index every support option by edge and by its vertices. A support ID
    # refers to one exact connected simple-boundary support in the inventory.
    all_options = []
    by_edge = defaultdict(list)
    vertex_to_options = defaultdict(set)
    support_cells = []
    for edge in sorted(options):
        for support in options[edge]:
            oid = len(all_options)
            support = frozenset(support)
            all_options.append((edge, support))
            by_edge[edge].append(oid)
            c = cells(tuple(sorted(support)))
            support_cells.append(c)
            for vertex in c[2]:
                vertex_to_options[vertex].add(oid)

    touch_cache = {}
    def options_touching(vertices):
        key = frozenset(vertices)
        if key not in touch_cache:
            result = set()
            for vertex in key:
                result.update(vertex_to_options[vertex])
            touch_cache[key] = result
        return touch_cache[key]

    def matched_edge_contractible(oid, edge):
        fset, eset, vset = support_cells[oid]
        target = tuple(sorted(edge))
        return collapse(
            (set(fset), set(eset), set(vset)),
            (set(), {target}, set(target)),
        )

    # Cache support-to-edge collapse once, since a support belongs to exactly
    # one distinguished edge.
    edge_collapse_cache = {}
    def edge_collapses(oid):
        if oid not in edge_collapse_cache:
            edge_collapse_cache[oid] = matched_edge_contractible(
                oid, all_options[oid][0]
            )
        return edge_collapse_cache[oid]

    first_edge_oids = by_edge[e1]
    first_edge_valid = [oid for oid in first_edge_oids if edge_collapses(oid)]
    first_endpoints = set(e1)

    per_second = []
    total_pair_witnesses = 0
    total_triangle_assignments = 0
    total_common_third = 0
    common_witnesses = []

    for e2 in second_edges:
        if first_endpoints.intersection(e2):
            raise AssertionError("frontier second edge collides with first edge")
        e2_oids = by_edge[e2]
        fixed_endpoints = first_endpoints | set(e2)
        first_pairs = []
        for oid1 in first_edge_valid:
            s1 = all_options[oid1][1]
            c1 = support_cells[oid1]
            for oid2 in e2_oids:
                if not edge_collapses(oid2):
                    continue
                s2 = all_options[oid2][1]
                common12 = intersection([s1, s2])
                if not common12[2] or not point_contractible(common12):
                    continue
                if not footprint(s1, s2, e1) or not footprint(s2, s1, e2):
                    continue
                first_pairs.append((oid1, oid2))
        expected_pair_count = frontier_rows[e2]["support_pair_witness_count"]
        if len(first_pairs) != expected_pair_count:
            raise AssertionError((
                "recomputed first-two support-pair count differs from frontier",
                e2, len(first_pairs), expected_pair_count
            ))
        if not first_pairs:
            raise AssertionError(("frontier edge lost all support-pair witnesses", e2))
        total_pair_witnesses += len(first_pairs)

        # For a fixed (e2,e3), aggregate fourth-edge possibilities over all
        # admissible support triples; graph 5 and graph 12 may use different
        # first-three supports and different fourth supports.
        by_third = defaultdict(lambda: {"graph5": set(), "graph12": set()})
        for oid1, oid2 in first_pairs:
            s1 = all_options[oid1][1]
            s2 = all_options[oid2][1]
            c1, c2 = support_cells[oid1], support_cells[oid2]
            possible_s3 = options_touching(c1[2]) & options_touching(c2[2])
            for oid3 in possible_s3:
                e3, s3 = all_options[oid3]
                if e3 in (e1, e2) or fixed_endpoints.intersection(e3):
                    continue
                if not edge_collapses(oid3):
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
                # Both non-root leaves of the star parent must be deletable.
                if not collapse(triple_union, union([s1, s3])):
                    continue
                if not collapse(triple_union, union([s1, s2])):
                    continue

                total_triangle_assignments += 1
                c3 = support_cells[oid3]
                hit5 = (
                    options_touching(c1[2])
                    - options_touching(c2[2])
                    - options_touching(c3[2])
                )
                hit12 = (
                    (options_touching(c2[2]) & options_touching(c3[2]))
                    - options_touching(c1[2])
                )
                endpoints123 = fixed_endpoints | set(e3)

                for oid4 in hit5:
                    e4, s4 = all_options[oid4]
                    if e4 in (e1, e2, e3) or endpoints123.intersection(e4):
                        continue
                    if footprint(s1, s4, e1) and footprint(s4, s1, e4):
                        by_third[e3]["graph5"].add(e4)

                for oid4 in hit12:
                    e4, s4 = all_options[oid4]
                    if e4 in (e1, e2, e3) or endpoints123.intersection(e4):
                        continue
                    if (
                        footprint(s2, s4, e2)
                        and footprint(s4, s2, e4)
                        and footprint(s3, s4, e3)
                        and footprint(s4, s3, e4)
                    ):
                        by_third[e3]["graph12"].add(e4)

        rows = []
        common_third = []
        for e3 in sorted(by_third):
            g5 = by_third[e3]["graph5"]
            g12 = by_third[e3]["graph12"]
            common = g5 & g12
            if common:
                common_third.append(e3)
                common_witnesses.append({
                    "second_edge": {"lower": list(e2[0]), "upper": list(e2[1])},
                    "third_edge": {"lower": list(e3[0]), "upper": list(e3[1])},
                    "common_fourth_edges": [
                        {"lower": list(e4[0]), "upper": list(e4[1])}
                        for e4 in sorted(common)
                    ],
                })
            rows.append({
                "third_edge": {"lower": list(e3[0]), "upper": list(e3[1])},
                "graph5_fourth_edge_count": len(g5),
                "graph5_fourth_edge_sha256": sha_edges(g5),
                "graph12_fourth_edge_count": len(g12),
                "graph12_fourth_edge_sha256": sha_edges(g12),
                "common_fourth_edge_count": len(common),
                "common_fourth_edge_sha256": sha_edges(common),
            })
        total_common_third += len(common_third)
        per_second.append({
            "second_edge": {"lower": list(e2[0]), "upper": list(e2[1])},
            "first_two_support_pair_witnesses": len(first_pairs),
            "third_edges_with_triangle_supports": len(by_third),
            "third_edges_with_common_fourth_edge": len(common_third),
            "third_edge_results": rows,
        })

    result = {
        "schema": "PF-I16-HALL-FOUR-INTERVAL-SECOND-EDGE-REPLACEMENT-SEARCH-v1",
        "target": inv["target"],
        "fixed_first_edge": {"lower": list(e1[0]), "upper": list(e1[1])},
        "frontier_candidate_second_edge_count": len(second_edges),
        "frontier_candidate_second_edge_sha256": frontier["candidate_second_edge_sha256"],
        "total_first_two_support_pair_witnesses": total_pair_witnesses,
        "total_triangle_support_assignments": total_triangle_assignments,
        "total_second_third_pairs_with_common_fourth_edge": total_common_third,
        "second_edges_with_any_common_fourth_edge": sum(
            row["third_edges_with_common_fourth_edge"] > 0 for row in per_second
        ),
        "common_edge_witnesses": common_witnesses,
        "per_second_edge": per_second,
        "filters": [
            "The first matched edge remains fixed; the second edge ranges over the complete first-edge-anchored frontier.",
            "Every compatible first-two support pair and every eligible third-edge support option is retained.",
            "The first-three supports each collapse to their matched edge; all pairwise intersections collapse to a vertex and have two-sided open-arc footprints.",
            "The first-three union is contractible and both non-root star-parent relative deletion collapses succeed.",
            "Graph 5 and graph 12 fourth-edge candidates are aggregated over all support triples for each fixed second and third edge.",
            "Fourth supports are relaxed supersets: no fourth-edge collapse or complete four-support L6c/L7b test is imposed."
        ],
        "nonclaims": [
            "The first matched edge remains anchored; this is not a search over all first-edge choices.",
            "The support bound is the Ngrid=12 inventory of connected one-to-three-rhombus supports.",
            "An empty common-fourth-edge result is only a bounded necessary-condition obstruction, not nonexistence of all four-interval lifts.",
            "A surviving common edge would be a candidate only and would still require complete L6c/L7b diamond certification.",
            "This does not establish geometric L8 or the all-orders Hall inequality."
        ],
    }
    payload = json.dumps(result, sort_keys=True, indent=2) + "\n"
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(payload)
    print(json.dumps({
        k: v for k, v in result.items()
        if k not in ("per_second_edge", "common_edge_witnesses")
    }, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
