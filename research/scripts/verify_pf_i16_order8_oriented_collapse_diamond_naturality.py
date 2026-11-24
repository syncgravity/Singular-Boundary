#!/usr/bin/env python3
"""Order-eight oriented-boundary and elementary-collapse diamond audit.

Reconstructs all 996 graph-5/graph-12 four-support boundary cycles from the
accepted rhombus faces, checks all 15 labelled intersections, and lifts every
source critical pair in the 60 represented order-eight source records through
both root-preserving graph maps. The other 446 of the 490 source diamonds are
verified source-side but have no four-support candidate in this finite family.
"""
from __future__ import annotations
import argparse, gzip, hashlib, itertools, json
from collections import Counter, defaultdict
from pathlib import Path

import export_pf_i16_hall_source_records as hall
import verify_pf_i16_hall_four_interval_parent_compatibility as geom

G5 = frozenset({(0,1),(0,2),(0,3),(1,2)})
G12 = frozenset({(0,1),(0,2),(1,2),(1,3),(2,3)})

def digest(x):
    return hashlib.sha256(json.dumps(x, sort_keys=True, separators=(",", ":")).encode()).hexdigest()

def edge_set(es):
    return frozenset(tuple(sorted(e)) for e in es)

def complex_dict(parts):
    return {k:set(v) for k,v in zip(("F","E","V"),parts)}

def union_complex(supports, indices):
    return {k:set().union(*(supports[i][k] for i in indices)) for k in ("F","E","V")}

def intersection_complex(supports, indices):
    return {k:set.intersection(*(set(supports[i][k]) for i in indices)) for k in ("F","E","V")}

def boundary_cycle(support, directed, face_edges):
    counts=Counter()
    for fid in support["F"]:
        counts.update(face_edges[fid])
    boundary={e for e,n in counts.items() if n==1}
    tail,head=tuple(directed[0]),tuple(directed[1])
    if tuple(sorted((tail,head))) not in boundary:
        return None
    adj=defaultdict(set)
    for a,b in boundary:
        adj[a].add(b); adj[b].add(a)
    if not adj or any(len(v)!=2 for v in adj.values()):
        return None
    seen=set(); stack=[next(iter(adj))]
    while stack:
        x=stack.pop()
        if x in seen: continue
        seen.add(x); stack.extend(adj[x]-seen)
    if seen!=set(adj):
        return None
    cycle=[tail,head]; previous,current=tail,head
    while True:
        choices=adj[current]-{previous}
        if len(choices)!=1: return None
        nxt=next(iter(choices))
        if nxt==tail: break
        if nxt in cycle: return None
        cycle.append(nxt); previous,current=current,nxt
    return cycle if len(cycle)==len(boundary) else None

def derive_footprint_word(i, supports, cycles):
    row=[]
    for j in range(4):
        if i==j: continue
        common=intersection_complex(supports,[i,j])
        counts=Counter()
        for fid in supports[i]["F"]:
            counts.update(FACE_EDGES[fid])
        boundary={e for e,n in counts.items() if n==1}
        shared=common["E"] & boundary
        if shared:
            if len(shared)!=1 or len(common["V"])!=2:
                raise AssertionError(("non-singleton edge footprint",i,j,shared,common["V"]))
            e=next(iter(shared))
            pos=next((k for k in range(len(cycles[i]))
                      if tuple(sorted((cycles[i][k],cycles[i][(k+1)%len(cycles[i])])))==e),None)
            if pos is None or pos<=1 or pos>=len(cycles[i])-1:
                raise AssertionError(("edge footprint outside open arc",i,j,pos))
            row.append({"neighbor":j,"cell_type":"edge",
                        "arc_positions":[pos-1,pos],
                        "cell_vertices":[list(cycles[i][pos]),list(cycles[i][(pos+1)%len(cycles[i])])]})
        elif common["V"]:
            common_boundary=common["V"] & set(cycles[i])
            if len(common_boundary)!=1 or common["E"]:
                raise AssertionError(("non-singleton vertex footprint",i,j,common_boundary,common["E"]))
            v=next(iter(common_boundary)); pos=cycles[i].index(v)
            if pos<=1:
                raise AssertionError(("vertex footprint at anchor endpoint",i,j,pos))
            row.append({"neighbor":j,"cell_type":"vertex",
                        "arc_positions":[pos-1],"cell_vertices":[list(v)]})
    row.sort(key=lambda x:(x["arc_positions"][0],x["neighbor"]))
    return row

