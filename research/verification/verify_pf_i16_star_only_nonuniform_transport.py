#!/usr/bin/env python3
"""Exact Hall obstruction for nonuniform transport on the star-only relation.

A unit source can be split arbitrarily among its distinct star-only candidate
trees, with target capacity one, iff the candidate bipartite graph has a
matching saturating every source (integrality of bipartite max flow).

This verifier enumerates the relation at n=4,6 and runs Hopcroft-Karp in each
exact cut-load class. It emits an alternating-reachability Hall witness when
the relation is infeasible. It does not test the full relation c(T)<=m(M).
"""
from collections import defaultdict, deque
from itertools import combinations, permutations


def matchings(items):
    items = tuple(items)
    if not items:
        yield ()
        return
    a = items[0]
    for j in range(1, len(items)):
        for tail in matchings(items[1:j] + items[j + 1:]):
            yield ((a, items[j]),) + tail


def overlap_edges(intervals):
    return tuple(
        (i, j) for i in range(len(intervals)) for j in range(i + 1, len(intervals))
        if max(intervals[i][0], intervals[j][0])
        < min(intervals[i][1], intervals[j][1])
    )


def spanning_trees(v, edges):
    if v == 1:
        yield ()
        return
    for chosen in combinations(edges, v - 1):
        parent = list(range(v))
        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        valid = True
        for a, b in chosen:
            x, y = find(a), find(b)
            if x == y:
                valid = False
                break
            parent[x] = y
        if valid and len({find(i) for i in range(v)}) == 1:
            yield chosen


STARS = (
    ((0, 1), (1, 2), (1, 3)),
    ((0, 2), (1, 2), (2, 3)),
)


def candidate_outputs(intervals, tau):
    root = next(i for i, I in enumerate(intervals) if I[0] == 1)
    adj = [[] for _ in intervals]
    for a, b in tau:
        adj[a].append(b)
        adj[b].append(a)
    parent = {root: None}
    stack = [root]
    while stack:
        u = stack.pop()
        for w in adj[u]:
            if w not in parent:
                parent[w] = u
                stack.append(w)
    vertices = [i for i in range(len(intervals)) if i != root]
    outputs = set()
    for order in permutations(vertices):
        pos = {u: i for i, u in enumerate(order)}
        if any(parent[u] != root and pos[parent[u]] > pos[u]
               for u in vertices):
            continue
        states = {frozenset({tuple(sorted(intervals[root]))})}
        for child in order:
            a, b = intervals[child]
            next_states = set()
            for tree in states:
                for u, w in tree:
                    if max(u, a) >= min(w, b):
                        continue
                    xs = sorted((u, w, a, b))
                    for star in STARS:
                        replacement = {
                            tuple(sorted((xs[i], xs[j]))) for i, j in star
                        }
                        new_tree = set(tree)
                        new_tree.remove((u, w))
                        new_tree.update(replacement)
                        next_states.add(frozenset(new_tree))
            states = next_states
            assert states, (intervals, tau, order, child)
        outputs.update(tuple(sorted(tree)) for tree in states)
    return outputs


def cut_load(edges, n):
    return tuple(sum(a <= k < b for a, b in edges) for k in range(1, n))


def hopcroft_karp(adjacency, right_count):
    left_count = len(adjacency)
    pair_left = [-1] * left_count
    pair_right = [-1] * right_count
    distance = [0] * left_count
    inf = 10**9

    def bfs():
        queue = deque()
        found = False
        for u in range(left_count):
            if pair_left[u] < 0:
                distance[u] = 0
                queue.append(u)
            else:
                distance[u] = inf
        while queue:
            u = queue.popleft()
            for v in adjacency[u]:
                mate = pair_right[v]
                if mate < 0:
                    found = True
                elif distance[mate] == inf:
                    distance[mate] = distance[u] + 1
                    queue.append(mate)
        return found

    def dfs(u):
        for v in adjacency[u]:
            mate = pair_right[v]
            if mate < 0 or (distance[mate] == distance[u] + 1 and dfs(mate)):
                pair_left[u] = v
                pair_right[v] = u
                return True
        distance[u] = inf
        return False

    while bfs():
        for u in range(left_count):
            if pair_left[u] < 0:
                dfs(u)

    # Alternating reachability from unmatched left vertices gives S,N(S).
    reachable_left = {u for u in range(left_count) if pair_left[u] < 0}
    reachable_right = set()
    queue = deque((0, u) for u in reachable_left)
    while queue:
        side, x = queue.popleft()
        if side == 0:
            for v in adjacency[x]:
                if v != pair_left[x] and v not in reachable_right:
                    reachable_right.add(v)
                    queue.append((1, v))
        else:
            mate = pair_right[x]
            if mate >= 0 and mate not in reachable_left:
                reachable_left.add(mate)
                queue.append((0, mate))
    size = sum(v >= 0 for v in pair_left)
    return size, reachable_left, reachable_right


def check(n, expected_sources, expected_profiles):
    classes = defaultdict(list)
    source_count = 0
    for matching in matchings(range(1, n + 1)):
        intervals = tuple(sorted(tuple(sorted(e)) for e in matching))
        profile = cut_load(intervals, n)
        overlap = overlap_edges(intervals)
        for tau in spanning_trees(len(intervals), overlap):
            outputs = candidate_outputs(intervals, tau)
            assert outputs
            for tree in outputs:
                assert cut_load(tree, n) == profile
            classes[profile].append(outputs)
            source_count += 1

    assert source_count == expected_sources, (n, source_count)
    assert len(classes) == expected_profiles, (n, len(classes))
    print(f"n={n}: sources={source_count}, exact_profiles={len(classes)}")
    for profile, source_sets in sorted(classes.items()):
        targets = sorted(set().union(*source_sets))
        target_index = {tree: i for i, tree in enumerate(targets)}
        adjacency = [
            [target_index[t] for t in sorted(outputs)]
            for outputs in source_sets
        ]
        matching_size, hall_left, hall_right = hopcroft_karp(
            adjacency, len(targets)
        )
        feasible = matching_size == len(source_sets)
        assert len(hall_left) >= len(hall_right)
        print(
            f"  profile={profile}: sources={len(source_sets)}, "
            f"candidate_targets={len(targets)}, max_matching={matching_size}, "
            f"fractional_transport={'FEASIBLE' if feasible else 'INFEASIBLE'}"
        )
        if not feasible:
            print(
                f"    Hall witness: |S|={len(hall_left)}, "
                f"|N(S)|={len(hall_right)}, deficiency="
                f"{len(hall_left)-len(hall_right)}"
            )
            assert len(hall_left) > len(hall_right)


def main():
    check(4, expected_sources=2, expected_profiles=1)
    check(6, expected_sources=22, expected_profiles=2)
    print("PASS: star-only nonuniform transport is feasible at n=4")
    print("CONFIRMED: star-only nonuniform transport is impossible at n=6")
    print("This obstruction is confined to the star-only candidate relation.")


if __name__ == "__main__":
    main()
