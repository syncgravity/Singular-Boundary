# Research Observatory v2.28-draft · Penrose primary / periodic controls

Open `index.html` together with `catalog.js`, `audit.js`, and `proofpaths.js` in the same folder (works without a server). The **740-record catalog** is generated from the immutable source Git tree `fd1c1c1c8db078f8ec9d591d182059bd1635b164` and records paths, Git blob identifiers and source sizes. Only 12 selected theorem bodies have editorial annotations; all remaining records explicitly say `Indexed path and Git blob only`.

The site includes a P0–P5 dependency navigator, searchable 740-file theorem catalog, four candidate proof routes, exact missing implications, the supplied historical archive audit, and evidence controls.

**Do not publish publicly before privacy and source-publication review.** Source links refer to the private GitHub repository. No secrets or binary data are embedded. The continuum mass gap is open.

See `HISTORICAL_DOUBLE_AUDIT_2026-11-04.md` for source-level findings and limitations.

To replay the mounted archive checks: `python observatory/tools/verify_stage26.py /path/to/uploads` (NumPy required). The checker makes no changes to inputs. The original archives must be supplied separately; this repository does not automatically contain them.


## New P0–P5 theorem integration (private draft)

[`integration.html`](integration.html) presents the quantified common-regulator theorem, conditional positive-time spectral-support lemma, six interactive gate interfaces, a geometric-versus-quantum-versus-double-uniform acceptance table, explicit Z5/prism/cubic model distinctions, and an incremental dissertation publication plan. This view is **proposed in a review branch only**; it is not a new certified theorem, not a change to the 740-path baseline catalog, and not deployed on GitHub Pages. Supporting drafts are in `docs/research/UNIFORM_INTERACTING_THEOREM_BRIDGE_2026-11-04.md` and `docs/research/DISSERTATION_EVOLUTION_AND_PUBLICATION_PLAN_2026-11-04.md` (both source paths relative to the repository root). The structural validator is `observatory/tools/verify_uniform_integration_contract.py` and checks presentation/contracts only, not mathematical truth.


## Proof Atlas · source-linked knowledge graph (proposed, not deployed)

[`graph.html`](graph.html) opens the private interactive 78-node / 116-link curated P0–P5 knowledge graph. Click a gate for its **exact unclosed acceptance criteria**, then explore finite theorem records, candidate model identity, signed-current and infrared obligations, and **26 hashed archived files**. The six continuum gates are OPEN. The existing 740 indexed theorem paths and 78 legacy proof pathways remain a separate discovery snapshot; they are not certified by graph inclusion. Graph code and data are offline (`graph.css`, `graph-app.js`, `knowledge-graph-data.js`); human-reviewable text records are `knowledge-graph.json` and `data-manifest.json`. No original numerical arrays or transcripts enter Git.

Source generation: `python observatory/tools/build_knowledge_graph.py`. Structural, SHA, model-scope and status validator: `python observatory/tools/verify_knowledge_graph.py` (optional `--data-dir /path/to/uploads`). The mathematical/ethical acceptance protocol is [`KNOWLEDGE_GRAPH_CLOSURE_PROTOCOL_2026-11-04.md`](../docs/research/KNOWLEDGE_GRAPH_CLOSURE_PROTOCOL_2026-11-04.md). Source originals remain in **Library → The Singular Boundary → Data** pending user-configured Git LFS. Browser annotations are local-only and must be exported/imported as JSON for review; they cannot close the canonical gates.


## P0 review increment (private, stacked draft)

The updated [`graph.html`](graph.html) now displays **80 curated nodes and 122 typed edges**. A *finite* P0 cubic heat-kernel transfer-action candidate and an explicitly **conditional** scale-telescope correlation criterion have been added, with both source and assumption labels. The selected temporal heat-kernel/space Wilson action has finite-time transfer positivity and the fixed-spatial-grid Kogut–Susskind limit; **it is not proved equivalent in the continuum to the isotropic 4D Wilson action**, and supplies no uniform interacting state, OS continuum theory or positive mass gap. All 6 gates remain **OPEN**. Rebuild and verify with the existing `observatory/tools/build_knowledge_graph.py` / `verify_knowledge_graph.py` plus `research/scripts/verify_heat_kernel_p0_2026_11_04.py`. The original 740 catalog and 78 historical proof paths are separate and unchanged.

Audit: `research/audits/P0_CUBIC_HEAT_KERNEL_TRANSFER_CERTIFICATE_2026-11-04.md`; simulation JSON `docs/evidence/P0_HEAT_KERNEL_TRANSFER_CHECKS_2026-11-04.json`; no new raw binary data in Git.

## 2026-11-05 · Penrose-first correction (draft, no deployment)

The Observatory [Proof Atlas](graph.html) now distinguishes the **primary Penrose/Fibonacci/coupled-ℤ⁵ quantum-gravity hypothesis**, the **area-matched square 2D spatial control**, and the later cubic 3D SU(2) control. Quantum gravity and 4D Yang–Mills are **separate OPEN objectives**. The graph contains 91 curated nodes and 163 typed links, distinct from the unchanged 740 theorem-path catalog, 78 earlier proof pathways, and 26 original uploaded files.

The archived Stage 26 runner/README and nested Stage 7 geometry code were recovered and inspected from the historical Git tree. The Stage 7 model pairs a Penrose model-set torus (scale 55) with a square 151×151 torus matched in **total physical area**, uses 20 temporal slices and reference beta 3.5, and is a 2+1D SU(2) scalar correlation campaign. The Stage 26 field named source_sha256 is the **Stage 9 checkpoint hash**, not a hash of executable Python code. Neither the recorded multihit arrays nor their descriptive averages reproduce Paper 2's spectral-zeta ratio, prove gravitational finiteness, or establish a mass gap.

Reproducible data profiling: research/scripts/verify_penrose_square_pairing_2026_11_05.py. Graph builder applies a non-destructive postbuild hierarchy module observatory/tools/reconcile_penrose_control.py, using docs/evidence/P0_PENROSE_SQUARE_PAIRING_2026-11-05.json. Verify with python observatory/tools/verify_knowledge_graph.py --data-dir /path/to/uploaded/originals. Original binaries remain in Library pending LFS. No gate promotion or public deployment.

[Read the governing audit](../docs/research/P0_MODEL_HIERARCHY_PENROSE_CONTROL_AUDIT_2026-11-05.md).
