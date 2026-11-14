#!/usr/bin/env python3
"""Exact finite checks of the link-coloured LS hypergraph identity.

The examples use independent symmetric Rademacher link variables and
same-time elementary factors Y_{i,e}=U_e.  All arithmetic is rational.
"""
from fractions import Fraction
from functools import lru_cache
from itertools import product
from math import prod


def set_partitions(items):
    items = tuple(items)
    if not items:
        yield ()
        return
    first, rest = items[0], items[1:]
    for partition in set_partitions(rest):
        yield ((first,),) + partition
        for j in range(len(partition)):
            yield partition[:j] + ((first,) + partition[j],) + partition[j + 1:]


@lru_cache(None)
def rademacher_cumulant(n):
    """Joint cumulant of n copies of one symmetric Rademacher variable."""
    if n == 0:
        raise ValueError("cumulant order must be positive")
    moment = Fraction(1 if n % 2 == 0 else 0)
    total = Fraction(0)
    for partition in set_partitions(tuple(range(n))):
        if len(partition) == 1:
            continue
        term = Fraction(1)
        for block in partition:
            term *= rademacher_cumulant(len(block))
        total += term
    return moment - total


def connected(vertex_count, hyperedges):
    if vertex_count <= 1:
        return True
    reached = {0}
    changed = True
    while changed:
        changed = False
        for edge in hyperedges:
            if reached.intersection(edge) and not set(edge).issubset(reached):
                reached.update(edge)
                changed = True
    return len(reached) == vertex_count


def hypergraph_ls(supports):
    """RHS of (H), with each link an independent Rademacher path."""
    row_count = len(supports)
    links = sorted(set().union(*map(set, supports)))
    incidence = {
        e: tuple(i for i, support in enumerate(supports) if e in support)
        for e in links
    }
    choices = [list(set_partitions(incidence[e])) for e in links]
    total = Fraction(0)

    def visit(k, edges, weight):
        nonlocal total
        if k == len(links):
            if connected(row_count, edges):
                total += weight
            return
        e = links[k]
        for partition in choices[k]:
            new_edges = edges + [tuple(block) for block in partition if len(block) > 1]
            new_weight = weight
            for block in partition:
                new_weight *= rademacher_cumulant(len(block))
            visit(k + 1, new_edges, new_weight)

    visit(0, [], Fraction(1))
    return total


def direct_product_cumulant(supports):
    """Direct joint cumulant of row products by exact state enumeration."""
    row_count = len(supports)
    links = sorted(set().union(*map(set, supports)))
    states = list(product((-1, 1), repeat=len(links)))
    link_index = {e: j for j, e in enumerate(links)}
    rows = []
    for support in supports:
        values = []
        for state in states:
            value = 1
            for e in support:
                value *= state[link_index[e]]
            values.append(Fraction(value))
        rows.append(values)

    @lru_cache(None)
    def joint_cumulant(indices):
        n = len(indices)
        moment = sum(
            (prod(rows[i][s] for i in indices) for s in range(len(states))),
            Fraction(0),
        ) / len(states)
        total = Fraction(0)
        for partition in set_partitions(tuple(range(n))):
            if len(partition) == 1:
                continue
            term = Fraction(1)
            for block in partition:
                subindices = tuple(indices[j] for j in block)
                term *= joint_cumulant(subindices)
            total += term
        return moment - total

    return joint_cumulant(tuple(range(row_count)))


def perfect_matchings(items):
    """Generate perfect matchings of an even-sized tuple."""
    items = tuple(items)
    if not items:
        yield ()
        return
    first = items[0]
    for j in range(1, len(items)):
        pair = (first, items[j])
        rest = items[1:j] + items[j + 1:]
        for matching in perfect_matchings(rest):
            yield (pair,) + matching


def check_eight_link_cancellation_witness():
    """Verify the exact cumulant and a huge positive subfamily of LS terms."""
    rows = tuple(range(8))
    matchings = list(perfect_matchings(rows))
    assert len(matchings) == 105

    # Alternating matchings form the cycle 0-1-2-3-4-5-6-7-0.
    m0 = tuple((i, i + 1) for i in (0, 2, 4, 6))
    m1 = ((1, 2), (3, 4), (5, 6), (7, 0))
    assert connected(8, list(m0) + list(m1))

    # For each of the other six link colours, any perfect matching is allowed.
    positive_connected_summands = len(matchings) ** 6
    exact_product_cumulant = rademacher_cumulant(8)
    assert positive_connected_summands == 105**6
    assert exact_product_cumulant == -272
    print(
        "PASS: eight-link witness has at least "
        f"{positive_connected_summands} connected +1 LS summands, "
        f"while the exact product cumulant is {exact_product_cumulant}"
    )


def check(name, supports, expected):
    lhs = direct_product_cumulant(supports)
    rhs = hypergraph_ls(supports)
    assert lhs == rhs == Fraction(expected), (name, lhs, rhs, expected)
    print(f"PASS: {name}: direct cumulant = hypergraph sum = {lhs}")


def main():
    check("two rows sharing two independent links", [(0, 1), (0, 1)], 1)
    check("three-row support path", [(0,), (0, 1), (1,)], 1)
    check("four-row support path", [(0,), (0, 1), (1, 2), (2,)], 1)
    check("three rows sharing one link", [(0,), (0,), (0,)], 0)
    check_eight_link_cancellation_witness()
    print("LIMIT: these exact finite checks do not prove an all-orders growth bound")


if __name__ == "__main__":
    main()
