#!/usr/bin/env python3
"""Exact integral max-flow test for split-demand cross-fiber Hall.

For n=10 every d(x)=number of non-root leaves divides 12. Multiply all
split demands by 12. Each fixed (parent,J) fiber sends demand
sum_x 12/d(x) to its common same-first-overcrowded-cut target row; each target
has capacity 12. A max flow saturating all fiber demand is exactly the
split-demand quotient Hall condition, unlike uniform row spreading.
"""
from collections import defaultdict, Counter, deque
from array import array
from verify_pf_i16_source_dependent_leaf_peeling import (
    sources, parent_data, inverse_last_switch, compress_tree, canonical_leaf,
)
from verify_pf_i16_local_switch_fractional_transport import candidate_outputs
from verify_pf_i16_n10_multivalued_pi_exchange_scc import nonroot_leaves
from verify_pf_i16_full_leaf_last_graph_n10 import encode_tree


class Dinic:
    def __init__(self,n):
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
                u=q.popleft()
                e=self.head[u]
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
                    it[u]=e
                    v=self.to[e]
                    if self.cap[e]>0 and level[v]==level[u]+1:
                        z=dfs(v,min(f,self.cap[e]))
                        if z:
                            self.cap[e]-=z; self.cap[e^1]+=z
                            return z
                    e=self.nxt[e]
                    it[u]=e
                return 0
            while flow<limit:
                z=dfs(s,limit-flow)
                if not z: break
                flow+=z
        return flow,level


def first_source_cut(intervals,n):
    p=[sum(a<=k<b for a,b in intervals) for k in range(1,n)]
    return next((k for k in range(1,n,2) if p[k-1]>=3),None)


def first_target_cut(T,n):
    p=[sum(a<=k<b for a,b in T) for k in range(1,n)]
    return next((k for k in range(1,n,2) if p[k-1]>=2),None)


def run(n,scale):
    fibers=defaultdict(list); source_classes=Counter()
    for intervals,tau in sources(n):
        k=first_source_cut(intervals,n)
        source_classes[k]+=1
        if k is None: continue
        for leaf in nonroot_leaves(intervals,tau):
            J=intervals[leaf]
            fibers[(parent_data(intervals,tau,leaf),J,k)].append((intervals,tau,leaf))
    print(f"n={n} source_classes={sorted(source_classes.items())} fibers={len(fibers)}",flush=True)
    fiber_rows=[]; target_ids={}
    total_demand=0; max_demand=0
    for fi,((parent,J,k),children) in enumerate(fibers.items()):
        pi,pt=parent
        if len(pi)==1: parent_targets={((1,2),)}
        else:
            pl=canonical_leaf(pi,pt)
            parent_targets=candidate_outputs(pi,pt,forced_last=pl)
        iv,tau,leaf=children[0]
        outs=candidate_outputs(iv,tau,forced_last=leaf)
        row=set()
        for T in outs:
            inv=inverse_last_switch(T,J,n)
            assert len(inv)==1
            P=compress_tree(next(iter(inv)),set(J),n)
            if P in parent_targets and first_target_cut(T,n)==k:
                code=encode_tree(T)
                row.add(code)
                if code not in target_ids: target_ids[code]=len(target_ids)
        demand=sum(scale//len(nonroot_leaves(iv,t)) for iv,t,_ in children)
        assert all(scale%len(nonroot_leaves(iv,t))==0 for iv,t,_ in children)
        if demand:
            assert row
            fiber_rows.append((demand,sorted(target_ids[t] for t in row),k))
            total_demand+=demand; max_demand=max(max_demand,demand)
        if (fi+1)%2000==0: print(f"  fibers_built={fi+1} targets={len(target_ids)}",flush=True)
    F=len(fiber_rows); T=len(target_ids)
    S=0; f0=1; t0=f0+F; sink=t0+T; flow=Dinic(sink+1)
    for i,(d,row,k) in enumerate(fiber_rows):
        flow.add(S,f0+i,d)
        for t in row: flow.add(f0+i,t0+t,d)
    for j in range(T): flow.add(t0+j,sink,scale)
    print(f"  flow_nodes={sink+1} fibers={F} targets={T} demand={total_demand} target_capacity={scale*T} max_fiber_demand={max_demand}",flush=True)
    got,level=flow.maxflow(S,sink,total_demand)
    print(f"  max_flow={got}/{total_demand} saturated={got==total_demand}",flush=True)
    if got<total_demand:
        # Residual source side is a weighted Hall-deficient fiber set.
        reachable=[i for i in range(F) if level[f0+i]>=0]
        neigh=set()
        demand=sum(fiber_rows[i][0] for i in reachable)
        for i in reachable: neigh.update(fiber_rows[i][1])
        print(f"  mincut_reachable_fibers={len(reachable)} neighborhood_targets={len(neigh)}")
        print(f"  witness_scaled_demand={demand} target_capacity={scale*len(neigh)} deficiency={demand-scale*len(neigh)}")
        print(f"  witness_cut_profile={sorted(Counter(fiber_rows[i][2] for i in reachable).items())}")
    assert got==total_demand


if __name__=="__main__":
    run(8,12)
    run(10,12)
