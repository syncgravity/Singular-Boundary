#!/usr/bin/env python3
"""n=10 leaf-last subgraph from four canonical parent-before-child orders.

For each source, use DFS/BFS orders with ascending/descending sibling order.
At each insertion use the connected-tree witness and all guarded local
patterns on that one witness edge. This remains a subrelation of the full
leaf-last neighborhood but is broader than a single fixed order.
"""
from collections import defaultdict, Counter, deque
from verify_pf_i16_source_dependent_leaf_peeling import (
    sources, canonical_leaf,
)
from verify_pf_i16_local_switch_fractional_transport import (
    LOCAL_TREES, tree_path, overlaps,
)
from verify_pf_i16_global_alternating_reroute import hopcroft_karp


def order_variants(intervals,tau,leaf):
    root=next(i for i,I in enumerate(intervals) if I[0]==1)
    adj=[[] for _ in intervals]
    for a,b in tau:
        adj[a].append(b); adj[b].append(a)
    parent={root:None}; depth={root:0}
    q=deque([root])
    while q:
        u=q.popleft()
        for v in adj[u]:
            if v not in parent:
                parent[v]=u; depth[v]=depth[u]+1; q.append(v)
    parent[leaf] = parent[leaf] if leaf in parent else next(p for p in adj[leaf] if p in parent)
    variants=[]
    for reverse in (False,True):
        def dfs_order():
            out=[]
            def dfs(u):
                kids=sorted((v for v in adj[u] if parent.get(v)==u and v!=leaf),
                            key=lambda z:intervals[z], reverse=reverse)
                for v in kids:
                    out.append(v); dfs(v)
            dfs(root)
            out.append(leaf)
            return out
        variants.append(dfs_order())
        nonleaf=[v for v in parent if v not in (root,leaf)]
        variants.append(sorted(nonleaf,key=lambda v:(depth[v],intervals[v]),
                               reverse=reverse)+[leaf])
    unique=[]
    seen=set()
    for order in variants:
        t=tuple(order)
        if t not in seen:
            seen.add(t); unique.append(t)
    return unique,root,adj,parent


def local_choices(tree_edges,J,parent_interval):
    inside=sorted({x for e in tree_edges for x in e if J[0]<x<J[1]})
    start,end=(inside[0],1) if inside else parent_interval
    path=tree_path(tree_edges,start,end)
    cand=[e for e in zip(path,path[1:])
          if overlaps(e,J) and not (J[0]<min(e)<max(e)<J[1])]
    assert cand,(tree_edges,J,parent_interval,path)
    u,v=sorted(cand[0]); xs=sorted((u,v,J[0],J[1]))
    out=[]
    for local in LOCAL_TREES:
        mapped=tuple(sorted(tuple(sorted((xs[a],xs[b]))) for a,b in local))
        if (u,v) in mapped: continue
        new=set(tree_edges); new.remove((u,v)); new.update(mapped)
        out.append(frozenset(new))
    assert len(out)>=2
    return out


def source_outputs(intervals,tau):
    leaf=canonical_leaf(intervals,tau)
    orders,root,adj,parent=order_variants(intervals,tau,leaf)
    all_outputs=set()
    for order in orders:
        states={frozenset({tuple(sorted(intervals[root]))})}
        for child in order:
            J=intervals[child]
            next_states=set()
            for state in states:
                next_states.update(local_choices(state,J,intervals[parent[child]]))
            states=next_states
        all_outputs.update(states)
    assert len(all_outputs)>=2**(len(intervals)-1)
    return all_outputs,len(orders)


def hall_witness(rows,ml,mr,right):
    rev={t:i for i,t in enumerate(right)}
    seen_l={i for i,v in enumerate(ml) if v<0}
    seen_r=set(); q=list(seen_l)
    while q:
        u=q.pop()
        for t in rows[u]:
            v=rev[t]
            if ml[u]==v or v in seen_r: continue
            seen_r.add(v)
            w=mr[v]
            if w>=0 and w not in seen_l:
                seen_l.add(w); q.append(w)
    return sorted(seen_l),len(seen_r)


def run(n=10):
    rows=[]; target_sources=defaultdict(list); order_hist=Counter()
    for intervals,tau in sources(n):
        outs,k=source_outputs(intervals,tau); order_hist[k]+=1
        idx=len(rows); rows.append(outs)
        for T in outs: target_sources[T].append(idx)
    right=sorted(target_sources)
    ml,mr,_=hopcroft_karp(rows)
    size=sum(v>=0 for v in ml)
    print(f"n={n}: sources={len(rows)}, target_union={len(right)}, "
          f"incidences={sum(map(len,rows))}, source_degree_range="
          f"[{min(map(len,rows))},{max(map(len,rows))}]")
    print(f"  order_variant_count_histogram={dict(sorted(order_hist.items()))}")
    print(f"  maximum_matching={size}/{len(rows)}, unmatched_sources={len(rows)-size}")
    if size<len(rows):
        A,nb=hall_witness(rows,ml,mr,right)
        print(f"  hall_witness_sources={len(A)}, neighbor_count={nb}, "
              f"deficiency={len(A)-nb}")
        print(f"  hall_witness_indices={A[:100]}")
    else:
        print("  LEFT_SATURATED")
    return size==len(rows)


if __name__=="__main__":
    run()
