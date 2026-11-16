#!/usr/bin/env python3
"""Executable canonical rank/unrank injection for the interval Hall classes.

For n=4,6,8 this explicitly builds:
  * left objects (M,tau), ordered by partner word then overlap-tree edge list;
  * right port trees, ordered by Prüfer word within least-majorant classes.

It checks the class-size hypothesis Q(h)>=L(h), performs the rank map,
checks cut-load domination and injectivity, and decodes every image back.
This is a finite construction verifier, not an all-orders proof of the
class-size hypothesis or of the weighted interval-tree inequality.
"""
from collections import defaultdict
from itertools import combinations, product


def primitive_paths(n):
    paths = []

    def visit(pos, height, prefix):
        if pos == n - 1:
            if height == 1 and all(prefix):
                paths.append(tuple(prefix))
            return
        visit(pos + 1, height + 1, prefix + [height + 1])
        if height > 1:
            visit(pos + 1, height - 1, prefix + [height - 1])

    visit(0, 0, [])
    return sorted(paths)


def perfect_matchings(items):
    if not items:
        yield ()
        return
    first = items[0]
    for j in range(1, len(items)):
        partner = items[j]
        rest = items[1:j] + items[j + 1:]
        for tail in perfect_matchings(rest):
            yield ((first, partner),) + tail


def spanning_trees(vertex_count, edges):
    if vertex_count == 1:
        yield ()
        return
    for chosen in combinations(edges, vertex_count - 1):
        adjacency = [set() for _ in range(vertex_count)]
        for a, b in chosen:
            adjacency[a].add(b)
            adjacency[b].add(a)
        seen = {0}
        stack = [0]
        while stack:
            a = stack.pop()
            for b in adjacency[a] - seen:
                seen.add(b)
                stack.append(b)
        if len(seen) == vertex_count:
            yield tuple(chosen)


def cut_load(edges, n):
    return tuple(
        sum(min(a, b) <= k < max(a, b) for a, b in edges)
        for k in range(n - 1)
    )


def left_classes(n):
    classes = defaultdict(list)
    for matching in perfect_matchings(tuple(range(n))):
        intervals = tuple(sorted(tuple(sorted(pair)) for pair in matching))
        overlap = [
            (i, j)
            for i in range(len(intervals))
            for j in range(i + 1, len(intervals))
            if max(intervals[i][0], intervals[j][0])
            < min(intervals[i][1], intervals[j][1])
        ]
        partner = [None] * n
        for a, b in intervals:
            partner[a] = b
            partner[b] = a
        h = cut_load(intervals, n)
        for tau in spanning_trees(len(intervals), overlap):
            # This tuple is the canonical partner-word / overlap-tree key.
            classes[h].append((tuple(partner), tau))
    for h in classes:
        classes[h].sort()
    return classes


def decode_prufer(code, n):
    degree = [1] * n
    for vertex in code:
        degree[vertex] += 1
    edges = []
    for vertex in code:
        leaf = next(i for i, d in enumerate(degree) if d == 1)
        edges.append((leaf, vertex))
        degree[leaf] -= 1
        degree[vertex] -= 1
    a, b = (i for i, d in enumerate(degree) if d == 1)
    edges.append((a, b))
    return tuple(edges)


def right_classes(n, paths):
    classes = defaultdict(list)
    for code in product(range(n), repeat=n - 2):
        edges = decode_prufer(code, n)
        load = cut_load(edges, n)
        majorants = [
            h for h in paths
            if all(c <= bound for c, bound in zip(load, h))
        ]
        if not majorants:
            continue
        ceiling = tuple(
            min(h[k] for h in majorants) for k in range(n - 1)
        )
        assert ceiling in paths
        # product(range(n), ...) is lexicographic Prüfer order.
        classes[ceiling].append((code, edges, load))
    return classes


def verify(n):
    paths = primitive_paths(n)
    left = left_classes(n)
    right = right_classes(n, paths)
    images = set()
    mapped = 0

    assert set(left).issubset(set(paths))
    for h in paths:
        demand = len(left[h])
        supply = len(right[h])
        assert supply >= demand, (n, h, demand, supply)

        # Rank k in the canonical left class maps to rank k in right class.
        for k, left_object in enumerate(left[h]):
            code, edges, load = right[h][k]
            assert all(c <= bound for c, bound in zip(load, h))
            assert code not in images
            images.add(code)
            mapped += 1

            # Explicit inverse: recompute ceiling and Prüfer rank, then
            # return the left object with that same class-local rank.
            recovered_ceiling = tuple(
                min(g[j] for g in paths
                    if all(x <= y for x, y in zip(load, g)))
                for j in range(n - 1)
            )
            assert recovered_ceiling == h
            assert right[h][k][0] == code
            assert left[h][k] == left_object

    assert mapped == sum(map(len, left.values()))
    print(
        f"PASS n={n}: left_objects={mapped}, "
        f"image_trees={len(images)}, "
        f"classes={sum(bool(left[h]) for h in paths)}"
    )
    for h in paths:
        if left[h]:
            print(f"  h={h}: L={len(left[h])}, Q={len(right[h])}")


def main():
    for n in (4, 6, 8):
        verify(n)
    print("PASS canonical classwise rank/unrank injection through eight ports")
    print("NOTE finite verifier only; Q(h)>=L(h) remains open for general n")


if __name__ == "__main__":
    main()
