#!/usr/bin/env python3
"""Exact relative-collapse certificates for order-eight four-support diamonds.

For every source critical deletion pair in graph-5/graph-12 and every retained
geometric witness/root-preserving labeling, computes both two-step elementary
collapse paths to the same grandparent support union.
"""
from __future__ import annotations
import argparse, gzip, hashlib, itertools, json
from collections import Counter, defaultdict
from pathlib import Path
import export_pf_i16_hall_source_records as hall

G5=frozenset({(0,1),(0,2),(0,3),(1,2)})
G12=frozenset({(0,1),(0,2),(1,2),(1,3),(2,3)})

def edges(es):
    return frozenset(tuple(sorted(e)) for e in es)

def isos(G):
    return [p for p in itertools.permutations(range(4))
            if p[0]==0 and edges((p[i],p[j]) for i,j in G)==G]

def digest(x):
    return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(",",":")).encode()).hexdigest()

def edge_key(row):
    return tuple(row["lower"]),tuple(row["upper"])

def face_vertices(row):
    m=tuple(row["lower"]); j,k=row["directions"]
    ej=tuple(int(t==j) for t in range(5)); ek=tuple(int(t==k) for t in range(5))
    add=lambda a,b:tuple(a[t]+b[t] for t in range(5))
    return {m,add(m,ej),add(add(m,ej),ek),add(m,ek)}

def edge_vertices(vertices):
    out=set()
    for a,b in itertools.combinations(sorted(vertices),2):
        if sum(abs(a[t]-b[t]) for t in range(5))==1:
            out.add(tuple(sorted((a,b))))
    return out

def cells(supports,face_vertices_table,face_edges_table):
    fs=set().union(*(set(s) for s in supports))
    es=set().union(*(face_edges_table[i] for i in fs))
    vs=set().union(*(face_vertices_table[i] for i in fs))
    return fs,es,vs

def collapse_certificate(src,tgt,face_vertices_table,face_edges_table):
    cf,ce,cv=map(set,src); tf,te,tv=map(set,tgt)
    face_edge_pairs=[]; edge_vertex_pairs=[]
    while True:
        found=None
        for edge in sorted(ce-te):
            incident=[fid for fid in cf if edge in face_edges_table[fid]]
            if len(incident)==1 and incident[0] not in tf:
                found=(edge,incident[0]); break
        if found is None: break
        edge,face=found
        ce.remove(edge); cf.remove(face)
        face_edge_pairs.append({"free_edge":[list(x) for x in edge],
                                "removed_face":face})
    while True:
        found=None
        for edge in sorted(ce-te):
            for vertex in edge:
                degree=sum(vertex in e for e in ce)
                in_face=any(vertex in face_vertices_table[fid] for fid in cf)
                if vertex not in tv and degree==1 and not in_face:
                    found=(vertex,edge); break
            if found is not None: break
        if found is None: break
        vertex,edge=found
        ce.remove(edge); cv.remove(vertex)
        edge_vertex_pairs.append({"free_vertex":list(vertex),
                                  "removed_edge":[list(x) for x in edge]})
    remainder={"extra_faces":len(cf-tf),"extra_edges":len(ce-te),
               "extra_vertices":len(cv-tv)}
    success=cf==tf and ce==te and cv==tv
    steps=([{"pair":"face-edge",**x} for x in face_edge_pairs]+
           [{"pair":"edge-vertex",**x} for x in edge_vertex_pairs])
    return {"success":success,"face_edge_pairs":face_edge_pairs,
            "edge_vertex_pairs":edge_vertex_pairs,"ordered_steps":steps,
            "pair_count":len(steps),"remainder":remainder}

def pair_token(step):
    if step["pair"]=="face-edge":
        edge=tuple(sorted(tuple(v) for v in step["free_edge"]))
        return ("face-edge",edge,int(step["removed_face"]))
    edge=tuple(sorted(tuple(v) for v in step["removed_edge"]))
    return ("edge-vertex",tuple(step["free_vertex"]),edge)

