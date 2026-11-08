# PF-I5 — Publication-script provenance and cut-and-project implementation audit

**Date:** 2026-11-07 (America/Denver)  
**Research status:** implementation-origin correction, NOT recovery of original publication code, NOT closure of PF-G0 or any other continuum proof gate.  
**Authoritative requirement:** The original direct cut-and-project scripts and their complete parameters must determine the graph/operator, not a newly written de Bruijn surrogate.

## 1. Current direct answer and source inventory

**The original seven or eight publication scripts have not yet been located or read in full.** The supplied \`Sharpe_dissertation_v10.7.tar.gz\` (SHA-256 \`c405acd6daa5a0a923429ab659b122b22231787d7a30e97db7f2974f278354d1\`) has 18 regular-file members, consisting of PDF papers/experiments/dissertation and filesystem metadata; **zero** \`.py\`, \`.ipynb\`, \`.m\`, \`.r\`, \`.jl\`, \`.cpp\`, \`.c\`, or \`.sh\` scripts. The five published-paper PDFs each have zero embedded files. The available \`syncgravity\` GitHub repositories are \`singular-boundary\` and \`Tau\`; the former's current main Git tree contains 3,315 entries/697 Python paths, including later reconstructed research scripts and historical nested archives; a source-identified 7–8-file publication suite has **not** been authenticated. The current Library / The Singular Boundary / Source includes \`Archive 4.zip\` and subsequent simulation/proof code, but no identifiable original Paper 1–4 spectral-zeta executable package.

**Absence from inspected materials is NOT evidence that the author did not create those scripts.** We need the actual publication code archive, precise filenames, or immutable Git identifiers before any claim to have reviewed them line by line.

## 2. What the papers actually say

- **Paper 1 §6.1** explicitly labels its P3 construction "**the de Bruijn pentagrid construction**"; gives five grid families, offsets, cell ceiling labels, rhombi, and Fibonacci hopping by family and level.
- **Paper 2 §2.1** explicitly says the P3 vertex set is obtained "following de Bruijn" from accepted \(\mathbb Z^5\) points. Its coupled spectral operator and original numerical generator are **not** identified solely by that statement.
- **Paper 3 §4.1** explicitly presents **acceptance-window cut-and-project** in the perpendicular plane using a regular decagon \(W\).
- Those printed descriptions cannot be silently replaced by one another as algorithms for finite numerical graphs. A correct equivalence comparison must match phason offsets, integer embedding and height/sum layers, window faces and boundary conventions, retained vertices, edge weights, and final crop.

## 3. The specific PF-I2 methodological error

The current \`research/scripts/verify_pf_i2_pentagrid.py\` function \`generate()\` states:

\`\`\`python
"""Enumerate de Bruijn grid-line intersections and all resulting rhombi."""
\`\`\`

It computes intersections of grid-line pairs and generates rhombus corner labels, with independently selected projected radius and grid-level cutoffs; the offsets are \(\gamma_j=\operatorname{frac}(j\sqrt{2}+j^2\sqrt{3})-\mathrm{mean}\), satisfying sum \(\gamma_j=0\). It does **not** construct the finite vertex set by enumerating the acceptance-window membership of source-original integer points. It is an independent implementation of **published Paper 1 pentagrid equations**, NOT the original seven-to-eight-script cut-and-project package and NOT a source-byte reproduction of the Paper 2 or Paper 4 numerical matrices.

**Correction to previous language:** PF-I2 recovers *printed mathematical rules* only. Its 186/616-site graph checks and PF-I3/PF-I4 illustrative finite spectra are model-specific controls, **not** source-authenticated cut-and-project numerical reproductions. General combinatorial and linear-algebra lemmas remain scoped to their hypotheses, but model-transfer or source-uniqueness conclusions are not warranted.

## 4. A genuine later direct cut-and-project implementation exists — but it is not the publication source

The independent \`Archive 4.zip\` (Library: \`/The Singular Boundary/Source/Archive 4.zip\`; SHA-256 \`b9c2286ab19a49830d7a20446284620079a02bd39fb7b0be304ca33c62590709\`) contains \`Phase_III_Cut_and_Project_Recomputed.zip\`, with \`Phase_III_CutProject_Recomputation/direct_cut_project.py\`:

- It selects integer labels using **internal-window membership** and oriented \(\mathbb Z^5\) basis-neighbor squares, not the old grid-crossing face constructor.
- Its acceptance conditions use **four hypersimplex-slice windows** indexed by \(h=1,2,3,4\), together with \(\sum\gamma_j=1\), and a finite open-disk face crop.
- It records \`DEFAULT_GAMMA=(.07,.19,.31,.43,.61)\` normalized to sum one (plus offset-step phasons), **not** the same source offsets as the PF-I2 verifier.
- The bundled \`README.md\` explicitly calls \`phase2.py\` and \`legacy_phase2.py\` the old **unverified** pentagrid generators, warning **not** to call \`phase2.penrose()\` to produce corrected research data.
- \`test_direct.py\` tests the direct window construction, incidence, gauge checks, restart and **agreement with a separately audited pentagrid code under the same phason offsets and disk crop**. **All six tests pass** when run locally using NumPy/SciPy.
- Original bytes for the later source script \`direct_cut_project.py\`: SHA-256 \`2eea2dbf76bfc6ea4e47d27c0acaeb4b65718b13af4d1bbacf10169714db0486\`. Companion \`audited_penrose.py\` SHA-256 \`d26f26314752321ff1b5853846542231da5a54614ee9d91cfda9941b15a15a5c\`; \`test_direct.py\` SHA-256 \`5c47b602e490f6fd7d2ee2191dcb20eac00e90d4bd63495a419a166e04a57eb6\`.

**This cross-method agreement supports the later Phase III accepted finite graph under matched conventions. It does not certify PF-I2's different offsets, original Paper 2/4 spectral-zeta code, or Paper 3's source decagon as identical to the four-slice window model.** No nonlinear Yang–Mills, continuum or gravitational claim follows from this finite crosscheck.

## 5. Next required evidence: eight-script original publication package

Do not close PF-G0 or describe the original numerical implementation as reviewed until the actual accompanying scripts are provided and each file has:

1. Exact filename, byte SHA-256, code language, version, execution environment, entrypoint, dependency map, and publication/equation link.
2. Full line-by-line review of cut-and-project lattice dimensions, orthogonal/projective coordinates, offset and window selection, integer sum-layer constraints, boundary degeneracies, and optional phason enumeration.
3. Independent reconstruction of integer vertex IDs, accepted edges, Fibonacci weights, Laplacian diagonal and mass, periodic controls, zero-mode filters, and the 35%-interior rule.
4. Re-execution (or explicitly documented missing runtime dependency) producing the original per-size graph counts and the **same** matrices for Paper 2/4's reported zeta ratios and determinant flow.
5. An Observatory provenance record with source hashes, contradictory/reconciled claims, exact reproducibility receipts, and explicit distinction between original-script outcomes and later control calculations.

**Gate state:** original publication source-code identification **OPEN**; PF-G0 **OPEN**; P0–P5, PF-G0–G5, the physical Yang–Mills gap and gravity UV objectives **OPEN**. Do not silently promote finite structural equivalence into publication-code identity.
