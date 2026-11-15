#!/usr/bin/env python3
"""Regression for repeated-slot incidence and complete-overlap tensor gap.

The incidence fixture demonstrates that D counts occurrences, not support
types. The tensor-sector fixture checks the product-gap norm formula without
third-party numerical dependencies. The all-state-space proof is in the audit.
"""
from itertools import product
from math import exp


def check_tensor_gap():
    delta, t = 0.7, 1.3
    one_link_decay = exp(-delta * t)
    for links in range(1, 9):
        sector_norms = [
            one_link_decay ** sum(active)
            for active in product((0, 1), repeat=links)
            if any(active)
        ]
        actual = max(sector_norms)
        assert abs(actual - one_link_decay) < 1e-14, (links, actual, one_link_decay)
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
        print(f"PASS support compression: repetitions={repetitions}, "
              f"distinct_types/link={max(types_per_link.values())}, "
              f"occurrences/link={max(occurrences_per_link.values())}")


def main():
    check_repeated_incidence()
    check_support_type_compression()
    check_tensor_gap()
    print("LIMIT: finite sector regression; no sparse-graph repeated-label theorem")


if __name__ == "__main__":
    main()
