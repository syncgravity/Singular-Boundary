# PF-I16: guarded reverse-mark survival and commutation lemma

Date: 2026-11-18

Branch: `research/pf-i16-admissible-exchange-2026-11-16`

Parent checkpoint verified immediately before this write:
`e565923ef59dc701ae10654d56fd399d2ce5ebf2`.

Status: **exact local inverse and two-mark survival criteria; sufficient local commutation criterion. No canonical Hall or all-orders Hall conclusion.**

## 1. Reconciled interval geometry

The operative interval-overlap predicate in
`verify_pf_i16_local_switch_fractional_transport.py` is

```python
max(u, a) < min(w, b)
```

for old edge `(u,w)` and inserted interval `J=(a,b)`. It means positive-length intersection of the two open intervals. It does **not** mean endpoint alternation: containment is also overlap.

This is consistent with the actual two-case witness in that verifier:

- if a current port lies inside J, the path to port 1 supplies an alternating edge;
- if no current port lies inside J, the parent interval contains J and the endpoint path supplies an edge spanning J.

The earlier sentence in `PF_I16_GUARDED_SWITCH_REVALIDATION_2026_11_16.md` saying “Because e and J overlap, their endpoints alternate” is too strong and is corrected here. The subsequent discussion in that note already distinguishes an alternating edge from an edge containing J.

Write the four distinct endpoints as x1<x2<x3<x4. With the three allowed local trees

```
S0 = {x1x2, x2x3, x2x4}
S1 = {x1x2, x2x3, x3x4}
S2 = {x1x3, x2x3, x3x4}
```

and old edge e required not to belong to S_j, the possible relative orders are exactly:

1. **Alternating:** e=x1x3 or e=x2x4. Exactly two of S0,S1,S2 avoid reinserting e.
2. **Old edge contains J:** e=x1x4 and J=x2x3. All three patterns avoid reinserting e.
3. **J contains old edge:** e=x2x3 and J=x1x4. All three patterns contain e, so the no-reinsertion guard rejects every pattern.

Thus every valid guarded overlap is either alternating or old-edge-contains-J. The last case is excluded by the guard. This is the exact local geometry; no blanket alternation assumption is available.

## 2. Exact reverse-mark definition and unique inverse

Let T be a port tree and J={a,b} a proposed deleted interval. A guarded reverse mark consists of a pair of distinct old endpoints {u,v}, disjoint from J, and an index j such that, on X=J union {u,v}:

- e={u,v} has positive interval overlap with J;
- e is not an edge of S_j;
- S_j is contained in E(T[X]);
- the complete set of T-edges incident to a or b equals the set of S_j-edges incident to a or b.

The last equality is the full incidence guard; it rules out extra edges at either newly inserted endpoint. Since T is a tree and e is excluded from S_j, these conditions identify the induced four-port local tree exactly. The inverse is

[
P_J(T)=(T\setminus\delta_T(J))\cup\{uv\},
qquad
\delta_T(J)=\{g\in E(T):g\cap J\ne\varnothing\}.
]

For fixed (T,J), the two old endpoints are uniquely determined by the external neighbors of J in the prescribed local pattern. Hence there is at most one parent tree P_J(T). This is uniqueness for a fixed mark; it does not imply uniqueness of J.

## 3. Exact survival test for a second mark

Let J and K be two valid reverse marks of the same target T, with old edges e_J and e_K. If J intersects K, then K cannot remain a two-endpoint mark after deleting J: at least one of its marked ports is gone.

Suppose J and K are disjoint. Then K survives as a *candidate pair* in P_J(T), but it need not remain a valid reverse mark. The exact incident-edge update is

[
\delta_{P_J(T)}(K)
=
(\delta_T(K)\setminus\delta_T(J))
\cup
\bigl(\{e_J\}\cap\delta_{P_J(T)}(K)\bigr).
]

Equivalently, because e_J is a single restored edge disjoint from J, its contribution is present precisely when e_J meets K. To test whether K is still a guarded reverse mark, one must additionally find two distinct surviving old endpoints outside K and verify the full four-port induced pattern, positive overlap, no-reinsertion, and exact incidence equality in P_J(T).

