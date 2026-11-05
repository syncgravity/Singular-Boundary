# The Singular Boundary — Proof Atlas closure and evidence protocol

**Private research source; 2026-11-04 America/Denver. Proposed Observatory v2.26-draft. The four-dimensional Yang–Mills existence and mass-gap problem is OPEN.**

## Purpose

The Proof Atlas is a curated, source-linked *research dependency* graph, not an evidence-validating inference engine. Its nodes identify (a) six P0–P5 proof gates, (b) the claimed final theorem, (c) candidate physical models, (d) precise submodel finite results, (e) proposed theorem interfaces, (f) unclosed mathematical/evidence work, (g) archived original binary/text files, and (h) a dissertation publication trajectory. Every edge has an explicit type, and **an edge is not automatically a proved mathematical implication**.

The canonical Observatory source snapshot v2.24 contains 740 indexed theorem paths and 78 proof pathways. These are preserved as a distinct discovery inventory. The 78 nodes and 116 edges of this draft atlas are *new curated objects*, not a replacement census and not a claim that all 740 files were independently audited.

## Source-model separations

- **Cubic**: an exact fixed-domain 3D geometric subdivision chain (R3-IR-586), a finite Gauss-invariant original-link KS reference (R3-IR-587) and a finite transfer positivity proposition (R3-IR-590). The cubic route is a benchmark for a full continuum construction, not yet such a construction. The prior R3-IR-586 already proved the geometry; November 4 P0 work provides **additional** tests and a specific naive *quantum* non-intertwining witness.
- **Historical coupled ℤ⁵ / Penrose**: dissertation v10.7 and supplied Stage26/Monte Carlo data; no source-certified genuine 3D nested SU(2) regulator equivalence to cubic or prism is established. Planar displacement data and integrity hashes are not evidence of a 3D continuum limit.
- **Extruded prism**: a constructed distinct oriented 3D *candidate*; not identified with the coupled ℤ⁵ generator and not yet a genuine directed refinement.
- **Straight strip**: corrected original-link 1D laboratory supporting exact P2/P4 progress (thermodynamic subsequences, P-77 five-state MPO, P-78 local Dirichlet/spectral measure); no automatic transport to the 3D spatial SU(2) action.

## Closure levels

The top-level numerical overview is **0 of 6 gates closed**. Each gate's checklist uses *met* only when a sharply scoped submodel statement is recorded and model-tagged, *partial* for incomplete interfaces, *open* for absent construction, and *blocked* for a documented model mismatch. A `met` sub-check does not mean the gate is closed.

The gate status is intentionally **not editable in the browser**. Any proposed new status must be source-linked, receive a clear statement of hypotheses and units, and be audited under `docs/research/HISTORICAL_RECORD_ACCEPTANCE_GATE_2026-11-01.md` before the canonical ledger changes. A personal browser flag (`needs-proof`, `needs-evidence`, `review-ready`) never counts as a theorem certificate.

The overall target demands a nontrivial four-dimensional OS-reconstructible SU(2) continuum QFT in the physical Gauss sector and a common gap Δ>0 in fixed physical energy units after both spatial volume and true 3D h→0 limits. A dense-family positive-time exponential estimate would be a *conditional* bridge if its hypotheses are independently constructed and verified. Positive moments, high-frequency spectral mass, finite-dimensional Ritz gaps, and all-finite-graph energy gaps are insufficient.

**P3** remains a *route-specific* Penrose Wilson-current/anti-depletion candidate and is not a universal axiom for every constructive cubic strategy.

## Protocol for adding a node and moving toward CLOSED

1. **Locate and pin source**: immutable file path and blob identity (if Git), or original file name, byte count and SHA-256 (if Library). For theorem statements, cite the statement actually supported by the source; for user-proposed work, label it a proposal.
2. **State physical scope**: model, gauge group, spatial dimension, operator domain, coupling, normalization, quantifiers, and whether the conclusion survives changes of scale and volume.
3. **Label evidence honestly**: `indexed`, `archived`, `candidate`, `finite`, `conditional`, `partial`, `obstruction`, `unresolved`, `open`. Only a reviewed full acceptance packet could create a distinct `closed` status; this draft contains none.
4. **Define closure criterion**: name the **missing lemma** and sufficient source-visible verification or reproducible regression. A task without acceptance criteria is research backlog, not evidence of closure.
5. **Demonstrate the interface**: prove the common-model operator and scale transfer before drawing a substantive dependency as `licensed`. Records from different models may have `candidate` or `model-blocked` edges, never silent equivalence.
6. **Review and version**: export user review notes to JSON, propose a PR with proof and validator changes, retain rejected/historical claims and their dates, and never silently modify the canonical claim ledger. Pages remains disabled/manual until explicitly authorized.

## Graph UI

`observatory/graph.html` runs with local `graph.css`, `graph-app.js` and `knowledge-graph-data.js`. It uses no external CDNs, APIs, telemetry, or remote JavaScript. Lenses: Proof spine, Evidence network, Open work, Data & provenance, Entire atlas. Search, click, pan, zoom, drag, keyboard selection, shift-click shortest relationship path, source links, datasets with SHA/Library custody, and locally saved personal annotations are supported. The graph JSON is exported directly. Import/export review notes use schema `singular-boundary.review-annotations.v1`; they are **not** automatically synced to GitHub or the Library.

`observatory/knowledge-graph.json` is human-reviewable canonical graph metadata. `knowledge-graph-data.js` is the generated offline JavaScript wrapper. `observatory/data-manifest.json` contains 26 SHA-256 source-file references but **no original numerical arrays or transcript bodies**. Run `python observatory/tools/verify_knowledge_graph.py` to check structural invariants, then `python observatory/tools/verify_knowledge_graph.py --data-dir /path/to/uploads` to compare the actual binary/text bytes.

## Data custody and Git LFS migration

Originals are preserved under **Library → The Singular Boundary → Data → Original Uploads / Source Conversations**. The 19 original dissertation/simulation/geometric files consist of eight 100-checkpoint Stage26 compact archives, eight sweep-10000 NPZs, one full Penrose seed-101 ZIP, one Whitney 11-face NPZ, and the dissertation tarball; plus seven transcript files for **26** total. Compact ZIP CRC checks and individual attached-file SHA-256 checks have been performed. No scientific claim follows solely from CRC or hash verification.

Once LFS is configured by the project owner, create a controlled migration mapping `file`, `bytes`, `sha256`, `library_path`, `git_lfs_path`, `lfs_oid`, and `verification_status`; fetch from Library, compute the same SHA-256, commit pointer objects only, and independently verify the pointers/objects before altering graph custody labels. No LFS migration or automatic Git binary commit is done by this work.

## Known review boundaries

- 740 indexed paths and 78 previously mapped proof routes are frozen-source metadata, not all independently certified; historical claim collisions remain unresolved.
- Graph render tests establish DOM interaction, SVG navigation, and editable local annotations, not mathematical correctness.
- Numerical simulation bytes are retained and hash checked but not independently validated as a source-certified 3D SU(2) regulator.
- This is a **draft stacked on the existing draft PR #57**, and no public deployment or canonical acceptance change is authorized.

**Reference:** `docs/research/PROOF_DEPENDENCIES.md`, `docs/research/REPOSITORY_REVIEW_AND_P0_OBJECTIVE_2026-11-04.md`, and the PR #55/#56/#57 research audits cited within the graph.
