#!/usr/bin/env python3
"""Exact rational verifier for the centered-edge connected-subgraph identity."""
from fractions import Fraction
from itertools import combinations, product
from math import factorial


def partitions(items):
    items = tuple(items)
    if not items:
        yield ()
        return
    first, *rest = items
    for p in partitions(rest):
        yield ((first,),) + p
        for k in range(len(p)):
            yield p[:k] + (p[k] + (first,),) + p[k + 1:]


def cumulant(indices, moment):
    total = Fraction(0)
    for part in partitions(tuple(indices)):
        term = Fraction((-1) ** (len(part) - 1) * factorial(len(part) - 1))
        for block in part:
            term *= moment(frozenset(block))
        total += term
    return total


def connected(n, edges, active):
    adjacency = [set() for _ in range(n)]
    for k in active:
        i, j = edges[k]
        adjacency[i].add(j)
        adjacency[j].add(i)
    seen = {0}
    stack = [0]
    while stack:
        i = stack.pop()
        for j in adjacency[i] - seen:
            seen.add(j)
            stack.append(j)
    return len(seen) == n


def edge_law(k):
    # P(x,y)=1/4(1+a*x+b*y+c*x*y), x,y in {-1,+1}.
    a = Fraction(1, 5 + k)
    b = Fraction(-1, 7 + k)
    c = Fraction(1, 6 + k)
    law = {}
    for x, y in product((-1, 1), repeat=2):
        law[(x, y)] = (1 + a*x + b*y + c*x*y) / 4
        assert law[(x, y)] > 0
    mu_i = sum(p*x for (x, y), p in law.items())
    mu_j = sum(p*y for (x, y), p in law.items())
    exy = sum(p*x*y for (x, y), p in law.items())
    cov = exy - mu_i*mu_j
    return law, mu_i, mu_j, cov


def check(n, edges, tag):
    laws = [edge_law(k + 1) for k in range(len(edges))]
    edge_data = [(law, mi, mj, cov) for law, mi, mj, cov in laws]

    def moment(rows):
        value = Fraction(1)
        for (i, j), (_, mi, mj, cov) in zip(edges, edge_data):
            if i in rows and j in rows:
                value *= mi*mj + cov
            elif i in rows:
                value *= mi
            elif j in rows:
                value *= mj
        return value

    lhs = cumulant(range(n), moment)
    rhs = Fraction(0)
    for mask in range(1 << len(edges)):
        active = [k for k in range(len(edges)) if (mask >> k) & 1]
        if not connected(n, edges, active):
            continue
        term = Fraction(1)
        for k, ((i, j), (_, mi, mj, cov)) in enumerate(zip(edges, edge_data)):
            term *= cov if k in active else mi*mj
        rhs += term
    assert lhs == rhs, (tag, lhs, rhs)
    print(f"PASS {tag}: n={n}, links={len(edges)}, exact rational identity")


def main():
    fixtures = [
        (4, [(0,1),(1,2),(2,3)], "path"),
        (4, [(0,1),(1,2),(2,3),(3,0)], "four-cycle"),
        (3, [(0,1),(1,2),(2,0)], "triangle"),
        (5, [(0,1),(1,2),(2,3),(3,4),(4,0)], "five-cycle"),
        (4, [(0,1),(0,2),(0,3)], "star"),
        (4, [(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)], "K4"),
        (3, [(0,1),(0,1),(1,2),(2,0)], "parallel-edge-cycle"),
        (4, [(0,1),(0,1),(1,2),(2,3),(3,0)], "parallel-square"),
        (6, [(0,1),(1,2),(2,0),(2,3),(3,4),(4,5),(5,2)], "two-cycles-glued"),
    ]
    for fixture in fixtures:
        check(*fixture)
    print("LIMIT: exact pair-incidence algebra only; higher-row hyperedges remain open")


if __name__ == "__main__":
    main()
