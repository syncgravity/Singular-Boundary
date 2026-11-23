#!/usr/bin/env python3
"""Artifact-pinned factorization of PF-I16 minimal four-cell alternating switches."""
from __future__ import annotations
import argparse, gzip, hashlib, itertools, json, zipfile
from collections import Counter
from pathlib import Path

HASHES = {
 "collapse": "d0d96755ceaa556759f6d5a2d0f60d0df1cd5f9805b12e5461c6d1747f6f8141",
 "diagrams": "aa2d4ae88b3d23e34007eed45858a54b7d98bfd9fa6c595b11635d04a74817ba",
 "inventory": "5b56a7485c0ab01e76f93868e331a2cb1790df01131d98c33376f7cb6370af4f",
}
def load(path, expected):
    raw=path.read_bytes()
    if zipfile.is_zipfile(path):
        with zipfile.ZipFile(path) as z:
            names=z.namelist(); assert len(names)==1, names
            raw=z.read(names[0])
    if path.suffix==".gz" or raw[:2]==b"\x1f\x8b": raw=gzip.decompress(raw)
    digest=hashlib.sha256(raw).hexdigest(); assert digest==expected,(path,digest,expected)
    return json.loads(raw),digest
def add(a,b): return tuple(x+y for x,y in zip(a,b))
def edge(a,b): return tuple(sorted((tuple(a),tuple(b))))
def face_vertices(r):
    m=tuple(r["lower"]); j,k=r["directions"]
    ej=tuple(int(i==j) for i in range(5)); ek=tuple(int(i==k) for i in range(5))
    return {m,add(m,ej),add(add(m,ej),ek),add(m,ek)}
def face_edges(r):
    v=sorted(face_vertices(r))
    return {edge(a,b) for a,b in itertools.combinations(v,2) if sum(abs(x-y) for x,y in zip(a,b))==1}
def union(ids,fv,fe):
    F=set(ids); return {"F":F,"E":set().union(*(fe[i] for i in F)),"V":set().union(*(fv[i] for i in F))}
def sequence(path):
    out=[]
    for stage in ("first_relative_collapse","second_relative_collapse"):
        for x in path[stage]["face_edge_pairs"]: out.append(("FE",edge(*x["free_edge"]),int(x["removed_face"])))
        for x in path[stage]["edge_vertex_pairs"]: out.append(("EV",tuple(x["free_vertex"]),edge(*x["removed_edge"])))
    return out
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
def dependency_close(seq,start,A,initial,fv,fe):
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
                else:
                    block.add(b); absorbed.append(b)
                changed=True; break
        if not changed:break
    assert replay(seq,start,A,fv,fe)==A
    prefix=[p for p in seq if p not in block]; suffix=[p for p in seq if p in block]
    assert seq==prefix+suffix
    return block,swaps,absorbed,prefix,suffix
def normalize_prefix(left,right,start,intermediate,fv,fe):
    left=list(left); right=list(right)
    if set(left)!=set(right): return None,("prefix-pair-set-mismatch",)
    swaps=0
    for i,want in enumerate(right):
        j=left.index(want,i)
        while j>i:
            a,b=left[j-1],left[j]
            s=replay(left[:j-1],start,intermediate,fv,fe); assert s is not None
            ab1=apply(s,a,intermediate,fv,fe); ab=apply(ab1,b,intermediate,fv,fe) if ab1 is not None else None
            ba1=apply(s,b,intermediate,fv,fe); ba=apply(ba1,a,intermediate,fv,fe) if ba1 is not None else None
            if ab is None or ba is None or ab!=ba:
                return swaps,("noncommuting-prefix-pair",j-1,a,b,ab is not None,ba is not None)
            left[j-1],left[j]=left[j],left[j-1]; swaps+=1; j-=1
    assert left==right and replay(left,start,intermediate,fv,fe)==intermediate
    return swaps,None
