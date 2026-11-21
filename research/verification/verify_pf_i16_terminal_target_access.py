#!/usr/bin/env python3
"""Exact test of universal access to the terminal target class Q.

For each nonterminal source, search all non-root leaf fibers. A target is
counted only if it is a guarded leaf-last output whose unique inverse parent
tree belongs to the canonical parent neighborhood. Q means exactly one
crossing edge at every odd cut. This is a finite diagnostic of the proposed
all-orders lemma; it is not itself a proof.
"""
from collections import defaultdict, Counter
from verify_pf_i16_source_dependent_leaf_peeling import (
    sources, parent_data, canonical_leaf, inverse_last_switch, compress_tree,
)
from verify_pf_i16_local_switch_fractional_transport import candidate_outputs
from verify_pf_i16_fixed_parent_leaf_fiber_expansion import nonroot_leaf_indices


def first_overcrowded_cut(intervals, n):
    return next((k for k in range(1, n, 2)
                 if sum(a <= k < b for a, b in intervals) >= 3), None)


def is_terminal_target(T, n):
    return all(sum(a <= k < b for a, b in T) == 1
               for k in range(1, n, 2))


def run(n, expected_sources):
    all_sources = list(sources(n))
    assert len(all_sources) == expected_sources
    fibers = defaultdict(list)
    source_cut = []
    for idx, (iv, tau) in enumerate(all_sources):
        k = first_overcrowded_cut(iv, n)
        source_cut.append(k)
        if k is None:
            continue
        for leaf in nonroot_leaf_indices(iv, tau):
            J = iv[leaf]
            p = parent_data(iv, tau, leaf)
            fibers[(p, J, k)].append((idx, iv, tau, leaf))

    parent_cache = {}
    covered = set()
    tested_fibers = 0
    raw_q_incidence = 0
    retained_q_incidence = 0
    q_targets = set()
    fibers_with_q = 0
    max_fiber = 0

    for (p, J, k), children in fibers.items():
        if all(idx in covered for idx, *_ in children):
            continue
        max_fiber = max(max_fiber, len(children))
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
        for civ, ctau, cleaf in [c[1:] for c in children[1:]]:
            assert candidate_outputs(civ, ctau, forced_last=cleaf) == raw
        tested_fibers += 1
        found = False
        for T in raw:
            if not is_terminal_target(T, n):
                continue
            raw_q_incidence += 1
            inv = inverse_last_switch(T, J, n)
            assert len(inv) == 1
            P = compress_tree(next(iter(inv)), set(J), n)
            if P in parent_targets:
                retained_q_incidence += 1
                q_targets.add(T)
                found = True
        if found:
            fibers_with_q += 1
            covered.update(idx for idx, *_ in children)

    uncovered = [i for i, k in enumerate(source_cut)
                 if k is not None and i not in covered]
    by_cut = Counter(source_cut[i] for i in uncovered)
    total_by_cut = Counter(k for k in source_cut if k is not None)
    print(f"n={n} sources={len(all_sources)} complement={sum(total_by_cut.values())}")
    print(f"  complement_by_first_cut={sorted(total_by_cut.items())}")
    print(f"  fibers_tested={tested_fibers} fibers_with_terminal_Q_neighbor={fibers_with_q}")
    print(f"  raw_Q_incidences={raw_q_incidence} retained_parent_canonical_Q_incidences={retained_q_incidence}")
    print(f"  distinct_retained_Q_targets={len(q_targets)} max_fiber_size_seen={max_fiber}")
    print(f"  uncovered_sources={len(uncovered)} uncovered_by_first_cut={sorted(by_cut.items())}")
    if uncovered:
        print("  first_uncovered_source=", all_sources[uncovered[0]])
    assert not uncovered, f"terminal-Q access fails at n={n}: {len(uncovered)}"


if __name__ == "__main__":
    run(6, 22)
    run(8, 608)
    run(10, 31744)
