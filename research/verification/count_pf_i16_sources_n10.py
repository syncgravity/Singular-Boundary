#!/usr/bin/env python3
"""Count n=10 PF-I16 sources before attempting the expensive target relation."""
from collections import Counter
from verify_pf_i16_source_dependent_leaf_peeling import sources
from verify_pf_i16_local_switch_fractional_transport import overlap_edges


def run(n=10):
    count = 0
    by_overlap_edges = Counter()
    by_matching = Counter()
    max_per_matching = 0
    for intervals, tau in sources(n):
        count += 1
        by_overlap_edges[len(overlap_edges(intervals))] += 1
        by_matching[intervals] += 1
    max_per_matching = max(by_matching.values(), default=0)
    print(f"n={n}: source_count={count}, perfect_matchings={len(by_matching)}, "
          f"max_overlap_trees_per_matching={max_per_matching}")
    print("  source_counts_by_overlap_edge_count=" +
          repr(dict(sorted(by_overlap_edges.items()))))
    print("  overlap_tree_counts_per_matching_histogram=" +
          repr(dict(sorted(Counter(by_matching.values()).items()))))
    print(f"  connected-tree distinct-output lower bound per source={2 ** (n//2-1)}")
    return count


if __name__ == "__main__":
    run()
