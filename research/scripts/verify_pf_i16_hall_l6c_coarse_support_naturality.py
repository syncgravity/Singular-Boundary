#!/usr/bin/env python3
"""Finite L6c coarse support-naturality verifier for n=6 -> n=4.

This deliberately forgets individual matched-edge identities after deletion,
but preserves interval support simple-homotopy type, the complete intersection
diagram (including empty/nonempty intersections), relative deletion collapse,
and coherence among all marked projections to the same parent.

No Hall loads, deficiencies, flows, matching outcomes, or observer data enter.
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
import verify_pf_i16_hall_l45_bounded_support as l45
import verify_pf_i16_hall_l123_motif_lift as l123
import export_pf_i16_hall_source_records as hall


def cells_for_support(S, face_records):
    faces = set(S)
    edges = set().union(*(l45.face_edge_set(face_records[k]) for k in faces))
    vertices = set().union(*(set(face_records[k]) for k in faces))
    return faces, edges, vertices


def collapse_to_subcomplex(faces, edges, vertices,
                           target_faces, target_edges, target_vertices,
                           face_records):
    cur_f, cur_e, cur_v = set(faces), set(edges), set(vertices)
    tgt_f, tgt_e, tgt_v = (set(target_faces), set(target_edges),
                           set(target_vertices))
    steps = []
    while True:
        found = None
        for edge in sorted(cur_e - tgt_e):
            incident = [face for face in cur_f
                        if edge in l45.face_edge_set(face_records[face])]
            if len(incident) == 1 and incident[0] not in tgt_f:
                found = edge, incident[0]
                break
        if found is None:
            break
        edge, face = found
        cur_e.remove(edge)
        cur_f.remove(face)
        steps.append({"pair": "face-edge", "free_edge": [list(x) for x in edge],
                      "removed_face": [list(face[0]), face[1], face[2]]})

    while True:
        found = None
        for edge in sorted(cur_e - tgt_e):
            for vertex in edge:
                degree = sum(vertex in e for e in cur_e)
                in_face = any(vertex in face_records[face]
                              for face in cur_f)
                if vertex not in tgt_v and degree == 1 and not in_face:
                    found = vertex, edge
                    break
            if found is not None:
                break
        if found is None:
            break
        vertex, edge = found
        cur_e.remove(edge)
        cur_v.remove(vertex)
        steps.append({"pair": "edge-vertex", "free_vertex": list(vertex),
                      "removed_edge": [list(x) for x in edge]})

    return (cur_f == tgt_f and cur_e == tgt_e and cur_v == tgt_v), steps, {
        "extra_faces": len(cur_f - tgt_f),
        "extra_edges": len(cur_e - tgt_e),
        "extra_vertices": len(cur_v - tgt_v),
    }


def collapse_support_to_edge(S, face_records):
    faces, edges, vertices = cells_for_support(S, face_records)
    if not edges:
        return False, []
    target_edge = sorted(edges)[0]
    ok, steps, _ = collapse_to_subcomplex(
        faces, edges, vertices, set(), {target_edge}, set(target_edge),
        face_records)
    return ok, steps


def collapse_support_to_vertex(S, face_records):
    faces, edges, vertices = cells_for_support(S, face_records)
    if not vertices:
        return False, []
    target_vertex = sorted(vertices)[0]
    ok, steps, _ = collapse_to_subcomplex(
        faces, edges, vertices, set(), set(), {target_vertex}, face_records)
    return ok, steps


def intersection_cells(A, B, face_records):
    af, ae, av = cells_for_support(A, face_records)
    bf, be, bv = cells_for_support(B, face_records)
    return af & bf, ae & be, av & bv


def collapse_intersection_to_vertex(A, B, face_records):
    faces, edges, vertices = intersection_cells(A, B, face_records)
    if not vertices:
        return False, []
    target_vertex = sorted(vertices)[0]
    ok, steps, _ = collapse_to_subcomplex(
        faces, edges, vertices, set(), set(), {target_vertex}, face_records)
    return ok, steps


def union_cells(supports, face_records):
    cells = [cells_for_support(S, face_records) for S in supports]
    return (set().union(*(x[0] for x in cells)),
            set().union(*(x[1] for x in cells)),
            set().union(*(x[2] for x in cells)))


def collapse_union_to_vertex(supports, face_records):
    faces, edges, vertices = union_cells(supports, face_records)
    if not vertices:
        return False, []
    target_vertex = sorted(vertices)[0]
    return collapse_to_subcomplex(
        faces, edges, vertices, set(), set(), {target_vertex}, face_records)


def relative_delete_collapse(child_supports, retained_indices, face_records):
    retained = [child_supports[i] for i in retained_indices]
    all_cells = union_cells(child_supports, face_records)
    target_cells = union_cells(retained, face_records)
    return collapse_to_subcomplex(*all_cells, *target_cells, face_records)


def diagram_signature(supports, overlap_graph, face_records):
    support_contractible = []
    for support in supports:
        ok, _ = collapse_support_to_edge(support, face_records)
        support_contractible.append(ok)

    pair_records = []
    for i, j in itertools.combinations(range(len(supports)), 2):
        common = intersection_cells(supports[i], supports[j], face_records)
        nonempty = bool(common[2])
        expected = (i, j) in overlap_graph
        if nonempty != expected:
            raise AssertionError(("intersection nerve differs from full overlap graph",
                                  i, j, nonempty, expected))
        intersection_ok = not nonempty
        if nonempty:
            intersection_ok, _ = collapse_intersection_to_vertex(
                supports[i], supports[j], face_records)
            if not intersection_ok:
                raise AssertionError(("nonempty support intersection is not collapsible",
                                      i, j))
        pair_records.append({"pair": [i, j], "nonempty": nonempty,
                             "intersection_contractible": intersection_ok})
    union_ok, _ = collapse_union_to_vertex(supports, face_records)
    if not all(support_contractible) or not union_ok:
        raise AssertionError(("support diagram is not contractible in required pieces",
                              support_contractible, union_ok))
    return {
        "support_count": len(supports),
        "each_support_contractible": all(support_contractible),
        "pair_intersections": pair_records,
        "union_contractible": union_ok,
        "overlap_graph": [list(x) for x in sorted(overlap_graph)],
    }


def parent_key(parent):
    return (tuple(tuple(x) for x in parent["parent_intervals"]),
            tuple(tuple(x) for x in parent["parent_tree_edges"]))


def run_target(name, labels, edges, faces, records):
    face_records = l45.target_face_records(faces)
    options = [l45.support_options(face_records, edge)
               for edge in l45.MOTIF_EDGES]
    results_by_graph = {}
    for row in records:
        graph = l45.source_graph(row)
        if graph not in results_by_graph:
            selected, witnesses = l45.choose_supports(
                graph, len(row["intervals"]), options, face_records)
            if selected is None:
                raise AssertionError((name, "child support assignment missing", graph))
            results_by_graph[graph] = selected

    marks = 0
    relative_pass = 0
    diagram_pass = 0
    collapse_pair_counts = Counter()
    collapse_length_counts = Counter()
    intersection_type_counts = Counter()
    parent_origins = defaultdict(list)
    max_relative_steps = 0
    explicit_witness = None

    for row in records:
        child_graph = l45.source_graph(row)
        child_supports = results_by_graph[child_graph]
        for parent in row["parents"]:
            marks += 1
            mark = int(parent["deleted_interval_index"])
            retained_old = [i for i in range(len(child_supports)) if i != mark]
            retained_supports = [child_supports[i] for i in retained_old]

            parent_graph = {tuple(x) for x in parent["parent_full_overlap_edges"]}
            parent_supports, _ = l45.choose_supports(
                parent_graph, len(parent["parent_intervals"]), options, face_records)
            if parent_supports is None:
                raise AssertionError((name, "parent support assignment missing",
                                      parent_graph))

            child_sig = diagram_signature(retained_supports,
                                          {(i, j) for i, j in itertools.combinations(
                                              range(len(retained_supports)), 2)
                                           if tuple(sorted((retained_old[i],
                                                            retained_old[j]))) in child_graph},
                                          face_records)
            parent_sig = diagram_signature(parent_supports, parent_graph,
                                           face_records)
            if child_sig != parent_sig:
                raise AssertionError((name, "coarse parent diagram mismatch",
                                      row["intervals"], mark, child_sig, parent_sig))
            diagram_pass += 1

            ok, steps, remainder = relative_delete_collapse(
                child_supports, retained_old, face_records)
            if not ok:
                raise AssertionError((name, "relative deletion collapse failed",
                                      row["intervals"], mark, remainder))
            relative_pass += 1
            collapse_length_counts[len(steps)] += 1
            max_relative_steps = max(max_relative_steps, len(steps))
            for step in steps:
                collapse_pair_counts[step["pair"]] += 1

            common_f, common_e, common_v = intersection_cells(
                retained_supports[0], retained_supports[1], face_records)
            if common_f:
                intersection_type = "face"
            elif common_e:
                intersection_type = "edge-or-path"
            elif common_v:
                intersection_type = "vertex"
            else:
                intersection_type = "empty"
            intersection_type_counts[intersection_type] += 1

            pkey = parent_key(parent)
            parent_origins[pkey].append({
                "child_intervals": [list(x) for x in row["intervals"]],
                "child_tree": [list(x) for x in row["tree_edges"]],
                "deleted_interval_index": mark,
                "child_restriction_signature": child_sig,
                "parent_signature": parent_sig,
            })

            if (tuple(tuple(x) for x in row["intervals"]) ==
                    ((1, 4), (2, 5), (3, 6)) and
                    tuple(tuple(x) for x in row["tree_edges"]) ==
                    ((0, 1), (0, 2)) and mark in (1, 2)):
                explicit_witness = {
                    "child_intervals": [list(x) for x in row["intervals"]],
                    "deleted_interval_index": mark,
                    "parent_intervals": [list(x) for x in parent["parent_intervals"]],
                    "retained_child_support_face_counts": [len(x) for x in retained_supports],
                    "retained_child_intersection_type": intersection_type,
                    "coarse_diagram_signature": child_sig,
                }

    coherence_groups = {}
    for key, origins in parent_origins.items():
        signatures = {json.dumps(x["child_restriction_signature"], sort_keys=True)
                      for x in origins}
        parent_signatures = {json.dumps(x["parent_signature"], sort_keys=True)
                             for x in origins}
        if len(signatures) != 1 or len(parent_signatures) != 1 or signatures != parent_signatures:
            raise AssertionError((name, "parent coherence failure", key,
                                  len(signatures), len(parent_signatures)))
        coherence_groups[str(key)] = {
            "origin_count": len(origins),
            "coherent": True,
            "coarse_signature": origins[0]["parent_signature"],
        }

    return {
        "target": name,
        "vertices": len(labels),
        "edges": len(edges),
        "faces": len(faces),
        "marked_projections_checked": marks,
        "relative_deletion_collapses_passed": relative_pass,
        "coarse_diagram_comparisons_passed": diagram_pass,
        "parent_coherence_groups": len(coherence_groups),
        "parent_coherence_groups_passed": len(coherence_groups),
        "parent_origins_per_group": sorted(x["origin_count"]
                                            for x in coherence_groups.values()),
        "retained_intersection_types": dict(sorted(intersection_type_counts.items())),
        "relative_collapse_length_histogram": dict(sorted(collapse_length_counts.items())),
        "relative_collapse_pair_counts": dict(sorted(collapse_pair_counts.items())),
        "maximum_relative_collapse_pairs": max_relative_steps,
        "explicit_two_mark_witnesses": explicit_witness,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=None)
    args = parser.parse_args()
    labels_o, edges_o, faces_o, center, cutoff = l123.original_source_complex(7)
    labels_c, edges_c, faces_c = l123.completed_window_core(7, center, cutoff)
    records = hall.source_records(6)
    if len(records) != 22 or sum(len(x["parents"]) for x in records) != 30:
        raise AssertionError("order-six source/mark count mismatch")

    face_keys_o = set(l45.target_face_records(faces_o))
    face_keys_c = set(l45.target_face_records(faces_c))
    if not face_keys_c <= face_keys_o:
        raise AssertionError("completed core face population is not contained in source replay")

    original = run_target("PF-I16 original-source replay",
                          labels_o, edges_o, faces_o, records)
    core = run_target("PF-I11 completed-window core",
                      labels_c, edges_c, faces_c, records)
    for field in ("marked_projections_checked",
                  "relative_deletion_collapses_passed",
                  "coarse_diagram_comparisons_passed",
                  "parent_coherence_groups_passed",
                  "retained_intersection_types",
                  "relative_collapse_length_histogram",
                  "relative_collapse_pair_counts"):
        if original[field] != core[field]:
            raise AssertionError(("target domains disagree", field,
                                  original[field], core[field]))

    result = {
        "schema": "PF-I16-HALL-L6C-COARSE-SUPPORT-NATURALITY-v1",
        "scope": "Ngrid=7 target domains; all n=6 sources and eligible marks; n=4 parents",
        "PF_I16_original_source": original,
        "PF_I11_completed_window_core": core,
        "nonclaims": [
            "does not preserve individual matched-edge identities across deletion",
            "does not establish L7 ordered-boundary compatibility",
            "does not establish L8 all-orders construction",
            "does not prove the all-orders Hall inequality",
        ],
    }
    payload = json.dumps(result, sort_keys=True, indent=2) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(payload)
    print(payload, end="")


if __name__ == "__main__":
    main()
