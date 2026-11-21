#!/usr/bin/env python3
"""Test source-constrained parent exchange connectivity for PF-I16 leaf peeling.

For each parent fiber, build the graph on C(p) whose edges are single
graphic-basis exchanges (tree symmetric difference of size 2). For every
child target shared by two or more children in that fiber, collect the
unique parent projections and test whether they lie in one connected
component of this admissible graph. This is a finite diagnostic, not a
proof of the all-orders exchange lemma.
"""
from collections import defaultdict, deque
from verify_pf_i16_source_dependent_leaf_peeling import (
    canonical_leaf, parent_data, inverse_last_switch, compress_tree, sources,
)
from verify_pf_i16_local_switch_fractional_transport import candidate_outputs


def connected_in_admissible_graph(vertices, a, b):
    if a == b:
        return True
    todo = deque([a])
    seen = {a}
    while todo:
        x = todo.popleft()
        for y in vertices:
            if y not in seen and len(set(x) ^ set(y)) == 2:
                if y == b:
                    return True
                seen.add(y)
                todo.append(y)
    return False


def run(n, expected):
    fibers = defaultdict(list)
    parent_targets = {}
    child_rows = {}
    projections = {}
    for intervals, tau in sources(n):
        leaf = canonical_leaf(intervals, tau)
        J = intervals[leaf]
        p = parent_data(intervals, tau, leaf)
        outputs = candidate_outputs(intervals, tau, forced_last=leaf)
        row = {}
        for T in outputs:
            inv = inverse_last_switch(T, J, n)
            assert len(inv) == 1
            row[T] = compress_tree(next(iter(inv)), set(J), n)
        child = (intervals, tau)
        fibers[p].append(child)
        child_rows[child] = outputs
        projections[child] = row
    for p in fibers:
        parent_targets[p] = candidate_outputs(*p)

    shared_targets = 0
    collision_pairs = 0
    disconnected_pairs = []
    max_distance = 0
    for p, children in fibers.items():
        admissible = parent_targets[p]
        # Each shared child target induces one pairwise collision for every
        # pair of children that can reach it.
        owners = defaultdict(list)
        for child in children:
            for T in child_rows[child]:
                owners[T].append(child)
        for T, who in owners.items():
            if len(who) < 2:
                continue
            shared_targets += 1
            ps = [projections[ch][T] for ch in who]
            for i in range(len(ps)):
                for j in range(i + 1, len(ps)):
                    collision_pairs += 1
                    a, b = ps[i], ps[j]
                    # BFS also returns shortest admissible exchange distance.
                    q = deque([(a, 0)])
                    seen = {a}
                    dist = None
                    while q:
                        x, d = q.popleft()
                        if x == b:
                            dist = d
                            break
                        for y in admissible:
                            if y not in seen and len(set(x) ^ set(y)) == 2:
                                seen.add(y)
                                q.append((y, d + 1))
                    if dist is None:
                        disconnected_pairs.append((p, T, a, b))
                    else:
                        max_distance = max(max_distance, dist)
    print(f"n={n}: parent_fibers={len(fibers)}, shared_child_targets={shared_targets}, "
          f"projection_collision_pairs={collision_pairs}, "
          f"disconnected_pairs={len(disconnected_pairs)}, "
          f"max_shortest_admissible_exchange_distance={max_distance}")
    if disconnected_pairs:
        print("  first_disconnection=", disconnected_pairs[0])
    assert sum(map(len, fibers.values())) == expected
    return not disconnected_pairs


def main():
    ok = True
    ok &= run(4, 2)
    ok &= run(6, 22)
    ok &= run(8, 608)
    print("Admissible parent-exchange connectivity test:", "PASS" if ok else "FAIL")
    if not ok:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
