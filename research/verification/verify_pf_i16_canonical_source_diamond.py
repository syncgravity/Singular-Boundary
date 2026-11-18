#!/usr/bin/env python3
"""Exact finite census for canonical source-level reverse-mark diamonds.

This is deliberately separate from the target-only mutual-survival census.
It tests the source projection and canonical-parent-neighborhood conditions
that the target-side diamond theorem does not supply.

For an ordered disjoint pair of target marks J,K on n ports:
  * compress K after deleting J, and J after deleting K;
  * choose parent sources p,q on n-2 ports whose canonical leaves are those
    compressed intervals;
  * require pi_K(p)=pi_J(q)=r as exact matching/overlap-tree source data;
  * form N(p,J), N(q,K) by lifting every canonical parent target and applying
    each admissible guarded final switch at the inserted mark;
  * intersect these neighborhoods, test mutual target-side survival, compute
    the common double inverse U, and test U in C_can(r).

Finite evidence only. No Hall or all-orders source-diamond theorem is asserted.
"""
from collections import defaultdict
from itertools import combinations

from verify_pf_i16_local_switch_fractional_transport import (
    LOCAL_TREES, candidate_outputs, overlaps,
)
from verify_pf_i16_source_dependent_leaf_peeling import (
    canonical_leaf, parent_data, sources,
)
from verify_pf_i16_reverse_mark_pair_census import (
    edge, inverse, local_records, relabel_tree,
)


def compress_pair(pair, removed, n):
    keep = [v for v in range(1, n + 1) if v not in removed]
    rank = {v: i + 1 for i, v in enumerate(keep)}
    return tuple(sorted(rank[v] for v in pair))


def lift_tree(tree, removed, n):
    keep = [v for v in range(1, n + 1) if v not in removed]
    return frozenset(edge(keep[a - 1], keep[b - 1]) for a, b in tree)


def canonical_outputs(source):
    intervals, tau = source
    if len(intervals) == 1:
        return candidate_outputs(intervals, tau)
    return candidate_outputs(
        intervals, tau, forced_last=canonical_leaf(intervals, tau)
    )


def fiber_neighborhood(parent_source, mark, n, parent_cache):
    """All guarded one-step lifts of canonical parent targets through mark."""
    if parent_source not in parent_cache:
        parent_cache[parent_source] = canonical_outputs(parent_source)
    answer = set()
    for parent_target in parent_cache[parent_source]:
        lifted = lift_tree(parent_target, set(mark), n)
        for old in sorted(lifted):
            if not overlaps(old, mark):
                continue
            ports = tuple(sorted((*mark, *old)))
            for local in LOCAL_TREES:
                local_edges = frozenset(
                    edge(ports[i], ports[j]) for i, j in local
                )
                if edge(*old) in local_edges:
                    continue
                target = (set(lifted) - {edge(*old)}) | set(local_edges)
                target = frozenset(target)
                # Check the exact guarded inverse, including induced pattern,
                # full endpoint incidence and no-reinsertion, rather than
                # trusting the forward construction alone.
                target0 = frozenset(edge(a - 1, b - 1) for a, b in target)
                mark0 = tuple(v - 1 for v in mark)
                records = local_records(target0, n, mark0)
                assert len(records) == 1, (
                    "forward lift did not have a unique exact inverse",
                    parent_source, mark, parent_target, old, local, records,
                )
                recovered = inverse(target0, mark0, records[0])
                lifted0 = frozenset(edge(a - 1, b - 1) for a, b in lifted)
                assert recovered == lifted0
                answer.add(target)
    return answer


def project_once(tree, mark, n):
    tree0 = frozenset(edge(a - 1, b - 1) for a, b in tree)
    mark0 = tuple(v - 1 for v in mark)
    records = local_records(tree0, n, mark0)
    if not records:
        return None
    assert len(records) == 1
    parent = inverse(tree0, mark0, records[0])
    remaining = sorted(set(range(n)) - set(mark0))
    return relabel_tree(parent, remaining)


def second_inverse(parent_tree, compressed_mark, parent_n):
    mark0 = tuple(v - 1 for v in compressed_mark)
    records = local_records(parent_tree, parent_n, mark0)
    if not records:
        return None
    assert len(records) == 1
    parent = inverse(parent_tree, mark0, records[0])
    remaining = sorted(set(range(parent_n)) - set(mark0))
    return relabel_tree(parent, remaining)


