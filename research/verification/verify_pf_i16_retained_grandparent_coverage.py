#!/usr/bin/env python3
"""Test whether every ordinary source output is retained by multivalued pi.

For each source r, enumerate all ordinary guarded outputs U. For every
non-root leaf L, reverse the final L-switch, and retain U through L exactly
when the projected parent target lies in the canonical leaf-last neighborhood
of pi_L(r). Compare the union of these retained rows with the full ordinary
neighborhood.

The n=6 case is covered by Theorem 3.1 in the retained-grandparent audit.
The n=8 case is the first possible obstruction: deleting a final leaf can
leave a three-interval parent whose canonical neighborhood is strict.
This is a finite diagnostic, not a sibling-diamond theorem or an
all-orders Hall proof.
"""
from collections import Counter

from verify_pf_i16_source_dependent_leaf_peeling import (
    sources, canonical_leaf, parent_data, inverse_last_switch, compress_tree,
)
from verify_pf_i16_local_switch_fractional_transport import candidate_outputs


def nonroot_leaves(intervals, tau):
    degree = [0] * len(intervals)
    for a, b in tau:
        degree[a] += 1
        degree[b] += 1
    root = next(i for i, I in enumerate(intervals) if I[0] == 1)
    return [i for i, d in enumerate(degree) if d == 1 and i != root]


def parent_canonical_outputs(parent):
    intervals, tau = parent
    if len(intervals) == 1:
        return candidate_outputs(intervals, tau)
    leaf = canonical_leaf(intervals, tau)
    return candidate_outputs(intervals, tau, forced_last=leaf)


def run(n, expected_sources):
    all_sources = list(sources(n))
    assert len(all_sources) == expected_sources, (n, len(all_sources))
    parent_cache = {}
    total_ordinary = 0
    total_retained = 0
    strict_sources = 0
    missing_hist = Counter()
    first_witness = None

    for idx, (intervals, tau) in enumerate(all_sources):
        leaves = nonroot_leaves(intervals, tau)
        ordinary = candidate_outputs(intervals, tau)
        raw_union = set()
        retained = set()
        per_leaf = {}

        for leaf in leaves:
            J = intervals[leaf]
            parent = parent_data(intervals, tau, leaf)
            if parent not in parent_cache:
                parent_cache[parent] = parent_canonical_outputs(parent)
            parent_targets = parent_cache[parent]
            raw = candidate_outputs(intervals, tau, forced_last=leaf)
            raw_union.update(raw)
            accepted = set()
            for T in raw:
                inv = inverse_last_switch(T, J, n)
                assert len(inv) == 1, (n, intervals, tau, J, T, inv)
                P = compress_tree(next(iter(inv)), set(J), n)
                if P in parent_targets:
                    accepted.add(T)
            per_leaf[leaf] = (parent, raw, accepted)
            retained.update(accepted)

        assert raw_union == ordinary, (
            "union over all final leaves did not recover ordinary outputs",
            n, intervals, tau, len(raw_union), len(ordinary),
        )
        missed = ordinary - retained
        total_ordinary += len(ordinary)
        total_retained += len(retained)
        if missed:
            strict_sources += 1
            missing_hist[len(missed)] += 1
            if first_witness is None:
                U = min(missed)
                witnesses = []
                for leaf, (parent, raw, accepted) in per_leaf.items():
                    if U in raw:
                        J = intervals[leaf]
                        inv = inverse_last_switch(U, J, n)
                        P = compress_tree(next(iter(inv)), set(J), n)
                        witnesses.append({
                            "leaf": J,
                            "parent": parent,
                            "projected_parent_target": P,
                            "parent_target_is_canonical": P in parent_cache[parent],
                        })
                first_witness = {
                    "source": (intervals, tau),
                    "target": U,
                    "nonroot_leaves": [intervals[L] for L in leaves],
                    "leaf_projections": witnesses,
                }

        if (idx + 1) % 100 == 0:
            print(f"  n={n} sources_checked={idx+1}/{len(all_sources)} "
                  f"parent_sources_cached={len(parent_cache)}", flush=True)

    print(f"n={n} sources={len(all_sources)} distinct_parent_sources={len(parent_cache)}")
    print(f"  ordinary_source_target_incidences={total_ordinary}")
    print(f"  retained_source_target_incidences={total_retained}")
    print(f"  sources_with_strict_retained_subset={strict_sources}")
    print(f"  missed_output_count_histogram={dict(sorted(missing_hist.items()))}")
    if first_witness is None:
        print("RESULT: every ordinary output is retained at this finite order.")
    else:
        print("FIRST_MISSED_OUTPUT_WITNESS:")
        print(first_witness)
        print("RESULT: universal ordinary-to-retained coverage fails at this finite order.")
    return first_witness


if __name__ == "__main__":
    assert run(6, 22) is None
    run(8, 608)
