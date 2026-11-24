#!/usr/bin/env python3
"""Artifact-pinned dependency-closed common-suffix audit for PF-I16 four-cell cases."""
from __future__ import annotations
import argparse, gzip, hashlib, itertools, json, zipfile
from collections import Counter
from pathlib import Path

HASHES = {
 "collapse": "d0d96755ceaa556759f6d5a2d0f60d0df1cd5f9805b12e5461c6d1747f6f8141",
 "diagrams": "aa2d4ae88b3d23e34007eed45858a54b7d98bfd9fa6c595b11635d04a74817ba",
 "inventory": ("5b56a7485c0ab01e76f93868e331a2cb1790df01131d98c33376f7cb6370af4f", "3e50240bf1b037f3de8dd4e4c4ab94d4523533c25ceeab4000410c641cf07b77"),
}
def load(path, expected):
    raw=path.read_bytes()
    if zipfile.is_zipfile(path):
        with zipfile.ZipFile(path) as z:
            names=z.namelist(); assert len(names)==1, names
            raw=z.read(names[0])
    if path.suffix==".gz" or raw[:2]==b"\x1f\x8b": raw=gzip.decompress(raw)
    digest=hashlib.sha256(raw).hexdigest(); assert (digest in expected if isinstance(expected, (tuple, list, set)) else digest == expected),(path,digest,expected)
    return json.loads(raw),digest
def add(a,b): return tuple(x+y for x,y in zip(a,b))
def edge(a,b): return tuple(sorted((tuple(a),tuple(b))))
def fv_of(r):
    m=tuple(r["lower"]); j,k=r["directions"]
    ej=tuple(int(i==j) for i in range(5)); ek=tuple(int(i==k) for i in range(5))
    return {m,add(m,ej),add(add(m,ej),ek),add(m,ek)}
def fe_of(r):
    v=sorted(fv_of(r))
    return {edge(a,b) for a,b in itertools.combinations(v,2) if sum(abs(x-y) for x,y in zip(a,b))==1}
def union(ids,fv,fe):
    F=set(ids); return {"F":F,"E":set().union(*(fe[i] for i in F)),"V":set().union(*(fv[i] for i in F))}
def path_pairs(path):
    out=[]
    for stage in ("first_relative_collapse","second_relative_collapse"):
        for x in path[stage]["face_edge_pairs"]: out.append(("FE",edge(*x["free_edge"]),int(x["removed_face"])))
        for x in path[stage]["edge_vertex_pairs"]: out.append(("EV",tuple(x["free_vertex"]),edge(*x["removed_edge"])))
    return out
def paired_edge(p): return p[1] if p[0]=="FE" else p[2]
def apply(s,p,A,fv,fe):
    F,E,V=set(s["F"]),set(s["E"]),set(s["V"])
    if p[0]=="FE":
        _,e,f=p; inc={q for q in F if e in fe[q]}
        if e not in E or f not in F or e in A["E"] or f in A["F"] or inc!={f}: return None
        F.remove(f); E.remove(e)
    else:
        _,v,e=p; ie={q for q in E if v in q}; iff={q for q in F if v in fv[q]}
        if v not in V or e not in E or v in A["V"] or e in A["E"] or ie!={e} or iff: return None
        E.remove(e); V.remove(v)
    return {"F":F,"E":E,"V":V}
def replay(seq,start,A,fv,fe):
    s={k:set(v) for k,v in start.items()}
    for p in seq:
        s=apply(s,p,A,fv,fe)
        if s is None:return None
    return s
def first_blocker(seq,start,A,P,fv,fe):
    seq=list(seq); swaps=0
    for right in range(len(seq)-1,0,-1):
        for j in range(right):
            if paired_edge(seq[j]) in P and paired_edge(seq[j+1]) not in P:
                a,b=seq[j],seq[j+1]; s=replay(seq[:j],start,A,fv,fe); assert s is not None
                ab1=apply(s,a,A,fv,fe); ab=apply(ab1,b,A,fv,fe) if ab1 is not None else None
                ba1=apply(s,b,A,fv,fe); ba=apply(ba1,a,A,fv,fe) if ba1 is not None else None
                if ab is None or ba is None or ab!=ba:return (a,b),swaps
                seq[j],seq[j+1]=b,a; swaps+=1
    return None,swaps
