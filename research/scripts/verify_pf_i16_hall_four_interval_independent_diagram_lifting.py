#!/usr/bin/env python3
"""Enumerate independent four-support realizations for graph-5 / graph-12.

Unlike witness_lifting.py, this verifier does NOT require the same exact
first-three face indices on the two source families. It records the complete
labelled intersection data, union/deletion collapses, and anchored multi-
footprint words for every actual four-support realization. It tests the
adopted coarse parent signature after deleting interval 4.

This is still a finite Ngrid=12 diagnostic. It does not claim an explicit
source-parent diagram isomorphism or all-further-deletion coherence.
"""
from __future__ import annotations
import argparse, hashlib, itertools, json
from collections import defaultdict
from pathlib import Path
import verify_pf_i16_hall_four_interval_parent_compatibility as geom

def edge_key(row):
    return tuple(row["lower"]), tuple(row["upper"])

def edge_obj(e):
    return {"lower": list(e[0]), "upper": list(e[1])}

def digest(x):
    return hashlib.sha256(json.dumps(x, sort_keys=True, separators=(",", ":")).encode()).hexdigest()

def boundary_cycle(support, directed, face_edges):
    from collections import Counter
    counts=Counter()
    for fid in support:
        counts.update(face_edges[fid])
    boundary=[e for e,n in counts.items() if n==1]
    adj=defaultdict(list)
    for a,b in boundary:
        adj[a].append(b); adj[b].append(a)
    if not adj or any(len(v)!=2 for v in adj.values()):
        return None
    tail,head=directed
    if tuple(sorted((tail,head))) not in set(boundary):
        return None
    cycle=[tail,head]; previous,current=tail,head
    while True:
        choices=[v for v in adj[current] if v!=previous]
        if len(choices)!=1:
            return None
        nxt=choices[0]
        if nxt==tail:
            break
        if nxt in cycle:
            return None
        cycle.append(nxt); previous,current=current,nxt
    return cycle if len(cycle)==len(adj) else None

def footprint_word(supports, edges, cells, intersection, face_edges):
    """Return anchored open-arc words, retaining footprint meet relations."""
    result=[]
    for i,si in enumerate(supports):
        cycle=boundary_cycle(si,edges[i],face_edges)
        if cycle is None:
            return None
        tail,head=edges[i]
        arc=[]; k=cycle.index(head)
        while True:
            arc.append(cycle[k])
            if cycle[k]==tail:
                break
            k=(k+1)%len(cycle)
        row=[]
        for j,sj in enumerate(supports):
            if i==j:
                continue
            common=intersection([si,sj])
            if not common[2]:
                continue
            _,shared_edges,shared_vertices=common
            if len(shared_vertices)==1 and not shared_edges:
                v=next(iter(shared_vertices))
                if v not in arc[1:-1]:
                    return None
                row.append({"neighbor":j,"cell_type":"vertex",
                            "arc_positions":[arc.index(v)],
                            "cell_vertices":[list(v)]})
            elif len(shared_edges)==1 and len(shared_vertices)==2:
                e=next(iter(shared_edges))
                positions=[q for q in range(len(arc)-1)
                           if set((arc[q],arc[q+1]))==set(e)]
                if len(positions)!=1 or positions[0]==0 or positions[0]>=len(arc)-2:
                    return None
                q=positions[0]
                row.append({"neighbor":j,"cell_type":"edge",
                            "arc_positions":[q,q+1],
                            "cell_vertices":[list(arc[q]),list(arc[q+1])]})
            else:
                return None
        row.sort(key=lambda x:(x["arc_positions"][0],x["neighbor"]))
        meets=[]
        for a,b in itertools.combinations(row,2):
            av={tuple(v) for v in a["cell_vertices"]}
            bv={tuple(v) for v in b["cell_vertices"]}
            meets.append({"neighbors":[a["neighbor"],b["neighbor"]],
                          "meet":bool(av&bv)})
        result.append({"support":i,
                       "ordered_footprints":row,
                       "footprint_meet_relations":meets})
    return result

