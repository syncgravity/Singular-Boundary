#!/usr/bin/env python3
"""Exact n=12 source-profile census around the first overcrowded cut.

For a connected interval-overlap graph, a non-tree source must have some cut
crossed by at least three matching intervals. This streams the source space
and records the first such cut, maximum interval depth, and overlap-tree class.
It is a diagnostic for a possible recursive complement matching, not a Hall
proof.
"""
from collections import Counter
from verify_pf_i16_source_dependent_leaf_peeling import sources
from verify_pf_i16_local_switch_fractional_transport import overlap_edges, matchings


def crossing_profile(intervals, n):
    return tuple(sum(a <= k < b for a, b in intervals)
                 for k in range(1, n))


def run(n=12):
    source_count = 0
    matching_count = 0
    tree_sources = 0
    complement_sources = 0
    first_overcrowded = Counter()
    max_depth_hist = Counter()
    first_and_max = Counter()
    matching_profiles = set()
    for intervals, tau in sources(n):
        source_count += 1
        if len(tau) == len(intervals) - 1:
            # tau is always a spanning tree; distinguish H_M itself being a tree.
            pass
        profile = crossing_profile(intervals, n)
        depth = max(profile, default=0)
        max_depth_hist[depth] += 1
        first = next((k for k, value in enumerate(profile, 1)
                      if value >= 3), None)
        if first is None:
            tree_sources += 1
            assert len(overlap_edges(intervals)) == len(intervals) - 1
        else:
            complement_sources += 1
            assert len(overlap_edges(intervals)) > len(intervals) - 1
            first_overcrowded[first] += 1
            first_and_max[(first, depth)] += 1
    for M in matchings(range(1, n + 1)):
        matching_count += 1
        intervals = tuple(sorted(tuple(sorted(e)) for e in M))
        matching_profiles.add(crossing_profile(intervals, n))
    print(f"n={n} matchings={matching_count} connected_sources={source_count}")
    print(f"  K_tree_overlap_sources={tree_sources} expected={2**(n//2-1)}")
    print(f"  complement_sources={complement_sources}")
    print(f"  first_overcrowded_cut_counts={sorted(first_overcrowded.items())}")
    print(f"  max_live_interval_depth_histogram={sorted(max_depth_hist.items())}")
    print(f"  (first_overcrowded_cut,max_depth)={sorted(first_and_max.items())}")
    print(f"  distinct_matching_cut_profiles={len(matching_profiles)}")
    assert tree_sources == 2 ** (n // 2 - 1)
    assert tree_sources + complement_sources == source_count
    assert all(k is not None for k, _ in first_and_max)


if __name__ == "__main__":
    run(12)
