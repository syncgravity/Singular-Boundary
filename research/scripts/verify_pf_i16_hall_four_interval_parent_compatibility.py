#!/usr/bin/env python3
"""Necessary parent-compatibility obstruction test for the four-interval lift.

Consumes the target-only Ngrid=12 support inventory. It enumerates every
one-to-three-rhombus support family on the frozen first three edges that is
compatible with the n=6 parent restrictions, then tests whether a fourth
edge/support can realize each of the 13 n=8 overlap graphs.

No Hall demands, loads, deficiencies, matching outcomes, or flows are read.
The test is intentionally one-sided: a common fourth edge must pass this
necessary L4/L5 + three-to-two parent-compatibility gate, but passing it would
not yet establish the four-way L6c/L7b diamond.
"""
from __future__ import annotations
import argparse
import hashlib
import itertools
import json
from collections import Counter, defaultdict
from functools import lru_cache
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import export_pf_i16_hall_source_records as hall

def edge_key(row):
    return (tuple(row["lower"]), tuple(row["upper"]))

def sha_edges(edges):
    rows = []
    for a, b in sorted(edges):
        rows.append(",".join(map(str, a)) + "->" + ",".join(map(str, b)))
    return hashlib.sha256(("\n".join(rows) + "\n").encode()).hexdigest()

def build_target(inv):
    basis = [tuple(int(i == j) for i in range(5)) for j in range(5)]
    face_vertices = []
    for row in inv["face_key_table"]:
        m = tuple(row["lower"])
        j, k = row["directions"]
        add = lambda *js: tuple(m[t] + sum(basis[q][t] for q in js)
                                for t in range(5))
        face_vertices.append(frozenset((m, add(j), add(j, k), add(k))))
    face_edges = []
    for vertices in face_vertices:
        face_edges.append(frozenset(
            tuple(sorted((a, b)))
            for a, b in itertools.combinations(vertices, 2)
            if sum(abs(x-y) for x, y in zip(a, b)) == 1))
    options = {}
    directions = {}
    for row in inv["edge_support_options"]:
        edge = edge_key(row["edge"])
        options[edge] = [frozenset(map(int, s)) for s in row["support_options"]]
        directions[edge] = edge
    return face_vertices, face_edges, options, directions

def make_geometry(face_vertices, face_edges):
    @lru_cache(None)
    def cells(skey):
        fs = frozenset(skey)
        es = frozenset().union(*(face_edges[i] for i in fs))
        vs = frozenset().union(*(face_vertices[i] for i in fs))
        return fs, es, vs

    def union(supports):
        parts = [cells(tuple(sorted(s))) for s in supports]
        return tuple(set().union(*(p[i] for p in parts)) for i in range(3))

    def intersection(supports):
        parts = [cells(tuple(sorted(s))) for s in supports]
        return tuple(set.intersection(*(set(p[i]) for p in parts)) for i in range(3))

    def collapse(src, tgt):
        cf, ce, cv = map(set, src)
        tf, te, tv = map(set, tgt)
        while True:
            found = None
            for edge in sorted(ce - te):
                incident = [fid for fid in cf if edge in face_edges[fid]]
                if len(incident) == 1 and incident[0] not in tf:
                    found = edge, incident[0]
                    break
            if found is None:
                break
            edge, face = found
            ce.remove(edge)
            cf.remove(face)
        while True:
            found = None
            for edge in sorted(ce - te):
                for vertex in edge:
                    degree = sum(vertex in e for e in ce)
                    in_face = any(vertex in face_vertices[fid] for fid in cf)
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
        return cf == tf and ce == te and cv == tv

    def point_contractible(complex_cells):
        f, e, v = map(set, complex_cells)
        if not v:
            return False
        return collapse((f, e, v), (set(), set(), {min(v)}))

    def edge_contractible(support):
        f, e, v = cells(tuple(sorted(support)))
        target = sorted(e)[0]
        return collapse((set(f), set(e), set(v)),
                        (set(), {target}, set(target)))

    def boundary_cycle(support, directed):
        counts = Counter()
        for fid in support:
            counts.update(face_edges[fid])
        boundary = [e for e, count in counts.items() if count == 1]
        adj = defaultdict(list)
        for a, b in boundary:
            adj[a].append(b)
            adj[b].append(a)
        if not adj or any(len(v) != 2 for v in adj.values()):
            return None
        tail, head = directed
        if tuple(sorted((tail, head))) not in set(boundary):
            return None
        cycle = [tail, head]
        previous, current = tail, head
        while True:
            choices = [v for v in adj[current] if v != previous]
            if len(choices) != 1:
                return None
            nxt = choices[0]
            if nxt == tail:
                break
            if nxt in cycle:
                return None
            cycle.append(nxt)
            previous, current = current, nxt
        if len(cycle) != len(adj):
            return None
        return cycle

    def open_arc_footprint(S, T, directed):
        cycle = boundary_cycle(S, directed)
        if cycle is None:
            return False
        _, se, sv = cells(tuple(sorted(S)))
        _, te, tv = cells(tuple(sorted(T)))
        shared_edges, shared_vertices = se & te, sv & tv
        if len(shared_vertices) == 1 and not shared_edges:
            vertex = next(iter(shared_vertices))
            if vertex not in cycle:
                return False
            shape = "vertex"
        elif len(shared_edges) == 1 and len(shared_vertices) == 2:
            edge = next(iter(shared_edges))
            boundary_edges = {
                tuple(sorted((cycle[i], cycle[(i+1) % len(cycle)])))
                for i in range(len(cycle))
            }
            if edge not in boundary_edges or set(edge) != set(shared_vertices):
                return False
            shape = "edge"
        else:
            return False
        tail, head = directed
        if tuple(sorted(directed)) in shared_edges:
            return False
        if tail in shared_vertices or head in shared_vertices:
            return False
        arc = []
        i = cycle.index(head)
        while True:
            arc.append(cycle[i])
            if cycle[i] == tail:
                break
            i = (i + 1) % len(cycle)
        if shape == "vertex":
            return next(iter(shared_vertices)) in arc[1:-1]
        return not (shared_vertices & {tail, head})

    return cells, union, intersection, collapse, point_contractible, edge_contractible, open_arc_footprint