def diagram(supports, edges, cells, union, intersection, collapse,
            point_contractible, face_edges):
    rows=[]
    for r in range(1,5):
        for inds in itertools.combinations(range(4),r):
            cc=intersection([supports[i] for i in inds])
            nonempty=bool(cc[2])
            rows.append({
                "indices":list(inds),
                "nonempty":nonempty,
                "face_count":len(cc[0]),
                "edge_count":len(cc[1]),
                "vertex_count":len(cc[2]),
                "point_contractible":bool(point_contractible(cc)) if nonempty else None,
                "cell_digest":digest([sorted(map(str,sorted(cc[k]))) for k in range(3)])
            })
    uu=union(supports)
    relative={str(i):bool(collapse(uu,union([supports[j] for j in range(4) if j!=i])))
              for i in range(4)}
    word=footprint_word(supports,edges,cells,intersection,face_edges)
    return {
        "intersections":rows,
        "all_nonempty_intersections_point_contractible":
            all(x["point_contractible"] for x in rows if x["nonempty"]),
        "union":{"face_count":len(uu[0]),"edge_count":len(uu[1]),
                 "vertex_count":len(uu[2]),
                 "point_contractible":bool(point_contractible(uu))},
        "relative_deletion_collapses":relative,
        "delete_interval_4_relative_collapse":relative["3"],
        "anchored_boundary_footprint_words":word
    }

