#!/usr/bin/env python3
"""Verify the 4D plaquette/link temporal-port budget on finite periodic lattices."""
from itertools import combinations, product
from math import comb

D = 4
L = 5


def canonical_link(x, mu):
    y = list(x)
    y[mu] = (y[mu] + 1) % L
    a, b = tuple(x), tuple(y)
    return (a, b) if a < b else (b, a)


def plaquette_boundary(x, mu, nu):
    x_mu = list(x); x_mu[mu] = (x_mu[mu] + 1) % L
    x_nu = list(x); x_nu[nu] = (x_nu[nu] + 1) % L
    return {
        canonical_link(x, mu),
        canonical_link(tuple(x_mu), nu),
        canonical_link(tuple(x_nu), mu),
        canonical_link(x, nu),
    }


def main():
    sites = list(product(range(L), repeat=D))
    rows = []
    for x in sites:
        for mu, nu in combinations(range(D), 2):
            rows.append((x, mu, nu, plaquette_boundary(x, mu, nu)))

    incidence = {}
    for row_id, (_, _, _, links) in enumerate(rows):
        assert len(links) == 4
        for e in links:
            incidence.setdefault(e, set()).add(row_id)

    # Every positively oriented link is in two plaquettes for each of
    # the three transverse directions, hence six distinct plaquettes.
    assert all(len(rows_i) == 6 for rows_i in incidence.values())

    r = len(rows)
    ports = sum(len(v) for v in incidence.values())
    assert ports == 4 * r
    assert max(map(len, incidence.values())) == 6

    # Bell numbers through six, with Bell(6)=203.
    bell = [1]
    for n in range(1, 7):
        bell.append(sum(comb(n - 1, k) * bell[k] for k in range(n)))
    assert bell[6] == 203

    # For any partition of an incident row set, disjoint blocks conserve
    # every other link's original row-time ports.
    for e, incident_rows in incidence.items():
        sample = sorted(incident_rows)
        for cut in range(1, len(sample)):
            blocks = (set(sample[:cut]), set(sample[cut:]))
            for e2, rows_e2 in incidence.items():
                if e2 == e:
                    continue
                before = len(rows_e2 & set(sample))
                after = sum(len(rows_e2 & block) for block in blocks)
                assert before == after

    print("PASS: 4D periodic plaquette incidence and temporal-port budget")
    print(f"plaquette rows={r}; active links={len(incidence)}; ports={ports}")
    print("row degree=4; link incidence=6; Bell(6)=203")
    print("all tested block partitions conserve every other link's ports")
    print("SCOPE: combinatorial incidence/port accounting only")


if __name__ == "__main__":
    main()
