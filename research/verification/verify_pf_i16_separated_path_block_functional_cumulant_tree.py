#!/usr/bin/env python3
"""Exact finite-state regression for separated Markov path-block cumulants."""
from fractions import Fraction
from itertools import product
from math import factorial


def partitions(items):
    items = tuple(items)
    if not items:
        yield ()
        return
    first, *rest = items
    for p in partitions(rest):
        yield ((first,),) + p
        for k in range(len(p)):
            yield p[:k] + (p[k] + (first,),) + p[k + 1:]


def cumulant(indices, moment):
    out = Fraction(0)
    for part in partitions(tuple(indices)):
        term = Fraction((-1) ** (len(part)-1) * factorial(len(part)-1))
        for block in part:
            term *= moment(frozenset(block))
        out += term
    return out


def cumulant_constant(q):
    return sum(
        factorial(len(part)-1) * (2 ** ((q-1)*len(part)))
        for part in partitions(range(q))
    )


def path_expectations(q, gaps, rho, reset_gap=None):
    # Each block is a two-time path segment [u_a,u_a+1].
    starts = []
    t = 0
    for a in range(q):
        starts.append(t)
        t += 1
        if a < q-1:
            t += gaps[a]
    last_time = starts[-1] + 1
    # Block function is (X_start + X_end + X_start*X_end)/3,
    # bounded by 1 and genuinely dependent on both endpoints.
    moments = {}
    for subset_mask in range(1 << q):
        value = Fraction(0)
        for path in product((-1, 1), repeat=last_time+1):
            weight = Fraction(1, 2)
            for k in range(1, last_time+1):
                if reset_gap is not None:
                    # Reset the transition from the left block endpoint
                    # to the right block start to an independent stationary draw.
                    reset_step = starts[reset_gap] + 1
                    if k == reset_step:
                        weight *= Fraction(1, 2)
                        continue
                weight *= (1 + rho*path[k-1]*path[k]) / 2
            obs = Fraction(1)
            for a in range(q):
                if (subset_mask >> a) & 1:
                    x, y = path[starts[a]], path[starts[a]+1]
                    obs *= Fraction(x + y + x*y, 3)
            value += weight * obs
        moments[frozenset(i for i in range(q) if (subset_mask >> i) & 1)] = value
    return moments


def check(q, gaps, rho, tag):
    moments = path_expectations(q, gaps, rho)
    kappa = cumulant(range(q), lambda s: moments[s])
    c = cumulant_constant(q)
    rhs = c * (rho ** sum(gaps))
    assert abs(kappa) <= rhs, (tag, kappa, rhs)

    # Reset each separating transition to stationarity. The path splits
    # into independent left/right groups, so the full q-cumulant is zero.
    for j in range(q-1):
        reset = path_expectations(q, gaps, rho, reset_gap=j)
        reset_kappa = cumulant(range(q), lambda s: reset[s])
        assert reset_kappa == 0, (tag, j, reset_kappa)
    print(
        f"PASS {tag}: q={q}, gaps={gaps}, "
        f"|kappa|={float(abs(kappa)):.6g}, exact reset cancellations"
    )


def main():
    rho = Fraction(2, 5)
    fixtures = [
        (2, [1], "two-block"),
        (3, [1, 2], "three-block-unequal-gaps"),
        (4, [1, 1, 2], "four-block"),
        (4, [2, 1, 1], "four-block-reversed-gaps"),
    ]
    for q, gaps, tag in fixtures:
        check(q, gaps, rho, tag)
    print("LIMIT: separated hulls only; interlaced multi-time blocks remain open")


if __name__ == "__main__":
    main()
