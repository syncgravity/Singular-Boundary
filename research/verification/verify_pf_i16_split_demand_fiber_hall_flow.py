#!/usr/bin/env python3
"""Exact integer max-flow test for split-demand parent/leaf fibers.

Each source x contributes 1/d(x) to each of its d(x) non-root leaf fibers.
For a fixed fiber F=(p,J), all child sources share the same target row N(F).
The weighted quotient Hall condition is tested exactly after multiplying by
L=lcm(1,...,s-1): fiber supply is L*delta(F), target capacity is L.

The resulting network has integral capacities. By max-flow integrality, a
full flow is an exact rational fractional Hall certificate for the fibers.
A deficient min cut rejects only this quotient reduction, not source Hall.
"""
from collections import defaultdict, deque
import json
from pathlib import Path
from fractions import Fraction
from math import lcm

from verify_pf_i16_source_dependent_leaf_peeling import (
    sources, parent_data, canonical_leaf, inverse_last_switch, compress_tree,
)
from verify_pf_i16_local_switch_fractional_transport import candidate_outputs
from verify_pf_i16_fixed_parent_leaf_fiber_expansion import nonroot_leaf_indices


class Dinic:
    def __init__(self, n):
        self.g=[[] for _ in range(n)]

    def add(self,u,v,c):
        a=[v,len(self.g[v]),c]
        b=[u,len(self.g[u]),0]
        self.g[u].append(a); self.g[v].append(b)

    def flow(self,s,t):
        total=0
        n=len(self.g)
        while True:
            level=[-1]*n; level[s]=0
            q=deque([s])
            while q:
                u=q.popleft()
                for v,rev,c in self.g[u]:
                    if c and level[v]<0:
                        level[v]=level[u]+1; q.append(v)
            if level[t]<0:
                break
            it=[0]*n
            def dfs(u,f):
                if u==t: return f
                while it[u]<len(self.g[u]):
                    e=self.g[u][it[u]]
                    v,rev,c=e
                    if c and level[v]==level[u]+1:
                        z=dfs(v,min(f,c))
                        if z:
                            e[2]-=z
                            self.g[v][rev][2]+=z
                            return z
                    it[u]+=1
                return 0
            while True:
                z=dfs(s,10**30)
                if not z: break
                total+=z
        seen={s}; q=deque([s])
        while q:
            u=q.popleft()
            for v,rev,c in self.g[u]:
                if c and v not in seen:
                    seen.add(v); q.append(v)
        return total,seen


