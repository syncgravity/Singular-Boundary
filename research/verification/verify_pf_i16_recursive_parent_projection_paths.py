#!/usr/bin/env python3
"""Test recursive parent projection of residual n=8 non-diamond collisions.

For every n=8 shared-target collision still disconnected after S/C/D, map
each endpoint (p,P) to the canonical-leaf parent-target block of the order-6
source p. Then compute shortest paths in the order-6 S/C/D block graph.

This tests parent-level connectivity only. It does not assert that a path
lifts to order eight; exact source/mark/guarded-inverse witnesses are still
required for such a lifting theorem.
"""
from __future__ import annotations
import argparse, json
from collections import Counter, defaultdict, deque
from pathlib import Path

import verify_pf_i16_cross_source_reverse_mark_exchange as census
import verify_pf_i16_projection_shifting_transitions as base
from verify_pf_i16_source_dependent_leaf_peeling import sources, parent_data, canonical_leaf

def tree_key(raw):
    return tuple(sorted(tuple(e) for e in raw))

def source_key(raw):
    return (tuple(tuple(x) for x in raw[0]), tuple(tuple(e) for e in raw[1]))

def build_graph(report):
    blocks=report["blocks"]
    by_id={b["block_id"]:b for b in blocks}
    adjacency=defaultdict(set)
    edge_types=defaultdict(set)
    # S-connected states have already been contracted into fixed (p,J,P) blocks.
    for e in report["D_edges"]:
        a,b=e["block_left"],e["block_right"]
        if a!=b:
            adjacency[a].add(b); adjacency[b].add(a)
            edge_types[tuple(sorted((a,b)))].add("D")
    target_blocks=defaultdict(list)
    for b in blocks:
        bid=b["block_id"]
        for T in b["lift_targets"]:
            target_blocks[tree_key(T)].append(bid)
    c_witnesses=set()
    for T,ids in target_blocks.items():
        ids=sorted(set(ids))
        for i,a in enumerate(ids):
            A=by_id[a]
            for b in ids[i+1:]:
                B=by_id[b]
                if (A["parent_source"]==B["parent_source"]
                    and A["parent_target"]==B["parent_target"]
                    and A["deleted_interval"]!=B["deleted_interval"]
                    and any(x!=y for x in A["child_source_indices"] for y in B["child_source_indices"])):
                    key=(a,b,T)
                    c_witnesses.add(key)
                    adjacency[a].add(b); adjacency[b].add(a)
                    edge_types[(a,b)].add("C")
    return by_id, adjacency, edge_types, c_witnesses

