#!/usr/bin/env python3
"""Exact pair Hall-slack census for the PF-I16 leaf-last graphs."""
from collections import Counter
from verify_pf_i16_simultaneous_three_edge_flexibility import build_case


def run(n):
    rows, _, metadata = build_case(n)
    targets = sorted(set().union(*rows))
    bit = {t: 1 << i for i, t in enumerate(targets)}
    masks = []
    for row in rows:
        m = 0
        for t in row:
            m |= bit[t]
        masks.append(m)
    minimum = None
    pairs = []
    hist = Counter()
    for i in range(len(rows)):
        for j in range(i + 1, len(rows)):
            slack = (masks[i] | masks[j]).bit_count() - 2
            hist[slack] += 1
            if minimum is None or slack < minimum:
                minimum = slack
                pairs = [(i, j)]
            elif slack == minimum:
                pairs.append((i, j))
    print(f"n={n}: sources={len(rows)}, targets={len(targets)}, "
          f"source_pairs={len(rows)*(len(rows)-1)//2}")
    print(f"  minimum_pair_slack={minimum}, minimizing_pairs={len(pairs)}")
    for i, j in pairs[:100]:
        same_parent = metadata[i]["parent"] == metadata[j]["parent"]
        same_matching = metadata[i]["intervals"] == metadata[j]["intervals"]
        print(f"    pair=({i},{j}), same_parent={same_parent}, "
              f"same_matching={same_matching}, "
              f"left_i={metadata[i]}, left_j={metadata[j]}")
    for slack in sorted(hist):
        print(f"  slack={slack}: pairs={hist[slack]}")


if __name__ == "__main__":
    run(6)
    run(8)
