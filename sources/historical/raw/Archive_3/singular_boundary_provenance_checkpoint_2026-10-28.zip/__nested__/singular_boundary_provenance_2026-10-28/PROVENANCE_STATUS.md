# The Singular Boundary — read-only provenance checkpoint (2026-10-28)

## Recovered and directly available

- Stage 7 original large matched pilot archive: source, `stage7_checkpointed.py`, Stage 7 report, test suites, action audit, two initial pilot checkpoint files and SHA256 manifest. Read-only ZIP inspected; no simulations run.
- Stage 9 local continuation instructions: confirm eight saved 20-slice configurations, separate seeds 101/211/307/419 for square and Penrose, and continuation requirements. These instructions are a historical description, **not** an independently rerun admission audit.
- Stage 22 and Stage 23 source: shifted slab boundaries, restricted sweeps and pilot benchmarks. `stage22_shifted.py` directly imports Stage 19 and Stage 21 modules.
- Stage 26 source and read-only Penrose incidence: recorded geometry at nt=20, source-array shapes 1,368,480 × 4, array/source hashes, but no certified historical R3 insertion or frozen-boundary partition.

## Source lineage

Stage 7 `setup_geometry()` (via `stage7_checkpointed.py`) → Stage 9 saved ensembles → Stage 19 catalogue/measurement and Stage 21 conditional sweep → Stage 22 shifted-slab handling → Stage 23 independent-outer pilot → Stage 26 outer chain measurements and incidence export.

This is a **source dependency lineage**, not a claim all intermediate numerical stage results are reproduced.

## Critical scientific boundaries

1. Stage 7 has warm-up checkpoints and no admitted production mass; Stage 9 instructions explicitly keep mass/continuum outputs null pending autocorrelation and physical matching gates.
2. The Stage 26 incidence export gives real simulated face words, but its default cavity-only partition does **not** certify the original R3 insertion set or exterior-fixed boundary links.
3. The historical R3 cavity cannot be uniquely designated from the Stage 26 full-lattice incidence without a definition of Q and the spatial/time placement and boundary convention.
4. Existing Stage 19 / 21 files should be retrieved from the user's saved originals only when a specific test needs their definitions. Never substitute a reimplementation silently.
5. No historical Monte Carlo sweeps, recomputation, mass fits or numerical certificates were rerun here.

## Deferred targeted request

If needed for the next exact R3 geometry/measure bridge: Stage 19 `stage19_mc.py` and Stage 21 `stage21_scalar_multilevel.py`, or the existing `stage19_complete` dependency bundle. Do not request Stage 19 results just to create another copy.

## Deliverables

- `artifact_manifest.csv`: hashes and sizes of the direct primary inputs used.
- `stage7_zip_inventory.json`: path/size/CRC inventory of Stage 7 ZIP members.
- `stage7_setup_geometry_excerpt.txt`: exact excerpt of original constructor.
- `PROVENANCE_STATUS.md`: this status.