def graph_key(row):
    return frozenset(tuple(sorted(map(int, e))) for e in row["full_overlap_edges"])

def triple_pattern(graph):
    g = frozenset((i, j) for i, j in graph if j < 3)
    if g == frozenset({(0, 1), (0, 2)}):
        return "star"
    if g == frozenset({(0, 1), (1, 2)}):
        return "path"
    if g == frozenset({(0, 1), (0, 2), (1, 2)}):
        return "triangle"
    raise AssertionError(("unsupported retained triple graph", sorted(g)))

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--inventory", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    inv = json.loads(args.inventory.read_text())
    face_vertices, face_edges, options, _ = build_target(inv)
    cells, union, intersection, collapse, point_contractible, edge_contractible, footprint = make_geometry(face_vertices, face_edges)

    fixed_edges = [edge_key(x) for x in inv["fixed_triple_edges"]]
    fixed_endpoints = {v for e in fixed_edges for v in e}
    fixed_options = [options[e] for e in fixed_edges]
    if [len(x) for x in fixed_options] != [28, 26, 28]:
        raise AssertionError(("frozen-edge support inventory changed",
                              [len(x) for x in fixed_options]))

    # The three parent patterns and their eligible reverse-leaf deletions.
    patterns = {
        "star": (frozenset({(0, 1), (0, 2)}), [1, 2]),
        "path": (frozenset({(0, 1), (1, 2)}), [2]),
        "triangle": (frozenset({(0, 1), (0, 2), (1, 2)}), [1, 2]),
    }

    def pair_graph_ok(supports, graph):
        for i, j in itertools.combinations(range(3), 2):
            common = intersection([supports[i], supports[j]])
            nonempty = bool(common[2])
            if nonempty != ((i, j) in graph):
                return False
            if nonempty:
                if not point_contractible(common):
                    return False
                if not footprint(supports[i], supports[j], fixed_edges[i]):
                    return False
                if not footprint(supports[j], supports[i], fixed_edges[j]):
                    return False
        return True

    parent_compatible = {}
    for name, (graph, marks) in patterns.items():
        good = []
        for supports in itertools.product(*fixed_options):
            if not all(edge_contractible(s) for s in supports):
                continue
            if not pair_graph_ok(supports, graph):
                continue
            triple_intersection = intersection(supports)
            if triple_intersection[2] and not point_contractible(triple_intersection):
                continue
            if not point_contractible(union(supports)):
                continue
            ok = True
            for mark in marks:
                retained = [i for i in range(3) if i != mark]
                retained_supports = [supports[i] for i in retained]
                if not collapse(union(supports), union(retained_supports)):
                    ok = False
                    break
                pair_intersection = intersection(retained_supports)
                if not pair_intersection[2] or not point_contractible(pair_intersection):
                    ok = False
                    break
                if not point_contractible(union(retained_supports)):
                    ok = False
                    break
            if ok:
                good.append(tuple(frozenset(s) for s in supports))
        parent_compatible[name] = good

    # All 608 order-eight sources and their actual eligible marks. This is
    # graph indexing only; no demands, flows, or Hall matching data are used.
    sources = hall.source_records(8)
    if len(sources) != 608 or sum(len(r["parents"]) for r in sources) != 1050:
        raise AssertionError("order-eight source/mark census changed")
    graph_sources = Counter()
    graph_marks = Counter()
    graph_mark3 = Counter()
    diamonds = 0
    for row in sources:
        g = graph_key(row)
        graph_sources[g] += 1
        marks = [int(p["deleted_interval_index"]) for p in row["parents"]]
        graph_marks[g] += len(marks)
        graph_mark3[g] += sum(m == 3 for m in marks)
        diamonds += len(marks) * (len(marks) - 1) // 2
    graphs = sorted(graph_sources, key=lambda g: (len(g), tuple(sorted(g))))
    if len(graphs) != 13 or diamonds != 490:
        raise AssertionError(("order-eight graph/diamond census", len(graphs), diamonds))
    if any(graph_mark3[g] == 0 for g in graphs):
        raise AssertionError("a four-interval graph lacks an eligible deletion of interval 4")

    # A fourth support must meet at least one of the first three supports for
    # every graph. Remove candidates whose entire support family is disjoint
    # from the union of every possible first-three support.
    fixed_any_vertices = set()
    for edge_options in fixed_options:
        for support in edge_options:
            fixed_any_vertices.update(cells(tuple(sorted(support)))[2])
    candidates = []
    for edge, edge_options in options.items():
        if edge in fixed_edges or set(edge) & fixed_endpoints:
            continue
        if any(cells(tuple(sorted(s)))[2] & fixed_any_vertices for s in edge_options):
            candidates.append(edge)
    candidates.sort()

    feasible_by_graph = {}
    witnesses_by_graph = {}
    for graph in graphs:
        pname = triple_pattern(graph)
        adjacency = tuple((i, 3) in graph for i in range(3))
        feasible = set()
        witnesses = {}
        for edge in candidates:
            found = False
            for parent_supports in parent_compatible[pname]:
                for fourth_support in options[edge]:
                    good = True
                    for i in range(3):
                        common = bool(cells(tuple(sorted(parent_supports[i])))[2] &
                                      cells(tuple(sorted(fourth_support)))[2])
                        if common != adjacency[i]:
                            good = False
                            break
                        if adjacency[i]:
                            if not footprint(parent_supports[i], fourth_support, fixed_edges[i]):
                                good = False
                                break
                            if not footprint(fourth_support, parent_supports[i], edge):
                                good = False
                                break
                    if good:
                        found = True
                        witnesses[edge] = {
                            "first_three_support_face_indices": [
                                sorted(s) for s in parent_supports
                            ],
                            "fourth_support_face_indices": sorted(fourth_support),
                        }
                        break
                if found:
                    break
            if found:
                feasible.add(edge)
        feasible_by_graph[graph] = feasible
        witnesses_by_graph[graph] = witnesses

    graph_rows = []
    for index, graph in enumerate(graphs, 1):
        pname = triple_pattern(graph)
        adj = [int((i, 3) in graph) for i in range(3)]
        feasible = feasible_by_graph[graph]
        graph_rows.append({
            "graph_index": index,
            "edges": [list(e) for e in sorted(graph)],
            "source_count": graph_sources[graph],
            "eligible_mark_count": graph_marks[graph],
            "interval_4_eligible_mark_count": graph_mark3[graph],
            "retained_parent_pattern": pname,
            "fourth_adjacency_vector": adj,
            "parent_compatible_triple_count": len(parent_compatible[pname]),
            "feasible_fourth_edge_count": len(feasible),
            "feasible_fourth_edge_sha256": sha_edges(feasible),
        })

    # These two graph types are a compact, explicit disjointness certificate:
    # both have a triangle on intervals 0,1,2, but require different fourth
    # interval attachment patterns.
    g5 = graphs[4]
    g12 = graphs[11]
    if len(feasible_by_graph[g5]) != 103 or len(feasible_by_graph[g12]) != 21:
        raise AssertionError("bounded candidate-set counts changed")
    pair_intersection = feasible_by_graph[g5] & feasible_by_graph[g12]
    if pair_intersection:
        raise AssertionError(("expected pairwise candidate obstruction", pair_intersection))

    max_graphs_per_edge = max(
        sum(edge in feasible_by_graph[g] for g in graphs)
        for edge in set().union(*(feasible_by_graph[g] for g in graphs))
    )
    result = {
        "schema": "PF-I16-HALL-FOUR-INTERVAL-PARENT-COMPATIBILITY-v1",
        "target_inventory_sha256": inv.get("target", {}).get("face_key_sha256"),
        "target": inv.get("target"),
        "source_census": {
            "order_eight_sources": len(sources),
            "eligible_reverse_leaf_projections": sum(len(r["parents"]) for r in sources),
            "distinct_overlap_graphs": len(graphs),
            "unordered_source_deletion_diamonds": diamonds,
        },
        "parent_compatible_triple_counts": {
            name: len(rows) for name, rows in parent_compatible.items()
        },
        "candidate_search": {
            "candidate_edges_vertex_disjoint_from_frozen_triple": inv["eligible_edges_vertex_disjoint_from_frozen_triple"],
            "locally_relevant_fourth_edges_after_support-incidence_prefilter": len(candidates),
            "graphs_realized_per_best_single_fourth_edge": max_graphs_per_edge,
            "common_fourth_edge_for_all_13_graphs": False,
            "graph_5_vs_graph_12_candidate_intersection_count": len(pair_intersection),
            "graph_5_vs_graph_12_candidate_intersection_sha256": sha_edges(pair_intersection),
        },
        "four_interval_graphs": graph_rows,
        "obstruction_pair": {
            "graph_5_edges": [list(e) for e in sorted(g5)],
            "graph_5_feasible_fourth_edge_count": len(feasible_by_graph[g5]),
            "graph_5_feasible_fourth_edge_sha256": sha_edges(feasible_by_graph[g5]),
            "graph_5_candidate_edges_with_support_witnesses": [
                {
                    "edge": {"lower": list(edge[0]), "upper": list(edge[1])},
                    **witnesses_by_graph[g5][edge],
                }
                for edge in sorted(feasible_by_graph[g5])
            ],
            "graph_12_edges": [list(e) for e in sorted(g12)],
            "graph_12_feasible_fourth_edge_count": len(feasible_by_graph[g12]),
            "graph_12_feasible_fourth_edge_sha256": sha_edges(feasible_by_graph[g12]),
            "graph_12_candidate_edges_with_support_witnesses": [
                {
                    "edge": {"lower": list(edge[0]), "upper": list(edge[1])},
                    **witnesses_by_graph[g12][edge],
                }
                for edge in sorted(feasible_by_graph[g12])
            ],
            "intersection_count": len(pair_intersection),
        },
        "scope": [
            "All connected simple-boundary supports of one to three rhombi for the fixed first three matched edges are enumerated.",
            "Parent-compatible triple families satisfy exact pairwise overlap graphs, single-cell open-arc footprints, support/union/intersection contractibility, and relative deletion collapse for every eligible three-interval leaf deletion.",
            "For each order-eight overlap graph, the fourth edge/support is tested against at least one parent-compatible first-three support family and the exact fourth-interval adjacency vector.",
            "All 13 graph types have at least one eligible deletion of interval 4, so the first-three parent restriction is necessary for every graph type.",
        ],
        "nonclaims": [
            "The fourth-support test does not yet compare all three other deletion restrictions for a four-support assignment.",
            "It does not perform the complete four-support L6c intersection diagram or four-union relative-collapse certificates.",
            "It does not perform the full L7b multi-footprint boundary-word comparison on every retained triple.",
            "It does not rule out a different first-three matched-edge motif or supports larger than three rhombi.",
            "It does not establish L8 or an all-orders Hall theorem.",
        ],
    }
    payload = json.dumps(result, sort_keys=True, indent=2) + "\n"
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(payload)
    print(payload, end="")

if __name__ == "__main__":
    main()
