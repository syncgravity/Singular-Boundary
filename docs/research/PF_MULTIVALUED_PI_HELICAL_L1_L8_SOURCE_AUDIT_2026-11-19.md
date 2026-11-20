# PF-I16 multivalued-π, incidence-lift L1–L8, and helical-observer source audit

**Date:** 2026-11-19  
**Purpose:** source reconciliation of research notes, verifier code, finite certificates, branch custody, and theorem status.

## Executive disposition

The repository contains substantial advances, but they are not all-orders closures:

1. Multivalued-π has finite Hall/matching evidence at n=6,8,10, including a successful n=10 max-flow certificate and replay. The all-orders Hall inequality and weighted one-link inequality remain open.
2. A detailed finite incidence-lift candidate has L1–L7 evidence for n=4,6 on two separate Ngrid=7 target domains. The later alternative triple passes finite L6c/L7b tests. The records explicitly state that these calculations were run in a research session and the committed verifiers were not clean-checkout executed. They are not all-orders theorems.
3. The earlier frozen support family fails L7b; the alternative triple is a later replacement candidate. Both records are valid within their own frozen assumptions.
4. Source-side deletion diamonds are proved at all finite orders. A separate canonical-sibling guarded port-tree diamond is also recorded as an all-finite-order theorem, but the stronger canonical-parent conclusion is false at n=10.
5. Accepted-face geometric L8 remains open.
6. The helical observer is supported as a kinematic sampling construction, not as a unique physical 3D helix, physical clock, real Lorentz C5 action, KK mass spectrum, or interacting PF Yang–Mills dynamics.

## 1. Custody and provenance

### Mainline sources

- `docs/research/Z5_REAL_STRUCTURE_AND_HELICAL_OBSERVER_SOURCE_AUDIT_2026-11-11.md` (blob SHA `566f7401d658674696594c415a90897ec07630df`).
- `research/geometry/PF_PAPER3_HELICAL_OBSERVER_PRIMARY_HYPOTHESIS_2026_11_07.md` (blob SHA `2fcbb7ccc8402fac2c7cbf6f9777f18205814a05`).
- `research/geometry/PF_CONCEPTUAL_3D_CONWAY_HELICAL_RECONSTRUCTION_2026_11_07.md` (blob SHA `a172d430d79817336c11acc4db70445443deca44`).
- `research/geometry/PF_HELICAL_OBSERVER_COVARIANCE_ALIAS_2026_11_07.md` (blob SHA `9755c3d6f39c8df737c0c75aed83977e6ad9d2b9`).
- `research/geometry/PF_HELICAL_HARMONIC_TRIAD_AND_INTERACTING_NULL_2026_11_07.md` (blob SHA `b9ab62826f8913669973d9af93d66f1e839e6154`).

### Incidence-lift branch

The L1–L7 finite-lift records and scripts are on `research/pf-i16-z5-incidence-lift-2026-11-18`, head `d22c033211a3206024cdab4e8c4a85fa3e97172b`. No open PR with that head branch was found at audit time. Primary records:
- `PF_I16_FIRST_INCIDENCE_LIFT_VERIFICATION_2026_11_18.md`
- `PF_I16_HALL_L123_MOTIF_LIFT_CHECK_2026_11_18.md`
- `PF_I16_HALL_L45_BOUNDED_SUPPORT_2026_11_18.md`
- `PF_I16_HALL_L6_PARENT_NATURALITY_OBSTRUCTION_2026_11_18.md`
- `PF_I16_HALL_L6C_COARSE_SUPPORT_NATURALITY_2026_11_18.md`
- `PF_I16_HALL_L7B_BOUNDARY_ORDER_TEST_2026_11_18.md`
- `PF_I16_HALL_L7B_LOCAL_MOTIF_OBSTRUCTION_2026_11_19.md`
- `PF_I16_HALL_ALTERNATIVE_TRIPLE_L6C_L7B_2026_11_19.md`
- `PF_I16_HALL_L7_L8_SOURCE_DELETION_DIAMOND_2026_11_19.md`
- `PF_I16_HALL_TO_PENROSE_FIBONACCI_INCIDENCE_LIFT_2026_11_18.md`

The records say the finite calculations were independently executed in-session; the repository scripts were committed and inspected but not run from a clean cloned checkout. The scripts are replay artifacts, not successful CI evidence.

### Multivalued-π branch