def bfs(adjacency,start,goal):
    if start==goal: return [start]
    q=deque([start]); prev={start:None}
    while q:
        u=q.popleft()
        for v in sorted(adjacency.get(u,())):
            if v in prev: continue
            prev[v]=u
            if v==goal:
                path=[v]
                while prev[path[-1]] is not None: path.append(prev[path[-1]])
                return list(reversed(path))
            q.append(v)
    return None

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--output",default="pf_i16_recursive_parent_projection_paths.json")
    args=ap.parse_args()

    # Exact order-six and order-eight source-preserving block censuses.
    report6=census.run(6)
    report8=census.run(8)
    blocks6,adj6,types6,c6=build_graph(report6)
    blocks8,adj8,types8,c8=build_graph(report8)

    src6=list(sources(6))
    source_index6={ (tuple(tuple(x) for x in iv),tuple(tuple(e) for e in tau)):i
                    for i,(iv,tau) in enumerate(src6) }
    lookup6={
        (source_key(b["parent_source"]),tuple(b["deleted_interval"]),tree_key(b["parent_target"])):b["block_id"]
        for b in report6["blocks"]
    }

    parent_map_cache={}
    def project_endpoint(parent_raw,target_raw):
        pk=source_key(parent_raw); P=tree_key(target_raw)
        key=(pk,P)
        if key in parent_map_cache: return parent_map_cache[key]
        if pk not in source_index6:
            raise AssertionError(("n=8 parent source absent from n=6 source enumeration",pk))
        si=source_index6[pk]
        iv,tau=src6[si]
        leaf=canonical_leaf(iv,tau)
        J=iv[leaf]
        r=parent_data(iv,tau,leaf)
        inv=base.exact_guarded_inverse(P,J,6)
        if inv is None:
            raise AssertionError(("canonical parent target has no exact inverse",si,J,P))
        U=base.compress_tree(inv[0],set(J),6)
        bkey=(r,J,U)
        if bkey not in lookup6:
            raise AssertionError(("canonical parent block missing",si,J,U))
        bid=lookup6[bkey]
        b=blocks6[bid]
        if si not in b["child_source_indices"] or P not in {tree_key(T) for T in b["lift_targets"]}:
            raise AssertionError(("parent source/target not in canonical block",si,P,bid))
        parent_map_cache[key]=bid
        return bid

    # Enumerate all non-diamond shared-target pairs that remain in different
    # S/C/D components at order eight.
    target_incidences=defaultdict(list)
    for b in report8["blocks"]:
        bid=b["block_id"]
        for si in b["child_source_indices"]:
            for T in b["lift_targets"]:
                target_incidences[tree_key(T)].append((si,bid))
    residual=[]
    residual_class=Counter()
    distance_hist=Counter()
    distance_cache={}
    first_witness=None
    disconnected_parent_paths=0
    max_distance=0
    for T,inc in target_incidences.items():
        inc=list(dict.fromkeys(inc))
        for i,(si,bi) in enumerate(inc):
            for sj,bj in inc[i+1:]:
                if si==sj or bi==bj: continue
                if census.DSU is None: raise AssertionError("DSU helper missing")
                # S/C/D connectivity at n=8 is exactly the component relation
                # generated by the graph edges reconstructed above.
                if _connected(adj8,bi,bj):
                    continue
                A=blocks8[bi]; B=blocks8[bj]
                rel=(A["parent_source"]==B["parent_source"],
                     A["parent_target"]==B["parent_target"],
                     A["deleted_interval"]==B["deleted_interval"])
                residual_class[rel]+=1
                pa=project_endpoint(A["parent_source"],A["parent_target"])
                pb=project_endpoint(B["parent_source"],B["parent_target"])
                pair=tuple(sorted((pa,pb)))
                if pair not in distance_cache:
                    distance_cache[pair]=bfs(adj6,pa,pb)
                path=distance_cache[pair]
                if path is None:
                    disconnected_parent_paths+=1
                    distance_hist["disconnected"]+=1
                else:
                    distance_hist[len(path)-1]+=1
                    max_distance=max(max_distance,len(path)-1)
                if first_witness is None:
                    first_witness={
                        "child_target":[list(e) for e in T],
                        "left":{"source_index":si,"parent_source":A["parent_source"],
                                "parent_target":A["parent_target"],"deleted_interval":A["deleted_interval"],
                                "order6_parent_block":pa},
                        "right":{"source_index":sj,"parent_source":B["parent_source"],
                                 "parent_target":B["parent_target"],"deleted_interval":B["deleted_interval"],
                                 "order6_parent_block":pb},
                        "order6_block_path":path,
                        "path_edge_types":[sorted(types6.get(tuple(sorted((u,v))),())) for u,v in zip(path or [],(path or [])[1:])]
                    }
                residual.append((bi,bj,pa,pb))

    result={
        "schema":"PF-I16-RECURSIVE-PARENT-PROJECTION-PATHS-v1",
        "orders":[6,8],
        "counts":{
            "order6_blocks":len(blocks6),"order6_C_witnesses":len(c6),
            "order6_block_graph_components":_component_count(adj6,len(blocks6)),
            "order8_blocks":len(blocks8),"order8_C_witnesses":len(c8),
            "order8_residual_non_diamond_collision_pairs":len(residual),
            "unique_order6_parent_block_pairs":len(distance_cache),
            "order6_parent_projection_path_length_histogram":dict(sorted(distance_hist.items(),key=lambda x:str(x[0]))),
            "order6_parent_projection_paths_disconnected":disconnected_parent_paths,
            "maximum_order6_parent_projection_path_length":max_distance,
            "residual_collision_classes":[
                {"same_parent_source":k[0],"same_parent_target":k[1],"same_deleted_interval":k[2],"pairs":v}
                for k,v in sorted(residual_class.items())
            ]
        },
        "first_residual_parent_projection_path":first_witness,
        "scope":{
            "parent_projection": "each n=8 parent pair (p,P) is mapped to the canonical-leaf block of the n=6 source p",
            "path_graph": "order-six S/C/D graph; S-blocks contracted, D edges source-diamond witnessed, C edges parent-sibling witnessed",
            "nonclaim": "an order-six path is not yet an order-eight path; no path-lifting theorem or Hall capacity result is asserted"
        }
    }
    Path(args.output).write_text(json.dumps(result,sort_keys=True,indent=2)+"\n")
    print(json.dumps(result["counts"],sort_keys=True))

def _connected(adjacency,a,b):
    if a==b: return True
    seen={a}; q=deque([a])
    while q:
        u=q.popleft()
        for v in adjacency.get(u,()):
            if v==b: return True
            if v not in seen: seen.add(v); q.append(v)
    return False

def _component_count(adjacency,n):
    seen=set(); count=0
    for start in range(n):
        if start in seen: continue
        count+=1; seen.add(start); q=deque([start])
        while q:
            for v in adjacency.get(q.popleft(),()):
                if v not in seen: seen.add(v); q.append(v)
    return count

if __name__=="__main__":
    main()
