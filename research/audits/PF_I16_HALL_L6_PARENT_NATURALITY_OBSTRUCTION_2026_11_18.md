# PF-I16 — L6 parent-naturality check: first obstruction

**Date:** 18 November 2026  
**Branch:** \`research/pf-i16-z5-incidence-lift-2026-11-18\`  
**Status:** L6 fails for the frozen rank-indexed port/edge assignment. The obstruction is combinatorial and occurs before face-support deletion or collapse is reached.

## 1. Frozen rule being tested

The L1–L3 assignment maps the lexicographically sorted matching intervals
\[
I_1<I_2<\cdots<I_s
\]
to the frozen, pairwise vertex-disjoint target edges
\[
e_1,e_2,\ldots,e_s.
\]
Thus the \(i\)-th interval's lower and upper ports map to the ordered endpoints of \(e_i\).

L6 requires that, after deleting any eligible non-root leaf interval and order-compressing the retained ports, the parent lift agree with the child lift on every retained port. Under the frozen rule, deleting interval \(I_m\) shifts every later retained interval down one rank. Its inherited target edge is \(e_i\), while the canonical parent assignment gives it \(e_{i-1}\).

Since the frozen edges are distinct, this is an immediate failure of parent naturality whenever a marked interval precedes a retained interval.

## 2. Exact same-parent, two-mark obstruction

Take
\[
P_6=(1<2<3<4<5<6),
\qquad
M=\{I_1=[1,4], I_2=[2,5], I_3=[3,6]\},
\]
with selected overlap tree
\[
\tau=\{I_1I_2,I_1I_3\}.
\]
The full overlap graph is the triangle. The root is \(I_1\); both \(I_2\) and \(I_3\) are eligible non-root leaves.

**Delete \(I_2=[2,5]\).** The retained ports are \(1,3,4,6\), which compress to \(1,2,3,4\). The parent intervals are
\[
I'_1=[1,3],\qquad I'_2=[2,4],
\]
with the one-edge parent tree \(I'_1I'_2\). The retained child interval \(I_3\), which was assigned \(e_3\), becomes parent interval \(I'_2\). Naturality therefore requires parent interval \(I'_2\) to use \(e_3\).

**Delete \(I_3=[3,6]\).** The retained ports are \(1,2,4,5\), again compressing to \(1,2,3,4\). The parent intervals and parent tree are exactly the same:
\[
M'=\{[1,3],[2,4]\},\qquad \tau'=\{I'_1I'_2\}.
\]
Now retained child interval \(I_2\), which was assigned \(e_2\), becomes parent interval \(I'_2\). Naturality requires the same parent interval \(I'_2\) to use \(e_2\).

Consequently the **same parent source** requires its second interval to map to both \(e_2\) and \(e_3\). Since \(e_2\ne e_3\), no single parent port map can satisfy both marked parent projections while retaining the frozen child assignments.

This is stronger than a single rank-shift example: it rules out resolving the issue merely by choosing a different parent map separately for each deletion. The two eligible marks lead to the same parent source with incompatible inherited maps.

## 3. Exhaustive order-six count

The verifier reuses the canonical source exporter and checks all order-six sources and all eligible marks:

| Quantity | Count |
|---|---:|
| Hall sources at \(n=6\) | 22 |
| Eligible non-root leaf marks | 30 |
| Marked deletions that shift at least one retained interval's rank | 14 |
| Distinct parent structures | 2 |
| Parent structures with conflicting inherited edge maps | 2 |

Thus 14 of the 30 marked projections already violate the frozen rank-indexed parent commutation. Both parent structures that occur in the finite order-six enumeration have multiple, incompatible inherited edge maps across their child/mark origins.

The exact checker is:
\`research/scripts/verify_pf_i16_hall_l6_rank_map_obstruction.py\`.

It uses only the ordered matching intervals, selected spanning trees, eligible marks, and parent compression records. No geometry, Hall loads, deficiency, flow, congestion, or observer data enters the check.

## 4. L6 verdict and scope

**L6 does not pass for the current frozen lift.** The obstruction is at the port-to-edge map:
\[
\Phi_{\mathrm{parent}}(\bar p)\ne
\Phi_{\mathrm{child}}(p)
\]
for retained ports in the rank-shifting cases, and the explicit two-mark example forces incompatible values for the same parent interval.

It is therefore premature to report support-exclusive face deletion or free-edge collapse as passed. Those tests presuppose a commuting retained-port map. The existing L4–L5 supports may still be geometrically meaningful, but they cannot repair a mismatch between distinct matched basis edges.

## 5. Principled repair paths (not applied)

Two mathematically distinct redesigns remain possible:

1. **Parent-contextual lifts / a coherent diagram.** Allow the parent lift to depend on the marked embedding, then require coherence when two marks produce the same parent. The explicit two-mark witness shows that this requires changing the edge assignment or enlarging the target motif; simply making the parent map mark-dependent while keeping \(e_i\) fixed is insufficient.
2. **Stable interval identities before quotienting.** Enrich the Hall source with persistent interval identities or an ancestry structure and assign target edges by those identities rather than current lexicographic rank. This changes the source category and must be specified independently of Hall outcomes. It must also resolve the fact that the same un-enriched parent source can arise with two distinct inherited identities.

A further possibility is to weaken L6 to naturality only after forgetting the individual matched-edge labels, but that abandons the present L2-preserving parent morphism and would need a newly stated axiom. None of these repairs is silently adopted here.

## 6. Next work

The next step should be a redesign decision before further collapse enumeration: choose whether the source object is to retain ancestry/marked-embedding data, or whether L6 should be weakened to a coarser support-level statement. Only after that choice should we rerun support-exclusive deletion, relative free-edge collapses, and retained-incidence preservation. This failure is a geometric-lift obstruction, **not** a counterexample to the Hall inequality.


## 7. Status after the revised hierarchy

The strict labelled-edge L6 requirement documented above remains **rejected for this frozen rank-indexed lift**. It is not silently reclassified as a pass.

The working hierarchy has now replaced it with L6c, coarse support naturality. The finite n=6 to n=4 test checks all 30 eligible marked projections in both Ngrid=7 target domains, including relative free-cell collapses, support/intersection contractibility, and coherence for both parent structures. That separate result is recorded in:

research/audits/PF_I16_HALL_L6C_COARSE_SUPPORT_NATURALITY_2026_11_18.md

L6c does not preserve the identity of each inherited matched basis edge. It preserves the retained support intersection diagram up to simple-homotopy equivalence. The strict L6 obstruction above remains useful as the reason for making that explicit change.
