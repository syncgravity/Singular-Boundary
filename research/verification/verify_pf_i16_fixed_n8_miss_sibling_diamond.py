#!/usr/bin/env python3
"""Focused n=12 sibling-diamond test for the first n=8 retained-row miss.

Fixes the exact four-interval common parent from the universal n=8
ordinary-to-retained counterexample. Enumerates all ten-port parent sources
whose canonical-leaf deletion gives that common parent, then tests every
ordered sibling-source diamond compatible with disjoint inserted marks.

For each common child target, it computes the exact common double inverse U
and tests the actual retained condition at r: at least one non-root leaf L
must reverse U to a target in C_can(pi_L(r)).

This is a targeted finite diagnostic. It neither proves nor disproves the
all-orders sibling-diamond lemma outside this fixed r.
"""
from collections import defaultdict
from itertools import combinations

from verify_pf_i16_source_dependent_leaf_peeling import (
    canonical_leaf, parent_data, sources, compress_tree, inverse_last_switch,
)
from verify_pf_i16_canonical_source_diamond import (
    compress_pair, fiber_neighborhood, project_once, second_inverse,
    canonical_outputs,
)

N = 12
R = (
    ((1, 4), (2, 5), (3, 7), (6, 8)),
    ((0, 1), (0, 2), (2, 3)),
)


def nonroot_leaves(intervals, tau):
    degree = [0] * len(intervals)
    for a, b in tau:
        degree[a] += 1
        degree[b] += 1
    root = next(i for i, I in enumerate(intervals) if I[0] == 1)
    return [i for i, d in enumerate(degree) if d == 1 and i != root]


def retained_routes(U, source, parent_cache):
    intervals, tau = source
    routes = []
    for leaf in nonroot_leaves(intervals, tau):
        J = intervals[leaf]
        inv = inverse_last_switch(U, J, len(intervals) * 2)
        if len(inv) != 1:
            continue
        P = compress_tree(next(iter(inv)), set(J), len(intervals) * 2)
        parent = parent_data(intervals, tau, leaf)
        if parent not in parent_cache:
            parent_cache[parent] = set(canonical_outputs(parent))
        if P in parent_cache[parent]:
            routes.append((J, P, parent))
    return routes


def main():
    parent_sources = list(sources(N - 2))
    by_mark = defaultdict(list)
    parent_cache = {}
    matched_sources = 0
    for p in parent_sources:
        intervals, tau = p
        leaf = canonical_leaf(intervals, tau)
        mark = intervals[leaf]
        r = parent_data(intervals, tau, leaf)
        if r == R:
            by_mark[mark].append(p)
            matched_sources += 1

    marks = list(combinations(range(1, N + 1), 2))
    fiber_cache = {}
    diamonds = 0
    common_incidences = 0
    mutual = 0
    retained = 0
    missed = 0
    first_miss = None
    same_parent = 0
    for J in marks:
        for K in marks:
            if J >= K or set(J) & set(K):
                continue
            Kp = compress_pair(K, set(J), N)
            Jq = compress_pair(J, set(K), N)
            for p in by_mark.get(Kp, ()):
                for q in by_mark.get(Jq, ()):
                    if p == q:
                        same_parent += 1
                        continue
                    diamonds += 1
                    fk, gk = (p, J), (q, K)
                    if fk not in fiber_cache:
                        fiber_cache[fk] = fiber_neighborhood(p, J, N, parent_cache)
                    if gk not in fiber_cache:
                        fiber_cache[gk] = fiber_neighborhood(q, K, N, parent_cache)
                    common = fiber_cache[fk] & fiber_cache[gk]
                    for T in common:
                        common_incidences += 1
                        Pj = project_once(T, J, N)
                        Pk = project_once(T, K, N)
                        Uj = second_inverse(Pj, Kp, N - 2)
                        Uk = second_inverse(Pk, Jq, N - 2)
                        if Uj is None or Uk is None:
                            continue
                        assert Uj == Uk, ("double inverse disagreement", J, K, p, q, T)
                        mutual += 1
                        routes = retained_routes(Uj, R, parent_cache)
                        if routes:
                            retained += 1
                        else:
                            missed += 1
                            if first_miss is None:
                                first_miss = {
                                    "J": J, "K": K, "p": p, "q": q,
                                    "T": tuple(sorted(T)), "U": Uj,
                                }

    print(f"fixed_common_parent={R}")
    print(f"ten_port_parent_sources={len(parent_sources)}")
    print(f"parent_sources_deleting_to_R={matched_sources}")
    print(f"distinct_parent_source_diamonds={diamonds}")
    print(f"same_parent_pairs_skipped={same_parent}")
    print(f"common_target_incidences={common_incidences}")
    print(f"mutual_double_inverse_incidences={mutual}")
    print(f"retained_common_inverses={retained}")
    print(f"unretained_common_inverses={missed}")
    if first_miss:
        print(f"FIRST_UNRETAINED_SIBLING_WITNESS={first_miss}")
    print("RESULT: targeted fixed-parent sibling-diamond census complete.")


if __name__ == "__main__":
    main()
