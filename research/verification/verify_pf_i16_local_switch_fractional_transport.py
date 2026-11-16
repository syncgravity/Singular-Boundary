#!/usr/bin/env python3
"""Finite fractional Hall certificate from all local-switch outputs.

For each left object (M,tau), enumerate every output tree obtainable by:
- rooting tau at the interval containing port 1;
- choosing any parent-before-child order;
- choosing any overlapping edge on the current parent-interval path; and
- choosing one of the two middle-centered stars or the increasing path.

Each source sends unit mass uniformly over its DISTINCT output trees. The
verifier checks that every port tree receives total mass at most one. Since
every output T satisfies c(T) <= m(M), this is a fractional Hall certificate
for every down-set at the tested orders. It is finite evidence only.
"""
from collections import Counter
from fractions import Fraction
from itertools import permutations


def matchings(items):
    items = tuple(items)
    if not items:
        yield ()
        return
    a = items[0]
    for j in range(1, len(items)):
        b = items[j]
        for tail in matchings(items[1:j] + items[j + 1:]):
            yield ((a, b),) + tail


def overlap_edges(intervals):
    return tuple(
        (i, j) for i in range(len(intervals))
        for j in range(i + 1, len(intervals))
        if max(intervals[i][0], intervals[j][0])
        < min(intervals[i][1], intervals[j][1])
    )


def components(v, edges, mask):
    parent = list(range(v))
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    for bit, (a, b) in enumerate(edges):
        if (mask >> bit) & 1:
            x, y = find(a), find(b)
            if x == y:
                return None
            parent[x] = y
    return {find(i) for i in range(v)}


def spanning_trees(v, edges):
    if v == 1:
        yield ()
        return
    for mask in range(1 << len(edges)):
        if mask.bit_count() != v - 1:
            continue
        c = components(v, edges, mask)
        if c is not None and len(c) == 1:
            yield tuple(edges[i] for i in range(len(edges))
                        if (mask >> i) & 1)


def local_path(local_edges, vertices, start, end):
    adj = {x: [] for x in vertices}
    for a, b in local_edges:
        adj[a].append(b)
        adj[b].append(a)
    stack = [(start, [start])]
    seen = set()
    while stack:
        v, path = stack.pop()
        if v == end:
            return path
        if v in seen:
            continue
        seen.add(v)
        for w in adj[v]:
            if w not in seen:
                stack.append((w, path + [w]))
    raise AssertionError((local_edges, start, end))


LOCAL_TREES = (
    ((0, 1), (1, 2), (1, 3)),  # star centered at x_2
    ((0, 1), (1, 2), (2, 3)),  # increasing path
    ((0, 2), (1, 2), (2, 3)),  # star centered at x_3
)



def tree_path(edges, start, end):
    adj = {}
    for a, b in edges:
        adj.setdefault(a, []).append(b)
        adj.setdefault(b, []).append(a)
    parent = {start: None}
    stack = [start]
    while stack:
        u = stack.pop()
        if u == end:
            break
        for w in adj.get(u, ()):
            if w not in parent:
                parent[w] = u
                stack.append(w)
    assert end in parent, (edges, start, end)
    path = []
    u = end
    while u is not None:
        path.append(u)
        u = parent[u]
    return tuple(reversed(path))


def overlaps(edge, interval):
    u, w = sorted(edge)
    a, b = interval
    return max(u, a) < min(w, b)

def candidate_outputs(intervals, tau):
    v = len(intervals)
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
    vertices = [i for i in range(v) if i != root]
    outputs = set()

    for order in permutations(vertices):
        position = {u: i for i, u in enumerate(order)}
        if any(parent[u] != root and position[parent[u]] > position[u]
               for u in vertices):
            continue

        states = [(
            {root: [intervals[root][0], intervals[root][1]]},
            frozenset({tuple(sorted(intervals[root]))}),
        )]
        for child in order:
            J = intervals[child]
            next_states = []
            for paths, tree_edges in states:
                # The parent interval and J interleave. On the unique
                # current-tree path between the parent endpoints, the first
                # edge leaving the open interval (J[0], J[1]) overlaps J.
                parent_interval = intervals[parent[child]]
                ppath = tree_path(tree_edges, *parent_interval)
                path_edges = tuple(zip(ppath, ppath[1:]))
                guaranteed = tuple(e for e in path_edges if overlaps(e, J))
                assert guaranteed, (
                    "parent path has no edge overlapping child interval",
                    intervals, tau, order, child, parent_interval, ppath, J,
                )
                # Keep the full edge-choice relation, but explicitly retain
                # the path witness in the candidate set and assert its two
                # guarded local replacements below.
                for u, w in sorted(tree_edges):
                    if not overlaps((u, w), J):
                        continue
                    xs = sorted((u, w, J[0], J[1]))
                    local_edge = tuple(sorted((u, w)))
                    assert local_edge in tree_edges
                    for local in LOCAL_TREES:
                        mapped = tuple(
                            tuple(sorted((xs[a], xs[b]))) for a, b in local
                        )
                        if local_edge in mapped:
                            continue
                        local_vertices = tuple(xs)
                        old_path = local_path(
                            mapped, local_vertices, u, w
                        )
                        child_path = local_path(
                            mapped, local_vertices, J[0], J[1]
                        )
                        new_edges = set(tree_edges)
                        new_edges.remove(local_edge)
                        new_edges.update(mapped)

                        new_paths = {}
                        for key, old in paths.items():
                            new = []
                            i = 0
                            while i < len(old):
                                if (i + 1 < len(old)
                                        and old[i] == u and old[i + 1] == w):
                                    new.extend(old_path)
                                    i += 2
                                else:
                                    new.append(old[i])
                                    i += 1
                            new_paths[key] = new
                        new_paths[child] = child_path
                        next_states.append(
                            (new_paths, frozenset(new_edges))
                        )
            assert len(next_states) >= 2 * len(states), (
                "fewer than two valid local choices per current state",
                intervals, tau, order, child, len(states), len(next_states),
            )
            states = next_states

        for _, tree_edges in states:
            outputs.add(tuple(sorted(tree_edges)))
    return outputs


