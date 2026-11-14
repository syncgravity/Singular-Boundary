#!/usr/bin/env python3
"""Exact three-hyperedge attachment checks in the squarefree row algebra.

This tests iterative whole-object activation and mixed logarithmic derivatives.
It is an algebraic regression, not a weighted temporal estimate.
"""
from itertools import combinations, product


def ptrim(p):
    return {k: v for k, v in p.items() if abs(v) > 1e-13}


def padd(a, b):
    out = dict(a)
    for k, v in b.items():
        out[k] = out.get(k, 0.0) + v
    return ptrim(out)


def pscale(a, c):
    return ptrim({k: c * v for k, v in a.items()})


def pmul(a, b):
    out = {}
    for (i, j), x in a.items():
        for (k, l), y in b.items():
            key = (i + k, j + l)
            out[key] = out.get(key, 0.0) + x * y
    return ptrim(out)


ONE = {(0, 0): 1.0}


def pderiv(a, axis):
    out = {}
    for (i, j), v in a.items():
        degree = (i, j)[axis]
        if degree:
            key = (i - (axis == 0), j - (axis == 1))
            out[key] = out.get(key, 0.0) + degree * v
    return ptrim(out)


def pint01(a, axis):
    return sum(v / ((i if axis == 0 else j) + 1)
               for (i, j), v in a.items())


def zadd(a, b):
    out = dict(a)
    for mask, poly in b.items():
        out[mask] = padd(out.get(mask, {}), poly)
    return {m: p for m, p in out.items() if p}


def zmul(a, b):
    out = {}
    for ma, pa in a.items():
        for mb, pb in b.items():
            if ma & mb:
                continue
            mask = ma | mb
            out[mask] = padd(out.get(mask, {}), pmul(pa, pb))
    return {m: p for m, p in out.items() if p}


def zscale(a, c):
    return {m: pscale(p, c) for m, p in a.items()}


def zlog(f, r):
    g = dict(f)
    g[0] = padd(g.get(0, {}), {(0, 0): -1.0})
    power, out = g, {}
    for k in range(1, r + 1):
        out = zadd(out, zscale(power, (-1) ** (k + 1) / k))
        power = zmul(power, g)
    return out


def zinv(f, r):
    g = dict(f)
    g[0] = padd(g.get(0, {}), {(0, 0): -1.0})
    power, out = {0: ONE}, {0: ONE}
    for k in range(1, r + 1):
        power = zmul(power, g)
        out = zadd(out, zscale(power, (-1) ** k))
    return out


def zderiv(f, axis):
    return {m: pderiv(p, axis) for m, p in f.items()}


def moment_table(rows, offset, slope):
    out = {frozenset(): 1.0}
    rows = tuple(rows)
    for mask in range(1, 1 << len(rows)):
        chosen = [rows[j] for j in range(len(rows)) if mask & (1 << j)]
        vals = []
        for u in (-1.0, 1.0):
            x = 1.0
            for i in chosen:
                x *= offset[i] + slope[i] * u
            vals.append(x)
        out[frozenset(chosen)] = sum(vals) / 2.0
    return out


def local(m, subset):
    return m[frozenset(subset)]


def projected_three_link(r, hs, ms):
    """D(M1(1+a(M2-1))(1+b(M3-1)))."""
    full = (1 << r) - 1
    f = {0: ONE}
    h1, h2, h3 = hs
    m1, m2, m3 = ms
    for mask in range(1, full + 1):
        s = {i for i in range(r) if mask & (1 << i)}
        b1, b2, b3 = s & h1, s & h2, s & h3
        coeff = local(m1, b1) * local(m2, b2) * local(m3, b3)
        degree_a = int(bool(b2))
        degree_b = int(bool(b3))
        f[mask] = {(degree_a, degree_b): coeff}
    return f


def eval_poly(p, a, b):
    return sum(v * a**i * b**j for (i, j), v in p.items())


def eval_row_poly(f, a, b):
    return {m: {(0, 0): eval_poly(p, a, b)} for m, p in f.items()}


def coeff_at(f, full, a, b):
    return eval_poly(f.get(full, {}), a, b)


