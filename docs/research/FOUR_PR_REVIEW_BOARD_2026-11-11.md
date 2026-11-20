# Four-PR review board · 2026-11-11

**Current target: four open PRs, tracked together in the Observatory graph v2.74.** This is a live coordination board, not a mathematical theorem index.

| PR | Title / role | Base | Head branch | Exact head SHA | Mergeability |
|---|---|---|---|---|---|
| [#107](https://github.com/syncgravity/Singular-Boundary/pull/107) | Canonical source-compatible spectral-inequality proof spine and Observatory integration | main | `architecture/source-compatible-spectral-spine-2026-11-11` | live branch head (self-updating) | **revalidation required** — latest compare is diverged (81 ahead / 93 behind); no mergeability claim until current PR checks and path reconciliation pass |
| [#106](https://github.com/syncgravity/Singular-Boundary/pull/106) | R3-IR finite-strip full-Hessian analysis | #107 branch | `audit/r3-ir-h2-trace-to-k-2026-11-10` | `12995f4e34e0a7125da881f0ec655da243e33c3e` | not mergeable; reconcile overlapping generated files |
| [#74](https://github.com/syncgravity/Singular-Boundary/pull/74) | Finite non-Abelian SU(2) positive-probability tube and theorem-index work | main | `audit/2026-11-06-nonabelian-tube-complete-theorem-index` | `447dcea7c54175bf46962de0222ceba519659796` | not mergeable; reconcile theorem index / graph snapshots |
| [#103](https://github.com/syncgravity/Singular-Boundary/pull/103) | Observatory publishing preparation | main | `pages-public-ready` | `53c608a3f3884066568525374c32b4fc2986f866` | not mergeable; reconcile publication target and workflow |

## Resolution rules

1. **#107 owns canonical mathematical architecture**: one S0–S5 spine and one generated current theorem inventory. No proof gate is closed by indexing.
2. **#106 remains a separate finite-strip model.** Preserve all unique full-Hessian derivations, analytic estimates, audit logs and verifier scripts. It may contribute to the Observatory as a separate node/route; it cannot silently become the PF physical Hamiltonian.
3. **#74 remains a finite-regulator evidence lane.** Preserve its tube certificate and verifier. Reconcile graph/index changes by regenerating from the current registry, not copying its historical generated snapshots wholesale.
4. **#103 remains publishing-only.** GitHub Pages is not the selected route. Tau serves the Observatory at `https://qualion.org/yang-mills` through Fly Deploy; keep source research private and deploy only the curated static Observatory assets.
5. Update this board and graph tracker whenever a base branch or head SHA changes. Record mergeability and CI separately. Do not close an unresolved PR to reach a target count.
6. Branch deletion is separate from PR closure/merge and remains subject to the SHA-checked dry-run retirement protocol.

## Current mathematical boundary

S0–S5 remain OPEN. The finite non-Abelian tube probability is not uniform in refinement/volume. The R3-IR full-Hessian contraction is conditional on its finite strip and does not prove the source-native PF continuum gap. Publishing readiness is not proof status.


## Mainline reconciliation update · 2026-11-11

The main branch now contains the research map, handoff records, PF-I16 preservation corpus, P0/P2/R3 audit reports, canonical spectral-inequality page, and synchronized 762-path theorem index. PR #107 remains open, but its head is now **81 commits ahead and 93 behind** main in the latest compare snapshot. The compare is divergent; do not treat the older "mergeable" label as current. The remaining 41 changed paths must be reconciled against the files already brought into main. Seven script paths listed in the branch comparison could not be fetched by the connector and are recorded as unresolved in [the PR #107 preservation ledger](PR107_BRANCH_PRESERVATION_LEDGER_2026-11-11.md).


## Live reconciliation snapshot · 2026-11-19

The board now tracks the expanded active set of eight open PRs. This live snapshot supersedes the four-PR table above for branch status, while preserving the original resolution rules and mathematical boundaries.

| PR | Base → head | Head SHA | Current state | Disposition |
|---|---|---|---|---|
| [#107](https://github.com/syncgravity/Singular-Boundary/pull/107) | `main` → `architecture/source-compatible-spectral-spine-2026-11-11` | `6e48d007c6b71e842b002442eb7d855d2a7c12f9` | Open; 81 commits; 41 files; not mergeable | Do not merge wholesale. Its branch is divergent (81 ahead / 544 behind in the latest compare); preserve/reconcile unique content. The failed graph check is a version-allowlist mismatch (`v2.74-four-pr-review-board`), not a theorem calculation failure. |
| [#106](https://github.com/syncgravity/Singular-Boundary/pull/106) | #107 branch → R3-IR finite-strip branch | `12995f4e34e0a7125da881f0ec655da243e33c3e` | Open draft; 64 commits; 28 files; not mergeable | Keep stacked; preserve the finite-strip model as a distinct reference lane. |
| [#74](https://github.com/syncgravity/Singular-Boundary/pull/74) | `main` → finite non-Abelian tube branch | `447dcea7c54175bf46962de0222ceba519659796` | Open draft; 21 commits; 19 files; not mergeable | Selective source/evidence reconciliation; do not copy generated snapshots. |
| [#103](https://github.com/syncgravity/Singular-Boundary/pull/103) | `main` → Pages publishing branch | `53c608a3f3884066568525374c32b4fc2986f866` | Open; 7 commits; 6 files; not mergeable | Publishing-only; retain selected Tau/Fly deployment route. |
| [#108](https://github.com/syncgravity/Singular-Boundary/pull/108) | `main` → parastichy lift correction | `1181077bdaae5dc0ca83b1fe3f3b2245f3def331` | Open draft; 59 commits; 19 files; not mergeable | Review as a separate geometry lane; no proof-gate promotion. |
| [#114](https://github.com/syncgravity/Singular-Boundary/pull/114) | `main` → product-cumulant hypergraph bridge | `52ddf77fd67f969f90acc9c31e0a8293e9af3759` | Open; 7 commits; 3 files; not mergeable | Preserve exact cumulant identities and degree-eight obstruction; reconcile base conflicts before integration. |
| [#118](https://github.com/syncgravity/Singular-Boundary/pull/118) | `main` → superrow cut-covariance lane | `eacc190efdb5c204d038449946e705f405a100c3` | Open draft; 605 commits; 210 files; not mergeable | Selective extraction only; no wholesale stack merge. |
| [#119](https://github.com/syncgravity/Singular-Boundary/pull/119) | `main` → four-interval diamond lane | `8e49e2480b0b6e291524784c4caf5d4967a2efad` | Open draft; 56 commits; 20 files; currently not mergeable | Keep unmerged while the expanded CI, source-parent audit, and actual source-diagram matching are incomplete. |

### Observatory synchronization

On 2026-11-19 the seven core Observatory pages were refreshed with one consistent PF-I16 four-interval frontier panel: `index.html`, `graph.html`, `handoff.html`, `integration.html`, `penrose-program.html`, `spectral-inequality.html`, and `yang-mills-proof.html`. Their shared status reports the latest completed CI snapshot (50/52 pair frontier; 64 pair/fourth-edge cases; 514 graph-5 and 482 graph-12 independent full-diagram candidates), links PR #119 and the durable work-gate record, and explicitly leaves L8 and S0–S5 open. Current mainline graph metadata is v3.04, 773 theorem-source paths, 298 curated nodes, and 703 typed relationships. These counts are navigational only.

All seven page-update push workflows have now completed successfully, including the final theorem-index/graph workflow (44676689424). PR #119's expanded rerun remains in progress and its current mergeability check is false. Recheck that lane before any merge decision.

### Merge order remains unchanged

1. Reconcile the #107 architecture content against current mainline and repair the verifier/graph-version contract; do not merge the 544-commit-stale branch.
2. Resolve #106 only against a stable architecture base, preserving its separate model.
3. Selectively reconcile #74, #114, #118 and #108 by unique source artifacts and explicit model boundaries.
4. Keep #103's deployment decision separate.
5. Keep #119 open until source-parent mark CI, full 15-entry source-diagram matching, oriented L7b footprint comparison, and restriction coherence are recorded.

No PR was merged or closed in this update. S0–S5 remain OPEN.