def load(edges, n):
    return tuple(
        sum(a <= k < b for a, b in edges) for k in range(1, n)
    )


def verify_tree(edges, n):
    assert len(edges) == n - 1
    parent = list(range(n + 1))
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    for a, b in edges:
        x, y = find(a), find(b)
        assert x != y
        parent[x] = y
    assert len({find(i) for i in range(1, n + 1)}) == 1


def check(n, expected_sources, expected_union):
    source_count = 0
    columns = Counter()
    incidence = Counter()
    degree_profile = {}
    min_degree = None
    max_degree = 0
    for matching in matchings(range(1, n + 1)):
        intervals = tuple(sorted(tuple(sorted(e)) for e in matching))
        overlap = overlap_edges(intervals)
        matching_load = load(intervals, n)
        for tau in spanning_trees(len(intervals), overlap):
            outputs = candidate_outputs(intervals, tau)
            assert len(outputs) >= 2 ** (n // 2 - 1), (
                "source distinct-output lower bound failed", n, intervals, tau, len(outputs)
            )
            source_count += 1
            min_degree = (len(outputs) if min_degree is None
                          else min(min_degree, len(outputs)))
            max_degree = max(max_degree, len(outputs))
            weight = Fraction(1, len(outputs))
            for T in outputs:
                verify_tree(T, n)
                assert all(x <= y for x, y in zip(load(T, n), matching_load)), (
                    n, intervals, tau, T, load(T, n), matching_load
                )
                columns[T] += weight
                incidence[T] += 1
                degree_profile.setdefault(T, Counter())[len(outputs)] += 1

    assert source_count == expected_sources, (n, source_count)
    assert len(columns) == expected_union, (n, len(columns))
    max_column = max(columns.values())
    max_incidence = max(incidence.values())
    degree_floor = 2 ** (n // 2 - 1)
    incidence_over_floor = Fraction(max_incidence, degree_floor)
    worst_tree = max(columns, key=columns.get)
    profile = degree_profile[worst_tree]
    profile_mass = sum((Fraction(count, degree) for degree, count in profile.items()), Fraction())
    assert profile_mass == columns[worst_tree]
    status = "PASS" if max_column <= 1 else "OVERLOAD"
    print(
        f"{status} n={n}: left_objects={source_count}, "
        f"candidate_trees={len(columns)}, "
        f"source_degree_range=[{min_degree},{max_degree}], "
        f"max_fractional_column_load={float(max_column):.12f}, "
        f"max_source_incidence={max_incidence}, "
        f"2^(s-1)_degree_floor={degree_floor}, "
        f"max_incidence_over_floor={float(incidence_over_floor):.12f}"
    )
    harmonic_degree = Fraction(incidence[worst_tree], columns[worst_tree])
    degree_bins = ((1, 127), (128, 191), (192, 255),
                   (256, 383), (384, 10**9))
    binned_profile = []
    for lo, hi in degree_bins:
        count = sum(c for d, c in profile.items() if lo <= d <= hi)
        mass = sum((Fraction(c, d) for d, c in profile.items()
                    if lo <= d <= hi), Fraction())
        binned_profile.append((f"{lo}-{hi}", count, mass))
    print(
        f"  worst_tree={worst_tree}; incidence={incidence[worst_tree]}; "
        f"harmonic_mean_source_degree={float(harmonic_degree):.12f}; "
        f"degree_strata={sorted(profile.items())}; "
        f"reconstructed_column={profile_mass}"
    )
    print(f"  degree_bin_profile={binned_profile}")
    # Report the largest single degree-stratum contribution over all targets.
    stratum_max = max(
        (Fraction(count, degree), T, degree, count)
        for T, hist in degree_profile.items()
        for degree, count in hist.items()
    )
    print(
        f"  max_single_stratum_mass={stratum_max[0]} "
        f"at_tree={stratum_max[1]}, source_degree={stratum_max[2]}, "
        f"sources_in_stratum={stratum_max[3]}"
    )


def main():
    check(4, expected_sources=2, expected_union=3)
    check(6, expected_sources=22, expected_union=43)
    check(8, expected_sources=608, expected_union=1493)
    print("Finite guarded-relation enumeration complete; OVERLOAD means this uniform transport is not a Hall certificate.")
    print("NOTE incidence/degree comparison is diagnostic; no all-orders bound is claimed")


if __name__ == "__main__":
    main()
