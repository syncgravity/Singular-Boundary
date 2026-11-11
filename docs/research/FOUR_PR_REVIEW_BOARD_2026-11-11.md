# Four-PR review board · 2026-11-11

**Current target: four open PRs, tracked together in the Observatory graph v2.74.** This is a live coordination board, not a mathematical theorem index.

| PR | Title / role | Base | Head branch | Exact head SHA | Mergeability |
|---|---|---|---|---|---|
| [#107](https://github.com/syncgravity/Singular-Boundary/pull/107) | Canonical source-compatible spectral-inequality proof spine and Observatory integration | main | `architecture/source-compatible-spectral-spine-2026-11-11` | `4e1f5d0bbd359471a8cf005c47bea965540939b7` | mergeable |
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
