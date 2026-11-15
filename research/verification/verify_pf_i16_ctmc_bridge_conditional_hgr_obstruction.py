#!/usr/bin/env python3
"""Finite CTMC stress test for conditional bridge HGR vs unconditioned L2 gaps.

Uses a fixed irreducible rational 3-state generator and a NumPy scaling/squaring
matrix exponential. This is a numerical counterexample to the stronger claim
that each endpoint-conditioned bridge HGR is bounded by the corresponding
unconditioned semigroup L2 norm. It does NOT refute the weaker tanh two-cut
composition bound.
"""
from __future__ import annotations

import math
import numpy as np


def expm_taylor(a: np.ndarray) -> np.ndarray:
    """Small-matrix exponential by scaling, Taylor expansion, and squaring."""
    norm = float(np.linalg.norm(a, ord=np.inf))
    scale = max(0, int(math.ceil(math.log2(norm / 0.5)))) if norm > 0.5 else 0
    b = a / (2**scale)
    term = np.eye(a.shape[0])
    total = term.copy()
    for k in range(1, 81):
        term = term @ b / k
        total += term
        if np.linalg.norm(term, ord=np.inf) < 1e-17:
            break
    for _ in range(scale):
        total = total @ total
    return total


def hgr(joint: np.ndarray) -> float:
    px = joint.sum(axis=1)
    py = joint.sum(axis=0)
    keep_x, keep_y = px > 1e-14, py > 1e-14
    normalized = joint[np.ix_(keep_x, keep_y)] / np.sqrt(
        px[keep_x, None] * py[None, keep_y]
    )
    singular = np.linalg.svd(normalized, compute_uv=False)
    return float(singular[1]) if len(singular) > 1 else 0.0


def l2_contraction(p: np.ndarray, pi: np.ndarray) -> float:
    normalized = np.sqrt(pi[:, None]) * p / np.sqrt(pi[None, :])
    return float(np.linalg.svd(normalized, compute_uv=False)[1])


def main() -> None:
    # Exact rational generator entries, with denominator 10^6.
    qgen = np.array(
        [
            [-187844, 167637, 20207],
            [45820559, -45891980, 71421],
            [7805983, 12454510, -20260493],
        ],
        dtype=np.float64,
    ) / 1_000_000.0
    pi = np.array(
        [
            464452312993715 / 466746007289039,
            3648076548611 / 933492014578078,
            939312042037 / 933492014578078,
        ],
        dtype=np.float64,
    )
    t1, t2 = 0.064, 0.078

    assert np.max(np.abs(qgen.sum(axis=1))) < 1e-13
    off_diagonal = qgen.copy()
    np.fill_diagonal(off_diagonal, np.inf)
    assert np.min(off_diagonal) > 0.0
    assert abs(float(pi.sum()) - 1.0) < 1e-14
    assert np.max(np.abs(pi @ qgen)) < 1e-11

    p1, p2 = expm_taylor(qgen * t1), expm_taylor(qgen * t2)
    for p in (p1, p2):
        assert np.max(np.abs(p.sum(axis=1) - 1.0)) < 1e-12
        assert np.min(p) > 0.0
        assert np.max(np.abs(pi @ p - pi)) < 1e-11

    q1, q2 = l2_contraction(p1, pi), l2_contraction(p2, pi)

    # Subjective bridge correlations: condition on the other endpoint.
    cond_left = []
    cond_right = []
    for z in range(3):
        joint = np.array(
            [[pi[i] * p1[i, j] * p2[j, z] for j in range(3)] for i in range(3)]
        )
        cond_left.append(hgr(joint))
    for x in range(3):
        joint = np.array(
            [[p1[x, j] * p2[j, k] for k in range(3)] for j in range(3)]
        )
        cond_right.append(hgr(joint))
    eps1, eps2 = max(cond_left), max(cond_right)

    # HGR between the middle state and the pair of endpoints.
    joint_pair = np.zeros((9, 3))
    for i in range(3):
        for j in range(3):
            for k in range(3):
                joint_pair[3 * i + k, j] = pi[i] * p1[i, j] * p2[j, k]
    rho_pair = hgr(joint_pair)

    # Stronger but invalid substitution: use unconditioned q_i in N-against-1.
    product_bound = math.sqrt(1.0 - (1.0 - q1**2) * (1.0 - q2**2))
    # Weaker two-cut tanh composition remains unviolated in this example.
    tanh_bound = math.tanh(math.atanh(q1) + math.atanh(q2))

    assert eps1 > q1 + 0.15
    assert eps2 > q2 + 0.15
    assert rho_pair > product_bound + 0.02
    assert rho_pair < tanh_bound - 0.05

    print("PASS: finite CTMC refutes endpoint-conditioned HGR <= unconditioned q")
    print(f"q_t={q1:.12f}; max_z HGR(X0,Xt | XT=z)={eps1:.12f}")
    print(f"q_T-t={q2:.12f}; max_x HGR(XT,Xt | X0=x)={eps2:.12f}")
    print(f"HGR((X0,XT),Xt)={rho_pair:.12f}")
    print(f"sqrt-product bound using q's={product_bound:.12f} [VIOLATED]")
    print(f"tanh two-cut bound using q's={tanh_bound:.12f} [not violated]")
    print("SCOPE: one finite CTMC numerical witness; no general semigroup theorem")


if __name__ == "__main__":
    main()
