#!/usr/bin/env python3
"""Exact full n=10 leaf-last graph and maximum matching.

Unlike the canonical subgraph tests, this uses every parent-before-child
insertion order and every guarded overlapping edge from candidate_outputs.
Trees are encoded as 45-bit masks on K_10 to keep the incidence graph compact.
"""
from collections import Counter
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
        free_degree=[sum(1 for t in row if t != right[ml[i]]) for i,row in enumerate(rows)]
        print(f"  free_target_degree_range=[{min(free_degree)},{max(free_degree)}], "
              f"histogram={dict(sorted(Counter(free_degree).items()))}")
        print(f"  sources_with_free_degree_le2={sum(d<=2 for d in free_degree)}")
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
