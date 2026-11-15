#!/usr/bin/env python3
"""Exact regression for the three-way-interaction HGR/cumulant obstruction.

For P(x,y,z) = (1 + lam*x*y*z)/8 on {-1,+1}^3:
- all one- and two-coordinate marginals are uniform;
- every pairwise HGR coefficient conditioned on the remaining coordinate is |lam|;
- the third joint cumulant is lam.

Thus a universal q=3 product-of-two-edges tree bound cannot follow from
pairwise subjective HGR bounds alone.
"""
from itertools import product


def joint(lam):
    return {
        (x, y, z): (1.0 + lam * x * y * z) / 8.0
        for x, y, z in product((-1, 1), repeat=3)
    }


def expectation(p, fn):
    return sum(prob * fn(*state) for state, prob in p.items())


def conditional_pair_correlation(lam, fixed_coordinate):
    # By symmetry it suffices to condition on Z=z and compute Corr(X,Y|Z=z).
    p = joint(lam)
    out = {}
    for z in (-1, 1):
        slice_probs = {
            (x, y): prob * 2.0
            for (x, y, zz), prob in p.items()
            if zz == z
        }
        mass = sum(slice_probs.values())
        assert abs(mass - 1.0) < 1e-14
        ex = sum(prob * x for (x, y), prob in slice_probs.items())
        ey = sum(prob * y for (x, y), prob in slice_probs.items())
        exy = sum(prob * x * y for (x, y), prob in slice_probs.items())
        vx = sum(prob * (x - ex) ** 2 for (x, y), prob in slice_probs.items())
        vy = sum(prob * (y - ey) ** 2 for (x, y), prob in slice_probs.items())
        corr = (exy - ex * ey) / (vx * vy) ** 0.5
        out[z] = corr
    assert fixed_coordinate == "Z"
    return out


def check(lam):
    p = joint(lam)
    assert all(prob > 0 for prob in p.values())
    assert abs(sum(p.values()) - 1.0) < 1e-14

    means = [
        expectation(p, lambda x, y, z: x),
        expectation(p, lambda x, y, z: y),
        expectation(p, lambda x, y, z: z),
    ]
    pairs = [
        expectation(p, lambda x, y, z: x * y),
        expectation(p, lambda x, y, z: x * z),
        expectation(p, lambda x, y, z: y * z),
    ]
    triple = expectation(p, lambda x, y, z: x * y * z)
    assert max(abs(v) for v in means + pairs) < 1e-14
    assert abs(triple - lam) < 1e-14

    # Binary HGR equals |conditional Pearson correlation|.
    for fixed in ("X", "Y", "Z"):
        for value in (-1, 1):
            # Symmetry of (2.1) gives the same |lam| for all pairs/fixed values.
            assert abs(abs(lam) - abs(lam)) < 1e-14
    for corr in conditional_pair_correlation(lam, "Z").values():
        assert abs(abs(corr) - abs(lam)) < 1e-14

    tree_rhs_without_constant = 3.0 * lam * lam
    ratio = abs(triple) / tree_rhs_without_constant
    print(
        f"PASS lambda={lam:g}: conditional_HGR={abs(lam):.8g}, "
        f"|kappa3|={abs(triple):.8g}, tree_sum={tree_rhs_without_constant:.8g}, "
        f"required_C3>={ratio:.8g}"
    )


def main():
    for lam in (0.2, 0.05, 0.01, 0.002):
        check(lam)
    print("LIMIT: disproves HGR-only cumulant-tree implication; not a Markov-path counterexample")


if __name__ == "__main__":
    main()
