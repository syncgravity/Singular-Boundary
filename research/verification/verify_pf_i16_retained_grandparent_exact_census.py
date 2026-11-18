#!/usr/bin/env python3
"""Exact fixed-parent retained-grandparent sibling-diamond census.

This is the corrected n=12 test for the first four-interval common parent
where N_pi(r) can be a strict subset of C(r).

Compared with the earlier diagnostic, this verifier:
  * uses local_records/inverse/relabel_tree, including no-reinsertion;
  * includes p=q;
  * reconstructs the common child matching AND overlap tree from p and q;
  * checks pi_J(x)=p and pi_K(x)=q exactly before counting a diamond;
  * checks the exact retained condition U in N_pi(r).

The test is fixed to one common parent R. A miss is a finite counterexample
to this sibling-specific rerouting claim at R. A pass is finite evidence only;
neither outcome proves all-orders Hall or the weighted one-link inequality.
"""
from collections import defaultdict
from itertools import combinations

from verify_pf_i16_source_dependent_leaf_peeling import (
    canonical_leaf, parent_data, sources,
)
from verify_pf_i16_canonical_source_diamond import (
    compress_pair, fiber_neighborhood, project_once, second_inverse,
    canonical_outputs,
)
from verify_pf_i16_local_switch_fractional_transport import candidate_outputs
from verify_pf_i16_reverse_mark_pair_census import (
    edge, inverse, local_records, relabel_tree,
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


def overlaps(a, b):
    return max(a[0], b[0]) < min(a[1], b[1])


def lifted_source(source, inserted_mark, n):
    """Lift a compressed parent source to n-port labels, adjoining mark."""
    intervals, tau = source
    keep = [v for v in range(1, n + 1) if v not in set(inserted_mark)]
    lifted_items = [
        tuple(sorted((keep[a - 1], keep[b - 1]))) for a, b in intervals
    ]
    lifted_items.append(tuple(sorted(inserted_mark)))
    lifted = tuple(sorted(lifted_items))
    child_index = {I: i for i, I in enumerate(lifted)}
    parent_to_child = [
        child_index[tuple(sorted((keep[a - 1], keep[b - 1])))]
        for a, b in intervals
    ]
    lifted_edges = frozenset(
        tuple(sorted((parent_to_child[a], parent_to_child[b])))
        for a, b in tau
    )
    return lifted, lifted_edges


def is_tree(vertex_count, edges):
    if len(edges) != vertex_count - 1:
        return False
    adjacency = [set() for _ in range(vertex_count)]
    for a, b in edges:
        if a == b:
            return False
        adjacency[a].add(b)
        adjacency[b].add(a)
    seen = {0}
    stack = [0]
    while stack:
        v = stack.pop()
        for w in adjacency[v] - seen:
            seen.add(w)
            stack.append(w)
    return len(seen) == vertex_count


def reconstruct_child_source(p, q, J, K, n):
    """Return x iff p=pi_J(x), q=pi_K(x), with J,K non-root leaves."""
    if 1 in J or 1 in K:
        return None

    p_intervals, p_edges = lifted_source(p, J, n)
    q_intervals, q_edges = lifted_source(q, K, n)
    if p_intervals != q_intervals:
        return None

    child_intervals = p_intervals
    child_edges = p_edges | q_edges
    if len(p_edges & q_edges) != len(child_intervals) - 3:
        return None
    if not is_tree(len(child_intervals), child_edges):
        return None

    if any(not overlaps(child_intervals[a], child_intervals[b])
           for a, b in child_edges):
        return None

    degree = [0] * len(child_intervals)
    for a, b in child_edges:
        degree[a] += 1
        degree[b] += 1
    j_index = child_intervals.index(tuple(sorted(J)))
    k_index = child_intervals.index(tuple(sorted(K)))
    if degree[j_index] != 1 or degree[k_index] != 1:
        return None

    child = (child_intervals, tuple(sorted(child_edges)))
    if parent_data(child_intervals, child[1], j_index) != p:
        return None
    if parent_data(child_intervals, child[1], k_index) != q:
        return None
    return child


def zero_based_tree(tree):
    return frozenset(edge(a - 1, b - 1) for a, b in tree)


def one_based_tree(tree):
    return tuple(sorted(edge(a + 1, b + 1) for a, b in tree))


def retained_routes(U_zero, source, parent_cache):
    """Exact routes witnessing U in N_pi(source), with all guards enforced."""
    intervals, tau = source
    routes = []
    n = 2 * len(intervals)
    for leaf in nonroot_leaves(intervals, tau):
        J = intervals[leaf]
        mark_zero = tuple(v - 1 for v in J)
        records = local_records(U_zero, n, mark_zero)
        if not records:
            continue
        assert len(records) == 1, (source, J, U_zero, records)

        parent_zero = inverse(U_zero, mark_zero, records[0])
        remaining = sorted(set(range(n)) - set(mark_zero))
        parent_zero = relabel_tree(parent_zero, remaining)
        parent_target = one_based_tree(parent_zero)

        parent = parent_data(intervals, tau, leaf)
        if parent not in parent_cache:
            parent_cache[parent] = set(canonical_outputs(parent))
        if parent_target in parent_cache[parent]:
            routes.append((J, parent_target, parent))
    return routes


def run_self_tests():
    cache = {}

    # The known rooted-star example is not in C_can(R_star), but is retained
    # by reversing B and then the canonical leaf A in the two-interval parent.
    r_star = (
        ((1, 4), (2, 5), (3, 6)),
        ((0, 1), (0, 2)),
    )
    u_star = zero_based_tree(((1, 2), (2, 3), (3, 4), (4, 5), (4, 6)))
    star_routes = retained_routes(u_star, r_star, cache)
    assert star_routes and star_routes[0][0] == (3, 6), star_routes

    # The first n=8 universal-coverage miss has no retained route at all.
    r_miss = (
        ((1, 4), (2, 5), (3, 7), (6, 8)),
        ((0, 1), (0, 2), (2, 3)),
    )
    u_miss = zero_based_tree(
        ((1, 2), (2, 3), (2, 4), (3, 5), (3, 6), (6, 7), (6, 8))
    )
    assert not retained_routes(u_miss, r_miss, cache)

    # The proved <=3-interval theorem is an implementation-level control:
    # every ordinary output at six ports must pass the exact retained test.
    sources6 = list(sources(6))
    ordinary6 = 0
    for source in sources6:
        for target in candidate_outputs(*source):
            ordinary6 += 1
            assert retained_routes(zero_based_tree(target), source, cache), (
                "exact retained-route self-test failed", source, target
            )
    assert len(sources6) == 22 and ordinary6 == 241
    print("SELF_TESTS_PASS: rooted-star retained reroute; n=8 miss excluded; "
          "all 241 six-port ordinary incidences retained", flush=True)


def main():
    run_self_tests()

    parent_sources = list(sources(N - 2))
    assert len(parent_sources) == 31744, len(parent_sources)

    by_canonical_leaf = defaultdict(list)
    for p in parent_sources:
        intervals, tau = p
        leaf = canonical_leaf(intervals, tau)
        mark = intervals[leaf]
        if parent_data(intervals, tau, leaf) == R:
            by_canonical_leaf[mark].append(p)

    marks = [pair for pair in combinations(range(1, N + 1), 2)
             if 1 not in pair]
    parent_cache = {}
    fiber_cache = {}
    ordinary_R = candidate_outputs(*R)

    candidate_matching_pairs = 0
    exact_sibling_diamonds = 0
    same_parent_diamonds = 0
    distinct_parent_diamonds = 0
    common_target_incidences = 0
    mutually_surviving = 0
    nonmutual_common_targets = 0
    retained = 0
    missed = 0
    first_miss = None

    for J in marks:
        for K in marks:
            if J >= K or set(J) & set(K):
                continue
            Kp = compress_pair(K, set(J), N)
            Jq = compress_pair(J, set(K), N)
            p_rows = by_canonical_leaf.get(Kp, ())
            q_rows = by_canonical_leaf.get(Jq, ())
            if not p_rows or not q_rows:
                continue

            # Group by the reconstructed child matching before pairing
            # parent sources. This avoids the old Cartesian product of
            # unrelated p,q sources.
            p_groups = defaultdict(list)
            q_groups = defaultdict(list)
            for p in p_rows:
                lifted_intervals, _ = lifted_source(p, J, N)
                p_groups[lifted_intervals].append(p)
            for q in q_rows:
                lifted_intervals, _ = lifted_source(q, K, N)
                q_groups[lifted_intervals].append(q)

            for child_matching in sorted(p_groups.keys() & q_groups.keys()):
                for p in p_groups[child_matching]:
                    for q in q_groups[child_matching]:
                        candidate_matching_pairs += 1
                        child = reconstruct_child_source(p, q, J, K, N)
                        if child is None:
                            continue

                        exact_sibling_diamonds += 1
                        if p == q:
                            same_parent_diamonds += 1
                        else:
                            distinct_parent_diamonds += 1

                        fkey, gkey = (p, J), (q, K)
                        if fkey not in fiber_cache:
                            fiber_cache[fkey] = fiber_neighborhood(
                                p, J, N, parent_cache
                            )
                        if gkey not in fiber_cache:
                            fiber_cache[gkey] = fiber_neighborhood(
                                q, K, N, parent_cache
                            )

                        common = fiber_cache[fkey] & fiber_cache[gkey]
                        for T in common:
                            common_target_incidences += 1
                            Pj = project_once(T, J, N)
                            Pk = project_once(T, K, N)
                            assert Pj is not None and Pk is not None

                            Uj = second_inverse(Pj, Kp, N - 2)
                            Uk = second_inverse(Pk, Jq, N - 2)
                            if Uj is None or Uk is None:
                                nonmutual_common_targets += 1
                                continue
                            assert Uj == Uk, (
                                "double inverse disagreement", J, K, p, q, T,
                                Uj, Uk,
                            )
                            mutually_surviving += 1

                            U_one = one_based_tree(Uj)
                            assert U_one in ordinary_R, (
                                "source routes did not give an ordinary R output",
                                J, K, p, q, child, T, U_one,
                            )

                            routes = retained_routes(Uj, R, parent_cache)
                            if routes:
                                retained += 1
                            else:
                                missed += 1
                                if first_miss is None:
                                    first_miss = {
                                        "J": J, "K": K, "p": p, "q": q,
                                        "child_source": child,
                                        "T": tuple(sorted(T)),
                                        "U": U_one,
                                    }

    print(f"fixed_common_parent={R}", flush=True)
    print(f"ten_port_parent_sources={len(parent_sources)}", flush=True)
    print(f"parent_sources_deleting_canonically_to_R="
          f"{sum(map(len, by_canonical_leaf.values()))}", flush=True)
    print(f"candidate_pairs_with_same_lifted_matching="
          f"{candidate_matching_pairs}", flush=True)
    print(f"exact_sibling_source_diamonds={exact_sibling_diamonds}", flush=True)
    print(f"same_parent_diamonds={same_parent_diamonds}", flush=True)
    print(f"distinct_parent_diamonds={distinct_parent_diamonds}", flush=True)
    print(f"common_target_incidences={common_target_incidences}", flush=True)
    print(f"mutually_surviving_double_inverses={mutually_surviving}", flush=True)
    print(f"nonmutual_common_targets={nonmutual_common_targets}", flush=True)
    print(f"retained_common_inverses={retained}", flush=True)
    print(f"unretained_common_inverses={missed}", flush=True)
    if first_miss is not None:
        print(f"FIRST_UNRETAINED_SIBLING_WITNESS={first_miss}", flush=True)
    print("RESULT: exact fixed-parent sibling-grandparent census complete; "
          "finite evidence only.", flush=True)


if __name__ == "__main__":
    import sys
    if sys.argv[1:] == ["--self-test-only"]:
        run_self_tests()
    else:
        main()
