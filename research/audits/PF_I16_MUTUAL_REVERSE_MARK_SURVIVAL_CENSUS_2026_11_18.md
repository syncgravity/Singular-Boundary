# PF-I16: mutual survival of guarded reverse marks — exhaustive small-tree census

Date: 2026-11-18

Status: **finite target-tree evidence through seven ports; mutual-survival commutation remains a conjecture, not an all-orders lemma.**

Verifier: `research/verification/verify_pf_i16_reverse_mark_pair_census.py`.

## 1. Exact object tested

A target is a labelled spanning tree T on [n]. A proposed reverse mark J={a,b} is accepted only when there are two distinct old endpoints u,v outside J such that, on the ordered four-port set X=J union {u,v}:

1. the induced target tree T[X] is exactly one of
   `S0={x1x2,x2x3,x2x4}`,
   `S1={x1x2,x2x3,x3x4}`, or
   `S2={x1x3,x2x3,x3x4}`;
2. the full set of T-edges incident to either endpoint of J equals the corresponding local-pattern incidence set (no extra incident edge);
3. the complementary old edge uv is not in the local pattern (no reinsertion);
4. the open intervals uv and J have positive-length intersection.

For each fixed (T,J), the verifier asserts at most one witness pair and pattern. The inverse is
[
P_J(T)=T[V\setminus J]\cup\{uv\}.
]

This is the target-side guarded inverse only. There is no matching M, overlap tree tau, source fiber, canonical parent neighborhood, or split demand in this census.

## 2. Four-port rank census

Exhausting all six possible rank pairs J among x1<x2<x3<x4 gives exactly:

| Mark ranks | Old-edge ranks | Admissible local patterns |
|---|---|---|
| (1,3) | (2,4) | S1, S2 |
| (2,3) | (1,4) | S0, S1, S2 |
| (2,4) | (1,3) | S0, S1 |

The extreme adjacent pairs (1,2) and (3,4) fail positive interval overlap with their complementary old edge. The outer pair (1,4) is rejected by no-reinsertion: the complementary middle edge (2,3) belongs to all three local patterns.

This confirms the five-pair rank list in the crossing-template audit, with the additional useful information of exactly which patterns realize each pair.

## 3. Exhaustive labelled-tree pair census

The verifier enumerates every Prüfer code, hence every labelled spanning tree, for n=5,6,7. For every target it enumerates all guarded reverse marks and every unordered pair of them.

| n | Trees | Max marks on one target | Unordered mark pairs | Disjoint mark pairs | Second mark survives first inverse | Both directions survive | Double inverses commute |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 5 | 125 | 4 | 40 | 10 | 0 | 0 | 0 |
| 6 | 1,296 | 6 | 424 | 118 | 58 | 58 | 58 |
| 7 | 16,807 | 8 | 6,377 | 2,331 | 1,701 | 1,701 | 1,701 |

“Disjoint mark pair” means J∩K=empty. This is necessary for K to remain a two-endpoint mark after deleting J. For every such pair, the verifier tests K in P_J(T) and J in P_K(T) using the full guarded inverse conditions; it does not assume that the original old-edge witness survives. The second mark may acquire a different old-edge witness after the first inverse.

For every pair for which both directions survive, the verifier lifts the newly validated witnesses to the original labels, computes both two-step inverses, and asserts equality on the remaining n-4 vertices. All assertions pass for n≤7.

## 4. Support geometry of mutually surviving pairs

For each mutually surviving pair, let X_J and X_K be the two four-port supports, including each mark and its old endpoints. The observed support-intersection types are:

| n | (|X_J∩X_K|, |e_J∩K|, |e_K∩J|) | Count |
|---:|---:|---:|
| 6 | (2,1,1) | 58 |
| 7 | (2,1,1) | 812 |
| 7 | (1,0,0) | 889 |

Thus disjoint four-port supports are not necessary for mutual survival. The local sufficient criterion in the preceding commutation audit (disjoint supports) remains sufficient, but it is not a classification and is not necessary. In the (2,1,1) type, each support meets the other mark in one old endpoint. In the (1,0,0) type, the supports share one old endpoint and neither old edge meets the opposite mark.

## 5. Candidate mutual-survival commutation lemma

The finite data motivate the following precise conjecture.

**Conjecture (guarded mutual-survival diamond).** Let T be a port tree and let J,K be disjoint two-port marks, each a valid guarded reverse mark of T. If K is still a valid guarded reverse mark of P_J(T), and J is still a valid guarded reverse mark of P_K(T), then the two resulting double inverses agree:
[
P_{K}^{,J}(P_J(T))=P_{J}^{,K}(P_K(T)),
]
where the superscript records that the second inverse witness is revalidated in the first parent tree and need not equal its original witness.

The census is consistent with this conjecture through seven ports. It does not prove it for arbitrary n. A proof must use the exact full-incidence guard and the fact that each first inverse deletes its marked vertices and restores the unique complementary edge; it must not assume the two original four-port supports are disjoint.

## 6. What this does and does not contribute to Hall

If the conjectured diamond lemma holds, it gives a canonical way to identify the common twice-reversed parent target whenever two reverse marks mutually survive. This could help organize overlap classes of target incidences and prevent counting the same two-step inverse history twice.

It still does not establish:
- that the parent sources associated with the two marks are compatible;
- that either twice-reversed target belongs to the relevant canonical leaf-last neighborhood;
- that all mutually surviving marks form a globally coherent equivalence class;
- that the weighted fiber demands in such a class fit target capacity one;
- any arbitrary-family mixed-fiber Hall inequality.

In particular, local target-side commutation is not a substitute for the canonical source/fiber condition. The next proof step is to prove or refute the mutual-survival diamond conjecture abstractly, then separately test whether its common parent target is canonical for both source histories.

No all-orders Hall theorem or unconditional weighted one-link inequality is claimed.