This is the useful distinction:

- disjointness J∩K=empty preserves the *pair* K;
- it does not by itself preserve K's switch witness;
- a second inverse exists only if the full guarded inverse test succeeds in the parent tree.

The branching five-port example in the preceding census illustrates this distinction: a disjoint pair can remain after the first inverse, while no second four-distinct-port reverse operation exists because only three ports remain.

## 4. Sufficient local commutation criterion

Let X_J=J union endpoints(e_J) and X_K=K union endpoints(e_K) be the two four-port supports. Suppose

[
J\cap X_K=\varnothing,\qquad e_J\notin E(T[X_K]),
]
[
K\cap X_J=\varnothing,\qquad e_K\notin E(T[X_J]).
	ag{LC}
]

Then the two inverse operations are locally independent: deleting the J-incident switch edges and restoring e_J does not alter the K-marked four-port tree or its incidence guard, and symmetrically for K. The two deletions remove disjoint endpoint pairs, and the two restored edges survive both operations. Therefore

[
P_K(P_J(T))=P_J(P_K(T))
]

after the natural restriction to V\(J\cup K\).

This is a **sufficient**, not necessary, criterion. Failure of (LC) does not prove noncommutation; it means the two inverse tests must be checked directly. Nor does (LC) establish canonical compatibility: after either inverse, the canonical leaf of the resulting parent source may differ from the other marked interval.

## 5. Canonical eligibility is a separate test

The repository's canonical leaf is not an arbitrary or inferred ordering. In
`verify_pf_i16_source_dependent_leaf_peeling.py`, `canonical_leaf(intervals,tau)`:

1. computes degrees in the overlap spanning tree;
2. excludes the root interval containing port 1;
3. selects the lexicographically least interval among the remaining leaves.

For a parent source p, the retained parent target condition in the multivalued-pi verifier is exactly that P_J(T) belong to the parent source's `candidate_outputs(..., forced_last=canonical_leaf(...))` set.

Consequently, even when (LC) holds and the two local inverses commute as port trees, the canonical parent-neighborhood conditions

[
P_J(T)\in C_{\rm can}(p_J),\qquad
P_K(T)\in C_{\rm can}(p_K)
]

must still be checked independently. Local commutation is not a canonical diamond theorem.

## 6. What this lemma contributes to mixed-fiber Hall

For a target T, a fiber F=(p,J) is incident exactly when J is a valid guarded reverse mark and P_J(T) belongs to C_can(p). The fixed-mark inverse is unique, so the target-congestion identity remains

[
L(T)=
\sum_{J\in\mathcal J(T)}
\sum_{p:\,P_J(T)\in C_{\rm can}(p)}
\lambda((p,J),T).
]

The local results above provide:

- an exact geometric restriction on each J;
- a unique parent target for fixed (T,J);
- a test for whether a second mark survives after one inverse;
- a sufficient condition for two inverse operations to commute.

They do **not** bound the number or total demand of canonical parent centers p for a fixed mark, nor the aggregate contribution of different marks J at one target. In particular, they do not prove the target capacity-one estimate or mixed-fiber Hall.

## 7. Next proof obligation

The next structural task is to classify *pairs of simultaneously eligible fibers*, not merely pairs of locally valid marks. For each target T and two distinct incident fibers (p,J),(q,K):

1. classify J∩K and the support interactions X_J,X_K;
2. determine whether both inverse operations exist and whether (LC) holds;
3. compute both parent sources and their actual canonical leaves;
4. test whether the opposite mark is the canonical leaf after the first projection (the restricted canonical-diamond case);
5. record the split demands δ(p,J), δ(q,K) and whether their target incidences can be charged disjointly.

Only after this pair classification should one attempt a higher-order overlap/expansion inequality. Pairwise commutation alone is not enough for arbitrary-family Hall, because pairwise compatible supports do not imply a capacity-one allocation for a family of fibers.

No all-orders mixed-fiber Hall theorem or unconditional weighted one-link inequality is claimed.