def cell_tokens(step):
    if step["pair"]=="face-edge":
        return {("edge",tuple(sorted(tuple(v) for v in step["free_edge"]))),
                ("face",int(step["removed_face"]))}
    return {("vertex",tuple(step["free_vertex"])),
            ("edge",tuple(sorted(tuple(v) for v in step["removed_edge"])))}

def pair_set(steps):
    return frozenset(pair_token(x) for x in steps)

def independent_reordering(a,b):
    if pair_set(a)!=pair_set(b): return False,0
    pos={pair_token(x):i for i,x in enumerate(b)}
    inversions=0
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            x,y=a[i],a[j]
            if pos[pair_token(x)]>pos[pair_token(y)]:
                inversions+=1
                if cell_tokens(x)&cell_tokens(y):
                    return False,inversions
    return True,inversions

def cell_digest(c):
    return digest({
        "faces":sorted(c[0]),
        "edges":[[list(a),list(b)] for a,b in sorted(c[1])],
        "vertices":[list(v) for v in sorted(c[2])]
    })

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--inventory",type=Path,required=True)
    ap.add_argument("--diagrams",type=Path,required=True)
    ap.add_argument("--parent-coherence",type=Path,required=True)
    ap.add_argument("--output",type=Path,required=True)
    a=ap.parse_args()
    inv=json.loads(a.inventory.read_text())
    data=json.loads(a.diagrams.read_text())
    parent_coherence=json.loads(a.parent_coherence.read_text())
    parent_lookup={}
    for family,summary in parent_coherence["families"].items():
        for row in summary["witness_results"]:
            parent_lookup[(family,row["pair_index"],row["witness_index"])]=row["parent_coherent_under_both_root_preserving_maps"]
    face_vertices_table=[face_vertices(x) for x in inv["face_key_table"]]
    face_edges_table=[edge_vertices(x) for x in face_vertices_table]
    sources=hall.source_records(8)
    assert len(sources)==608
    families={"graph5":G5,"graph12":G12}
    family_sources={name:[r for r in sources if edges(r["full_overlap_edges"])==G]
                    for name,G in families.items()}
    summaries={}; case_lookup={}; all_rows=[]
    for family,G in families.items():
        src=family_sources[family]
        mark_pairs=sorted({tuple(sorted((m,n))) for r in src
                           for m,n in itertools.combinations(r["eligible_reverse_marks"],2)})
        source_indices_by_pair=defaultdict(list)
        for si,r in enumerate(src):
            for m,n in itertools.combinations(r["eligible_reverse_marks"],2):
                source_indices_by_pair[tuple(sorted((m,n)))].append(si)
        key=family+"_witnesses"
        candidates=[(pi,pair,wi,w) for pi,pair in enumerate(data["per_pair"])
                    for wi,w in enumerate(pair[key])]
        same_pairset_tests=0; total_tests=0; witness_all_pairset=0
        witness_rows=[]
        for pi,pair,wi,w in candidates:
            supports=[set(s) for s in w["support_face_indices"]]
            full=cells(supports,face_vertices_table,face_edges_table)
            diagram=w["diagram"]
            # Export all four deterministic single-deletion certificates,
            # including the root deletion when it is source-ineligible.
            single_deletion_certificates={}
            for i in range(4):
                target=cells([supports[j] for j in range(4) if j!=i],
                             face_vertices_table,face_edges_table)
                cert=collapse_certificate(full,target,face_vertices_table,face_edges_table)
                if cert["success"]!=bool(diagram["relative_deletion_collapses"][str(i)]):
                    raise AssertionError(("relative-collapse verifier disagreement",family,pi,wi,i))
                single_deletion_certificates[str(i)]=cert
            perm_results=[]
            for perm in isos(G):
                diamonds=[]
                for m,n in mark_pairs:
                    gm,gn=perm[m],perm[n]
                    parent_m=cells([supports[i] for i in range(4) if i!=gm],
                                   face_vertices_table,face_edges_table)
                    parent_n=cells([supports[i] for i in range(4) if i!=gn],
                                   face_vertices_table,face_edges_table)
                    grand=cells([supports[i] for i in range(4) if i not in (gm,gn)],
                                face_vertices_table,face_edges_table)
                    c_m=single_deletion_certificates[str(gm)]
                    c_n_after_m=collapse_certificate(parent_m,grand,face_vertices_table,face_edges_table)
                    c_n=single_deletion_certificates[str(gn)]
                    c_m_after_n=collapse_certificate(parent_n,grand,face_vertices_table,face_edges_table)
                    certs=[c_m,c_n_after_m,c_n,c_m_after_n]
                    if not all(x["success"] and not any(x["remainder"].values()) for x in certs):
                        raise AssertionError(("two-path relative collapse failed",family,pi,wi,perm,m,n))
                    path_mn=c_m["ordered_steps"]+c_n_after_m["ordered_steps"]
                    path_nm=c_n["ordered_steps"]+c_m_after_n["ordered_steps"]
                    same=pair_set(path_mn)==pair_set(path_nm)
                    commutes,inversions=independent_reordering(path_mn,path_nm) if same else (False,0)
                    if same and not commutes:
                        raise AssertionError(("same collapse pairs are not related by disjoint swaps",family,pi,wi,perm,m,n))
                    same_pairset_tests+=int(same); total_tests+=1
                    target_hash=cell_digest(grand)
                    row={
                        "source_mark_pair":[m,n],"mapped_geometric_supports":[gm,gn],
                        "source_record_indices":source_indices_by_pair[(m,n)],
                        "path_delete_m_then_n":{
                            "first_relative_collapse":c_m,
                            "second_relative_collapse":c_n_after_m,
                            "ordered_pair_set_sha256":digest(sorted(map(str,pair_set(path_mn)))),
                            "ordered_sequence_sha256":digest(path_mn),
                            "final_target_cell_digest":target_hash
                        },
                        "path_delete_n_then_m":{
                            "first_relative_collapse":c_n,
                            "second_relative_collapse":c_m_after_n,
                            "ordered_pair_set_sha256":digest(sorted(map(str,pair_set(path_nm)))),
                            "ordered_sequence_sha256":digest(path_nm),
                            "final_target_cell_digest":target_hash
                        },
                        "same_elementary_pair_set":same,
                        "same_target_union":True,
                        "paths_related_by_commuting_disjoint_elementary_pairs":commutes,
                        "disjoint_swap_inversion_count":inversions
                    }
                    diamonds.append(row)
                all_pairset=all(x["same_elementary_pair_set"] for x in diamonds)
                perm_results.append({"source_to_support_isomorphism":list(perm),
                                     "all_critical_pairs_same_elementary_pair_set":all_pairset,
                                     "diamond_certificates":diamonds})
            verdicts=[x["all_critical_pairs_same_elementary_pair_set"] for x in perm_results]
            if len(set(verdicts))!=1:
                raise AssertionError(("collapse-pair coherence depends on graph automorphism",family,pi,wi))
            # Count witnesses once, after verifying both root-preserving maps.
            witness_all_pairset+=int(verdicts[0])
            wid=digest({"family":family,"pair":pi,"witness":wi,
                        "fourth_edge":w["fourth_edge"],
                        "supports":w["support_face_indices"]})[:20]
            witness_rows.append({"pair_index":pi,"witness_index":wi,"witness_id":wid,
                                 "second_edge":pair["second_edge"],"third_edge":pair["third_edge"],
                                 "fourth_edge":w["fourth_edge"],
                                 "single_deletion_certificates":single_deletion_certificates,
                                 "all_critical_pairs_same_elementary_pair_set":verdicts[0],
                                 "permutation_results":perm_results})
        summaries[family]={
            "source_count":len(src),"retained_witness_count":len(candidates),
            "unique_source_critical_mark_pairs": [list(x) for x in mark_pairs],
            "source_critical_diamond_count":sum(len(list(itertools.combinations(r["eligible_reverse_marks"],2))) for r in src),
            "diamond_path_tests":total_tests,
            "same_elementary_pair_set_tests":same_pairset_tests,
            "different_elementary_pair_set_tests":total_tests-same_pairset_tests,
            "witnesses_with_all_critical_pairs_same_pair_set":witness_all_pairset,
            "witnesses_with_any_different_pair_set":len(candidates)-witness_all_pairset,
            "witness_results":witness_rows
        }
        case_lookup[family]={
            (row["pair_index"],row["witness_index"]):{
                "collapse_pair_coherent":row["all_critical_pairs_same_elementary_pair_set"],
                "parent_diagram_coherent":parent_lookup[(family,row["pair_index"],row["witness_index"])]
            } for row in witness_rows
        }
    common_cases=[]; common_count=0; joint_count=0; collapse_only_count=0; parent_only_count=0
    for pi,pair in enumerate(data["per_pair"]):
        for e4 in pair["common_fourth_edges_with_independent_full_parent4_lifts"]:
            common_count+=1
            ek=(tuple(e4["lower"]),tuple(e4["upper"]))
            g5_all=[wi for wi,w in enumerate(pair["graph5_witnesses"])
                    if (tuple(w["fourth_edge"]["lower"]),tuple(w["fourth_edge"]["upper"]))==ek]
            g12_all=[wi for wi,w in enumerate(pair["graph12_witnesses"])
                     if (tuple(w["fourth_edge"]["lower"]),tuple(w["fourth_edge"]["upper"]))==ek]
            g5_collapse=[wi for wi in g5_all if case_lookup["graph5"][(pi,wi)]["collapse_pair_coherent"]]
            g12_collapse=[wi for wi in g12_all if case_lookup["graph12"][(pi,wi)]["collapse_pair_coherent"]]
            g5_parent=[wi for wi in g5_all if case_lookup["graph5"][(pi,wi)]["parent_diagram_coherent"]]
            g12_parent=[wi for wi in g12_all if case_lookup["graph12"][(pi,wi)]["parent_diagram_coherent"]]
            g5_joint=[wi for wi in g5_all if all(case_lookup["graph5"][(pi,wi)].values())]
            g12_joint=[wi for wi in g12_all if all(case_lookup["graph12"][(pi,wi)].values())]
            collapse_ok=bool(g5_collapse and g12_collapse)
            parent_ok=bool(g5_parent and g12_parent)
            joint_ok=bool(g5_joint and g12_joint)
            collapse_only_count+=int(collapse_ok)
            parent_only_count+=int(parent_ok)
            joint_count+=int(joint_ok)
            common_cases.append({"pair_index":pi,"second_edge":pair["second_edge"],
                "third_edge":pair["third_edge"],"fourth_edge":e4,
                "graph5_collapse_coherent_witness_indices":g5_collapse,
                "graph12_collapse_coherent_witness_indices":g12_collapse,
                "graph5_parent_coherent_witness_indices":g5_parent,
                "graph12_parent_coherent_witness_indices":g12_parent,
                "graph5_joint_coherent_witness_indices":g5_joint,
                "graph12_joint_coherent_witness_indices":g12_joint,
                "both_families_collapse_pair_coherent":collapse_ok,
                "both_families_parent_diagram_coherent":parent_ok,
                "both_families_joint_coherent":joint_ok})
    assert common_count==64 and collapse_only_count==28 and parent_only_count==50 and joint_count==18
    joint_rows=[x for x in common_cases if x["both_families_joint_coherent"]]
    joint_fourth_edges=Counter((tuple(x["fourth_edge"]["lower"]),tuple(x["fourth_edge"]["upper"])) for x in joint_rows)
    assert len(joint_fourth_edges)==1
    joint_edge,joint_edge_frequency=next(iter(joint_fourth_edges.items()))
    assert joint_edge_frequency==18
    joint_second_third_frequency=Counter()
    for row in joint_rows:
        joint_second_third_frequency[edge_key(row["second_edge"])]+=1
        joint_second_third_frequency[edge_key(row["third_edge"])]+=1
    assert len({x["pair_index"] for x in joint_rows})==18
    assert summaries["graph5"]["witnesses_with_all_critical_pairs_same_pair_set"]==312
    assert summaries["graph12"]["witnesses_with_all_critical_pairs_same_pair_set"]==102
    result={
        "schema":"PF-I16-FOUR-SUPPORT-RELATIVE-COLLAPSE-DIAMONDS-v1",
        "scope":"Ngrid=12 finite graph-5/graph-12 four-support witnesses; all source critical deletion-mark pairs; deterministic elementary relative-collapse certificates",
        "inventory_target":inv["target"],
        "diagram_artifact_sha256":hashlib.sha256(a.diagrams.read_bytes()).hexdigest(),
        "parent_coherence_artifact_sha256":hashlib.sha256(a.parent_coherence.read_bytes()).hexdigest(),
        "families":summaries,
        "common_fourth_edge_case_count":common_count,
        "common_cases_with_both_families_collapse_pair_coherent":collapse_only_count,
        "common_cases_with_both_families_parent_diagram_coherent":parent_only_count,
        "common_cases_with_both_families_joint_coherent":joint_count,
        "common_cases_not_passing_joint_coherence":common_count-joint_count,
        "joint_coherent_distinct_second_third_pairs":len({x["pair_index"] for x in joint_rows}),
        "joint_coherent_fourth_edge":{"lower":list(joint_edge[0]),"upper":list(joint_edge[1])},
        "joint_coherent_fourth_edge_frequency":joint_edge_frequency,
        "joint_coherent_variable_second_third_edge_frequency":[
            {"edge":{"lower":list(e[0]),"upper":list(e[1])},"count":n}
            for e,n in sorted(joint_second_third_frequency.items())
        ],
        "common_case_results":common_cases,
        "conclusions":{
            "all_3984_single_deletion_certificates_match_original_booleans":True,
            "all_source_critical_two_path_collapse_certificates_succeed":True,
            "both_paths_reach_the_same_grandparent_union":True,
            "same_pair_set_paths_commute_by_disjoint_swaps":True,
            "graph5_all_pair_set_coherent_witnesses":312,
            "graph12_all_pair_set_coherent_witnesses":102,
            "both_families_have_strict_pair_set_coherent_witness_in_28_of_64_common_cases":True,
            "both_families_pass_parent_and_collapse_coherence_in_18_of_64_common_cases":True,
            "all_18_joint_cases_share_one_fourth_matched_edge":True,
            "different_pair_set_cases_are_not_no_go_results":True,
            "geometric_L8_closed":False
        },
        "nonclaims":[
            "A passing pair-set diamond means the two complete paths use the same elementary free-pair matching and differ only by swaps of disjoint elementary collapses. It does not establish equality of the induced deformation-retraction maps beyond those commuting swaps.",
            "A different-pair-set result means the two deterministic collapse algorithms found different valid free-pair matchings to the same target union. It is not a proof that no common matching or alternate collapse certificate exists.",
            "The 28/64 common-case count pairs independent graph-5 and graph-12 support witnesses sharing the matched-edge quadruple; it does not imply identical first-three support face sets.",
            "No all-orders collapse confluence, geometric L8, Hall theorem, or physical mass-gap result follows."
        ]
    }
    a.output.parent.mkdir(parents=True,exist_ok=True)
    with gzip.open(a.output,"wt",encoding="utf-8",compresslevel=9) as f:
        json.dump(result,f,sort_keys=True,separators=(",",":"))
    print(json.dumps({"schema":result["schema"],
        "graph5":{k:v for k,v in summaries["graph5"].items() if k not in ("witness_results",)},
        "graph12":{k:v for k,v in summaries["graph12"].items() if k not in ("witness_results",)},
        "common_cases":common_count,"collapse_only_coherent_cases":collapse_only_count,
        "parent_only_coherent_cases":parent_only_count,"joint_coherent_cases":joint_count,
        "joint_fourth_edge":{"lower":list(joint_edge[0]),"upper":list(joint_edge[1])},
        "joint_second_third_edge_count":len(joint_second_third_frequency)},sort_keys=True,indent=2))

if __name__=="__main__":
    main()
