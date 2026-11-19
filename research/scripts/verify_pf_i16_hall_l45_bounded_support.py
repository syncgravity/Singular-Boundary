#!/usr/bin/env python3
"""Bounded L4-L5 support and overlap-witness check for PF-I16 Hall sources.

The target-side port/matching-edge map is imported unchanged from the frozen
L1-L3 verifier. This script constructs connected one- or two-rhombus supports
whose distinguished matching edge is on the support boundary, then checks
the exact full interval-overlap graph (including non-tree edges).

No Hall loads, deficiencies, flows, matchings, observer phases, or helical
coordinates are used to choose supports.
"""
from __future__ import annotations
import argparse
import itertools
import json
from collections import Counter, defaultdict
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import verify_pf_i16_hall_l123_motif_lift as l123
import export_pf_i16_hall_source_records as hall

NGRID = 7
MOTIF_EDGES = l123.MOTIF_EDGES


def as_label(v):
    return tuple(int(x) for x in v)


def face_key(face):
    vertices = [as_label(v) for v in face]
    lower = tuple(min(v[j] for v in vertices) for j in range(5))
    upper = tuple(max(v[j] for v in vertices) for j in range(5))
    dirs = tuple(j for j in range(5) if upper[j] - lower[j] == 1)
    if len(dirs) != 2 or any(upper[j] != lower[j] for j in range(5) if j not in dirs):
        raise AssertionError(("not an elementary rhombus", face))
    j, k = dirs
    expected = tuple(as_label(v) for v in l123.face_tuple(lower, j, k))
    if tuple(vertices) != expected:
        raise AssertionError(("noncanonical face order", face, expected))
    return (lower, j, k)


def face_sort_key(key):
    return (key[0], key[1], key[2])


def is_elementary_edge(a, b):
    return sum(abs(x-y) for x, y in zip(a, b)) == 1


def target_face_records(faces):
    out = {}
    for face in faces:
        key = face_key(face)
        if key in out:
            raise AssertionError(("duplicate accepted face", key))
        out[key] = frozenset(as_label(v) for v in face)
    return out


def face_edge_set(vertices):
    return frozenset(tuple(sorted((a, b)))
                     for a, b in itertools.combinations(vertices, 2)
                     if is_elementary_edge(a, b))


def support_options(face_records, edge):
    """All connected supports of <=2 faces with the matched edge on boundary."""
    a, b, direction = edge
    a, b = as_label(a), as_label(b)
    keys = sorted(face_records, key=face_sort_key)
    incident = [key for key in keys if a in face_records[key] and b in face_records[key]]
    if len(incident) != 2:
        raise AssertionError(("expected two accepted incident rhombi", edge, incident))

    face_edges = {key: face_edge_set(face_records[key]) for key in keys}
    adjacency = {key: set() for key in keys}
    edge_to_faces = defaultdict(set)
    for key in keys:
        for e in face_edges[key]:
            edge_to_faces[e].add(key)
    for incident_faces in edge_to_faces.values():
        for x, y in itertools.combinations(incident_faces, 2):
            adjacency[x].add(y)
            adjacency[y].add(x)

    supports = set()
    for root in incident:
        supports.add(frozenset((root,)))
        for neighbor in adjacency[root]:
            S = frozenset((root, neighbor))
            # The distinguished matching edge remains a boundary 1-cell.
            count = sum(a in face_records[k] and b in face_records[k] for k in S)
            if count == 1:
                supports.add(S)

    ordered = sorted(supports,
                     key=lambda S: tuple(sorted(face_sort_key(k) for k in S)))
    if len(ordered) != 8:
        raise AssertionError(("unexpected bounded support candidate count", edge, len(ordered)))
    for S in ordered:
        if len(S) == 2:
            x, y = tuple(S)
            if not (face_edges[x] & face_edges[y]):
                raise AssertionError(("two-face support is not edge-connected", S))
        if sum(a in face_records[k] and b in face_records[k] for k in S) != 1:
            raise AssertionError(("matched edge is not on support boundary", edge, S))
    return ordered


def support_vertices(S, face_records):
    return frozenset().union(*(face_records[k] for k in S))


def support_edges(S, face_records):
    return frozenset().union(*(face_edge_set(face_records[k]) for k in S))


