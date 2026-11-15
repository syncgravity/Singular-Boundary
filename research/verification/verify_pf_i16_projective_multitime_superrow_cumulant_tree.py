#!/usr/bin/env python3
"""Finite combinatorial regression for the projective multi-time super-row tree.

This checks only the slot-partition connectivity and maximum-tree domination
used in PF_I16_PROJECTIVE_MULTITIME_SUPERROW_CUMULANT_TREE_2026_11_15.md.
It is not a verifier for the SU(2) semigroup or the analytic cumulant formula.
"""
from fractions import Fraction
from itertools import product
from math import factorial


def set_partitions(items):
    """Yield each set partition once, represented as tuples of frozensets."""
    items = tuple(items)
    if not items:
        yield ()
        return
    first, *rest = items
    for partition in set_partitions(rest):
        yield (frozenset((first,)),) + partition
        for k, block in enumerate(partition):
            merged = list(partition)
            merged[k] = block | {first}
            yield tuple(merged)


def canonical_partitions(items):
    # The recursive generator above can produce duplicates by block order.
    unique = set()
    for p in set_partitions(items):
        key = tuple(sorted((tuple(sorted(b)) for b in p)))
        unique.add(key)
    return [tuple(frozenset(b) for b in p) for p in sorted(unique)]


def dsu_find(parent, x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x


def dsu_union(parent, a, b):
    ra, rb = dsu_find(parent, a), dsu_find(parent, b)
    if ra != rb:
        parent[rb] = ra


def is_connected_rows(nrows, partitions_by_link):
    parent = list(range(nrows))
    for parts in partitions_by_link:
        for block in parts:
            rows = sorted({slot[0] for slot in block})
            for row in rows[1:]:
                dsu_union(parent, rows[0], row)
    return len({dsu_find(parent, i) for i in range(nrows)}) == 1


def block_max_tree_weight(block, ratio):
    times = [slot[1] for slot in block]
    return ratio ** (max(times) - min(times))


def max_spanning_tree_weight(nrows, slots_by_link, ratio):
    edges = {}
    for slots in slots_by_link.values():
        for i, si in enumerate(slots):
            for sj in slots[i + 1:]:
                ri, ti = si
                rj, tj = sj
                if ri == rj:
                    continue
                pair = tuple(sorted((ri, rj)))
                weight = ratio ** abs(ti - tj)
                edges[pair] = max(edges.get(pair, Fraction(0)), weight)

    parent = list(range(nrows))
    total = Fraction(1)
    chosen = 0
    for (a, b), weight in sorted(edges.items(), key=lambda item: item[1], reverse=True):
        if dsu_find(parent, a) != dsu_find(parent, b):
            dsu_union(parent, a, b)
            total *= weight
            chosen += 1
            if chosen == nrows - 1:
                return total
    return Fraction(0)


def check_fixture(name, nrows, slots_by_link, ratio=Fraction(1, 2)):
    links = sorted(slots_by_link)
    local_partitions = []
    for link in links:
        slots = tuple(slots_by_link[link])
        local_partitions.append(canonical_partitions(slots))

    row_max_tree = max_spanning_tree_weight(nrows, slots_by_link, ratio)
    if row_max_tree == 0:
        raise AssertionError(f"{name}: fixture row graph is disconnected")

    checked = 0
    connected = 0
    for choice in product(*local_partitions):
        checked += 1
        if not is_connected_rows(nrows, choice):
            continue
        connected += 1
        local_weight = Fraction(1)
        for parts in choice:
            for block in parts:
                local_weight *= block_max_tree_weight(block, ratio)
        if local_weight > row_max_tree:
            raise AssertionError(
                f"{name}: local slot-tree product exceeds row maximum tree: "
                f"{local_weight} > {row_max_tree}; partition={choice}"
            )
    if connected == 0:
        raise AssertionError(f"{name}: no connected LS slot partitions found")
    print(
        f"PASS {name}: {checked} local partition combinations, "
        f"{connected} connected, all tree weights dominated"
    )


def bell_numbers(n):
    bell = [1]
    for k in range(1, n + 1):
        bell.append(sum(
            __import__("math").comb(k - 1, j) * bell[j]
            for j in range(k)
        ))
    return bell


def check_local_partition_envelope():
    bell = bell_numbers(6)
    assert bell == [1, 1, 2, 5, 15, 52, 203]
    # Directly enumerate the exact local LS coefficient:
    # K_q = sum_{pi in Pi([q])} prod_{B in pi} (|B|-1)! = q!.
    for q in range(1, 7):
        enumerated = sum(
            __import__("math").prod(factorial(len(block) - 1) for block in part)
            for part in canonical_partitions(range(q))
        )
        assert enumerated == factorial(q)
    # Exact integer form of (q!)^(1/q) <= (6!)^(1/6).
    for q in range(1, 7):
        assert factorial(q) ** 6 <= factorial(6) ** q
    # Verify the per-link factorization envelope for several port profiles.
    for profile in ([6, 6, 2], [4, 3, 3, 2], [5, 5, 4], [2, 2, 2, 2, 2, 2]):
        lhs = 1
        total_slots = 0
        for q in profile:
            lhs *= factorial(q)
            total_slots += q
        # Avoid floating-point roots: lhs <= (6!)^(total_slots/6).
        assert lhs ** 6 <= factorial(6) ** total_slots
    print("PASS Bell(6)=203; exact K_q=q! for q<=6; exponential local partition envelope")


def main():
    # Interlaced ports, including repeated link labels within a row.
    check_fixture(
        "interlaced-cycle",
        4,
        {
            "a": [(0, 0), (1, 4), (2, 1), (3, 5)],
            "b": [(0, 6), (2, 2)],
            "c": [(1, 0), (3, 7)],
        },
    )
    check_fixture(
        "two-overlap-links-between-row-pairs",
        4,
        {
            "a": [(0, 0), (1, 3), (2, 1)],
            "b": [(0, 5), (1, 2), (3, 6)],
            "c": [(2, 4), (3, 0)],
        },
    )
    check_fixture(
        "six-port-hyperedge-with-tail",
        6,
        {
            "a": [(0, 0), (1, 3), (2, 1), (3, 5), (4, 2), (5, 7)],
            "b": [(2, 8), (5, 4)],
        },
    )
    check_local_partition_envelope()
    print("LIMIT: finite combinatorial regression only; no SU(2) analytic or KP verification")


if __name__ == "__main__":
    main()