def main():
    for n in (6, 8):
        m = n - 2
        parent_sources = list(sources(m))
        source_meta = {}
        by_leaf = defaultdict(list)
        canonical_parent_cache = {}
        for source in parent_sources:
            intervals, tau = source
            leaf = canonical_leaf(intervals, tau)
            leaf_interval = intervals[leaf]
            r = parent_data(intervals, tau, leaf)
            source_meta[source] = (leaf_interval, r)
            by_leaf[leaf_interval].append(source)

        # Cache each (parent source, target mark) neighborhood.
        fiber_cache = {}
        candidate_mark_pairs = 0
        c2_source_diamonds = 0
        common_target_incidences = 0
        mutually_surviving = 0
        c3_pass = 0
        c3_failures = []
        one_way_survival = 0
        no_survival = 0
        support_types = defaultdict(int)

        marks = list(combinations(range(1, n + 1), 2))
        for J in marks:
            for K in marks:
                if J >= K or set(J) & set(K):
                    continue
                candidate_mark_pairs += 1
                Kp = compress_pair(K, set(J), n)
                Jq = compress_pair(J, set(K), n)
                for p in by_leaf.get(Kp, ()):
                    rp = source_meta[p][1]
                    for q in by_leaf.get(Jq, ()):
                        rq = source_meta[q][1]
                        if rp != rq:
                            continue
                        r = rp
                        c2_source_diamonds += 1
                        fkey, gkey = (p, J), (q, K)
                        if fkey not in fiber_cache:
                            fiber_cache[fkey] = fiber_neighborhood(
                                p, J, n, canonical_parent_cache
                            )
                        if gkey not in fiber_cache:
                            fiber_cache[gkey] = fiber_neighborhood(
                                q, K, n, canonical_parent_cache
                            )
                        common = fiber_cache[fkey] & fiber_cache[gkey]
                        for T in common:
                            common_target_incidences += 1
                            Pj = project_once(T, J, n)
                            Pk = project_once(T, K, n)
                            K_small = compress_pair(K, set(J), n)
                            J_small = compress_pair(J, set(K), n)
                            Uj = second_inverse(Pj, K_small, n - 2)
                            Uk = second_inverse(Pk, J_small, n - 2)
                            if Uj is None or Uk is None:
                                if (Uj is None) != (Uk is None):
                                    one_way_survival += 1
                                else:
                                    no_survival += 1
                                continue
                            mutually_surviving += 1
                            assert Uj == Uk, (
                                "target-side mutual-survival diamond failed",
                                n, J, K, p, q, r, T, Uj, Uk,
                            )
                            support_types[
                                (len(set(J) | set(K)),)
                            ] += 1
                            Uj_one_based = frozenset(
                                edge(a + 1, b + 1) for a, b in Uj
                            )
                            if Uj_one_based in canonical_outputs(r):
                                c3_pass += 1
                            else:
                                c3_failures.append({
                                    "n": n, "J": J, "K": K,
                                    "p": p, "q": q, "r": r,
                                    "target": T, "common_parent_target": Uj_one_based,
                                    "canonical_parent_targets": canonical_outputs(r),
                                })

        print(f"n={n}: parent_sources={len(parent_sources)}")
        print(f"  ordered_disjoint_mark_pairs={candidate_mark_pairs}")
        print(f"  exact_sibling_source_diamonds_C2={c2_source_diamonds}")
        print(f"  common_target_incidences={common_target_incidences}")
        print(f"  mutually_surviving_target_pairs={mutually_surviving}")
        print(f"  one_way_survival={one_way_survival}, no_survival={no_survival}")
        print(f"  C3_pass={c3_pass}, C3_fail={len(c3_failures)}")
        print(f"  support_types={dict(sorted(support_types.items()))}")
        if c3_failures:
            witness = c3_failures[0]
            print("  FIRST_C3_FAILURE:")
            for key, value in witness.items():
                print(f"    {key}={value}")
            print("RESULT: canonical source-level diamond fails in this finite case.")
        else:
            print("RESULT: no C3 failure among the tested mutually surviving incidences.")
        print("NOTE: finite census only; no arbitrary-family Hall consequence.")


if __name__ == "__main__":
    main()
