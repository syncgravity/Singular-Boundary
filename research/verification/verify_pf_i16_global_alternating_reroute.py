#!/usr/bin/env python3
"""Global alternating-path diagnostic for PF-I16 leaf-last neighborhoods.

Build the complete child-source -> final-tree graph and a deterministic
left-saturating matching. For every target shared by multiple child sources,
test whether its matched owner can be rerouted along an alternating path to
an unmatched target. Such a path would allow any competing child to take the
shared target while preserving a left-saturating assignment.

This is a finite single-collision rerouting test, not a simultaneous
multi-collision theorem and not an all-orders Hall proof.
"""
from collections import defaultdict, deque
from verify_pf_i16_source_dependent_leaf_peeling import (
    canonical_leaf, parent_data, inverse_last_switch, compress_tree, sources,
)
from verify_pf_i16_local_switch_fractional_transport import candidate_outputs


def hopcroft_karp(rows):
    right = {t: i for i, t in enumerate(sorted({t for row in rows for t in row}))}
    adj = [[right[t] for t in sorted(row)] for row in rows]
    nl, nr = len(adj), len(right)
    ml, mr = [-1] * nl, [-1] * nr
    inf = nl + nr + 1
    dist = [inf] * nl

    def bfs():
        q = deque()
        found = inf
        for u in range(nl):
            if ml[u] < 0:
                dist[u] = 0
                q.append(u)
            else:
                dist[u] = inf
        while q:
            u = q.popleft()
            if dist[u] >= found:
                continue
            for v in adj[u]:
                w = mr[v]
                if w < 0:
                    found = dist[u] + 1
                elif dist[w] == inf:
                    dist[w] = dist[u] + 1
                    q.append(w)
        return found < inf

    def dfs(u):
        for v in adj[u]:
            w = mr[v]
            if w < 0 or (dist[w] == dist[u] + 1 and dfs(w)):
                ml[u], mr[v] = v, u
                return True
        dist[u] = inf
        return False

    while bfs():
        for u in range(nl):
            if ml[u] < 0:
                dfs(u)
    ordered_right = sorted(right, key=right.get)
    return ml, mr, ordered_right


def reroute_from_target(start, rows, matched_left, right_owner, child_fiber):
    """Find alternating path R -> matched L -> unmatched R -> ... -> free R."""
    q = deque([start])
    predecessor = {start: None}
    predecessor_owner = {}
    while q:
        target = q.popleft()
        owner = right_owner.get(target)
        if owner is None:
            targets = []
            owners = []
            cur = target
            while cur is not None:
                targets.append(cur)
                prev = predecessor[cur]
                if prev is not None:
                    owners.append(predecessor_owner[cur])
                cur = prev
            targets.reverse()
            owners.reverse()
            fibers = {child_fiber[x] for x in owners}
            return targets, len(fibers)
        for nxt in rows[owner]:
            if nxt == matched_left[owner] or nxt in predecessor:
                continue
            predecessor[nxt] = target
            predecessor_owner[nxt] = owner
            q.append(nxt)
    return None, None


def run(n, expected_sources):
    child_rows = []
    child_fibers = []
    child_projection = []
    fiber_children = defaultdict(list)
    parent_neighborhoods = {}
    target_owners = defaultdict(list)

    for intervals, tau in sources(n):
        leaf = canonical_leaf(intervals, tau)
        J = intervals[leaf]
        p = parent_data(intervals, tau, leaf)
        parent_neighborhoods.setdefault(p, None)
        outputs = candidate_outputs(intervals, tau, forced_last=leaf)
        row_projection = {}
        for T in outputs:
            inv = inverse_last_switch(T, J, n)
            assert len(inv) == 1
            P = compress_tree(next(iter(inv)), set(J), n)
            row_projection[T] = P
        idx = len(child_rows)
        child_rows.append(outputs)
        child_fibers.append(p)
        child_projection.append(row_projection)
        fiber_children[p].append(idx)
        for T in outputs:
            target_owners[T].append(idx)

    for p in parent_neighborhoods:
        parent_neighborhoods[p] = candidate_outputs(*p)
    for i, row in enumerate(child_rows):
        assert all(child_projection[i][T] in parent_neighborhoods[child_fibers[i]]
                   for T in row)

    ml, mr, right_index = hopcroft_karp(child_rows)
    assert sum(v >= 0 for v in ml) == expected_sources
    matched_left = {i: next(t for t, j in right_index.items() if j == ml[i])
                    for i in range(len(ml))}
    target_by_index = {j: t for t, j in right_index.items()}
    right_owner = {target_by_index[j]: i for j, i in enumerate(mr) if i >= 0}
    free_targets = sum(v < 0 for v in mr)
    right = sorted(right_index, key=right_index.get)

    collision_targets = [T for T, owners in target_owners.items()
                         if len(owners) > 1]
    collision_pairs = sum(len(owners) * (len(owners) - 1) // 2
                          for owners in target_owners.values())
    tested = repaired = 0
    max_alt_edges = max_fibers = 0
    first_failure = None
    path_lengths = defaultdict(int)
    for T in collision_targets:
        matched_owner = right_owner[T]
        for challenger in target_owners[T]:
            if challenger == matched_owner:
                continue
            tested += 1
            path, fiber_hops = reroute_from_target(
                T, child_rows, matched_left, right_owner, child_fibers
            )
            if path is None:
                if first_failure is None:
                    first_failure = (T, matched_owner, challenger)
                continue
            repaired += 1
            edges = (len(path) - 1) // 2
            max_alt_edges = max(max_alt_edges, edges)
            max_fibers = max(max_fibers, fiber_hops)
            path_lengths[edges] += 1

    print(f"n={n}: sources={len(child_rows)}, target_union={len(right)}, "
          f"parent_fibers={len(fiber_children)}, free_targets={free_targets}")
    print(f"  collision_targets={len(collision_targets)}, "
          f"collision_pairs={collision_pairs}, "
          f"challenger_reroutes={repaired}/{tested}, "
          f"reroute_failures={tested-repaired}, "
          f"max_alternating_steps={max_alt_edges}, "
          f"max_parent_fibers_on_path={max_fibers}")
    print(f"  alternating_path_length_histogram={dict(sorted(path_lengths.items()))}")
    if first_failure:
        T, owner, challenger = first_failure
        print(f"  first_failure_target={T}")
        print(f"  matched_owner_parent={child_fibers[owner]}")
        print(f"  challenger_parent={child_fibers[challenger]}")
    assert len(child_rows) == expected_sources
    return tested == repaired


def main():
    ok = True
    ok &= run(4, 2)
    ok &= run(6, 22)
    ok &= run(8, 608)
    print("Global alternating reroute test:", "PASS" if ok else "FAIL")
    if not ok:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
