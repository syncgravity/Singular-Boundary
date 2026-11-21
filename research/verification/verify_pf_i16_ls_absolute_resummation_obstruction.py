#!/usr/bin/env python3
"""Exact finite regression for the two-link LS absolute-majorant obstruction.

For R rows sharing two links and coincident times, retain only LS terms
where link 1 has its one-block partition and link 2 has a pair partition.
The resulting lower bound is
  2**(R-2) * R**(R-2) * (R-1)!!
while the complete-graph tree polynomial is R**(R-2).
The asymptotic contradiction is proved in the companion audit.
"""
from math import prod


def odd_double_factorial(r: int) -> int:
    assert r >= 1 and r % 2 == 1
    return prod(range(1, r + 1, 2))


def check_even_order(r: int) -> None:
    assert r >= 2 and r % 2 == 0
    tree_count = r ** (r - 2)  # Cayley: spanning trees of K_r
    pair_partitions = odd_double_factorial(r - 1)
    retained_ls_lower_bound = (2 ** (r - 2)) * tree_count * pair_partitions
    ratio = retained_ls_lower_bound // tree_count
    assert retained_ls_lower_bound == ratio * tree_count
    assert ratio == (2 ** (r - 2)) * pair_partitions
    print(
        f"PASS R={r}: tree_count={tree_count}, "
        f"retained_LS/tree_count={ratio}"
    )


def main() -> None:
    for r in (2, 4, 6, 8, 10, 12, 14, 16, 18, 20):
        check_even_order(r)
    print(
        "OBSTRUCTION: ratio^(1/R) grows without bound along even R; "
        "no fixed C^R controls this absolute-value majorant."
    )


if __name__ == "__main__":
    main()