def run(n, expected_sources):
    s=n//2
    scale=1
    for d in range(1,s):
        scale=lcm(scale,d)
    fibers=defaultdict(list)
    all_sources=list(sources(n))
    for iv,tau in all_sources:
        leaves=nonroot_leaf_indices(iv,tau)
        for leaf in leaves:
            J=iv[leaf]
            p=parent_data(iv,tau,leaf)
            fibers[(p,J)].append((iv,tau,leaf))
    assert sum(len(v) for v in fibers.values())==sum(
        len(nonroot_leaf_indices(iv,tau)) for iv,tau in all_sources)
    source_count=len(all_sources)
    assert source_count==expected_sources,(n,source_count,expected_sources)

    rows=[]
    demand_total=Fraction(0)
    targets=set()
    raw_incidences=0
    retained_incidences=0
    parent_neighborhood_cache={}
    for key,children in fibers.items():
        iv,tau,leaf=children[0]
        J=iv[leaf]
        raw_row=candidate_outputs(iv,tau,forced_last=leaf)
        raw_incidences+=len(raw_row)
        for civ,ctau,cleaf in children[1:]:
            assert candidate_outputs(civ,ctau,forced_last=cleaf)==raw_row
        p=key[0]
        if p not in parent_neighborhood_cache:
            pi,pt=p
            if len(pi)==1:
                parent_neighborhood_cache[p]={((1,2),)}
            else:
                parent_leaf=canonical_leaf(pi,pt)
                parent_neighborhood_cache[p]=candidate_outputs(
                    pi,pt,forced_last=parent_leaf
                )
        canonical_parent_targets=parent_neighborhood_cache[p]
        row=set()
        for T in raw_row:
            inverse=inverse_last_switch(T,J,n)
            assert len(inverse)==1,(n,key,T,inverse)
            parent_tree=compress_tree(next(iter(inverse)),set(J),n)
            if parent_tree in canonical_parent_targets:
                row.add(T)
        row=frozenset(row)
        retained_incidences+=len(row)
        demand=sum((Fraction(1,len(nonroot_leaf_indices(civ,ctau)))
                    for civ,ctau,cleaf in children),Fraction(0))
        representative=(iv,tau,leaf)
        rows.append((key,demand,row,representative))
        demand_total+=demand
        targets.update(row)
    target_list=sorted(targets)
    tid={T:i for i,T in enumerate(target_list)}
    nf=len(rows); nt=len(target_list)
    src=0; f0=1; t0=f0+nf; sink=t0+nt
    net=Dinic(sink+1)
    flow_edge_refs=[]
    for i,(key,demand,row,representative) in enumerate(rows):
        supply=demand*scale
        assert supply.denominator==1,(key,demand,scale)
        net.add(src,f0+i,int(supply))
        for T in row:
            edge_index=len(net.g[f0+i])
            net.add(f0+i,t0+tid[T],int(demand_total*scale))
            flow_edge_refs.append((i,tid[T],edge_index))
    for j in range(nt):
        net.add(t0+j,sink,scale)
    sent,reachable=net.flow(src,sink)
    total=int(demand_total*scale)
    print(f"n={n} sources={source_count} fibers={nf} targets={nt} scale={scale}")
    print(f"  raw_leaf_last_fiber_incidences={raw_incidences} retained_multivalued_pi_incidences={retained_incidences}")
    print(f"  exact_total_demand={demand_total} scaled={total}")
    print(f"  max_flow={sent} deficit={total-sent}")
    if sent==total:
        print("RESULT: exact split-demand quotient Hall flow exists.")
        if n == 10:
            # Preserve a compact replayable witness: targets are interned once,
            # and each fiber stores only positive target-flow assignments.
            target_load=[0]*nt
            assignments=[[] for _ in rows]
            used_targets=set()
            for i,j,eidx in flow_edge_refs:
                edge=net.g[f0+i][eidx]
                units=net.g[t0+j][edge[1]][2]
                if units:
                    assignments[i].append([j,units])
                    target_load[j]+=units
                    used_targets.add(j)
            assert max(target_load,default=0)<=scale
            assert sum(target_load)==total
            cert_targets=[target_list[j] for j in sorted(used_targets)]
            remap={old:new for new,old in enumerate(sorted(used_targets))}
            cert_fibers=[]
            for i,(key,demand,row,representative) in enumerate(rows):
                parent,J=key
                pi,pt=parent
                iv,tau,leaf=representative
                pi_out,pt_out=iv,tau
                cert_fibers.append({
                    "parent_intervals":[list(e) for e in pi],
                    "parent_tree":[list(e) for e in pt],
                    "deleted_interval":list(J),
                    "representative_intervals":[list(e) for e in pi_out],
                    "representative_tree":[list(e) for e in pt_out],
                    "representative_leaf_index":leaf,
                    "demand":[demand.numerator,demand.denominator],
                    "assignments":[[remap[j],units] for j,units in assignments[i] if units],
                })
            certificate={
                "schema":"pf-i16-split-demand-flow-v1",
                "n":10,
                "scale":scale,
                "source_count":source_count,
                "fiber_count":nf,
                "target_count":len(cert_targets),
                "total_demand":[demand_total.numerator,demand_total.denominator],
                "scaled_total_demand":total,
                "max_flow":sent,
                "max_target_load":max(target_load,default=0),
                "used_target_count":len(used_targets),
                "targets":[[list(e) for e in T] for T in cert_targets],
                "fibers":cert_fibers,
            }
            out=Path("n10_split_demand_flow_certificate.json")
            out.write_text(json.dumps(certificate,separators=(",",":")),encoding="utf-8")
            print(f"  flow_certificate={out} bytes={out.stat().st_size}")
            print(f"  positive_fiber_target_arcs={sum(len(x) for x in assignments)}")
            print(f"  used_targets={len(used_targets)} max_target_load={max(target_load)}")
    else:
        rf=[i for i in range(nf) if f0+i in reachable]
        rt=[j for j in range(nt) if t0+j in reachable]
        d=sum((rows[i][1] for i in rf),Fraction(0))
        print(f"  min_cut_fibers={len(rf)} min_cut_neighbors={len(rt)}")
        print(f"  min_cut_demand={d} neighbor_capacity={len(rt)} deficiency={d-len(rt)}")
        print("RESULT: this fiber quotient fails Hall; source-level Hall is not disproved.")
    return sent==total



