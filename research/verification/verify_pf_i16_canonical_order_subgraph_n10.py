#!/usr/bin/env python3
"""Build a compact n=10 leaf-last switch subgraph using one canonical order.

For each source, fix the rooted DFS parent-before-child order with its
canonical leaf last. At each insertion use the connected-tree witness edge
and retain every guarded local pattern on that edge (at least two).
This is a deterministic subrelation of the full leaf-last neighborhood.
"""
from collections import defaultdict, Counter
from verify_pf_i16_source_dependent_leaf_peeling import (
    sources, canonical_leaf, parent_data,
)
from verify_pf_i16_local_switch_fractional_transport import (
    LOCAL_TREES, tree_path, overlaps,
)
from verify_pf_i16_global_alternating_reroute import hopcroft_karp


def canonical_order(intervals, tau, leaf):
    root = next(i for i, I in enumerate(intervals) if I[0] == 1)
    adj = [[] for _ in intervals]
    for a,b in tau:
        adj[a].append(b); adj[b].append(a)
    order=[]
    def dfs(u,p):
        for v in sorted(adj[u], key=lambda z: intervals[z]):
            if v == p or v == leaf:
                continue
            order.append(v)
            dfs(v,u)
    dfs(root,-1)
    order.append(leaf)
    assert len(order)==len(intervals)-1
    pos={v:i for i,v in enumerate(order)}
    assert all((v==root or pos.get(v,10**9)>pos.get(parent, -1))
               for v,parent in [])
    return order, root, adj


def local_choices(tree_edges, J, parent_interval):
    inside=sorted({x for e in tree_edges for x in e if J[0]<x<J[1]})
    if inside:
        start,end=inside[0],1
    else:
        start,end=parent_interval
    path=tree_path(tree_edges,start,end)
    candidates=[
        e for e in zip(path,path[1:])
        if overlaps(e,J) and not (J[0]<min(e)<max(e)<J[1])
    ]
    assert candidates, (tree_edges,J,parent_interval,path)
    u,v=sorted(candidates[0])
    xs=sorted((u,v,J[0],J[1]))
    choices=[]
    for local in LOCAL_TREES:
        mapped=tuple(sorted(tuple(sorted((xs[a],xs[b]))) for a,b in local))
        if (u,v) in mapped:
            continue
        new=set(tree_edges)
        new.remove((u,v))
        new.update(mapped)
        choices.append(frozenset(new))
    assert len(choices)>=2
    return choices


def outputs_for_source(intervals,tau):
    leaf=canonical_leaf(intervals,tau)
    order,root,adj=canonical_order(intervals,tau,leaf)
    tree={tuple(sorted(intervals[root]))}
    states={frozenset(tree)}
    for child in order:
        J=intervals[child]
        parent=next(p for p in adj[child] if p in order[:order.index(child)])
        next_states=set()
        for state in states:
            next_states.update(local_choices(state,J,intervals[parent]))
        states=next_states
    return states


def run(n=10):
    rows=[]
    target_sources=defaultdict(list)
    matching_counts=Counter()
    for intervals,tau in sources(n):
        outs=outputs_for_source(intervals,tau)
        assert len(outs)>=2**(n//2-1), (intervals,tau,len(outs))
        idx=len(rows)
        rows.append(outs)
        matching_counts[intervals]+=1
        for T in outs:
            target_sources[T].append(idx)
    right=sorted(target_sources)
    rid={t:i for i,t in enumerate(right)}
    adj=[[rid[t] for t in sorted(row)] for row in rows]
    ml,mr=hopcroft_karp(adj)
    size=sum(v>=0 for v in ml)
    incidence=Counter(len(v) for v in target_sources.values())
    print(f"n={n}: sources={len(rows)}, target_union={len(right)}, "
          f"incidences={sum(map(len,rows))}, source_degree_range="
          f"[{min(map(len,rows))},{max(map(len,rows))}]")
    print(f"  source_count_by_matching_histogram={dict(sorted(Counter(matching_counts.values()).items()))}")
    print(f"  target_incidence_histogram={dict(sorted(incidence.items()))}")
    print(f"  maximum_matching={size}/{len(rows)}, unmatched_sources={len(rows)-size}")
    return size==len(rows)


if __name__=="__main__":
    assert run()
