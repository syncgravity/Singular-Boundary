# PR #107 integration-branch preservation ledger

**Branch:** `architecture/source-compatible-spectral-spine-2026-11-11`  
**Destination:** `main`  
**Comparison snapshot:** 2026-11-11, 81 commits ahead / 89 behind, 41 changed paths. This is a dated comparison, not a live branch status.

## Disposition

PR #107 was not merged wholesale. Its history is divergent and its generated Observatory outputs were based on an earlier theorem registry. Instead, the useful source records and canonical proof/handoff documents were reconciled into `main`; generated outputs were rebuilt from the current mainline registry.

- Eight finite-model research audit reports were copied verbatim to their original paths.
- The P0 source-archive metadata was copied verbatim.
- The repository handoff, branch lifecycle, four-PR review board, consolidation archive, and canonical source-compatible proof specification were copied to `docs/research/`.
- The PF-I16 and Z5/helical-observer review records were copied to `docs/research/`.
- The canonical spectral-inequality and handoff Observatory pages were copied; the main Observatory home was patched to link them and its theorem counts were refreshed.
- The six PF-I16 geometry dossiers listed in the comparison are already preserved in `main`; their original source blob hashes are in [the PF-I16 preservation ledger](PF_I16_BRANCH_PRESERVATION_LEDGER_2026-11-11.md).
- The live theorem registry and all generated catalog/current-navigator/graph outputs were regenerated from the current `main` source registry. The resulting count is 762, not the older 761 snapshot.
- The root README was not replaced wholesale; its navigation, status date, PF-I16 disposition and current index count were reconciled with mainline content.
- The seven script paths listed below could not be fetched from the named branch ref through the available GitHub file interface (404). They are therefore **not claimed as imported**. They remain explicit follow-up retrieval items.

## Source records copied from the branch

| Path | Original source-branch blob SHA-1 |
|---|---|
| `docs/evidence/P0_SOURCE_ARCHIVE_METADATA_2026-11-05.json` | `6149b1e1682c0be74198e119f40948bb28516ecc` |
| `docs/research/BRANCH_LIFECYCLE_2026-11-11.md` | `486715c2960d23ddbd14b0152cedf5c048636de0` |
| `docs/research/CONSOLIDATION_ARCHIVE_2026-11-11.md` | `eca508ec13bf07a71db41aef2f8e19ea0c5dc360` |
| `docs/research/FOUR_PR_REVIEW_BOARD_2026-11-11.md` | `42ddc27f35161ced7092f3264eb43a0ed440741a` |
| `docs/research/PF_I16_BRANCH_RECONCILIATION_2026-11-11.md` | `49653df374efe8abdc1c5fc50ab068118f33cba8` |
| `docs/research/REPOSITORY_HANDOFF_2026-11-11.md` | `277898fcc638f2c273bd1e1c01a63f9408ea74f3` |
| `docs/research/SOURCE_COMPATIBLE_SPECTRAL_INEQUALITY_PROGRAM_2026-11-11.md` | `60e23d0cc474f09d6b63a7f04b90d8ec86524ed9` |
| `docs/research/Z5_REAL_STRUCTURE_AND_HELICAL_OBSERVER_SOURCE_AUDIT_2026-11-11.md` | `566f7401d658674696594c415a90897ec07630df` |
| `observatory/spectral-inequality.html` | `02ad65964decfcb067aab1510c7c9486e82e0051` |
| `observatory/handoff.html` | `491367595defa66e6d24080bea5ba297e16a49b2` |
| `research/audits/P0_REFINEMENT_AND_P4_SOURCE_VISIBLE_AUDIT_2026-11-05.md` | `f78e482e692831ad2b53a3d25615eb87dac8569a` |
| `research/audits/P2_QUANTITATIVE_LOCAL_FSUM_2026-11-04.md` | `ed891c07c9e6021929f16b5a143ee508553ded0b` |
| `research/audits/R3_COUPLED_CUBIC_QUANTUM_VACUUM_LINK_DELETION_2026-11-06.md` | `1185a92c19a2fad07ff5bada4c416298d183052e` |
| `research/audits/R3_COUPLED_CUBIC_VACUUM_TO_FLOW_AVERAGED_CURVATURE_2026-11-06.md` | `9a8b31f5f82a8f7b7f43a1d28a23cc6795d4be53` |
| `research/audits/R3_COUPLED_VACUUM_FLOW_ENTROPY_AND_AVERAGED_FORCE_2026-11-06.md` | `ce625cf9da9fee75f7346e0fd1b8aca51d817c61` |
| `research/audits/R3_ONE_PLAQUETTE_GIBBS_CLASSICAL_ACTION_TRANSFER_AUDIT_2026-11-06.md` | `7d467e64205f3f8af9aa2d6b981c9d9231585281` |
| `research/audits/R3_QUANTUM_ONE_FACE_VACUUM_REGULARITY_AND_CAP_AUDIT_2026-11-06.md` | `c2833edb6fe53627a9044fb4a7a52cc9906e506c` |
| `research/audits/R3_SIGNED_CENTER_HESSIAN_FLOW_INSTABILITY_2026-11-06.md` | `19bc1f9991bfdafac5a3773b5c367720845b6a99` |

## Mainline generated or reconciled rather than copied

- `README.md` — merged selected navigation/status changes; retained main's current research content.
- `docs/research/THEOREM_INDEX_LIVE.json` — updated to 762 source paths with exact blob SHA and byte count.
- `docs/research/THEOREM_INDEX.md` — added the PF-I16 connected-cycle gate exactly once.
- `docs/research/THEOREM_INDEX_CURRENT.md` and `observatory/catalog.js` — regenerated from the live registry.
- `observatory/knowledge-graph.json` and `observatory/knowledge-graph-data.js` — synchronized; 285 nodes and 678 relationships.
- `observatory/index.html` and `observatory/README.md` — linked the new pages and refreshed current counts.
- `observatory/handoff.html` — repaired the consolidation-archive link to point into `docs/research/`.

## Explicit retrieval items

The branch comparison listed these seven scripts, but `fetch_file` returned 404 for each at the named branch ref. No content was fabricated and no placeholder was committed:

- `research/scripts/audit_attached_sources_2026-11-05.py`
- `research/scripts/verify_cubic_vacuum_flow_entropy_2026-11-06.py`
- `research/scripts/verify_cubic_vacuum_flow_mean_defect_2026-11-06.py`
- `research/scripts/verify_p0_refinement_2026-11-05.py`
- `research/scripts/verify_quantitative_fsum_2026-11-04.py`
- `research/scripts/verify_signed_center_hessian_2026-11-06.py`
- `research/scripts/verify_source_visible_spectral_weight_2026-11-05.py`

The original branch and PR remain intact. These retrieval items should be recovered from the source commit or a local checkout before the branch can be considered fully reconciled.

## Model boundaries retained

The P0 cubic refinement benchmark is an explicit cubic reference and does not authenticate a 3D Penrose regulator. The P2 local f-sum result is conditional on its straight-strip antecedents and gives a positive first spectral moment, not a gap. The R3 cubic-vacuum and Wilson-flow records are finite cubic-model results and obstructions; they are not source-native PF-I16 dynamics. These records are preserved as distinct contributions and cannot be used as if they were one physical regulator.