def encode_pair(p):
    if p[0]=="FE":
        return {"kind":"FE","free_edge":[list(p[1][0]),list(p[1][1])],"removed_face":p[2]}
    return {"kind":"EV","free_vertex":list(p[1]),"removed_edge":[list(p[2][0]),list(p[2][1])]}

def collapse_sequence(src, tgt, face_edges, face_vertices):
    F,E,V=(set(src[k]) for k in ("F","E","V"))
    TF,TE,TV=(set(tgt[k]) for k in ("F","E","V"))
    out=[]
    while True:
        found=None
        for e in sorted(E-TE):
            incident=[f for f in F if e in face_edges[f]]
            if len(incident)==1 and incident[0] not in TF:
                found=(e,incident[0]); break
        if found is None: break
        e,f=found; out.append(("FE",e,f)); E.remove(e); F.remove(f)
    while True:
        found=None
        for e in sorted(E-TE):
            for v in e:
                degree=sum(v in ee for ee in E)
                in_face=any(v in face_vertices[f] for f in F)
                if v not in TV and degree==1 and not in_face:
                    found=(v,e); break
            if found is not None: break
        if found is None: break
        v,e=found; out.append(("EV",v,e)); E.remove(e); V.remove(v)
    final={"F":F,"E":E,"V":V}
    if final!={"F":TF,"E":TE,"V":TV}:
        return None
    return out

def apply_pair(state,pair,target,face_edges,face_vertices):
    F,E,V=(set(state[k]) for k in ("F","E","V"))
    TF,TE,TV=(set(target[k]) for k in ("F","E","V"))
    if pair[0]=="FE":
        _,e,f=pair
        incident={g for g in F if e in face_edges[g]}
        if e not in E or f not in F or e in TE or f in TF or incident!={f}:
            return None
        F.remove(f); E.remove(e)
    else:
        _,v,e=pair
        degree=sum(v in ee for ee in E)
        in_face=any(v in face_vertices[g] for g in F)
        if v not in V or e not in E or v in TV or e in TE or degree!=1 or in_face:
            return None
        E.remove(e); V.remove(v)
    return {"F":F,"E":E,"V":V}

def replay(pairs,start,target,face_edges,face_vertices):
    state={k:set(v) for k,v in start.items()}
    for p in pairs:
        state=apply_pair(state,p,target,face_edges,face_vertices)
        if state is None: return None
    return state

def pair_cells(p):
    return (("E",p[1]),("F",p[2])) if p[0]=="FE" else (("V",p[1]),("E",p[2]))

def alternating_cycle(left,right):
    adj=defaultdict(set)
    for p in (set(left)-set(right)) | (set(right)-set(left)):
        a,b=pair_cells(p); adj[a].add(b); adj[b].add(a)
    if not adj or any(len(v)!=2 for v in adj.values()):
        return False,0
    seen=set(); stack=[next(iter(adj))]
    while stack:
        x=stack.pop()
        if x in seen: continue
        seen.add(x); stack.extend(adj[x]-seen)
    return len(seen)==len(adj),len(adj)

def normalize(left,right,start,target,face_edges,face_vertices):
    left=list(left); right=list(right)
    if set(left)!=set(right): return None
    swaps=0
    for i,want in enumerate(right):
        j=left.index(want,i)
        while j>i:
            state=replay(left[:j-1],start,target,face_edges,face_vertices)
            if state is None: return None
            a,b=left[j-1],left[j]
            ab1=apply_pair(state,a,target,face_edges,face_vertices)
            ab=apply_pair(ab1,b,target,face_edges,face_vertices) if ab1 is not None else None
            ba1=apply_pair(state,b,target,face_edges,face_vertices)
            ba=apply_pair(ba1,a,target,face_edges,face_vertices) if ba1 is not None else None
            if ab is None or ba is None or ab!=ba: return None
            left[j-1],left[j]=left[j],left[j-1]; swaps+=1; j-=1
    return swaps if left==right else None

