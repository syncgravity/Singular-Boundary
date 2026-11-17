#!/usr/bin/env python3
"""Exact integer Hall test for the fixed-representative reverse-mark selector.

For each parent source p, first find an injective representative Q(p) in
its canonical parent leaf-last target neighborhood. For each row (p,J),
construct all guarded one-switch lifts of Q(p) with J inserted last.
The row quota is ceil(sum_{x in X(p,J)} 1/d(x)). A unit-capacity bipartite
matching after cloning rows by these quotas is exactly the selector condition.
"""
from collections import defaultdict, deque
from fractions import Fraction
from itertools import permutations
from array import array

from verify_pf_i16_source_dependent_leaf_peeling import (
    sources, parent_data, canonical_leaf, compress_tree,
)
from verify_pf_i16_local_switch_fractional_transport import (
    candidate_outputs, LOCAL_TREES,
)


def nonroot_leaves(intervals, tau):
    deg = [0] * len(intervals)
    for a, b in tau:
        deg[a] += 1
        deg[b] += 1
    root = next(i for i, I in enumerate(intervals) if I[0] == 1)
    return [i for i, d in enumerate(deg) if d == 1 and i != root]


def parent_neighborhood(parent):
    intervals, tau = parent
    if len(intervals) == 1:
        return {((1, 2),)}
    leaf = canonical_leaf(intervals, tau)
    return candidate_outputs(intervals, tau, forced_last=leaf)


def expand_parent_tree(parent_target, J, n):
    """Undo parent port compression, restoring the child labels outside J."""
    removed = set(J)
    remaining = [x for x in range(1, n + 1) if x not in removed]
    return tuple(sorted(tuple(sorted((remaining[a - 1], remaining[b - 1])))
                        for a, b in parent_target))


def one_switch_lifts(parent_target, J):
    """All guarded outputs of inserting J into the fixed parent tree."""
    a, b = J
    out = set()
    for u, v in parent_target:
        if not (u < b and a < v or u < a and b < v or a < u < b < v
                or a < v < b < u):
            # Use the exact overlap predicate below; this branch is only a
            # cheap reject for disjoint edges and is intentionally symmetric.
            if not (u < b and a < v):
                continue
        if not (min(u, v) < b and a < max(u, v)):
            continue
        xs = sorted((a, b, u, v))
        old = tuple(sorted((u, v)))
        for local in LOCAL_TREES:
            mapped = {
                tuple(sorted((xs[i], xs[j]))) for i, j in local
            }
            if old in mapped:
                continue
            tree = (set(parent_target) - {old}) | mapped
            if len(tree) == len(parent_target) + 2:
                out.add(tuple(sorted(tree)))
    return out


class Dinic:
    def __init__(self, n):
        self.n = n
        self.head = array('i', [-1]) * n
        self.to = array('i')
        self.cap = array('q')
        self.nxt = array('i')

    def add(self, u, v, c):
        i = len(self.to)
        self.to.append(v); self.cap.append(c); self.nxt.append(self.head[u]); self.head[u] = i
        self.to.append(u); self.cap.append(0); self.nxt.append(self.head[v]); self.head[v] = i + 1

    def maxflow(self, s, t, limit):
        flow = 0
        level = array('i', [-1]) * self.n
        it = array('i', [0]) * self.n
        while flow < limit:
            for i in range(self.n):
                level[i] = -1
            level[s] = 0
            q = deque([s])
            while q:
                u = q.popleft()
                e = self.head[u]
                while e != -1:
                    v = self.to[e]
                    if self.cap[e] and level[v] < 0:
                        level[v] = level[u] + 1
                        q.append(v)
                    e = self.nxt[e]
            if level[t] < 0:
                return flow, level
            for i in range(self.n):
                it[i] = self.head[i]

            def dfs(u, f):
                if u == t:
                    return f
                e = it[u]
                while e != -1:
                    it[u] = e
                    v = self.to[e]
                    if self.cap[e] and level[v] == level[u] + 1:
                        z = dfs(v, min(f, self.cap[e]))
                        if z:
                            self.cap[e] -= z
                            self.cap[e ^ 1] += z
                            return z
                    e = self.nxt[e]
                    it[u] = e
                return 0

            while flow < limit:
                z = dfs(s, limit - flow)
                if not z:
                    break
                flow += z
        return flow, level



def enumerate_n6_parent_representatives(parent_sources, fibers):
    """Exhaust every injective parent representative assignment at n=6."""
    from itertools import product
    parents = sorted(parent_sources, key=repr)
    neighborhoods = [sorted(parent_neighborhood(p), key=repr) for p in parents]
    choices = []
    for assignment in product(*neighborhoods):
        if len(set(assignment)) != len(assignment):
            continue
        Q = dict(zip(parents, assignment))
        rows = []
        targets = {}
        for (p, J), children in sorted(fibers.items(), key=lambda z: repr(z[0])):
            P = expand_parent_tree(Q[p], J, 6)
            lifts = one_switch_lifts(P, J)
            d = sum((Fraction(1, len(nonroot_leaves(iv, tau)))
                     for iv, tau in children), Fraction(0))
            quota = (d.numerator + d.denominator - 1) // d.denominator
            ids = []
            for T in lifts:
                if T not in targets:
                    targets[T] = len(targets)
                ids.append(targets[T])
            rows.append((p, J, d, quota, sorted(set(ids))))
        F, T = len(rows), len(targets)
        S = 0; r0 = 1; t0 = r0 + F; sink = t0 + T
        net = Dinic(sink + 1)
        total = 0
        for i, row in enumerate(rows):
            net.add(S, r0+i, row[3]); total += row[3]
            for j in row[4]:
                net.add(r0+i, t0+j, 1)
        for j in range(T):
            net.add(t0+j, sink, 1)
        got, _ = net.maxflow(S, sink, total)
        choices.append((got == total, got, total, Q, rows, targets))
    passed = [x for x in choices if x[0]]
    print(f"  n6_parent_representative_assignments={len(choices)} "
          f"selector_feasible={len(passed)}", flush=True)
    if passed:
        for ok, got, total, Q, _, _ in passed[:3]:
            print(f"  feasible_Q={Q} flow={got}/{total}", flush=True)
    else:
        best = max(choices, key=lambda x: x[1])
        print(f"  best_Q={best[3]} flow={best[1]}/{best[2]}", flush=True)
        # Show the exact minimal deficient row family from the min cut.
        Q = best[3]
        for p, J, d, quota, _ in best[4]:
            if quota > 1:
                P = expand_parent_tree(Q[p], J, 6)
                print(f"  high_quota_row parent={p} J={J} demand={d} "
                      f"quota={quota} lifts={one_switch_lifts(P,J)}", flush=True)


