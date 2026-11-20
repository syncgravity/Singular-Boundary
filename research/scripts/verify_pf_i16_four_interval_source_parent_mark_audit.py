#!/usr/bin/env python3
"""Audit legal deletion marks and every induced parent tree for graph-5 / graph-12."""
from __future__ import annotations
import argparse, collections, hashlib, json
from pathlib import Path
import export_pf_i16_hall_source_records as hall

G5=frozenset({(0,1),(0,2),(0,3),(1,2)})
G12=frozenset({(0,1),(0,2),(1,2),(1,3),(2,3)})

def graph(row):
    return frozenset(tuple(e) for e in row["full_overlap_edges"])

def summarize(rows):
    root_hist=collections.Counter(r["root_interval_index"] for r in rows)
    mark_hist=collections.Counter()
    other_marks=collections.Counter()
    parent_tree_hist=collections.Counter()
    source_ids=[]
    for i,r in enumerate(rows):
        marks=tuple(r["eligible_reverse_marks"])
        mark_hist.update(marks)
        if 3 in marks:
            other=tuple(x for x in marks if x!=3)
            other_marks[other]+=1
            p=next(x for x in r["parents"] if x["deleted_interval_index"]==3)
            parent_tree_hist[tuple(tuple(e) for e in p["parent_tree_edges"])]+=1
            source_ids.append({
                "source_index":i,
                "intervals":r["intervals"],
                "tree_edges":r["tree_edges"],
                "eligible_marks":marks,
                "parent_after_delete_3":p["parent_intervals"],
                "parent_tree_after_delete_3":p["parent_tree_edges"]
            })
    return {
        "source_count":len(rows),
        "root_index_histogram":dict(sorted(root_hist.items())),
        "eligible_mark_histogram":dict(sorted(mark_hist.items())),
        "sources_with_mark_3":len(source_ids),
        "other_eligible_marks_when_3_is_eligible":dict(sorted((str(k),v) for k,v in other_marks.items())),
        "parent_tree_after_delete_3_histogram":dict(sorted((str(k),v) for k,v in parent_tree_hist.items())),\n        "parent_tree_after_delete_3_is_not_unique":len(parent_tree_hist)>1,
        "source_rows_with_mark_3":source_ids
    }

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--output",type=Path,required=True)
    a=p.parse_args()
    rows=hall.source_records(8)
    g5=summarize([r for r in rows if graph(r)==G5])
    g12=summarize([r for r in rows if graph(r)==G12])
    assert len(rows)==608
    assert g5["source_count"]==12 and g5["sources_with_mark_3"]==12
    assert g12["source_count"]==48 and g12["sources_with_mark_3"]==36
    assert g5["root_index_histogram"]=={0:12}
    assert g12["root_index_histogram"]=={0:48}
    assert g5["other_eligible_marks_when_3_is_eligible"]=={"(1, 2)":4,"(1,)":4,"(2,)":4}
    assert g12["other_eligible_marks_when_3_is_eligible"]=={"()":12,"(1,)":12,"(2,)":12}
    assert g5["parent_tree_after_delete_3_histogram"]=={\n        "((0, 1), (0, 2))":4,\n        "((0, 1), (1, 2))":4,\n        "((0, 2), (1, 2))":4\n    }
    assert g12["parent_tree_after_delete_3_histogram"]=={\n        "((0, 1), (0, 2))":12,\n        "((0, 1), (1, 2))":12,\n        "((0, 2), (1, 2))":12\n    }
    result={
        "schema":"PF-I16-FOUR-INTERVAL-SOURCE-PARENT-MARK-AUDIT-v1",
        "source_record_canonical_payload_sha256":hall.build([8])["sha256_canonical_payload"],
        "order_eight_source_count":len(rows),
        "graph5":g5,
        "graph12":g12,
        "conclusion":{
            "interval_0_is_root_and_never_an_eligible_reverse_mark":True,
            "drop_0_relative_collapse_is_not_a_source_parent_requirement":True,
            "all_actual_co-deletions_with_interval_3_are_interval_1_or_2":True,
            "existing_triple_verifier_checks_drop_1_and_drop_2":True
        },
        "nonclaims":[
            "This audits source deletion marks and parent trees, not the target support-to-source embedding for every surviving edge quadruple.",
            "It does not compare the exported four-support incidence diagrams with all source-parent diagrams.",
            "It does not certify L7b boundary words or restriction coherence."
        ]
    }
    a.output.parent.mkdir(parents=True,exist_ok=True)
    a.output.write_text(json.dumps(result,sort_keys=True,indent=2)+"\n")
    print(json.dumps({k:v for k,v in result.items() if k not in ("graph5","graph12")},sort_keys=True,indent=2))
    print(json.dumps({"graph5":{k:v for k,v in g5.items() if k!="source_rows_with_mark_3"},
                      "graph12":{k:v for k,v in g12.items() if k!="source_rows_with_mark_3"}},sort_keys=True,indent=2))
if __name__=="__main__":
    main()
