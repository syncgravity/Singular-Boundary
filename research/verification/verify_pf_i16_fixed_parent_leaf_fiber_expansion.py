#!/usr/bin/env python3
"""Verify the fixed-(parent source, deleted interval) fiber expansion lemma."""
from collections import defaultdict, Counter
from fractions import Fraction

from verify_pf_i16_source_dependent_leaf_peeling import (
    sources, canonical_leaf, parent_data, inverse_last_switch, compress_tree,
)
from verify_pf_i16_local_switch_fractional_transport import candidate_outputs


def nonroot_leaf_indices(intervals, tau):
    degree = [0] * len(intervals)
    for a, b in tau:
        degree[a] += 1
        degree[b] += 1
    root = next(i for i, I in enumerate(intervals) if I[0] == 1)
    return [i for i, d in enumerate(degree) if d == 1 and i != root]


def check(n, expected_sources):
    fibers = defaultdict(list)
    source_count = 0
    for intervals, tau in sources(n):
        leaves = nonroot_leaf_indices(intervals, tau)
        for leaf in leaves:
            J = intervals[leaf]
            parent = parent_data(intervals, tau, leaf)
            fibers[(parent, J)].append((intervals, tau, leaf))
        source_count += 1
    assert source_count == expected_sources

    total_parent_targets = 0
    total_lifts = 0
    min_lifts_per_parent_target = None
    max_fiber_size = 0
    min_neighborhood_slack = None
    checked = 0
    parent_demand = Counter()
    parent_capacity = {}
    quotient_column_load = Counter()

    for (parent, J), children in fibers.items():
        pi, pt = parent
        nchild = n
        s = n // 2
        assert len(children) <= s - 1
        max_fiber_size = max(max_fiber_size, len(children))

        # The child leaf-last row depends only on (parent,J), not on which
        # parent interval is the unique overlap-tree neighbor of J.
        child_rows = []
        for intervals, tau, leaf in children:
            child_rows.append(candidate_outputs(intervals, tau,
                                                forced_last=leaf))
        assert all(row == child_rows[0] for row in child_rows[1:]), (
            "same (parent,J) fiber has different child neighborhoods",
            n, parent, J,
        )

        parent_leaf = canonical_leaf(pi, pt)
        parent_targets = candidate_outputs(pi, pt, forced_last=parent_leaf)
        lift_counts = Counter()
        for T in child_rows[0]:
            inverse = inverse_last_switch(T, J, nchild)
            assert len(inverse) == 1
            P = compress_tree(next(iter(inverse)), set(J), nchild)
            if P in parent_targets:
                lift_counts[P] += 1

        assert set(lift_counts) == set(parent_targets), (
            "a canonical parent target has no child lift", n, parent, J,
            len(parent_targets), len(lift_counts),
        )
        local_min = min(lift_counts.values())
        assert local_min >= 2, (
            "fewer than two child lifts for a fixed parent target",
            n, parent, J, min(lift_counts.values()),
        )
        retained = sum(lift_counts.values())
        weight = len(children)
        parent_demand[parent] += weight
        parent_capacity[parent] = len(parent_targets)
        row = set(T for T in child_rows[0]
                  if compress_tree(next(iter(inverse_last_switch(T, J, nchild))),
                                   set(J), nchild) in parent_targets)
        assert len(row) == retained
        mass = Fraction(weight, len(row))
        for T in row:
            quotient_column_load[T] += mass
        assert retained >= 2 * len(parent_targets)
        assert retained >= 2 ** (s - 1)
        assert retained >= len(children)
        slack = retained - len(children)
        min_neighborhood_slack = (slack if min_neighborhood_slack is None
                                  else min(min_neighborhood_slack, slack))
        min_lifts_per_parent_target = (
            local_min if min_lifts_per_parent_target is None
            else min(min_lifts_per_parent_target, local_min)
        )
        total_parent_targets += len(parent_targets)
        total_lifts += retained
        checked += 1

    print(
        f"PASS n={n}: sources={source_count}, fixed_parent_leaf_fibers={checked}, "
        f"fiber_size_max={max_fiber_size}, "
        f"canonical_parent_target_total={total_parent_targets}, "
        f"retained_lift_total={total_lifts}, "
        f"min_lifts_per_parent_target={min_lifts_per_parent_target}, "
        f"min_fiber_Hall_slack={min_neighborhood_slack}, "
        f"parent_demand_range=[{min(parent_demand.values())},{max(parent_demand.values())}], "
        f"parent_capacity_range=[{min(parent_capacity.values())},{max(parent_capacity.values())}], "
        f"max_uniform_quotient_column={float(max(quotient_column_load.values())):.12f}"
    )


def main():
    check(4, 2)
    check(6, 22)
    check(8, 608)
    print("Fixed-(parent,J) local Hall expansion verified.")
    print("This does not establish Hall across different (parent,J) fibers.")


if __name__ == "__main__":
    main()
