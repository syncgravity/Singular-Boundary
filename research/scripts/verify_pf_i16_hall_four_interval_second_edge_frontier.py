#!/usr/bin/env python3
"""First-edge-anchored frontier for a demand-independent four-interval motif.

Enumerates every second matched edge in the Ngrid=12 accepted target that can
form a valid two-interval parent with the fixed first edge, retaining every
support-pair witness. This is a target-only necessary-condition stage before
the more expensive triangle and graph-5/graph-12 fourth-edge search.

No Hall demands, loads, deficiencies, matching outcomes, or flows are read.
"""
from __future__ import annotations
import argparse, hashlib, json
from collections import defaultdict
from pathlib import Path
import verify_pf_i16_hall_four_interval_parent_compatibility as geom

def edge_key(row):
    return (tuple(row["lower"]), tuple(row["upper"]))

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--inventory",type=Path,required=True)
    ap.add_argument("--output",type=Path,required=True)
    a=ap.parse_args()
    inv=json.loads(a.inventory.read_text())
    fv,fe,options,_=geom.build_target(inv)
    cells,union,intersection,collapse,point_contractible,edge_contractible,footprint=geom.make_geometry(fv,fe)
    e1=edge_key(inv["fixed_triple_edges"][0])
    endpoints=set(e1)
    def edge_collapse(s,e):
        f,ed,v=cells(tuple(sorted(s)))
        target=tuple(sorted(e))
        return collapse((set(f),set(ed),set(v)),(set(),{target},set(target)))
    first=[]
    for i,s in enumerate(options[e1]):
        if edge_collapse(s,e1):
            first.append((i,s,cells(tuple(sorted(s)))))
    candidate_rows=[]
    pair_count=0
    for e2 in sorted(options):
        if e2==e1 or endpoints.intersection(e2):
            continue
        witnesses=[]
        for i,s1,c1 in first:
            for j,s2 in enumerate(options[e2]):
                if not edge_collapse(s2,e2):
                    continue
                c2=cells(tuple(sorted(s2)))
                # Fast exact intersection prefilter before collapse/arc tests.
                if not (c1[2] & c2[2]):
                    continue
                common=intersection([s1,s2])
                if not common[2] or not point_contractible(common):
                    continue
                if not footprint(s1,s2,e1) or not footprint(s2,s1,e2):
                    continue
                witnesses.append({"first_support_index":i,"second_support_index":j})
        if witnesses:
            pair_count += len(witnesses)
            candidate_rows.append({
                "second_edge":{"lower":list(e2[0]),"upper":list(e2[1])},
                "support_pair_witness_count":len(witnesses),
                "support_pair_witnesses":witnesses
            })
    edge_lines=[]
    for row in candidate_rows:
        e=row["second_edge"]
        edge_lines.append(",".join(map(str,e["lower"]))+"->"+",".join(map(str,e["upper"])))
    digest=hashlib.sha256(("\\n".join(edge_lines)+"\\n").encode()).hexdigest()
    result={
      "schema":"PF-I16-HALL-FOUR-INTERVAL-SECOND-EDGE-FRONTIER-v1",
      "target":inv["target"],
      "fixed_first_edge":{"lower":list(e1[0]),"upper":list(e1[1])},
      "eligible_second_edge_count":len(options)-1,
      "first_edge_support_options":len(options[e1]),
      "first_edge_support_options_collapsing_to_matched_edge":len(first),
      "second_edges_with_parent_compatible_support_pair":len(candidate_rows),
      "total_parent_compatible_support_pair_witnesses":pair_count,
      "candidate_second_edge_sha256":digest,
      "candidate_second_edges":candidate_rows,
      "filters":[
        "Second matched edge is vertex-disjoint from the fixed first matched edge.",
        "Both supports are connected simple-boundary inventory supports and collapse to their distinguished matched edge.",
        "Their intersection is nonempty and collapses to a vertex.",
        "The shared footprint is a single boundary cell on both open complementary arcs."
      ],
      "nonclaims":[
        "No third edge or fourth edge is selected in this frontier stage.",
        "No Hall demands, loads, deficiencies, matching outcomes, or flows are read.",
        "This is not a four-interval L6c/L7b certificate or an all-orders lift."
      ]
    }
    a.output.parent.mkdir(parents=True,exist_ok=True)
    a.output.write_text(json.dumps(result,sort_keys=True,indent=2)+"\\n")
    print(json.dumps({k:v for k,v in result.items() if k!="candidate_second_edges"},sort_keys=True,indent=2))

if __name__=="__main__":
    main()
