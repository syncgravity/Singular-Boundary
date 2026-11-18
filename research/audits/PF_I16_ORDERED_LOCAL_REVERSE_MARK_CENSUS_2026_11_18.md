# PF-I16: ordered local reverse-mark census for the two overlap shapes

Date: 2026-11-18

Branch: `research/pf-i16-admissible-exchange-2026-11-16`

Parent head inspected before this write: `375ddd99a43ac1301004d1fb30e4795f76dab814`.

Status: **exact finite local census under the recorded guarded-switch definition; not a canonical-eligibility or Hall theorem.**

## 1. Controlling semantics

Use the guarded transition and inverse conditions in:

- `PF_I16_GUARDED_SWITCH_REVALIDATION_2026_11_16.md`;
- `PF_I16_REVERSE_SWITCH_TRANSITION_2026_11_16.md`;
- `PF_I16_CROSSING_REVERSE_MARK_TEMPLATES_2026_11_17.md`.

For sorted distinct endpoints (x_1<x_2<x_3<x_4), the only permitted local inserted trees are

[
S_0={x_1x_2,x_2x_3,x_2x_4},quad
S_1={x_1x_2,x_2x_3,x_3x_4},quad
S_2={x_1x_3,x_2x_3,x_3x_4}.
]

A reverse mark (J) and replaced edge (e) are tested by requiring: four distinct endpoints; positive interval overlap; (e\notin S_j) (no reinsertion); (S_j\subseteq E(T)); and exact incidence equality
[
\delta_T(J)=\delta_{S_j}(J).
]
This census uses the full inverse-incidence test, not a visual degree guess. The two possible orders of interval endpoints relative to the old edge are not assumed to be alternating: containment is allowed by the interval-overlap definition.

## 2. Exhaustive five-port census

For each displayed five-vertex tree below, enumerate all (5!=120) assignments of distinct port labels, every candidate two-element interval (J), every disjoint candidate old edge (e), and all three local patterns (S_0,S_1,S_2). Retain exactly the tuples satisfying the guarded inverse tests above. This is a finite exhaustive local census; it is not the repository's full source/fiber/canonical-neighborhood verifier.

### A. Path shape

Tree edges:
[
\ell u,\quad ub,\quad bc,\quad cv.
]
Displayed candidate marks:
[
J_I=\{b,c\},\qquad J_{II}=\{\ell,b\}.
]

There are exactly **two** port labelings (a labeling and its order reversal) for which both displayed marks are valid simultaneously. For representative labels
[
(\ell,u,b,c,v)=(1,2,3,4,5),
]
the complete valid reverse-mark list is:

| Mark (J) | Replaced edge (e) | Pattern | Signature |
|---|---|---|---|
| ({\ell,b}) | ({u,c}) | (S_1) | Type II, endpoint degrees (1,2) |
| ({u,b}) | ({\ell,c}) | (S_1) | Type I, endpoint degrees (2,2) |
| ({b,c}) | ({u,v}) | (S_1) | Type I, endpoint degrees (2,2) |
| ({b,v}) | ({u,c}) | (S_1) | Type II, endpoint degrees (1,2) |

Every valid mark contains (b). Therefore after reversing any one of these marks, every other mark in this list has a deleted endpoint. There is no second reverse step using another mark from the original target.

### B. Branching shape

Tree edges:
[
\ell b,\quad bc,\quad be,\quad cv.
]
Displayed candidate marks:
[
J_I=\{\ell,b\},\qquad J_{II}=\{\ell,c\}.
]

There are exactly **four** port labelings for which both displayed marks are valid simultaneously (two mirror pairs). For representative labels
[
(\ell,b,c,e,v)=(1,3,4,2,5),
]
the complete valid reverse-mark list is:

| Mark (J) | Replaced edge (e) | Pattern | Signature |
|---|---|---|---|
| ({\ell,b}) | ({c,e}) | (S_2) | Type I, endpoint degrees (1,3) |
| ({\ell,c}) | ({b,v}) | (S_1) | Type II, endpoint degrees (1,2) |
| ({b,e}) | ({\ell,c}) | (S_2) | Type I, endpoint degrees (1,3) |
| ({c,e}) | ({b,v}) | (S_1) | Type II, endpoint degrees (1,2) |

Here the earlier conversational explanation needs a precise correction. After reversing ({\ell,b}), the mark ({c,e}) is disjoint from the deleted pair, so it is not accurate to say that every other displayed mark itself contains a deleted endpoint. But the parent has only three remaining ports. A guarded reverse switch requires four distinct ports (the two marked endpoints and the two endpoints of a disjoint replaced edge), so no second reverse step is possible. The same cardinality obstruction applies after reversing ({\ell,c}).

## 3. Corrected disposition of the prior conversational claims

- The complete lists stated for the two representative labelings are confirmed by the exhaustive local census above.
- The path case has the stronger property that all valid marks share (b).
- The branching case does **not** have that property: a disjoint mark remains as a pair after one inverse, but cannot form a second guarded reverse switch on a three-port parent.
- Thus the phrase “no third mark survives” should be replaced by the exact statement: **no second guarded reverse operation is possible after the first inverse**, for these five-port configurations. In the branching case this is because only three ports remain, not because every other mark contains a deleted endpoint.
- The census is conditional on the specified five-vertex tree and port labeling. It does not assert that the displayed pair is valid for arbitrary labelings; the simultaneous-validity counts are 2 and 4, respectively.

## 4. Explicit proof boundary

This local census does not test or establish
[
P_J(T)\in C_{\rm can}(p).
]
It does not enumerate parent sources (p), fiber multiplicities, split demands (delta(F)), or neighborhoods away from the displayed target. It therefore gives no mixed-fiber Hall expansion estimate and no all-orders Hall result.

The next required step remains the target-side census with actual source/fiber data: for each valid ((T,J)), compute (P_J(T)), enumerate every canonical parent center (p) with (P_J(T)\in C_{\rm can}(p)), retain (delta(p,J)), and measure target congestion and neighborhood expansion. The existing target-congestion identity (RC) remains the controlling formula.

No weighted one-link inequality is claimed unconditionally.
