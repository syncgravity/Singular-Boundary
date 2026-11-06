# Research Observatory v2.29 — Mathematical Physics Proof Atlas

**Source status:** integrated on the private `main` branch, November 5, 2026. **Mathematical status:** all P0–P5 continuum Yang–Mills gates and the independent quantum-gravity objective remain **OPEN**. Merging the site is not proof acceptance or permission to publish it publicly.

## Explore the proof

- [Observatory overview](index.html) — the complete proof-program entry point, P0–P5 dependencies, routes, obstructions and source catalog.
- [Interactive Proof Atlas](graph.html) — 101 curated mathematical-physics nodes and 189 typed edges; starts on the **Cubic → Quasicrystal** model-transfer view.
- [Uniform interacting theorem integration](integration.html) — the conditional physical-time spectral-support bridge, common-regulator requirements and explicit continuum obligations.
- [Mathematical-physics reader guide](MATHEMATICAL_PHYSICS_GUIDE.md) — precise meanings of models, results, obstacles, interfaces, review status, and the six cross-model T0–T5 conditions.

The **740-record theorem index** and **78 previously identified proof pathways** are historical discovery baselines, not independently accepted proof counts; they remain unchanged. The Atlas has **26 immutable original-file entries** with SHA-256 digests and Library paths, covering the Penrose and square ensembles, Whitney data, source papers and historical source records. The actual original binary/transcript bytes remain in **Library → The Singular Boundary → Data**, not in ordinary Git, until an independently verified Git LFS migration is configured.

### Model boundaries

The original quasicrystalline model (Fibonacci/Penrose/coupled ℤ⁵), its square 2D periodic comparison, and the later cubic 3D SU(2) reference are **not interchangeable**. Finite Gauss-invariant cubic estimates and positive transfer constructions are useful within their declared models but do not establish a weak-bare-coupling, nontrivial interacting 4D continuum mass gap. No 3D quasicrystal transfer theorem has been proved. The proposed quasicrystalline gravitational ultraviolet mechanism requires its own physically justified gravitational operator; it does not follow from a Yang–Mills mass gap, nor does a lattice spectral-zeta ratio prove it.

The graph uses mathematical objects and open obligations as readable node names; source document titles, archive names and their hashes are preserved as **provenance**, not rebranded into new mathematical claims. Review flags are browser-local and exportable as JSON. Such notes never close a gate or alter the append-only historical claim ledger.

## New P0/T2 result awaiting mathematical review (2026-11-05)

The next finite-model source checkpoint combines [Haar holonomy-block magnetic loss](../research/theorems/R3_CUBIC_HAAR_BLOCK_MAGNETIC_LEAKAGE_2026-11-05.md), [exact four-face Wilson-character recovery](../research/theorems/R3_CUBIC_FACE_BLOCK_HAAR_RECOVERY_2026-11-05.md) and [an isolated planar character-convolution law](../research/theorems/R3_SU2_PLANAR_BLOCK_CHARACTER_TRANSFER_2026-11-05.md). These establish why a one-face kinematic Haar compression discards magnetic information and why a four-face product retains coarse Wilson information at coefficient 1/8. The planar weight also generates higher representations, so the effective action does not remain a single-parameter fundamental Wilson weight.

**Status:** exact finite / planar calculations, pending independent source review. The 101-node v2.29 Atlas, its 189 edges, and all six OPEN YM gates remain unchanged; this is a source-index update rather than a gate promotion or public deployment. Verifiers and source-pinned JSON are in `research/scripts/verify_{haar_block_compression,fine_plaquette_cluster,planar_character_block}_2026_11_05.py` and `docs/evidence/`. The full original-byte package and execution logs reside in Library → The Singular Boundary → Proof Audits → Cubic Haar Blocking 2026-11-05.

## Reproduce and audit

Open `index.html` and `graph.html` with `catalog.js`, `proofpaths.js`, `audit.js`, `graph.css`, `graph-app.js` and `knowledge-graph-data.js` in one folder. The atlas uses no externally hosted script or stylesheet.

From the repository root:

```bash
python observatory/tools/build_knowledge_graph.py
python observatory/tools/verify_knowledge_graph.py
python observatory/tools/verify_knowledge_graph.py --data-dir /path/to/original-files
python research/scripts/verify_cubic_penrose_gate_boundaries_2026_11_05.py
node --check observatory/graph-app.js
```

The optional `--data-dir` rechecks original file sizes and SHA-256 values; without those files, the validator checks the committed manifest and graph structure. The source-derived proof audits include [P0 model identity](../docs/research/P0_MODEL_HIERARCHY_PENROSE_CONTROL_AUDIT_2026-11-05.md), [cubic-to-quasicrystal transfer constraints](../docs/research/YM_CUBIC_PENROSE_TRANSFER_AND_INFRARED_GATES_2026-11-05.md), [closure protocol](../docs/research/KNOWLEDGE_GRAPH_CLOSURE_PROTOCOL_2026-11-04.md), and [historical archive audit](HISTORICAL_DOUBLE_AUDIT_2026-11-04.md). **Structural tests and hashes do not verify mathematical truth.**

## Publication boundary

This private repository's [Pages workflow](../.github/workflows/pages.yml) has **only a manual `workflow_dispatch` trigger**. The source merge did **not** trigger publication; public release requires an explicit separate decision and privacy/source review. GitHub Pages would expose the curated static site even if this repository remains private. Do not publish historical source identifiers or research summaries without that review.

**Release provenance:** stacked changes were merged through [PR #57](https://github.com/syncgravity/singular-boundary/pull/57), [#58](https://github.com/syncgravity/singular-boundary/pull/58), [#59](https://github.com/syncgravity/singular-boundary/pull/59), [#60](https://github.com/syncgravity/singular-boundary/pull/60), and [#61](https://github.com/syncgravity/singular-boundary/pull/61), retaining their detailed scientific assumptions and archive history.
