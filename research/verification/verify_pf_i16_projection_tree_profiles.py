#!/usr/bin/env python3
"""Finite-order audit of PF-I16 temporal projection/profile combinatorics.

This verifies, for m <= 8, the centered Pi+Q expansion of an ordered
stationary Markov cumulant and a coefficientwise comparison with Cayley-tree
cut profiles. It is a finite combinatorial check, not an all-orders proof.
"""
from collections import Counter
from itertools import product
from math import factorial
import argparse


def set_partitions(items):
    if not items:
        yield []
        return
    x = items[0]
    for p in set_partitions(items[1:]):
        yield [[x]] + [b[:] for b in p]
        for j in range(len(p)):
            q = [b[:] for b in p]
            q[j] = [x] + q[j]
            yield q


def nonzero_q_choices(block):
    """Q edges in each segment; Pi cuts may not leave centered singletons."""
    r = len(block)
    if r < 2:
        return []
    out = []
    for mask in range(1 << (r - 1)):
        cuts = [j for j in range(r - 1) if not (mask >> j) & 1]
        bounds = [-1] + cuts + [r - 1]
        segment_lengths = [bounds[j + 1] - bounds[j]
                           for j in range(len(bounds) - 1)]
        if all(n >= 2 for n in segment_lengths):
            out.append(tuple((block[j], block[j + 1])
                             for j in range(r - 1) if (mask >> j) & 1))
    return out


def projection_terms(m):
    coeff = Counter()
    for part in set_partitions(list(range(m))):
        k = len(part)
        if any(len(block) == 1 for block in part):
            continue
        choices = [nonzero_q_choices(block) for block in part]
        if any(not c for c in choices):
            continue
        mu = (-1) ** (k - 1) * factorial(k - 1)
        for selected in product(*choices):
            edges = tuple(sorted(edge for group in selected for edge in group))
            coeff[edges] += mu
    return {edges: c for edges, c in coeff.items() if c}


def profile(edges, m):
    return tuple(sum(1 for a, b in edges if a <= gap < b) - 1
                 for gap in range(m - 1))


def interval_connected(edges, m):
    if not edges:
        return False
    if min(a for a, _ in edges) != 0 or max(b for _, b in edges) != m - 1:
        return False
    return all(any(a <= gap < b for a, b in edges)
               for gap in range(m - 1))


def tree_profile_counts(m):
    counts = Counter()
    if m == 2:
        counts[(0,)] = 1
        return counts
    for code in product(range(m), repeat=m - 2):
        degree = [1] * m
        for v in code:
            degree[v] += 1
        edges = []
        for v in code:
            leaf = next(i for i, d in enumerate(degree) if d == 1)
            edges.append((min(leaf, v), max(leaf, v)))
            degree[leaf] -= 1
            degree[v] -= 1
        leaves = [i for i, d in enumerate(degree) if d == 1]
        edges.append(tuple(sorted(leaves)))
        counts[profile(edges, m)] += 1
    return counts


def audit(m):
    terms = projection_terms(m)
    proj_profiles = Counter()
    for edges, coefficient in terms.items():
        if not interval_connected(edges, m):
            raise AssertionError(
                f"disconnected surviving interval family: m={m}, {edges}")
        p = profile(edges, m)
        if any(x < 0 for x in p):
            raise AssertionError(f"uncovered temporal gap: m={m}, {edges}")
        proj_profiles[p] += abs(coefficient)
    trees = tree_profile_counts(m)
    violations = [(p, n, trees.get(p, 0))
                  for p, n in proj_profiles.items() if n > trees.get(p, 0)]
    return {
        "m": m,
        "surviving_projection_terms": len(terms),
        "absolute_coefficient_mass": sum(abs(c) for c in terms.values()),
        "projection_profiles": len(proj_profiles),
        "tree_profiles": len(trees),
        "coefficientwise_violations": violations,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-m", type=int, default=8)
    args = parser.parse_args()
    if not 2 <= args.max_m <= 8:
        raise SystemExit("--max-m must be between 2 and 8")
    for m in range(2, args.max_m + 1):
        result = audit(m)
        print(result)
        if result["coefficientwise_violations"]:
            raise SystemExit(1)
    print("PASS: finite coefficientwise profile domination for audited orders only")


if __name__ == "__main__":
    main()
