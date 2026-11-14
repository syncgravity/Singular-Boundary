#!/usr/bin/env python3
"""Exhaustive small-state test of the interlaced multi-cut maximal-correlation conjecture.

This is a regression/falsification test for binary stationary reset chains, not a proof
for arbitrary stationary Markov kernels.
"""
from itertools import product
from math import atanh, tanh
import numpy as np


def maximal_correlation(q, gaps, colors):
    n = len(colors)
    s_pos = [i for i, c in enumerate(colors) if c == 0]
    t_pos = [i for i, c in enumerate(colors) if c == 1]
    s_states = list(product((-1, 1), repeat=len(s_pos)))
    t_states = list(product((-1, 1), repeat=len(t_pos)))
    s_index = {x: i for i, x in enumerate(s_states)}
    t_index = {x: i for i, x in enumerate(t_states)}
    joint = np.zeros((len(s_states), len(t_states)), dtype=float)

    for path in product((-1, 1), repeat=n):
        prob = 0.5
        for j, gap in enumerate(gaps):
            rho = q ** gap
            prob *= (1.0 + rho * path[j] * path[j + 1]) / 2.0
        s = tuple(path[i] for i in s_pos)
        t = tuple(path[i] for i in t_pos)
        joint[s_index[s], t_index[t]] += prob

    ps = joint.sum(axis=1)
    pt = joint.sum(axis=0)
    normalized = joint / np.sqrt(np.outer(ps, pt))
    singular_values = np.linalg.svd(normalized, compute_uv=False)
    return float(singular_values[1])


def main():
    tested = 0
    worst_slack = float("inf")
    worst_case = None
    for n in range(2, 7):
        for colors in product((0, 1), repeat=n):
            if 0 not in colors or 1 not in colors:
                continue
            cuts = [j for j in range(n - 1) if colors[j] != colors[j + 1]]
            if not cuts:
                continue
            for gaps in product((1, 2), repeat=n - 1):
                for q in (0.1, 0.3, 0.5, 0.7, 0.9):
                    rho = maximal_correlation(q, gaps, colors)
                    cut_strength = sum(atanh(q ** gaps[j]) for j in cuts)
                    bound = tanh(cut_strength)
                    slack = bound - rho
                    if slack < worst_slack:
                        worst_slack = slack
                        worst_case = (n, colors, gaps, q, rho, bound)
                    assert rho <= bound + 2e-10, (
                        "counterexample found: "
                        f"n={n}, colors={colors}, gaps={gaps}, q={q}, "
                        f"rho={rho}, bound={bound}"
                    )
                    tested += 1

    print("PASS: exhaustive binary-chain multi-cut maximal-correlation tests")
    print(f"cases={tested}; worst additive slack={worst_slack:.12g}")
    print(f"closest case={worst_case}")
    print("SCOPE: finite binary reset chains, n<=6, gaps in {{1,2}}")
    print("NOT A PROOF: arbitrary stationary or nonreversible Markov kernels")


if __name__ == "__main__":
    main()