def parent_signature(supports, union, intersection, collapse, point_contractible):
    """Coarse L6c signature of the retained 0,1,2 parent after deleting 3."""
    pairs=[]
    for i,j in ((0,1),(0,2),(1,2)):
        cc=intersection([supports[i],supports[j]])
        pairs.append({"indices":[i,j],"nonempty":bool(cc[2]),
                      "point_contractible":bool(point_contractible(cc)) if cc[2] else None})
    tri=intersection(supports)
    uu=union(supports)
    return {
        "pair_intersections":pairs,
        "triple_intersection":{"nonempty":bool(tri[2]),
            "point_contractible":bool(point_contractible(tri)) if tri[2] else None},
        "union_point_contractible":bool(point_contractible(uu)),
        "retained_parent_relative_collapses":{
            "delete_interval_2":bool(collapse(uu,union([supports[0],supports[2]]))),
            "delete_interval_3":bool(collapse(uu,union([supports[0],supports[1]])))
        }
    }

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--inventory",type=Path,required=True)
    ap.add_argument("--replacement",type=Path,required=True)
    ap.add_argument("--output",type=Path,required=True)
    a=ap.parse_args()
    inv=json.loads(a.inventory.read_text())
    rep=json.loads(a.replacement.read_text())
    fv,fe,options,_=geom.build_target(inv)
    cells,union,intersection,collapse,point_contractible,edge_contractible,footprint=geom.make_geometry(fv,fe)
    e1=edge_key(inv["fixed_triple_edges"][0])
    all_options=[]; by_edge=defaultdict(list); support_cells=[]
    for e in sorted(options):
        for s in options[e]:
            oid=len(all_options); s=frozenset(s)
            all_options.append((e,s)); by_edge[e].append(oid)
            support_cells.append(cells(tuple(sorted(s))))
    edge_collapse_cache={}
    def edge_collapses(oid):
        if oid not in edge_collapse_cache:
            e,s=all_options[oid]; f,ed,v=support_cells[oid]
            edge_collapse_cache[oid]=collapse((set(f),set(ed),set(v)),
                (set(),{tuple(sorted(e))},set(e)))
        return edge_collapse_cache[oid]
    def pair_ok(i,j,required):
        si,sj=all_options[i][1],all_options[j][1]
        cc=intersection([si,sj]); nonempty=bool(cc[2])
        if nonempty!=required:
            return False
        if not required:
            return True
        return (point_contractible(cc)
                and footprint(si,sj,all_options[i][0])
                and footprint(sj,si,all_options[j][0]))
    pairs={}
    for row in rep["common_edge_witnesses"]:
        e2=edge_key(row["second_edge"]); e3=edge_key(row["third_edge"])
        pairs[(e2,e3)]={edge_key(x) for x in row["common_fourth_edges"]}
    if len(pairs)!=52:
        raise AssertionError(("expected 52 replacement pairs",len(pairs)))
    first_oids=[i for i in by_edge[e1] if edge_collapses(i)]
    out_pairs=[]; total_triples=0; total_g5=0; total_g12=0
    total_common_full_edges=0; pairs_with_common_full=0
    for (e2,e3),e4_candidates in sorted(pairs.items()):
        first_pairs=[]
        for i1 in first_oids:
            for i2 in by_edge[e2]:
                if edge_collapses(i2) and pair_ok(i1,i2,True):
                    first_pairs.append((i1,i2))
        triples=[]
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
                triples.append((i1,i2,i3))
        total_triples+=len(triples)
        g5_records=[]; g12_records=[]
        for e4 in sorted(e4_candidates):
            for i1,i2,i3 in triples:
                s1,s2,s3=(all_options[i][1] for i in (i1,i2,i3))
                for i4 in by_edge[e4]:
                    if not edge_collapses(i4): continue
                    s4=all_options[i4][1]
                    if (pair_ok(i1,i4,True) and pair_ok(i2,i4,False)
                        and pair_ok(i3,i4,False)):
                        ss=[s1,s2,s3,s4]
                        d=diagram(ss,[e1,e2,e3,e4],cells,union,intersection,
                                  collapse,point_contractible,fe)
                        ps=parent_signature(ss[:3],union,intersection,collapse,point_contractible)
                        g5_records.append({"fourth_edge":edge_obj(e4),
                            "support_face_indices":[sorted(all_options[i][1]) for i in (i1,i2,i3,i4)],
                            "parent_restriction_signature":ps,"diagram":d})
                    if (pair_ok(i1,i4,False) and pair_ok(i2,i4,True)
                        and pair_ok(i3,i4,True)):
                        ss=[s1,s2,s3,s4]
                        d=diagram(ss,[e1,e2,e3,e4],cells,union,intersection,
                                  collapse,point_contractible,fe)
                        ps=parent_signature(ss[:3],union,intersection,collapse,point_contractible)
                        g12_records.append({"fourth_edge":edge_obj(e4),
                            "support_face_indices":[sorted(all_options[i][1]) for i in (i1,i2,i3,i4)],
                            "parent_restriction_signature":ps,"diagram":d})
        total_g5+=len(g5_records); total_g12+=len(g12_records)
        def good_parent4(rec):
            d=rec["diagram"]
            return (d["all_nonempty_intersections_point_contractible"]
                    and d["union"]["point_contractible"]
                    and d["delete_interval_4_relative_collapse"])
        good5=[x for x in g5_records if good_parent4(x)]
        good12=[x for x in g12_records if good_parent4(x)]
        edges5={edge_key(x["fourth_edge"]) for x in good5}
        edges12={edge_key(x["fourth_edge"]) for x in good12}
        common=sorted(edges5&edges12)
        if common:
            pairs_with_common_full+=1; total_common_full_edges+=len(common)
        out_pairs.append({
            "second_edge":edge_obj(e2),"third_edge":edge_obj(e3),
            "aggregated_common_fourth_edge_count":len(e4_candidates),
            "qualifying_first_three_assignments":len(triples),
            "graph5_actual_four_support_count":len(g5_records),
            "graph12_actual_four_support_count":len(g12_records),
            "graph5_parent4_full_diagram_count":len(good5),
            "graph12_parent4_full_diagram_count":len(good12),
            "common_fourth_edges_with_independent_full_parent4_lifts":[edge_obj(e) for e in common],
            "graph5_witnesses":good5,
            "graph12_witnesses":good12
        })
    result={
        "schema":"PF-I16-HALL-FOUR-INTERVAL-INDEPENDENT-DIAGRAM-LIFTING-v1",
        "target":inv["target"],
        "replacement_json_sha256":hashlib.sha256(a.replacement.read_bytes()).hexdigest(),
        "fixed_first_edge":edge_obj(e1),
        "aggregated_pairs_reopened":len(pairs),
        "qualifying_first_three_assignments_sum":total_triples,
        "graph5_actual_four_support_witnesses":total_g5,
        "graph12_actual_four_support_witnesses":total_g12,
        "pairs_with_common_fourth_edge_and_independent_full_parent4_lifts":pairs_with_common_full,
        "common_fourth_edges_with_independent_full_parent4_lifts_sum":total_common_full_edges,
        "per_pair":out_pairs,
        "nonclaims":[
            "The two graph families use independent first-three support assignments; this is compatible with the adopted L6c dimension/identity-forgetting convention but is not itself an explicit diagram isomorphism.",
            "The parent restriction signature is a coarse finite L6c signature; it has not been compared to every actual source-parent record.",
            "Boundary words are exported with exact order and footprint meeting data, but no source-prescribed multi-footprint word has yet been certified against all relevant order-eight sources.",
            "No restriction coherence under all further deletions, all-orders accepted-face confluence, geometric L8, or all-orders Hall theorem is proved."
        ]
    }
    a.output.parent.mkdir(parents=True,exist_ok=True)
    a.output.write_text(json.dumps(result,sort_keys=True,indent=2)+"\n")
    print(json.dumps({k:v for k,v in result.items() if k!="per_pair"},sort_keys=True,indent=2))

if __name__=="__main__":
    main()
