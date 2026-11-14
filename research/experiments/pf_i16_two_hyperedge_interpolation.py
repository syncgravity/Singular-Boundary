#!/usr/bin/env python3
"""Exact two-hyperedge nilpotent interpolation checks.

Run:
    python research/experiments/pf_i16_two_hyperedge_interpolation.py

The tests retain each link's complete moment table, including nonzero means.
They verify an exact interpolation identity in the squarefree row algebra.
They do not prove a uniform time-integrated estimate.
"""
from itertools import product


def padd(a, b):
    out = list(a) + [0] * max(0, len(b) - len(a))
    for i, x in enumerate(b):
        out[i] += x
    return trim(out)


def trim(a):
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


def pscale(a, c):
    return trim([c * x for x in a])


def pmul(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return trim(out)


def pderiv(a):
    return trim([i * a[i] for i in range(1, len(a))] or [0])


def pint01(a):
    return sum(x / (i + 1) for i, x in enumerate(a))


def zadd(a, b):
    out = dict(a)
    for mask, poly in b.items():
        out[mask] = padd(out.get(mask, [0]), poly)
    return {m: p for m, p in out.items() if any(p)}


def zmul(a, b):
    out = {}
    for ma, pa in a.items():
        for mb, pb in b.items():
            if ma & mb:
                continue  # squarefree row variables: z_i^2 = 0
            mask = ma | mb
            out[mask] = padd(out.get(mask, [0]), pmul(pa, pb))
    return {m: p for m, p in out.items() if any(p)}


def zscale(a, c):
    return {m: pscale(p, c) for m, p in a.items()}


def zpower_series_log(f, r):
    # f = 1 + g, and g is in the nilpotent augmentation ideal.
    g = dict(f)
    g[0] = padd(g.get(0, [0]), [-1])
    power = g
    out = {}
    for k in range(1, r + 1):
        out = zadd(out, zscale(power, (-1) ** (k + 1) / k))
        power = zmul(power, g)
    return out


def zpower_series_inverse(f, r):
    g = dict(f)
    g[0] = padd(g.get(0, [0]), [-1])
    power = {0: [1]}
    out = {0: [1]}
    for k in range(1, r + 1):
        power = zmul(power, g)
        out = zadd(out, zscale(power, (-1) ** k))
    return out


def moment_table(rows, offsets, slopes):
    """Moments of Y_i = offset_i + slope_i U, U a shared Rademacher."""
    rows = tuple(rows)
    out = {frozenset(): 1}
    for mask in range(1, 1 << len(rows)):
        selected = [rows[j] for j in range(len(rows)) if mask & (1 << j)]
        vals = []
        for u in (-1, 1):
            value = 1
            for i in selected:
                value *= offsets[i] + slopes[i] * u
            vals.append(value)
        out[frozenset(selected)] = sum(vals) / 2
    return out


def local_moment(table, subset):
    return table[frozenset(subset)]


def projected_interpolation(r, h1, h2, m1, m2):
    """F_lambda(z)=D(M1 [1+lambda(M2-1)]), represented by row masks."""
    full = (1 << r) - 1
    f = {0: [1]}
    for mask in range(1, full + 1):
        s = {i for i in range(r) if mask & (1 << i)}
        b1 = s & h1
        b2 = s & h2
        coeff = local_moment(m1, b1) * local_moment(m2, b2)
        # Every nonempty monomial of the second whole link object is
        # multiplied by lambda; its constant coefficient remains one.
        f[mask] = [0, coeff] if b2 else [coeff]
    return f


def coefficient(poly, mask):
    return poly.get(mask, [0])


def direct_cumulant_via_log(f, r):
    return sum(coefficient(zpower_series_log(f, r), (1 << r) - 1))


def test_overlap_sizes_and_nonzero_means():
    # r=3..7; H1 and H2 cover every row and have every possible
    # overlap size q=1,...,r. All local slot means are nonzero.
    tests = 0
    for r in range(3, 8):
        rows = set(range(r))
        offsets1 = {i: 0.35 + 0.07 * i for i in rows}
        slopes1 = {i: 0.21 + 0.025 * i for i in rows}
        offsets2 = {i: 0.42 + 0.035 * i for i in rows}
        slopes2 = {i: -0.17 + 0.018 * i for i in rows}
        m1 = moment_table(rows, offsets1, slopes1)
        m2 = moment_table(rows, offsets2, slopes2)
        assert all(m1[frozenset({i})] != 0 and
                   m2[frozenset({i})] != 0 for i in rows)

        for q in range(1, r + 1):
            # q shared rows; the union is all rows.
            h1 = set(range(r - 1)) if q < r else set(rows)
            h2 = set(range(q)) | ({r - 1} if q < r else set())
            assert h1 | h2 == rows and len(h1 & h2) == q
            f = projected_interpolation(r, h1, h2, m1, m2)
            full = (1 << r) - 1
            logf = zpower_series_log(f, r)
            target = sum(coefficient(logf, full))

            # Exact logarithmic derivative:
            # d/dlambda log F = (dF/dlambda) F^{-1}.
            df = {mask: pderiv(poly) for mask, poly in f.items()}
            invf = zpower_series_inverse(f, r)
            integrand = zmul(df, invf)
            integrated = pint01(coefficient(integrand, full))
            assert abs(integrated - target) < 1e-8, (
                r, q, integrated, target
            )
            # Endpoint check also verifies the possible one-hyperedge
            # baseline when H1 is all rows (q=r).
            at_one = target
            at_zero = coefficient(
                zpower_series_log({m: [p[0]] for m, p in f.items()}, r),
                full
            )[0]
            assert abs(integrated - (at_one - at_zero)) < 1e-8
            tests += 1
    return tests


def test_two_row_g2_with_nonzero_means():
    # For r=2 and both links incident to both rows:
    # integral_0^1 d lambda [z1 z2] d_lambda log F_lambda
    # = E(X1 X2)E(Y1 Y2)-E(X1)E(X2)E(Y1)E(Y2).
    m1 = {
        frozenset(): 1, frozenset({0}): 2, frozenset({1}): 3,
        frozenset({0, 1}): 11,
    }
    m2 = {
        frozenset(): 1, frozenset({0}): 5, frozenset({1}): 7,
        frozenset({0, 1}): 41,
    }
    f = projected_interpolation(2, {0, 1}, {0, 1}, m1, m2)
    full = 3
    integrand = zmul(
        {mask: pderiv(poly) for mask, poly in f.items()},
        zpower_series_inverse(f, 2),
    )
    got = pint01(coefficient(integrand, full))
    expected = 11 * 41 - (2 * 5) * (3 * 7)
    ce, cf = 11 - 2 * 3, 41 - 5 * 7
    g2 = ce * cf + ce * 5 * 7 + 2 * 3 * cf
    assert abs(got - expected) < 1e-10
    assert expected == g2


def test_disjoint_hyperedges_give_zero_cross_cumulant():
    # H1={0,1}, H2={2,3}; row-diagonal projection factorizes.
    r = 4
    rows = set(range(r))
    m1 = moment_table(rows, {i: 0.4 + i / 10 for i in rows},
                      {i: 0.2 + i / 20 for i in rows})
    m2 = moment_table(rows, {i: 0.6 + i / 12 for i in rows},
                      {i: -0.1 + i / 30 for i in rows})
    f = projected_interpolation(r, {0, 1}, {2, 3}, m1, m2)
    assert abs(direct_cumulant_via_log(f, r)) < 1e-10


def main():
    n = test_overlap_sizes_and_nonzero_means()
    test_two_row_g2_with_nonzero_means()
    test_disjoint_hyperedges_give_zero_cross_cumulant()
    print(
        "PASS: two-hyperedge log interpolation; "
        f"{n} overlap-size/nonzero-mean cases; G2; disjoint factorization"
    )


if __name__ == "__main__":
    main()
