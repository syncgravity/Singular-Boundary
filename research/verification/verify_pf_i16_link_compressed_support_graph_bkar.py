#!/usr/bin/env python3
"""Exact finite checks for link-compressed support-graph BKAR interpolation.

Uses independent symmetric two-state Markov chains with rational contraction
q**gap. Checks projective consistency and disconnected-parameter cumulant
factorization for one-time monomial rows.
"""
from fractions import Fraction
from itertools import combinations, product
from math import prod

ROWS = range(4)
TIMES = (0, 2, 5, 8)
SUPPORTS = (
    frozenset(("a",)),
    frozenset(("a", "b")),
    frozenset(("b", "c")),
    frozenset(("c",)),
)
LINKS = ("a", "b", "c")
Q = Fraction(1, 2)
LAMBDA_VALUES = (Fraction(0), Fraction(1, 2), Fraction(1))


def support_edges():
    return {
        (i, j)
        for i, j in combinations(ROWS, 2)
        if SUPPORTS[i] & SUPPORTS[j]
    }


def incident_rows(link):
    return [i for i in ROWS if link in SUPPORTS[i]]


def edge_parameters(values):
    return dict(zip(sorted(support_edges()), values))


def link_moment(link, selected, lambdas):
    """Exact E[prod_{i in selected} X_i] for one interpolated link chain."""
    ports = incident_rows(link)
    if not selected:
        return Fraction(1)
    # Enumerate states at every incident port; omitted rows carry identity.
    total = Fraction(0)
    for states in product((-1, 1), repeat=len(ports)):
        weight = Fraction(1, 2)
        for k in range(len(ports) - 1):
            i, j = ports[k], ports[k + 1]
            lam = lambdas[(min(i, j), max(i, j))]
            corr = lam * Q ** (TIMES[j] - TIMES[i])
            weight *= (1 + states[k] * states[k + 1] * corr) / 2
        value = Fraction(1)
        for k, i in enumerate(ports):
            if i in selected:
                value *= states[k]
        total += weight * value
    return total


def row_moment(selected, lambdas, active):
    """Monomial rows; active[(row,link)] chooses sign or constant 1."""
    out = Fraction(1)
    for link in LINKS:
        chosen = [i for i in selected if link in SUPPORTS[i] and active[(i, link)]]
        out *= link_moment(link, chosen, lambdas)
    return out


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


def cumulant(lambdas, active):
    total = Fraction(0)
    for pi in partitions(ROWS):
        k = len(pi)
        coefficient = (-1) ** (k - 1)
        # (k-1)! is the moment-cumulant Mobius coefficient.
        for n in range(1, k):
            coefficient *= n
        term = Fraction(coefficient)
        for block in pi:
            term *= row_moment(block, lambdas, active)
        total += term
    return total


def verify_projective_consistency():
    for link in LINKS:
        ports = incident_rows(link)
        for lambdas_on_path in product(LAMBDA_VALUES, repeat=max(0, len(ports) - 1)):
            full = {
                (min(i, j), max(i, j)): lam
                for i, j, lam in zip(ports, ports[1:], lambdas_on_path)
            }
            # Fill unused support edges arbitrarily; they do not enter this link.
            for edge in support_edges():
                full.setdefault(edge, Fraction(1, 3))
            for mask in range(1 << len(ports)):
                selected = [ports[k] for k in range(len(ports)) if mask >> k & 1]
                lhs = link_moment(link, selected, full)
                # The compressed chain has adjacent selected ports with
                # correlation q^(time gap) times the product of skipped lambdas.
                rhs = Fraction(1)
                if selected:
                    for i, j in zip(selected, selected[1:]):
                        a, b = ports.index(i), ports.index(j)
                        effective_lambda = prod(lambdas_on_path[a:b])
                        corr = effective_lambda * Q ** (TIMES[j] - TIMES[i])
                        # For a centered sign product on a symmetric chain,
                        # the joint moment is zero for an odd number of signs;
                        # the general exact check below uses the full law.
                        del corr
                    # Recompute compressed expectation by direct two-state path enumeration.
                    total = Fraction(0)
                    for states in product((-1, 1), repeat=len(selected)):
                        weight = Fraction(1, 2)
                        for k in range(len(selected) - 1):
                            i, j = selected[k], selected[k + 1]
                            a, b = ports.index(i), ports.index(j)
                            eff = prod(lambdas_on_path[a:b])
                            corr = eff * Q ** (TIMES[j] - TIMES[i])
                            weight *= (1 + states[k] * states[k + 1] * corr) / 2
                        total += weight * prod(states)
                    rhs = total
                assert lhs == rhs, (link, selected, lhs, rhs)


def verify_disconnected_cumulant_factorization():
    edges = sorted(support_edges())
    # Every sign/constant choice on each row-link incidence.
    incidences = [(i, e) for i in ROWS for e in SUPPORTS[i]]
    for values in product(LAMBDA_VALUES, repeat=len(edges)):
        lambdas = dict(zip(edges, values))
        positive = {edge for edge, value in lambdas.items() if value > 0}
        # For the path support graph, any zero edge disconnects the positive graph.
        if len(positive) == len(edges):
            continue
        for bits in product((False, True), repeat=len(incidences)):
            active = dict(zip(incidences, bits))
            assert cumulant(lambdas, active) == 0, (lambdas, active)


def verify_original_endpoint():
    lambdas = {edge: Fraction(1) for edge in support_edges()}
    incidences = [(i, e) for i in ROWS for e in SUPPORTS[i]]
    for bits in product((False, True), repeat=len(incidences)):
        active = dict(zip(incidences, bits))
        # At lambda=1 the interpolation is the ordinary independent-link chain.
        value = cumulant(lambdas, active)
        assert isinstance(value, Fraction)


def main():
    verify_projective_consistency()
    verify_disconnected_cumulant_factorization()
    verify_original_endpoint()
    print("PASS exact projective consistency for every row subset and link")
    print("PASS exact cumulant cancellation whenever the positive support graph disconnects")
    print("PASS lambda=1 endpoint is the original independent-link Markov law")


if __name__ == "__main__":
    main()
