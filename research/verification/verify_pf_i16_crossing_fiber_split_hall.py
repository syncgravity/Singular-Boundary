#!/usr/bin/env python3
"""Exact split-demand Hall test for crossing fibers at the first crowded cut.

This isolates the crossing-leaf part of BQH_k while retaining the full
multivalued-pi parent-canonical restriction. For each source x in X_k,
only non-root leaf intervals J with J[0] <= k < J[1] are retained.
The source-side localization theorem predicts J[0] in {k-1,k} for k>=5
(and {1,2,3} for k=3).

The combined max-flow for each k tests arbitrary mixed families from both
crossing endpoint classes simultaneously. A full flow proves the exact
split-demand quotient Hall inequality for that finite crossing subfamily.
It does not prove BQH_k for non-crossing fibers or all orders.
"""
from collections import defaultdict, Counter, deque
from array import array
from fractions import Fraction
from math import lcm

from verify_pf_i16_source_dependent_leaf_peeling import (
    sources, parent_data, inverse_last_switch, compress_tree, canonical_leaf,
)
from verify_pf_i16_local_switch_fractional_transport import candidate_outputs
from verify_pf_i16_n10_multivalued_pi_exchange_scc import nonroot_leaves
from verify_pf_i16_overcrowded_cut_split_maxflow import (
    first_source_cut, first_target_cut,
)


class Dinic:
    def __init__(self, n):
        self.n=n
        self.head=array('i',[-1])*n
        self.to=array('i')
        self.cap=array('q')
        self.nxt=array('i')
    def add(self,u,v,c):
        i=len(self.to)
        self.to.append(v); self.cap.append(c); self.nxt.append(self.head[u]); self.head[u]=i
        self.to.append(u); self.cap.append(0); self.nxt.append(self.head[v]); self.head[v]=i+1
    def maxflow(self,s,t,limit):
        flow=0; n=self.n
        level=array('i',[-1])*n
        it=array('i',[0])*n
        while flow<limit:
            for i in range(n): level[i]=-1
            level[s]=0; q=deque([s])
            while q:
                u=q.popleft(); e=self.head[u]
                while e!=-1:
                    v=self.to[e]
                    if self.cap[e]>0 and level[v]<0:
                        level[v]=level[u]+1; q.append(v)
                    e=self.nxt[e]
            if level[t]<0: break
            for i in range(n): it[i]=self.head[i]
            def dfs(u,f):
                if u==t: return f
                e=it[u]
                while e!=-1:
                    it[u]=e; v=self.to[e]
                    if self.cap[e]>0 and level[v]==level[u]+1:
                        z=dfs(v,min(f,self.cap[e]))
                        if z:
                            self.cap[e]-=z; self.cap[e^1]+=z
                            return z
                    e=self.nxt[e]; it[u]=e
                return 0
            while flow<limit:
                z=dfs(s,limit-flow)
                if not z: break
                flow+=z
        return flow,level


def run(n, scale=12):
    fibers=defaultdict(list); source_classes=Counter()
    for iv,tau in sources(n):
        k=first_source_cut(iv,n)
        source_classes[k]+=1
        if k is None: continue
        for leaf in nonroot_leaves(iv,tau):
            J=iv[leaf]
            if J[0] <= k < J[1]:
                if k >= 5:
                    assert J[0] in (k-1,k), (n,k,J)
                else:
                    assert J[0] in (1,2,3), (n,k,J)
                fibers[(parent_data(iv,tau,leaf),J,k)].append((iv,tau,leaf))

    parent_cache={}
    by_cut=defaultdict(list)
    class_counts=Counter()
    raw_inc=retained_inc=0
    target_ids_by_cut=defaultdict(dict)
    for (parent,J,k),children in fibers.items():
        pi,pt=parent
        if parent not in parent_cache:
            if len(pi)==1:
                parent_cache[parent]={((1,2),)}
            else:
                pl=canonical_leaf(pi,pt)
                parent_cache[parent]=candidate_outputs(pi,pt,forced_last=pl)
        iv,tau,leaf=children[0]
        raw=candidate_outputs(iv,tau,forced_last=leaf)
        assert all(candidate_outputs(civ,ctau,forced_last=cleaf)==raw
                   for civ,ctau,cleaf in children[1:])
        raw_inc+=len(raw)
        row=set()
        for T in raw:
            if first_target_cut(T,n)!=k: continue
            inv=inverse_last_switch(T,J,n)
            assert len(inv)==1
            P=compress_tree(next(iter(inv)),set(J),n)
            if P in parent_cache[parent]:
                row.add(T)
        retained_inc+=len(row)
        assert row, (n,parent,J,k)
        d=sum((Fraction(1,len(nonroot_leaves(civ,ctau)))
               for civ,ctau,_ in children),Fraction(0))
        assert (d*scale).denominator==1, (n,d,scale)
        ids=target_ids_by_cut[k]
        for T in row:
            if T not in ids: ids[T]=len(ids)
        by_cut[k].append((int(d*scale),[ids[T] for T in row],J[0],len(children)))
        class_counts[(k,J[0])]+=1

    print(f"n={n} source_classes={sorted(source_classes.items(),key=lambda z:(-1 if z[0] is None else z[0]))}")
    print(f"  crossing_fibers={len(fibers)} raw_incidences={raw_inc} retained_same_cut_parent_canonical_incidences={retained_inc}")
    print(f"  fibers_by_(cut,left_endpoint)={sorted(class_counts.items())}")
    all_ok=True
    for k,rows in sorted(by_cut.items()):
        targets=target_ids_by_cut[k]
        demand=sum(d for d,_,_,_ in rows)
        S=0; f0=1; t0=f0+len(rows); sink=t0+len(targets)
        net=Dinic(sink+1)
        for i,(d,row,a,child_count) in enumerate(rows):
            net.add(S,f0+i,d)
            for t in row: net.add(f0+i,t0+t,d)
        for j in range(len(targets)): net.add(t0+j,sink,scale)
        got,level=net.maxflow(S,sink,demand)
        print(f"  cut={k} crossing_fibers={len(rows)} targets={len(targets)} split_demand={Fraction(demand,scale)} scaled={demand} flow={got} deficit={demand-got}")
        if got!=demand:
            all_ok=False
            reach=[i for i in range(len(rows)) if level[f0+i]>=0]
            neigh=set()
            for i in reach: neigh.update(rows[i][1])
            w=sum(rows[i][0] for i in reach)
            print(f"    MINCUT fibers={len(reach)} targets={len(neigh)} demand={Fraction(w,scale)} capacity={len(neigh)} deficiency={Fraction(w,scale)-len(neigh)}")
    print("RESULT: crossing-fiber quotient Hall " + ("PASS" if all_ok else "FAIL") + " at this finite order.")
    return all_ok


if __name__=="__main__":
    assert run(8)
    assert run(10)