def intersection_witness(S, T, face_records):
    """Return a canonical strongest shared cell: face, then edge, then vertex."""
    common_faces = sorted(S & T, key=face_sort_key)
    if common_faces:
        key = common_faces[0]
        return {"type": "shared_face",
                "face": {"lower": list(key[0]), "directions": [key[1], key[2]]}}

    common_edges = sorted(support_edges(S, face_records) &
                          support_edges(T, face_records))
    if common_edges:
        a, b = common_edges[0]
        return {"type": "shared_edge", "vertices": [list(a), list(b)]}

    common_vertices = sorted(support_vertices(S, face_records) &
                             support_vertices(T, face_records))
    if common_vertices:
        return {"type": "shared_vertex", "vertex": list(common_vertices[0])}
    return None


def source_graph(record):
    return {tuple(sorted((int(i), int(j))))
            for i, j in record["full_overlap_edges"]}


def choose_supports(graph, s, options, face_records):
    """Lexicographically first exact-intersection realization of the full graph."""
    for indices in itertools.product(*[range(len(options[i])) for i in range(s)]):
        selected = [options[i][indices[i]] for i in range(s)]
        witnesses = {}
        valid = True
        for i, j in itertools.combinations(range(s), 2):
            witness = intersection_witness(selected[i], selected[j], face_records)
            if ((i, j) in graph) != (witness is not None):
                valid = False
                break
            witnesses[(i, j)] = witness
        if valid:
            return selected, witnesses
    return None, None


