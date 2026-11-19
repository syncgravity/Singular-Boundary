#!/usr/bin/env python3
"""Verify the local L4/L5/L7b obstruction for the frozen PF-I16 motif.

This is an incidence certificate, not a search over interval supports.  It
rebuilds both Ngrid=7 target complexes, verifies the exact accepted rhombi
incident to the three distinguished matched edges, and checks the vertex
incidences used in the local impossibility argument.
"""
from __future__ import annotations

import itertools
import json
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import verify_pf_i16_hall_l123_motif_lift as l123
import verify_pf_i16_hall_l45_bounded_support as l45


M = (0, 1, 0, 0, 0)
M2 = (0, 1, 0, 1, 0)
M3 = (0, 1, 1, 0, -1)
VSTAR = (0, 1, 1, 1, 0)

EXPECTED = {
    "e1": {(M, 0, 4), (M, 3, 4)},
    "e2": {(M, 3, 4), (M2, 2, 4)},
    "e3": {(M, 2, 3), (M3, 3, 4)},
}


def verify_target(name, labels, edges, faces):
    if (len(labels), len(edges), len(faces)) not in {
        (1550, 3017, 1468), (1432, 2761, 1330)
    }:
        raise AssertionError((name, "unexpected target population",
                              len(labels), len(edges), len(faces)))

    records = l45.target_face_records(faces)
    matched = {
        "e1": ((0, 1, 0, 0, 0), (0, 1, 0, 0, 1)),
        "e2": ((0, 1, 0, 1, 0), (0, 1, 0, 1, 1)),
        "e3": ((0, 1, 1, 0, 0), (0, 1, 1, 1, 0)),
    }

    incidence = {}
    for edge_name, (a, b) in matched.items():
        incident = {
            key for key, vertices in records.items()
            if a in vertices and b in vertices
        }
        if incident != EXPECTED[edge_name]:
            raise AssertionError((name, edge_name, "incident-face mismatch",
                                  sorted(incident), sorted(EXPECTED[edge_name])))
        if len(incident) != 2:
            raise AssertionError((name, edge_name, "expected exactly two incident faces"))
        incidence[edge_name] = sorted(incident)

    # The common face is simultaneously incident to e1 and e2.
    f20 = records[(M, 3, 4)]
    e1a, e1b = matched["e1"]
    e2a, e2b = matched["e2"]
    if not {e1a, e1b, e2a, e2b} <= set(f20):
        raise AssertionError((name, "shared e1/e2 face misses a marked endpoint"))

    # The alternative e2 face contains v*, as does every e3-incident face.
    f2star = records[(M2, 2, 4)]
    if not {e2a, e2b, VSTAR} <= set(f2star):
        raise AssertionError((name, "alternative e2 face misses v*"))
    for key in EXPECTED["e3"]:
        if VSTAR not in records[key]:
            raise AssertionError((name, "an e3-incident face misses v*", key))

    return {
        "target": name,
        "population": {"V": len(labels), "E": len(edges), "F": len(faces)},
        "incident_faces": {
            edge_name: [
                {"lower": list(key[0]), "directions": [key[1], key[2]]}
                for key in incidence[edge_name]
            ]
            for edge_name in ("e1", "e2", "e3")
        },
        "shared_e1_e2_face_contains_both_marked_edges": True,
        "alternative_e2_face_contains_vstar": True,
        "both_e3_incident_faces_contain_vstar": True,
    }


def main():
    labels_o, edges_o, faces_o, center, cutoff = l123.original_source_complex(7)
    labels_c, edges_c, faces_c = l123.completed_window_core(7, center, cutoff)

    original = verify_target("PF-I16 original-source replay",
                             labels_o, edges_o, faces_o)
    core = verify_target("PF-I11 completed-window core",
                         labels_c, edges_c, faces_c)

    if not set(l45.target_face_records(faces_c)) <= set(l45.target_face_records(faces_o)):
        raise AssertionError("completed-window core is not a face subcomplex of source replay")
    if original["incident_faces"] != core["incident_faces"]:
        raise AssertionError("the two target domains disagree on motif incidence")

    result = {
        "schema": "PF-I16-HALL-L7B-LOCAL-MOTIF-OBSTRUCTION-v1",
        "targets": [original, core],
        "logical_consequence": [
            "L4 keeps each distinguished matched edge on the support boundary.",
            "Each distinguished edge has exactly two accepted incident rhombi, so a support contains exactly one of them.",
            "The e2 support cannot choose the rhombus shared with e1: that rhombus contains both endpoints of e1, forbidden by the L7b open complementary-arc footprint.",
            "Therefore the e2 support must choose its other incident rhombus, which contains v*.",
            "Every e3 support contains v* because v* is an endpoint of e3.",
            "Thus the e2 and e3 supports intersect at v*, contradicting L5 disjointness for the non-overlapping leaves."
        ],
        "scope": [
            "The obstruction is independent of support face-count bounds.",
            "It applies to the frozen e1/e2/e3 assignment and the explicit three-interval star source.",
            "It is not an obstruction to every possible incidence lift or target assignment.",
            "It is not a Hall counterexample and does not prove or disprove the all-orders Hall inequality."
        ]
    }
    print(json.dumps(result, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
