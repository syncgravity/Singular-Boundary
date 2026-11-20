#!/usr/bin/env python3
"""Source-labelled finite restriction audit for PF-I16 order-eight support candidates.

The output constructs explicit finite port-to-Z5 embeddings for every source
matching and root-preserving overlap-graph isomorphism, while keeping the
non-uniqueness of the geometric labeling and the L7b/collapse-map gaps explicit.
"""
from __future__ import annotations
import argparse, gzip, hashlib, itertools, json
from collections import Counter
from pathlib import Path
import export_pf_i16_hall_source_records as hall

G5=frozenset({(0,1),(0,2),(0,3),(1,2)})
G12=frozenset({(0,1),(0,2),(1,2),(1,3),(2,3)})

def edges(es):
    return frozenset(tuple(sorted(e)) for e in es)

def digest(x):
    return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(",",":")).encode()).hexdigest()

def isos(G):
    return [p for p in itertools.permutations(range(4))
            if p[0]==0 and edges((p[i],p[j]) for i,j in G)==G]

def face_vertices(row):
    m=tuple(row["lower"]); j,k=row["directions"]
    ej=tuple(int(t==j) for t in range(5))
    ek=tuple(int(t==k) for t in range(5))
    add=lambda a,b:tuple(a[t]+b[t] for t in range(5))
    return {m,add(m,ej),add(add(m,ej),ek),add(m,ek)}

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--diagrams",type=Path,required=True)
    ap.add_argument("--inventory",type=Path,required=True)
    ap.add_argument("--output",type=Path,required=True)
    a=ap.parse_args()
    data=json.loads(a.diagrams.read_text())
    inventory=json.loads(a.inventory.read_text())
    face_vertex_table=[face_vertices(x) for x in inventory["face_key_table"]]
    sources=hall.source_records(8)
    assert len(sources)==608
    families={"graph5":G5,"graph12":G12}
    summaries={}; witness_rows=[]; map_rows=[]; parent_port_restriction_checks=0
    for family,G in families.items():
        perms=isos(G)
        assert len(perms)==2 and all(p[0]==0 for p in perms)
        src=[(i,r) for i,r in enumerate(sources)
             if edges(r["full_overlap_edges"])==G]
        marked=[(i,r) for i,r in src if 3 in r["eligible_reverse_marks"]]
        tree_hist=Counter()
        for _,r in marked:
            p3=next(p for p in r["parents"] if p["deleted_interval_index"]==3)
            tree_hist[tuple(tuple(e) for e in p3["parent_tree_edges"])]+=1
        key=family+"_witnesses"
        candidates=[(pi,wi,pair,w) for pi,pair in enumerate(data["per_pair"])
                    for wi,w in enumerate(pair[key])]
        drop_hist=Counter(); fp_hist=Counter(); nmap=0
        critical_diamonds=sum(len(list(itertools.combinations(r["eligible_reverse_marks"],2)))
                              for _,r in src)
        for pi,wi,pair,w in candidates:
            d=w["diagram"]
            assert len(d["intersections"])==15
            imap={tuple(x["indices"]):x for x in d["intersections"]}
            assert len(imap)==15
            g=edges(k for k,v in imap.items() if len(k)==2 and v["nonempty"])
            assert g==G
            assert d["all_nonempty_intersections_point_contractible"]
            assert d["union"]["point_contractible"]
            for i,v in d["relative_deletion_collapses"].items():
                drop_hist[(int(i),bool(v))]+=1
            word_rows={x["support"]:x for x in d["anchored_boundary_footprint_words"]}
            words={i:x["ordered_footprints"] for i,x in word_rows.items()}
            assert set(words)==set(range(4))
            fp=tuple(len(words[i]) for i in range(4)); fp_hist[fp]+=1
            # Check ordered positions, reciprocal pair footprints, and meet bits.
            for i,row in words.items():
                full=word_rows[i]
                cycle=[tuple(v) for v in full["oriented_boundary_cycle"]]
                arc=[tuple(v) for v in full["open_complementary_arc"]]
                tail,head=map(tuple,full["marked_edge_orientation"])
                assert len(cycle)==full["boundary_length"] and len(set(cycle))==len(cycle)
                assert cycle[0]==tail and cycle[1]==head
                assert arc==cycle[1:]+[cycle[0]] and arc[0]==head and arc[-1]==tail
                starts=[x["arc_positions"][0] for x in row]
                assert starts==sorted(starts)
                for footprint in row:
                    pos=footprint["arc_positions"]
                    verts={tuple(v) for v in footprint["cell_vertices"]}
                    if footprint["cell_type"]=="vertex":
                        assert len(pos)==1 and 0<pos[0]<len(arc)-1
                        assert arc[pos[0]] in verts and len(verts)==1
                    else:
                        assert len(pos)==2 and 0<pos[0]<len(arc)-2
                        assert set(arc[pos[0]:pos[0]+2])==verts and len(verts)==2
                meets=full["footprint_meet_relations"]
                expected=[bool({tuple(v) for v in x["cell_vertices"]} &
                               {tuple(v) for v in y["cell_vertices"]})
                          for x,y in itertools.combinations(row,2)]
                assert [x["meet"] for x in meets]==expected
            for inds,entry in imap.items():
                if len(inds)!=2: continue
                i,j=inds
                left=[x for x in words[i] if x["neighbor"]==j]
                right=[x for x in words[j] if x["neighbor"]==i]
                if entry["nonempty"]:
                    assert len(left)==len(right)==1
                    assert left[0]["cell_type"]==right[0]["cell_type"]
                    assert {tuple(v) for v in left[0]["cell_vertices"]}=={tuple(v) for v in right[0]["cell_vertices"]}
                else:
                    assert not left and not right
            wid=digest({"family":family,"pair":pi,"witness":wi,
                        "edge":w["fourth_edge"],"supports":w["support_face_indices"]})[:20]
            target_edges=[data["fixed_first_edge"],pair["second_edge"],pair["third_edge"],w["fourth_edge"]]
            target_supports=w["support_face_indices"]
            assert len(target_edges)==len(target_supports)==4
            assert len({tuple(v) for e in target_edges for v in (e["lower"],e["upper"])})==8
            for e in target_edges:
                delta=[e["upper"][t]-e["lower"][t] for t in range(5)]
                assert sum(abs(x) for x in delta)==1 and sum(x==1 for x in delta)==1
                assert all(x>=0 for x in delta)
            witness_rows.append({
                "family":family,"pair_index":pi,"witness_index":wi,"witness_id":wid,
                "second_edge":pair["second_edge"],"third_edge":pair["third_edge"],
                "fourth_edge":w["fourth_edge"],"support_face_indices":w["support_face_indices"],
                "intersection_diagram":d["intersections"],
                "relative_deletion_collapses":d["relative_deletion_collapses"],
                "union":d["union"],"ordered_boundary_footprint_words":d["anchored_boundary_footprint_words"],
                "root_preserving_graph_isomorphisms":[list(p) for p in perms],
                "target_boundary_word_internally_consistent":True
            })
            for si,r in src:
                for perm in perms:
                    nmap+=1
                    # Source interval i is assigned to geometric support/edge perm[i].
                    # Its ordered endpoints p<q map to the lower/upper endpoint of
                    # that positively oriented unit Z^5 edge.
                    port_to_z5={}
                    interval_edge_map=[]
                    for i,(p,q) in enumerate(r["intervals"]):
                        support_index=perm[i]
                        edge=target_edges[support_index]
                        lo=tuple(edge["lower"]); hi=tuple(edge["upper"])
                        assert p<q
                        port_to_z5[str(p)]=list(lo); port_to_z5[str(q)]=list(hi)
                        face_ids=target_supports[support_index]
                        incident=[fid for fid in face_ids
                                  if lo in face_vertex_table[fid] and hi in face_vertex_table[fid]]
                        assert len(incident)==1,(family,pi,wi,si,perm,i,incident)
                        assert lo in face_vertex_table[incident[0]] and hi in face_vertex_table[incident[0]]
                        interval_edge_map.append({
                            "source_interval_index":i,"source_interval":[p,q],
                            "geometric_support_index":support_index,
                            "matched_edge":{"lower":list(lo),"upper":list(hi)},
                            "positive_unit_direction":next(t for t,x in enumerate(hi)
                                if x-lo[t]==1),
                            "unique_accepted_rhombus_containing_matched_edge":incident[0]
                        })
                    assert set(map(int,port_to_z5))==set(range(1,9))
                    assert len({tuple(v) for v in port_to_z5.values()})==8
                    # Recheck the full source overlap graph against the mapped
                    # geometric intersection table, including nonedges.
                    source_graph=edges(r["full_overlap_edges"])
                    for i,j in itertools.combinations(range(4),2):
                        assert ((i,j) in source_graph)==imap[tuple(sorted((perm[i],perm[j]))) ]["nonempty"]
                    legal={str(m):bool(d["relative_deletion_collapses"][str(perm[m])])
                           for m in r["eligible_reverse_marks"]}
                    assert all(legal.values()),(family,pi,wi,si,perm,legal)
                    parent_maps=[]
                    for parent in r["parents"]:
                        m=parent["deleted_interval_index"]
                        retained=[j for j in range(4) if j!=m]
                        # Restrict the child port embedding to retained ports,
                        # then apply the source's exact order-compression map.
                        compression={int(k):v for k,v in parent["port_order_compression"].items()}
                        restricted_port_map={str(compression[p]):port_to_z5[str(p)]
                                             for p in parent["retained_ports_before_compression"]}
                        parent_port_map={}
                        for parent_i,(p,q) in enumerate(parent["parent_intervals"]):
                            edge=target_edges[perm[retained[parent_i]]]
                            parent_port_map[str(p)]=edge["lower"]
                            parent_port_map[str(q)]=edge["upper"]
                        assert restricted_port_map==parent_port_map,(family,pi,wi,si,perm,m)
                        parent_port_restriction_checks+=1
                        tree_geom=[tuple(sorted((perm[retained[x]],perm[retained[y]])))
                                   for x,y in parent["parent_tree_edges"]]
                        checks=[]
                        for x,y in tree_geom:
                            ent=imap[(x,y)]
                            assert ent["nonempty"] and ent["point_contractible"]
                            wx=[z for z in words[x] if z["neighbor"]==y]
                            wy=[z for z in words[y] if z["neighbor"]==x]
                            assert len(wx)==len(wy)==1
                            assert wx[0]["cell_type"]==wy[0]["cell_type"]
                            checks.append({"edge":[x,y],"intersection_nonempty_contractible":True,
                                           "reciprocal_ordered_footprints":True,
                                           "cell_type":wx[0]["cell_type"]})
                        parent_maps.append({
                            "deleted_interval_index":m,"deleted_interval":parent["deleted_interval"],
                            "mapped_support":perm[m],"parent_intervals":parent["parent_intervals"],
                            "parent_port_map":parent_port_map,
                            "port_map_restriction_commutes":True,
                            "source_parent_tree_edges":parent["parent_tree_edges"],
                            "mapped_geometric_parent_tree_edges":tree_geom,
                            "tree_edge_checks":checks,"relative_collapse_pass":legal[str(m)]
                        })
                    diamonds=[]
                    marks=r["eligible_reverse_marks"]
                    for m,n in itertools.combinations(marks,2):
                        pm=next(p for p in r["parents"] if p["deleted_interval_index"]==m)
                        pn=next(p for p in r["parents"] if p["deleted_interval_index"]==n)
                        rm=[j for j in range(4) if j!=m]
                        rn=[j for j in range(4) if j!=n]
                        def second(parent,deleted):
                            keep=[j for j in range(3) if j!=deleted]
                            ren={old:new for new,old in enumerate(keep)}
                            return sorted(tuple(sorted((ren[x],ren[y])))
                                for x,y in parent["parent_tree_edges"]
                                if x!=deleted and y!=deleted)
                        tmn=second(pm,rm.index(n)); tnm=second(pn,rn.index(m))
                        assert tmn==tnm and len(tmn)==1,(family,si,m,n,tmn,tnm)
                        remain=[j for j in range(4) if j not in (m,n)]
                        pairkey=tuple(sorted((perm[remain[0]],perm[remain[1]])))
                        ent=imap[pairkey]
                        assert ent["nonempty"] and ent["point_contractible"]
                        assert legal[str(m)] and legal[str(n)]
                        diamonds.append({
                            "source_marks":[m,n],"mapped_supports":[perm[m],perm[n]],
                            "parent_tree_after_m_then_n":tmn,"parent_tree_after_n_then_m":tnm,
                            "source_tree_diamond_commutes":True,
                            "remaining_support_pair":list(pairkey),
                            "remaining_pair_intersection_nonempty_contractible":True,
                            "both_relative_collapses_pass":True,
                            "incidence_table_restriction_coherent":True,
                            "collapse_map_commutation_proved":False
                        })
                    map_rows.append({
                        "family":family,"pair_index":pi,"witness_index":wi,"witness_id":wid,
                        "source_index":si,"source_intervals":r["intervals"],
                        "source_tree_edges":r["tree_edges"],
                        "source_to_target_port_map":port_to_z5,
                        "source_interval_to_target_edge_map":interval_edge_map,
                        "L1_port_map_injective":True,"L2_positive_unit_edges":True,
                        "L3_endpoints_in_accepted_support_faces":True,
                        "L4_L5_full_overlap_graph_preserved":True,
                        "eligible_reverse_marks":marks,
                        "source_to_support_graph_isomorphism":list(perm),
                        "mapped_eligible_supports":sorted(perm[m] for m in marks),
                        "all_legal_relative_collapses_pass":True,
                        "parent_maps":parent_maps,"source_diamonds":diamonds,
                        "all_parent_port_restrictions_natural":True,
                        "finite_source_to_target_port_embedding_verified":True,
                        "unique_source_to_target_graph_isomorphism_identified":False
                    })
        summaries[family]={
            "source_record_count":len(src),"source_records_with_mark_3":len(marked),
            "source_mark_sets":{str(k):v for k,v in sorted(Counter(tuple(r["eligible_reverse_marks"]) for _,r in marked).items())},
            "parent_tree_after_delete_3_histogram":{str(k):v for k,v in sorted(tree_hist.items())},
            "root_preserving_graph_isomorphisms":[list(p) for p in perms],
            "retained_geometric_witnesses":len(candidates),
            "source_critical_diamond_count":critical_diamonds,
            "witness_source_map_rows":nmap,
            "finite_L1_L3_port_embeddings_verified":nmap,
            "relative_deletion_histogram":{str(k):v for k,v in sorted(drop_hist.items())},
            "footprint_count_patterns":{str(k):v for k,v in fp_hist.items()},
            "all_legal_source_deletions_pass":True,
            "all_source_parent_tree_edges_have_contractible_geometric_pairs":True
        }
    assert len(witness_rows)==996
    assert len(map_rows)==58608
    result={
        "schema":"PF-I16-SOURCE-LABELLED-FOUR-SUPPORT-RESTRICTION-AUDIT-v2",
        "source_order":8,"source_record_count":len(sources),
        "diagram_artifact_sha256":hashlib.sha256(a.diagrams.read_bytes()).hexdigest(),
        "graph_families":summaries,"witness_rows":witness_rows,"source_parent_map_rows":map_rows,
        "conclusions":{
            "root_preserving_overlap_graph_correspondence_combinatorially_compatible":True,
            "all_legal_source_parent_relative_collapses_pass":True,
            "all_source_parent_tree_edges_match_nonempty_contractible_geometric_pairs":True,
            "all_15_intersection_entries_retained_for_each_witness":True,
            "ordered_multi_footprint_words_internally_checked":True,
            "all_oriented_boundary_cycles_exported_and_checked":True,
            "all_44_source_parent_tree_diamonds_commute":True,
            "all_44_remaining_pair_table_restrictions_are_nonempty_contractible":True,
            "finite_order8_source_interval_to_geometric_edge_embedding_verified":True,
            "all_parent_port_map_restrictions_commute":True,
            "parent_port_restriction_check_count":parent_port_restriction_checks,
            "only_graph5_and_graph12_source_families_audited":True,
            "unique_source_to_target_graph_isomorphism_identified":False,
            "source_prescribed_oriented_boundary_word_comparison_complete":False,
            "elementary_collapse_map_commutation_certified":False,
            "full_geometric_restriction_coherence_certified":False,
            "geometric_L8_closed":False
        },
        "nonclaims":[
            "The 58,608 source/witness/isomorphism rows now include explicit finite port-to-Z5 maps: source interval i maps its ordered endpoints to the lower/upper endpoints of target edge perm[i]. L1 injectivity, L2 positive unit-edge realization, L3 accepted-support endpoint membership, and exact L4/L5 overlap-graph preservation are checked for every row. This is a constructed finite embedding for each retained candidate, not a unique source-prescribed map; both root-preserving graph automorphisms remain valid.",
            "The source record contains no prescribed oriented boundary cycle or multi-footprint word. The target words are checked for internal order, reciprocal pair footprints, and meeting relations, but no source-prescribed L7b comparison is available.",
            "The source parent-tree diamonds commute exactly at the abstract tree level, and the stored intersection table restricts coherently to the remaining pair. Relative-collapse booleans do not supply elementary collapse maps or prove those maps commute.",
            "The source exporter specifies pairwise interval overlap only. Higher-order triple and four-way intersections remain target-geometric data without a source-side prescribed comparison.",
            "No geometric L8 or all-orders Hall theorem follows from this finite Ngrid=12 audit."
        ]
    }
    a.output.parent.mkdir(parents=True,exist_ok=True)
    with gzip.open(a.output,"wt",encoding="utf-8",compresslevel=9) as f:
        json.dump(result,f,sort_keys=True,separators=(",",":"))
    print(json.dumps({"schema":result["schema"],"witness_rows":len(witness_rows),
        "source_parent_map_rows":len(map_rows),"families":summaries,
        "conclusions":result["conclusions"]},sort_keys=True,indent=2))

if __name__=="__main__":
    main()
