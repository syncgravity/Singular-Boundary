# Consolidation archive and final audit · 2026-11-11

**Canonical open integration PR:** [#107 — Establish one source-compatible spectral-inequality proof spine](https://github.com/syncgravity/Singular-Boundary/pull/107)

This ledger records the disposition of the 12-PR cleanup. It distinguishes merged content from explicitly archived branch histories. Closing a PR does not delete its branch. No unmerged branch is deleted or force-moved by this consolidation.

## Merged into the #107 integration branch

The following research contributions were reviewed for scope and merged as separate commits into `architecture/source-compatible-spectral-spine-2026-11-11`:

- [#55 — quantitative local SU(2) f-sum](https://github.com/syncgravity/Singular-Boundary/pull/55): conditional first excitation-frequency moment lower bound; explicitly **not** a lower bound on the bottom of positive spectral support and not a gap.
- [#56 — P0 refinement / P4 source-visible audit](https://github.com/syncgravity/Singular-Boundary/pull/56): source archive hashes and cubic refinement benchmark; explicitly not coupled-Z5/Penrose source certification.
- [#79 — one-plaquette classical-action transfer audit](https://github.com/syncgravity/Singular-Boundary/pull/79): exact solvable Gibbs countercalibration; not the interacting 3D vacuum.
- [#80 — one-face quantum-vacuum cap audit](https://github.com/syncgravity/Singular-Boundary/pull/80): exact one-face ground-state estimate; not the coupled 3D vacuum.
- [#81 — coupled cubic vacuum link-deletion](https://github.com/syncgravity/Singular-Boundary/pull/81): finite original-link cubic SU(2) variational/Sobolev result for bare plaquette action; no positive-flow renormalized-curvature or continuum result.
- [#82 — cubic vacuum-to-flow averaged defect](https://github.com/syncgravity/Singular-Boundary/pull/82): finite coupled-cubic expectation/averaged-force estimate; physical curvature normalization still diverges at the stated scale.
- [#83 — signed center-Hessian obstruction](https://github.com/syncgravity/Singular-Boundary/pull/83): exact global pointwise Wilson-flow contraction obstruction; does not refute vacuum-weighted smoothing.
- [#84 — transported vacuum entropy / averaged force](https://github.com/syncgravity/Singular-Boundary/pull/84): exact finite-regulator transport and time-averaged force identities; not pointwise physical-curvature regularity.

These are subordinate evidence and obstruction lanes. Their original PR discussions and commits remain in Git history. No theorem IDs or canonical proof-gate statuses were promoted.

## Explicitly archived, then closed unmerged

These three PRs overlap the current Observatory/catalog/handoff files. Their original branches are retained unchanged, and their complete changed-path inventories are recorded below. The branch heads are immutable provenance anchors; do not delete these refs as part of routine merged-branch pruning. Their Observatory snapshots are historical alternatives, not the current canonical graph.

### [#106 — R3-IR finite-strip full-Hessian audit](https://github.com/syncgravity/Singular-Boundary/pull/106)

- Branch: `audit/r3-ir-h2-trace-to-k-2026-11-10`
- Preserved head: [`12995f4e34e0a7125da881f0ec655da243e33c3e`](https://github.com/syncgravity/Singular-Boundary/commit/12995f4e34e0a7125da881f0ec655da243e33c3e)
- Disposition: **archived branch, PR closed unmerged** because its generated Observatory/index snapshot conflicts with the newer #107 canonical interface. The finite-strip research remains available at the exact branch head; it is not merged into the PF source-native model and is not a continuum gap result.
- Changed paths:
  - `README.md`
  - `docs/research/THEOREM_INDEX.md`
  - `docs/research/THEOREM_INDEX_CURRENT.md`
  - `docs/research/THEOREM_INDEX_LIVE.json`
  - `observatory/README.md`
  - `observatory/graph.html`
  - `observatory/index.html`
  - `observatory/knowledge-graph-data.js`
  - `research/audits/R3_IR_3D_REGULATOR_TRANSFER_AUDIT_2026-11-11.log`
  - `research/audits/R3_IR_3D_REGULATOR_TRANSFER_AUDIT_2026-11-11.md`
  - `research/audits/R3_IR_ADVERSARIAL_FULL_HESSIAN_ENERGY_INEQUALITY_AUDIT_2026-11-11.md`
  - `research/audits/R3_IR_BOUNDED_INCIDENCE_ANALYTIC_EXTENSION_2026-11-11.md`
  - `research/audits/R3_IR_BOUNDED_INCIDENCE_EXTENSION_2026-11-11.log`
  - `research/audits/R3_IR_COMMON_MEASURE_SMOOTH_CORE_FINITE_STRIP_EXTENSION_2026-11-11.md`
  - `research/audits/R3_IR_CONDITIONAL_FULL_HESSIAN_FINITE_STRIP_PROPOSITION_2026-11-11.md`
  - `research/audits/R3_IR_FULL_HESSIAN_ENERGY_BYPASS_AUDIT_2026-11-10.md`
  - `research/audits/R3_IR_FULL_HESSIAN_WEIGHTED_SCHUR_CURVATURE_CHECK_2026-11-11.md`
  - `research/audits/R3_IR_LOCAL_GEOMETRY_SOURCE_AND_INCIDENCE_AUDIT_2026-11-11.md`
  - `research/audits/R3_IR_LOCAL_GEOMETRY_SOURCE_AUDIT_2026-11-11.log`
  - `research/audits/R3_IR_LOCAL_GEOMETRY_SOURCE_AUDIT_2026-11-11_SHA256.txt`
  - `research/audits/R3_IR_SHARP_WEIGHTED_ANALYTIC_INPUTS_2026-11-11.log`
  - `research/audits/R3_IR_SHARP_WEIGHTED_BOCHNER_AND_TRACE_POINCARE_2026-11-11.md`
  - `research/audits/verify_R3_IR_bounded_incidence_extension_2026-11-11.py`
  - `research/audits/verify_R3_IR_local_geometry_source_audit_2026-11-11.py`
  - `research/audits/verify_R3_IR_projected_Z5_degree8_transfer_2026-11-11.py`
  - `research/audits/verify_R3_IR_sharp_weighted_analytic_inputs_2026-11-11.py`
  - `research/problems/R3-IR.md`
  - `research/theorems/R3_IR_H2_WEIGHTED_TRACE_TO_K_COUPLING_AUDIT_2026-11-10.md`

### [#74 — finite non-Abelian SU(2) positive-probability tube and theorem index](https://github.com/syncgravity/Singular-Boundary/pull/74)

- Branch: `audit/2026-11-06-nonabelian-tube-complete-theorem-index`
- Preserved head: [`447dcea7c54175bf46962de0222ceba519659796`](https://github.com/syncgravity/Singular-Boundary/commit/447dcea7c54175bf46962de0222ceba519659796)
- Disposition: **archived branch, PR closed unmerged** because its theorem-index, graph and Observatory files represent an earlier, conflicting snapshot. Its finite non-Abelian tube theorem is finite-regulator positive probability only; its lower probability certificate is not uniform in refinement or volume.
- Changed paths:
  - `.github/workflows/theorem-index.yml`
  - `docs/evidence/R3_NONABELIAN_CARTAN_TUBE_2026-11-06.json`
  - `docs/research/PROOF_DEPENDENCIES.md`
  - `docs/research/THEOREM_INDEX.md`
  - `docs/research/THEOREM_INDEX_CURRENT.json`
  - `docs/research/THEOREM_INDEX_CURRENT.md`
  - `observatory/MATHEMATICAL_PHYSICS_GUIDE.md`
  - `observatory/README.md`
  - `observatory/graph-app.js`
  - `observatory/graph.html`
  - `observatory/index.html`
  - `observatory/knowledge-graph-data.js`
  - `observatory/knowledge-graph.json`
  - `observatory/tools/add_nonabelian_tube_graph.py`
  - `observatory/tools/build_knowledge_graph.py`
  - `observatory/tools/verify_knowledge_graph.py`
  - `research/scripts/verify_nonabelian_cartan_tube_2026_11_06.py`
  - `research/theorems/R3_FINITE_NONABELIAN_CARTAN_TUBE_POSITIVE_TIME_CERTIFICATE_2026-11-06.md`
  - `scripts/verify_theorem_inventory.py`

### [#103 — public GitHub Pages preparation](https://github.com/syncgravity/Singular-Boundary/pull/103)

- Branch: `pages-public-ready`
- Preserved head: [`53c608a3f3884066568525374c32b4fc2986f866`](https://github.com/syncgravity/Singular-Boundary/commit/53c608a3f3884066568525374c32b4fc2986f866)
- Disposition: **archived branch, PR closed unmerged**. Publishing configuration is kept separate from mathematical integration and no Pages activation/public deployment is authorized by this cleanup.
- Changed paths:
  - `.github/workflows/pages.yml`
  - `observatory/PUBLISHING.md`
  - `observatory/conceptual-atlas.html`
  - `observatory/index.html`
  - `observatory/penrose-program.html`
  - `observatory/yang-mills-proof.html`

## Helical observer audit — preserve as an observation protocol, not dynamics

The Paper 3 source dossier and its follow-up audits remain the authoritative observer subroute:

- [Primary Paper 3 source-fidelity audit](https://github.com/syncgravity/Singular-Boundary/blob/main/research/geometry/PF_PAPER3_HELICAL_OBSERVER_PRIMARY_HYPOTHESIS_2026_11_07.md)
- [Exact Z13 aliasing and interacting two-point reciprocity](https://github.com/syncgravity/Singular-Boundary/blob/main/research/geometry/PF_HELICAL_OBSERVER_COVARIANCE_ALIAS_2026_11_07.md)
- [Harmonic triad, lift nonuniqueness and interacting rotor null](https://github.com/syncgravity/Singular-Boundary/blob/main/research/geometry/PF_HELICAL_HARMONIC_TRIAD_AND_INTERACTING_NULL_2026_11_07.md)
- [Observer-marked handedness and parity audit](https://github.com/syncgravity/Singular-Boundary/blob/main/research/geometry/PF_OBSERVER_MARKED_HANDEDNESS_PARITY_AUDIT_2026_11_07.md)

The observer pitches (3/13,5/13,8/13) and conditional (m=10) ratios (3:5:8) are **kinematic sampling frequencies**, not Hamiltonian eigenvalues or mass ratios. Integer sampling has exact 13-phase aliasing; (8\equiv-5\pmod{13}), so H2/H3 have the same real discrete power spectrum and cyclic two-point autocorrelation under the stated phase-uniform protocol. A chiral unequal-lag three-point statistic can distinguish ordering, but a nonzero value is not Penrose-specific: non-Penrose scalar and interacting one-loop SU(2) controls also produce nonzero contrast. The projected complex circle does not uniquely determine a 3D longitudinal lift, physical metric, clock, two-strand construction or torsion. An observer mark can retain handedness in a parity-even vacuum, but does not dynamically select a physical orientation.

**Strategy:** keep the helical observer as a source-aware, gauge-invariant probe/falsification protocol under PF-G0/PF-H0–H5. Do not make it the physical Hamiltonian, clock, or source of the mass-gap estimate. Its source-authenticated coupled-ℤ^5 geometry, 3D lift, closed Wilson-probe dictionary and matched interacting-vacuum h/R-uniform covariance remain open.

## Final proof status

The single canonical target remains the source-compatible interacting-vacuum Poincaré inequality, uniform in regulator refinement and physical volume, followed by infrared exclusion and nontrivial 4D OS reconstruction. S0–S5 remain OPEN. Finite exact results, conditional finite-strip estimates, source-index integrity, numerical checks and counterexamples remain distinct evidence classes. No Yang–Mills mass-gap proof is claimed.
