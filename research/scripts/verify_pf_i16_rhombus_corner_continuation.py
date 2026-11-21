#!/usr/bin/env python3
"""Replay the common continuation of the 64 minimal PF-I16 rhombus-corner cases.

Inputs are the three immutable workflow artifacts: collapse diamonds, independent
four-support diagrams, and the Ngrid=12 accepted-face inventory. This is an
artifact-level finite check; it does not prove a global collapse-map homotopy or L8.
"""
from __future__ import annotations
import argparse, gzip, hashlib, itertools, json, zipfile
from collections import Counter
from pathlib import Path

EXPECTED = {
    "collapse_zip": "a717a6ef2e1006225f31ef64b5a22033e2305b8bfe8fec53e3e3c2a885f6adbf",
    "diagrams_zip": "5761aef67b7ede6d8580eefff60a422307d2d69eefd3a18382c56b36e3372903",
    "inventory_zip": "82a493237a7d20e74d17e1d4b563e0fde3143d33989b6515d426fb24237afc94",
}

def load_zip(path: Path, expected: str, gzip_member: bool=False):
    raw_zip = path.read_bytes()
    digest = hashlib.sha256(raw_zip).hexdigest()
    if digest != expected:
        raise AssertionError((str(path), digest, expected))
    with zipfile.ZipFile(path) as z:
        names = z.namelist()
        if len(names) != 1:
            raise AssertionError((str(path), names))
        payload = z.read(names[0])
    if gzip_member:
        payload = gzip.decompress(payload)
    return json.loads(payload), hashlib.sha256(payload).hexdigest()

def add(a,b): return tuple(x+y for x,y in zip(a,b))
def edge_key(a,b): return tuple(sorted((tuple(a),tuple(b))))
def face_vertices(row):
    m=tuple(row["lower"]); j,k=row["directions"]
    ej=tuple(int(i==j) for i in range(5)); ek=tuple(int(i==k) for i in range(5))
    return {m,add(m,ej),add(add(m,ej),ek),add(m,ek)}
def face_edges(row):
    vs=sorted(face_vertices(row))
    return {edge_key(a,b) for a,b in itertools.combinations(vs,2)
            if sum(abs(x-y) for x,y in zip(a,b))==1}
def support_cells(face_ids, fv, fe):
    fs=set(face_ids); es=set().union(*(fe[i] for i in fs)); vs=set().union(*(fv[i] for i in fs))
    return fs,es,vs

