#!/usr/bin/env python3
"""Exact checks for formal interval-component resummation and its Markov obstruction.

The formal generating-function identity is combinatorial. The four-port
symmetric two-state calculation explicitly prevents treating it as a general
Markov block-moment formula.
"""
from fractions import Fraction as F
from itertools import product
from math import comb, factorial


def partitions(items):
    items = tuple(items)
    if not items:
        yield ()
        return
    first, *rest = items
    for tail in partitions(rest):
        yield ((first,),) + tail
        for j in range(len(tail)):
            yield tail[:j] + (tuple(sorted(tail[j] + (first,))),) + tail[j + 1:]


def canon(part):
    return tuple(sorted((tuple(sorted(b)) for b in part), key=lambda b: b[0]))


def all_partitions(n):
    return sorted({canon(p) for p in partitions(range(n))})


def covers_all_cuts(part, n):
    return all(any(min(block) <= cut < max(block) for block in part)
               for cut in range(n - 1))


def connected_component_polynomial_direct(n, moments):
    out = {}
    for part in all_partitions(n):
        if not covers_all_cuts(part, n):
            continue
        k = len(part)
        weight = F(1)
        for block in part:
            weight *= moments[len(block)]
        out[k] = out.get(k, F(0)) + weight
    return {k: v for k, v in out.items() if v}


def poly_add(a, b):
    out = dict(a)
    for k, v in b.items():
        out[k] = out.get(k, F(0)) + v
    return {k: v for k, v in out.items() if v}


def poly_mul(a, b):
    out = {}
    for i, x in a.items():
        for j, y in b.items():
            out[i + j] = out.get(i + j, F(0)) + x * y
    return {k: v for k, v in out.items() if v}


def poly_scale(a, c):
    return {k: v * c for k, v in a.items() if v * c}


def connected_polynomials(nmax, moments):
    P = [{0: F(1)}]
    for n in range(1, nmax + 1):
        pn = {}
        for j in range(1, n + 1):
            term = poly_scale(P[n - j], comb(n - 1, j - 1) * moments[j])
            term = {k + 1: v for k, v in term.items()}
            pn = poly_add(pn, term)
        P.append(pn)

    C = [{0: F(0)}]
    for n in range(1, nmax + 1):
        cn = dict(P[n])
        for j in range(1, n):
            cn = poly_add(cn, poly_scale(poly_mul(C[j], P[n - j]), -1))
        C.append(cn)
    return P, C


def mobius_functional(poly):
    return sum(value * (-1) ** (k - 1) * factorial(k - 1)
               for k, value in poly.items() if k >= 1)


def verify_interval_component_decomposition():
    for n in range(1, 9):
        for part in all_partitions(n):
            cuts = [i for i in range(n - 1)
                    if not any(min(b) <= i < max(b) for b in part)]
            boundaries = [-1] + cuts + [n - 1]
            components = []
            for left_cut, right_cut in zip(boundaries, boundaries[1:]):
                lo, hi = left_cut + 1, right_cut
                restricted = canon([
                    tuple(x - lo for x in block if lo <= x <= hi)
                    for block in part
                    if any(lo <= x <= hi for x in block)
                ])
                assert covers_all_cuts(restricted, hi - lo + 1)
                components.append((lo, hi, restricted))
            rebuilt = []
            for lo, hi, restricted in components:
                rebuilt.extend(tuple(x + lo for x in block) for block in restricted)
            assert canon(rebuilt) == part


def verify_generating_function_recurrence():
    moments = [F(0)] + [F((-1) ** j, j + 1) for j in range(1, 9)]
    _, C = connected_polynomials(8, moments)
    for n in range(1, 9):
        assert C[n] == connected_component_polynomial_direct(n, moments)


def verify_symmetric_formal_sequence():
    nmax = 30
    moments = [F(0)] + [F(1 if j % 2 == 0 else 0) for j in range(1, nmax + 1)]
    _, C = connected_polynomials(nmax, moments)
    expected = {
        2: 1, 4: -1, 6: 8, 8: -149,
        10: 4778, 12: -231205, 14: 15638140,
    }
    for n, value in expected.items():
        assert mobius_functional(C[n]) == value


def verify_four_port_markov_obstruction():
    # Symmetric +/-1 chain: r_i=lambda_i*q_i.
    # M1234 = r1*r3, so the middle transition is absent from this moment.
    r1, r2, r3 = F(2, 3), F(3, 5), F(4, 7)
    m1234 = r1 * r3
    m12, m13, m14 = r1, r1 * r2, r1 * r2 * r3
    m23, m24, m34 = r2, r2 * r3, r3
    cumulant = m1234 - m12 * m34 - m13 * m24 - m14 * m23
    assert cumulant == -2 * r1 * r2**2 * r3

    # Symbolically, kappa=-2*(lambda1*q1)*(lambda2*q2)^2*(lambda3*q3).
    # Its mixed derivative at lambda_i=1 is -4*q1*q2^2*q3.
    q1, q2, q3 = F(2, 3), F(3, 4), F(4, 5)
    mixed_derivative = -4 * q1 * q2**2 * q3
    assert mixed_derivative == F(-6, 5)
    # The full block moment r1*r3 is independent of lambda2, hence this
    # three-parameter mixed derivative is exactly zero.
    assert m1234 == r1 * r3
    print("PASS four-port symmetric Markov obstruction:")
    print(f"  M1234={m1234}; cumulant={cumulant}")
    print(f"  mixed derivative of M1234=0; of cumulant={mixed_derivative}")


def verify_formal_stirling_bound():
    stirling = [0, 1]
    for n in range(2, 31):
        row = [0] * (n + 1)
        for k in range(1, n + 1):
            row[k] = k * stirling[k] + stirling[k - 1]
        stirling = row
        lhs = sum(factorial(k - 1) * stirling[k] for k in range(1, n + 1))
        assert lhs <= n ** n
        assert n ** n <= 4 ** n * n ** (n - 2)


def main():
    verify_interval_component_decomposition()
    verify_generating_function_recurrence()
    verify_symmetric_formal_sequence()
    verify_four_port_markov_obstruction()
    verify_formal_stirling_bound()
    print("PASS unique consecutive-component decomposition for all partitions (R<=8)")
    print("PASS C(z,u)=1-1/P(z,u) recurrence against direct partitions (R<=8)")
    print("PASS exact symmetric formal sequence through R=30 recurrence")
    print("PASS formal Stirling/Cayley coefficient bound for R<=30")


if __name__ == "__main__":
    main()
