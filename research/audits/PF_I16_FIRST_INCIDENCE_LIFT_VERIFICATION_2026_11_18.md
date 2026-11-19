# PF-I16 — First verification pass for the marked incidence lift

**Date:** 18 November 2026  
**Branch:** `research/pf-i16-z5-incidence-lift-2026-11-18`  
**Status:** source conventions verified; Hall enumerator cross-check passed at n=4,6; finite lift feasibility not yet decidable from L1–L8 as presently specified.

## 1. Source convention fixed

The target chosen for this pass is the PF-I9 direct \\mathbb Z^5 cut-and-project construction, not the PF-I2 finite pentagrid surrogate and not the later Phase III construction with its different phason convention.

The PF-I9 direct verifier uses
- \\(e_j^\\perp=(\\cos(4\\pi j/5),\\sin(4\\pi j/5))\\);
- integer height \\(h=\\sum_j K_j\\in\\{1,2,3,4\\}\\);
- source phason
  \\[\\gamma=(-0.4207319701594539,-0.27446760021748134,0.3358983848622447,0.41036598507972605,-0.05106479956503551),\\]
  whose coordinates sum to zero up to floating-point roundoff;
- strict relative-interior vertex-window membership in the projected hypersimplex slice \\(W_h\\);
- strict relative-interior face-triangle membership in \\(T_{jk,h}\\), for \\(h=1,2\\).

The face test is independent and stricter than vertex acceptance. In the executable it is implemented by half-space equations for the convex hull of projected 0/1 vertices of the appropriate hypersimplex or three-coordinate face slice, with a strict \\(10^{-9}\\) margin. A vertex-only acceptance test is not a valid face enumerator.

The PF-I9 direct generator performs accepted-label BFS from finite seeds, then enumerates basis-square faces and checks the face triangle. Its BFS has a caller-specified radial collar. This is a finite patch generator, not an enumeration of the entire infinite accepted complex.

## 2. Hall source cross-check

I independently reimplemented the source definitions for the small orders:
- perfect matchings of ordered ports;
- strict interval overlap \\(\\max(a_i,a_j)<\\min(b_i,b_j)\\);
- spanning trees of the full overlap graph;
- non-root degree-one intervals as eligible reverse marks.

Results:

| Order | Hall sources | Eligible reverse marks |
|---:|---:|---:|
| n=4 | 2 | 2 |
| n=6 | 22 | 30 |

These agree with the existing repository's recorded source counts (2 and 22). The n=6 example from the ordered-structure note is a member of this independently reproduced source set.

This check verifies the Hall combinatorial source enumeration only. It does not construct any \\(\\Phi,\\epsilon,\\kappa\\).

## 3. What can and cannot yet be decided

The geometry formulas for L3 can now be implemented without substituting a different phason or confusing vertex windows with face triangles. However, the proposed lift problem is not yet a finite constraint problem, for three independent reasons:

1. **No finite target domain is specified.** The PF-I9 accepted complex is infinite. The existing direct generator requires a radial cutoff/collar, but L1–L8 do not prescribe one, nor do they prescribe a translation quotient or a finite search radius. An arbitrary cutoff could manufacture a false infeasibility result.
2. **The interval support variables are not finitely encoded.** L4 says each interval maps to a connected face-supported subcomplex with an ordered boundary trace, but does not bound its face count or specify whether the boundary trace is a simple cycle, a walk, a chain, or a marked path. Without this, the search space is unbounded even after choosing a finite target patch.
3. **L5/L6 lack an operational incidence rule.** “Shared-incidence witness” is allowed to be a vertex, edge path, or face, but no map is specified from the combinatorial overlap witness to the geometric incidence. “Remove support exclusive to the deleted leaf” also needs an exact support-difference/collapse rule. Thus parent naturality cannot yet be machine-checked uniquely.

These are specification gaps, not mathematical obstructions and not counterexamples to the existence of a lift.

## 4. Immediate correction to the solver plan

Before running a feasibility solver, freeze the following additional finite conventions:

- a declared finite accepted target patch (or a translation-normalized finite search theorem);
- a maximum support size, or a proof-derived bound, for each interval's face subcomplex;
- a precise boundary-trace type and its orientation/order map to Hall ports;
- a typed overlap-witness rule for each Hall overlap edge;
- a deterministic support deletion/collapse operator for every eligible reverse mark.

The bounds must be declared as part of the candidate lift class, not tuned after seeing Hall or observer outcomes. Run a hierarchy of increasing target patches and support bounds; report “not found within bound” separately from a certified global obstruction. A global nonexistence result requires a proof that the chosen finite reduction is exhaustive.

## 5. Verification status

- Hall source enumeration n=4,6: **PASS** (2 and 22 sources; 2 and 30 eligible marks).
- PF-I9 vertex-window and face-triangle formulas: **source implementation inspected**.
- Source phason: **recovered exactly from PF-I9 comparison evidence**.
- L1–L8 finite feasibility: **BLOCKED by under-specification**, not failed.
- Any actual \\(\\mathbb Z^5\\) marked incidence lift: **not yet constructed**.
- Parent naturality, observer phases, and Hall relevance: **not yet tested**.

No Hall loads, target congestion, or helical phase data enter this verification pass.
