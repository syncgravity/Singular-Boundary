#!/usr/bin/env python3
"""Necessary L7b oriented-boundary position test for frozen PF-I16 supports.

The test anchors each support boundary at its distinguished lower-to-upper
matched edge. It compares the relative position of the retained pairwise
intersection footprint with respect to that directed edge, before and after
each eligible parent deletion. This is a necessary invariant for any
orientation-preserving boundary equivalence that preserves the marked edge.

A mismatch is a genuine obstruction to the frozen support family under this
relative-order convention; a match is not a complete L7b proof.
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


def oriented_boundary_cycle(S, face_records, distinguished_edge):
    """Return the support boundary cycle beginning with the directed edge."""
    edge_counts = Counter()
    for key in S:
        edge_counts.update(l45.face_edge_set(face_records[key]))
    boundary = [edge for edge, count in edge_counts.items() if count == 1]
    adj = defaultdict(list)
    for a, b in boundary:
        adj[a].append(b)
        adj[b].append(a)
    if not adj or any(len(neighbors) != 2 for neighbors in adj.values()):
        raise AssertionError(("support boundary is not one cycle", S, adj))

    tail, head = distinguished_edge
    if tuple(sorted((tail, head))) not in set(boundary):
        raise AssertionError(("distinguished edge is not on support boundary",
                              distinguished_edge, S))
    cycle = [tail, head]
    previous, current = tail, head
    while True:
        choices = [v for v in adj[current] if v != previous]
        if len(choices) != 1:
            raise AssertionError(("boundary continuation is not unique",
                                  current, choices))
        nxt = choices[0]
        if nxt == tail:
            break
        if nxt in cycle:
            raise AssertionError(("boundary walk self-intersects", cycle, nxt))
        cycle.append(nxt)
        previous, current = current, nxt
    if len(cycle) != len(adj):
        raise AssertionError(("boundary cycle omitted vertices",
                              len(cycle), len(adj)))
    return cycle


def support_cells(S, face_records):
    faces = set(S)
    edges = set().union(*(l45.face_edge_set(face_records[k]) for k in faces))
    vertices = set().union(*(set(face_records[k]) for k in faces))
    return faces, edges, vertices


def footprint_record(S, T, face_records, distinguished_edge):
    """Record the shared subcomplex as seen on S's oriented boundary."""
    cycle = oriented_boundary_cycle(S, face_records, distinguished_edge)
    boundary_edges = [
        tuple(sorted((cycle[i], cycle[(i + 1) % len(cycle)])))
        for i in range(len(cycle))
    ]
    _, se, sv = support_cells(S, face_records)
    _, te, tv = support_cells(T, face_records)
    shared_edges = se & te
    shared_vertices = sv & tv
    edge_positions = [i for i, edge in enumerate(boundary_edges)
                      if edge in shared_edges]
    vertex_positions = [i for i, vertex in enumerate(cycle)
                        if vertex in shared_vertices]
    tail, head = distinguished_edge
    marked = tuple(sorted((tail, head))) in shared_edges

    if marked:
        category = "contains_marked_edge"
    elif tail in shared_vertices and head in shared_vertices:
        category = "both_endpoints_without_marked_edge"
    elif tail in shared_vertices:
        category = "tail_endpoint_only"
    elif head in shared_vertices:
        category = "head_endpoint_only"
    elif edge_positions or vertex_positions:
        category = "open_complementary_arc"
    else:
        category = "empty"

    return {
        "category": category,
        "boundary_cycle": [list(v) for v in cycle],
        "boundary_length": len(cycle),
        "footprint_edge_positions": edge_positions,
        "footprint_vertex_positions": vertex_positions,
        "contains_distinguished_edge": marked,
        "contains_tail": tail in shared_vertices,
        "contains_head": head in shared_vertices,
        "shared_face_count": len(set(S) & set(T)),
        "shared_edge_count": len(shared_edges),
        "shared_vertex_count": len(shared_vertices),
    }


def graph_key(edges):
    return tuple(sorted(tuple(x) for x in edges))


