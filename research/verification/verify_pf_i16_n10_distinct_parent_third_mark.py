#!/usr/bin/env python3
"""Focused n=10 census of the first nontrivial canonical third-mark case.

Only source diamonds whose common parent r has three intervals and a
root-centered overlap-tree star are retained. This variant excludes the
degenerate case p=q, to test whether the n=10 obstruction is confined to
identified sibling parent sources. Such an r has two non-root
leaves A<B; C_can(r) requires A last. The verifier separates:
  (i) A is a guarded reverse mark of U;
  (ii) B survives after reversing A;
  (iii) U is in C_can(r).

It also records where the two child leaves J,K attach in r. This is finite
diagnostic evidence only; it does not prove the all-orders lemma.
"""
from collections import defaultdict, Counter
from itertools import combinations

from verify_pf_i16_canonical_source_diamond import (
    canonical_outputs, compress_pair, fiber_neighborhood,
    project_once, second_inverse,
)
from verify_pf_i16_source_dependent_leaf_peeling import (
    canonical_leaf, parent_data, sources,
)
from verify_pf_i16_reverse_mark_pair_census import (
    edge, inverse, local_records, relabel_tree,
)


def rooted_star_data(source):
    intervals, tau = source
    if len(intervals) != 3:
        return None
    root = next(i for i, I in enumerate(intervals) if I[0] == 1)
    degree = [0] * 3
    for a, b in tau:
        degree[a] += 1
        degree[b] += 1
    leaves = [i for i, d in enumerate(degree) if d == 1 and i != root]
    if degree[root] != 2 or len(leaves) != 2:
        return None
    A = min(leaves, key=lambda i: intervals[i])
    B = next(i for i in leaves if i != A)
    return root, A, B


def attachment_of_canonical_leaf(source):
    intervals, tau = source
    leaf = canonical_leaf(intervals, tau)
    neighbor = next(b if a == leaf else a for a, b in tau if leaf in (a, b))
    keep = [i for i in range(len(intervals)) if i != leaf]
    old_to_new = {old: new for new, old in enumerate(keep)}
    return old_to_new[neighbor]