def check_target(name, labels, edges, faces, records, core_face_signatures=None):
    face_records = target_face_records(faces)
    options = [support_options(face_records, edge) for edge in MOTIF_EDGES]
    if core_face_signatures is not None:
        for opts in options:
            for S in opts:
                if not all(k in core_face_signatures for k in S):
                    raise AssertionError((name, "support absent from completed core", S))

    results_by_graph = {}
    witness_counts = Counter()
    source_count = 0
    support_face_count = 0
    min_vertex_margin = float("inf")
    min_face_margin = float("inf")
    max_faces_per_support = 0
    pattern_counts = Counter()

    for record in records:
        intervals = [tuple(x) for x in record["intervals"]]
        s = len(intervals)
        graph = source_graph(record)
        graph_key = (s, tuple(sorted(graph)))
        if graph_key not in results_by_graph:
            selected, witnesses = choose_supports(graph, s, options, face_records)
            if selected is None:
                raise AssertionError((name, "no L4-L5 support assignment", graph_key))
            results_by_graph[graph_key] = (selected, witnesses)

        selected, witnesses = results_by_graph[graph_key]
        # Verify each interval support and its oriented lower-to-upper boundary trace.
        for i, (p, q) in enumerate(intervals):
            a, b, direction = MOTIF_EDGES[i]
            a, b = as_label(a), as_label(b)
            if tuple(b[t] - a[t] for t in range(5)) != tuple(int(t == direction) for t in range(5)):
                raise AssertionError(("signed matching edge changed", i))
            S = selected[i]
            if not S or len(S) > 2:
                raise AssertionError(("support size outside tested bound", S))
            if sum(a in face_records[k] and b in face_records[k] for k in S) != 1:
                raise AssertionError(("oriented matching edge not on support boundary", i, S))
            if len(S) == 2:
                x, y = tuple(S)
                if not (face_edge_set(face_records[x]) & face_edge_set(face_records[y])):
                    raise AssertionError(("support not connected along an edge", i, S))
            # The interval's ordered trace is the boundary edge Phi(p) -> Phi(q).
            if p >= q:
                raise AssertionError(("interval endpoint order reversed", p, q))
            if a not in labels or b not in labels or (a, b) not in edges:
                raise AssertionError(("support endpoint/edge absent from target", i))
            for key in S:
                if key not in face_records:
                    raise AssertionError(("support face absent from target", key))
                support_face_count += 1
                max_faces_per_support = max(max_faces_per_support, len(S))
                min_face_margin = min(min_face_margin,
                                      l123.face_margin(key[0], key[1], key[2]))
                for v in face_records[key]:
                    min_vertex_margin = min(min_vertex_margin, l123.window_margin(v))

        # L5 is checked against every edge of the full overlap graph, not just tau.
        for i, j in itertools.combinations(range(s), 2):
            witness = witnesses[(i, j)]
            if (i, j) in graph:
                if witness is None:
                    raise AssertionError(("missing full-graph overlap witness", i, j))
                witness_counts[witness["type"]] += 1
            elif witness is not None:
                raise AssertionError(("non-overlapping intervals share support incidence",
                                      i, j, witness))
        source_count += 1
        pattern_counts[str(graph_key)] += 1

    assignment_report = {}
    for graph_key, (selected, witnesses) in sorted(results_by_graph.items()):
        assignment_report[str(graph_key)] = {
            "supports": [
                [{"lower": list(k[0]), "directions": [k[1], k[2]]}
                 for k in sorted(S, key=face_sort_key)]
                for S in selected
            ],
            "witnesses": {
                f"{i+1}-{j+1}": witnesses[(i, j)]
                for i, j in itertools.combinations(range(len(selected)), 2)
            }
        }

    return {
        "target": name,
        "vertices": len(labels),
        "edges": len(edges),
        "faces": len(faces),
        "hall_sources_checked": source_count,
        "L4_sources_passed": source_count,
        "L5_sources_passed": source_count,
        "distinct_full_overlap_patterns": len(results_by_graph),
        "full_overlap_pattern_counts": dict(sorted(pattern_counts.items())),
        "support_candidates_per_interval_edge": [len(x) for x in options],
        "maximum_faces_per_interval_support": max_faces_per_support,
        "support_face_occurrences_checked": support_face_count,
        "typed_full_overlap_witness_counts": dict(sorted(witness_counts.items())),
        "support_assignments_by_full_overlap_pattern": assignment_report,
        "nonoverlap_pairs_with_shared_incidence": 0,
        "minimum_support_vertex_window_margin": min_vertex_margin,
        "minimum_support_face_triangle_margin": min_face_margin,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=None)
    args = parser.parse_args()

    labels_o, edges_o, faces_o, center, cutoff = l123.original_source_complex(NGRID)
    labels_c, edges_c, faces_c = l123.completed_window_core(NGRID, center, cutoff)
    if (len(labels_o), len(edges_o), len(faces_o)) != (1550, 3017, 1468):
        raise AssertionError("PF-I16 original-source Ngrid=7 population mismatch")
    if (len(labels_c), len(edges_c), len(faces_c)) != (1432, 2761, 1330):
        raise AssertionError("PF-I11 completed-core Ngrid=7 population mismatch")
    if l123.sha_labels(labels_c) != l123.EXPECTED_CORE_LABEL_SHA:
        raise AssertionError("PF-I11 completed-core vertex hash mismatch")
    if l123.sha_faces(faces_c) != l123.EXPECTED_CORE_FACE_SHA:
        raise AssertionError("PF-I11 completed-core face hash mismatch")

    face_records_o = target_face_records(faces_o)
    face_records_c = target_face_records(faces_c)
    common_faces = set(face_records_o) & set(face_records_c)
    # The completed-core rhombi must all occur in the original-source replay.
    if len(common_faces) != len(face_records_c):
        raise AssertionError(("completed-core faces are not contained in source replay",
                              len(common_faces), len(face_records_c)))
    records = {n: hall.source_records(n) for n in (4, 6)}
    if len(records[4]) != 2 or len(records[6]) != 22:
        raise AssertionError("Hall source enumeration count mismatch")

    result = {
        "schema": "PF-I16-HALL-L45-BOUNDED-SUPPORT-v1",
        "scope": "Ngrid=7 finite targets; Hall source orders n=4,6; L4-L5 only",
        "target_center": center.tolist(),
        "target_cutoff": cutoff,
        "common_accepted_face_count": len(common_faces),
        "orders": {}
    }
    for n in (4, 6):
        rows = records[n]
        original_result = check_target(
            "PF-I16 original-source replay", labels_o, edges_o, faces_o, rows,
            core_face_signatures=common_faces)
        core_result = check_target(
            "PF-I11 completed-window core", labels_c, edges_c, faces_c, rows,
            core_face_signatures=common_faces)
        if (original_result["support_assignments_by_full_overlap_pattern"] !=
                core_result["support_assignments_by_full_overlap_pattern"]):
            raise AssertionError(("the two target domains selected different supports", n))
        result["orders"][str(n)] = {
            "source_count": len(rows),
            "PF_I16_original_source": original_result,
            "PF_I11_completed_window_core": core_result,
        }
    result["nonclaims"] = [
        "L6 parent naturality and support deletion",
        "L7 global port-order compatibility beyond each interval trace",
        "L8 all-orders construction",
        "helical observer phases",
        "Hall theorem"
    ]
    payload = json.dumps(result, sort_keys=True, indent=2) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(payload)
    print(payload, end="")


if __name__ == "__main__":
    main()