def typed_pairs(path):
    out=[]
    for stage in ("first_relative_collapse","second_relative_collapse"):
        c=path[stage]
        for x in c["face_edge_pairs"]:
            out.append(("FE",edge_key(*x["free_edge"]),int(x["removed_face"])))
        for x in c["edge_vertex_pairs"]:
            out.append(("EV",tuple(x["free_vertex"]),edge_key(*x["removed_edge"])))
    return out

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--collapse",type=Path,required=True)
    ap.add_argument("--diagrams",type=Path,required=True)
    ap.add_argument("--inventory",type=Path,required=True)
    ap.add_argument("--output",type=Path,required=True)
    a=ap.parse_args()
    collapse,ch=load_zip(a.collapse,EXPECTED["collapse_zip"],True)
    diagrams,dh=load_zip(a.diagrams,EXPECTED["diagrams_zip"])
    inventory,ih=load_zip(a.inventory,EXPECTED["inventory_zip"])
    table=inventory["face_key_table"]
    fv=[face_vertices(x) for x in table]
    fe=[face_edges(x) for x in table]
    diagram_lookup={(pi,wi):w for pi,pair in enumerate(diagrams["per_pair"])
                    for wi,w in enumerate(pair["graph5_witnesses"])}
    count=0; witnesses=set(); pair_types=Counter(); intersection_types=Counter()
    rows=[]
    for witness in collapse["families"]["graph5"]["witness_results"]:
        pi,wi=witness["pair_index"],witness["witness_index"]
        dw=diagram_lookup[(pi,wi)]
        supports=dw["support_face_indices"]
        for perm in witness["permutation_results"]:
            pmap=perm["source_to_support_isomorphism"]
            for cert in perm["diamond_certificates"]:
                if cert["same_elementary_pair_set"] or cert["source_mark_pair"] != [1,2]:
                    continue
                left=typed_pairs(cert["path_delete_m_then_n"])
                right=typed_pairs(cert["path_delete_n_then_m"])
                diff=set(left)^set(right)
                faces={x[2] for x in diff if x[0]=="FE"}
                edges={x[1] if x[0]=="FE" else x[2] for x in diff}
                vertices={x[1] for x in diff if x[0]=="EV"}
                if (len(faces),len(edges),len(vertices),len(diff)) != (1,2,1,4):
                    continue
                face=next(iter(faces)); P=fe[face]-edges
                if len(P)!=2: raise AssertionError((pi,wi,"P not two-edge arc",P))
                removed={pmap[i] for i in cert["source_mark_pair"]}
                retained=[i for i in range(4) if i not in removed]
                A=support_cells(set().union(*(set(supports[i]) for i in retained)),fv,fe)
                P_vertices=set().union(*(set(e) for e in P))
                A_intersection_edges=P & A[1]
                A_intersection_vertices=P_vertices & A[2]
                if A_intersection_edges or len(A_intersection_vertices)!=1:
                    raise AssertionError((pi,wi,"unexpected P/A intersection",A_intersection_edges,A_intersection_vertices))
                def P_restriction(seq):
                    return [x for x in seq if (x[1] if x[0]=="FE" else x[2]) in P]
                pleft=P_restriction(left); pright=P_restriction(right)
                if pleft != pright:
                    raise AssertionError((pi,wi,"P-edge collapse restrictions differ",pleft,pright))
                removed_P_edges={x[1] if x[0]=="FE" else x[2] for x in pleft}
                if removed_P_edges != P or len(pleft)!=2:
                    raise AssertionError((pi,wi,"P not completely removed once",P,pleft))
                count+=1; witnesses.add(witness["witness_id"])
                pair_types[tuple(x[0] for x in pleft)]+=1
                intersection_types[(len(A_intersection_edges),len(A_intersection_vertices))]+=1
                rows.append({"pair_index":pi,"witness_index":wi,"source_mark_pair":[1,2],
                             "root_preserving_map":pmap,"rhombus_face":face,
                             "complementary_arc_edges":[[list(x),list(y)] for x,y in sorted(P)],
                             "grandparent_support_labels":retained,
                             "arc_grandparent_intersection_vertex":list(next(iter(A_intersection_vertices))),
                             "common_arc_collapse_pairs":[
                                 ({"type":"face-edge","free_edge":[list(x[1][0]),list(x[1][1])],"removed_face":x[2]}
                                  if x[0]=="FE" else
                                  {"type":"edge-vertex","free_vertex":list(x[1]),"removed_edge":[list(x[2][0]),list(x[2][1])]}) for x in pleft]})
    if count!=64 or len(witnesses)!=32:
        raise AssertionError(("unexpected four-cell case census",count,len(witnesses)))
    result={"schema":"PF-I16-RHOMBUS-CORNER-COMMON-CONTINUATION-v1",
      "inputs":{"collapse_zip_sha256":EXPECTED["collapse_zip"],"collapse_payload_sha256":ch,
                 "independent_diagrams_zip_sha256":EXPECTED["diagrams_zip"],"independent_diagrams_payload_sha256":dh,
                 "support_inventory_zip_sha256":EXPECTED["inventory_zip"],"support_inventory_payload_sha256":ih},
      "scope":"64 graph-5 Ngrid=12 four-cell alternating-cycle certificates, source marks [1,2], both root-preserving graph maps; 32 distinct geometric witnesses represented twice",
      "counts":{"certificates":count,"distinct_geometric_witnesses":len(witnesses),
                "identical_ordered_P_edge_collapse_restrictions":count,
                "P_edge_pair_type_histogram":[{"types":list(k),"count":v} for k,v in sorted(pair_types.items())],
                "P_grandparent_intersection_histogram":[{"edges":k[0],"vertices":k[1],"count":v} for k,v in sorted(intersection_types.items())]},
      "conclusions":{"complementary_arc_is_not_retained_as_edges_in_grandparent":True,
        "complementary_arc_meets_grandparent_in_exactly_one_vertex":True,
        "both_paths_remove_the_two_arc_edges_in_the_same_order_with_the_same_pairing":True,
        "this_identifies_a_common_local_continuation_candidate":True,
        "common_suffix_after_reordering_interleaved_collapses_not_proved":True,
        "global_restriction_naturality_not_proved":True,"geometric_L8_closed":False},
      "rows":rows}
    a.output.write_text(json.dumps(result,indent=2,sort_keys=True)+"\n")
    print(json.dumps({"certificates":count,"distinct_witnesses":len(witnesses),
      "pair_types":[{"types":list(k),"count":v} for k,v in sorted(pair_types.items())],
      "P_intersection_types":[{"edges":k[0],"vertices":k[1],"count":v} for k,v in sorted(intersection_types.items())],
      "common_ordered_arc_collapse":count},sort_keys=True))
if __name__=="__main__":main()
