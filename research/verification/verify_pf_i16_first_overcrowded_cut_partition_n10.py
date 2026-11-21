#!/usr/bin/env python3
"""Test whether first-overcrowded source cuts can partition the n=10 Hall graph.

A connected interval matching has odd cut loads 1,3,5,... . For a non-tree
overlap graph, let k be the first odd cut with m_k>=3. Targets are classified
by their first odd cut with c_k>=2. This verifier tests whether every source
has a neighbor in the target class with the same k.
"""
from collections import Counter
from itertools import combinations
from verify_pf_i16_n10_multivalued_pi_exchange_scc import build_rows
from verify_pf_i16_source_dependent_leaf_peeling import sources
from verify_pf_i16_local_switch_fractional_transport import overlap_edges

N=10
EDGES=list(combinations(range(1,N+1),2))
EDGE_INDEX={e:i for i,e in enumerate(EDGES)}


def first_source_cut(intervals):
    profile=[sum(a<=k<b for a,b in intervals) for k in range(1,N)]
    return next((k for k in range(1,N,2) if profile[k-1]>=3),None)


def first_target_cut(mask):
    profile=[0]*(N-1)
    for i,(a,b) in enumerate(EDGES):
        if (mask>>i)&1:
            for k in range(a,b):
                profile[k-1]+=1
    return next((k for k in range(1,N,2) if profile[k-1]>=2),None)


def run():
    rows, raw, parents=build_rows(N)
    src=list(sources(N))
    assert len(src)==len(rows)
    target_class={}
    for mask in set().union(*rows):
        target_class[mask]=first_target_cut(mask)
    failures=[]
    class_source=Counter()
    class_target=Counter()
    degree_by_class=Counter()
    for i,((intervals,tau),row) in enumerate(zip(src,rows)):
        k=first_source_cut(intervals)
        if k is None:
            assert len(overlap_edges(intervals))==N//2-1
            assert all(target_class[t] is None for t in row)
            continue
        class_source[k]+=1
        classes={target_class[t] for t in row}
        class_target.update(c for c in classes if c is not None)
        if k not in classes:
            failures.append((i,k,len(row),sorted(classes,key=lambda x:(x is None,x))))
        degree_by_class[k]+=len(row)
    print(f"n={N} sources={len(src)} target_union={len(target_class)}")
    print(f"  source_first_overcrowded_counts={sorted(class_source.items())}")
    print(f"  sources_with_same_cut_target_neighbor={sum(class_source.values())-len(failures)}/{sum(class_source.values())}")
    print(f"  failures={len(failures)}")
    print(f"  target_first_overcrowded_class_incidence_counts={sorted(class_target.items())}")
    print(f"  source_degree_sums_by_first_cut={sorted(degree_by_class.items())}")
    if failures:
        print("  first_failures=")
        for x in failures[:20]: print("   ",x)
    assert not failures


if __name__=="__main__":
    run()