def close_block(seq,start,A,initial,fv,fe):
    seq=list(seq); block=set(initial); swaps=0; absorbed=[]
    while True:
        changed=False
        for j in range(len(seq)-1):
            if seq[j] in block and seq[j+1] not in block:
                a,b=seq[j],seq[j+1]; s=replay(seq[:j],start,A,fv,fe); assert s is not None
                ab1=apply(s,a,A,fv,fe); ab=apply(ab1,b,A,fv,fe) if ab1 is not None else None
                ba1=apply(s,b,A,fv,fe); ba=apply(ba1,a,A,fv,fe) if ba1 is not None else None
                if ab is not None and ba is not None and ab==ba:
                    seq[j],seq[j+1]=b,a; swaps+=1
                else:block.add(b); absorbed.append(b)
                changed=True; break
        if not changed:break
    assert replay(seq,start,A,fv,fe)==A
    prefix=[p for p in seq if p not in block]; suffix=[p for p in seq if p in block]
    assert seq==prefix+suffix
    return block,swaps,absorbed,prefix,suffix

def main():
    ap=argparse.ArgumentParser()
    for name in ("collapse","diagrams","inventory"): ap.add_argument("--"+name,required=True,type=Path)
    ap.add_argument("--output",required=True,type=Path); a=ap.parse_args()
    col,ch=load(a.collapse,HASHES["collapse"]); dia,dh=load(a.diagrams,HASHES["diagrams"]); inv,ih=load(a.inventory,HASHES["inventory"])
    fv=[fv_of(x) for x in inv["face_key_table"]]; fe=[fe_of(x) for x in inv["face_key_table"]]
    lookup={(pi,wi):w for pi,pair in enumerate(dia["per_pair"]) for wi,w in enumerate(pair["graph5_witnesses"])}
    rows=[]; sizes=Counter(); words=Counter(); blockers=Counter(); mids=Counter(); swaps=Counter(); witnesses=set()
    for w in col["families"]["graph5"]["witness_results"]:
        pi,wi=w["pair_index"],w["witness_index"]; supports=lookup[(pi,wi)]["support_face_indices"]
        for pm in w["permutation_results"]:
            pmap=pm["source_to_support_isomorphism"]
            for cert in pm["diamond_certificates"]:
                if cert["same_elementary_pair_set"] or cert["source_mark_pair"]!=[1,2]:continue
                L=path_pairs(cert["path_delete_m_then_n"]); R=path_pairs(cert["path_delete_n_then_m"]); D=set(L)^set(R)
                F={p[2] for p in D if p[0]=="FE"}; E={p[1] if p[0]=="FE" else p[2] for p in D}; V={p[1] for p in D if p[0]=="EV"}
                if (len(F),len(E),len(V),len(D))!=(1,2,1,4):continue
                P=fe[next(iter(F))]-E; assert len(P)==2
                rem={pmap[i] for i in cert["source_mark_pair"]}; keep=[i for i in range(4) if i not in rem]
                A=union(set().union(*(set(supports[i]) for i in keep)),fv,fe)
                X=union(set().union(*(set(supports[i]) for i in range(4))),fv,fe)
                P_ops={p for p in L if paired_edge(p) in P}; assert len(P_ops)==2 and P_ops=={p for p in R if paired_edge(p) in P}
                bL,_=first_blocker(L,X,A,P,fv,fe); bR,_=first_blocker(R,X,A,P,fv,fe)
                assert (bL is None)==(bR is None) and bL==bR
                initial=P_ops if bL is None else P_ops|{bL[1]}
                if bL is not None:blockers[(bL[0][0],bL[1][0])]+=1
                BL,sL,aL,pL,sufL=close_block(L,X,A,initial,fv,fe)
                BR,sR,aR,pR,sufR=close_block(R,X,A,initial,fv,fe)
                assert BL==BR and sufL==sufR
                midL=replay(pL,X,A,fv,fe); midR=replay(pR,X,A,fv,fe)
                assert midL is not None and midL==midR
                assert replay(sufL,midL,A,fv,fe)==A
                assert len(D-BL)==4
                sizes[len(BL)]+=1; words[(len(BL),"".join(p[0] for p in sufL))]+=1
                mids[(len(midL["F"]),len(midL["E"]),len(midL["V"]))]+=1; swaps[(sL,sR)]+=1
                witnesses.add(w["witness_id"])
                rows.append({"pair_index":pi,"witness_index":wi,"witness_id":w["witness_id"],
                    "root_preserving_map":pmap,"dependency_closed_pair_count":len(BL),
                    "common_suffix_pair_word":[p[0] for p in sufL],"valid_adjacent_swaps":{"left":sL,"right":sR},
                    "absorbed_dependency_pairs":{"left":len(aL),"right":len(aR)},
                    "same_ordered_suffix":True,"same_intermediate_inventory":True,
                    "intermediate_inventory_counts":{"faces":len(midL["F"]),"edges":len(midL["E"]),"vertices":len(midL["V"])},
                    "alternating_cycle_pairings_remain_in_prefix":True,"prefix_pair_sets_equal":set(pL)==set(pR)})
    assert len(rows)==64 and len(witnesses)==32
    assert sizes==Counter({2:16,4:8,5:24,8:16}) and sum(blockers.values())==48
    assert all(not r["prefix_pair_sets_equal"] for r in rows)
    result={"schema":"PF-I16-FOUR-CELL-DEPENDENCY-CLOSED-COMMON-SUFFIX-v1",
      "inputs":{"collapse_payload_sha256":ch,"diagrams_payload_sha256":dh,"inventory_payload_sha256":ih},
      "scope":"64 graph-5 Ngrid=12 minimal four-cell certificates; source marks [1,2]; both root-preserving maps; immutable inputs",
      "counts":{"certificate_map_rows":64,"distinct_geometric_witnesses":32,
        "dependency_closed_block_sizes":[{"pair_operations":k,"count":v} for k,v in sorted(sizes.items())],
        "first_blocker_types":[{"P_operation":k[0],"interfering_operation":k[1],"count":v} for k,v in sorted(blockers.items())],
        "common_suffix_words":[{"pair_count":k[0],"word":k[1],"count":v} for k,v in sorted(words.items())],
        "intermediate_inventory_counts":[{"faces":k[0],"edges":k[1],"vertices":k[2],"count":v} for k,v in sorted(mids.items())],
        "valid_adjacent_swap_count_pairs":[{"left":k[0],"right":k[1],"count":v} for k,v in sorted(swaps.items())],
        "common_ordered_suffixes":64,"same_intermediate_inventories":64,
        "prefix_pair_sets_still_differ":64,"alternating_cycle_pairings_not_absorbed":64},
      "conclusions":{"all_64_cases_have_dependency_closed_common_ordered_suffix":True,
        "all_moves_use_certified_valid_adjacent_swaps":True,"both_prefixes_reach_same_intermediate_inventory":True,
        "alternating_cycle_pairings_remain_in_prefix":True,
        "this_factors_common_continuation_but_does_not_compare_prefix_collapse_maps":True,
        "global_restriction_naturality_not_proved":True,"geometric_L8_closed":False},"rows":rows}
    a.output.write_text(json.dumps(result,indent=2,sort_keys=True)+"\n",encoding="utf-8")
    print(json.dumps(result["counts"],sort_keys=True))
if __name__=="__main__":main()
