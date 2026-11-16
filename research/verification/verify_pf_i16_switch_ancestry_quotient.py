#!/usr/bin/env python3
"""Ancestry-resolved version of the PF-I16 three-move transport enumerator.

Unlike the set-valued candidate enumerator, this records every insertion
history ending at each target tree.  It then quotients histories sourcewise:
the transport still assigns 1 / (# DISTINCT output trees) to a source-target
incidence, never 1 / (# histories).

This is a diagnostic certificate generator.  It makes history coalescence
visible and prevents a history count from being mistaken for transport mass.
"""
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import permutations

from verify_pf_i16_local_switch_fractional_transport import (
    LOCAL_TREES, components, load, matchings, overlap_edges,
    spanning_trees, verify_tree, local_path,
)


def ancestry_outputs(intervals, tau):
    """Return target -> (number of histories, lexicographically first history).

    A history step is (child_interval_index, replaced_edge, local_tree_index).
    Child order is parent-before-child.  Distinct histories may coalesce to
    the same final labeled tree; they are counted but then quotiented here.
    """
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
    # A state retains the complete history, not just its current tree.
    final_histories = defaultdict(list)
    for order in permutations(vertices):
        position = {u: i for i, u in enumerate(order)}
        if any(parent[u] != root and position[parent[u]] > position[u]
               for u in vertices):
            continue

        states = [(
            {root: [intervals[root][0], intervals[root][1]]},
            frozenset({tuple(sorted(intervals[root]))}),
            (),
        )]
        for child in order:
            J = intervals[child]
            next_states = []
            for paths, tree_edges, history in states:
                for u, w in sorted(tree_edges):
                    if max(u, J[0]) >= min(w, J[1]):
                        continue
                    xs = sorted((u, w, J[0], J[1]))
                    local_edge = tuple(sorted((u, w)))
                    assert local_edge in tree_edges
                    for local_index, local in enumerate(LOCAL_TREES):
                        mapped = tuple(
                            tuple(sorted((xs[a], xs[b]))) for a, b in local
                        )
                        if local_edge in mapped:
                            continue
                        old_path = local_path(mapped, tuple(xs), u, w)
                        child_path = local_path(mapped, tuple(xs), J[0], J[1])
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
                        step = (child, local_edge, local_index)
                        next_states.append((
                            new_paths, frozenset(new_edges), history + (step,)
                        ))
            states = next_states

        for _, tree_edges, history in states:
            target = tuple(sorted(tree_edges))
            # Independently replay the exact inverse transition from this
            # fixed final tree, deleting the newest interval at each step.
            reverse_history(intervals, history, target, 2 * v)
            final_histories[target].append((order, history))

    result = {}
    for target, histories in final_histories.items():
        canonical = min(histories)
        result[target] = (len(histories), canonical)
    return result


def reverse_history(intervals, history, target, n):
    """Invert a complete forward history from its fixed final tree.

    At each reverse step, the two endpoints of the last inserted interval
    must have exactly their prescribed local-switch incidences. Delete those
    vertices and restore the replaced edge. This is the inverse transition,
    not a count of raw histories.
    """
    current = set(target)
    remaining = set(range(1, n + 1))
    for child, old_edge, local_index in reversed(history):
        a, b = intervals[child]
        u, w = old_edge
        xs = sorted((u, w, a, b))
        local = LOCAL_TREES[local_index]
        mapped = {
            tuple(sorted((xs[i], xs[j]))) for i, j in local
        }
        expected = {edge for edge in mapped if a in edge or b in edge}
        actual = {edge for edge in current if a in edge or b in edge}
        assert actual == expected, (
            "reverse incidence obstruction", intervals, history,
            tuple(sorted(current)), child, old_edge, local_index,
            actual, expected,
        )
        assert tuple(sorted(old_edge)) not in mapped, (
            "replaced edge reappears in local switch", intervals, history,
            tuple(sorted(current)), mapped,
        )
        assert mapped <= current, (
            "missing local switch tree", intervals, history,
            tuple(sorted(current)), mapped,
        )
        current = {
            edge for edge in current if a not in edge and b not in edge
        }
        current.add(tuple(sorted(old_edge)))
        remaining.remove(a)
        remaining.remove(b)

        # The inverse must be a tree on exactly the surviving vertices.
        assert len(current) == len(remaining) - 1
        parent = {v: v for v in remaining}
        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        for x, y in current:
            rx, ry = find(x), find(y)
            assert rx != ry, ("reverse cycle", current, remaining)
            parent[rx] = ry
        assert len({find(v) for v in remaining}) == 1

    root = next(I for I in intervals if I[0] == 1)
    assert remaining == set(root)
    assert current == {tuple(sorted(root))}
    return tuple(sorted(current))


def run(n):
    columns = Counter()
    incidence = Counter()
    raw_history_count = Counter()
    max_coalescence = 0
    max_coalescence_example = None
    source_count = 0
    for matching in matchings(range(1, n + 1)):
        intervals = tuple(sorted(tuple(sorted(e)) for e in matching))
        overlap = overlap_edges(intervals)
        matching_load = load(intervals, n)
        for tau in spanning_trees(len(intervals), overlap):
            outputs = ancestry_outputs(intervals, tau)
            degree = len(outputs)
            assert degree >= 3 ** (n // 2 - 1)
            source_count += 1
            weight = Fraction(1, degree)
            for T, (history_count, canonical) in outputs.items():
                verify_tree(T, n)
                assert all(a <= b for a, b in zip(load(T, n), matching_load))
                columns[T] += weight
                incidence[T] += 1
                raw_history_count[T] += history_count
                if history_count > max_coalescence:
                    max_coalescence = history_count
                    max_coalescence_example = (intervals, tau, T, history_count, canonical)

    worst = max(columns, key=columns.get)
    print(f"n={n}: sources={source_count}, targets={len(columns)}")
    print(f"  max weighted column={columns[worst]} at {worst}")
    print(f"  worst target distinct source incidences={incidence[worst]}")
    print(f"  worst target raw histories={raw_history_count[worst]}")
    print(f"  global max histories for one source-target pair={max_coalescence}")
    print(f"  max-coalescence example={max_coalescence_example}")
    assert columns[worst] <= 1


if __name__ == "__main__":
    run(4)
    run(6)
    print("NOTE: histories are diagnostic; the transport quotient is source-target incidence.")
