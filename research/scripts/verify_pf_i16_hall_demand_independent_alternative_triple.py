#!/usr/bin/env python3
"""Demand-independent search for alternative PF-I16 three-edge incidence motifs.

Search domain: accepted elementary edges incident to exactly two accepted
rhombi in the Ngrid=7 PF-I11 completed-window core. Candidate supports are
connected one- or two-rhombus unions with the distinguished edge on a simple
support boundary. The search asks for one fixed ordered edge triple admitting
star, path, and triangle overlap-support patterns, with every overlap footprint
on the open complementary boundary arc of both supports.

No Hall source records, demands, loads, deficiencies, matchings, or flows are
read or used.
"""
from __future__ import annotations

import itertools
import json
from collections import Counter, defaultdict
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import verify_pf_i16_hall_l123_motif_lift as l123
import verify_pf_i16_hall_l45_bounded_support as l45


PATTERNS = {
    "star": {(0, 1), (0, 2)},
    "path": {(0, 1), (1, 2)},
    "triangle": {(0, 1), (0, 2), (1, 2)},
}


def edge_sort(edge):
    return (edge[0], edge[1])


def face_sort(key):
    return (key[0], key[1], key[2])


def edge_options(face_records):
    face_edges = {k: l45.face_edge_set(v) for k, v in face_records.items()}
    edge_to_faces = defaultdict(set)
    for key, edges in face_edges.items():
        for edge in edges:
            edge_to_faces[edge].add(key)

    face_adjacency = {k: set() for k in face_records}
    for incident in edge_to_faces.values():
        for x, y in itertools.combinations(incident, 2):
            face_adjacency[x].add(y)
            face_adjacency[y].add(x)

    def boundary_cycle(support):
        counts = Counter()
        for key in support:
            for edge in face_edges[key]:
                counts[edge] += 1
        boundary = {edge for edge, count in counts.items() if count == 1}
        adjacency = defaultdict(set)
        for a, b in boundary:
            adjacency[a].add(b)
            adjacency[b].add(a)
        if len(adjacency) < 4 or any(len(v) != 2 for v in adjacency.values()):
            return None
        start = min(adjacency)
        first = min(adjacency[start])
        cycle = [start, first]
        previous, current = start, first
        while True:
            choices = sorted(adjacency[current] - {previous})
            if not choices:
                return None
            nxt = choices[0]
            if nxt == start:
                break
            if nxt in cycle:
                return None
            cycle.append(nxt)
            previous, current = current, nxt
        if len(cycle) != len(adjacency):
            return None
        return cycle, boundary

    def describe(support, edge):
        boundary = boundary_cycle(support)
        if boundary is None:
            return None
        cycle, boundary_edges = boundary
        a, b = edge

        def directed_index(vertices):
            for i in range(len(vertices)):
                if vertices[i] == a and vertices[(i + 1) % len(vertices)] == b:
                    return i
            return None

        i = directed_index(cycle)
        if i is None:
            cycle = list(reversed(cycle))
            i = directed_index(cycle)
        if i is None:
            return None

        # The open complementary arc runs from b to a, excluding both ends.
        arc_vertices = []
        index = (i + 2) % len(cycle)
        while cycle[index] != a:
            arc_vertices.append(cycle[index])
            index = (index + 1) % len(cycle)
        path = [b] + arc_vertices + [a]
        arc_edges = {tuple(sorted((x, y))) for x, y in zip(path, path[1:])}

        return {
            "faces": frozenset(support),
            "vertices": frozenset().union(*(face_records[k] for k in support)),
            "edges": frozenset().union(*(face_edges[k] for k in support)),
            "arc_vertices": frozenset(arc_vertices),
            "arc_edges": frozenset(arc_edges),
            "cycle": cycle,
        }

    result = {}
    for edge in sorted(edge_to_faces, key=edge_sort):
        incident = sorted(edge_to_faces[edge], key=face_sort)
        # Work with stable interior links: exactly two accepted incident faces.
        if len(incident) != 2:
            continue
        supports = set()
        for face in incident:
            supports.add(frozenset((face,)))
            for neighbor in face_adjacency[face]:
                candidate = frozenset((face, neighbor))
                if sum(k in incident for k in candidate) == 1:
                    supports.add(candidate)
        ordered = sorted(
            supports,
            key=lambda s: tuple(sorted(face_sort(k) for k in s))
        )
        descriptions = [describe(s, edge) for s in ordered]
        descriptions = [x for x in descriptions if x is not None]
        if descriptions:
            result[edge] = descriptions
    return result


