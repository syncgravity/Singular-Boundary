#!/usr/bin/env python3
"""Full finite L6c/L7b check for the demand-independent alternative triple.

The support assignment is frozen from the target-only search dated 2026-11-19.
No Hall demands, loads, deficiencies, matching outcomes, or flows are read.
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

NGRID = 7
EDGES = [
    ((-7, -4, 5, 7, 0), (-6, -4, 5, 7, 0)),
    ((-7, -3, 5, 7, -1), (-7, -3, 6, 7, -1)),
    ((-6, -3, 5, 6, -1), (-6, -3, 5, 6, 0)),
]
def fk(lower, j, k):
    return (tuple(lower), j, k)

STAR = [
    {fk((-7, -4, 5, 7, 0), 0, 1)},
    {fk((-7, -3, 5, 7, -1), 2, 4)},
    {fk((-6, -3, 4, 6, 0), 2, 3), fk((-6, -3, 5, 6, -1), 3, 4)},
]
PATH = [
    {fk((-7, -4, 5, 7, 0), 0, 1)},
    {fk((-7, -3, 5, 7, -1), 0, 2), fk((-7, -3, 5, 7, -1), 0, 4)},
    {fk((-6, -3, 5, 6, -1), 1, 3), fk((-6, -3, 5, 6, -1), 1, 4)},
]
TRIANGLE = [
    {fk((-7, -4, 5, 7, 0), 0, 1)},
    {fk((-7, -3, 5, 7, -1), 0, 2), fk((-7, -3, 5, 7, -1), 0, 4)},
    {fk((-6, -3, 4, 6, 0), 2, 3), fk((-6, -3, 5, 6, -1), 3, 4)},
]
SUPPORTS = {
    frozenset({(0, 1), (0, 2)}): STAR,
    frozenset({(0, 1), (1, 2)}): PATH,
    frozenset({(0, 1), (0, 2), (1, 2)}): TRIANGLE,
}
# The n=4 parent has two intervals and one full-overlap edge. This fixed
# parent assignment is the first two PATH supports, independent of origin.
PARENT_SUPPORTS = PATH[:2]
PARENT_GRAPH = frozenset({(0, 1)})

def norm_edge(e):
    return tuple(sorted((tuple(map(int, e[0])), tuple(map(int, e[1])))))

def source_graph(row):
    return frozenset(tuple(sorted(map(int, e))) for e in row["full_overlap_edges"])

def parent_key(parent):
    return (tuple(tuple(x) for x in parent["parent_intervals"]),
            tuple(tuple(x) for x in parent["parent_tree_edges"]))

def cells(S, face_records):
    fs = set(S)
    es = set().union(*(l45.face_edge_set(face_records[k]) for k in fs))
    vs = set().union(*(set(face_records[k]) for k in fs))
    return fs, es, vs

def collapse(src, tgt, face_records):
    cf, ce, cv = map(set, src)
    tf, te, tv = map(set, tgt)
    steps = []
    while True:
        found = None
        for edge in sorted(ce - te):
            incident = [face for face in cf
                        if edge in l45.face_edge_set(face_records[face])]
            if len(incident) == 1 and incident[0] not in tf:
                found = edge, incident[0]
                break
        if found is None:
            break
        edge, face = found
        ce.remove(edge)
        cf.remove(face)
        steps.append({"pair": "face-edge",
                      "free_edge": [list(x) for x in edge],
                      "removed_face": [list(face[0]), face[1], face[2]]})
    while True:
        found = None
        for edge in sorted(ce - te):
            for vertex in edge:
                degree = sum(vertex in e for e in ce)
                in_face = any(vertex in face_records[f] for f in cf)
                if vertex not in tv and degree == 1 and not in_face:
                    found = vertex, edge
                    break
            if found is not None:
                break
        if found is None:
            break
        vertex, edge = found
        ce.remove(edge)
        cv.remove(vertex)
        steps.append({"pair": "edge-vertex",
                      "free_vertex": list(vertex),
                      "removed_edge": [list(x) for x in edge]})
    remainder = {"extra_faces": len(cf - tf),
                 "extra_edges": len(ce - te),
                 "extra_vertices": len(cv - tv)}
    return cf == tf and ce == te and cv == tv, steps, remainder

def union_cells(supports, face_records):
    parts = [cells(S, face_records) for S in supports]
    return tuple(set().union(*(p[i] for p in parts)) for i in range(3))

def intersection_cells(A, B, face_records):
    a, b = cells(A, face_records), cells(B, face_records)
    return tuple(a[i] & b[i] for i in range(3))

def collapse_to_edge(S, face_records):
    f, e, v = cells(S, face_records)
    target = sorted(e)[0]
    return collapse((f, e, v), (set(), {target}, set(target)), face_records)

def collapse_intersection(A, B, face_records):
    f, e, v = intersection_cells(A, B, face_records)
    if not v:
        return False, [], {"empty": True}
    target = {sorted(v)[0]}
    return collapse((f, e, v), (set(), set(), target), face_records)

def diagram_signature(supports, graph, face_records):
    support_ok = [collapse_to_edge(S, face_records)[0] for S in supports]
    pair_rows = []
    for i, j in itertools.combinations(range(len(supports)), 2):
        f, e, v = intersection_cells(supports[i], supports[j], face_records)
        nonempty = bool(v)
        expected = (i, j) in graph
        if nonempty != expected:
            raise AssertionError(("intersection nerve mismatch", i, j, nonempty, expected))
        ok = True
        if nonempty:
            ok = collapse_intersection(supports[i], supports[j], face_records)[0]
        if not ok:
            raise AssertionError(("nonempty intersection not collapsible", i, j))
        pair_rows.append({"pair": [i, j], "nonempty": nonempty,
                          "intersection_contractible": ok})
    u = union_cells(supports, face_records)
    union_ok = collapse(u, (set(), set(), {sorted(u[2])[0]}), face_records)[0]
    if not all(support_ok) or not union_ok:
        raise AssertionError(("support diagram not contractible", support_ok, union_ok))
    return {
        "support_count": len(supports),
        "each_support_contractible": all(support_ok),
        "pair_intersections": pair_rows,
        "union_contractible": union_ok,
        "overlap_graph": [list(x) for x in sorted(graph)],
    }

def relative_delete(child_supports, retained, face_records):
    return collapse(union_cells(child_supports, face_records),
                    union_cells([child_supports[i] for i in retained], face_records),
                    face_records)

def oriented_boundary(S, face_records, directed_edge):
    counts = Counter()
    for face in S:
        counts.update(l45.face_edge_set(face_records[face]))
    boundary = [e for e, count in counts.items() if count == 1]
    adj = defaultdict(list)
    for a, b in boundary:
        adj[a].append(b)
        adj[b].append(a)
    if not adj or any(len(v) != 2 for v in adj.values()):
        raise AssertionError(("support boundary is not one cycle", S))
    tail, head = directed_edge
    if tuple(sorted((tail, head))) not in set(boundary):
        raise AssertionError(("marked edge not on boundary", directed_edge, S))
    cycle = [tail, head]
    previous, current = tail, head
    while True:
        choices = [v for v in adj[current] if v != previous]
        if len(choices) != 1:
            raise AssertionError(("nonunique boundary continuation", current, choices))
        nxt = choices[0]
        if nxt == tail:
            break
        if nxt in cycle:
            raise AssertionError(("boundary cycle self-intersection", cycle, nxt))
        cycle.append(nxt)
        previous, current = current, nxt
    if len(cycle) != len(adj):
        raise AssertionError(("boundary cycle incomplete", len(cycle), len(adj)))
    return cycle

def full_footprint(S, T, face_records, directed_edge):
    cycle = oriented_boundary(S, face_records, directed_edge)
    _, se, sv = cells(S, face_records)
    _, te, tv = cells(T, face_records)
    shared_edges, shared_vertices = se & te, sv & tv
    boundary_edges = {
        tuple(sorted((cycle[i], cycle[(i + 1) % len(cycle)])))
        for i in range(len(cycle))
    }
    if not shared_vertices:
        raise AssertionError("retained overlap footprint is empty")
    if not shared_edges and len(shared_vertices) == 1:
        shape = "vertex"
        vertex = next(iter(shared_vertices))
        if vertex not in cycle:
            raise AssertionError("shared vertex is not on support boundary")
        positions = [cycle.index(vertex)]
    elif len(shared_edges) == 1 and len(shared_vertices) == 2:
        shape = "edge"
        edge = next(iter(shared_edges))
        if edge not in boundary_edges or set(edge) != set(shared_vertices):
            raise AssertionError("shared edge is not one boundary cell")
        positions = [i for i in range(len(cycle))
                     if tuple(sorted((cycle[i], cycle[(i + 1) % len(cycle)]))) == edge]
    else:
        raise AssertionError(("footprint is not one connected boundary cell",
                              len(shared_edges), len(shared_vertices)))
    tail, head = directed_edge
    if tuple(sorted(directed_edge)) in shared_edges:
        category = "contains_marked_edge"
    elif tail in shared_vertices and head in shared_vertices:
        category = "both_endpoints_without_marked_edge"
    elif tail in shared_vertices:
        category = "tail_endpoint_only"
    elif head in shared_vertices:
        category = "head_endpoint_only"
    else:
        category = "open_complementary_arc"
    # The complementary arc is oriented head -> ... -> tail.
    arc = [head]
    index = cycle.index(head)
    while True:
        index = (index + 1) % len(cycle)
        arc.append(cycle[index])
        if cycle[index] == tail:
            break
    if category == "open_complementary_arc":
        if shape == "vertex":
            if next(iter(shared_vertices)) not in arc[1:-1]:
                raise AssertionError("vertex footprint is not strictly inside open arc")
        else:
            if shared_vertices & {tail, head}:
                raise AssertionError("edge footprint touches marked endpoint")
            if positions[0] == 0:
                raise AssertionError("edge footprint is the marked edge")
    return {
        "category": category,
        "shape": shape,
        "boundary_length": len(cycle),
        "boundary_cycle": [list(v) for v in cycle],
        "footprint_positions": positions,
        "footprint_vertices": [list(v) for v in sorted(shared_vertices)],
        "footprint_edges": [[list(a), list(b)] for a, b in sorted(shared_edges)],
        "complementary_arc_order": [list(v) for v in arc],
    }

def validate_support_family(supports, face_records, target_edges):
    for i, S in enumerate(supports):
        if not S or not S <= face_records.keys():
            raise AssertionError(("support face absent", i, S))
        a, b = EDGES[i]
        if a not in target_edges[0] or b not in target_edges[0]:
            raise AssertionError(("support endpoint absent", i, a, b))
        if (a, b) not in target_edges[1]:
            raise AssertionError(("matched elementary edge absent", i, a, b))
        if not collapse_to_edge(S, face_records)[0]:
            raise AssertionError(("support not collapsible", i, S))
        oriented_boundary(S, face_records, (a, b))

def pair_type(A, B, face_records):
    f, e, v = intersection_cells(A, B, face_records)
    return ("face" if f else "edge" if e else "vertex" if v else "empty")

def run_target(name, labels, edges, faces, records):
    face_records = l45.target_face_records(faces)
    label_set = {tuple(map(int, x)) for x in labels}
    edge_set = {norm_edge(e) for e in edges}
    for supports in (STAR, PATH, TRIANGLE, PARENT_SUPPORTS):
        validate_support_family(supports, face_records, (label_set, edge_set))
    # Exact L4-L5 incidence, including non-overlap pairs.
    for graph, supports in list(SUPPORTS.items()) + [(PARENT_GRAPH, PARENT_SUPPORTS)]:
        for i, j in itertools.combinations(range(len(supports)), 2):
            common = intersection_cells(supports[i], supports[j], face_records)
            if bool(common[2]) != ((i, j) in graph):
                raise AssertionError(("L5 graph mismatch", graph, i, j))
            if (i, j) in graph:
                full_footprint(supports[i], supports[j], face_records, EDGES[i])
                full_footprint(supports[j], supports[i], face_records, EDGES[j])
    parent_sig = diagram_signature(PARENT_SUPPORTS, PARENT_GRAPH, face_records)
    marks = relative_pass = diagram_pass = 0
    collapse_pairs = Counter()
    collapse_hist = Counter()
    intersection_types = Counter()
    parent_origins = defaultdict(list)
    l7_comparisons = l7_mismatches = l7_projection_failures = 0
    l7_shape_pairs = Counter()
    l7_categories = Counter()
    projection_certificates = []
    max_steps = 0
    min_vertex_margin = float("inf")
    min_face_margin = float("inf")
    all_selected_faces = set()
    for graph, supports in SUPPORTS.items():
        for S in supports:
            all_selected_faces.update(S)
    all_selected_faces.update(*PARENT_SUPPORTS)
    for face in all_selected_faces:
        min_face_margin = min(min_face_margin,
                              l123.face_margin(face[0], face[1], face[2]))
        for vertex in face_records[face]:
            min_vertex_margin = min(min_vertex_margin, l123.window_margin(vertex))
    for row in records:
        graph = source_graph(row)
        child_supports = SUPPORTS[graph]
        for parent in row["parents"]:
            marks += 1
            mark = int(parent["deleted_interval_index"])
            retained = [i for i in range(3) if i != mark]
            retained_supports = [child_supports[i] for i in retained]
            retained_graph = frozenset(
                (new_i, new_j)
                for new_i, old_i in enumerate(retained)
                for new_j, old_j in enumerate(retained)
                if new_i < new_j and tuple(sorted((old_i, old_j))) in graph
            )
            child_sig = diagram_signature(retained_supports, retained_graph, face_records)
            if child_sig != parent_sig:
                raise AssertionError(("L6c diagram mismatch", row["intervals"], mark,
                                      child_sig, parent_sig))
            diagram_pass += 1
            ok, steps, remainder = relative_delete(child_supports, retained, face_records)
            if not ok:
                raise AssertionError(("L6c relative collapse failed", row["intervals"],
                                      mark, remainder))
            relative_pass += 1
            collapse_hist[len(steps)] += 1
            max_steps = max(max_steps, len(steps))
            for step in steps:
                collapse_pairs[step["pair"]] += 1
            intersection_types[pair_type(retained_supports[0],
                                         retained_supports[1], face_records)] += 1
            pkey = parent_key(parent)
            parent_origins[pkey].append({
                "child_intervals": row["intervals"],
                "tree_edges": row["tree_edges"],
                "deleted_interval_index": mark,
                "child_restriction_signature": child_sig,
                "parent_signature": parent_sig,
            })
            # Full L7b restriction: compare the single retained footprint on
            # each interval boundary, anchored at that interval's directed edge.
            interval_rows = []
            for parent_i, old_i in enumerate(retained):
                other_old = retained[1 - parent_i]
                child_fp = full_footprint(child_supports[old_i],
                                          child_supports[other_old],
                                          face_records, EDGES[old_i])
                parent_fp = full_footprint(PARENT_SUPPORTS[parent_i],
                                           PARENT_SUPPORTS[1 - parent_i],
                                           face_records, EDGES[parent_i])
                l7_comparisons += 1
                same = child_fp["category"] == parent_fp["category"]
                if not same:
                    l7_mismatches += 1
                l7_shape_pairs[(child_fp["shape"], parent_fp["shape"])] += 1
                l7_categories[(child_fp["category"], parent_fp["category"])] += 1
                interval_rows.append({
                    "retained_child_interval_index": old_i,
                    "parent_interval_index": parent_i,
                    "child_footprint": child_fp,
                    "parent_footprint": parent_fp,
                    "orientation_preserving_alignment": (
                        "edge-identification" if child_fp["shape"] == "edge"
                        else "contract-parent-footprint-edge-to-vertex"
                    ),
                    "cyclic_placement_matches": same,
                })
            projection_pass = all(x["cyclic_placement_matches"] for x in interval_rows)
            if not projection_pass:
                l7_projection_failures += 1
            projection_certificates.append({
                "child_intervals": row["intervals"],
                "child_tree_edges": row["tree_edges"],
                "deleted_interval_index": mark,
                "parent_intervals": parent["parent_intervals"],
                "interval_comparisons": interval_rows,
                "L7b_projection_pass": projection_pass,
            })
    coherence_groups = []
    for pkey, origins in sorted(parent_origins.items()):
        child_sigs = {json.dumps(x["child_restriction_signature"], sort_keys=True)
                      for x in origins}
        parent_sigs = {json.dumps(x["parent_signature"], sort_keys=True)
                       for x in origins}
        if len(child_sigs) != 1 or len(parent_sigs) != 1 or child_sigs != parent_sigs:
            raise AssertionError(("L6c parent coherence failed", pkey))
        coherence_groups.append({"parent_key": repr(pkey),
                                 "origin_count": len(origins),
                                 "coherent": True,
                                 "coarse_signature": origins[0]["parent_signature"]})
    # L7b coherence: every origin to one exact parent has the same ordered
    # two-interval footprint word, and that word equals the parent word.
    grouped_words = defaultdict(list)
    for cert in projection_certificates:
        pkey = next(parent_key(p) for row in records
                    if row["intervals"] == cert["child_intervals"]
                    and row["tree_edges"] == cert["child_tree_edges"]
                    for p in row["parents"]
                    if p["deleted_interval_index"] == cert["deleted_interval_index"])
        cw = tuple(x["child_footprint"]["category"]
                   for x in cert["interval_comparisons"])
        pw = tuple(x["parent_footprint"]["category"]
                   for x in cert["interval_comparisons"])
        grouped_words[pkey].append((cw, pw))
    l7_coherence = []
    for pkey, words in grouped_words.items():
        cwords = {x[0] for x in words}
        pwords = {x[1] for x in words}
        if len(cwords) != 1 or len(pwords) != 1 or cwords != pwords:
            raise AssertionError(("L7b parent boundary-word coherence failed", pkey))
        l7_coherence.append({"parent_key": repr(pkey),
                             "origin_count": len(words),
                             "distinct_child_words": [list(x) for x in sorted(cwords)],
                             "distinct_parent_words": [list(x) for x in sorted(pwords)],
                             "coherent": True})
    if min_vertex_margin <= 1e-9 or min_face_margin <= 1e-9:
        raise AssertionError("strict PF-I16 acceptance margin failure")
    return {
        "target": name,
        "vertices": len(labels), "edges": len(edges), "faces": len(faces),
        "marked_projections": marks,
        "L6c_relative_deletion_collapses": relative_pass,
        "L6c_child_parent_diagram_comparisons": diagram_pass,
        "L6c_parent_coherence_groups": len(coherence_groups),
        "L6c_parent_coherence": coherence_groups,
        "L6c_retained_intersection_types": dict(sorted(intersection_types.items())),
        "L6c_relative_collapse_length_histogram": dict(sorted(collapse_hist.items())),
        "L6c_relative_collapse_pair_counts": dict(sorted(collapse_pairs.items())),
        "L6c_maximum_relative_collapse_pairs": max_steps,
        "L7b_interval_footprint_comparisons": l7_comparisons,
        "L7b_cyclic_placement_mismatches": l7_mismatches,
        "L7b_projection_failures": l7_projection_failures,
        "L7b_shape_comparison_counts": {
            f"{a}->{b}": n for (a, b), n in sorted(l7_shape_pairs.items())},
        "L7b_cyclic_category_comparison_counts": {
            f"{a}->{b}": n for (a, b), n in sorted(l7_categories.items())},
        "L7b_parent_boundary_word_coherence": l7_coherence,
        "L7b_projection_certificates": projection_certificates,
        "strict_acceptance_margins": {
            "minimum_vertex_window_margin": min_vertex_margin,
            "minimum_face_triangle_margin": min_face_margin,
        },
        "parent_diagram_signature": parent_sig,
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
    original_keys = set(l45.target_face_records(faces_o))
    core_keys = set(l45.target_face_records(faces_c))
    if not core_keys <= original_keys:
        raise AssertionError("PF-I11 completed core is not a PF-I16 face subcomplex")
    records = hall.source_records(6)
    if len(records) != 22 or sum(len(r["parents"]) for r in records) != 30:
        raise AssertionError("Hall source/mark count mismatch")
    original = run_target("PF-I16 original-source replay", labels_o, edges_o,
                          faces_o, records)
    core = run_target("PF-I11 completed-window core", labels_c, edges_c,
                      faces_c, records)
    comparable = [k for k in original if k not in ("target", "vertices", "edges", "faces")]
    for key in comparable:
        if original[key] != core[key]:
            raise AssertionError(("target-domain outputs differ", key))
    result = {
        "schema": "PF-I16-HALL-ALTERNATIVE-TRIPLE-L6C-L7B-v1",
        "scope": "Ngrid=7 PF-I16 source replay and PF-I11 completed core; all n=6 sources and eligible marks; n=4 parents",
        "frozen_candidate_edges": [
            {"lower": list(a), "upper": list(b),
             "direction": next(j for j in range(5) if b[j] - a[j] == 1)}
            for a, b in EDGES],
        "support_assignment": {
            "star": [[[list(k[0]), k[1], k[2]] for k in sorted(S)] for S in STAR],
            "path": [[[list(k[0]), k[1], k[2]] for k in sorted(S)] for S in PATH],
            "triangle": [[[list(k[0]), k[1], k[2]] for k in sorted(S)] for S in TRIANGLE],
            "parent": [[[list(k[0]), k[1], k[2]] for k in sorted(S)]
                        for S in PARENT_SUPPORTS],
        },
        "PF_I16_original_source": original,
        "PF_I11_completed_window_core": core,
        "independence": {
            "hall_source_records_used_only_for_projection_indexing": True,
            "hall_demands_or_loads_read": False,
            "deficiencies_or_flow_outcomes_read": False,
            "support_choice_uses_only_target_geometry": True,
        },
        "nonclaims": [
            "finite L6c/L7b does not establish L8 or an all-orders incidence lift",
            "finite L6c/L7b does not prove the all-orders Hall inequality",
            "no claim is made beyond n=6 child sources and n=4 parents",
        ],
    }
    payload = json.dumps(result, sort_keys=True, indent=2) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(payload)
    print(payload, end="")

if __name__ == "__main__":
    main()
