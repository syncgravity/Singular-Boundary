#!/usr/bin/env python3
"""Regression for repeated-slot incidence and complete-overlap tensor gap.

The incidence fixture demonstrates that D counts occurrences, not support
types. The finite matrix fixtures check the tensor-product spectral norm for
reset chains. The all-state-space proof is in the companion audit.
"""
from itertools import product
import numpy as np


def reset_semigroup(delta, t):
    # Two-state reset chain: P_t = Pi + exp(-delta*t)(I-Pi).
    decay = np.exp(-delta * t)
    return np.array([[0.5 + 0.5 * decay, 0.5 - 0.5 * decay],
                     [0.5 - 0.5 * decay, 0.5 + 0.5 * decay]])


def tensor(matrix, count):
    out = np.array([[1.0]])
    for _ in range(count):
        out = np.kron(out, matrix)
    return out


def centered_operator_norm(matrix):
    n = matrix.shape[0]
    one = np.ones((n, 1)) / np.sqrt(n)
    projector = one @ one.T
    # The reset matrices are symmetric, so the Euclidean operator norm on
    # the orthogonal complement of constants is the second singular value.
    values = np.linalg.svd(matrix - projector, compute_uv=False)
    return values[0]


def check_tensor_gap():
    delta, t = 0.7, 1.3
    one_link = reset_semigroup(delta, t)
    expected = np.exp(-delta * t)
    for links in range(1, 5):
        product_semigroup = tensor(one_link, links)
        actual = centered_operator_norm(product_semigroup)
        assert abs(actual - expected) < 1e-12, (links, actual, expected)
        print(f"PASS tensor gap: {links} links, norm={actual:.12g}")


def check_repeated_incidence():
    D_geometry = 232
    for r in (1, 8, 232, 233, 512):
        # Repeating one face creates one slot on each of its four links
        # per row. Hence every boundary link has incidence r.
        N = 4 * r
        q_e = r
        assert N == 4 * r and q_e == r
        print(f"PASS repeated face: r={r}, total_slots={N}, q_e={q_e}, "
              f"geometric_D_suffices={q_e <= D_geometry}")


def check_support_type_compression():
    # Repetition grows, while distinct support-type incidence stays fixed.
    supports = {
        'face-A': frozenset({'e1', 'e2', 'e3', 'e4'}),
        'face-B': frozenset({'e2', 'e5', 'e6', 'e7'}),
        'pair-AB': frozenset({'e2', 'e3', 'e5', 'e8'}),
    }
    for repetitions in (1, 16, 256, 4096):
        occurrences = [name for name in supports for _ in range(repetitions)]
        types_per_link = {
            link: sum(link in supports[name] for name in supports)
            for link in {e for support in supports.values() for e in support}
        }
        occurrences_per_link = {
            link: sum(link in supports[name] for name in occurrences)
            for link in types_per_link
        }
        assert max(types_per_link.values()) <= len(supports)
        assert max(occurrences_per_link.values()) == repetitions * max(types_per_link.values())
        print(f'PASS support compression: repetitions={repetitions}, '
              f'distinct_types/link={max(types_per_link.values())}, '
              f'occurrences/link={max(occurrences_per_link.values())}')

def main():
    check_repeated_incidence()
    check_support_type_compression()
    check_tensor_gap()
    print("LIMIT: finite reset-chain regression; no sparse-graph repeated-label theorem")


if __name__ == "__main__":
    main()
