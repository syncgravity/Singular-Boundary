#!/usr/bin/env python3
"""Source-labelled finite restriction audit for PF-I16 order-eight support candidates.

The output explicitly separates abstract source/graph compatibility from an
unauthenticated source-interval to target matched-edge embedding.
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

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--diagrams",type=Path,required=True)
    ap.add_argument("--output",type=Path,required=True)
    a=ap.parse_args()
    data=json.loads(a.diagrams.read_text())
    sources=hall.source_records(8)
    assert len(sources)==608
    families={"graph5":G5,"graph12":G12}
    summaries={}; witness_rows=[]; map_rows=[]
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
                              for _,r in marked)
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
            words={x["support"]:x["ordered_footprints"]
                   for x in d["anchored_boundary_footprint_words"]}
            assert set(words)==set(range(4))
            fp=tuple(len(words[i]) for i in range(4)); fp_hist[fp]+=1
            # Check ordered positions, reciprocal pair footprints, and meet bits.
            for i,row in words.items():
                starts=[x["arc_positions"][0] for x in row]
                assert starts==sorted(starts)
                meets=next(x["footprint_meet_relations"]
                           for x in d["anchored_boundary_footprint_words"]
                           if x["support"]==i)
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
            witness_rows.append({
                "family":family,"pair_index":pi,"witness_index":wi,"witness_id":wid,
                "second_edge":pair["second_edge"],"third_edge":pair["third_edge"],
                "fourth_edge":w["fourth_edge"],"support_face_indices":w["support_face_indices"],
                "intersection_diagram":d["intersections"],
                "relative_deletion_collapses":d["relative_deletion_collapses"],
                "union":d["union"],"ordered_boundary_footprint_words":d["anchored_boundary_footprint_words"],
                "root_preserving_graph_isomorphisms":[list(p) for p in perms],
                "target_boundary_word_internally_consistent":True,
                "source_interval_to_edge_embedding_authenticated":False
            })
            for si,r in marked:
                for perm in perms:
                    nmap+=1
                    legal={str(m):bool(d["relative_deletion_collapses"][str(perm[m])])
                           for m in r["eligible_reverse_marks"]}
                    assert all(legal.values()),(family,pi,wi,si,perm,legal)
                    parent_maps=[]
                    for parent in r["parents"]:
                        m=parent["deleted_interval_index"]
                        retained=[j for j in range(4) if j!=m]
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
                        assert tmn==tnm,(family,si,m,n,tmn,tnm)
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
                        "eligible_reverse_marks":marks,
                        "source_to_support_graph_isomorphism":list(perm),
                        "mapped_eligible_supports":sorted(perm[m] for m in marks),
                        "all_legal_relative_collapses_pass":True,
                        "parent_maps":parent_maps,"source_diamonds":diamonds,
                        "source_to_target_edge_embedding_authenticated":False
                    })
        summaries[family]={
            "source_record_count":len(src),"source_records_with_mark_3":len(marked),
            "source_mark_sets":{str(k):v for k,v in sorted(Counter(tuple(r["eligible_reverse_marks"]) for _,r in marked).items())},
            "parent_tree_after_delete_3_histogram":{str(k):v for k,v in sorted(tree_hist.items())},
            "root_preserving_graph_isomorphisms":[list(p) for p in perms],
            "retained_geometric_witnesses":len(candidates),
            "source_critical_diamond_count":critical_diamonds,
            "witness_source_map_rows":nmap,
            "relative_deletion_histogram":{str(k):v for k,v in sorted(drop_hist.items())},
            "footprint_count_patterns":{str(k):v for k,v in fp_hist.items()},
            "all_legal_source_deletions_pass":True,
            "all_source_parent_tree_edges_have_contractible_geometric_pairs":True
        }
    assert len(witness_rows)==996
    assert len(map_rows)==47040
    result={
        "schema":"PF-I16-SOURCE-LABELLED-FOUR-SUPPORT-RESTRICTION-AUDIT-v1",
        "source_order":8,"source_record_count":len(sources),
        "diagram_artifact_sha256":hashlib.sha256(a.diagrams.read_bytes()).hexdigest(),
        "graph_families":summaries,"witness_rows":witness_rows,"source_parent_map_rows":map_rows,
        "conclusions":{
            "root_preserving_overlap_graph_correspondence_combinatorially_compatible":True,
            "all_legal_source_parent_relative_collapses_pass":True,
            "all_source_parent_tree_edges_match_nonempty_contractible_geometric_pairs":True,
            "all_15_intersection_entries_retained_for_each_witness":True,
            "ordered_multi_footprint_words_internally_checked":True,
            "all_44_source_parent_tree_diamonds_commute":True,
            "all_44_remaining_pair_table_restrictions_are_nonempty_contractible":True,
            "source_interval_to_geometric_edge_embedding_authenticated":False,
            "source_prescribed_oriented_boundary_word_comparison_complete":False,
            "elementary_collapse_map_commutation_certified":False,
            "full_geometric_restriction_coherence_certified":False,
            "geometric_L8_closed":False
        },
        "nonclaims":[
            "The 47,040 source/witness/isomorphism rows are exhaustive combinatorial compatibility cross-checks, not authenticated source-record-to-target-edge embeddings. The canonical source exporter supplies port intervals, overlap graphs, parent trees, and reverse marks, but no map from an interval or reverse mark to a geometric matched-edge vector.",
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
