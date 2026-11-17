#!/usr/bin/env python3
"""Exact full n=10 leaf-last graph and maximum matching.

Unlike the canonical subgraph tests, this uses every parent-before-child
insertion order and every guarded overlapping edge from candidate_outputs.
Trees are encoded as 45-bit masks on K_10 to keep the incidence graph compact.
"""
from collections import Counter, defaultdict
from array import array
import sys
from verify_pf_i16_source_dependent_leaf_peeling import (
    sources, canonical_leaf,
)
from verify_pf_i16_local_switch_fractional_transport import candidate_outputs
from verify_pf_i16_global_alternating_reroute import hopcroft_karp


def encode_tree(tree):
    mask=0
    for a,b in tree:
        if a>b: a,b=b,a
        # Lexicographic edge index among 1<=a<b<=10.
        idx=sum(10-u for u in range(1,a)) + (b-a-1)
        mask |= 1 << idx
    return mask


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



def sink_scc_census(rows, ml, mr, right):
    """Exact sink-SCC census in the matching-relative digraph.

    Vertices are left sources.  There is an arc x -> y (x != y) when
    source x is adjacent to the target matched to source y.  A sink SCC
    with no neighbor among genuinely unmatched right targets is a tight
    Hall block.  Adjacency is stored in compact unsigned-int arrays.
    """
    n = len(rows)
    owner = {right[j]: i for j, i in enumerate(mr) if i >= 0}
    free_targets = {right[j] for j, i in enumerate(mr) if i < 0}
    adj = [array('I') for _ in range(n)]
    rev = [array('I') for _ in range(n)]
    for x, row in enumerate(rows):
        for target in row:
            y = owner.get(target)
            if y is not None and y != x:
                adj[x].append(y)
                rev[y].append(x)

    # Iterative Kosaraju first pass; avoid recursion-depth dependence.
    seen = bytearray(n)
    order = []
    for root in range(n):
        if seen[root]:
            continue
        seen[root] = 1
        stack = [(root, 0)]
        while stack:
            v, pos = stack[-1]
            if pos < len(adj[v]):
                w = adj[v][pos]
                stack[-1] = (v, pos + 1)
                if not seen[w]:
                    seen[w] = 1
                    stack.append((w, 0))
            else:
                order.append(v)
                stack.pop()

    # Second pass on the reversed graph.
    comp = [-1] * n
    comp_members = []
    for root in reversed(order):
        if comp[root] >= 0:
            continue
        cid = len(comp_members)
        members = []
        comp[root] = cid
        stack = [root]
        while stack:
            v = stack.pop()
            members.append(v)
            for w in rev[v]:
                if comp[w] < 0:
                    comp[w] = cid
                    stack.append(w)
        comp_members.append(members)

    # Full condensation and componentwise free-target census.
    dag = [set() for _ in comp_members]
    free_by_comp = [set() for _ in comp_members]
    source_degree = [0] * len(comp_members)
    for x, row in enumerate(rows):
        cx = comp[x]
        source_degree[cx] += len(row)
        for target in row:
            y = owner.get(target)
            if y is not None and comp[y] != cx:
                dag[cx].add(comp[y])
            elif target in free_targets:
                free_by_comp[cx].add(target)
    indegree = [0] * len(comp_members)
    for cx, children in enumerate(dag):
        for cy in children:
            indegree[cy] += 1
    print("  condensation_components="
          + repr([(cid, len(comp_members[cid]), len(dag[cid]),
                   indegree[cid], len(free_by_comp[cid]),
                   source_degree[cid], min(comp_members[cid]))
                  for cid in range(len(comp_members))]))
    print("  condensation_arcs="
          + repr([(cx, cy) for cx, children in enumerate(dag)
                  for cy in sorted(children)]))

    sink = bytearray([1]) * len(comp_members)
    for x in range(n):
        cx = comp[x]
        for y in adj[x]:
            if comp[y] != cx:
                sink[cx] = 0
    sink_ids = [i for i, flag in enumerate(sink) if flag]
    census = []
    zero_free = []
    for cid in sink_ids:
        members = comp_members[cid]
        free_neighbors = set()
        for x in members:
            free_neighbors.update(t for t in rows[x] if t in free_targets)
        item = (len(members), len(free_neighbors), min(members))
        census.append(item)
        if not free_neighbors:
            zero_free.append(item)

    census.sort()
    zero_free.sort()
    print(f"  matching_relative_arcs={sum(map(len, adj))}")
    print(f"  scc_count={len(comp_members)}, sink_scc_count={len(sink_ids)}")
    print(f"  sink_scc_zero_free_count={len(zero_free)}, "
          f"positive_free_count={len(sink_ids)-len(zero_free)}")
    if census:
        print(f"  sink_scc_size_range=[{min(z[0] for z in census)},"
              f"{max(z[0] for z in census)}]")
        print(f"  sink_scc_free_neighbor_range=[{min(z[1] for z in census)},"
              f"{max(z[1] for z in census)}]")
        print(f"  sink_scc_census_size_free_minindex={census}")
    if zero_free:
        print(f"  ZERO_FREE_SINK_SCCS={zero_free}")
    else:
        print("  NO_ZERO_FREE_SINK_SCC")
    return census

def run(n=10):
    rows=[]
    degrees=Counter()
    for idx,(intervals,tau) in enumerate(sources(n)):
        leaf=canonical_leaf(intervals,tau)
        outs=candidate_outputs(intervals,tau,forced_last=leaf)
        encoded={encode_tree(T) for T in outs}
        assert len(encoded)==len(outs)
        assert len(encoded)>=2**(n//2-1)
        rows.append(encoded)
        degrees[len(encoded)]+=1
        if (idx+1)%2000==0:
            print(f"  processed_sources={idx+1}",flush=True)
    target_union=set().union(*rows)
    ml,mr,right=hopcroft_karp(rows)
    size=sum(v>=0 for v in ml)
    print(f"n={n}: sources={len(rows)}, target_union={len(target_union)}, "
          f"incidences={sum(map(len,rows))}, degree_range="
          f"[{min(degrees)},{max(degrees)}]")
    print(f"  source_degree_histogram={dict(sorted(degrees.items()))}")
    print(f"  maximum_matching={size}/{len(rows)}, unmatched_sources={len(rows)-size}")
    if size==len(rows):
        # A free target is unmatched by every left source, i.e. mr[j] < 0.
        # Excluding only row i's own matched target is NOT sufficient:
        # its other neighbors may be matched to other sources.
        free_targets={right[j] for j,owner in enumerate(mr) if owner<0}
        free_degree=[sum(1 for t in row if t in free_targets) for row in rows]
        print(f"  free_target_count={len(free_targets)}")
        print(f"  true_free_target_degree_range=[{min(free_degree)},{max(free_degree)}], "
              f"histogram={dict(sorted(Counter(free_degree).items()))}")
        print(f"  sources_with_true_free_degree_le2={sum(d<=2 for d in free_degree)}")
        sink_scc_census(rows, ml, mr, right)
    if size<len(rows):
        A,nb=hall_witness(rows,ml,mr,right)
        print(f"  hall_witness_sources={len(A)}, neighbor_count={nb}, "
              f"deficiency={len(A)-nb}")
        print(f"  hall_witness_first_indices={A[:100]}")
    else:
        owner={right[j]:i for j,i in enumerate(mr) if i>=0}
        free=len(set(right)-set(owner))
        print(f"  LEFT_SATURATED free_targets={free}")
    return size==len(rows)


if __name__=="__main__":
    assert run()