def overlaps(a, b):
    return bool(
        (a["faces"] & b["faces"])
        or (a["edges"] & b["edges"])
        or (a["vertices"] & b["vertices"])
    )


def overlap_on_both_open_arcs(a, b):
    common_vertices = a["vertices"] & b["vertices"]
    if not common_vertices:
        return False
    if not common_vertices <= a["arc_vertices"]:
        return False
    if not common_vertices <= b["arc_vertices"]:
        return False
    if a["faces"] & b["faces"]:
        return False
    common_edges = a["edges"] & b["edges"]
    if common_edges and not common_edges <= a["arc_edges"]:
        return False
    if common_edges and not common_edges <= b["arc_edges"]:
        return False
    return True


def realize_pattern(edges, options, pattern):
    e1, e2, e3 = edges
    for s1 in options[e1]:
        for s2 in options[e2]:
            for s3 in options[e3]:
                supports = (s1, s2, s3)
                valid = True
                for i, j in ((0, 1), (0, 2), (1, 2)):
                    shared = overlaps(supports[i], supports[j])
                    required = (i, j) in pattern
                    if shared != required:
                        valid = False
                        break
                    if required and not overlap_on_both_open_arcs(
                        supports[i], supports[j]
                    ):
                        valid = False
                        break
                if valid:
                    return supports
    return None


def search(face_records):
    options = edge_options(face_records)
    vertex_index = defaultdict(list)
    for edge in sorted(options, key=edge_sort):
        for option_index, support in enumerate(options[edge]):
            for vertex in support["vertices"]:
                vertex_index[vertex].append((edge, option_index, support))

    for e1 in sorted(options, key=edge_sort):
        endpoints1 = set(e1)
        for root_support in options[e1]:
            by_edge = {}
            for vertex in sorted(root_support["arc_vertices"]):
                for edge, option_index, leaf_support in vertex_index[vertex]:
                    if edge == e1 or endpoints1.intersection(edge):
                        continue
                    if overlap_on_both_open_arcs(root_support, leaf_support):
                        by_edge.setdefault(edge, {})[option_index] = leaf_support

            leaf_edges = sorted(by_edge, key=edge_sort)
            for i, e2 in enumerate(leaf_edges):
                for e3 in leaf_edges[i + 1:]:
                    if set(e2).intersection(e3):
                        continue

                    # The star pattern requires disjoint leaf supports.
                    star_disjoint = any(
                        s2["vertices"].isdisjoint(s3["vertices"])
                        for s2 in by_edge[e2].values()
                        for s3 in by_edge[e3].values()
                    )
                    if not star_disjoint:
                        continue

                    triple = (e1, e2, e3)
                    solutions = {
                        name: realize_pattern(triple, options, pattern)
                        for name, pattern in PATTERNS.items()
                    }
                    if all(solutions.values()):
                        return options, triple, solutions
    return options, None, None


def edge_record(edge):
    a, b = edge
    direction = next(j for j in range(5) if b[j] - a[j] == 1)
    return {"lower": list(a), "upper": list(b), "direction": direction}


def support_record(support):
    return [
        {"lower": list(key[0]), "directions": [key[1], key[2]]}
        for key in sorted(support["faces"], key=face_sort)
    ]


def pair_record(a, b):
    return {
        "shared_faces": len(a["faces"] & b["faces"]),
        "shared_edges": len(a["edges"] & b["edges"]),
        "shared_vertices": len(a["vertices"] & b["vertices"]),
        "open_arc_on_both_supports": overlap_on_both_open_arcs(a, b),
        "disjoint_including_vertices": a["vertices"].isdisjoint(b["vertices"]),
    }


def verify_in_target(name, options, triple, solutions, face_records):
    for edge in triple:
        if edge not in options:
            raise AssertionError((name, "candidate edge absent", edge))
    for pattern_name, supports in solutions.items():
        for edge, support in zip(triple, supports):
            face_set = support["faces"]
            if not any(x["faces"] == face_set for x in options[edge]):
                raise AssertionError((name, "support not admissible", pattern_name, edge))
            if not face_set <= set(face_records):
                raise AssertionError((name, "support face absent", pattern_name))
        for i, j in ((0, 1), (0, 2), (1, 2)):
            shared = overlaps(supports[i], supports[j])
            required = (i, j) in PATTERNS[pattern_name]
            if shared != required:
                raise AssertionError((name, "wrong overlap graph", pattern_name, i, j))
            if required and not overlap_on_both_open_arcs(supports[i], supports[j]):
                raise AssertionError((name, "footprint not in both open arcs",
                                      pattern_name, i, j))


