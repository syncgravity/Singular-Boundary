#!/usr/bin/env python3
"""Exact test of the blockwise row-normalized split-demand allocation.

For each first-crowded-cut fiber F in X_k, this tests the sufficient
allocation lambda(F,T)=delta(F)/|N_k(F)| on T in N_k(F), where
N_k(F)=N(F) intersect Y_k. The test is diagnostic: a failure rejects this
allocation only, not blockwise Hall or the multivalued-pi Hall theorem.
"""
from collections import Counter, defaultdict
from fractions import Fraction

from verify_pf_i16_source_dependent_leaf_peeling import (
    sources, parent_data, canonical_leaf, inverse_last_switch, compress_tree,
)
from verify_pf_i16_local_switch_fractional_transport import candidate_outputs
from verify_pf_i16_fixed_parent_leaf_fiber_expansion import nonroot_leaf_indices


EXPECTED = {6: 22, 8: 608, 10: 31744}


def first_crowded_cut(edges, n, threshold):
    for k in range(1, n, 2):
        if sum(a <= k < b for a, b in edges) >= threshold:
            return k
    return None


def run(n):
    all_sources = list(sources(n))
    assert len(all_sources) == EXPECTED[n], (n, len(all_sources))
    fibers = defaultdict(list)
    terminal_sources = 0
    for iv, tau in all_sources:
        k = first_crowded_cut(iv, n, 3)
        if k is None:
            terminal_sources += 1
            continue
        for leaf in nonroot_leaf_indices(iv, tau):
            J = iv[leaf]
            p = parent_data(iv, tau, leaf)
            fibers[(p, J, k)].append((iv, tau, leaf))

    parent_cache = {}
    target_block_cache = {}
    target_load = defaultdict(Fraction)
    target_incidents = defaultdict(list)
    row_sizes = Counter()
    empty = []
    fiber_count_by_cut = Counter()
    target_count_by_cut = Counter()
    incidence_count_by_cut = Counter()
    demand_by_cut = Counter()
    source_count_by_cut = Counter()

    for (p, J, k), children in fibers.items():
        fiber_count_by_cut[k] += 1
        demand = Fraction(0)
        for iv, tau, leaf in children:
            d = len(nonroot_leaf_indices(iv, tau))
            demand += Fraction(1, d)
            source_count_by_cut[k] += 1
        iv, tau, leaf = children[0]
        raw = candidate_outputs(iv, tau, forced_last=leaf)
        for civ, ctau, cleaf in children[1:]:
            assert candidate_outputs(civ, ctau, forced_last=cleaf) == raw

        if p not in parent_cache:
            pi, pt = p
            if len(pi) == 1:
                parent_cache[p] = {((1, 2),)}
            else:
                pl = canonical_leaf(pi, pt)
                parent_cache[p] = candidate_outputs(pi, pt, forced_last=pl)

        retained = set()
        for T in raw:
            inv = inverse_last_switch(T, J, n)
            assert len(inv) == 1, (n, p, J, T, inv)
            projected = compress_tree(next(iter(inv)), set(J), n)
            if projected not in parent_cache[p]:
                continue
            if T not in target_block_cache:
                target_block_cache[T] = first_crowded_cut(T, n, 2)
            if target_block_cache[T] == k:
                retained.add(T)

        demand_by_cut[k] += demand
        row_sizes[len(retained)] += 1
        if not retained:
            empty.append((k, p, J, demand, len(children)))
            continue

        share = demand / len(retained)
        for T in retained:
            target_load[T] += share
            target_incidents[T].append((p, J, demand, len(retained), share))
            incidence_count_by_cut[k] += 1
            target_count_by_cut[k] += 1

    # Distinct target counts, rather than incidences.
    distinct_targets_by_cut = Counter()
    for T in target_load:
        k = target_block_cache[T]
        distinct_targets_by_cut[k] += 1

    print(f"RNL_BLOCKWISE n={n} sources={len(all_sources)} terminal_sources={terminal_sources}")
    print(f"  fibers={len(fibers)} parent_sources={len(parent_cache)}")
    print(f"  fibers_by_cut={sorted(fiber_count_by_cut.items())}")
    print(f"  exact_demand_by_cut={[(k,str(v)) for k,v in sorted(demand_by_cut.items())]}")
    print(f"  distinct_targets_by_cut={sorted(distinct_targets_by_cut.items())}")
    print(f"  positive_incidences_by_cut={sorted(incidence_count_by_cut.items())}")
    print(f"  same_block_row_size_histogram={sorted(row_sizes.items())}")
    if empty:
        k,p,J,demand,child_count=empty[0]
        print(f"  EMPTY_ROW_COUNT={len(empty)} first_empty=(cut={k},J={J},demand={demand},children={child_count},parent={p})")
    else:
        print("  EMPTY_ROW_COUNT=0")

    for k in sorted(fiber_count_by_cut):
        loads = [(v,T) for T,v in target_load.items() if target_block_cache[T] == k]
        if not loads:
            print(f"  cut={k} NO_TARGET_LOADS")
            continue
        maximum = max(v for v,_ in loads)
        overloaded = [(v,T) for v,T in loads if v > 1]
        print(f"  cut={k} max_load={maximum} overloaded_targets={len(overloaded)}")
        if overloaded:
            v,T=max(overloaded,key=lambda item:item[0])
            print(f"  cut={k} first_max_overload={v} target={T}")
            for p,J,demand,row_size,share in sorted(
                target_incidents[T], key=lambda x:(x[2],x[3],x[1])
            ):
                print(f"    incident J={J} demand={demand} row_size={row_size} share={share} parent={p}")

    passed = not empty and all(v <= 1 for v in target_load.values())
    print(f"  RNL_BLOCKWISE_RESULT={'PASS' if passed else 'FAIL'}")
    return passed


if __name__ == "__main__":
    results = [run(n) for n in (6, 8, 10)]
    print("OVERALL_RNL_BLOCKWISE=" + ("PASS" if all(results) else "FAIL"))
