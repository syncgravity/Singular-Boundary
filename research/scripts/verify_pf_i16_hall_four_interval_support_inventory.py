#!/usr/bin/env python3
"""Target-only inventory of all one-, two-, and three-rhombus supports.

The search is independent of Hall source records, demands, flows, and
deficiencies. It enumerates every connected face support of size <=3 for
eligible matched edges, with the matched edge on a simple support boundary.
"""
from __future__ import annotations
import argparse, itertools, json, hashlib
from collections import Counter, defaultdict
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import verify_pf_i16_hall_l123_motif_lift as l123
import verify_pf_i16_hall_l45_bounded_support as l45
import verify_pf_i16_hall_alternative_triple_l6c_l7b as alt

NGRID = 12
FIXED_EDGES = [tuple(map(tuple, e)) for e in alt.EDGES]

def connected(S, adjacency):
    seen = {next(iter(S))}
    stack = list(seen)
    while stack:
        x = stack.pop()
        for y in adjacency[x] & S:
            if y not in seen:
                seen.add(y); stack.append(y)
    return seen == S

def simple_boundary(S, face_records, face_edges):
    counts = Counter()
    for f in S:
        counts.update(face_edges[f])
    boundary = [e for e, n in counts.items() if n == 1]
    adj = defaultdict(set)
    for a, b in boundary:
        adj[a].add(b); adj[b].add(a)
    if len(adj) < 4 or any(len(v) != 2 for v in adj.values()):
        return False
    start = min(adj); prev = None; cur = start; seen = []
    while True:
        seen.append(cur)
        choices = sorted(adj[cur] - ({prev} if prev is not None else set()))
        if not choices: return False
        nxt = choices[0]
        if nxt == start: break
        if nxt in seen: return False
        prev, cur = cur, nxt
    return len(seen) == len(adj)

def inventory(face_records):
    face_edges = {f: l45.face_edge_set(v) for f, v in face_records.items()}
    edge_faces = defaultdict(set)
    for f, es in face_edges.items():
        for e in es: edge_faces[e].add(f)
    adjacency = {f: set() for f in face_records}
    for incident in edge_faces.values():
        for a, b in itertools.combinations(incident, 2):
            adjacency[a].add(b); adjacency[b].add(a)

    out = {}
    size_hist = Counter()
    total_supports = 0
    for edge, incident in edge_faces.items():
        if len(incident) != 2: continue
        incident = set(incident)
        options = set()
        for root in incident:
            # All faces at graph distance at most two from this root suffice
            # for a connected support of at most three faces containing root.
            near = {root} | adjacency[root]
            near |= set().union(*(adjacency[x] for x in adjacency[root])) if adjacency[root] else set()
            near.discard(next(iter(incident - {root})))
            candidates = sorted(near, key=lambda x: (x[0], x[1], x[2]))
            for k in (1, 2):
                for extra in itertools.combinations([x for x in candidates if x != root], k):
                    S = frozenset((root, *extra))
                    if len(S & incident) != 1: continue
                    if not connected(S, adjacency): continue
                    if not simple_boundary(S, face_records, face_edges): continue
                    options.add(S)
            S = frozenset((root,))
            if simple_boundary(S, face_records, face_edges): options.add(S)
        ordered = sorted(options, key=lambda S: tuple(sorted(S)))
        if ordered:
            out[edge] = ordered
            size_hist[len(ordered)] += 1
            total_supports += len(ordered)
    return out, edge_faces, size_hist, total_supports

def edge_record(e):
    a, b = e
    return {"lower": list(a), "upper": list(b),
            "direction": next(j for j in range(5) if b[j] - a[j] == 1)}

def sha_face_keys(keys):
    raw = "\n".join(f"{m}|{j}|{k}" for m,j,k in sorted(keys)) + "\n"
    return hashlib.sha256(raw.encode()).hexdigest()

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--output", type=Path, required=True)
    a = p.parse_args()
    labels_o, edges_o, faces_o, center, cutoff = l123.original_source_complex(NGRID)
    labels_c, edges_c, faces_c = l123.completed_window_core(NGRID, center, cutoff)
    rec_o = l45.target_face_records(faces_o)
    rec_c = l45.target_face_records(faces_c)
    if not set(rec_c) <= set(rec_o):
        raise AssertionError("completed core is not a subcomplex of original-source replay")
    options, edge_faces, option_hist, total = inventory(rec_c)

    fixed_endpoints = {v for e in FIXED_EDGES for v in e}
    eligible = [e for e in options if not (set(e) & fixed_endpoints)]
    eligible.sort()
    fixed_present = all(tuple(sorted(e)) in options or
                        tuple(sorted(e)) in edge_faces for e in FIXED_EDGES)
    if not fixed_present:
        raise AssertionError("one of the frozen triple edges is absent from target")
    face_keys = set().union(*(set(S) for e in eligible for S in options[e]))
    margins_v = [l123.window_margin(v) for S in (options[e][i] for e in eligible for i in range(len(options[e]))) for f in S for v in rec_c[f]]
    margins_f = [l123.face_margin(f[0], f[1], f[2]) for e in eligible for S in options[e] for f in S]
    if min(margins_v, default=0) <= 1e-9 or min(margins_f, default=0) <= 1e-9:
        raise AssertionError("non-strict acceptance margin in enumerated supports")

    result = {
      "schema": "PF-I16-HALL-FOUR-INTERVAL-SUPPORT-INVENTORY-v1",
      "scope": "Ngrid=12 PF-I11 completed core; all eligible edges with exactly two accepted incident rhombi; all connected simple-boundary supports of one to three rhombi",
      "target": {"vertices": len(labels_c), "edges": len(edges_c), "faces": len(faces_c),
                 "face_key_sha256": sha_face_keys(rec_c)},
      "original_source_control": {"vertices": len(labels_o), "edges": len(edges_o), "faces": len(faces_o)},
      "eligible_matched_edges": len(options),
      "eligible_edges_vertex_disjoint_from_frozen_triple": len(eligible),
      "total_support_options_all_eligible_edges": total,
      "support_option_count_histogram": {str(k): v for k,v in sorted(option_hist.items())},
      "fourth_edge_support_option_count_histogram": {
        str(k): sum(len(options[e]) == k for e in eligible)
        for k in sorted({len(options[e]) for e in eligible})},
      "fourth_edge_candidate_sample": [edge_record(e) for e in eligible[:20]],
      "enumerated_support_face_key_count": len(face_keys),
      "minimum_strict_vertex_margin": min(margins_v),
      "minimum_strict_face_margin": min(margins_f),
      "fixed_triple_edges": [edge_record(e) for e in FIXED_EDGES],
      "support_bound": 3,
      "nonclaims": [
        "No four-interval overlap graph compatibility is tested in this inventory.",
        "No L6c intersection-diagram or relative-collapse test is performed.",
        "No L7b multi-footprint boundary-word test is performed.",
        "No Hall source records, demands, loads, deficiencies, matchings, or flows are read.",
        "No all-orders geometric incidence lift is established."
      ]
    }
    a.output.parent.mkdir(parents=True, exist_ok=True)
    a.output.write_text(json.dumps(result, sort_keys=True, indent=2) + "\n")
    print(json.dumps(result, sort_keys=True, indent=2))

if __name__ == "__main__":
    main()
