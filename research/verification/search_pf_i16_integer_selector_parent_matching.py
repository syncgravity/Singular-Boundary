#!/usr/bin/env python3
"""Search parent representative matchings for the integer mixed selector Hall condition.

Unlike a fixed arbitrary parent matching, Q is chosen jointly with the
integer row-capacity test. The search is exhaustive at n=6 and uses a
reproducible randomized perfect-matching search at n=8. This is a finite
diagnostic, not an all-orders proof.
"""
from collections import defaultdict, deque
from fractions import Fraction
from random import Random
from array import array

from verify_pf_i16_source_dependent_leaf_peeling import (
    sources, parent_data, compress_tree,
)
from verify_pf_i16_integer_mixed_selector_hall import (
    nonroot_leaves, parent_neighborhood, expand_parent_tree,
    one_switch_lifts, Dinic,
)


def ceil_fraction(x):
    return (x.numerator + x.denominator - 1) // x.denominator


def randomized_parent_matching(parents, neighborhoods, rng):
    """Return a perfect matching, randomizing both left and right order."""
    rights = sorted(set().union(*(set(neighborhoods[p]) for p in parents)), key=repr)
    owner = {}
    chosen = {}

    # Constrained vertices first reduces backtracking; random tie order avoids
    # repeatedly selecting the same lexicographic representative.
    left = list(parents)
    rng.shuffle(left)
    left.sort(key=lambda p: len(neighborhoods[p]))

    def augment(p, seen):
        opts = list(neighborhoods[p])
        rng.shuffle(opts)
        for t in opts:
            if t in seen:
                continue
            seen.add(t)
            q = owner.get(t)
            if q is None or augment(q, seen):
                owner[t] = p
                chosen[p] = t
                return True
        return False

    for p in left:
        if not augment(p, set()):
            return None
    return chosen


def build_fibers(n):
    fibers = defaultdict(list)
    parent_sources = set()
    for iv, tau in sources(n):
        for leaf in nonroot_leaves(iv, tau):
            p = parent_data(iv, tau, leaf)
            J = iv[leaf]
            parent_sources.add(p)
            fibers[(p, J)].append((iv, tau))
    return fibers, sorted(parent_sources, key=repr)


def evaluate_Q(n, fibers, Q):
    rows = []
    target_ids = {}
    for (p, J), children in sorted(fibers.items(), key=lambda z: repr(z[0])):
        P = expand_parent_tree(Q[p], J, n)
        lifts = one_switch_lifts(P, J)
        demand = sum((Fraction(1, len(nonroot_leaves(iv, tau)))
                      for iv, tau in children), Fraction(0))
        quota = ceil_fraction(demand)
        ids = []
        for T in lifts:
            if T not in target_ids:
                target_ids[T] = len(target_ids)
            ids.append(target_ids[T])
        if quota > len(set(ids)):
            return quota, len(set(ids)), None, (p, J, demand, lifts)
        rows.append((demand, quota, sorted(set(ids)), p, J))
    F, T = len(rows), len(target_ids)
    S = 0; r0 = 1; t0 = r0 + F; sink = t0 + T
    net = Dinic(sink + 1)
    total = 0
    for i, (_, quota, neigh, _, _) in enumerate(rows):
        net.add(S, r0+i, quota)
        total += quota
        for j in neigh:
            net.add(r0+i, t0+j, 1)
    for j in range(T):
        net.add(t0+j, sink, 1)
    got, level = net.maxflow(S, sink, total)
    if got == total:
        return got, total, rows, None
    cut_rows = [i for i in range(F) if level[r0+i] >= 0]
    cut_targets = set()
    for i in cut_rows:
        cut_targets.update(rows[i][2])
    witness = {
        "rows": len(cut_rows),
        "targets": len(cut_targets),
        "quota": sum(rows[i][1] for i in cut_rows),
        "deficiency": sum(rows[i][1] for i in cut_rows)-len(cut_targets),
        "sample": [(rows[i][3], rows[i][4], str(rows[i][0]),
                    rows[i][1], len(rows[i][2])) for i in cut_rows[:8]],
    }
    return got, total, rows, witness