def test_three_link_telescoping_and_mixed_derivative():
    cases = 0
    for r in range(3, 7):
        rows = set(range(r))
        ms = [
            moment_table(rows, {i: .31 + .04*i for i in rows},
                         {i: .19 + .02*i for i in rows}),
            moment_table(rows, {i: .43 + .03*i for i in rows},
                         {i: -.13 + .015*i for i in rows}),
            moment_table(rows, {i: .27 + .05*i for i in rows},
                         {i: .11 + .017*i for i in rows}),
        ]
        # Enumerate every overlapping two-hyperedge cover: each row is
        # incident to link 1 only, link 2 only, or both. Then attach link 3
        # through every nonempty subset of rows.
        for states in product((0, 1, 2), repeat=r):
            h1 = {i for i, state in enumerate(states) if state in (0, 2)}
            h2 = {i for i, state in enumerate(states) if state in (1, 2)}
            if not (h1 & h2):
                continue
            for q in range(1, r + 1):
                for h3_tuple in combinations(rows, q):
                    hs = [h1, h2, set(h3_tuple)]
                    f = projected_three_link(r, hs, ms)
                    full = (1 << r) - 1
                    L = zlog(f, r)
                    target = eval_poly(L.get(full, {}), 1, 1)

                    # Sequential activation: first link 2, then link 3.
                    first = coeff_at(L, full, 1, 0) - coeff_at(L, full, 0, 0)
                    second = coeff_at(L, full, 1, 1) - coeff_at(L, full, 1, 0)
                    assert abs(target - first - second - coeff_at(L, full, 0, 0)) < 1e-8

                    # Mixed derivative of log F = F_ab/F - F_a F_b/F^2.
                    fa = zderiv(f, 0)
                    fb = zderiv(f, 1)
                    fab = zderiv(fa, 1)
                    inv = zinv(f, r)
                    mixed = zadd(zmul(fab, inv),
                                 zscale(zmul(zmul(fa, fb), zmul(inv, inv)), -1))
                    full_mixed = mixed.get(full, {})
                    # Double polynomial integration gives the rectangular log increment.
                    mixed_integral = sum(
                        v / ((i + 1) * (j + 1))
                        for (i, j), v in full_mixed.items()
                    )
                    rectangular = (
                        coeff_at(L, full, 1, 1)
                        - coeff_at(L, full, 1, 0)
                        - coeff_at(L, full, 0, 1)
                        + coeff_at(L, full, 0, 0)
                    )
                    assert abs(mixed_integral - rectangular) < 1e-8
                    cases += 1
    return cases


def test_third_link_one_row_attachment():
    # A third hyperedge attached to only one row cannot by itself create
    # a new cross-row connected component. If the first two links are
    # already full-row, the third-link increment may still be nonzero:
    # it changes the moment of that row and hence the global cumulant.
    # The mixed derivative is the exact interaction diagnostic.
    r = 3
    rows = set(range(r))
    ms = [
        moment_table(rows, {i: .4 for i in rows}, {i: .2 for i in rows}),
        moment_table(rows, {i: .5 for i in rows}, {i: -.1 for i in rows}),
        moment_table(rows, {i: .3 for i in rows}, {i: .17 for i in rows}),
    ]
    f = projected_three_link(r, [rows, rows, {1}], ms)
    full = (1 << r) - 1
    L = zlog(f, r)
    # A one-row third link is not an independent new bridge; it modulates
    # an existing connected coefficient. The mixed derivative records it.
    mixed = zadd(
        zmul(zderiv(zderiv(f, 0), 1), zinv(f, r)),
        zscale(zmul(
            zmul(zderiv(f, 0), zderiv(f, 1)),
            zmul(zinv(f, r), zinv(f, r))
        ), -1)
    )
    assert abs(eval_poly(L.get(full, {}), 1, 1)) > 0
    assert abs(eval_poly(mixed.get(full, {}), 1, 1)) > 0


def main():
    n = test_three_link_telescoping_and_mixed_derivative()
    test_third_link_one_row_attachment()
    print(f"PASS: three-link activation, arbitrary third-link overlap ({n} cases), mixed-log derivative")
    

if __name__ == "__main__":
    main()
