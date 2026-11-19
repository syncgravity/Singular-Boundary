#!/usr/bin/env python3
"""Canonical Hall source records for the PF-I16 incidence-lift checks.

Enumerates perfect matchings on ordered ports, the strict-interior overlap
graph, all of its spanning trees, and every eligible non-root leaf mark.
No Hall loads, matchings, target geometry, or observer data are consulted.
"""
from __future__ import annotations
import argparse, hashlib, itertools, json
from collections import Counter
from pathlib import Path

def perfect_matchings(ports):
    if not ports:
        yield ()
        return
    a=ports[0]
    for k in range(1,len(ports)):
        b=ports[k]
        for tail in perfect_matchings(ports[1:k]+ports[k+1:]):
            yield ((a,b),)+tail

def is_tree(vertices, edges):
    if len(vertices)==1:
        return len(edges)==0
    if len(edges)!=len(vertices)-1:
        return False
    adj={v:set() for v in vertices}
    for a,b in edges:
        adj[a].add(b); adj[b].add(a)
    seen={vertices[0]}; stack=[vertices[0]]
    while stack:
        x=stack.pop()
        for y in adj[x]-seen:
            seen.add(y); stack.append(y)
    return len(seen)==len(vertices)

def source_records(n):
    if n<2 or n%2:
        raise ValueError("n must be a positive even integer")
    records=[]
    for raw in perfect_matchings(tuple(range(1,n+1))):
        intervals=tuple(sorted(raw))
        s=len(intervals)
        overlap=[(i,j) for i,j in itertools.combinations(range(s),2)
                 if max(intervals[i][0],intervals[j][0]) < min(intervals[i][1],intervals[j][1])]
        trees=[()] if s==1 else [e for e in itertools.combinations(overlap,s-1)
                                  if is_tree(list(range(s)),e)]
        for tree in trees:
            adjacency={i:set() for i in range(s)}
            for a,b in tree:
                adjacency[a].add(b); adjacency[b].add(a)
            root=next(i for i,I in enumerate(intervals) if I[0]==1)
            marks=[i for i in range(s) if i!=root and len(adjacency[i])==1]
            row={"ports":list(range(1,n+1)),
                 "intervals":[list(I) for I in intervals],
                 "full_overlap_edges":[list(e) for e in overlap],
                 "root_interval_index":root,
                 "tree_edges":[list(e) for e in tree],
                 "eligible_reverse_marks":marks,
                 "parents":[]}
            for mark in marks:
                deleted=set(intervals[mark])
                retained=[p for p in range(1,n+1) if p not in deleted]
                compression={p:i+1 for i,p in enumerate(retained)}
                parent_intervals=tuple(sorted(
                    (compression[a],compression[b])
                    for i,(a,b) in enumerate(intervals) if i!=mark))
                old_indices=[i for i in range(s) if i!=mark]
                old_to_new={old:new for new,old in enumerate(old_indices)}
                parent_tree=sorted(
                    [old_to_new[a],old_to_new[b]]
                    for a,b in tree if a!=mark and b!=mark)
                parent_overlap=[[i,j] for i,j in itertools.combinations(range(s-1),2)
                    if max(parent_intervals[i][0],parent_intervals[j][0])
                       < min(parent_intervals[i][1],parent_intervals[j][1])]
                if parent_tree != sorted(parent_tree):
                    raise AssertionError("parent tree edge order is not canonical")
                if any(e not in parent_overlap for e in parent_tree):
                    raise AssertionError("deleted-leaf tree edge is not a parent overlap edge")
                if not is_tree(list(range(s-1)),parent_tree):
                    raise AssertionError("deleting a non-root leaf did not leave a parent spanning tree")
                row["parents"].append({
                    "deleted_interval_index":mark,
                    "deleted_interval":list(intervals[mark]),
                    "retained_ports_before_compression":retained,
                    "port_order_compression":{str(k):v for k,v in compression.items()},
                    "parent_intervals":[list(I) for I in parent_intervals],
                    "parent_full_overlap_edges":parent_overlap,
                    "parent_tree_edges":parent_tree})
            records.append(row)
    records.sort(key=lambda r:(r["intervals"],r["tree_edges"]))
    return records

def build(n_values):
    result={"schema":"PF-I16-HALL-SOURCE-RECORDS-v1",
            "conventions":{"ports":"1..n in linear order",
             "overlap":"max(a_i,a_j) < min(b_i,b_j)",
             "tree":"all spanning trees of the full overlap graph",
             "root":"unique interval whose left endpoint is 1",
             "marks":"non-root degree-one vertices of the selected tree",
             "parent":"delete marked endpoints and order-compress retained ports"},
            "orders":{}}
    for n in n_values:
        rows=source_records(n)
        hist=Counter(len(r["eligible_reverse_marks"]) for r in rows)
        result["orders"][str(n)]={"source_count":len(rows),
            "eligible_mark_count":sum(k*v for k,v in hist.items()),
            "mark_histogram":{str(k):v for k,v in sorted(hist.items())},
            "sources":rows}
    payload=json.dumps(result,sort_keys=True,separators=(",",":"))+"\n"
    result["sha256_canonical_payload"]=hashlib.sha256(payload.encode()).hexdigest()
    return result

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--orders",nargs="+",type=int,default=[4,6])
    p.add_argument("--output",type=Path,required=True)
    a=p.parse_args()
    obj=build(a.orders)
    a.output.parent.mkdir(parents=True,exist_ok=True)
    a.output.write_text(json.dumps(obj,sort_keys=True,indent=2)+"\n")
    for n,row in obj["orders"].items():
        print(json.dumps({"n":int(n),"sources":row["source_count"],
            "eligible_marks":row["eligible_mark_count"],
            "mark_histogram":row["mark_histogram"]}),flush=True)

if __name__=="__main__":
    main()
