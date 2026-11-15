#!/usr/bin/env python3
"""Reproduce a rational 3-state counterexample to the discrete-time multi-cut HGR bound.

The transition matrix and stationary law are rational. SVD is used only to evaluate
the two finite-dimensional maximal-correlation norms numerically.
"""
from fractions import Fraction
import numpy as np


def normalized_second_singular_value(joint):
    px = joint.sum(axis=1)
    py = joint.sum(axis=0)
    normalized = joint / np.sqrt(np.outer(px, py))
    singular = np.linalg.svd(normalized, compute_uv=False)
    return float(singular[1])


def main():
    Pq = [
        [Fraction(130, 1000), Fraction(539, 1000), Fraction(331, 1000)],
        [Fraction(52, 1000), Fraction(947, 1000), Fraction(1, 1000)],
        [Fraction(956, 1000), Fraction(36, 1000), Fraction(8, 1000)],
    ]
    piq = [Fraction(26270, 308613),
           Fraction(273302, 308613),
           Fraction(9041, 308613)]

    assert all(sum(row) == 1 for row in Pq)
    assert all(sum(piq[i] * Pq[i][j] for i in range(3)) == piq[j]
               for j in range(3))

    P = np.array([[float(x) for x in row] for row in Pq])
    pi = np.array([float(x) for x in piq])
    s = np.sqrt(pi)
    centered = (s[:, None] * P) / s[None, :] - np.outer(s, s)
    q = float(np.linalg.svd(centered, compute_uv=False)[0])

    joint = np.zeros((9, 3), dtype=float)
    for a in range(3):
        for y in range(3):
            for b in range(3):
                joint[3 * a + b, y] = pi[a] * P[a, y] * P[y, b]
    rho = normalized_second_singular_value(joint)
    bound = 2.0 * q / (1.0 + q * q)

    assert rho > bound + 1e-3, (q, rho, bound)
    print("PASS: exact rational stationarity and row-stochasticity")
    print(f"one-step centered-L2 contraction q={q:.12f}")
    print(f"rho_max((X0,X2),X1)={rho:.12f}")
    print(f"proposed two-cut bound={bound:.12f}")
    print(f"strict violation={rho - bound:.12f}")
    print("SCOPE: refutes the discrete-time kernel statement only;")
    print("does not refute the continuous-time Markov-semigroup version.")


if __name__ == "__main__":
    main()
