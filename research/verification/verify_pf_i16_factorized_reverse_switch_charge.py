#!/usr/bin/env python3
"""Exact reverse-switch factorized charge over the FULL canonical parent neighborhood.

For each fixed fiber F=(p,J), split its demand delta(F) uniformly over every
P in the COMPLETE C_can(p), then split that parent-target share uniformly
over ALL valid final-switch lifts T of P (without imposing a target cut class).

Thus alpha(F,P)=delta(F)/|C_can(p)| and
beta(F,P,T)=1/|L_J(P)|.

The resulting exact target load is
  L(T)=sum_{F,P: P_J(T)=P} delta(F)/(|C_can(p)| |L_J(P)|).
This is a genuine two-stage, nonuniform-on-child-targets transport. It differs
from spreading delta(F) uniformly over the whole child row.

A maximum column load <= 1 is a finite fractional Hall certificate. A load
above 1 only rejects this particular factorized allocation.
"""
from collections import defaultdict, Counter
from fractions import Fraction

from verify_pf_i16_source_dependent_leaf_peeling import (
    sources, parent_data, inverse_last_switch, compress_tree, canonical_leaf,
)
from verify_pf_i16_local_switch_fractional_transport import candidate_outputs
from verify_pf_i16_fixed_parent_leaf_fiber_expansion import nonroot_leaf_indices
from verify_pf_i16_full_leaf_last_graph_n10 import encode_tree


def first_source_cut(intervals, n):
    loads=[sum(a<=k<b for a,b in intervals) for k in range(1,n)]
    return next((k for k in range(1,n,2) if loads[k-1]>=3), None)


def parent_neighborhood(parent):
    pi,pt=parent
    if len(pi)==1:
        return {((1,2),)}
    leaf=canonical_leaf(pi,pt)
    return candidate_outputs(pi,pt,forced_last=leaf)


def run(n, expected_sources):
    fibers=defaultdict(list)
    class_counts=Counter()
    for intervals,tau in sources(n):
        k=first_source_cut(intervals,n)
        class_counts[k]+=1
        if k is None:
            continue
        for leaf in nonroot_leaf_indices(intervals,tau):
            J=intervals[leaf]
            p=parent_data(intervals,tau,leaf)
            fibers[(p,J,k)].append((intervals,tau,leaf))
    source_count=sum(class_counts.values())
    assert source_count==expected_sources,(n,source_count,expected_sources)

    loads=defaultdict(Fraction)
    total_demand=Fraction(0)
    fiber_count=0
    parent_target_total=0
    lift_total=0
    min_lifts=None
    max_lifts=0
    demand_by_cut=Counter()

    for (p,J,k),children in fibers.items():
        # The row is common to every child source in this fixed (p,J) fiber.
        child_rows=[candidate_outputs(iv,tau,forced_last=leaf)
                    for iv,tau,leaf in children]
        assert all(row==child_rows[0] for row in child_rows)
        C=parent_neighborhood(p)
        assert C
        demand=sum((Fraction(1,len(nonroot_leaf_indices(iv,tau)))
                    for iv,tau,leaf in children),Fraction(0))
        assert demand>0

        # For each canonical parent target, recover its exact valid child lifts.
        lifts=defaultdict(set)
        for T in child_rows[0]:
            inv=inverse_last_switch(T,J,n)
            assert len(inv)==1
            P=compress_tree(next(iter(inv)),set(J),n)
            if P in C:
                lifts[P].add(encode_tree(T))
        assert set(lifts)==set(encode_tree(P) for P in C), (
            "some canonical parent target lacks a final-switch lift",n,p,J,k,
            len(C),len(lifts))
        # alpha uniform over complete C_can(p); beta uniform over each
        # parent's complete final-switch lift set.
        for Pcode,Ts in lifts.items():
            share=demand/Fraction(len(C),1)/Fraction(len(Ts),1)
            for Tcode in Ts:
                loads[Tcode]+=share
            lift_total+=len(Ts)
            min_lifts=len(Ts) if min_lifts is None else min(min_lifts,len(Ts))
            max_lifts=max(max_lifts,len(Ts))
        total_demand+=demand
        demand_by_cut[k]+=demand
        parent_target_total+=len(C)
        fiber_count+=1

    assert sum(loads.values(),Fraction(0))==total_demand
    max_load=max(loads.values(),default=Fraction(0))
    overloaded=[(T,v) for T,v in loads.items() if v>1]
    top=sorted(loads.items(),key=lambda z:(-z[1],z[0]))[:10]
    print(f"n={n} source_classes={sorted(class_counts.items(),key=lambda z:(-1 if z[0] is None else z[0]))}")
    print(f"  complement_sources={source_count-class_counts[None]} fibers={fiber_count}")
    print(f"  total_split_demand={total_demand} by_cut={dict(sorted(demand_by_cut.items()))}")
    print(f"  canonical_parent_target_incidences={parent_target_total} all_valid_lifts={lift_total}")
    print(f"  lifts_per_parent_target_range=[{min_lifts},{max_lifts}]")
    print(f"  child_target_columns={len(loads)}")
    print(f"  max_factorized_target_load={max_load} ({float(max_load):.12f})")
    print(f"  overloaded_targets={len(overloaded)}")
    print(f"  top_10_target_loads={top}")
    print("RESULT: factorized complete-parent-neighborhood charge saturates all demand."
          if max_load<=1 else
          "RESULT: this factorized charge overloads targets; this does NOT imply Hall failure.")
    return max_load, len(overloaded)


if __name__=="__main__":
    run(4,2)
    run(6,22)
    run(8,608)
    run(10,31744)
