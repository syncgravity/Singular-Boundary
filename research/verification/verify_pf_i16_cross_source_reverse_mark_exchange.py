#!/usr/bin/env python3
"""Build the cross-source S / same-source D reverse-mark incidence complex.

A state retains (x,J,P,T), where p=pi_J(x) and P=P_J(T) is the exact
canonical-parent projection. S-edges are sibling-lift moves within a fixed
(p,J,P) block; this verifier explicitly includes distinct child sources.
D-edges are witnessed same-source deletion diamonds at a common target,
with the ordinary common-parent target U retained (not canonicalized).

The graph is a finite structural census at n=6,8. It is not a fractional
capacity allocation, a PFEL proof, or an all-orders Hall theorem.
"""
from __future__ import annotations
import argparse, hashlib, json, sys
from collections import Counter, defaultdict
from fractions import Fraction
from pathlib import Path

import verify_pf_i16_projection_shifting_transitions as base
from verify_pf_i16_source_dependent_leaf_peeling import sources, parent_data
from verify_pf_i16_local_switch_fractional_transport import candidate_outputs
from verify_pf_i16_fixed_parent_leaf_fiber_expansion import nonroot_leaf_indices

sys.setrecursionlimit(100000)

EXPECTED = {
    6: {"sources":22},
    8: {"sources":608},
}

class DSU:
    def __init__(self,n):
        self.p=list(range(n)); self.sz=[1]*n
    def find(self,x):
        while self.p[x]!=x:
            self.p[x]=self.p[self.p[x]]
            x=self.p[x]
        return x
    def union(self,a,b):
        a=self.find(a); b=self.find(b)
        if a==b: return False
        if self.sz[a]<self.sz[b]: a,b=b,a
        self.p[b]=a; self.sz[a]+=self.sz[b]
        return True

