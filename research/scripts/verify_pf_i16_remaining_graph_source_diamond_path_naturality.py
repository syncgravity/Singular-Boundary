#!/usr/bin/env python3
"""Replay both orders of source-eligible deletion diamonds in the remaining order-eight graph families.

Inputs are the pinned accepted-face inventory, parent-compatibility graph
catalogue, and full graph-1/2/3 candidate-diagram audit. For every candidate,
every source record, every root-preserving source-to-support map, and every
pair of eligible source marks, this verifier checks source endpoint compression,
the retained-support intersection/footprint, both two-step relative-collapse
paths, and the same-pair or alternating-cycle/dependency-closed comparison.
"""
from __future__ import annotations
import argparse, hashlib, itertools, json
from collections import Counter, defaultdict
from pathlib import Path

import export_pf_i16_hall_source_records as hall
import verify_pf_i16_hall_four_interval_parent_compatibility as geom
import verify_pf_i16_order8_oriented_collapse_diamond_naturality as order8

def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--inventory",type=Path,required=True)
    ap.add_argument("--parent-compatibility",type=Path,required=True)
    ap.add_argument("--candidate-diagrams",type=Path,required=True)
    ap.add_argument("--output",type=Path,required=True)
    a=ap.parse_args()

    inv=json.loads(a.inventory.read_text())
    compat=json.loads(a.parent_compatibility.read_text())
    candidates=json.loads(a.candidate_diagrams.read_text())
    assert candidates["schema"]=="PF-I16-REMAINING-GRAPH-FULL-DIAGRAM-CANDIDATE-AUDIT-v1"
    assert candidates["total_full_diagram_passes"]==333
    assert compat["schema"]=="PF-I16-HALL-FOUR-INTERVAL-PARENT-COMPATIBILITY-v1"

    face_vertices,face_edges,_,_=geom.build_target(inv)
    cells,_,intersection,_,point_contractible,_,_=geom.make_geometry(face_vertices,face_edges)
    order8.FACE_EDGES=face_edges
    fixed=[(tuple(x["lower"]),tuple(x["upper"])) for x in inv["fixed_triple_edges"]]
    assert len(fixed)==3
    graphs={x["graph_index"]:frozenset(tuple(sorted(e)) for e in x["edges"])
            for x in compat["four_interval_graphs"]}
    source_rows=hall.source_records(8)
    source_by_index={i:sr for i,sr in enumerate(source_rows)}
    source_graphs={i:frozenset(tuple(sorted(e)) for e in sr["full_overlap_edges"])
                   for i,sr in source_by_index.items()}

    pair_counts=Counter()
    same_pair_counts=Counter()
    cycle_counts=Counter()
    block_counts=Counter()
    extra_counts=Counter()
    prefix_swaps=Counter()
    extra_order=Counter()
    map_rows=Counter()
    source_diamond_keys=set()
    path_rows=[]
    all_checks=Counter()

    for cand in candidates["candidates"]:
        if not cand["full_diagram_pass"]:
            continue
        gi=cand["graph_index"]
        graph=graphs[gi]
        supports=[order8.complex_dict(cells(tuple(sorted(s))))
                  for s in cand["support_face_indices"]]
        edges=fixed+[ (tuple(cand["fourth_edge"]["lower"]),
                       tuple(cand["fourth_edge"]["upper"])) ]
        assert len(supports)==len(edges)==4
        cycles=[]
        for i in range(4):
            cyc=order8.boundary_cycle(supports[i],edges[i],face_edges)
            assert cyc is not None
            cycles.append(cyc)
        words=[order8.derive_footprint_word(i,supports,cycles) for i in range(4)]
        full=order8.union_complex(supports,range(4))

        for mr in cand["source_map_eligible_deletion_checks"]:
            si=mr["source_index"]
            sr=source_by_index[si]
            perm=tuple(mr["source_to_support_map"])
            assert source_graphs[si]==graph
            assert source_graphs[si] in graphs.values()
            assert len(perm)==4 and perm[0]==0
            eligible=tuple(sorted(int(x) for x in sr["eligible_reverse_marks"]))
            assert list(eligible)==mr["eligible_source_marks"]
            assert all(mr["eligible_deletion_checks"][str(perm[m])]
                       for m in eligible)
            map_rows[gi]+=1
            intervals=tuple(tuple(x) for x in sr["intervals"])
            tree=tuple(tuple(x) for x in sr["tree_edges"])
            for m,n in itertools.combinations(eligible,2):
                sm,sn=perm[m],perm[n]
                assert sm!=sn and sm!=0 and sn!=0
                remaining=tuple(sorted(set(range(4))-{sm,sn}))
                assert len(remaining)==2

                # Source-side endpoint compression in both orders.
                im,tm,cm=order8.delete_source(intervals,tree,m,8)
                n1=n-1 if n>m else n
                imn,tmn,cnm=order8.delete_source(im,tm,n1,6)
                inn,tn,cn=order8.delete_source(intervals,tree,n,8)
                m1=m-1 if m>n else m
                inm,tnm,cnm2=order8.delete_source(inn,tn,m1,6)
                cmn={p:cnm[cm[p]] for p in cm if cm[p] in cnm}
                cnm_final={p:cnm2[cn[p]] for p in cn if cn[p] in cnm2}
                assert (imn,tmn,cmn)==(inm,tnm,cnm_final)
                source_diamond_keys.add((gi,si,tuple(sorted((m,n)))))
                all_checks["source_endpoint_compression_diamonds"]+=1

                # The retained pair must be the same contractible intersection
                # footprint seen from both oriented support boundaries.
                common=order8.intersection_complex(supports,remaining)
                assert common["V"] and point_contractible(
                    tuple(common[k] for k in ("F","E","V")))
                wa=[x for x in words[remaining[0]] if x["neighbor"]==remaining[1]]
                wb=[x for x in words[remaining[1]] if x["neighbor"]==remaining[0]]
                assert len(wa)==len(wb)==1
                assert wa[0]["cell_type"]==wb[0]["cell_type"]
                assert {tuple(v) for v in wa[0]["cell_vertices"]}=={
                    tuple(v) for v in wb[0]["cell_vertices"]}
                all_checks["retained_pair_common_footprints"]+=1

                # Construct the two orders U4 -> U3 -> U2.
                mid_m=order8.union_complex(supports,[i for i in range(4) if i!=sm])
                mid_n=order8.union_complex(supports,[i for i in range(4) if i!=sn])
                target=order8.union_complex(supports,remaining)
                a1=order8.collapse_sequence(full,mid_m,face_edges,face_vertices)
                a2=order8.collapse_sequence(mid_m,target,face_edges,face_vertices)
                b1=order8.collapse_sequence(full,mid_n,face_edges,face_vertices)
                b2=order8.collapse_sequence(mid_n,target,face_edges,face_vertices)
                assert all(x is not None for x in (a1,a2,b1,b2)),(gi,cand["candidate_index"],si,m,n)
                L=a1+a2
                R=b1+b2
                assert order8.replay(L,full,target,face_edges,face_vertices)==target
                assert order8.replay(R,full,target,face_edges,face_vertices)==target
                all_checks["two_order_paths_replay"]+=1

                same=set(L)==set(R)
                pair_counts[(gi,"same" if same else "different")]+=1
                cycle_size=None
                swaps=None
                blockL=blockR=None
                prefix_norm=None
                extra_wordL=extra_wordR=()
                if same:
                    swaps=order8.normalize(L,R,full,target,face_edges,face_vertices)
                    assert swaps is not None
                    same_pair_counts[(gi,swaps)]+=1
                else:
                    ok,cycle_size=order8.alternating_cycle(L,R)
                    assert ok,(gi,cand["candidate_index"],si,m,n)
                    cycle_counts[(gi,cycle_size)]+=1
                    dL=set(L)-set(R)
                    dR=set(R)-set(L)
                    blockL,_,prefixL,suffixL=order8.dependency_close(
                        L,full,target,dL,face_edges,face_vertices)
                    blockR,_,prefixR,suffixR=order8.dependency_close(
                        R,full,target,dR,face_edges,face_vertices)
                    midL=order8.replay(prefixL,full,target,face_edges,face_vertices)
                    midR=order8.replay(prefixR,full,target,face_edges,face_vertices)
                    assert set(prefixL)==set(prefixR) and midL==midR
                    assert (blockL-dL)==(blockR-dR)
                    assert order8.replay(suffixL,midL,target,face_edges,face_vertices)==target
                    assert order8.replay(suffixR,midR,target,face_edges,face_vertices)==target
                    prefix_norm=order8.normalize(prefixL,prefixR,full,midL,face_edges,face_vertices)
                    assert prefix_norm is not None
                    extraL=blockL-dL
                    extraR=blockR-dR
                    extra_wordL=tuple(p[0] for p in suffixL if p in extraL)
                    extra_wordR=tuple(p[0] for p in suffixR if p in extraR)
                    block_counts[(gi,len(blockL))]+=1
                    extra_counts[(gi,len(extraL))]+=1
                    prefix_swaps[(gi,prefix_norm)]+=1
                    extra_order[(gi,len(blockL),extra_wordL,extra_wordR,
                                 extra_wordL==extra_wordR)]+=1
                path_rows.append({
                    "graph_index":gi,"candidate_index":cand["candidate_index"],
                    "source_index":si,"source_to_support_map":list(perm),
                    "source_marks":[m,n],"support_marks":[sm,sn],
                    "retained_supports":list(remaining),
                    "left_path_length":len(L),"right_path_length":len(R),
                    "left_path_sha256":order8.digest([order8.encode_pair(p) for p in L]),
                    "right_path_sha256":order8.digest([order8.encode_pair(p) for p in R]),
                    "same_elementary_pair_set":same,
                    "same_pair_set_normalizing_swaps":swaps,
                    "alternating_cycle_cell_count":cycle_size,
                    "dependency_closed_suffix_pairs":len(blockL) if blockL is not None else None,
                    "common_extra_pair_count":len(blockL-(set(L)-set(R))) if blockL is not None else None,
                    "common_prefix_pair_set":bool(blockL is not None),
                    "prefix_normalizing_valid_swaps":prefix_norm,
                    "left_common_extra_pair_word":list(extra_wordL),
                    "right_common_extra_pair_word":list(extra_wordR),
                    "common_extra_pair_order_equal":(extra_wordL==extra_wordR) if blockL is not None else None
                })

    total=sum(v for (_,kind),v in pair_counts.items())
    expected={4:0,6:1080,7:520,8:840,9:228,10:960,11:96,13:31104}
    by_graph={str(gi):sum(v for (g,_),v in pair_counts.items() if g==gi) for gi in expected}
    assert by_graph=={str(k):v for k,v in expected.items()},by_graph
    assert total==4084
    assert all_checks["source_endpoint_compression_diamonds"]==total
    assert all_checks["retained_pair_common_footprints"]==total
    assert all_checks["two_order_paths_replay"]==total

    summary={
        "schema":"PF-I16-REMAINING-GRAPH-SOURCE-DIAMOND-PATH-NATURALITY-v1",
        "inputs":{"inventory_sha256":sha(a.inventory),
                  "parent_compatibility_sha256":sha(a.parent_compatibility),
                  "candidate_diagrams_sha256":sha(a.candidate_diagrams)},
        "candidate_diagrams_checked":sum(1 for x in candidates["candidates"] if x["full_diagram_pass"]),
        "candidate_diagrams_rejected":sum(1 for x in candidates["candidates"] if not x["full_diagram_pass"]),
        "source_map_rows_by_graph":{str(k):map_rows[k] for k in (1,2,3)},
        "source_diamond_path_instances_by_graph":by_graph,
        "total_source_diamond_path_instances":total,
        "checks":dict(all_checks),
        "pair_set_comparison":{
            "same_pair_set":sum(v for (_,v),n in [] ) if False else sum(v for (g,k),v in pair_counts.items() if k=="same"),
            "different_pair_sets":sum(v for (g,k),v in pair_counts.items() if k=="different"),
            "same_pair_set_valid_adjacent_swap_normalizations":sum(same_pair_counts.values()),
            "alternating_cycle_sizes":[{"graph":g,"cells":k,"rows":v}
                                       for (g,k),v in sorted(cycle_counts.items())],
            "dependency_closed_suffix_sizes":[{"graph":g,"pairs":k,"rows":v}
                                              for (g,k),v in sorted(block_counts.items())],
            "common_extra_pair_counts":[{"graph":g,"pairs":k,"rows":v}
                                        for (g,k),v in sorted(extra_counts.items())],
            "prefix_normalizing_swap_counts":[{"graph":g,"swaps":k,"rows":v}
                                              for (g,k),v in sorted(prefix_swaps.items())],
            "order_sensitive_rows":sum(v for (g,k,l,r,eq),v in extra_order.items() if not eq),
            "order_aligned_rows":sum(v for (g,k,l,r,eq),v in extra_order.items() if eq),
            "common_extra_pair_order_templates":[
                {"graph":g,"suffix_pairs":k,"left_word":list(l),"right_word":list(r),
                 "order_equal":eq,"rows":v}
                for (g,k,l,r,eq),v in sorted(extra_order.items())
            ]
        },
        "source_diamond_keys":[{"graph":g,"source_index":si,"marks":list(mn)}
                               for g,si,mn in sorted(source_diamond_keys)],
        "path_certificates":path_rows,
        "nonclaims":[
            "finite passing candidate diagrams in graph families 4, 6, 7, 8, 9, 10, 11, and 13 only",
            "path-level naturality is not an all-orders local switch theorem",
            "58 rejected candidate diagrams are excluded because their full union is not point-contractible and source-eligible relative deletion fails",
            "does not prove geometric L8, split-demand Hall, or the all-orders weighted one-link inequality"
        ]
    }
    a.output.write_text(json.dumps(summary,sort_keys=True,indent=2)+"\n")
    print(json.dumps({k:v for k,v in summary.items()
                      if k not in ("path_certificates","source_diamond_keys","common_extra_pair_order_templates")},sort_keys=True,indent=2))

if __name__=="__main__":
    main()