def main():
    ap=argparse.ArgumentParser()
    for name in ("collapse","diagrams","inventory"): ap.add_argument("--"+name,required=True,type=Path)
    ap.add_argument("--output",required=True,type=Path); a=ap.parse_args()
    col,ch=load(a.collapse,HASHES["collapse"]); dia,dh=load(a.diagrams,HASHES["diagrams"]); inv,ih=load(a.inventory,HASHES["inventory"])
    fv=[face_vertices(x) for x in inv["face_key_table"]]; fe=[face_edges(x) for x in inv["face_key_table"]]
    lookup={(pi,wi):w for pi,pair in enumerate(dia["per_pair"]) for wi,w in enumerate(pair["graph5_witnesses"])}
    rows=[]; sizes=Counter(); extras=Counter(); extra_words=Counter(); suffix_words=Counter(); prefix_swaps=Counter(); mids=Counter(); witnesses=set()
    for w in col["families"]["graph5"]["witness_results"]:
        pi,wi=w["pair_index"],w["witness_index"]; supports=lookup[(pi,wi)]["support_face_indices"]
        for pm in w["permutation_results"]:
            pmap=pm["source_to_support_isomorphism"]
            for cert in pm["diamond_certificates"]:
                if cert["same_elementary_pair_set"] or cert["source_mark_pair"]!=[1,2]: continue
                L=sequence(cert["path_delete_m_then_n"]); R=sequence(cert["path_delete_n_then_m"])
                diffL=set(L)-set(R); diffR=set(R)-set(L); D=diffL|diffR
                F={p[2] for p in D if p[0]=="FE"}; E={p[1] if p[0]=="FE" else p[2] for p in D}; V={p[1] for p in D if p[0]=="EV"}
                if (len(F),len(E),len(V),len(D))!=(1,2,1,4): continue
                rem={pmap[i] for i in cert["source_mark_pair"]}; keep=[i for i in range(4) if i not in rem]
                A=union(set().union(*(set(supports[i]) for i in keep)),fv,fe)
                X=union(set().union(*(set(supports[i]) for i in range(4))),fv,fe)
                assert replay(L,X,A,fv,fe)==A and replay(R,X,A,fv,fe)==A
                BL,swL,abL,pL,sufL=dependency_close(L,X,A,diffL,fv,fe)
                BR,swR,abR,pR,sufR=dependency_close(R,X,A,diffR,fv,fe)
                extraL,extraR=BL-diffL,BR-diffR
                assert extraL==extraR and set(pL)==set(pR)
                midL=replay(pL,X,A,fv,fe); midR=replay(pR,X,A,fv,fe)
                assert midL is not None and midL==midR
                assert replay(sufL,midL,A,fv,fe)==A and replay(sufR,midR,A,fv,fe)==A
                psw,err=normalize_prefix(pL,pR,X,midL,fv,fe); assert err is None and psw is not None
                assert set(sufL)-set(sufR)==diffL and set(sufR)-set(sufL)==diffR
                orderL=[p for p in sufL if p in extraL]; orderR=[p for p in sufR if p in extraR]
                sizes[len(BL)]+=1; extras[len(extraL)]+=1
                extra_words[("".join(p[0] for p in orderL),"".join(p[0] for p in orderR))]+=1
                suffix_words[(len(BL),"".join(p[0] for p in sufL),"".join(p[0] for p in sufR))]+=1
                prefix_swaps[psw]+=1; mids[(len(midL["F"]),len(midL["E"]),len(midL["V"]))]+=1; witnesses.add(w["witness_id"])
                rows.append({"pair_index":pi,"witness_index":wi,"witness_id":w["witness_id"],"root_preserving_map":pmap,
                    "dependency_closed_suffix_pairs":{"left":len(BL),"right":len(BR)},"common_extra_pairs":len(extraL),
                    "common_extra_order_equal":orderL==orderR,"left_suffix_pair_word":[p[0] for p in sufL],
                    "right_suffix_pair_word":[p[0] for p in sufR],"prefix_normalizing_valid_swaps":psw,
                    "same_prefix_pair_set":True,"same_intermediate_inventory":True,
                    "intermediate_inventory_counts":{"faces":len(midL["F"]),"edges":len(midL["E"]),"vertices":len(midL["V"])},
                    "both_suffixes_replay_to_grandparent":True})
    assert len(rows)==64 and len(witnesses)==32
    assert sizes==Counter({4:16,6:8,7:24,10:16}) and extras==Counter({2:16,4:8,5:24,8:16})
    assert sum(v for k,v in extra_words.items() if k[0]==k[1])==56
    assert sum(v for k,v in extra_words.items() if k[0]!=k[1])==8
    result={"schema":"PF-I16-FOUR-CELL-ALTERNATING-SWITCH-FACTORIZATION-v1",
      "inputs":{"collapse_payload_sha256":ch,"diagrams_payload_sha256":dh,"inventory_payload_sha256":ih},
      "scope":"64 graph-5 Ngrid=12 minimal four-cell certificates; source marks [1,2]; both root-preserving maps; immutable artifacts",
      "counts":{"certificate_map_rows":64,"distinct_geometric_witnesses":32,
        "dependency_closed_suffix_pair_counts":[{"pairs":k,"count":v} for k,v in sorted(sizes.items())],
        "common_extra_pair_counts":[{"pairs":k,"count":v} for k,v in sorted(extras.items())],
        "common_extra_order_words":[{"left":k[0],"right":k[1],"count":v} for k,v in sorted(extra_words.items())],
        "left_right_suffix_words":[{"pairs":k[0],"left":k[1],"right":k[2],"count":v} for k,v in sorted(suffix_words.items())],
        "prefix_normalizing_valid_swap_counts":[{"swaps":k,"count":v} for k,v in sorted(prefix_swaps.items())],
        "intermediate_inventory_counts":[{"faces":k[0],"edges":k[1],"vertices":k[2],"count":v} for k,v in sorted(mids.items())],
        "same_prefix_pair_sets":64,"same_intermediate_inventories":64,"prefixes_normalized_by_valid_swaps":64,
        "both_local_suffixes_replay_to_grandparent":64,"common_extra_order_equal":56,"common_extra_order_different":8},
      "conclusions":{"each_path_factors_into_a_prefix_and_dependency_closed_local_switch_suffix":True,
        "prefixes_have_same_pair_set_and_same_intermediate_inventory":True,
        "prefixes_are_related_by_valid_adjacent_collapse_commutations":True,
        "suffix_pair_sets_differ_only_by_original_four_alternating_pairs":True,
        "common_extra_suffix_pair_sets_agree_in_all_rows":True,
        "eight_rows_require_a_larger_order_sensitive_switch_template":True,
        "finite_switch_factorization_not_restriction_naturality":True,"geometric_L8_closed":False},"rows":rows}
    a.output.write_text(json.dumps(result,indent=2,sort_keys=True)+"\n",encoding="utf-8")
    print(json.dumps(result["counts"],sort_keys=True))
if __name__=="__main__":main()