def run(n):
    parent_cache={}
    source_rows={}
    block_ids={}
    block_sources=defaultdict(set)
    block_targets=defaultdict(set)
    block_source_targets=defaultdict(dict)
    fiber_sources=defaultdict(set)
    fiber_demand=defaultdict(lambda: 0)
    source_target_marks=defaultdict(list)
    target_blocks=defaultdict(lambda: defaultdict(set))
    state_count=0
    raw_outputs=0
    retained_outputs=0
    inverse_rejects=0
    canonical_rejects=0

    for source_index,(intervals,tau) in enumerate(sources(n)):
        leaves=nonroot_leaf_indices(intervals,tau)
        d=len(leaves)
        source_rows[source_index]=(intervals,tau,leaves,d)
        for Jidx in leaves:
            J=intervals[Jidx]
            parent=parent_data(intervals,tau,Jidx)
            fiber=(parent,J)
            fiber_sources[fiber].add(source_index)
            fiber_demand[fiber] += 1/d
            C=base.canonical_parent_targets(parent,parent_cache)
            raw=candidate_outputs(intervals,tau,forced_last=Jidx)
            raw_outputs+=len(raw)
            by_parent_target=defaultdict(set)
            for T in raw:
                inv=base.exact_guarded_inverse(T,J,n)
                if inv is None:
                    inverse_rejects+=1
                    continue
                P=base.compress_tree(inv[0],set(J),n)
                if P not in C:
                    canonical_rejects+=1
                    continue
                by_parent_target[P].add(T)
            if set(by_parent_target)!=set(C):
                raise AssertionError(("parent target coverage mismatch",n,source_index,J,
                                      len(C),len(by_parent_target)))
            for P,Ts in by_parent_target.items():
                key=(parent,J,P)
                if key not in block_ids:
                    block_ids[key]=len(block_ids)
                bid=block_ids[key]
                old=block_source_targets[bid].get(source_index)
                if old is not None and old!=frozenset(Ts):
                    raise AssertionError(("same source/block row changed",n,source_index,key))
                block_source_targets[bid][source_index]=frozenset(Ts)
                block_sources[bid].add(source_index)
                block_targets[bid].update(Ts)
                retained_outputs+=len(Ts)
                for T in Ts:
                    source_target_marks[(source_index,T)].append((Jidx,bid,P))
                    target_blocks[T][bid].add(source_index)

    source_count=len(source_rows)
    assert source_count==EXPECTED[n]["sources"],(n,source_count)
    # Verify the fixed-(p,J,P) cross-source block is exactly a Cartesian
    # product of its child sources and lift targets.
    block_rows=[]
    s_edge_count=0
    cross_source_s_edges=0
    same_source_s_edges=0
    cross_source_same_target_pairs=0
    total_states=0
    for key,bid in block_ids.items():
        srcs=sorted(block_sources[bid])
        Ts=sorted(block_targets[bid])
        for si in srcs:
            assert block_source_targets[bid][si]==frozenset(Ts),(
                "cross-source lift rows differ",n,key,si,len(Ts),
                len(block_source_targets[bid][si]))
        ns,nt=len(srcs),len(Ts)
        states=ns*nt
        total_states+=states
        # S edges join two incidence states when the parent block (p,J,P)
        # is fixed and the child target changes. Count unordered edges.
        same_source_s_edges += ns*(nt*(nt-1)//2)
        cross_source_s_edges += (ns*(ns-1)//2)*(nt*(nt-1)//2)*2
        cross_source_same_target_pairs += (ns*(ns-1)//2)*nt
        s_edge_count += same_source_s_edges + cross_source_s_edges
        block_rows.append({
            "block_id":bid,"parent_source":key[0],"deleted_interval":list(key[1]),
            "parent_target":base.encode_tree(key[2]),"child_source_count":ns,
            "lift_target_count":nt,"incidence_state_count":states,
            "split_demand_before_parent_target_choice":str(sum(
                (Fraction(1,source_rows[si][3]) for si in srcs),Fraction(0))),
            "same_source_S_edges":ns*(nt*(nt-1)//2),
            "cross_source_target_changing_S_edges":
                (ns*(ns-1)//2)*(nt*(nt-1)//2)*2,
            "cross_source_same_target_state_pairs":
                (ns*(ns-1)//2)*nt,
        })

    # Each source/target pair can carry multiple reverse marks. Add D edges
    # only when the exact two guarded inverses survive and their ordinary
    # common-parent target U is certified by base.mutual_diamond.
    dsu=DSU(len(block_ids))
    ordinary_cache={}
    diamond_cache={}
    d_edges=[]
    d_rejects=0
    same_target_non_diamond_pairs=0
    same_target_cross_source_pairs=0
    target_collision_hist=Counter()
    non_diamond_by_target=[]
    for T,owners in target_blocks.items():
        incidences=[]
        for bid,srcs in owners.items():
            for si in srcs:
                incidences.append((si,bid))
        target_collision_hist[len(incidences)]+=1
        for i in range(len(incidences)):
            si,bi=incidences[i]
            for sj,bj in incidences[i+1:]:
                if si!=sj:
                    same_target_cross_source_pairs+=1
                    if bi!=bj:
                        same_target_non_diamond_pairs+=1
        if len(incidences)>1:
            non_diamond_by_target.append((T,len(incidences),len(owners),len({x[0] for x in incidences})))

    for (si,T),marks in source_target_marks.items():
        # One source has at most one state per mark/target, but keep the exact
        # parent-target projection in the record.
        marks=sorted(set(marks),key=lambda z:z[0])
        if len(marks)<2:
            continue
        intervals,tau,leaves,d=source_rows[si]
        mark_to_idx={intervals[j]:j for j in leaves}
        for i in range(len(marks)):
            Jidx,bJ,P=marks[i]
            for Kidx,bK,Q in marks[i+1:]:
                witness=base.mutual_diamond(
                    T,intervals,tau,Jidx,Kidx,n,si,ordinary_cache,diamond_cache)
                if witness is None:
                    d_rejects+=1
                    continue
                # The D-edge retains the ordinary common-parent target U.
                U=witness["U"]
                dsu.union(bJ,bK)
                d_edges.append((bJ,bK,si,T,Jidx,Kidx,P,Q,U))

    # Components of the block graph under witnessed D edges; S-connected
    # blocks are already represented by their block vertices.
    comps=defaultdict(list)
    for bid in range(len(block_ids)):
        comps[dsu.find(bid)].append(bid)
    comp_rows=[]
    comp_size_hist=Counter()
    for bids in comps.values():
        srcset=set(); tgtset=set(); demand=0
        for bid in bids:
            srcset.update(block_sources[bid])
            tgtset.update(block_targets[bid])
            demand += sum((Fraction(1,source_rows[si][3]) for si in block_sources[bid]),Fraction(0))
        comp_size_hist[len(bids)]+=1
        comp_rows.append({"blocks":len(bids),"distinct_sources":len(srcset),
                          "distinct_targets":len(tgtset),
                          "target_capacity":len(tgtset),
                          "sum_of_block_source_demands_before_P_choice":str(demand)})
    comp_rows.sort(key=lambda x:(-x["blocks"],-x["distinct_sources"],-x["distinct_targets"]))

    # Determine whether cross-source target collisions lie inside one D/S
    # component after the S blocks are contracted.
    connected_non_diamond=0
    disconnected_non_diamond=0
    for T,owners in target_blocks.items():
        inc=[(si,bid) for bid,srcs in owners.items() for si in srcs]
        for i,(si,bi) in enumerate(inc):
            for sj,bj in inc[i+1:]:
                if si==sj or bi==bj:
                    continue
                if dsu.find(bi)==dsu.find(bj):
                    connected_non_diamond+=1
                else:
                    disconnected_non_diamond+=1

    result={
        "schema":"PF-I16-CROSS-SOURCE-REVERSE-MARK-EXCHANGE-v1",
        "order":n,
        "source_count":source_count,
        "counts":{
            "parent_leaf_fibers":len(fiber_sources),
            "parent_target_blocks":len(block_ids),
            "source_mark_incidences":sum(len(v) for v in fiber_sources.values()),
            "source_parent_target_child_target_states":total_states,
            "distinct_child_targets":len(target_blocks),
            "raw_forced_leaf_outputs":raw_outputs,
            "retained_parent_canonical_outputs":retained_outputs,
            "fixed_parent_target_block_cartesian_checks":sum(len(v) for v in block_sources.values()),
            "blocks_with_multiple_child_sources":sum(len(v)>1 for v in block_sources.values()),
            "max_child_sources_per_block":max((len(v) for v in block_sources.values()),default=0),
            "max_lift_targets_per_block":max((len(v) for v in block_targets.values()),default=0),
            "same_source_S_edges":same_source_s_edges,
            "cross_source_target_changing_S_edges":cross_source_s_edges,
            "cross_source_same_target_state_pairs":cross_source_same_target_pairs,
            "D_diamond_witnesses":len(d_edges),
            "D_diamond_rejections":d_rejects,
            "D_connected_block_pairs":len({tuple(sorted((a,b))) for a,b,*_ in d_edges}),
            "non_diamond_cross_source_target_collision_pairs":same_target_non_diamond_pairs,
            "cross_source_target_collision_pairs_total":same_target_cross_source_pairs,
            "non_diamond_pairs_connected_by_global_S_D_paths":connected_non_diamond,
            "non_diamond_pairs_in_distinct_components":disconnected_non_diamond,
            "S_D_block_components":len(comps),
            "S_D_component_block_size_histogram":dict(sorted(comp_size_hist.items())),
            "largest_components":comp_rows[:20],
            "target_incidence_multiplicity_histogram":dict(sorted(target_collision_hist.items())),
        },
        "scope":{
            "S_edges": "all target-changing sibling-lift edges within fixed (p,J,P), including distinct child sources",
            "D_edges": "same-source mutually surviving reverse-mark diamonds with exact common ordinary-parent U",
            "nonclaims":[
                "the duplicated block demand fields are diagnostics before choosing an allocation over parent targets P",
                "component connectivity is not a fractional capacity allocation or a Hall proof",
                "non-diamond collisions may remain even when their block endpoints are connected by longer S/D paths",
                "no source-derived Z5 or helical phase map is used"
            ]
        },
        "blocks":block_rows,
        "D_edges":[],
    }
    # Emit compact, explicit D witnesses without serializing source internals.
    result["D_edges"]=[
        {"block_left":a,"block_right":b,"source_index":si,"target":base.encode_tree(T),
         "J_index":J,"K_index":K,"P":base.encode_tree(P),"Q":base.encode_tree(Q),
         "ordinary_U":base.encode_tree(U)}
        for a,b,si,T,J,K,P,Q,U in d_edges
    ]
    canonical=json.dumps(result,sort_keys=True,separators=(",",":")).encode()
    result["canonical_sha256"]=hashlib.sha256(canonical).hexdigest()
    print(json.dumps(result["counts"],sort_keys=True))
    return result

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--output",default="pf_i16_cross_source_reverse_mark_exchange.json")
    args=ap.parse_args()
    reports=[run(6),run(8)]
    payload={"schema":"PF-I16-CROSS-SOURCE-REVERSE-MARK-EXCHANGE-BATCH-v1",
             "orders":reports,
             "conclusion":"Finite cross-source S/D incidence census only; PFEL and Hall remain open."}
    Path(args.output).write_text(json.dumps(payload,sort_keys=True,indent=2)+"\n")
    print("wrote",args.output)

if __name__=="__main__":
    main()
