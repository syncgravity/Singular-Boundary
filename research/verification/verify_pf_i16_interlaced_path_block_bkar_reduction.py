#!/usr/bin/env python3
"""Exact regressions for the interlaced path-block BKAR reduction.

This checks only finite combinatorics and one exact Markov-chain derivative
obstruction. It does NOT prove the connected-log derivative estimate.
"""
from fractions import Fraction
from itertools import combinations, product


def is_tree(vertex_count, edges):
    parent = list(range(vertex_count))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for u, v, _weight in edges:
        if u == v:
            return False
        ru, rv = find(u), find(v)
        if ru == rv:
            return False
        parent[ru] = rv
    return len(edges) == vertex_count - 1 and len({find(i) for i in range(vertex_count)}) == 1


def row_trees(q):
    pairs = list(combinations(range(q), 2))
    for chosen in combinations(pairs, q - 1):
        if is_tree(q, [(u, v, Fraction(1)) for u, v in chosen]):
            yield chosen


def check_multigraph_tree_weight_identity(labels, q):
    weights = [Fraction(1, k + 2) for k in range(len(labels) - 1)]
    temporal_edges = [
        (labels[k], labels[k + 1], weights[k])
        for k in range(len(labels) - 1)
        if labels[k] != labels[k + 1]
    ]
    row_sums = {
        (i, j): sum(
            (w for u, v, w in temporal_edges if {u, v} == {i, j}),
            Fraction(0),
        )
        for i, j in combinations(range(q), 2)
    }

    lhs = Fraction(0)
    for chosen in combinations(temporal_edges, q - 1):
        if is_tree(q, chosen):
            term = Fraction(1)
            for _u, _v, w in chosen:
                term *= w
            lhs += term

    rhs = Fraction(0)
    for tree in row_trees(q):
        term = Fraction(1)
        for edge in tree:
            term *= row_sums[edge]
        rhs += term

    assert lhs == rhs, (labels, lhs, rhs)


def exact_path_moments(rhos):
    """Enumerate a stationary symmetric binary chain at five port times."""
    total = {
        "A": Fraction(0),
        "B": Fraction(0),
        "C": Fraction(0),
        "AB": Fraction(0),
        "AC": Fraction(0),
        "BC": Fraction(0),
        "ABC": Fraction(0),
    }
    for states in product((-1, 1), repeat=5):
        probability = Fraction(1, 2)
        for k, rho_k in enumerate(rhos):
            probability *= (1 + rho_k * states[k] * states[k + 1]) / 2
        a = states[0] * states[3]
        b = states[1]
        c = states[2] + states[4]
        values = {
            "A": a,
            "B": b,
            "C": c,
            "AB": a * b,
            "AC": a * c,
            "BC": b * c,
            "ABC": a * b * c,
        }
        for key, value in values.items():
            total[key] += probability * value
    return total


def check_derivative_collapse_obstruction():
    # Port labels A,B,C,A,C: A={0,3}, B={1}, C={2,4}.
    # All five ports are used; hulls of A and C overlap.
    rho = Fraction(1, 2)
    for x, y, z in [
        (Fraction(1, 3), Fraction(2, 5), Fraction(1, 4)),
        (Fraction(2, 3), Fraction(1, 2), Fraction(3, 7)),
        (Fraction(3, 4), Fraction(2, 3), Fraction(1, 5)),
    ]:
        r1, r2, r3, r4 = rho * x, rho * y, rho * z, rho * z
        moments = exact_path_moments((r1, r2, r3, r4))
        expected = {
            "A": r1 * r2 * r3,
            "B": Fraction(0),
            "C": Fraction(0),
            "AB": Fraction(0),
            "AC": Fraction(0),
            "BC": r2 + r2 * r3 * r4,
            "ABC": r1 * r3 + r1 * r4,
        }
        assert moments == expected, (moments, expected)

        kappa = (
            moments["ABC"]
            - moments["AB"] * moments["C"]
            - moments["AC"] * moments["B"]
            - moments["BC"] * moments["A"]
            + 2 * moments["A"] * moments["B"] * moments["C"]
        )
        expected_kappa = rho**2 * x * z * (
            2 - rho**2 * y**2 - rho**4 * y**2 * z**2
        )
        assert kappa == expected_kappa

        # Exact mixed derivatives with respect to x=lambda_AB and
        # z=lambda_AC; y=lambda_BC is held fixed.
        d_kappa = rho**2 * (
            2 - rho**2 * y**2 - 3 * rho**4 * y**2 * z**2
        )
        d_full_moment = 2 * rho**2
        difference = -rho**4 * y**2 * (1 + 3 * rho**2 * z**2)
        assert d_kappa - d_full_moment == difference
        assert difference != 0


def main():
    fixtures = [
        (2, [0, 1, 0, 1, 0]),
        (3, [0, 1, 0, 2, 1, 2]),
        (3, [0, 1, 2, 0, 2, 1, 0]),
        (4, [0, 1, 2, 3, 0, 2, 1, 3]),
        (5, [0, 1, 2, 3, 4, 0, 2, 4, 1, 3]),
    ]
    for q, labels in fixtures:
        check_multigraph_tree_weight_identity(labels, q)
    check_derivative_collapse_obstruction()
    print("PASS interlaced temporal-tree weight identity and exact derivative-collapse obstruction")


if __name__ == "__main__":
    main()
