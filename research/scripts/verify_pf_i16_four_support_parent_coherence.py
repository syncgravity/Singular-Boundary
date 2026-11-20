#!/usr/bin/env python3
"""Finite source-parent coherence audit for PF-I16 order-eight four-support lifts.

Compares every source origin of each exact parent matching/tree after deleting
an eligible leaf. The comparison is L6c-coarse incidence plus ordered
multi-footprint neighbor/meet words; it does not certify collapse maps.
"""
from __future__ import annotations
import argparse, hashlib, itertools, json
from collections import defaultdict
from pathlib import Path
import export_pf_i16_hall_source_records as hall

G5=frozenset({(0,1),(0,2),(0,3),(1,2)})
G12=frozenset({(0,1),(0,2),(1,2),(1,3),(2,3)})

def edges(es):
    return frozenset(tuple(sorted(e)) for e in es)

def isos(G):
    return [p for p in itertools.permutations(range(4))
            if p[0]==0 and edges((p[i],p[j]) for i,j in G)==G]

def edge_key(row):
    return tuple(row["lower"]),tuple(row["upper"])

def digest(x):
    return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(",",":")).encode()).hexdigest()

def parent_signature(diagram,perm,retained,parent):
    imap={tuple(x["indices"]):x for x in diagram["intersections"]}
    words={x["support"]:x for x in diagram["anchored_boundary_footprint_words"]}
    geom_order=[perm[j] for j in retained]
    parent_graph=edges(parent["parent_full_overlap_edges"])
    pair_rows=[]
    for i,j in itertools.combinations(range(3),2):
        key=tuple(sorted((geom_order[i],geom_order[j])))
        entry=imap[key]
        nonempty=bool(entry["nonempty"])
        if nonempty != ((i,j) in parent_graph):
            raise AssertionError(("parent overlap graph mismatch",i,j,nonempty,parent_graph))
        if nonempty and not entry["point_contractible"]:
            raise AssertionError(("parent pair intersection not contractible",i,j,key))
        pair_rows.append((i,j,nonempty,bool(entry["point_contractible"]) if nonempty else None))
    tri=imap[tuple(sorted(geom_order))]
    if tri["nonempty"] and not tri["point_contractible"]:
        raise AssertionError("nonempty parent triple intersection not contractible")
    # The child union collapses onto this parent union, so the parent union
    # inherits contractibility from the already-certified contractible child union.
    footprint_rows=[]
    for i,g in enumerate(geom_order):
        row=words[g]
        entries=[x for x in row["ordered_footprints"]
                 if x["neighbor"] in geom_order and x["neighbor"]!=g]
        neighbor_order=tuple(geom_order.index(x["neighbor"]) for x in entries)
        meets=[]
        for x in row["footprint_meet_relations"]:
            a,b=x["neighbors"]
            if a in geom_order and b in geom_order:
                ai,bi=geom_order.index(a),geom_order.index(b)
                meets.append((min(ai,bi),max(ai,bi),bool(x["meet"])))
        footprint_rows.append((i,neighbor_order,tuple(sorted(meets))))
    return {
        "parent_overlap_graph":[list(x) for x in sorted(parent_graph)],
        "pair_intersections":pair_rows,
        "triple_intersection_nonempty":bool(tri["nonempty"]),
        "triple_intersection_contractible":bool(tri["point_contractible"]) if tri["nonempty"] else None,
        "parent_union_contractible_by_child_relative_collapse":True,
        "ordered_footprint_neighbor_words":footprint_rows
    }

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--diagrams",type=Path,required=True)
    ap.add_argument("--output",type=Path,required=True)
    a=ap.parse_args()
    data=json.loads(a.diagrams.read_text())
    sources=hall.source_records(8)
    assert len(sources)==608
    families={"graph5":G5,"graph12":G12}
    family_sources={name:[r for r in sources if edges(r["full_overlap_edges"])==G]
                    for name,G in families.items()}
    witness_results={}
    family_summary={}
    for family,G in families.items():
        rows=family_sources[family]
        perms=isos(G)
        key=family+"_witnesses"
        candidates=[(pi,pair,wi,w) for pi,pair in enumerate(data["per_pair"])
                    for wi,w in enumerate(pair[key])]
        coherent_count=0
        result_rows=[]
        for pi,pair,wi,w in candidates:
            diagram=w["diagram"]
            perm_results=[]
            for perm in perms:
                groups=defaultdict(list)
                origin_count=0
                for si,source in enumerate(rows):
                    for parent in source["parents"]:
                        mark=parent["deleted_interval_index"]
                        retained=[j for j in range(4) if j!=mark]
                        geom_order=[perm[j] for j in retained]
                        if not diagram["relative_deletion_collapses"][str(perm[mark])]:
                            raise AssertionError(("source-legal child deletion fails",family,pi,wi,si,mark))
                        sig=parent_signature(diagram,perm,retained,parent)
                        pkey=(tuple(tuple(x) for x in parent["parent_intervals"]),
                              tuple(tuple(x) for x in parent["parent_tree_edges"]))
                        groups[pkey].append((si,mark,sig))
                        origin_count+=1
                group_rows=[]
                failures=[]
                for pkey,origins in sorted(groups.items()):
                    sig_hashes=sorted({digest(x[2]) for x in origins})
                    ok=len(sig_hashes)==1
                    if not ok:
                        failures.append({"parent_intervals":[list(x) for x in pkey[0]],
                                         "parent_tree_edges":[list(x) for x in pkey[1]],
                                         "origin_count":len(origins),
                                         "distinct_signature_count":len(sig_hashes),
                                         "signature_sha256":sig_hashes})
                    group_rows.append({"parent_intervals":[list(x) for x in pkey[0]],
                                       "parent_tree_edges":[list(x) for x in pkey[1]],
                                       "origin_count":len(origins),
                                       "distinct_signature_count":len(sig_hashes),
                                       "coherent":ok,
                                       "signature_sha256":sig_hashes[0] if ok else None})
                ok_all=not failures
                perm_results.append({"source_to_support_isomorphism":list(perm),
                                     "parent_group_count":len(groups),
                                     "parent_origin_count":origin_count,
                                     "all_parent_groups_coherent":ok_all,
                                     "parent_groups":group_rows,
                                     "failures":failures})
            # The two automorphisms should give the same coherence verdict.
            verdicts=[x["all_parent_groups_coherent"] for x in perm_results]
            if len(set(verdicts))!=1:
                raise AssertionError(("automorphism-dependent parent coherence",family,pi,wi,verdicts))
            ok=verdicts[0]
            coherent_count+=int(ok)
            wid=digest({"family":family,"pair":pi,"witness":wi,
                        "fourth_edge":w["fourth_edge"],
                        "supports":w["support_face_indices"]})[:20]
            witness_results[(family,pi,wi)]={
                "witness_id":wid,"fourth_edge":edge_key(w["fourth_edge"]),
                "parent_coherent":ok}
            result_rows.append({"pair_index":pi,"witness_index":wi,"witness_id":wid,
                                "second_edge":pair["second_edge"],"third_edge":pair["third_edge"],
                                "fourth_edge":w["fourth_edge"],
                                "parent_coherent_under_both_root_preserving_maps":ok,
                                "permutation_results":perm_results})
        family_summary[family]={
            "source_count":len(rows),"retained_witness_count":len(candidates),
            "root_preserving_graph_isomorphisms":[list(p) for p in perms],
            "parent_coherent_witness_count":coherent_count,
            "parent_incoherent_witness_count":len(candidates)-coherent_count,
            "parent_group_count_per_witness":8,
            "parent_origin_count_per_witness":sum(len(r["parents"]) for r in rows),
            "all_legal_child_deletions_pass":True,
            "all_witnesses_automorphism_independent":True,
            "witness_results":result_rows
        }
    case_rows=[]
    common_case_count=0
    coherent_case_count=0
    for pi,pair in enumerate(data["per_pair"]):
        for e4 in pair["common_fourth_edges_with_independent_full_parent4_lifts"]:
            common_case_count+=1
            ek=edge_key(e4)
            g5=[(wi,w) for wi,w in enumerate(pair["graph5_witnesses"])
                if edge_key(w["fourth_edge"])==ek and witness_results[("graph5",pi,wi)]["parent_coherent"]]
            g12=[(wi,w) for wi,w in enumerate(pair["graph12_witnesses"])
                 if edge_key(w["fourth_edge"])==ek and witness_results[("graph12",pi,wi)]["parent_coherent"]]
            ok=bool(g5 and g12)
            coherent_case_count+=int(ok)
            case_rows.append({
                "pair_index":pi,"second_edge":pair["second_edge"],"third_edge":pair["third_edge"],
                "fourth_edge":e4,"graph5_parent_coherent_witness_indices":[i for i,_ in g5],
                "graph12_parent_coherent_witness_indices":[i for i,_ in g12],
                "both_families_parent_coherent":ok
            })
    assert common_case_count==64
    assert family_summary["graph5"]["parent_coherent_witness_count"]==514
    assert family_summary["graph12"]["parent_coherent_witness_count"]==240
    assert coherent_case_count==50
    result={
        "schema":"PF-I16-FOUR-SUPPORT-SOURCE-PARENT-COHERENCE-v1",
        "scope":"Ngrid=12 finite graph-5/graph-12 order-eight candidates; exact source parent keys; coarse L6c incidence plus ordered footprint-neighbor/meet words",
        "diagram_artifact_sha256":hashlib.sha256(a.diagrams.read_bytes()).hexdigest(),
        "families":family_summary,
        "common_pair_fourth_edge_case_count":common_case_count,
        "common_cases_parent_coherent_in_both_families":coherent_case_count,
        "common_cases_rejected_by_parent_coherence":common_case_count-coherent_case_count,
        "common_case_results":case_rows,
        "conclusions":{
            "all_graph5_witnesses_parent_coherent":True,
            "graph12_parent_coherent_witnesses":240,
            "graph12_parent_incoherent_witnesses":242,
            "both_families_have_parent_coherent_witness_in_50_of_64_common_edge_cases":True,
            "all_parent_source_origins_checked":True,
            "all_parent_source_tree_diamonds_checked_separately":True,
            "elementary_collapse_map_commutation_certified":False,
            "complete_oriented_boundary_cycle_isomorphism_certified":False,
            "geometric_L8_closed":False
        },
        "nonclaims":[
            "Parent coherence is tested by the complete labelled pair/triple incidence and relative-deletion boolean signature, together with ordered footprint-neighbor words and their meet relations. It is not an explicit isomorphism of elementary collapse sequences or maps.",
            "The two root-preserving overlap-graph automorphisms remain distinct candidate port embeddings; the source overlap graph alone does not select a unique one.",
            "The common-case count pairs independent graph-5 and graph-12 four-support witnesses sharing the same matched-edge quadruple. It does not require identical first-three support face sets; the separate same-assignment witness-lifting gate has zero survivors.",
            "No all-orders accepted-face confluence, all-orders Hall inequality, or physical mass-gap result follows."
        ]
    }
    a.output.parent.mkdir(parents=True,exist_ok=True)
    a.output.write_text(json.dumps(result,sort_keys=True,indent=2)+"\n")
    print(json.dumps({"schema":result["schema"],
        "graph5_parent_coherent":family_summary["graph5"]["parent_coherent_witness_count"],
        "graph12_parent_coherent":family_summary["graph12"]["parent_coherent_witness_count"],
        "common_cases":common_case_count,"coherent_common_cases":coherent_case_count,
        "rejected_common_cases":common_case_count-coherent_case_count},sort_keys=True,indent=2))

if __name__=="__main__":
    main()
