#!/usr/bin/env python3
"""Recover same-triple witnesses behind aggregated second-edge survivors.

This is a stricter witness-lifting gate, not the final L6c/L7b theorem.
For each of the 52 (second, third) pairs retained by the replacement search,
it requires one identical first-three support assignment to admit an actual
fourth support for BOTH decisive graph-5 and graph-12 attachment patterns.
Each fourth support must collapse to its distinguished edge; pairwise
intersection/nonintersection, point-collapse, and two-sided open-arc tests
are recomputed. All nonempty higher intersections, union collapses, and
single-deletion relative collapses are exported as data for the next full
diagram comparison.

No Hall demands, loads, deficiencies, matchings, or flows are read.
"""
from __future__ import annotations
import argparse, hashlib, itertools, json
from collections import defaultdict
from pathlib import Path
import verify_pf_i16_hall_four_interval_parent_compatibility as geom

def edge_key(row):
    return (tuple(row["lower"]), tuple(row["upper"]))

def edge_obj(e):
    return {"lower": list(e[0]), "upper": list(e[1])}

def digest(obj):
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--inventory", type=Path, required=True)
    ap.add_argument("--replacement", type=Path, required=True)
    ap.add_argument("--output", type=Path, required=True)
    a=ap.parse_args()
    inv=json.loads(a.inventory.read_text())
    rep=json.loads(a.replacement.read_text())
    fv,fe,options,_=geom.build_target(inv)
    cells,union,intersection,collapse,point_contractible,edge_contractible,footprint=geom.make_geometry(fv,fe)

    e1=edge_key(inv["fixed_triple_edges"][0])
    all_options=[]
    by_edge=defaultdict(list)
    support_cells=[]
    for e in sorted(options):
        for s in options[e]:
            oid=len(all_options)
            s=frozenset(s)
            all_options.append((e,s))
            by_edge[e].append(oid)
            support_cells.append(cells(tuple(sorted(s))))

    edge_collapse_cache={}
    def edge_collapses(oid):
        if oid not in edge_collapse_cache:
            e,s=all_options[oid]
            f,ed,v=support_cells[oid]
            edge_collapse_cache[oid]=collapse((set(f),set(ed),set(v)),
                (set(),{tuple(sorted(e))},set(e)))
        return edge_collapse_cache[oid]

    def pair_ok(i,j,required):
        si, sj=all_options[i][1], all_options[j][1]
        common=intersection([si,sj])
        nonempty=bool(common[2])
        if nonempty != required:
            return False
        if not required:
            return True
        return (point_contractible(common)
                and footprint(si,sj,all_options[i][0])
                and footprint(sj,si,all_options[j][0]))

    def family_diagram(oids):
        ss=[all_options[i][1] for i in oids]
        diagram=[]
        for r in range(1,len(ss)+1):
            for inds in itertools.combinations(range(len(ss)),r):
                cc=intersection([ss[i] for i in inds])
                nonempty=bool(cc[2])
                diagram.append({
                    "indices":list(inds),
                    "nonempty":nonempty,
                    "face_count":len(cc[0]),"edge_count":len(cc[1]),"vertex_count":len(cc[2]),
                    "point_contractible": bool(point_contractible(cc)) if nonempty else None,
                    "cell_digest":digest([sorted(map(str, sorted(cc[k]))) for k in range(3)])
                })
        uu=union(ss)
        return {
            "intersection_diagram":diagram,
            "union_cells":{"face_count":len(uu[0]),"edge_count":len(uu[1]),"vertex_count":len(uu[2]),
                           "point_contractible":bool(point_contractible(uu))},
            "relative_deletion_collapses":{
                str(i):bool(collapse(uu,union([ss[j] for j in range(len(ss)) if j!=i])))
                for i in range(len(ss))
            }
        }

    # The first edge is fixed by the preceding frontier. Only the 52 pairs
    # from the audited aggregated survivor list are reopened.
    pairs={}
    for row in rep["common_edge_witnesses"]:
        e2=edge_key(row["second_edge"]); e3=edge_key(row["third_edge"])
        pairs[(e2,e3)]={edge_key(x) for x in row["common_fourth_edges"]}
    if len(pairs)!=52:
        raise AssertionError(("expected all 52 surviving pairs",len(pairs)))

    first_oids=[i for i in by_edge[e1] if edge_collapses(i)]
    first_end=set(e1)
    rows=[]
    total_triangle_assignments=0
    total_same_triple_common=0
    total_full_pairwise_witnesses=0

    for (e2,e3), e4_candidates in sorted(pairs.items()):
        first_pairs=[]
        for i1 in first_oids:
            for i2 in by_edge[e2]:
                if not edge_collapses(i2): continue
                if not pair_ok(i1,i2,True): continue
                first_pairs.append((i1,i2))
        pair_assignments=0
        same_triple=[]
        for i1,i2 in first_pairs:
            s1,s2=all_options[i1][1],all_options[i2][1]
            for i3 in by_edge[e3]:
                if not edge_collapses(i3): continue
                if not pair_ok(i1,i3,True) or not pair_ok(i2,i3,True): continue
                ss=[s1,s2,all_options[i3][1]]
                uu=union(ss)
                if not point_contractible(uu): continue
                if not collapse(uu,union([ss[0],ss[2]])): continue
                if not collapse(uu,union([ss[0],ss[1]])): continue
                pair_assignments+=1
                total_triangle_assignments+=1

                # The graph-5 attachment vector is (1,0,0);
                # graph-12 is (0,1,1), in interval order 0,1,2.
                supports_by_graph={"graph5":[],"graph12":[]}
                for e4 in sorted(e4_candidates):
                    for i4 in by_edge[e4]:
                        if not edge_collapses(i4): continue
                        ok5=(pair_ok(i1,i4,True)
                             and pair_ok(i2,i4,False)
                             and pair_ok(i3,i4,False))
                        ok12=(pair_ok(i1,i4,False)
                              and pair_ok(i2,i4,True)
                              and pair_ok(i3,i4,True))
                        if ok5: supports_by_graph["graph5"].append((e4,i4))
                        if ok12: supports_by_graph["graph12"].append((e4,i4))
                g5={e for e,_ in supports_by_graph["graph5"]}
                g12={e for e,_ in supports_by_graph["graph12"]}
                common=g5 & g12
                if common:
                    total_same_triple_common+=len(common)
                    witness_rows=[]
                    for e4 in sorted(common):
                        o5=[i for e,i in supports_by_graph["graph5"] if e==e4]
                        o12=[i for e,i in supports_by_graph["graph12"] if e==e4]
                        for i45 in o5:
                            for i412 in o12:
                                d5=family_diagram([i1,i2,i3,i45])
                                d12=family_diagram([i1,i2,i3,i412])
                                # A genuine candidate must have every nonempty
                                # higher intersection and the union collapsible,
                                # and all three single-deletion relative collapses.
                                full5=(all(x["point_contractible"] for x in d5["intersection_diagram"] if x["nonempty"])
                                       and d5["union_cells"]["point_contractible"]
                                       and all(d5["relative_deletion_collapses"].values()))
                                full12=(all(x["point_contractible"] for x in d12["intersection_diagram"] if x["nonempty"])
                                        and d12["union_cells"]["point_contractible"]
                                        and all(d12["relative_deletion_collapses"].values()))
                                witness_rows.append({
                                    "fourth_edge":edge_obj(e4),
                                    "support_face_indices_graph5":sorted(all_options[i45][1]),
                                    "support_face_indices_graph12":sorted(all_options[i412][1]),
                                    "graph5_diagram":d5,"graph12_diagram":d12,
                                    "all_intersections_union_and_deletions_contractible_graph5":full5,
                                    "all_intersections_union_and_deletions_contractible_graph12":full12
                                })
                    same_triple.append({
                        "first_three_support_face_indices":[
                            sorted(all_options[i][1]) for i in (i1,i2,i3)
                        ],
                        "common_fourth_edges":witness_rows
                    })
                    total_full_pairwise_witnesses+=len(witness_rows)
        rows.append({
            "second_edge":edge_obj(e2),"third_edge":edge_obj(e3),
            "aggregated_common_fourth_edge_count":len(e4_candidates),
            "first_two_support_pair_assignments":len(first_pairs),
            "qualifying_first_three_support_assignments":pair_assignments,
            "same_first_three_support_assignment_survivors":len(same_triple),
            "same_assignment_witnesses":same_triple
        })

    result={
        "schema":"PF-I16-HALL-FOUR-INTERVAL-WITNESS-LIFTING-v1",
        "target":inv["target"],
        "replacement_json_sha256":hashlib.sha256(a.replacement.read_bytes()).hexdigest(),
        "fixed_first_edge":edge_obj(e1),
        "aggregated_surviving_second_third_pairs":len(pairs),
        "qualifying_first_three_support_assignments_recomputed":total_triangle_assignments,
        "same_triple_common_fourth_edge_witness_count":total_same_triple_common,
        "full_pairwise_support_witness_tuple_count":total_full_pairwise_witnesses,
        "pairs_with_same_triple_survivor":sum(bool(x["same_assignment_witnesses"]) for x in rows),
        "per_pair":rows,
        "filters":[
            "Reopens every one of the 52 aggregated surviving (second,third) pairs.",
            "The same exact first-three support assignment must witness both graph-5 and graph-12 fourth-edge attachment patterns.",
            "Each of the four supports collapses to its distinguished matched edge.",
            "Every pairwise intersection/nonintersection matches the required graph and every nonempty pair intersection collapses to a vertex with two-sided open-arc footprints.",
            "The first-three union and the two retained triangle-parent deletion collapses are recomputed.",
            "All 15 pair/triple/four-way intersection entries, union collapse, and all three single-deletion relative collapses are recorded for every same-triple witness."
        ],
        "nonclaims":[
            "The two graph patterns are checked as separate four-interval source families; their fourth support may differ.",
            "The exported intersection and collapse data are not yet an explicit L6c diagram isomorphism against every source parent record.",
            "The exported footprint booleans are not the complete ordered multi-footprint L7b boundary-word comparison.",
            "This does not prove restriction coherence for all further source deletions, geometric L8, or the all-orders Hall inequality."
        ]
    }
    a.output.parent.mkdir(parents=True,exist_ok=True)
    a.output.write_text(json.dumps(result,sort_keys=True,indent=2)+"\n")
    print(json.dumps({k:v for k,v in result.items() if k!="per_pair"},sort_keys=True,indent=2))

if __name__=="__main__":
    main()
