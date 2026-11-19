# PF-I16 — L7 order compatibility: scope refinement and finite checks

Date: 18 November 2026  
Branch: research/pf-i16-z5-incidence-lift-2026-11-18  
Scope: frozen Ngrid=7 L1-L5 support construction; Hall source orders n=4,6; all 30 eligible n=6 marked parent projections.

## 1. The order structure must be stated without inventing a target total order

The source ports have a canonical linear order. The accepted Penrose/Fibonacci target is a finite subcomplex of the projected Z^5 lattice. It has no canonical total order on its vertices supplied by the cut-and-project construction.

In particular, imposing lexicographic order on Z^5 labels would be an auxiliary convention, not an invariant of the physical projection or the accepted face complex. Imposing order by a chosen physical projection axis would introduce an extra direction and can change under rotation of the physical frame. Neither is part of the frozen lift.

Therefore L7 is split into two parts:

- **L7a — source-order naturality:** preserve the ordered list of intervals and the lower-to-upper orientation of each interval under parent deletion.
- **L7b — oriented boundary-order compatibility:** each interval support has an oriented boundary circle, with the distinguished matched edge appearing in the direction lower port to upper port; the overlap footprints on those circles must form compatible cyclically ordered data under parent restriction.

L7 does not require a global linear order on all target vertices. Such an order may only be added if a target-side order structure is independently motivated and fixed before testing.

## 2. L7a: finite source-order result

For every source record, intervals are sorted by their lower endpoints. Since the intervals are disjoint as matched pairs, their lower endpoints are distinct. For a marked deletion, the retained ports are listed in increasing order and compressed by the strictly increasing map
[
c_J:{1,ldots,n}\setminus{a_J,b_J}longrightarrow{1,ldots,n-2}.
]

For every retained interval (I_i=[a_i,b_i]), its image is
[
ar I_i=[c_J(a_i),c_J(b_i)].
]
Strict monotonicity gives
[
a_i<b_iimplies c_J(a_i)<c_J(b_i).
]
For two retained intervals with (a_i<a_k), one has
[
c_J(a_i)<c_J(a_k),
]
so their sorted order is unchanged. Thus the retained interval-index map is strictly increasing; it is not an arbitrary permutation.

The exporter `research/scripts/export_pf_i16_hall_source_records.py` records the retained-port list, the compression map, the parent intervals, and the parent tree for every mark. The finite n=6 enumeration has 30 eligible marked projections, and the parent checks recorded in the source audit passed for all 30.

**L7a verdict:** pass for all 30 finite marked projections, by the exact order-preserving compression rule. This is a source-order statement, not an assertion that `Phi` is monotone into an invented total order on Z^5.

## 3. Local oriented boundary trace

The frozen L4 support construction assigns each interval a connected union of one or two accepted rhombi. Its distinguished elementary edge occurs in exactly one selected face, so it is a boundary edge of the support. A one-rhombus support has a four-edge boundary cycle. Two distinct edge-adjacent rhombi form a disk with a six-edge boundary cycle in the tested local tiling patch.

For each interval, orient this boundary cycle so that the distinguished edge is traversed from `Phi(a_i)` to `Phi(b_i)`. The construction has not reversed any matched edge: all three frozen motif edges remain oriented (+e_j), and every source interval uses the lower endpoint as the tail and the upper endpoint as the head.

This establishes existence and direction of each individual oriented boundary trace. It does not yet establish the cyclic order of every overlap footprint relative to the distinguished edge, nor compatibility of those footprints between child and parent supports.

## 4. Why L7b remains a separate test

L6c deliberately forgets the identity and dimension of a shared cell. L7b must add order information without restoring the rejected strict edge-label naturality.

The proposed invariant is an **oriented boundary-incidence word** for each support family:

1. Mark the distinguished interval edge as a directed boundary 1-cell.
2. Mark the intersection of each pair of supports as a connected footprint on each oriented boundary cycle.
3. Record the cyclic order of footprint components and their endpoints relative to the distinguished directed edge.
4. Compare child-restricted and parent words up to orientation-preserving subdivision/collapse, preserving the cyclic order and marked direction but not the identity of target cells.
5. For parents reached through multiple marks, require the resulting ordered words to agree up to the same equivalence.

A shared face, edge, or vertex may have different cell dimension in child and parent; that difference is permitted by L6c. What L7b must preserve is the oriented cyclic order of the induced footprint, not its cell label.

The current L4-L5 audit gives the exact support assignments and witness types. The L6c audit gives all 30 deletion projections and the two-mark coherence example. Neither audit computes the full oriented boundary-incidence words. No L7b pass is claimed here.

## 5. Explicit two-mark check: what is already established

For the source
[
M={[1,4],[2,5],[3,6]},qquad 	au={I_1I_2,I_1I_3},
]
deleting (I_2) or (I_3) yields the same ordered parent intervals ([1,3]<[2,4]). The retained child supports in both cases are two-rhombus disks. Their distinguished edges remain directed lower-to-upper, and their shared-face footprint lies in the non-distinguished face of each support. The parent support diagram has the same interval order and the same coarse disk/intersection incidence.

Thus the explicit obstruction to strict edge-label naturality does not itself obstruct L7a or the local oriented-boundary condition. A full L7b comparison still requires the boundary-incidence-word computation.

## 6. Status

| Condition | Status |
|---|---|
| L7a: retained interval order under parent compression | **Pass**, all 30 marked projections |
| Individual interval boundary orientation | **Pass**, frozen L4 construction |
| L7b: cyclic order of all overlap footprints | **Open; not yet computed** |
| L7b: child-parent ordered-word equivalence | **Open; not yet computed** |
| L7b: parent coherence across all incoming marks | **Open; not yet computed** |

The correct current conclusion is a partial L7 result, not a blanket L7 pass or failure.

## 7. Next computation

Implement a boundary-incidence-word extractor using the exact support assignments from `verify_pf_i16_hall_l45_bounded_support.py`. For each one- or two-rhombus support, extract its boundary cycle, orient it by the distinguished matched edge, and mark every pairwise support-intersection footprint. Then compare child-restricted and parent words up to orientation-preserving subdivision/collapse for all 30 marked projections in both target domains.

Do not introduce lexicographic Z^5 order, a fitted physical axis, observer phases, or any Hall-dependent tie-break. If a footprint is disconnected or has incompatible cyclic order, report the first explicit obstruction rather than repairing it by reversing a boundary orientation.