def dependency_close(pairs,start,target,initial,face_edges,face_vertices):
    ordered=list(pairs); block=set(initial); swaps=0
    while True:
        changed=False
        for j in range(len(ordered)-1):
            if ordered[j] in block and ordered[j+1] not in block:
                a,b=ordered[j],ordered[j+1]
                state=replay(ordered[:j],start,target,face_edges,face_vertices)
                assert state is not None
                ab1=apply_pair(state,a,target,face_edges,face_vertices)
                ab=apply_pair(ab1,b,target,face_edges,face_vertices) if ab1 is not None else None
                ba1=apply_pair(state,b,target,face_edges,face_vertices)
                ba=apply_pair(ba1,a,target,face_edges,face_vertices) if ba1 is not None else None
                if ab is not None and ba is not None and ab==ba:
                    ordered[j],ordered[j+1]=b,a; swaps+=1
                else:
                    block.add(b)
                changed=True; break
        if not changed: break
    assert replay(ordered,start,target,face_edges,face_vertices)==target
    prefix=[p for p in ordered if p not in block]
    suffix=[p for p in ordered if p in block]
    assert ordered==prefix+suffix
    return block,swaps,prefix,suffix

def delete_source(intervals,tree,mark,nports):
    retained=[p for p in range(1,nports+1) if p not in intervals[mark]]
    compression={p:i+1 for i,p in enumerate(retained)}
    parent_intervals=tuple(sorted((compression[a],compression[b])
                                  for i,(a,b) in enumerate(intervals) if i!=mark))
    old=[i for i in range(len(intervals)) if i!=mark]
    oldmap={o:i for i,o in enumerate(old)}
    parent_tree=tuple(sorted(tuple(sorted((oldmap[a],oldmap[b])))
                             for a,b in tree if a!=mark and b!=mark))
    return parent_intervals,parent_tree,compression

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--diagrams",type=Path,required=True)
    ap.add_argument("--inventory",type=Path,required=True)
    ap.add_argument("--source-audit",type=Path,required=True)
    ap.add_argument("--output",type=Path,required=True)
    a=ap.parse_args()
    data=json.loads(a.diagrams.read_text())
    inv=json.loads(a.inventory.read_text())
    with gzip.open(a.source_audit,"rt",encoding="utf-8") as f:
        source_audit=json.load(f)
    diagram_sha=hashlib.sha256(a.diagrams.read_bytes()).hexdigest()
    face_sha=digest(inv["face_key_table"])
    assert diagram_sha=="aa2d4ae88b3d23e34007eed45858a54b7d98bfd9fa6c595b11635d04a74817ba",diagram_sha
    assert face_sha=="c20b727809eeb173ec11f584c2d60fc7afa3283e39a2dc3ccde0187703ce9ec9",face_sha
    assert source_audit["schema"]=="PF-I16-SOURCE-LABELLED-FOUR-SUPPORT-RESTRICTION-AUDIT-v1"
    assert len(source_audit["witness_rows"])==996
    assert len(source_audit["source_parent_map_rows"])==58608

    face_vertices,face_edges,options,_=geom.build_target(inv)
    global FACE_EDGES
    FACE_EDGES=face_edges
    sources=hall.source_records(8)
    assert len(sources)==608
    source_by_index={i:r for i,r in enumerate(sources)}
    family_graph={"graph5":G5,"graph12":G12}
    witness_lookup={}
    boundary_rows=[]
    intersection_entries=relative_checks=cycle_checks=arc_checks=word_checks=0
    footprint_count_hist=Counter()
    map_coarse_swap_counts=Counter(); map_word_swap_counts=Counter()
    for wr in source_audit["witness_rows"]:
        fam=wr["family"]; pi=wr["pair_index"]; wi=wr["witness_index"]
        dw=data["per_pair"][pi][fam+"_witnesses"][wi]
        supports=[complex_dict(geom.cells(tuple(sorted(s)))) for s in dw["support_face_indices"]]
        edges=[data["fixed_first_edge"],wr["second_edge"],wr["third_edge"],wr["fourth_edge"]]
        cycles=[]
        for i in range(4):
            cyc=boundary_cycle(supports[i],(edges[i]["lower"],edges[i]["upper"]),face_edges)
            assert cyc is not None,(wr["witness_id"],i,"invalid anchored boundary cycle")
            stored=next(x for x in dw["diagram"]["anchored_boundary_footprint_words"] if x["support"]==i)
            assert cyc==[tuple(v) for v in stored["oriented_boundary_cycle"]]
            assert stored["marked_edge_orientation"]==[edges[i]["lower"],edges[i]["upper"]]
            arc=cyc[1:]+[cyc[0]]
            assert arc==[tuple(v) for v in stored["open_complementary_arc"]]
            assert len(cyc)==stored["boundary_length"]==8
            cycles.append(cyc); cycle_checks+=1; arc_checks+=1
        for i in range(4):
            derived=derive_footprint_word(i,supports,cycles)
            stored=next(x for x in dw["diagram"]["anchored_boundary_footprint_words"] if x["support"]==i)
            assert derived==stored["ordered_footprints"],(wr["witness_id"],i)
            # Recompute footprint meeting relations.
            meets=[]
            for x,y in itertools.combinations(derived,2):
                xv={tuple(v) for v in x["cell_vertices"]}
                yv={tuple(v) for v in y["cell_vertices"]}
                meets.append({"neighbors":[x["neighbor"],y["neighbor"]],"meet":bool(xv&yv)})
            assert meets==stored["footprint_meet_relations"]
            word_checks+=1
        # The two root-preserving graph maps differ by swapping support labels 1 and 2.
        # Check whether that swap preserves the coarse intersection table or the
        # finer ordered boundary words; the source exporter prescribes neither word.
        swap={0:0,1:2,2:1,3:3}
        def swap_indices(inds):
            return tuple(sorted(swap[x] for x in inds))
        imap={tuple(x["indices"]):x for x in dw["diagram"]["intersections"]}
        coarse_sig=lambda x:(x["nonempty"],x["face_count"],x["edge_count"],x["vertex_count"],x["point_contractible"])
        coarse_ok=all(coarse_sig(e)==coarse_sig(imap[swap_indices(inds)]) for inds,e in imap.items())
        map_coarse_swap_counts[(fam,coarse_ok)]+=1
        word_rows={x["support"]:x["ordered_footprints"] for x in dw["diagram"]["anchored_boundary_footprint_words"]}
        word_ok=True
        for i in range(4):
            relabelled=[(swap[x["neighbor"]],x["cell_type"],tuple(x["arc_positions"])) for x in word_rows[i]]
            target_word=[(x["neighbor"],x["cell_type"],tuple(x["arc_positions"])) for x in word_rows[swap[i]]]
            if relabelled!=target_word:
                word_ok=False
                break
        map_word_swap_counts[(fam,word_ok)]+=1
            footprint_count_hist[len(derived)]+=1
        # Exact all-15 labelled intersection content, including empty entries.
        imap={tuple(x["indices"]):x for x in dw["diagram"]["intersections"]}
        assert len(imap)==15
        for r in range(1,5):
            for inds in itertools.combinations(range(4),r):
                cc=intersection_complex(supports,inds)
                entry=imap[inds]
                h=digest([sorted(map(str,sorted(cc[k]))) for k in ("F","E","V")])
                assert entry["cell_digest"]==h
                assert entry["face_count"]==len(cc["F"])
                assert entry["edge_count"]==len(cc["E"])
                assert entry["vertex_count"]==len(cc["V"])
                assert entry["nonempty"]==bool(cc["V"])
                pc=geom.point_contractible(tuple(cc[k] for k in ("F","E","V"))) if cc["V"] else None
                assert entry["point_contractible"]==pc
                intersection_entries+=1
        full=union_complex(supports,range(4))
        for i in range(4):
            target=union_complex(supports,[j for j in range(4) if j!=i])
            ok=geom.collapse(tuple(full[k] for k in ("F","E","V")),
                             tuple(target[k] for k in ("F","E","V")))
            assert bool(ok)==bool(dw["diagram"]["relative_deletion_collapses"][str(i)])
            relative_checks+=1
        witness_lookup[(fam,pi,wi)]={"row":wr,"diagram":dw,"supports":supports,"edges":edges}
        boundary_rows.append({"family":fam,"pair_index":pi,"witness_index":wi,
                              "witness_id":wr["witness_id"],"oriented_cycles":cycles,
                              "footprint_word_digests":[digest(derived_footprints) for derived_footprints in
                                  [next(x for x in dw["diagram"]["anchored_boundary_footprint_words"] if x["support"]==i)["ordered_footprints"] for i in range(4)]]})

    # Verify all 608 source records and all 490 source-side deletion diamonds.
    source_diamonds=source_diamonds_ok=0
    geometric_source_diamonds=set()
    for si,sr in enumerate(sources):
        ints=tuple(tuple(x) for x in sr["intervals"])
        tree=tuple(tuple(x) for x in sr["tree_edges"])
        for m,n in itertools.combinations(sr["eligible_reverse_marks"],2):
            source_diamonds+=1
            im,tm,cm=delete_source(ints,tree,m,8)
            n1=n-1 if n>m else n
            imn,tmn,cnm=delete_source(im,tm,n1,6)
            inn,tn,cn=delete_source(ints,tree,n,8)
            m1=m-1 if m>n else m
            inm,tnm,cnm2=delete_source(inn,tn,m1,6)
            cmn={p:cnm[cm[p]] for p in cm if cm[p] in cnm}
            cnm_final={p:cnm2[cn[p]] for p in cn if cn[p] in cnm2}
            assert (imn,tmn,cmn)==(inm,tnm,cnm_final),(si,m,n)
            source_diamonds_ok+=1
            if edge_set(sr["full_overlap_edges"]) in (G5,G12):
                geometric_source_diamonds.add((edge_set(sr["full_overlap_edges"]),si,tuple(sorted((m,n)))))
    assert source_diamonds==source_diamonds_ok==490
    assert footprint_count_hist==Counter({1:514,2:1478,3:1992})
    assert map_coarse_swap_counts==Counter({("graph5",True):178,("graph5",False):336,("graph12",True):110,("graph12",False):372})
    assert map_word_swap_counts==Counter({("graph5",False):514,("graph12",False):482})
    assert len(geometric_source_diamonds)==44

    # Recheck the 58,608 finite source-to-target maps and collect the actual
    # source-diamond instances represented by the graph-5/graph-12 geometry.
    map_rows=source_audit["source_parent_map_rows"]
    assert len(map_rows)==58608
    map_diamond_instances=0
    parent_restrictions=0
    weights=Counter()
    source_map_keys=set()
    for mr in map_rows:
        fam=mr["family"]; pi=mr["pair_index"]; wi=mr["witness_index"]
        key=(fam,pi,wi)
        wr=witness_lookup[key]["row"]
        obj=witness_lookup[key]
        sr=source_by_index[mr["source_index"]]
        perm=mr["source_to_support_graph_isomorphism"]
        assert edge_set(sr["full_overlap_edges"])==family_graph[fam]
        assert list(sr["intervals"])==mr["source_intervals"]
        assert list(sr["tree_edges"])==mr["source_tree_edges"]
        assert perm in ([0,1,2,3],[0,2,1,3])
        edges=obj["edges"]
        port_map={}
        interval_edge_map=[]
        for i,(p,q) in enumerate(sr["intervals"]):
            support_index=perm[i]
            edge=edges[support_index]
            lo=tuple(edge["lower"]); hi=tuple(edge["upper"])
            port_map[str(p)]=list(lo); port_map[str(q)]=list(hi)
            face_ids=obj["diagram"]["support_face_indices"][support_index]
            incident=[fid for fid in face_ids if lo in face_vertices[fid] and hi in face_vertices[fid]]
            assert len(incident)==1
            interval_edge_map.append((support_index,lo,hi,incident[0]))
        assert port_map==mr["source_to_target_port_map"]
        assert len(set(tuple(v) for v in port_map.values()))==8
        assert mr["L1_port_map_injective"] and mr["L2_positive_unit_edges"] and mr["L3_endpoints_in_accepted_support_faces"]
        source_graph=edge_set(sr["full_overlap_edges"])
        imap={tuple(x["indices"]):x for x in obj["diagram"]["diagram"]["intersections"]}
        for i,j in itertools.combinations(range(4),2):
            assert ((i,j) in source_graph)==imap[tuple(sorted((perm[i],perm[j]))) ]["nonempty"]
        assert mr["L4_L5_full_overlap_graph_preserved"]
        for parent in sr["parents"]:
            m=parent["deleted_interval_index"]
            retained=[j for j in range(4) if j!=m]
            comp={int(k):v for k,v in parent["port_order_compression"].items()}
            restricted={str(comp[p]):port_map[str(p)] for p in parent["retained_ports_before_compression"]}
            parent_map={}
            for parent_i,(p,q) in enumerate(parent["parent_intervals"]):
                e=edges[perm[retained[parent_i]]]
                parent_map[str(p)]=e["lower"]; parent_map[str(q)]=e["upper"]
            assert restricted==parent_map
            parent_restrictions+=1
        for d in mr["source_diamonds"]:
            m,n=d["source_marks"]
            sm,sn=perm[m],perm[n]
            pair=tuple(sorted((sm,sn)))
            rem=tuple(sorted(set(range(4))-{sm,sn}))
            assert tuple(sorted(d["remaining_support_pair"]))==rem
            assert d["source_tree_diamond_commutes"]
            assert d["both_relative_collapses_pass"]
            assert d["remaining_pair_intersection_nonempty_contractible"]
            wa=[x for x in next(x for x in obj["diagram"]["diagram"]["anchored_boundary_footprint_words"] if x["support"]==rem[0])["ordered_footprints"] if x["neighbor"]==rem[1]]
            wb=[x for x in next(x for x in obj["diagram"]["diagram"]["anchored_boundary_footprint_words"] if x["support"]==rem[1])["ordered_footprints"] if x["neighbor"]==rem[0]]
            assert len(wa)==len(wb)==1
            assert wa[0]["cell_type"]==wb[0]["cell_type"]
            assert {tuple(v) for v in wa[0]["cell_vertices"]}=={tuple(v) for v in wb[0]["cell_vertices"]}
            weights[(key,pair)]+=1
            map_diamond_instances+=1
            source_map_keys.add((fam,mr["source_index"],tuple(sorted((m,n)))))
    assert parent_restrictions==98192
    assert map_diamond_instances==43696
    assert len(source_map_keys)==44

    # Construct both elementary-collapse orders for each unique witness/map
    # support-pair. The path is U4 -> U3(-m) -> U2(-m,-n), and conversely.
    path_rows=[]
    pair_set_counts=Counter(); cycle_counts=Counter(); same_swap_counts=Counter()
    family_pair_counts=defaultdict(Counter)
    block_counts=Counter(); extra_counts=Counter(); prefix_swap_counts=Counter()
    extra_order_counts=Counter()
    for (key,pair),weight in sorted(weights.items(),key=lambda x:(x[0][0],x[0][1])):
        obj=witness_lookup[key]; supports=obj["supports"]
        full=union_complex(supports,range(4))
        m,n=pair
        mid_m=union_complex(supports,[i for i in range(4) if i!=m])
        mid_n=union_complex(supports,[i for i in range(4) if i!=n])
        target=union_complex(supports,[i for i in range(4) if i not in pair])
        a1=collapse_sequence(full,mid_m,face_edges,face_vertices)
        a2=collapse_sequence(mid_m,target,face_edges,face_vertices)
        b1=collapse_sequence(full,mid_n,face_edges,face_vertices)
        b2=collapse_sequence(mid_n,target,face_edges,face_vertices)
        assert all(x is not None for x in (a1,a2,b1,b2)),(key,pair)
        L=a1+a2; R=b1+b2
        assert replay(L,full,target,face_edges,face_vertices)==target
        assert replay(R,full,target,face_edges,face_vertices)==target
        same=set(L)==set(R)
        pair_set_counts["same" if same else "different"]+=weight
        family_pair_counts[key[0]]["same_pair_set" if same else "different_pair_set"]+=weight
        cycle_size=None; swaps=None
        blockL=blockR=None; prefixL=prefixR=None; suffixL=suffixR=None
        prefix_norm=None; extra_wordL=extra_wordR=()
        if same:
            swaps=normalize(L,R,full,target,face_edges,face_vertices)
            assert swaps is not None
            same_swap_counts[swaps]+=weight
        else:
            ok,cycle_size=alternating_cycle(L,R)
            assert ok and cycle_size in (4,6,8,12),(key,pair,cycle_size)
            cycle_counts[cycle_size]+=weight
            family_pair_counts[key[0]][f"alternating_cycle_{cycle_size}_cells"]+=weight
            dL=set(L)-set(R); dR=set(R)-set(L)
            blockL,sl,prefixL,suffixL=dependency_close(L,full,target,dL,face_edges,face_vertices)
            blockR,sr,prefixR,suffixR=dependency_close(R,full,target,dR,face_edges,face_vertices)
            midL=replay(prefixL,full,target,face_edges,face_vertices)
            midR=replay(prefixR,full,target,face_edges,face_vertices)
            assert set(prefixL)==set(prefixR) and midL==midR
            assert (blockL-dL)==(blockR-dR)
            assert replay(suffixL,midL,target,face_edges,face_vertices)==target
            assert replay(suffixR,midR,target,face_edges,face_vertices)==target
            prefix_norm=normalize(prefixL,prefixR,full,midL,face_edges,face_vertices)
            assert prefix_norm is not None
            prefix_swap_counts[prefix_norm]+=weight
            extraL=blockL-dL; extraR=blockR-dR
            extra_wordL=tuple(p[0] for p in suffixL if p in extraL)
            extra_wordR=tuple(p[0] for p in suffixR if p in extraR)
            block_counts[len(blockL)]+=weight
            extra_counts[len(extraL)]+=weight
            extra_order_counts[(len(blockL),extra_wordL,extra_wordR,extra_wordL==extra_wordR)]+=weight
        path_rows.append({
            "family":key[0],"pair_index":key[1],"witness_index":key[2],
            "support_pair":list(pair),"source_map_diamond_instances":weight,
            "left_path_length":len(L),"right_path_length":len(R),
            "left_path_sha256":digest([encode_pair(p) for p in L]),
            "right_path_sha256":digest([encode_pair(p) for p in R]),
            "same_elementary_pair_set":same,"same_pair_set_normalizing_swaps":swaps,
            "alternating_cycle_cell_count":cycle_size,
            "dependency_closed_left_suffix_pairs":len(blockL) if blockL is not None else None,
            "dependency_closed_right_suffix_pairs":len(blockR) if blockR is not None else None,
            "common_extra_pair_count":len(blockL-(set(L)-set(R))) if blockL is not None else None,
            "common_prefix_pair_set":bool(prefixL is not None),
            "common_intermediate_inventory":bool(prefixL is not None),
            "prefix_normalizing_valid_swaps":prefix_norm,
            "left_common_extra_pair_word":list(extra_wordL),
            "right_common_extra_pair_word":list(extra_wordR),
            "common_extra_pair_order_equal":(extra_wordL==extra_wordR) if prefixL is not None else None
        })

    assert sum(pair_set_counts.values())==43696
    assert pair_set_counts==Counter({"same":25472,"different":18224})
    assert cycle_counts==Counter({4:256,6:7488,8:9120,12:1360})
    assert sum(same_swap_counts.values())==25472
    assert sum(prefix_swap_counts.values())==18224
    assert block_counts==Counter({4:1696,5:8064,6:32,7:1680,8:3824,10:1360,11:1568})
    assert extra_counts==Counter({0:1632,1:2160,2:6912,4:4496,5:512,6:1296,7:1152,8:64})
    order_sensitive=sum(v for (_,_,_,eq),v in extra_order_counts.items() if not eq)
    assert order_sensitive==5424

    result={
        "schema":"PF-I16-ORDER8-ORIENTED-COLLAPSE-DIAMOND-NATURALITY-v1",
        "inputs":{"diagram_json_sha256":diagram_sha,"face_key_table_sha256":face_sha,
                  "source_audit_schema":source_audit["schema"]},
        "source_scope":{
            "all_order8_source_records":608,"all_source_deletion_diamonds":490,
            "source_diamonds_commuting_by_endpoint_compression":source_diamonds_ok,
            "graph5_graph12_source_records":60,"graph5_graph12_unique_source_diamonds":44,
            "source_diamonds_with_current_geometric_support_lifts":44,
            "source_diamonds_not_represented_by_current_graph5_graph12_candidates":446
        },
        "geometry":{
            "four_support_witnesses":996,"anchored_oriented_boundary_cycles_reconstructed":cycle_checks,
            "open_complementary_arcs_reconstructed":arc_checks,
            "ordered_multi_footprint_words_reconstructed":word_checks,
            "all_15_labelled_intersections_recomputed":intersection_entries,
            "relative_single_deletion_collapse_checks":relative_checks,
            "footprint_count_histogram":[{"footprints":k,"support_boundaries":v} for k,v in sorted(footprint_count_hist.items())],
            "root_preserving_map_swap_symmetry":{
                "coarse_intersection_diagram_invariant_rows":sum(v for (fam,ok),v in map_coarse_swap_counts.items() if ok),
                "coarse_intersection_diagram_noninvariant_rows":sum(v for (fam,ok),v in map_coarse_swap_counts.items() if not ok),
                "ordered_footprint_word_invariant_rows":sum(v for (fam,ok),v in map_word_swap_counts.items() if ok),
                "ordered_footprint_word_noninvariant_rows":sum(v for (fam,ok),v in map_word_swap_counts.items() if not ok),
                "by_family":[{"family":fam,"coarse_invariant":map_coarse_swap_counts[(fam,True)],
                    "coarse_noninvariant":map_coarse_swap_counts[(fam,False)],
                    "ordered_word_invariant":map_word_swap_counts[(fam,True)],
                    "ordered_word_noninvariant":map_word_swap_counts[(fam,False)]}
                    for fam in ("graph5","graph12")]
            },
            "source_witness_map_rows":len(map_rows),
            "parent_port_restriction_checks":parent_restrictions,
            "source_diamond_geometric_lifts":map_diamond_instances,
            "unique_source_diamonds_lifted":len(source_map_keys)
        },
        "collapse_diamonds":{
            "source_map_diamond_instances":sum(pair_set_counts.values()),
            "same_elementary_pair_set":pair_set_counts["same"],
            "same_pair_set_valid_adjacent_swap_normalizations":sum(same_swap_counts.values()),
            "different_elementary_pair_sets":pair_set_counts["different"],
            "different_pair_sets_form_one_connected_alternating_cycle":sum(cycle_counts.values()),
            "alternating_cycle_cell_counts":[{"cells":k,"rows":v} for k,v in sorted(cycle_counts.items())],
            "by_source_graph_family":[{"family":fam,**dict(counts)} for fam,counts in sorted(family_pair_counts.items())],
            "dependency_closed_factorizations":sum(prefix_swap_counts.values()),
            "common_prefix_pair_set_and_intermediate_inventory":sum(prefix_swap_counts.values()),
            "common_extra_pair_set":sum(prefix_swap_counts.values()),
            "both_local_suffixes_replay_to_same_parent":sum(prefix_swap_counts.values()),
            "dependency_closed_suffix_pair_counts":[{"pairs":k,"rows":v} for k,v in sorted(block_counts.items())],
            "common_extra_pair_counts":[{"pairs":k,"rows":v} for k,v in sorted(extra_counts.items())],
            "same_pair_set_swap_count_histogram":[{"swaps":k,"rows":v} for k,v in sorted(same_swap_counts.items())],
            "prefix_normalizing_swap_count_histogram":[{"swaps":k,"rows":v} for k,v in sorted(prefix_swap_counts.items())],
            "order_sensitive_common_extra_pair_order_rows":order_sensitive,
            "order_aligned_common_extra_pair_order_rows":sum(v for (_,_,_,eq),v in extra_order_counts.items() if eq),
            "common_extra_pair_order_templates":[
                {"suffix_pairs":k[0],"left_word":list(k[1]),"right_word":list(k[2]),
                 "order_equal":k[3],"rows":v}
                for k,v in sorted(extra_order_counts.items())
            ]
        },
        "witness_pair_certificates":path_rows,
        "boundary_cycle_certificates":boundary_rows,
        "conclusions":{
            "all_996_witnesses_have_exact_anchored_oriented_boundary_cycles":True,
            "all_996_witnesses_have_exact_ordered_multi_footprint_words":True,
            "all_14940_labelled_intersections_including_empty_are_recomputed":True,
            "all_490_source_side_deletion_diamonds_commute":True,
            "all_44_source_diamonds_in_graph5_graph12_families_have_geometric_lifts":True,
            "all_43696_geometric_collapse_paths_replay":True,
            "all_same_pair_set_diamonds_normalize_by_valid_adjacent_swaps":True,
            "all_different_pair_set_diamonds_are_single_alternating_cycles":True,
            "all_different_pair_set_diamonds_factor_through_common_prefix_and_local_suffix":True,
            "all_446_other_source_diamonds_have_geometric_lifts":False,
            "unique_source_to_target_graph_isomorphism_identified":False,
            "source_prescribed_oriented_boundary_word_authenticated":False,
            "elementary_collapse_map_commutation_as_maps_proved":False,
            "geometric_L8_closed":False
        },
        "nonclaims":[
            "The source exporter supplies interval endpoints, overlap graphs, spanning trees and eligible reverse marks, but no Z5 displacement or source-prescribed oriented boundary word. Both root-preserving graph maps remain admissible.",
            "The 44 geometric source diamonds are precisely those in the graph-5 and graph-12 source families represented by the current four-support candidate inventory. The remaining 446 of the 490 source diamonds belong to other order-eight overlap-graph families and are not geometrically lifted here.",
            "The collapse sequences are deterministic finite free-pair certificates. Their pair-set comparison, alternating-cycle classification and dependency-closed factorization are finite results; no all-orders local switch lemma or natural homotopy of collapse maps is claimed.",
            "No all-orders PF-I16 Hall inequality or geometric L8 theorem follows."
        ]
    }
    a.output.parent.mkdir(parents=True,exist_ok=True)
    a.output.write_text(json.dumps(result,sort_keys=True,indent=2)+"\n")
    print(json.dumps({"source_scope":result["source_scope"],"geometry":result["geometry"],
                      "collapse_diamonds":{k:v for k,v in result["collapse_diamonds"].items()
                                           if k not in ("common_extra_pair_order_templates",)},
                      "conclusions":result["conclusions"]},sort_keys=True,indent=2))

if __name__=="__main__":
    main()
