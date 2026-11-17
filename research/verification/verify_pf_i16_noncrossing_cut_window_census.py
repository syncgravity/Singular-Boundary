#!/usr/bin/env python3
"""Exact cut-window census for non-crossing and crossing leaf fibers.

Tests q(j)=j-1[a<=j]-1[b<=j] and the parent-load intersection formula.
It deliberately does not assume the parent's first crowded odd cut is
determined by the child's k.
"""
from collections import Counter

from verify_pf_i16_source_dependent_leaf_peeling import sources, parent_data
from verify_pf_i16_local_switch_fractional_transport import load
from verify_pf_i16_n10_multivalued_pi_exchange_scc import nonroot_leaves
from verify_pf_i16_overcrowded_cut_split_maxflow import first_source_cut


def parent_first(intervals):
    p=load(intervals, 2*len(intervals))
    return next((q for q in range(1,2*len(intervals),2) if p[q-1]>=3),None)


def check_window(iv,tau,leaf,k):
    n=2*len(iv); a,b=iv[leaf]
    qmap={j:j-int(a<=j)-int(b<=j) for j in range(1,n)}
    assert all(qmap[j]<=qmap[j+1] for j in range(1,n-1))
    q0=qmap[k]
    window=[j for j,q in qmap.items() if q==q0]
    assert window
    if b<=k: assert q0==k-2
    elif a>k: assert q0==k
    else: assert q0==k-1

    piv,_=parent_data(iv,tau,leaf)
    for q in range(1,n-2):
        js=[j for j,v in qmap.items() if v==q]
        assert js
        direct=sum(x<=q<y for x,y in piv)
        via_intersection=sum(
            all(x<=j<y for j in js) for i,(x,y) in enumerate(iv) if i!=leaf
        )
        assert direct==via_intersection,(iv,leaf,q,js,direct,via_intersection)
    return q0,tuple(window),piv


def run(n):
    totals=Counter(); first=Counter(); windows=Counter()
    for iv,tau in sources(n):
        k=first_source_cut(iv,n)
        if k is None: continue
        for leaf in nonroot_leaves(iv,tau):
            a,b=iv[leaf]
            cls="left" if b<=k else "right" if a>k else "crossing"
            q0,window,piv=check_window(iv,tau,leaf,k)
            pf=parent_first(piv)
            totals[(k,cls)]+=1
            first[(k,cls,pf)]+=1
            windows[(k,cls,q0,window)]+=1
    print(f"n={n} fibers={sum(totals.values())}")
    for (k,cls),count in sorted(totals.items()):
        dist=sorted(
            ((pf,c) for (kk,cc,pf),c in first.items()
             if kk==k and cc==cls),
            key=lambda z:(-1 if z[0] is None else z[0])
        )
        wdist=sorted((q,w,c) for (kk,cc,q,w),c in windows.items()
                     if kk==k and cc==cls)
        print(f"  child_cut={k} class={cls} fibers={count} parent_first_cut={dist}")
        print(f"    distinguished_parent_cut_windows={wdist}")
    print("PASS: cut compression and parent-load intersection identities verified.")
    print("No first-crowded parent-block theorem is inferred.")


if __name__=="__main__":
    for n in (6,8,10):
        run(n)
