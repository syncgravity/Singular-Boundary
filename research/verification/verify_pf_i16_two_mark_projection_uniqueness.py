#!/usr/bin/env python3
"""Exact finite census of two-mark projection stability for PF-I16.

For each source x=(M,tau), each pair of eligible non-root leaves J,K,
and each target T retained through both marks, compute the two compressed
parent targets P_J(T), P_K(T). Group common targets by the ordered pair
(P,Q). The group containing T is exactly the finite set of common retained
targets with the same two reverse-mark projections.

This is a finite diagnostic, not an all-orders theorem. It tests whether a
target-changing exchange square can preserve both projected parent targets.
"""
from collections import Counter, defaultdict

from verify_pf_i16_source_dependent_leaf_peeling import (
    sources,
    inverse_last_switch,
    compress_tree,
)
from verify_pf_i16_local_switch_fractional_transport import candidate_outputs
from verify_pf_i16_fixed_parent_leaf_fiber_expansion import nonroot_leaf_indices


def census(n, expected_sources):
    source_count = 0
    leaf_pair_count = 0
    common_target_incidences = 0
    stable_group_histogram = Counter()
    largest_stable_group = 0
    first_nonunique = None

    for intervals, tau in sources(n):
        source_count += 1
        leaves = nonroot_leaf_indices(intervals, tau)
        if len(leaves) < 2:
            continue

        rows = {
            j: candidate_outputs(intervals, tau, forced_last=j)
            for j in leaves
        }
        projections = {}
        for j in leaves:
            J = intervals[j]
            projections[j] = {}
            for target in rows[j]:
                inverse = inverse_last_switch(target, J, n)
                assert inverse is not None, (n, intervals, tau, J, target)
                projections[j][target] = compress_tree(inverse, set(J), n)

        for i, j in enumerate(leaves):
            for k in leaves[i + 1:]:
                leaf_pair_count += 1
                common = rows[j] & rows[k]
                common_target_incidences += len(common)

                # A target T' belongs to L_J^K(P;Q) exactly when it is
                # common to the J-last and K-last rows and has projections
                # (P,Q). Grouping therefore computes every stable set.
                groups = defaultdict(list)
                for target in common:
                    key = (projections[j][target], projections[k][target])
                    groups[key].append(target)

                for (P, Q), targets in groups.items():
                    size = len(targets)
                    stable_group_histogram[size] += 1
                    largest_stable_group = max(largest_stable_group, size)
                    if size > 1 and first_nonunique is None:
                        first_nonunique = (
                            intervals, tau, intervals[j], intervals[k],
                            P, Q, tuple(sorted(targets)),
                        )

    assert source_count == expected_sources, (n, source_count)
    assert stable_group_histogram, (n, "no simultaneous two-mark targets")
    print(
        f"n={n}: sources={source_count}, eligible_leaf_pairs={leaf_pair_count}, "
        f"common_target_incidences={common_target_incidences}, "
        f"projection_pair_groups={sum(stable_group_histogram.values())}, "
        f"stable_group_histogram={dict(sorted(stable_group_histogram.items()))}, "
        f"largest_stable_group={largest_stable_group}"
    )
    if first_nonunique is not None:
        print(f"  first_nonunique={first_nonunique}")
    assert largest_stable_group == 1, (n, first_nonunique)
    return {
        "sources": source_count,
        "leaf_pairs": leaf_pair_count,
        "common_target_incidences": common_target_incidences,
        "stable_group_histogram": dict(stable_group_histogram),
        "largest_stable_group": largest_stable_group,
    }


def main():
    census(6, expected_sources=22)
    census(8, expected_sources=608)
    print(
        "Two-mark projection-uniqueness census complete for n=6,8. "
        "No all-orders result is claimed."
    )


if __name__ == "__main__":
    main()
