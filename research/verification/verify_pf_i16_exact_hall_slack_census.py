#!/usr/bin/env python3
"""Exact Hall-slack census for the n=6 PF-I16 leaf-last graph.

The graph has 22 source vertices, so every source subset is enumerated.
Neighborhoods are represented as Python integer bitsets; the census is exact.
"""
from collections import Counter, defaultdict
from verify_pf_i16_simultaneous_three_edge_flexibility import build_case


def run(n=6):
    rows, requirements, metadata = build_case(n)
    assert len(rows) == 22, (n, len(rows))
    targets = sorted(set().union(*rows))
    target_bit = {t: 1 << i for i, t in enumerate(targets)}
    row_masks = []
    for row in rows:
        mask = 0
        for t in row:
            mask |= target_bit[t]
        row_masks.append(mask)

    N = len(rows)
    unions = [0] * (1 << N)
    by_size = defaultdict(Counter)
    zero_sets = []
    one_sets = []
    min_sets = []
    min_slack = N + len(targets)
    for mask in range(1, 1 << N):
        bit = mask & -mask
        i = bit.bit_length() - 1
        prev = mask ^ bit
        unions[mask] = unions[prev] | row_masks[i]
        size = mask.bit_count()
        slack = unions[mask].bit_count() - size
        by_size[size][slack] += 1
        if slack < min_slack:
            min_slack = slack
            min_sets = [mask]
        elif slack == min_slack:
            min_sets.append(mask)
        if slack == 0:
            zero_sets.append(mask)
        elif slack == 1:
            one_sets.append(mask)

    print(f"n={n}: sources={N}, targets={len(targets)}, subsets={(1<<N)-1}")
    print(f"  minimum_nonempty_Hall_slack={min_slack}")
    print(f"  subsets_attaining_minimum={len(min_sets)}")
    for m in sorted(min_sets, key=lambda z: (z.bit_count(), z)):
        ids = [i for i in range(N) if m & (1 << i)]
        fibers = Counter(metadata[i]["parent"] for i in ids)
        neigh_mask = unions[m]
        neigh_ids = [j for j in range(len(targets)) if neigh_mask & (1 << j)]
        neigh_trees = [targets[j] for j in neigh_ids]
        print(f"    minimum_set_sources={ids}, size={len(ids)}, "
              f"neighborhood_size={len(neigh_trees)}, "
              f"parent_fiber_sizes={sorted(fibers.values())}")
        for tree in neigh_trees:
            print(f"      critical_target={tree}")
    print(f"  zero_slack_subsets={len(zero_sets)}, one_slack_subsets={len(one_sets)}")
    for size in sorted(by_size):
        c = by_size[size]
        print(f"  size={size}: min_slack={min(c)}, zero={c[0]}, one={c[1]}")

    # Inclusion-minimal tight sets are the most immediate exchange bottlenecks.
    zero_set = set(zero_sets)
    minimal_tight = [
        m for m in zero_sets
        if not any((m ^ (1 << i)) in zero_set
                   for i in range(N) if m & (1 << i))
    ]
    print(f"  inclusion_minimal_tight_sets={len(minimal_tight)}")
    for m in minimal_tight[:40]:
        ids = [i for i in range(N) if m & (1 << i)]
        fibers = Counter(metadata[i]["parent"] for i in ids)
        print(f"    tight_sources={ids}, size={len(ids)}, parent_fiber_sizes={sorted(fibers.values())}")

    # Small low-slack sets with parent-fiber composition.
    print("  smallest_one_slack_sets:")
    for m in sorted(one_sets, key=lambda z: (z.bit_count(), z))[:30]:
        ids = [i for i in range(N) if m & (1 << i)]
        fibers = Counter(metadata[i]["parent"] for i in ids)
        print(f"    sources={ids}, size={len(ids)}, fibers={sorted(fibers.values())}")

    # For every tight set A, report how many targets its neighborhood contains.
    for m in minimal_tight[:20]:
        ids = [i for i in range(N) if m & (1 << i)]
        neigh = unions[m].bit_count()
        print(f"  tight_certificate: |A|={len(ids)}, |N(A)|={neigh}, sources={ids}")


if __name__ == "__main__":
    run()
