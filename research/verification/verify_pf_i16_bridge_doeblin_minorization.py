#!/usr/bin/env python3
"""Finite-state regression for the uniform Markov-bridge Doeblin minorization."""
from __future__ import annotations

import numpy as np


def hgr(joint: np.ndarray) -> float:
    px = joint.sum(axis=1)
    py = joint.sum(axis=0)
    keep_x, keep_y = px > 1e-14, py > 1e-14
    normalized = joint[np.ix_(keep_x, keep_y)] / np.sqrt(
        px[keep_x, None] * py[None, keep_y]
    )
    singular = np.linalg.svd(normalized, compute_uv=False)
    return float(singular[1]) if len(singular) > 1 else 0.0


def main() -> None:
    # Strictly positive stationary Markov kernel; exact rational entries.
    p = np.array(
        [[130, 539, 331], [52, 947, 1], [956, 36, 8]], dtype=np.float64
    ) / 1000.0
    pi = np.array([26270, 273302, 9041], dtype=np.float64) / 308613.0
    assert np.max(np.abs(p.sum(axis=1) - 1.0)) < 1e-14
    assert np.max(np.abs(pi @ p - pi)) < 1e-12
    assert np.min(p) > 0.0

    # Relative transition densities p_n(i,j)=P^n(i,j)/pi(j).
    # Every row of P^n is a convex combination of rows of P, so these
    # one-step extrema bound all n>=1.
    density = p / pi[None, :]
    m, M = float(density.min()), float(density.max())
    delta = (m / M) ** 2
    bridge_hgr_bound = 1.0 - delta

    max_hgr = 0.0
    cases = 0
    for left_gap in (0, 1, 2, 3):
        for middle_gap in (1, 2, 3):
            for right_gap in (0, 1, 2, 3):
                d = middle_gap
                pl = np.linalg.matrix_power(p, left_gap) if left_gap else None
                pd = np.linalg.matrix_power(p, d)
                pr = np.linalg.matrix_power(p, right_gap) if right_gap else None
                ptotal = (
                    np.linalg.matrix_power(p, left_gap + d + right_gap)
                    if left_gap and right_gap
                    else None
                )
                for x in (range(3) if left_gap else (None,)):
                    for y in (range(3) if right_gap else (None,)):
                        if left_gap and right_gap:
                            joint = np.array(
                                [
                                    [
                                        pl[x, u] * pd[u, v] * pr[v, y]
                                        / ptotal[x, y]
                                        for v in range(3)
                                    ]
                                    for u in range(3)
                                ]
                            )
                        elif left_gap:
                            joint = np.array(
                                [
                                    [pl[x, u] * pd[u, v] for v in range(3)]
                                    for u in range(3)
                                ]
                            )
                        elif right_gap:
                            joint = np.array(
                                [
                                    [
                                        pi[u] * pd[u, v] * pr[v, y] / pi[y]
                                        for v in range(3)
                                    ]
                                    for u in range(3)
                                ]
                            )
                        else:
                            joint = pi[:, None] * pd
                        rho = hgr(joint)
                        max_hgr = max(max_hgr, rho)
                        cases += 1
                        assert rho <= bridge_hgr_bound + 2e-12

    print("PASS: finite-state bridge kernels satisfy the Doeblin HGR bound")
    print(f"uniform density bounds: m={m:.12f}, M={M:.12f}")
    print(f"minorization delta=(m/M)^2={delta:.12e}")
    print(f"conditional HGR upper bound={bridge_hgr_bound:.12f}")
    print(f"largest enumerated conditional HGR={max_hgr:.12f}")
    print(f"endpoint/gap configurations checked={cases}")
    print("SCOPE: finite-state regression of the bridge-minorization algebra")


if __name__ == "__main__":
    main()
