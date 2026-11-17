#!/usr/bin/env python3
"""Exact Hall-slack census over unions of complete parent fibers.

At n=8 there are 22 parent fibers, so all 2^22 unions are enumerable even
though there are 608 individual child sources. This tests whether the low
slack seen at n=6 has a parent-fiber-level analogue.
"""
from collections import Counter, defaultdict
from verify_pf_i16_simultaneous_three_edge_flexibility import build_case


def run(n):
    rows, _, metadata = build_case(n)
    fibers = defaultdict(list)
    for i, meta in enumerate(metadata):
        fibers[meta["parent"]].append(i)
    fiber_keys = sorted(fibers, key=repr)
    F = len(fiber_keys)
    targets = sorted(set().union(*rows))
    target_bit = {t: 1 << i for i, t in enumerate(targets)}
    fiber_masks = []
    fiber_sizes = []
    for key in fiber_keys:
        mask = 0
        for source in fibers[key]:
            for tree in rows[source]:
                mask |= target_bit[tree]
        fiber_masks.append(mask)
        fiber_sizes.append(len(fibers[key]))

    unions = [0] * (1 << F)
    sizes = [0] * (1 << F)
    min_slack = None
    minima = []
    by_cardinality = defaultdict(Counter)
    for subset in range(1, 1 << F):
        bit = subset & -subset
        i = bit.bit_length() - 1
        prev = subset ^ bit
        unions[subset] = unions[prev] | fiber_masks[i]
        sizes[subset] = sizes[prev] + fiber_sizes[i]
        slack = unions[subset].bit_count() - sizes[subset]
        by_cardinality[subset.bit_count()][slack] += 1
        if min_slack is None or slack < min_slack:
            min_slack = slack
            minima = [subset]
        elif slack == min_slack:
            minima.append(subset)

    print(f"n={n}: sources={len(rows)}, targets={len(targets)}, "
          f"parent_fibers={F}, nonempty_fiber_unions={(1<<F)-1}")
    print(f"  minimum_fiber_union_slack={min_slack}, "
          f"minimizers={len(minima)}")
    for subset in minima:
        ids = [i for i in range(F) if subset & (1 << i)]
        source_count = sizes[subset]
        target_count = unions[subset].bit_count()
        print(f"    fibers={ids}, fiber_sizes={[fiber_sizes[i] for i in ids]}, "
              f"sources={source_count}, targets={target_count}")
        for i in ids:
            print(f"      parent[{i}]={fiber_keys[i]}")
    for k in sorted(by_cardinality):
        vals = by_cardinality[k]
        print(f"  fiber_count={k}: min_slack={min(vals)}, "
              f"zero={vals[0]}, one={vals[1]}, two={vals[2]}")
    return min_slack


if __name__ == "__main__":
    run(6)
    run(8)