def parent_key(parent):
    return (tuple(tuple(x) for x in parent["parent_intervals"]),
            tuple(tuple(x) for x in parent["parent_tree_edges"]))


def assignment(graph, count, options, face_records):
    selected, _ = l45.choose_supports(graph, count, options, face_records)
    if selected is None:
        raise AssertionError(("no frozen L4-L5 support assignment", graph, count))
    return selected


def run_target(name, labels, edges, faces, records):
    face_records = l45.target_face_records(faces)
    options = [l45.support_options(face_records, edge)
               for edge in l45.MOTIF_EDGES]

    assignments = {}
    def get_assignment(graph, count):
        key = (tuple(sorted(graph)), count)
        if key not in assignments:
            assignments[key] = assignment(graph, count, options, face_records)
        return assignments[key]

    projection_rows = []
    group_rows = defaultdict(list)
    failure_count = 0
    interval_comparisons = 0
    interval_mismatches = 0
    mismatch_by_graph_and_mark = Counter()

    for row in records:
        child_graph = {tuple(x) for x in row["full_overlap_edges"]}
        child_supports = get_assignment(child_graph, len(row["intervals"]))
        for parent in row["parents"]:
            mark = int(parent["deleted_interval_index"])
            retained_old = [i for i in range(len(child_supports)) if i != mark]
            parent_graph = {tuple(x) for x in parent["parent_full_overlap_edges"]}
            parent_supports = get_assignment(parent_graph, len(parent["parent_intervals"]))
            if len(retained_old) != 2 or len(parent_supports) != 2:
                raise AssertionError("L7b finite test expects two retained intervals")

            child_pair = tuple(sorted((retained_old[0], retained_old[1])))
            parent_pair = (0, 1)
            child_overlaps = child_pair in child_graph
            parent_overlaps = parent_pair in parent_graph
            if child_overlaps != parent_overlaps:
                raise AssertionError(("parent deletion changed retained overlap",
                                      row["intervals"], mark))

            interval_records = []
            for parent_index, old_index in enumerate(retained_old):
                if child_overlaps:
                    other_old = retained_old[1 - parent_index]
                    child_fp = footprint_record(
                        child_supports[old_index], child_supports[other_old],
                        face_records, l45.MOTIF_EDGES[old_index][:2])
                    parent_fp = footprint_record(
                        parent_supports[parent_index], parent_supports[1-parent_index],
                        face_records, l45.MOTIF_EDGES[parent_index][:2])
                else:
                    child_fp = {"category": "empty"}
                    parent_fp = {"category": "empty"}

                interval_comparisons += 1
                same = child_fp["category"] == parent_fp["category"]
                if not same:
                    interval_mismatches += 1
                interval_records.append({
                    "retained_child_interval_index": old_index,
                    "parent_interval_index": parent_index,
                    "child_footprint": child_fp,
                    "parent_footprint": parent_fp,
                    "relative_position_class_matches": same,
                })

            projection_pass = all(x["relative_position_class_matches"]
                                  for x in interval_records)
            if not projection_pass:
                failure_count += 1
                mismatch_by_graph_and_mark[
                    (graph_key(child_graph), mark)] += 1

            child_word = tuple(x["child_footprint"]["category"]
                               for x in interval_records)
            parent_word = tuple(x["parent_footprint"]["category"]
                                for x in interval_records)
            pkey = parent_key(parent)
            group_rows[pkey].append({
                "child_word": child_word,
                "parent_word": parent_word,
                "projection_pass": projection_pass,
            })
            projection_rows.append({
                "child_intervals": [list(x) for x in row["intervals"]],
                "child_tree_edges": [list(x) for x in row["tree_edges"]],
                "child_full_overlap_edges": [list(x) for x in sorted(child_graph)],
                "deleted_interval_index": mark,
                "parent_intervals": parent["parent_intervals"],
                "parent_tree_edges": parent["parent_tree_edges"],
                "interval_comparisons": interval_records,
                "projection_pass": projection_pass,
            })

    groups = []
    for key, origins in sorted(group_rows.items()):
        child_words = sorted({x["child_word"] for x in origins})
        parent_words = sorted({x["parent_word"] for x in origins})
        groups.append({
            "parent_intervals": [list(x) for x in key[0]],
            "parent_tree_edges": [list(x) for x in key[1]],
            "origin_count": len(origins),
            "distinct_child_restriction_words": [list(x) for x in child_words],
            "distinct_parent_words": [list(x) for x in parent_words],
            "origins_not_matching_parent_word": sum(
                x["child_word"] != x["parent_word"] for x in origins),
            "coherent": len(child_words) == 1 and child_words == parent_words,
        })

    return {
        "target": name,
        "vertices": len(labels),
        "edges": len(edges),
        "faces": len(faces),
        "marked_projections_checked": len(projection_rows),
        "necessary_interval_position_comparisons": interval_comparisons,
        "interval_position_mismatches": interval_mismatches,
        "projections_failing_necessary_position_test": failure_count,
        "projections_passing_necessary_position_test":
            len(projection_rows) - failure_count,
        "failure_counts_by_child_overlap_graph_and_deleted_index": [
            {"graph": [list(x) for x in graph], "deleted_interval_index": mark,
             "failures": count}
            for (graph, mark), count in sorted(mismatch_by_graph_and_mark.items())
        ],
        "parent_coherence_groups": groups,
        "projection_certificates": projection_rows,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=None)
    args = parser.parse_args()

    labels_o, edges_o, faces_o, center, cutoff = l123.original_source_complex(7)
    labels_c, edges_c, faces_c = l123.completed_window_core(7, center, cutoff)
    if (len(labels_o), len(edges_o), len(faces_o)) != (1550, 3017, 1468):
        raise AssertionError("PF-I16 Ngrid=7 population mismatch")
    if (len(labels_c), len(edges_c), len(faces_c)) != (1432, 2761, 1330):
        raise AssertionError("PF-I11 Ngrid=7 population mismatch")

    records = hall.source_records(6)
    if len(records) != 22 or sum(len(x["parents"]) for x in records) != 30:
        raise AssertionError("order-six source/mark count mismatch")

    faces_o_keys = set(l45.target_face_records(faces_o))
    faces_c_keys = set(l45.target_face_records(faces_c))
    if not faces_c_keys <= faces_o_keys:
        raise AssertionError("PF-I11 completed-core faces not contained in PF-I16 replay")

    original = run_target("PF-I16 original-source replay",
                          labels_o, edges_o, faces_o, records)
    core = run_target("PF-I11 completed-window core",
                      labels_c, edges_c, faces_c, records)
    comparable = (
        "marked_projections_checked",
        "necessary_interval_position_comparisons",
        "interval_position_mismatches",
        "projections_failing_necessary_position_test",
        "projections_passing_necessary_position_test",
        "failure_counts_by_child_overlap_graph_and_deleted_index",
        "parent_coherence_groups",
        "projection_certificates",
    )
    for field in comparable:
        if original[field] != core[field]:
            raise AssertionError(("target domains disagree", field))

    result = {
        "schema": "PF-I16-HALL-L7B-ORIENTED-BOUNDARY-POSITION-v1",
        "scope": "Ngrid=7 target domains; all n=6 sources and eligible marks; n=4 parents",
        "criterion": (
            "necessary relative-position invariant under orientation-preserving "
            "boundary equivalence preserving the distinguished directed matched edge"
        ),
        "interpretation": (
            "A mismatch disproves L7b for the frozen support family under this "
            "relative convention. A match is only a necessary-condition pass, "
            "not a complete boundary-word equivalence proof."
        ),
        "PF_I16_original_source": original,
        "PF_I11_completed_window_core": core,
        "nonclaims": [
            "does not prove L7b for projections passing the necessary test",
            "does not prove no alternative L4-L5 support assignment can satisfy L7b",
            "does not establish L8 or the all-orders Hall inequality",
        ],
    }
    payload = json.dumps(result, sort_keys=True, indent=2) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(payload)
    print(payload, end="")


if __name__ == "__main__":
    main()
