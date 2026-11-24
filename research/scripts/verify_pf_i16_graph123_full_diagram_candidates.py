#!/usr/bin/env python3
"""Lift graph-1/2/3 parent-compatible fourth-edge candidates to full diagrams.

The parent-compatibility search only checks the first-three parent restriction
and the fourth support's pairwise incidence/footprints. This verifier
independently checks all 15 labelled intersections, all four relative
deletion collapses, the full union, and anchored multi-footprint boundary
words for each candidate witness.
"""
from __future__ import annotations
import argparse, hashlib, itertools, json, traceback
from collections import Counter, defaultdict
from pathlib import Path

import verify_pf_i16_hall_four_interval_parent_compatibility as geom
import verify_pf_i16_order8_oriented_collapse_diamond_naturality as order8

def digest_bytes(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--inventory",type=Path,required=True)
    ap.add_argument("--parent-compatibility",type=Path,required=True)
    ap.add_argument("--output",type=Path,required=True)
    args=ap.parse_args()
    inv=json.loads(args.inventory.read_text())
    compat=json.loads(args.parent_compatibility.read_text())
    assert compat["schema"]=="PF-I16-HALL-FOUR-INTERVAL-PARENT-COMPATIBILITY-v1"
    fv,fe,options,_=geom.build_target(inv)
    cells,union,intersection,collapse,point_contractible,edge_contractible,footprint=geom.make_geometry(fv,fe)
    order8.FACE_EDGES=fe
    fixed=[(tuple(x["lower"]),tuple(x["upper"])) for x in inv["fixed_triple_edges"]]
    assert len(fixed)==3
    graphs={x["graph_index"]:frozenset(tuple(sorted(e)) for e in x["edges"])
            for x in compat["four_interval_graphs"]}
    selected=[x for x in compat["all_graph_candidate_edges_with_support_witnesses"]
              if x["graph_index"] in (1,2,3)]
    expected={1:99,2:110,3:75}
    assert {x["graph_index"]:len(x["candidate_witnesses"]) for x in selected}==expected

    results=[]
    summary_debug={}
    passed_by_graph=Counter()
    fail_by_graph=defaultdict(Counter)
    boundary_lengths=Counter()
    footprint_counts=Counter()
    intersection_hist=Counter()
    for fam in selected:
        gi=fam["graph_index"]; graph=graphs[gi]
        for wi,w in enumerate(fam["candidate_witnesses"]):
            supports=[frozenset(x) for x in w["first_three_support_face_indices"]]
            supports.append(frozenset(w["fourth_support_face_indices"]))
            edge=w["edge"]
            edges=fixed+[(tuple(edge["lower"]),tuple(edge["upper"]))]
            row={"graph_index":gi,"candidate_index":wi,"fourth_edge":edge,
                 "support_face_indices":[sorted(s) for s in supports],
                 "checks":{},"failures":[]}
            try:
                complexes=[order8.complex_dict(cells(tuple(sorted(s)))) for s in supports]
                # Each marked support must collapse to its exact matched edge.
                edge_ok=[]
                for i,(F,E,V) in enumerate(complexes):
                    target=(set(),{tuple(sorted(edges[i]))},set(edges[i]))
                    edge_ok.append(bool(collapse((set(F),set(E),set(V)),target)))
                row["checks"]["four_matched_edge_relative_collapses"]=edge_ok
                if not all(edge_ok): row["failures"].append("matched_edge_relative_collapse")
                # All 15 labelled intersections are recomputed, including empty entries.
                intersections=[]
                for r in range(1,5):
                    for inds in itertools.combinations(range(4),r):
                        cc=order8.intersection_complex(complexes,inds)
                        nonempty=bool(cc["V"])
                        pc=bool(point_contractible(tuple(cc[k] for k in ("F","E","V")))) if nonempty else None
                        entry={"indices":list(inds),"nonempty":nonempty,
                               "face_count":len(cc["F"]),"edge_count":len(cc["E"]),
                               "vertex_count":len(cc["V"]),"point_contractible":pc}
                        intersections.append(entry)
                        intersection_hist[(r,nonempty,pc)]+=1
                        if nonempty and not pc:
                            row["failures"].append("noncontractible_intersection:"+",".join(map(str,inds)))
                row["checks"]["all_15_intersections"]=len(intersections)==15
                row["checks"]["all_nonempty_intersections_point_contractible"]=all(
                    x["point_contractible"] for x in intersections if x["nonempty"])
                row["intersections"]=intersections
                # The complete four-support overlap graph must equal the source graph.
                actual=frozenset(tuple(x["indices"]) for x in intersections
                                 if len(x["indices"])==2 and x["nonempty"])
                row["checks"]["full_overlap_graph_matches"]=actual==graph
                if actual!=graph:
                    row["failures"].append("full_overlap_graph_mismatch")
                # Full union and all four relative deletions.
                full=order8.union_complex(complexes,range(4))
                union_pc=bool(point_contractible(tuple(full[k] for k in ("F","E","V"))))
                row["checks"]["four_support_union_point_contractible"]=union_pc
                if not union_pc: row["failures"].append("union_not_point_contractible")
                relative={}
                for i in range(4):
                    retained=order8.union_complex(complexes,[j for j in range(4) if j!=i])
                    relative[str(i)]=bool(collapse(
                        tuple(full[k] for k in ("F","E","V")),
                        tuple(retained[k] for k in ("F","E","V"))))
                row["checks"]["all_four_relative_deletion_collapses"]=relative
                if not all(relative.values()): row["failures"].append("relative_deletion_collapse")
                # Reconstruct anchored cycles and all ordered multi-footprint words.
                cycles=[]
                for i in range(4):
                    cyc=order8.boundary_cycle(complexes[i],edges[i],fe)
                    if cyc is None:
                        raise AssertionError(("invalid anchored boundary cycle",i))
                    cycles.append(cyc); boundary_lengths[len(cyc)]+=1
                words=[]
                for i in range(4):
                    word=order8.derive_footprint_word(i,complexes,cycles)
                    words.append(word); footprint_counts[len(word)]+=1
                row["checks"]["four_anchored_boundary_cycles"]=True
                row["checks"]["four_ordered_footprint_words"]=True
                row["boundary_lengths"]=[len(x) for x in cycles]
                row["footprint_counts"]=[len(x) for x in words]
                row["footprint_words"]=words
                row["full_diagram_pass"]=not row["failures"]
            except Exception as e:
                row["failures"].append(type(e).__name__+":"+str(e))
                if "traceback" not in summary_debug:
                    summary_debug["traceback"]=traceback.format_exc()
                row["full_diagram_pass"]=False
            if row["full_diagram_pass"]:
                passed_by_graph[gi]+=1
            else:
                for reason in row["failures"]:
                    fail_by_graph[gi][reason.split(":")[0]]+=1
            results.append(row)

    summary={
        "schema":"PF-I16-GRAPH123-FULL-DIAGRAM-CANDIDATE-AUDIT-v1",
        "input_sha256":{"inventory":digest_bytes(args.inventory),
                        "parent_compatibility":digest_bytes(args.parent_compatibility)},
        "candidate_counts":expected,
        "full_diagram_pass_counts":{str(k):passed_by_graph[k] for k in (1,2,3)},
        "full_diagram_failure_counts":{str(k):dict(fail_by_graph[k]) for k in (1,2,3)},
        "boundary_length_histogram":dict(sorted(boundary_lengths.items())),
        "footprint_count_histogram":dict(sorted(footprint_counts.items())),
        "intersection_census":{
            str(k):v for k,v in sorted(intersection_hist.items(),key=lambda x:str(x[0]))
        },
        "total_candidates":len(results),
        "total_full_diagram_passes":sum(passed_by_graph.values()),
        "first_failure_traceback":summary_debug.get("traceback"),
        "nonclaims":[
            "this candidate family is finite and limited to graph families 1, 2, and 3",
            "no source-to-target port map or source deletion diamond is checked here",
            "a full finite diagram pass does not prove all-orders L6c/L7b naturality or Hall"
        ],
        "candidates":results
    }
    args.output.write_text(json.dumps(summary,sort_keys=True,indent=2)+"\n")
    print(json.dumps({k:v for k,v in summary.items() if k not in ("candidates","intersection_census")},sort_keys=True))

if __name__=="__main__":
    main()
