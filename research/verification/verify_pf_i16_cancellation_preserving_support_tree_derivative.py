#!/usr/bin/env python3
"""Exact finite checks for the cancellation-preserving support-tree derivative.

Part I checks the algebraic identity
  d_T cumulant(M_B) = d_T M_[R]
whenever M_B depends only on edge variables whose endpoints both lie in B.

Part II checks the link-chain operator insertion bound on exact two-state
stationary Markov chains with rational transition parameters.
"""
from fractions import Fraction
from itertools import combinations, product
from math import prod

ZERO = Fraction(0)
ONE = Fraction(1)


def partitions(items):
    items = tuple(items)
    if not items:
        yield ()
        return
    first, *rest = items
    for tail in partitions(rest):
        yield ((first,),) + tail
        for k in range(len(tail)):
            yield tail[:k] + (tuple(sorted(tail[k] + (first,))),) + tail[k + 1:]


def trees(n):
    """All labeled trees via Prüfer sequences."""
    if n == 2:
        yield {(0, 1)}
        return
    for seq in product(range(n), repeat=n - 2):
        degree = [1] * n
        for v in seq:
            degree[v] += 1
        edges = set()
        for v in seq:
            leaf = next(i for i, d in enumerate(degree) if d == 1)
            edges.add(tuple(sorted((leaf, v))))
            degree[leaf] -= 1
            degree[v] -= 1
        left = [i for i, d in enumerate(degree) if d == 1]
        edges.add(tuple(sorted(left)))
        yield edges


# Sparse multivariate polynomial: exponent tuple -> Fraction coefficient.
def p_add(a, b):
    out = dict(a)
    for mon, c in b.items():
        out[mon] = out.get(mon, ZERO) + c
        if out[mon] == 0:
            del out[mon]
    return out


def p_mul(a, b):
    out = {}
    for ma, ca in a.items():
        for mb, cb in b.items():
            mon = tuple(x + y for x, y in zip(ma, mb))
            out[mon] = out.get(mon, ZERO) + ca * cb
    return {m: c for m, c in out.items() if c}


def p_derivative(poly, variable):
    out = {}
    for mon, c in poly.items():
        if mon[variable]:
            new = list(mon)
            factor = new[variable]
            new[variable] -= 1
            key = tuple(new)
            out[key] = out.get(key, ZERO) + factor * c
    return {m: c for m, c in out.items() if c}


def cumulant_polynomial(n, moments, edge_index):
    out = {}
    for pi in partitions(range(n)):
        k = len(pi)
        coefficient = Fraction((-1) ** (k - 1) * prod(range(1, k)))
        term = {tuple(0 for _ in edge_index): coefficient}
        for block in pi:
            term = p_mul(term, moments[frozenset(block)])
        out = p_add(out, term)
    return out


def verify_partition_cancellation():
    checked = 0
    for n in range(2, 6):
        edges = list(combinations(range(n), 2))
        edge_index = {edge: k for k, edge in enumerate(edges)}
        zero = tuple(0 for _ in edges)
        moments = {}
        # Give each block moment a nontrivial deterministic polynomial,
        # using only variables whose two endpoints lie inside that block.
        for mask in range(1, 1 << n):
            block = frozenset(i for i in range(n) if mask >> i & 1)
            poly = {zero: Fraction(2 + len(block))}
            internal = [edge_index[e] for e in edges if set(e) <= block]
            for j, v in enumerate(internal):
                mon = list(zero)
                mon[v] = 1
                poly[tuple(mon)] = Fraction((j + 1) * (len(block) + 1), 7)
            for j, v in enumerate(internal):
                for w in internal[j + 1:]:
                    mon = list(zero)
                    mon[v] = mon[w] = 1
                    poly[tuple(mon)] = Fraction((j + 2) * (len(block) + 2), 11)
            moments[block] = poly
        for tree in trees(n):
            derivative_vars = [edge_index[e] for e in sorted(tree)]
            lhs = cumulant_polynomial(n, moments, edge_index)
            for v in derivative_vars:
                lhs = p_derivative(lhs, v)
            rhs = moments[frozenset(range(n))]
            for v in derivative_vars:
                rhs = p_derivative(rhs, v)
            assert lhs == rhs, (n, tree, lhs, rhs)
            checked += 1
    print(f"PASS exact partition-cancellation identity for {checked} labeled trees (R=2..5)")


def mat_mul(a, b):
    return [
        [sum((a[i][k] * b[k][j] for k in range(2)), ZERO) for j in range(2)]
        for i in range(2)
    ]


def mat_vec(a, v):
    return [sum((a[i][k] * v[k] for k in range(2)), ZERO) for i in range(2)]


def chain_expectation(functions, gaps, lambdas, differentiated):
    """Exact stationary expectation with Q inserted on differentiated gaps."""
    rho = [Fraction(1, 2) ** d for d in gaps]
    pi = [[Fraction(1, 2), Fraction(1, 2)],
          [Fraction(1, 2), Fraction(1, 2)]]
    q_ops = [
        [[r / 2, -r / 2], [-r / 2, r / 2]]
        for r in rho
    ]
    k_ops = []
    for r, lam in zip(rho, lambdas):
        p = [[(1 + r) / 2, (1 - r) / 2],
             [(1 - r) / 2, (1 + r) / 2]]
        k_ops.append([
            [(1 - lam) * pi[i][j] + lam * p[i][j] for j in range(2)]
            for i in range(2)
        ])
    ops = [q_ops[i] if i in differentiated else k_ops[i] for i in range(len(gaps))]
    # Row-vector stationary law, then diagonal multipliers and transitions.
    row = [Fraction(1, 2) * functions[0][0], Fraction(1, 2) * functions[0][1]]
    for i, op in enumerate(ops):
        row = [row[0] * op[0][j] + row[1] * op[1][j] for j in range(2)]
        row = [row[j] * functions[i + 1][j] for j in range(2)]
    return sum(row, ZERO)


def verify_operator_insertion_bound():
    checked = 0
    for n_ports in range(2, 6):
        gaps = tuple(range(1, n_ports))
        for signs in product((-1, 1), repeat=n_ports):
            functions = tuple((Fraction(s), Fraction(-s)) for s in signs)
            for lambdas in product((Fraction(0), Fraction(1, 2), ONE), repeat=n_ports - 1):
                for mask in range(1 << (n_ports - 1)):
                    differentiated = {j for j in range(n_ports - 1) if mask >> j & 1}
                    value = abs(chain_expectation(functions, gaps, lambdas, differentiated))
                    bound = prod((Fraction(1, 2) ** gaps[j] for j in differentiated), start=ONE)
                    assert value <= bound, (n_ports, signs, lambdas, differentiated, value, bound)
                    checked += 1
    print(f"PASS exact L2 insertion estimate for {checked} two-state chain cases")


def main():
    verify_partition_cancellation()
    verify_operator_insertion_bound()


if __name__ == "__main__":
    main()
