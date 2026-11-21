#!/usr/bin/env python3
"""Test split-demand transport after partitioning by first overcrowded odd cut.

For each fixed (parent source,J) fiber, restrict its common target row to
trees whose first odd cut with at least two crossing edges equals the source
matching's first odd cut with at least three crossing intervals. The resulting
uniform quotient transport is a sufficient Hall test for each cut block.
"""
from collections import defaultdict, Counter
from fractions import Fraction
from verify_pf_i16_source_dependent_leaf_peeling import (
    sources, parent_data, inverse_last_switch, compress_tree,
)
from verify_pf_i16_local_switch_fractional_transport import candidate_outputs


def leaves(intervals,tau):
    deg=[0]*len(intervals)
    for a,b in tau: deg[a]+=1;deg[b]+=1
    root=next(i for i,I in enumerate(intervals) if I[0]==1)
    return [i for i,d in enumerate(deg) if d==1 and i!=root]


def first_source_cut(intervals,n):
    p=[sum(a<=k<b for a,b in intervals) for k in range(1,n)]
    return next((k for k in range(1,n,2) if p[k-1]>=3),None)


def first_target_cut(T,n):
    p=[sum(a<=k<b for a,b in T) for k in range(1,n)]
    return next((k for k in range(1,n,2) if p[k-1]>=2),None)


def run(n):
    fibers=defaultdict(list)
    source_count=0
    source_class=Counter()
    for intervals,tau in sources(n):
        k=first_source_cut(intervals,n)
        source_class[k]+=1
        for leaf in leaves(intervals,tau):
            fibers[(parent_data(intervals,tau,leaf),intervals[leaf],k)].append((intervals,tau,leaf))
        source_count+=1
    loads=Counter()
    row_sizes=Counter()
    empty=[]
    fiber_counts=Counter()
    max_fiber=0
    for (parent,J,k),children in fibers.items():
        if k is None: continue
        max_fiber=max(max_fiber,len(children))
        rows=[candidate_outputs(iv,tau,forced_last=leaf) for iv,tau,leaf in children]
        assert all(r==rows[0] for r in rows)
        pi,pt=parent
        if len(pi)==1:
            parent_targets={((1,2),)}
        else:
            from verify_pf_i16_source_dependent_leaf_peeling import canonical_leaf
            pl=canonical_leaf(pi,pt)
            parent_targets=candidate_outputs(pi,pt,forced_last=pl)
        row_k=set()
        for T in rows[0]:
            P=compress_tree(next(iter(inverse_last_switch(T,J,n))),set(J),n)
            if P in parent_targets and first_target_cut(T,n)==k:
                row_k.add(T)
        if not row_k:
            empty.append((parent,J,k,len(children),len(rows[0])))
            continue
        demand=sum((Fraction(1,len(leaves(iv,tau))) for iv,tau,leaf in children),Fraction())
        mass=demand/len(row_k)
        for T in row_k: loads[(k,T)]+=mass
        row_sizes[k]+=len(row_k)
        fiber_counts[k]+=1
    per_cut={}
    for k in sorted(set(source_class)-{None}):
        vals=[v for (kk,_),v in loads.items() if kk==k]
        per_cut[k]=(len(vals),max(vals) if vals else Fraction(0),sum(vals,Fraction()))
    overloaded=[(key,val) for key,val in loads.items() if val>1]
    print(f"n={n} sources={source_count} source_classes={sorted(source_class.items(), key=lambda z: (-1 if z[0] is None else z[0]))}")
    print(f"  complement_fibers_by_cut={sorted(fiber_counts.items())}")
    print(f"  target_incidence_sum_by_cut={sorted(row_sizes.items())}")
    print(f"  max_fiber_size={max_fiber} empty_same_cut_fibers={len(empty)}")
    if empty: print("  first_empty=",empty[:10])
    print(f"  target_columns_by_cut={per_cut}")
    print(f"  max_uniform_column_load={max((v for v in loads.values()),default=Fraction(0))}")
    print(f"  overloaded_columns={len(overloaded)}")
    if overloaded: print("  worst=",sorted(overloaded,key=lambda x:-x[1])[:10])
    assert not empty


if __name__=="__main__":
    run(8)
    run(10)