def evaluate_single_parent(n, p, fibers, parent_target):
    rows = []
    target_ids = {}
    for (pp, J), children in sorted(fibers.items(), key=lambda z: repr(z[0])):
        if pp != p:
            continue
        P = expand_parent_tree(parent_target, J, n)
        lifts = one_switch_lifts(P, J)
        demand = sum((Fraction(1, len(nonroot_leaves(iv, tau)))
                      for iv, tau in children), Fraction(0))
        quota = ceil_fraction(demand)
        ids = []
        for T in lifts:
            if T not in target_ids:
                target_ids[T] = len(target_ids)
            ids.append(target_ids[T])
        rows.append((demand, quota, sorted(set(ids)), J))
    F, T = len(rows), len(target_ids)
    S = 0; r0 = 1; t0 = r0 + F; sink = t0 + T
    net = Dinic(sink + 1)
    total = 0
    for i, (_, quota, neigh, _) in enumerate(rows):
        net.add(S, r0+i, quota); total += quota
        for j in neigh:
            net.add(r0+i, t0+j, 1)
    for j in range(T):
        net.add(t0+j, sink, 1)
    got, _ = net.maxflow(S, sink, total)
    return got, total, rows


def local_parent_census(n, fibers, parents):
    no_local_Q = []
    for p in parents:
        choices = sorted(parent_neighborhood(p), key=repr)
        feasible = []
        best = (0, 0, None)
        for P in choices:
            got, total, rows = evaluate_single_parent(n, p, fibers, P)
            if got > best[0]:
                best = (got, total, P)
            if got == total:
                feasible.append(P)
        if not feasible:
            no_local_Q.append((p, len(choices), best))
    print(f"n={n} parent_fibers_without_any_locally_feasible_Q={len(no_local_Q)}",
          flush=True)
    for p, count, best in no_local_Q[:5]:
        print(f"  local_obstruction parent={p} choices={count} "
              f"best={best[0]}/{best[1]} Q={best[2]}", flush=True)
    return no_local_Q

def exhaustive_n6(fibers, parents):
    from itertools import product
    neighborhoods = {p: sorted(parent_neighborhood(p), key=repr)
                     for p in parents}
    feasible = []
    tested = 0
    for assignment in product(*(neighborhoods[p] for p in parents)):
        if len(set(assignment)) != len(assignment):
            continue
        Q = dict(zip(parents, assignment))
        tested += 1
        got, total, rows, witness = evaluate_Q(6, fibers, Q)
        if got == total:
            feasible.append((Q, total))
    print(f"n=6 exhaustive_parent_Q={tested} feasible_selector_Q={len(feasible)}",
          flush=True)
    if feasible:
        Q, total = feasible[0]
        print(f"n=6 example_Q={Q} integer_demand={total}", flush=True)
    assert feasible, "No n=6 parent representative assignment supports selector Hall."


def randomized_n8(fibers, parents, trials=1000, seed=161117, allowed=None):
    neighborhoods = (allowed if allowed is not None else
                     {p: sorted(parent_neighborhood(p), key=repr)
                      for p in parents})
    rng = Random(seed)
    best = None
    seen_Q = set()
    for k in range(trials):
        Q = randomized_parent_matching(parents, neighborhoods, rng)
        if Q is None:
            continue
        signature = tuple((p, Q[p]) for p in parents)
        seen_Q.add(signature)
        got, total, rows, witness = evaluate_Q(8, fibers, Q)
        if best is None or got * best[1] > best[0] * total:
            best = (got, total, witness, Q)
        if got == total:
            print(f"n=8 selector_Q_found trial={k+1}/{trials} "
                  f"integer_demand={total}", flush=True)
            print(f"n=8 Q={Q}", flush=True)
            return
        if (k+1) % 25 == 0:
            print(f"n=8 trials={k+1} best_flow={best[0]}/{best[1]} "
                  f"witness={best[2]}", flush=True)
    print(f"n=8 NO_SELECTOR_Q_FOUND trials={trials} distinct_Q={len(seen_Q)} "
          f"best_flow={best[0]}/{best[1]} witness={best[2]}", flush=True)
    print(f"n=8 best_Q={best[3]}", flush=True)
    raise SystemExit(1)


def main():
    f6, p6 = build_fibers(6)
    exhaustive_n6(f6, p6)
    f8, p8 = build_fibers(8)
    print(f"n=8 parent_sources={len(p8)} fibers={len(f8)}", flush=True)
    allowed = local_parent_census(8, f8, p8)
    print(f"n=8 locally_feasible_parent_choices={sum(len(v) for v in allowed.values())} "
          f"choice_range=[{min(map(len, allowed.values()))},{max(map(len, allowed.values()))}]", flush=True)
    randomized_n8(f8, p8, allowed=allowed)


if __name__ == "__main__":
    main()
