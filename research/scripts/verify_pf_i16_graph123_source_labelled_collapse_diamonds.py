#!/usr/bin/env python3
"""Source-labelled parent naturality and collapse-diamond audit for graph 1-3.

Consumes the 284 selected full-diagram candidate witnesses. For every source
record and every root-preserving graph map, verifies the port embedding,
eligible parent-port restriction, source parent-tree diamond, and both
elementary relative-collapse paths. Differing collapse-pair sets are factored
by the existing dependency-closed local-switch verifier.
"""
from __future__ import annotations
import argparse, hashlib, itertools, json
from collections import Counter, defaultdict
from pathlib import Path

import export_pf_i16_hall_source_records as hall
import verify_pf_i16_hall_four_interval_parent_compatibility as geom
import verify_pf_i16_order8_oriented_collapse_diamond_naturality as order8

def edge_set(es):
    return frozenset(tuple(sorted(e)) for e in es)

def isos(G):
    return [p for p in itertools.permutations(range(4))
            if p[0]==0 and edge_set((p[i],p[j]) for i,j in G)==G]

def source_graph(sr):
    return edge_set(sr["full_overlap_edges"])

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--inventory",type=Path,required=True)
    ap.add_argument("--diagram-audit",type=Path,required=True)
    ap.add_argument("--output",type=Path,required=True)
    a=ap.parse_args()
    inv=json.loads(a.inventory.read_text())
    data=json.loads(a.diagram_audit.read_text())
    assert data["schema"]=="PF-I16-GRAPH123-FULL-DIAGRAM-CANDIDATE-AUDIT-v1"
    fv,fe,options,_=geom.build_target(inv)
    cells,union,intersection,collapse,point_contractible,edge_contractible,footprint=geom.make_geometry(fv,fe)
    order8.FACE_EDGES=fe
    face_vertex_table=fv
    fixed=[{"lower":x["lower"],"upper":x["upper"]} for x in inv["fixed_triple_edges"]]
    source_rows=hall.source_records(8)
    graph_by_index={x["graph_index"]:edge_set(x["edges"]) for x in
                    [{"graph_index":g,"edges":data_graph} for g,data_graph in []]}
    # Candidate graph identity is source-labelled, not inferred from row order.
    graph_defs={
        1:edge_set(((0,1),(0,2),(0,3))),
        2:edge_set(((0,1),(0,2),(2,3))),
        3:edge_set(((0,1),(1,2),(1,3))),
    }
    src_by_graph=defaultdict(list)
    for si,sr in enumerate(source_rows):
        g=source_graph(sr)
        for gi,G in graph_defs.items():
            if g==G: src_by_graph[gi].append((si,sr))
    maps_by_graph={gi:isos(G) for gi,G in graph_defs.items()}
    candidate_rows=data["candidates"]
    assert len(candidate_rows)==284

    geom_summary=Counter()
    source_map_rows=[]
    diamond_rows=[]
    path_pair_counts=Counter()
    alternating_cycle_counts=Counter()
    same_pair_normalization=Counter()
    dependency_prefix_counts=Counter()
    suffix_size_counts=Counter()
    source_diamond_counts=Counter()
    parent_restriction_counts=Counter()
    first_examples={}

    for ci,cand in enumerate(candidate_rows):
        gi=cand["graph_index"]
        G=graph_defs[gi]
        supports=[frozenset(x) for x in cand["support_face_indices"]]
        complexes=[order8.complex_dict(cells(tuple(sorted(s)))) for s in supports]
        target_edges=fixed+[
            {"lower":cand["fourth_edge"]["lower"],"upper":cand["fourth_edge"]["upper"]}
        ]
        imap={tuple(x["indices"]):x for x in cand["intersections"]}
        words={x["support"]:x["footprint_words"] for x in cand["footprint_words"]}
        rel=cand["checks"]["all_four_relative_deletion_collapses"]
        full=order8.union_complex(complexes,range(4))
        wid=f"g{gi}-candidate{cand['candidate_index']}"

        for si,sr in src_by_graph[gi]:
            marks=sorted(int(x["deleted_interval_index"]) for x in sr["parents"])
            for perm in maps_by_graph[gi]:
                port_to_z5={}
                interval_edge_map=[]
                for i,(p,q) in enumerate(sr["intervals"]):
                    support_index=perm[i]
                    edge=target_edges[support_index]
                    lo=tuple(edge["lower"]); hi=tuple(edge["upper"])
                    assert p<q
                    port_to_z5[str(p)]=list(lo); port_to_z5[str(q)]=list(hi)
                    face_ids=supports[support_index]
                    incident=[fid for fid in face_ids if lo in face_vertex_table[fid] and hi in face_vertex_table[fid]]
                    assert len(incident)==1,(gi,ci,si,perm,i,incident)
                    delta=[hi[t]-lo[t] for t in range(5)]
                    assert sum(abs(x) for x in delta)==1 and sum(x==1 for x in delta)==1 and all(x>=0 for x in delta)
                    interval_edge_map.append({
                        "source_interval_index":i,"source_interval":list(sr["intervals"][i]),
                        "support_index":support_index,"matched_edge":{"lower":list(lo),"upper":list(hi)},
                        "positive_unit_direction":next(t for t,x in enumerate(delta) if x==1),
                        "accepted_face":incident[0]
                    })
                assert set(map(int,port_to_z5))==set(range(1,9))
                assert len({tuple(v) for v in port_to_z5.values()})==8
                for i,j in itertools.combinations(range(4),2):
                    assert ((i,j) in G)==bool(imap[tuple(sorted((perm[i],perm[j]))) ]["nonempty"])
                legal={str(m):bool(rel[str(perm[m])]) for m in marks}
                assert all(legal.values()),(gi,ci,si,perm,legal)

                parent_maps=[]
                for parent in sr["parents"]:
                    m=int(parent["deleted_interval_index"])
                    retained=[j for j in range(4) if j!=m]
                    compression={int(k):v for k,v in parent["port_order_compression"].items()}
                    restricted={str(compression[p]):port_to_z5[str(p)]
                                for p in parent["retained_ports_before_compression"]}
                    parent_map={}
                    for parent_i,(p,q) in enumerate(parent["parent_intervals"]):
                        edge=target_edges[perm[retained[parent_i]]]
                        parent_map[str(p)]=edge["lower"]
                        parent_map[str(q)]=edge["upper"]
                    assert restricted==parent_map,(gi,ci,si,perm,m)
                    parent_restriction_counts[gi]+=1
                    tree_geom=[tuple(sorted((perm[retained[x]],perm[retained[y]])))
                               for x,y in parent["parent_tree_edges"]]
                    tree_checks=[]
                    for x,y in tree_geom:
                        entry=imap[(x,y)]
                        assert entry["nonempty"] and entry["point_contractible"]
                        wx=[z for z in words[x] if z["neighbor"]==y]
                        wy=[z for z in words[y] if z["neighbor"]==x]
                        assert len(wx)==len(wy)==1
                        assert wx[0]["cell_type"]==wy[0]["cell_type"]
                        assert {tuple(v) for v in wx[0]["cell_vertices"]}=={tuple(v) for v in wy[0]["cell_vertices"]}
                        tree_checks.append({"edge":[x,y],"reciprocal_footprint":True})
                    parent_maps.append({"deleted_mark":m,"mapped_support":perm[m],
                        "parent_port_map":parent_map,"port_restriction_commutes":True,
                        "mapped_parent_tree_edges":[list(x) for x in tree_geom],
                        "tree_edge_checks":tree_checks})

                source_diamonds=[]
                for m,n in itertools.combinations(marks,2):
                    source_diamond_counts[gi]+=1
                    pm=next(x for x in sr["parents"] if int(x["deleted_interval_index"])==m)
                    pn=next(x for x in sr["parents"] if int(x["deleted_interval_index"])==n)
                    rm=[j for j in range(4) if j!=m]
                    rn=[j for j in range(4) if j!=n]
                    def second(parent,deleted):
                        keep=[j for j in range(3) if j!=deleted]
                        ren={old:new for new,old in enumerate(keep)}
                        return sorted(tuple(sorted((ren[x],ren[y])))
                            for x,y in parent["parent_tree_edges"] if x!=deleted and y!=deleted)
                    tmn=second(pm,rm.index(n)); tnm=second(pn,rn.index(m))
                    assert tmn==tnm and len(tmn)==1,(gi,si,m,n,tmn,tnm)
                    remaining=[j for j in range(4) if j not in (m,n)]
                    pairkey=tuple(sorted((perm[remaining[0]],perm[remaining[1]])))
                    entry=imap[pairkey]
                    assert entry["nonempty"] and entry["point_contractible"]
                    assert legal[str(m)] and legal[str(n)]

                    target_m=order8.union_complex(complexes,[j for j in range(4) if j!=perm[m]])
                    target_n=order8.union_complex(complexes,[j for j in range(4) if j!=perm[n]])
                    target_mn=order8.union_complex(complexes,[j for j in range(4) if j not in (perm[m],perm[n])])
                    seq_m=order8.collapse_sequence(full,target_m,fe,fv)
                    seq_n=order8.collapse_sequence(full,target_n,fe,fv)
                    seq_n_after_m=order8.collapse_sequence(target_m,target_mn,fe,fv)
                    seq_m_after_n=order8.collapse_sequence(target_n,target_mn,fe,fv)
                    if any(x is None for x in (seq_m,seq_n,seq_n_after_m,seq_m_after_n)):
                        raise AssertionError(("elementary collapse sequence missing",gi,ci,si,perm,m,n))
                    left=seq_m+seq_n_after_m
                    right=seq_n+seq_m_after_n
                    assert order8.replay(left,full,target_mn,fe,fv)==target_mn
                    assert order8.replay(right,full,target_mn,fe,fv)==target_mn
                    same=set(left)==set(right)
                    path_pair_counts[(gi,"same" if same else "different")]+=1
                    diamond={"source_marks":[m,n],"mapped_supports":[perm[m],perm[n]],
                             "remaining_support_pair":list(pairkey),
                             "source_parent_tree_diamond_commutes":True,
                             "both_elementary_paths_replay":True,
                             "left_pair_count":len(left),"right_pair_count":len(right),
                             "same_elementary_pair_set":same}
                    if same:
                        swaps=order8.normalize(left,right,full,target_mn,fe,fv)
                        assert swaps is not None,(gi,ci,si,perm,m,n,"same pair set not commutable")
                        same_pair_normalization[(gi,swaps)]+=1
                        diamond["adjacent_commutation_swaps"]=swaps
                    else:
                        is_cycle,cycle_cells=order8.alternating_cycle(left,right)
                        alternating_cycle_counts[(gi,cycle_cells if is_cycle else -cycle_cells)]+=1
                        initial=set(left)^set(right)
                        block_l,sw_l,prefix_l,suffix_l=order8.dependency_close(left,full,target_mn,initial,fe,fv)
                        block_r,sw_r,prefix_r,suffix_r=order8.dependency_close(right,full,target_mn,initial,fe,fv)
                        assert set(prefix_l)==set(prefix_r),(gi,ci,si,perm,m,n,"prefix pair sets differ")
                        mid_l=order8.replay(prefix_l,full,target_mn,fe,fv)
                        mid_r=order8.replay(prefix_r,full,target_mn,fe,fv)
                        assert mid_l==mid_r,(gi,ci,si,perm,m,n,"prefix inventories differ")
                        assert order8.replay(suffix_l,mid_l,target_mn,fe,fv)==target_mn
                        assert order8.replay(suffix_r,mid_r,target_mn,fe,fv)==target_mn
                        extra_l=set(suffix_l)-initial
                        extra_r=set(suffix_r)-initial
                        assert extra_l==extra_r,(gi,ci,si,perm,m,n,"additional suffix pairs differ")
                        prefix_swaps=order8.normalize(prefix_l,prefix_r,full,target_mn,fe,fv)
                        assert prefix_swaps is not None,(gi,ci,si,perm,m,n,"common prefix not commutation-normalizable")
                        dependency_prefix_counts[(gi,len(block_l),len(block_r),prefix_swaps)]+=1
                        suffix_size_counts[(gi,len(suffix_l))]+=1
                        diamond.update({
                            "alternating_cycle_is_single":is_cycle,
                            "alternating_cycle_cell_count":cycle_cells,
                            "left_dependency_block_pairs":len(block_l),
                            "right_dependency_block_pairs":len(block_r),
                            "common_prefix_pair_count":len(prefix_l),
                            "common_prefix_normalization_swaps":prefix_swaps,
                            "same_intermediate_inventory":True,
                            "common_additional_suffix_pairs":len(extra_l),
                            "both_local_suffixes_replay":True
                        })
                        if not is_cycle:
                            diamond["warning"]="difference is not one alternating cycle"
                    source_diamonds.append(diamond)
                    if gi not in first_examples:
                        first_examples[gi]={"candidate_index":ci,"source_index":si,
                            "source_to_support_map":list(perm),"diamond":diamond}
                    diamond_rows.append({"graph_index":gi,"candidate_index":ci,
                        "source_index":si,"source_to_support_map":list(perm),"diamond":diamond})

                source_map_rows.append({
                    "graph_index":gi,"candidate_index":ci,"source_index":si,
                    "source_intervals":[list(x) for x in sr["intervals"]],
                    "source_tree_edges":[list(x) for x in sr["tree_edges"]],
                    "source_to_support_map":list(perm),"source_to_target_port_map":port_to_z5,
                    "source_interval_to_target_edge_map":interval_edge_map,
                    "eligible_reverse_marks":marks,"eligible_deletion_checks":legal,
                    "parent_maps":parent_maps,"source_diamonds":source_diamonds,
                    "all_parent_port_restrictions_commute":True
                })
                geom_summary[(gi,"source_map_rows")]+=1

    result={
        "schema":"PF-I16-GRAPH123-SOURCE-LABELLED-COLLAPSE-DIAMONDS-v1",
        "diagram_artifact_sha256":hashlib.sha256(a.diagram_audit.read_bytes()).hexdigest(),
        "inventory_artifact_sha256":hashlib.sha256(a.inventory.read_bytes()).hexdigest(),
        "candidate_count":len(candidate_rows),
        "source_map_rows":len(source_map_rows),
        "source_diamond_instances":len(diamond_rows),
        "source_map_rows_by_graph":{str(g):sum(1 for r in source_map_rows if r["graph_index"]==g) for g in (1,2,3)},
        "source_diamond_instances_by_graph":{str(g):sum(1 for r in diamond_rows if r["graph_index"]==g) for g in (1,2,3)},
        "parent_port_restriction_checks_by_graph":{str(g):parent_restriction_counts[g] for g in (1,2,3)},
        "collapse_pair_set_counts":[{"graph":g,"same_pair_set":path_pair_counts[(g,"same")],
                                     "different_pair_set":path_pair_counts[(g,"different")]} for g in (1,2,3)],
        "same_pair_normalization_histogram":[{"graph":g,"swaps":s,"rows":v}
                                             for (g,s),v in sorted(same_pair_normalization.items())],
        "alternating_cycle_histogram":[{"graph":g,"cells":sz,"rows":v}
                                        for (g,sz),v in sorted(alternating_cycle_counts.items())],
        "dependency_closed_factorization_histogram":[
            {"graph":g,"left_block_pairs":l,"right_block_pairs":r,"prefix_swaps":sw,"rows":v}
            for (g,l,r,sw),v in sorted(dependency_prefix_counts.items())],
        "dependency_suffix_size_histogram":[{"graph":g,"suffix_pairs":s,"rows":v}
                                             for (g,s),v in sorted(suffix_size_counts.items())],
        "first_examples":{str(k):v for k,v in first_examples.items()},
        "source_map_rows_data":source_map_rows,
        "diamond_rows":diamond_rows,
        "nonclaims":[
            "the 284 candidate diagrams are one selected parent-compatible support witness per candidate fourth edge, not an exhaustive enumeration of every support assignment",
            "the source-to-support graph maps include all root-preserving graph automorphisms; no unique source-prescribed labeling is selected",
            "finite source parent-port naturality and elementary collapse path factorization do not prove all-orders restriction naturality or geometric L8"
        ]
    }
    a.output.write_text(json.dumps(result,sort_keys=True,indent=2)+"\n")
    print(json.dumps({k:v for k,v in result.items() if k not in ("source_map_rows_data","diamond_rows","first_examples")},sort_keys=True))

if __name__=="__main__":
    main()
