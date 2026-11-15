#!/usr/bin/env python3
"""Exact regression for the three-way-interaction HGR/cumulant obstruction.

For P(x,y,z) = (1 + lam*x*y*z)/8 on {-1,+1}^3, each pair has conditional
HGR |lam| given the remaining coordinate, while kappa(X,Y,Z)=lam.
"""
from itertools import product


def joint(lam):
    return {
        (x, y, z): (1.0 + lam * x * y * z) / 8.0
        for x, y, z in product((-1, 1), repeat=3)
    }


def conditional_corr(p, i, j, k, fixed):
    pairs = {}
    for state, prob in p.items():
        if state[k] == fixed:
            key = (state[i], state[j])
            pairs[key] = pairs.get(key, 0.0) + 2.0 * prob
    assert abs(sum(pairs.values()) - 1.0) < 1e-14
    ex = sum(prob * x for (x, y), prob in pairs.items())
    ey = sum(prob * y for (x, y), prob in pairs.items())
    exy = sum(prob * x * y for (x, y), prob in pairs.items())
    vx = sum(prob * (x - ex) ** 2 for (x, y), prob in pairs.items())
    vy = sum(prob * (y - ey) ** 2 for (x, y), prob in pairs.items())
    return (exy - ex * ey) / (vx * vy) ** 0.5


def check(lam):
    p = joint(lam)
    assert all(prob > 0 for prob in p.values())
    assert abs(sum(p.values()) - 1.0) < 1e-14

    means = [sum(prob * state[i] for state, prob in p.items()) for i in range(3)]
    pairs = [
        sum(prob * state[i] * state[j] for state, prob in p.items())
        for i, j in ((0, 1), (0, 2), (1, 2))
    ]
    triple = sum(prob * x * y * z for (x, y, z), prob in p.items())
    assert max(abs(v) for v in means + pairs) < 1e-14
    assert abs(triple - lam) < 1e-14

    conditional = []
    for i, j, k in ((0, 1, 2), (0, 2, 1), (1, 2, 0)):
        for fixed in (-1, 1):
            corr = conditional_corr(p, i, j, k, fixed)
            assert abs(abs(corr) - abs(lam)) < 1e-14
            conditional.append(corr)

    # For q=3 there are three spanning trees, each with two eta=|lam| edges.
    tree_sum = 3.0 * lam * lam
    required_constant = abs(triple) / tree_sum
    print(
        f"PASS lambda={lam:g}: max_conditional_HGR={max(map(abs, conditional)):.8g}, "
        f"|kappa3|={abs(triple):.8g}, tree_sum={tree_sum:.8g}, "
        f"required_C3>={required_constant:.8g}"
    )


def main():
    for lam in (0.2, 0.05, 0.01, 0.002):
        check(lam)
    print("LIMIT: disproves HGR-only cumulant-tree implication; not a Markov-path counterexample")


if __name__ == "__main__":
    main()
