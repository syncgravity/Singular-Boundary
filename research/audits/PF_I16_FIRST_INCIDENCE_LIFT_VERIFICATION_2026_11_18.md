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


---

## 6. Correction: finite accepted target domains already exist

**This section supersedes the “no finite target domain is specified” conclusion in §3.1 and the corresponding PF-I9-only framing in §1.** That conclusion was too broad. Earlier PF-I11/PF-I16 work supplies two independently defined finite target domains. The remaining issue is not absence of finite geometry; it is the missing Hall-to-target association and the operational semantics of L4–L6.

### 6.1 Original-source finite complex (PF-I16)

The PF-I16 source replay `research/scripts/verify_pf_i16_authentic_source_three_face.py` independently reimplements the indexed original `paper6_extend_local.py` selection and the PF-I11 strict face-triangle test. At Ngrid=7 it reports:

- 1,550 selected vertices;
- 3,017 elementary edges;
- 1,468 accepted rhombi;
- at most two accepted faces incident to any original link in this crop.

The verifier explicitly states that the private original source bytes were **not** directly executed; this is an independent reimplementation, not byte-identical source replay. Its eight finite population counts match the recorded values, but that provenance distinction remains material.

### 6.2 Completed-window core (PF-I11)

The independent completed-window construction is implemented by `research/scripts/verify_pf_i11_completed_core.py`, using the direct accepted-window generator and an explicit collar. Its Ngrid=7 evidence record reports:

- 1,432 vertices;
- 2,761 edges;
- 1,330 accepted rhombi;
- one connected component;
- all 1,330 faces peel by free-edge collapses.

This is deliberately **not** the original source-retained population: the same record reports 1,550 source-retained vertices. The completed-window core is a separate control domain, not a replacement for the original-source complex.

### 6.3 Geometry interface already available

`research/scripts/verify_pf_i11_intrinsic_su2.py` supplies the reusable `Complex` representation and `assemble_complex(labels, gamma, source_Ngrid)` constructor. It stores:
- accepted integer labels;
- elementary basis edges;
- accepted rhombi and direction-pair families;
- oriented face-edge incidence indices and signs;
- face heights, phason, and source Ngrid.

Its face constructor checks strict internal triangle membership independently of the four-corner test. The original-source constructor `source_complex` requires the private SHA-pinned source file; the public PF-I16 replay is an independent alternative with explicitly weaker provenance.

### 6.4 Phason separation

Do not merge the PF-I9 direct-construction phason with the PF-I16/PF-I11 generic source phason. The first verification pass's §1 describes PF-I9's gamma and remains a record of that distinct construction. The PF-I16 original-source replay instead uses
[
\gamma_j=((j\sqrt2+j^2\sqrt3)\bmod 1),\quad
\gamma\leftarrow\gamma-\operatorname{mean}(\gamma),\quad
\gamma_4=-\sum_{j=0}^3\gamma_j.
]
The completed-window core uses the generic source gamma imported from its source module. Every run must label the construction and gamma convention in its output.

## 7. Corrected finite verification plan

The first two test domains are now fixed by existing research, not invented cutoffs:

| Domain | Ngrid=7 | Provenance / interpretation |
|---|---:|---|
| PF-I16 original-source replay | V=1,550; E=3,017; F=1,468 | Independent reimplementation of indexed private source; original bytes not executed |
| PF-I11 completed-window core | V=1,432; E=2,761; F=1,330 | Direct full-window incident-star core; source-retained population remains separate |

The initial Hall test orders remain n=4 and n=6. The Hall source records are to be enumerated independently (2 and 22 sources; 2 and 30 eligible marks respectively). No Hall load, deficiency, allocation, or observer phase is an input to target construction or lift search.

Before running the constraint checker, the candidate encoding must be declared as a **bounded model class**, not silently treated as the unique meaning of L4–L6:

1. **Port labels and matching edges:** retain L1 and L2 literally. Each port receives a distinct accepted label; each matched pair maps to one actual accepted elementary edge with signed unit increment.
2. **Interval support:** candidate support is a connected set of accepted rhombi in the chosen finite complex. Enumerate support cardinalities in an announced ladder (start at one face, then increase); the finite complex's total face count is an absolute finite ceiling for that crop, not a universal bound.
3. **Boundary trace variants:** test separately (A) an oriented simple boundary cycle of the support, and (B) an oriented boundary walk with repeated vertices/edges permitted. In either variant, the trace is a target-side ordered object; do not equate its length with the number of Hall ports without an explicit port-to-trace rule. Internal Hall ports must remain represented in the support data.
4. **Overlap witness variants:** for each strict-overlap edge in the full interval graph, record separately whether the two supports intersect in a vertex, an edge, or a face. The selected tree edges are marked among these witnesses; non-tree overlap edges remain present and checked.
5. **Parent naturality:** implement deletion only after a support-difference rule is fixed. Candidate rule: remove the marked leaf's support-exclusive faces, then perform only free-edge elementary collapses; reject if a retained port, matched edge, interval support, or required overlap witness is lost. Compare this with independently lifting the compressed parent. Keep each eligible mark as a distinct state even when parent projections coincide.
6. **Independence:** generate and freeze candidate lifts without inspecting Hall neighborhood sizes, reverse-degree loads, flow solutions, or perpendicular observer phases.

A result is scoped to its declared domain, support bound, and trace/witness variant. “No lift found” means no lift in that bounded model class; it is not a global nonexistence theorem. A global obstruction requires an exhaustive reduction proof. If a variant is infeasible, retain the minimal conflicting constraints and report the first failed axiom.

## 8. Updated status

- Existing finite target domains: **AVAILABLE** (two distinct Ngrid=7 domains above).
- Reusable accepted-complex incidence interface: **AVAILABLE** (`Complex`, `assemble_complex`).
- Hall source counts n=4,6: **PASS**, as recorded in §2.
- Actual `Phi, epsilon, kappa` correspondence: **NOT YET CONSTRUCTED**.
- L4 boundary-trace and L5/L6 overlap/deletion semantics: **candidate variants specified above; not yet selected or executed**.
- Finite lift feasibility: **NOT YET RUN**. The previous “no finite target domain” blocker is withdrawn; the remaining blocker is the explicit candidate encoding and the Hall-to-target constraint implementation.
- All-orders Hall theorem: **OPEN**. No finite geometric lift result alone proves it.


---

## 9. Next check executed: canonical Hall source records and marked-parent audit

Added `research/scripts/export_pf_i16_hall_source_records.py`. It independently enumerates:
- every perfect matching of the ordered ports;
- the strict-interior interval-overlap graph;
- every spanning tree of that graph;
- the root interval and every eligible non-root leaf;
- each marked parent after endpoint deletion and order compression, including its full overlap graph and induced parent tree.

The exporter now asserts for **every** eligible mark that deleting the non-root leaf leaves a valid spanning tree of the parent's full strict-overlap graph. It does not use any target geometry, Hall load, deficiency, flow, or observer coordinate.

Independent execution of the same enumeration and parent checks gives:

| Order | Sources | Eligible marks | Marks/source histogram | Parent-tree checks |
|---:|---:|---:|---|---:|
| 4 | 2 | 2 | 1: 2 | 2/2 pass |
| 6 | 22 | 30 | 1: 14; 2: 8 | 30/30 pass |

This is a source-side verification, not a geometric lift. It confirms the combinatorial parent operation is well-defined for every enumerated marked source at these two orders. In particular, the six-port example in §2 is included in the enumeration; all marks are retained, including distinct marks even if parent projections happen to coincide.

### Status after this check

- Canonical source-record exporter: **ADDED**.
- n=4/n=6 source counts: **PASS** (2 and 22).
- Eligible reverse marks: **PASS** (2 and 30).
- Parent endpoint deletion and order compression: **PASS** for all 32 marks.
- Parent overlap-tree validity: **PASS** for all 32 marks.
- `Phi, epsilon, kappa` construction: **NOT YET TESTED**.
- L1–L3 target assignment and L4–L6 support/overlap naturality: **NEXT**.

The next geometric check should begin with L1–L3 on each of the two existing Ngrid=7 target domains, retaining the original-source replay and completed-window core as separate cases. It must produce explicit target labels and signed basis edges, not infer feasibility from the large V/E/F counts alone.