def main():
    labels_o, edges_o, faces_o, center, cutoff = l123.original_source_complex(7)
    labels_c, edges_c, faces_c = l123.completed_window_core(7, center, cutoff)
    if (len(labels_o), len(edges_o), len(faces_o)) != (1550, 3017, 1468):
        raise AssertionError("PF-I16 original-source population mismatch")
    if (len(labels_c), len(faces_c)) != (1432, 1330):
        raise AssertionError("PF-I11 completed-core population mismatch")
    if l123.sha_labels(labels_c) != l123.EXPECTED_CORE_LABEL_SHA:
        raise AssertionError("PF-I11 completed-core label hash mismatch")
    if l123.sha_faces(faces_c) != l123.EXPECTED_CORE_FACE_SHA:
        raise AssertionError("PF-I11 completed-core face hash mismatch")

    original_records = l45.target_face_records(faces_o)
    core_records = l45.target_face_records(faces_c)
    if not set(core_records) <= set(original_records):
        raise AssertionError("completed core is not a face subcomplex of source replay")

    core_options, triple, solutions = search(core_records)
    if triple is None:
        raise AssertionError("no alternative triple found in completed-window core")

    original_options = edge_options(original_records)
    verify_in_target("PF-I11 completed-window core",
                     core_options, triple, solutions, core_records)
    verify_in_target("PF-I16 original-source replay",
                     original_options, triple, solutions, original_records)

    all_vertices = set()
    all_faces = set()
    patterns_out = {}
    for name, supports in solutions.items():
        all_vertices.update(*(s["vertices"] for s in supports))
        all_faces.update(*(s["faces"] for s in supports))
        patterns_out[name] = {
            "supports": [support_record(s) for s in supports],
            "pairwise_intersections": {
                f"{i+1}-{j+1}": pair_record(supports[i], supports[j])
                for i, j in ((0, 1), (0, 2), (1, 2))
            },
        }

    min_vertex_margin = min(l123.window_margin(v) for v in all_vertices)
    min_face_margin = min(
        l123.face_margin(key[0], key[1], key[2]) for key in all_faces
    )
    if min_vertex_margin <= 1e-9 or min_face_margin <= 1e-9:
        raise AssertionError("candidate violates strict target acceptance")

    result = {
        "schema": "PF-I16-HALL-DEMAND-INDEPENDENT-ALTERNATIVE-TRIPLE-v1",
        "search_scope": (
            "Ngrid=7 PF-I11 completed-window core; links with exactly two "
            "accepted incident rhombi; connected supports of one or two "
            "rhombi with simple boundary"
        ),
        "target_controls": {
            "PF-I16_original_source": {
                "vertices": len(labels_o), "edges": len(edges_o), "faces": len(faces_o)
            },
            "PF-I11_completed_core": {
                "vertices": len(labels_c), "edges": None, "faces": len(faces_c)
            },
            "core_faces_are_subset_of_original_source": True,
            "candidate_verified_in_both_domains": True,
        },
        "candidate_edges_in_interval_order": [edge_record(e) for e in triple],
        "candidate_edge_options_in_core": len(core_options),
        "accepted_supports": patterns_out,
        "strict_acceptance_margins": {
            "minimum_vertex_window_margin": min_vertex_margin,
            "minimum_face_triangle_margin": min_face_margin,
        },
        "independence": {
            "hall_source_records_read": False,
            "hall_demands_read": False,
            "hall_loads_or_deficiencies_read": False,
            "matching_or_flow_results_read": False,
        },
        "nonclaims": [
            "This is not a full L6c parent-naturality verification.",
            "Open-arc placement is a necessary L7b geometric filter, not the complete L7b subdivision/collapse comparison.",
            "No all-orders incidence lift or Hall theorem is established.",
        ],
    }
    # Count the completed core's elementary basis edges as a population control.
    core_edge_count = sum(
        1 for a in labels_c for j in range(5)
        if tuple(a[t] + int(t == j) for t in range(5)) in labels_c
    )
    result["target_controls"]["PF-I11_completed_core"]["edges"] = core_edge_count
    if core_edge_count != 2761:
        raise AssertionError("PF-I11 completed-core edge count mismatch")

    print(json.dumps(result, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