The Hall advances are on `research/pf-i16-direct-mixed-hall-2026-11-18`, head `72c7b0fdebd488a9a084667b8fe7ab2b4e464d65). Key records:
- `PF_I16_MULTIVALUED_PI_ALL_ORDERS_PROOF_PROGRAM_2026_11_16.md`
- `PF_I16_N10_MULTIVALUED_PI_MATCHING_CERTIFICATE_2026_11_17.md`
- `PF_I16_N10_SPLIT_DEMAND_FLOW_CERTIFICATE_REPLAY_2026_11_18.md`
- `PF_I16_N10_SPLIT_DEMAND_FLOW_CERTIFICATE_RESULT_2026_11_18.md`
- `PF_I16_CUT_CLASS_LOCAL_HALL_THEOREM_2026_11_17.md`
- `PF_I16_BLOCKWISE_SPLIT_DEMAND_HALL_REDUCTION_2026_11_17.md`
- `PF_I16_DISTINCT_PARENT_DIAMOND_THEOREM_2026_11_18.md`
- `PF_I16_HELICAL_REVERSE_MARK_BRIDGE_AUDIT_2026_11_18.md`

These are branch records and should not be described as mainline-merged evidence until selectively reconciled and reviewed.

## 2. Multivalued-π: established finite results and open theorem

The proof-program note defines a source (x=(M,\tau)), parent projections through eligible non-root leaves, and a multivalued restricted neighborhood (R_n(x)). The all-orders target is
\[
|N_{R_n}(A)|\ge |A|\quad\text{for every }A\subseteq X_n
\]
at every even order. The recorded down-set Hall argument would then yield the weighted one-link inequality.

Finite evidence:
- Restricting each child to its canonical leaf has a finite n=10 deficiency of 92. This rejects that restricted relation, not the multivalued relation.
- Allowing all eligible non-root leaves gives 31,744 child sources, 95,864 target trees, and a matching saturating all 31,744 sources.
- The n=10 matching certificate was independently replayed. Leaf and target are selected jointly by finite maximum matching; this is not a canonical or local all-orders selector. Parent-source/parent-target pairs can be reused by multiple child lifts.
- The corrected n=10 split-demand flow has 21,280 fibers, 95,864 eligible target vertices, 49,584 positive arcs, scaled demand=max flow=380,928, and maximum target load 12/12. Replay verifies fiber conservation, eligibility, capacity and total flow. It shares canonical source enumeration and switch/compression primitives, so it is independent of the flow algorithm/certificate serialization, not a wholly independent implementation of the relation.
- Successful workflow 44432123349 checked out commit `75141c303dfad6191c5a797c262b704a6049fe5a`; artifact ZIP SHA-256 `d23af0dcf97433db01d209f220c0cafd6baef08109dea9f11ae78757e577d096`. Earlier run 44426921009 failed in a post-flow diagnostic due to a missing `Counter` import; the corrected rerun is authoritative.
- The proof-program record also cites exact n=6 and n=8 split-demand flows. These remain finite-order results.

The missing theorem is a structural capacity-sensitive global exchange/augmentation principle controlling simultaneous collisions across leaves and parent fibers.

**Verdict:** finite multivalued-π Hall evidence at n=6,8,10; all-orders Hall and the weighted inequality remain open. This is distinct from the geometric incidence-lift program.

## 3. Incidence-lift L1–L7: exact scope

The lift is `L_n=(Phi_n, epsilon_n, kappa_n)`: ports map to accepted Z5 vertices, matched pairs to oriented elementary edges, intervals to connected face-supported subcomplexes with ordered boundary traces.

Two distinct Ngrid=7 targets must remain separate:
- PF-I16 original-source replay: V=1,550, E=3,017, F=1,468. It is an independent reimplementation of an indexed private source; original private bytes were not executed byte-identically.
- PF-I11 completed-window core: V=1,432, E=2,761, F=1,330. It is a separate completed-window core, not a replacement for the source-retained PF-I16 population. Its frozen vertex/face hashes are checked.

Both finite lift checks use the generic phason
\[
\gamma_j=((j\sqrt2+j^2\sqrt3)\bmod1),\quad
\gamma\leftarrow\gamma-\operatorname{mean}(\gamma),\quad
\gamma_4=-\sum_{j=0}^3\gamma_j.
\]
Do not substitute the distinct PF-I9 direct-construction phason in the initial verification note.

### L1–L3

For all 2 n=4 sources and 22 n=6 sources, in each target, the frozen three-edge motif passes:
- L1: port injectivity;
- L2: each matched pair is an actual signed elementary basis edge;
- L3: strict vertex-window and face-triangle acceptance.

The verifier explicitly does not claim interval supports, overlap witnesses, parent naturality, L7, L8, helical phases, or Hall.

### L4–L5

The bounded verifier uses connected one- or two-rhombus supports, with each distinguished matched edge on its support boundary. It checks the full interval-overlap graph, including non-tree edges, and requires non-overlapping pairs to have disjoint supports even at vertices. Across 24 n=4,6 source records it records 40 shared-face, 22 shared-edge, and 2 shared-vertex witnesses, with zero non-overlap pairs sharing incidence. Both targets select identical supports/witnesses in their common accepted-face population.

This is a finite support-family result, not a universal two-rhombus bound.

### Strict L6 versus L6c

Strict labelled-edge L6 fails for the frozen rank-indexed edge assignment: 14/30 n=6 marked projections shift a retained interval's rank, and both parent structures have incompatible inherited edge maps. The explicit two-mark example forces the same un-enriched parent source's second interval to inherit both e2 and e3.

The branch explicitly replaces strict L6 with L6c: forget individual shared-cell identity/dimension, but preserve the coarse intersection diagram (including empty/nonempty and simple-homotopy type), contractibility of retained supports/intersections/union, relative free-face deletion collapses, and coherence across all marked projections to each parent.

For n=6 to n=4, L6c reports 30/30 marked projections, 30/30 relative deletion collapses, 30/30 coarse diagram comparisons, and 2/2 parent-coherence groups in each target. This does not establish higher-order triple/four-way diagrams.

### L7b: old obstruction and newer candidate

The first lexicographically selected L4–L5 support family fails the anchored boundary-position test; only 14/30 projections pass its necessary condition. A local two-case incidence argument proves that the **old frozen three-edge motif** cannot satisfy L4+L5+the adopted open-complementary-arc condition, independently of support face-count. This is candidate-specific, not a no-go for all lifts.

The later alternative-triple construction freezes a different target-side support assignment (star/path/triangle cases). Its audit reports:
- L6c: 30/30 projections, collapses, diagram comparisons, and 2/2 parent groups in each target.
- L7b: 60/60 anchored cyclic-footprint comparisons, zero mismatches, 30/30 projections passing, and 2/2 parent boundary-word coherence groups in each target.
- Footprints are one connected boundary cell in the open complementary arc. Dimension can change (32 vertex-to-edge, 28 edge-to-edge), as allowed by L6c. There is only one retained footprint per boundary in these n=6 tests; multiple-footprint ordering is not tested here.
- Support choice is target-geometric and demand-independent.

**Provenance:** this alternative-triple audit says the calculations were executed in-session and the verifier committed/fetched back, but not run from a clean cloned checkout. It is a finite research result, not clean-CI-certified theorem evidence.

**Verdict:** finite L1–L7b evidence for n=4,6 in two Ngrid=7 targets. Strict L6 failed and was explicitly replaced by L6c. The old L7b candidate failed; the later alternative triple passes the adopted finite test. No all-orders incidence-lift theorem is established.

## 4. L8 terminology collision and confluence boundary

The records use “L8” in two different ways:
1. `PF_I16_HALL_TO_PENROSE_FIBONACCI_INCIDENCE_LIFT_2026_11_18.md` uses L8 for **Hall independence**: the lift is constructed without Hall deficiency, congestion, allocation or desired matching outcomes.
2. `PF_I16_HALL_L7_L8_SOURCE_DELETION_DIAMOND_2026_11_19.md` and later four-interval work use L8 for **construction independence / accepted-face support-diagram confluence**.

These are distinct requirements. Disambiguate as “L8-Hall-independence” and “G-L8 geometric confluence”; neither proves the other.

The source deletion lemma proves that two distinct eligible non-root leaf deletions commute, since endpoint compression and restriction/reindexing commute. Its n=8 regression checks 608 sources, 1,050 marked projections, 13 overlap graphs and all 490 simultaneous-mark diamonds with zero failures. The lemma is all-finite-order; the census is an implementation regression, not its proof.

A separate canonical-sibling guarded port-tree diamond proves equality of two guarded inverse orders under its stated canonical-neighborhood hypotheses, with common output in the ordinary parent neighborhood. The stronger canonical-parent conclusion is false at n=10: the cited census reports 286,440 failures.

Geometric L8 remains open. It requires support-to-source matching for every four-support candidate; all 15 labelled intersections including emptiness; relative deletion collapses along both paths; oriented boundary cycles anchored at directed matched edges; ordered multi-footprint words and meeting relations; and commutation of geometric diagram isomorphisms with all further restrictions. The n=8 census is an index for that work, not geometric L8.

## 5. Helical observer: source facts and nonclaims

The mainline real-structure audit retains
\[
\mathbb R^5=\mathbb R_{\rm triv}\oplus V_{72^\circ}\oplus V_{144^\circ}.
\]
It proves a no-go for the claimed real Lorentz-boost action on the same four real effective coordinates: the finite odd-order C5 representation has no nonzero fixed vector, while a finite subgroup preserving a future timelike cone would yield a fixed future timelike vector by averaging. The 144-degree rotation-to-real-boost claim also fails the finite-order test.

Paper 3 §7 defines a constant-radius complementary-plane circle (z_2(\tau)=A e^{2\pi i p\tau}), with p=3/13,5/13,8/13. At integer sampling all three visit the same 13-point grid in different orders; H2 and H3 reverse order. Conditional on the m=10 mode, f=10p gives arithmetic ratio 3:5:8. Paper 3 Remark 6 calls this kinematic sampling, not a field equation. It is not a KK mass spectrum.

The 3D lift is underdetermined: (X_v(t)=(A\cos\omega t,A\sin\omega t,vt)) has the same planar projection for different v but different curvature/torsion. A longitudinal coordinate, physical metric, clock and action require independent derivation.

Other unresolved source matters:
- 34:55 Conway-worm/double-spiral counts are not mapped to five Z5 directions or a directed observer path.
- Paper 3 and Paper 4 failure-band conventions differ (about 0.062 R_W versus 2 R_W(1-cos18°) ≈ 0.0978869 R_W); no reconciliation is recorded.
- The Paper 3 primary note and harmonic-triad note cite different dissertation PDF SHA-256 values (`ece7f92a...` and `de86cf0c...`). Resolve source artifact identity before treating them as one byte-identical source.
- Exact 13-sample alias, two-point reciprocity and harmonic-triad nulls are mathematical/calibration controls. The cited SU(2) rotor is a one-loop nongeometric control, not the coupled PF 3D interacting theory.
- The reverse-mark/helical bridge audit says no source-derived map currently sends a Hall port/interval/reverse mark to a Z5 lattice vector. Assigning phases by interval index or congestion would be arbitrary.

**Verdict:** the helical observer remains a kinematic proposal with useful exact finite alias/null results. Physical 3D helical action, real Lorentz C5 action, authentic 34:55 mapping and interacting PF quantum dynamics remain open or obstructed in their current formulations.

## 6. Observatory corrections required

1. Keep finite L1–L7 candidates separate from all-orders theorem nodes; record branch-only custody and lack of clean-checkout runs.
2. Preserve strict L6 as a superseded obstruction; record L6c as the adopted finite replacement.
3. Mark the old L7b failure candidate-specific and the alternative-triple result as the current finite candidate.
4. Split L8-Hall-independence from G-L8 geometric confluence.
5. Keep source-side deletion diamonds exact without promoting geometric L8.
6. Record n=10 multivalued-π matching and split-demand flow as finite certificates only.
7. Record the dissertation SHA discrepancy and missing source-to-reverse-mark map.
8. Do not promote branch-only scripts/results into mainline theorem-source counts until reviewed, cleanly replayed, and artifact/checksum-backed.

## 7. Next audit gates

- Clean-checkout replay of L1–L7 scripts at the exact incidence branch SHA, with pinned dependencies and saved JSON outputs.
- Resolve PF-I16 private-source provenance or retain the weaker independent-reimplementation label; keep PF-I11 core separate.
- Reconcile dissertation PDF checksums and archive manifests.
- Audit n=6 and n=8 split-demand flow artifacts/replay boundaries alongside n=10.
- For G-L8, map each surviving four-support candidate to actual order-eight source-parent records and compare full labelled diagrams, collapses, oriented cycles and multi-footprint words over all 490 source diamonds.
- Derive or explicitly abandon a source-authenticated map from reverse-mark data to Z5 displacement before assigning helical phases.

**No all-orders Hall theorem, all-orders accepted-face lift, geometric L8, physical 3D helical action, or continuum Yang–Mills gap is closed by this audit.**
