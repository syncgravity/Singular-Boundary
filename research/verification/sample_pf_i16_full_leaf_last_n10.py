#!/usr/bin/env python3
"""Spread sample of full n=10 leaf-last neighborhoods (all orders/edges)."""
from collections import Counter
from verify_pf_i16_source_dependent_leaf_peeling import (
    sources, canonical_leaf,
)
from verify_pf_i16_local_switch_fractional_transport import candidate_outputs


def run(n=10, stride=157):
    degrees=[]; chosen=[]; count=0
    for idx,(intervals,tau) in enumerate(sources(n)):
        if idx % stride:
            continue
        leaf=canonical_leaf(intervals,tau)
        outs=candidate_outputs(intervals,tau,forced_last=leaf)
        degrees.append(len(outs))
        chosen.append((idx,len(outs),intervals,tau))
        count+=1
    print(f"n={n}: sampled_sources={count}, stride={stride}, "
          f"degree_range=[{min(degrees)},{max(degrees)}], "
          f"mean_degree={sum(degrees)/len(degrees):.3f}")
    print(f"  degree_histogram={dict(sorted(Counter(degrees).items()))}")
    print("  sampled_source_degrees=" +
          repr([(i,d) for i,d,_,_ in chosen]))
    return degrees


if __name__=="__main__":
    run()