def run(n, expected_sources):
    source_rows = list(sources(n))
    assert len(source_rows) == expected_sources
    fibers = defaultdict(list)
    parent_sources = set()
    for intervals, tau in source_rows:
        parent_sources.update(
            parent_data(intervals, tau, leaf)
            for leaf in nonroot_leaves(intervals, tau)
        )
        for leaf in nonroot_leaves(intervals, tau):
            J = intervals[leaf]
            p = parent_data(intervals, tau, leaf)
            fibers[(p, J)].append((intervals, tau))

    # One injective representative target per parent source.
    parents = sorted(parent_sources, key=repr)
    parent_neigh = [parent_neighborhood(p) for p in parents]
    right_parent = sorted(set().union(*parent_neigh), key=repr)
    rid = {t: i for i, t in enumerate(right_parent)}
    adj = [[rid[t] for t in sorted(row, key=repr)] for row in parent_neigh]
    ml = [-1] * len(adj); mr = [-1] * len(right_parent)
    dist = [0] * len(adj)

    def bfs():
        q = deque()
        found = False
        for u in range(len(adj)):
            if ml[u] < 0:
                dist[u] = 0; q.append(u)
            else:
                dist[u] = -1
        while q:
            u = q.popleft()
            for v in adj[u]:
                w = mr[v]
                if w < 0:
                    found = True
                elif dist[w] < 0:
                    dist[w] = dist[u] + 1; q.append(w)
        return found

    def dfs(u):
        for v in adj[u]:
            w = mr[v]
            if w < 0 or (dist[w] == dist[u] + 1 and dfs(w)):
                ml[u] = v; mr[v] = u
                return True
        dist[u] = -1
        return False

    while bfs():
        for u in range(len(adj)):
            if ml[u] < 0:
                dfs(u)
    pm = sum(v >= 0 for v in ml)
    print(f"n={n}: child_sources={len(source_rows)} parent_sources={len(parents)} "
          f"parent_matching={pm}/{len(parents)}", flush=True)
    assert pm == len(parents), "No injective parent representative matching Q."

    Q = {parents[i]: right_parent[ml[i]] for i in range(len(parents))}
    rows = []
    target_ids = {}
    max_demand = Fraction(0)
    for (p, J), children in sorted(fibers.items(), key=lambda z: repr(z[0])):
        # All child sources in a fixed (p,J) fiber must have the same d-neighborhood.
        P = expand_parent_tree(Q[p], J, n)
        lifts = one_switch_lifts(P, J)
        assert lifts, ("empty fixed-representative row", n, p, J)
        d = sum((Fraction(1, len(nonroot_leaves(iv, tau)))
                 for iv, tau in children), Fraction(0))
        quota = (d.numerator + d.denominator - 1) // d.denominator
        max_demand = max(max_demand, d)
        if quota == 0:
            continue
        ids = []
        for T in lifts:
            if T not in target_ids:
                target_ids[T] = len(target_ids)
            ids.append(target_ids[T])
        rows.append((p, J, d, quota, sorted(set(ids))))
    F = len(rows); T = len(target_ids)
    S = 0; row0 = 1; target0 = row0 + F; sink = target0 + T
    flow = Dinic(sink + 1)
    total = 0
    for i, (_, _, d, quota, neigh) in enumerate(rows):
        flow.add(S, row0 + i, quota); total += quota
        for j in neigh:
            flow.add(row0 + i, target0 + j, 1)
    for j in range(T):
        flow.add(target0 + j, sink, 1)
    got, level = flow.maxflow(S, sink, total)
    print(f"  rows={F} targets={T} integer_demand={total} "
          f"max_row_fractional_demand={max_demand} flow={got}/{total}", flush=True)
    if got != total:
        cut_rows = [i for i in range(F) if level[row0 + i] >= 0]
        cut_targets = set()
        for i in cut_rows:
            cut_targets.update(rows[i][4])
        demand = sum(rows[i][3] for i in cut_rows)
        print(f"  HALL_FAILURE rows={len(cut_rows)} neighbors={len(cut_targets)} "
              f"quota_sum={demand} deficiency={demand-len(cut_targets)}")
        print("  first_rows=" + repr([
            (rows[i][0], rows[i][1], str(rows[i][2]), rows[i][3],
             len(rows[i][4])) for i in cut_rows[:12]
        ]))
        if n == 6:
            enumerate_n6_parent_representatives(parent_sources, fibers)
        raise SystemExit(1)
    print(f"PASS n={n}: exact integer selector Hall condition.", flush=True)


if __name__ == "__main__":
    run(6, 22)
    run(8, 608)