def main():
    n = 10
    parent_sources = list(sources(n - 2))
    by_leaf = defaultdict(list)
    meta = {}
    parent_target_cache = {}
    fiber_cache = {}
    ordinary_outputs_cache = {}

    for source in parent_sources:
        intervals, tau = source
        leaf = canonical_leaf(intervals, tau)
        mark = intervals[leaf]
        r = parent_data(intervals, tau, leaf)
        star = rooted_star_data(r)
        if star is None:
            continue
        attachment = attachment_of_canonical_leaf(source)
        by_leaf[mark].append(source)
        meta[source] = (r, attachment)

    marks = list(combinations(range(1, n + 1), 2))
    mark_pairs = 0
    source_diamonds = 0
    same_parent_diamonds = 0
    distinct_parent_diamonds = 0
    common_incidences = 0
    mutual_survivors = 0
    no_second_survival = 0
    A_valid = 0
    A_invalid = 0
    B_survives_after_A = 0
    B_fails_after_A = 0
    C3_pass = 0
    C3_fail = 0
    attachment_types = Counter()
    first_failures = []

    for J in marks:
        for K in marks:
            if J >= K or set(J) & set(K):
                continue
            mark_pairs += 1
            Kp = compress_pair(K, set(J), n)
            Jq = compress_pair(J, set(K), n)
            for p in by_leaf.get(Kp, ()):
                rp, ap = meta[p]
                for q in by_leaf.get(Jq, ()):
                    rq, aq = meta[q]
                    if rp != rq:
                        continue
                    r = rp
                    if p == q:
                        same_parent_diamonds += 1
                        continue
                    distinct_parent_diamonds += 1
                    root, Aidx, Bidx = rooted_star_data(r)
                    def typ(v):
                        return "A" if v == Aidx else "B" if v == Bidx else "R"
                    attachment_types[(typ(ap), typ(aq))] += 1
                    source_diamonds += 1

                    fkey, gkey = (p, J), (q, K)
                    if fkey not in fiber_cache:
                        fiber_cache[fkey] = fiber_neighborhood(
                            p, J, n, parent_target_cache
                        )
                    if gkey not in fiber_cache:
                        fiber_cache[gkey] = fiber_neighborhood(
                            q, K, n, parent_target_cache
                        )
                    common = fiber_cache[fkey] & fiber_cache[gkey]

                    for T in common:
                        common_incidences += 1
                        Pj = project_once(T, J, n)
                        Pk = project_once(T, K, n)
                        K_small = compress_pair(K, set(J), n)
                        J_small = compress_pair(J, set(K), n)
                        Uj = second_inverse(Pj, K_small, n - 2)
                        Uk = second_inverse(Pk, J_small, n - 2)
                        if Uj is None or Uk is None:
                            no_second_survival += 1
                            continue
                        mutual_survivors += 1
                        assert Uj == Uk, ("target diamond disagreement", J, K, p, q, T)
                        U = Uj
                        U_one = tuple(sorted(edge(a + 1, b + 1) for a, b in U))
                        if r not in ordinary_outputs_cache:
                            ordinary_outputs_cache[r] = {
                                tuple(sorted(edge(a, b) for a, b in z))
                                for z in candidate_outputs_all(r)
                            }
                            ordinary_outputs_cache[r].update(canonical_outputs(r))
                        assert U_one in ordinary_outputs_cache[r], ("double inverse not in parent neighborhood", r, U_one)

                        intervals, tau = r
                        L = intervals[Aidx]
                        B = intervals[Bidx]
                        U0 = frozenset(edge(a - 1, b - 1) for a, b in U_one)
                        L0 = tuple(v - 1 for v in L)
                        L_records = local_records(U0, n - 4, L0)
                        if not L_records:
                            A_invalid += 1
                            C3_fail += 1
                            if len(first_failures) < 5:
                                first_failures.append({
                                    "kind": "A_not_reverse_mark",
                                    "J": J, "K": K, "p": p, "q": q,
                                    "r": r, "A": L, "B": B, "U": U_one,
                                })
                            continue
                        A_valid += 1
                        parent_after_A = inverse(U0, L0, L_records[0])
                        remaining = sorted(set(range(n - 4)) - set(L0))
                        parent_after_A = relabel_tree(parent_after_A, remaining)
                        B_small = compress_pair(B, set(L), n - 4)
                        B0 = tuple(v - 1 for v in B_small)
                        B_records = local_records(parent_after_A, n - 6, B0)
                        if B_records:
                            B_survives_after_A += 1
                            C3_pass += 1
                        else:
                            B_fails_after_A += 1
                            C3_fail += 1
                            if len(first_failures) < 5:
                                first_failures.append({
                                    "kind": "B_does_not_survive_A",
                                    "J": J, "K": K, "p": p, "q": q,
                                    "r": r, "A": L, "B": B, "U": U_one,
                                    "P_A_U": parent_after_A,
                                })

    print(f"n={n}, parent_sources={len(parent_sources)}, star_child_parents={len(meta)}")
    print(f"disjoint_mark_pairs={mark_pairs}, source_diamonds={source_diamonds}")
    print(f"same_parent_diamonds={same_parent_diamonds}, distinct_parent_diamonds={distinct_parent_diamonds}")
    print(f"common_target_incidences={common_incidences}, mutual_survivors={mutual_survivors}")
    print(f"no_second_survival={no_second_survival}")
    print(f"A_valid={A_valid}, A_invalid={A_invalid}")
    print(f"B_survives_after_A={B_survives_after_A}, B_fails_after_A={B_fails_after_A}")
    print(f"C3_pass={C3_pass}, C3_fail={C3_fail}")
    print(f"attachment_types={dict(sorted(attachment_types.items()))}")
    if first_failures:
        print("FIRST_FAILURES:")
        for item in first_failures:
            print(item)
    print("NOTE: focused finite census only; no all-orders third-mark or Hall theorem.")


def candidate_outputs_all(source):
    # The full source neighborhood is computed by the unforced order search.
    from verify_pf_i16_local_switch_fractional_transport import candidate_outputs
    intervals, tau = source
    return candidate_outputs(intervals, tau)


if __name__ == "__main__":
    main()