def terminal_target_access_diagnostic(n, expected_sources):
    """Test whether every nonterminal source has a Q-neighbor in R_n.

    Q consists of trees with exactly one edge crossing every odd cut. The
    check uses all non-root leaf fibers and the same parent-canonical inverse
    filter as the split-demand Hall verifier. A failure is diagnostic only;
    it does not affect the quotient-flow result above.
    """
    all_sources = list(sources(n))
    assert len(all_sources) == expected_sources
    fibers = defaultdict(list)
    source_cut = []
    for idx, (iv, tau) in enumerate(all_sources):
        k = next((k for k in range(1, n, 2)
                  if sum(a <= k < b for a, b in iv) >= 3), None)
        source_cut.append(k)
        if k is None:
            continue
        for leaf in nonroot_leaf_indices(iv, tau):
            J = iv[leaf]
            p = parent_data(iv, tau, leaf)
            fibers[(p, J, k)].append((idx, iv, tau, leaf))

    parent_cache = {}
    covered = set()
    fibers_tested = 0
    raw_q_incidences = 0
    retained_q_incidences = 0
    q_targets = set()
    fibers_with_q = 0

    for (p, J, k), children in fibers.items():
        if all(idx in covered for idx, *_ in children):
            continue
        if p not in parent_cache:
            pi, pt = p
            if len(pi) == 1:
                parent_cache[p] = {((1, 2),)}
            else:
                pl = canonical_leaf(pi, pt)
                parent_cache[p] = candidate_outputs(pi, pt, forced_last=pl)
        parent_targets = parent_cache[p]
        iv, tau, leaf = children[0][1:]
        raw = candidate_outputs(iv, tau, forced_last=leaf)
        for civ, ctau, cleaf in [child[1:] for child in children[1:]]:
            assert candidate_outputs(civ, ctau, forced_last=cleaf) == raw
        fibers_tested += 1
        found = False
        for T in raw:
            if not all(sum(a <= k0 < b for a, b in T) == 1
                       for k0 in range(1, n, 2)):
                continue
            raw_q_incidences += 1
            inverse = inverse_last_switch(T, J, n)
            assert len(inverse) == 1
            P = compress_tree(next(iter(inverse)), set(J), n)
            if P in parent_targets:
                retained_q_incidences += 1
                q_targets.add(T)
                found = True
        if found:
            fibers_with_q += 1
            covered.update(idx for idx, *_ in children)

    uncovered = [i for i, k in enumerate(source_cut)
                 if k is not None and i not in covered]
    by_cut = Counter(source_cut[i] for i in uncovered)
    total_by_cut = Counter(k for k in source_cut if k is not None)
    print(f"TERMINAL_Q_ACCESS n={n} complement={sum(total_by_cut.values())}")
    print(f"  complement_by_first_cut={sorted(total_by_cut.items())}")
    print(f"  fibers_tested={fibers_tested} fibers_with_Q={fibers_with_q}")
    print(f"  raw_Q_incidences={raw_q_incidences} retained_parent_canonical_Q_incidences={retained_q_incidences}")
    print(f"  distinct_retained_Q_targets={len(q_targets)}")
    print(f"  uncovered_sources={len(uncovered)} uncovered_by_first_cut={sorted(by_cut.items())}")
    print("  CONJECTURE_STATUS=" + ("PASSES_FINITE_TEST" if not uncovered else "FAILS_FINITE_TEST"))
    if uncovered:
        print(f"  first_uncovered_source={all_sources[uncovered[0]]}")


if __name__=="__main__":
    run(6,22)
    run(8,608)
    run(10,31744)
    terminal_target_access_diagnostic(6,22)
    terminal_target_access_diagnostic(8,608)
    terminal_target_access_diagnostic(10,31744)
