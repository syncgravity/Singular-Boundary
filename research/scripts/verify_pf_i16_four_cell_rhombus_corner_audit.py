#!/usr/bin/env python3
"""Verify graph-5 four-cell alternating-cycle geometry from a CI artifact.

Input is the decompressed JSON payload from artifact 14680929981.
This checks typed pair-set symmetric differences; it does not replay collapse
validity, reconstruct the complete target inventory, or prove geometric L8.
"""
from __future__ import annotations
import json
import sys
from collections import defaultdict
from pathlib import Path


def canon_edge(edge):
    return tuple(sorted(tuple(vertex) for vertex in edge))


def pair_set(path):
    result = set()
    for stage in ("first_relative_collapse", "second_relative_collapse"):
        collapse = path[stage]
        for pair in collapse["face_edge_pairs"]:
            result.add(("FE", canon_edge(pair["free_edge"]), pair["removed_face"]))
        for pair in collapse["edge_vertex_pairs"]:
            result.add(("EV", tuple(pair["free_vertex"]), canon_edge(pair["removed_edge"])))
    return result


def classify(certificate):
    left = pair_set(certificate["path_delete_m_then_n"])
    right = pair_set(certificate["path_delete_n_then_m"])
    difference = left ^ right
    faces, edges, vertices = set(), set(), set()
    adjacency = defaultdict(set)
    for kind, first, second in difference:
        if kind == "FE":
            edges.add(first)
            faces.add(second)
            a, b = ("E", first), ("F", second)
        else:
            vertices.add(first)
            edges.add(second)
            a, b = ("V", first), ("E", second)
        adjacency[a].add(b)
        adjacency[b].add(a)
    is_four_cycle = (
        len(difference) == 4
        and (len(faces), len(edges), len(vertices)) == (1, 2, 1)
        and len(adjacency) == 4
        and all(len(neighbors) == 2 for neighbors in adjacency.values())
    )
    if not is_four_cycle:
        return None
    shared_vertex = next(iter(vertices))
    residual_endpoints = []
    for edge in edges:
        if shared_vertex not in edge:
            raise AssertionError("edge is not incident to the shared vertex")
        residual_endpoints.append(next(point for point in edge if point != shared_vertex))
    if len(set(residual_endpoints)) != 2:
        raise AssertionError("residual endpoints are not distinct")
    face = next(iter(faces))
    face_edges = {edge for kind, edge, f in difference if kind == "FE" and f == face}
    if face_edges != edges:
        raise AssertionError("both alternating edges must meet the same face")
    return face, shared_vertex, tuple(sorted(residual_endpoints))


def main(path: Path):
    data = json.loads(path.read_text())
    family = data["families"]["graph5"]
    count, witness_ids, patterns = 0, set(), set()
    for witness in family["witness_results"]:
        for permutation in witness["permutation_results"]:
            for certificate in permutation["diamond_certificates"]:
                if certificate["same_elementary_pair_set"]:
                    continue
                pattern = classify(certificate)
                if pattern is None:
                    continue
                count += 1
                witness_ids.add(witness["witness_id"])
                patterns.add((witness["witness_id"], witness["pair_index"], pattern))
    assert count == 64, count
    assert len(witness_ids) == 32, len(witness_ids)
    assert len(patterns) == 32, len(patterns)
    print(json.dumps({
        "schema": "PF-I16-FOUR-CELL-RHOMBUS-CORNER-AUDIT-v1",
        "graph5_four_cycle_certificate_count": count,
        "distinct_geometric_witness_count": len(witness_ids),
        "root_preserving_map_multiplicity": 2,
        "all_cases_have_one_face_two_edges_one_vertex": True,
        "all_cases_have_distinct_residual_endpoints": True,
        "two_edge_disk_strict_endpoint_equality_model_applies": False,
        "grandparent_arc_retention_verified": False,
        "restriction_naturality_verified": False,
        "geometric_L8_closed": False
    }, indent=2))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit(f"usage: {sys.argv[0]} path/to/pf_i16_four_support_relative_collapse_diamonds.json")
    main(Path(sys.argv[1]))
