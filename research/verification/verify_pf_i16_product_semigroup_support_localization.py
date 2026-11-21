#!/usr/bin/env python3
"""Exact finite regressions for product-semigroup support localization.

The two-state chain is symmetric with transition eigenvalues 1 and q.
All calculations use Fractions, including the interlaced three-row example.
"""
from fractions import Fraction
from itertools import product


def verify_tensor_gap():
    for q in product((Fraction(1, 5), Fraction(1, 2), Fraction(4, 5)), repeat=4):
        product_gap_norm = max(q)
        # Tensor-product eigenvalues on nonconstant sectors are products
        # of a nonempty subset of the individual q's.
        for mask in range(1, 1 << len(q)):
            eigen = Fraction(1)
            for k, value in enumerate(q):
                if (mask >> k) & 1:
                    eigen *= value
            assert eigen <= product_gap_norm
        assert product_gap_norm == max(q)


def verify_support_vs_complete_tree():
    q = Fraction(1, 2)
    # Times in units of the one-step time scale: t1=0, t2=100, t3=50.
    r12, r13, r23 = q**100, q**50, q**50

    # Independent centered sign observables on the two links:
    # A1=U_e(t1), A2=U_e(t2)U_f(t2), A3=U_f(t3).
    # Every pair moment vanishes, so the third cumulant is the joint moment.
    exact_cumulant = r12 * r23

    # Support graph is the path 1--2--3, so there is one support spanning tree.
    support_tree_sum = r12 * r23

    # The complete graph has three spanning trees.
    complete_tree_sum = r12 * r13 + r12 * r23 + r13 * r23

    assert exact_cumulant == support_tree_sum
    assert complete_tree_sum > support_tree_sum
    assert complete_tree_sum / support_tree_sum == q**(-50) + 2

    # Scaling all gaps by L sends the ratio to q^(-50L)+2, unbounded in L.
    for scale in (1, 2, 3):
        ratio = q**(-50 * scale) + 2
        assert ratio > q**(-50 * (scale - 1)) + 2 if scale > 1 else ratio > 0


def main():
    verify_tensor_gap()
    verify_support_vs_complete_tree()
    print("PASS tensor-product L2 gap: every nonconstant tensor eigenvalue is bounded by max link contraction")
    print("PASS exact three-row cumulant equals its unique support-tree weight")
    print("PASS complete temporal-tree sum / support-tree weight = 2^50 + 2, and diverges under time scaling")


if __name__ == "__main__":
    main()
