# PF-I16: matching-relative exchange criterion for multivalued leaf projections

Date: 2026-11-17

Branch: `research/pf-i16-admissible-exchange-2026-11-16`

Verifier: `research/verification/verify_pf_i16_n10_multivalued_pi_exchange_scc.py`

Workflow: [44048791345](https://github.com/syncgravity/Singular-Boundary/actions/runs/44048791345)

## 1. Exchange digraph

Let G=(X,Y,E) be a finite bipartite graph and let mu:X->Y be a matching saturating X. Write Y_free=Y\mu(X). Define the matching-relative digraph D_mu on X by

```
x -> z  iff  x != z and (x, mu(z)) is in E.
```

An arc x->z means that x can take the right vertex currently assigned to z. Also record a free-neighbor at x whenever x is adjacent to some y in Y_free.

For A subset X, the exact slack identity is

```
|N(A)| - |A| = |F(A)| + |out_D(A)|,
```

where F(A)=N(A) intersect Y_free and out_D(A) is the set of arcs from A to X\A. This follows by partitioning N(A) into unmatched right vertices and matched right vertices mu(z); the latter are indexed injectively by z in X.

Consequently, a nonempty set A has zero Hall slack if and only if it is out-closed in D_mu and has no free neighbor. Every such set contains a sink strongly connected component with no free neighbor. Conversely, a sink SCC with no free neighbor is itself a zero-slack Hall set.

Thus:
- G has strict Hall expansion |N(A)| >= |A|+1 for every nonempty A iff every sink SCC of D_mu has at least one free right neighbor.
- Equivalently, every vertex of D_mu can reach a free right neighbor.

This is a matching-relative certificate for strict Hall expansion, not merely a test of a chosen matching.

## 2. Every edge is individually exchangeable under strict Hall expansion

Suppose every vertex of D_mu can reach a free right vertex. Take any edge (x,y) in E, with y != mu(x), and let z be the owner of y, so y=mu(z) and x->z is an arc.

Follow a directed path from z to a vertex adjacent to a free right vertex. In the corresponding alternating sequence, each intermediate source gives up its matched right vertex and takes the next source's matched right vertex. If the path reaches x before reaching a free right vertex, close the alternating cycle through the prescribed edge x-y. Otherwise the path reaches a free right vertex without using x, and flipping it gives an augmenting reroute that assigns x to y.

Therefore every edge of G belongs to some left-saturating matching. This is a *single-edge* flexibility result; it does not say arbitrary collections of prescribed edges can be realized simultaneously.

The criterion is exact relative to the selected matching: a sink SCC with no free neighbor is precisely the obstruction to strict Hall expansion, and edges entering such a closed tight block need not be individually exchangeable.

## 3. Application to the multivalued-pi relation

The new n=10 verifier reconstructs the same relation as the independently certified multivalued-pi graph:
- for each child source, range over all non-root overlap-tree leaves;
- delete the selected leaf interval to obtain its parent source;
- retain child outputs whose inverse final-switch projection belongs to the canonical parent neighborhood;
- deduplicate child targets per source;
- compute a left-saturating matching;
- build D_mu and enumerate its sink SCCs and their free right neighbors.

The test asks whether the n=10 multivalued-pi graph has any sink SCC with no free right neighbor. If none exists, it establishes strict Hall expansion for every nonempty child-source subset in this finite graph and, additionally, individual exchangeability of every one of its incidences.

This finite test does not prove the same SCC condition for arbitrary even n. The all-orders task is now sharpened to a structural proof that the matching-relative digraph of the multivalued-pi relation has no sink SCC without a free target (or, more directly, that every nonempty source set has positive Hall slack).

## 4. Proof boundary

A left-saturating matching alone proves Hall's non-strict inequalities. The extra no-zero-free-sink-SCC condition proves *strict* Hall expansion and universal single-edge flexibility. Neither statement by itself supplies an all-orders construction of the matching or a simultaneous prescribed-edge theorem.

The weighted one-link inequality remains conditional on an all-orders load-dominating matching. No Yang--Mills mass-gap conclusion is claimed here.
