#!/usr/bin/env python3
"""Exact triple Hall-slack census for the n=8 PF-I16 leaf-last graph."""
from collections import Counter
from verify_pf_i16_simultaneous_three_edge_flexibility import build_case


def run(n=8):
    rows, _, metadata = build_case(n)
    targets = sorted(set().union(*rows))
    bit = {t: 1 << i for i, t in enumerate(targets)}
    masks = []
    for row in rows:
        m = 0
        for t in row:
            m |= bit[t]
        masks.append(m)

    N = len(rows)
    minimum = None
    minimizers = []
    hist = Counter()
    total = 0
    for i in range(N):
        mi = masks[i]
        for j in range(i + 1, N):
            mij = mi | masks[j]
            for k in range(j + 1, N):
                slack = (mij | masks[k]).bit_count() - 3
                hist[slack] += 1
                total += 1
                if minimum is None or slack < minimum:
                    minimum = slack
                    minimizers = [(i, j, k)]
                elif slack == minimum:
                    minimizers.append((i, j, k))

    print(f"n={n}: sources={N}, targets={len(targets)}, "
          f"source_triples={total}")
    print(f"  minimum_triple_slack={minimum}, minimizing_triples={len(minimizers)}")
    for triple in minimizers[:100]:
        i, j, k = triple
        same_matching = (metadata[i]["intervals"] == metadata[j]["intervals"]
                         == metadata[k]["intervals"])
        same_parent = (metadata[i]["parent"] == metadata[j]["parent"]
                       == metadata[k]["parent"])
        print(f"    triple={triple}, same_matching={same_matching}, "
              f"same_parent={same_parent}")
        for q in triple:
            print(f"      source[{q}]={metadata[q]}")
    for slack in sorted(hist):
        print(f"  slack={slack}: triples={hist[slack]}")
    return minimum


if __name__ == "__main__":
    run()
