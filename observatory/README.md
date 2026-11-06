# Research Observatory v2.38-draft — Mathematical Physics Proof Atlas


## Finite three-dimensional transverse-shell result · scope-limited (2026-11-06)

The first full `2×2×1` cubic spatial slab about a four-face block has 20 plaquettes, including 12 transverse xz/yz faces. For the **positive truncated** SU(2) magnetic weight `1+λ tr U_p` (not the Wilson exponential or time-transfer action), exact Haar integration of 25 interior links gives `Z(U;λ)=P0(λ)+P1(λ)χ1(U)+E12`, with `P0=1+λ⁶/4+λ¹⁰/64`, `P1=λ⁴/8+λ⁸/32+λ¹⁰/128`, and an explicit finite sup-norm bound on `E12`. A single transverse cubical bulge supplies `λ⁸χ1/32`, the first shell correction; the full 16-face outer sphere supplies the **exact adjoint character coefficient** `λ¹⁶/16384`. This calculation checks actual **3D spatial** magnetic coupling, but is **not** a physical-time interacting correlation estimate, a 3D Wilson-exponential RG theorem, a refinement-uniform estimate, or a Penrose equivalence. It **closes no P0–P5 or T0–T5 gate**.

See [exact 3D transverse-shell report](../research/theorems/R3_CUBIC_FIRST_TRANSVERSE_SHELL_CHARACTER_BLOCK_2026-11-06.md) and its [reproducible verifier](../research/scripts/verify_cubic_transverse_shell_2026_11_06.py). The 2²⁰ squarefree face configurations were enumerated independently; only 32 pass the Haar center-parity test, while all higher-order non-manifold channels were bounded without unjustified factorization. The next step is **the full Wilson exponential plus temporal heat-kernel transfer, with the nonabelian recoupling channels included**, not a claim of a continuum gap.

**Source status:** v2.37-draft review branch stacked on PR #63; v2.29 remains integrated on the private `main` branch. **Mathematical status:** all P0–P5 continuum Yang–Mills gates and the independent quantum-gravity objective remain **OPEN**. Merging the site is not proof acceptance or permission to publish it publicly.

## Explore the proof

- [Observatory overview](index.html) — the complete proof-program entry point, P0–P5 dependencies, routes, obstructions and source catalog.
- [Interactive Proof Atlas](graph.html) — 108 curated mathematical-physics nodes and 208 typed edges; starts on the **Cubic → Quasicrystal** model-transfer view.
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

## Finite full-Wilson and two-step temporal memory checkpoint · November 6, 2026

The 2×2×1 slab now uses the **normalized full Wilson exponential** rather than the positive truncated plaquette polynomial. Four five-face complementary caps generate an exact all-spin SU(2) character kernel; the first transverse coefficient is exact at arbitrary bottom coupling, and higher shell supports carry an explicit sup-norm bound. The cap kernel itself contains an order-seven Taylor correction—distinct from the fact that there are no new six/seven-face supports. On the same original-link finite cubic Hamiltonian, positive symmetric SU(2) heat-kernel transfer exhibits **strict positive vacuum memory** under spatial Haar projection, with leading two-time discrepancy ε²×(20 β_h²/4). This is a **finite** dynamical obstruction to Markovian projection, not a continuum mass-gap or positive physical-time infrared theorem.

Sources: `research/theorems/R3_FULL_WILSON_3D_SHELL_AND_TEMPORAL_MEMORY_2026-11-06.md`, `research/scripts/verify_wilson_shell_time_2026_11_06.py`, `docs/evidence/R3_FULL_WILSON_3D_SHELL_TIME_MEMORY_2026-11-06.json`, `observatory/tools/add_wilson_time_graph.py`. The continuing **OPEN** gate is a renormalized multiscale two-time influence kernel and uniform interacting connected correlations. v2.37-draft contains **108 physics nodes / 208 typed edges**, 26 original file hashes; all six Yang–Mills gates remain OPEN. No merge into main or public Pages deployment has occurred.

## Exact finite two-time influence across two cubic refinements · November 6, 2026

The physical original-link Wilson/Kogut–Susskind Hamiltonian is decomposed into the retained eight-boundary-holonomy-product sector P and its complement Q. The interaction block B=QHP has the **exact all-coarse-state** identity `B*B=(beta_h² F_h/4)P`. This supports a rigorously positive non-Markovian Volterra memory `B*e^{-tQHQ}B` and an energy-dependent Feshbach self-energy, with explicit finite-resolvent upper and lower bounds; the positive symmetric transfer has an exact all-step discrete memory recurrence. On the **same physical 3D slab** a `2×2×1` mesh (20 faces, 33 edges) refines to `4×4×2` (128 faces, 170 edges), with matching eight coarse boundary products. The **bare zero-time influence ratio is `(128/5)[g0(h)/g0(h/2)]⁴`**. It is not a renormalized physical divergence or a spectrum result. The graph has 111 nodes and 218 links; all P0–P5 gates, Penrose transfer and physical quantum-gravity claims remain OPEN.

Read the [full proof](../research/theorems/R3_EXACT_TWO_TIME_INFLUENCE_AND_DYADIC_SCALING_2026-11-06.md), [reproducible verifier](../research/scripts/verify_two_scale_influence_2026_11_06.py), and [new model-specific graph overlay](tools/add_two_scale_influence_graph.py). Source bytes and verification archives are preserved in Library → The Singular Boundary → Proof Audits → Two-Scale Influence Kernel 2026-11-06. This is a stacked **draft**, not merged into canonical v2.29 main and not publicly deployed.

## Finite interacting-vacuum coarse observables and full Schur form · 2026-11-06

A positive smooth finite SU(2) Wilson ground state Ω provides a **true-vacuum probability law** Ω² dHaar, whose conditional marginal ρ on the same eight coarse physical boundary holonomies defines an isometric, gauge-invariant local observable map. Unlike bare Haar projection, its P/Q mixing on the vacuum vanishes; on nonconstant coarse Wilson probes the exact off-diagonal strength is **four times the conditional variance of the ground-state logarithmic-score drift**. The projected generator is `-a ρ^-1 div(ρ grad)` with `a=α_h` or `2α_(h/2)`, and the complete energy-dependent effective operator is defined by a valid **variational shorted form**, not by silently applying the bounded-block Feshbach formula to an unbounded drift.

An analytically solvable **SU(2) one-vertex/two-loop gauge graph** has identical coarse Haar law and compressed generator to a free coarse rotor, yet strictly different physical-time two-point correlations. The counterexample is **not** the cubic Wilson action and is not a mass-gap result. The finite model provides an exact observable-map **candidate** but no computable or uniform control of Ω, ρ, induced potentials, conditional-score variance, full Schur forms, or nontrivial 4D continuum. Status: **115 nodes / 231 typed edges**, all P0–P5 OPEN. Original 26 source archives remain unchanged in Library.

[Finite interacting-vacuum theorem](../research/theorems/R3_VACUUM_WEIGHTED_OBSERVABLE_MAP_AND_SCHUR_FORM_2026-11-06.md) · [independent SU2 verifier](../research/scripts/verify_vacuum_weighted_block_2026_11_06.py) · [new model-scope overlay](tools/add_vacuum_weighted_block_graph.py). This v2.37-draft is stacked on PR #66, not merged or deployed.

## Exact finite Wilson marginal bounds and a physically fixed loop · November 6, 2026

For the *actual* finite cubic interacting SU(2) Wilson ground state Ω, a direct Feynman–Kac + Peter–Weyl heat-kernel minorization gives the explicit true-vacuum marginal pointwise estimate **exp(−2Λ)≤ρ≤exp(2Λ)**, with **Λ=64F/g₀⁴+E log(101/99)**. Every finite fundamental Wilson loop consequently has positive variance bounded below. **This global estimate is drastically nonuniform in F,E and weak bare coupling** and is not an infrared theorem.

For a non-self-intersecting loop of L original elementary links, the exact centered normalized first spectral moment is **−C′(0)=α L Eρ(1−W²/4)/Varρ(W)**. In the fixed physical unit square, L=4n on an n³ mesh. Assuming the **unproved** adjacent-scale marginal comparison |log(ρf/ρc)|≤δ, the raw first moment ratio lies in **4[g₀(h/2)²/g₀(h)²] exp(±2δ)**. A positive spectral counterexample shows diverging first moments can coexist with a strictly positive infrared gap, and a bounded-source Hellinger estimate explicitly depends on the finite spectral gap—hence using it to infer a uniform gap is circular.

**Proposed Observatory v2.37-draft:** 124 curated physics nodes, 260 typed links, and the 26 original file hashes unchanged. The four new entries separate finite marginal control, finite Wilson sum rule, conditional time-normalization comparison, and an **OPEN** local/multiscale renormalization task. **All P0–P5 continuum gates and the gravitational objective remain OPEN.**

[Finite theorem and proof](../research/theorems/R3_FINITE_WILSON_MARGINAL_HARNACK_AND_TWO_SCALE_SUM_RULE_2026-11-06.md) · [independent checker](../research/scripts/verify_marginal_harnack_2026_11_06.py) · [idempotent graph overlay](tools/add_marginal_harnack_graph.py). Source and SHA-256 evidence preserved in Library → The Singular Boundary → Proof Audits → Marginal Harnack and Wilson Sum Rule 2026-11-06. Review branch is stacked on PR #67, not merged or publicly deployed.

## Gap-independent local Wilson Fisher and fixed-mesh thermodynamic subsequences · November 6, 2026

The cubic original-link SU(2) Wilson vacuum now has a **volume-independent local kinetic-energy estimate**, proved by excising a link and incident plaquettes and comparing the true interacting ground energy with a Haar-constant trial state on those links: **αΣ_{e∈S}⟨Cₑ⟩ + Σ_{p touching S}⟨Vₚ⟩ ≤ β·#{plaquettes touching S}**. Every original cubic link touches at most four faces. The actual interacting marginal for an arbitrarily long *simple physical Wilson-loop holonomy* therefore obeys **∫|∇√ρ_C|²≤16/g₀⁴**, with no dependence on the box size or contour's number of elementary edges. Compact SU(2) Sobolev and Haar trace anti-concentration give an explicit strictly positive **Wilson variance lower bound uniform in volume at fixed g₀**, avoiding the previous global Harnack factor proportional to E/F.

At fixed h,g₀, the local Wilson densities consequently possess **strong-L¹ thermodynamic subsequences** and their centered Wilson spectral measures are tight with bounded first moments; no uniqueness, infrared spectral exclusion, h→0 construction or 4D OS theorem is implied. The Fisher bound **degrades as g₀⁻⁴** under the actual weak-bare-coupling continuum trajectory; a scale-uniform renormalized local marginal and full time-dependent Schur comparison are still OPEN. This is a stronger local result than the older global Harnack, but not a pointwise local Harnack or continuum renormalization.

**Review graph v2.37-draft:** 124 curated mathematical-physics nodes / 260 typed edges. 26 original archive hashes unchanged; P0–P5 and quantum-gravity objective remain OPEN. Source [theorem](../research/theorems/R3_LOCAL_INTERACTING_SU2_FISHER_AND_THERMODYNAMIC_SUBSEQUENCE_2026-11-06.md), [independent checks](../research/scripts/verify_local_link_fisher_2026_11_06.py), [idempotent overlay](tools/add_local_fisher_graph.py). Reproducibility package and checksums are preserved in Library → The Singular Boundary → Proof Audits → Local Wilson Fisher and Thermodynamic Subsequence 2026-11-06. Stacked draft on PR #68; no main merge, Git LFS change or public deployment.

## Gauge-equivariant spatial Wilson flow and Fisher–gap obstruction · November 6, 2026

The previous local SU(2) Wilson-vacuum theorem gives a volume-independent but g₀⁻⁴-degrading **Fisher** estimate. The new *exact* compact SU(2) smooth class-rotor example shows Fisher(ρ)≤3 and Var_ρ(trU)≥1 can coexist with a positive **class-sector spectral gap ≤ε→0**. This model has an explicit conjugation-invariant class potential **different from the cubic Wilson action**. Its scope is to reject an invalid inference, not the Yang–Mills conjecture.

A separate **finite gauge-equivariant 3D spatial Wilson-action flow** defines a genuine flowed link-field observable: **||Hess S_W||≤4**, **||DΦ_s||≤e^{4s}**, with a factorial decay bound for dependence on distant original links at fixed *lattice* flow time. On an isolated plaquette the flowed trace is a nonlinear SU(2) class function with exactly solvable evolution. Crucially, *group heat convolution of a single fundamental Wilson character* merely scales it by e^(−3s/4), leaving its normalized deterministic physical-time correlation unchanged. Externally smoothing the readout marginal is **not** the gauge-field flow.

For a finite *true interacting* Wilson ground state, the exact covariance–Dirichlet matrix relation is **−C′_a(0)=α_h(aᵀG_h a)/(aᵀS_h a)**. Uniform control would provide ultraviolet first-moment tightness for selected normalized states, **not** a positive infrared gap. Current worst-case gradient-flow bounds do **not** remain uniform at fixed physical radius s=t_phys/h². A complete four-dimensional physically normalized flowed field and its **full interacting Schur/long-time correlations** remain an **OPEN** P2/T2/T3 interface. No quasicrystalline regulator equivalence or quantum-gravity UV result.

**Review graph v2.37-draft:** 128 nodes, 275 typed edges, 26 unchanged original-file provenance records, all six YM gates and independent gravity goal OPEN. [Proof and scope](../research/theorems/R3_GAUGE_COVARIANT_SPATIAL_FLOW_AND_FISHER_GAP_OBSTRUCTION_2026-11-06.md) · [verified program](../research/scripts/verify_spatial_wilson_flow_2026_11_06.py) · [source-pinned overlay](tools/add_spatial_flow_fisher_gap_graph.py). Research ZIP and SHA-256 manifest in Library → The Singular Boundary → Proof Audits → Spatial Wilson Flow and Fisher Gap 2026-11-06. Stacked draft on PR #69; no merge or public deployment.

## Fixed physical-radius linearized 3D curvature flow and nonlinear plaquette audit · 2026-11-05

Starting from the **same** finite gauge-equivariant spatial Wilson flow, the exact quadratic expansion at a flat SU(2) connection is (S_W=(1/8)||d_1a||²+O(a³)), so (partial_s a=-(1/4)d_1^*d_1a) in the linearization. At a **fixed physical flow time** (	au=h²s>0), its Lie-algebra curvature obeys (F_h(	au)=exp[-	au d_1d_1^*/(4h²)]F_h(0)). Positive spectral calculus supplies the **uniform-in-(h,R)** bound (||L_h^{k/2}F_h(	au)||≤[2k/(e	au)]^{k/2}||F_h(0)||), (L_h=d_1d_1^*/h²); this is exact for the **flat-field linearization**, not the full nonlinear interacting theory. For a separate **periodic cubic Fourier reference**, each fixed transverse mode converges to its physical heat multiplier at **O(h²)** with explicit constants.

In a distinct, **nonlinear isolated four-link SU(2) plaquette with free-Haar/electric vacuum**, deterministic long spatial flow has (operatorname{Var}(x_s)sim4sqrt2arepsilon^{3/2}) and normalized initial electric moment (simalpha/(4arepsilon)), (arepsilon=1-	anh s); positive-time free-electric correlations collapse despite unit normalization. This is **not** a counterexample to nonperturbative 4D Yang–Mills or to a fixed-physical-size Wilson loop along refinement. It demonstrates why variance and spatial smoothing alone are inadequate.

**Draft v2.37:** 128 curated mathematical-physics nodes, 275 typed relationships, 26 immutable original-file references. All six YM continuum gates, all Penrose transfer obligations and the separate gravitational UV objective remain **OPEN**. [Exact flat-field and Haar proof](../research/theorems/R3_FIXED_PHYSICAL_RADIUS_LINEARIZED_CUBIC_FLOW_2026-11-05.md) · [reproducible verifier](../research/scripts/verify_physical_radius_linearized_flow.py) · [graph overlay](tools/add_physical_radius_linear_flow_graph.py). Source archive and SHA-256 manifest are preserved in Library → The Singular Boundary → Proof Audits → Physical-Radius Linearized Cubic Flow 2026-11-05. Stacked draft on PR #70; no main merge, public deployment or Git LFS action.

## Exact full nonlinear 3D cubic physical-action dissipation · 2026-11-06

The previous v2.37 result is **flat-field linearized smoothing**. This checkpoint proves an exact **nonlinear classical** gauge-equivariant spatial Wilson energy identity at fixed physical flow time `tau=h²s`: `E_h(Phi_{tau/h²}U)+8 integral_0^tau h^-3 sum_e |grad_e S_h|² dt=E_h(U)`, `E_h=8S_h/h`. If total initial classical energy stays bounded as h changes, evolving energy and **time-integrated** force have bounds with no new mesh-dependent constants. The nonlinear result is **not** a uniform pointwise curvature-derivative estimate or a result about the interacting quantum vacuum.

Energy positivity yields conditional small plaquette holonomy `theta_p≤(pi/2)sqrt(h E_initial)` and weak compactness of the **positive curvature-energy measures** on a fixed compact physical box. However, a genuine SU(2) one-link configuration `U_e=exp(sqrt h T3)` has total physical energy tending to 4, `theta_p/h²=h^-3/2`, and an **atomic energy-measure limit 4 delta_center at initial flow time**. Thus classical action bounds alone cannot give diffuse curvature or full nonlinear parabolic regularity. Smooth continuum classical initial connections do have bounded physical action under exact link holonomy sampling.

For the **actual finite interacting SU(2) Wilson vacuum**, strict positivity and full Haar support of its ground-state density, combined with finite flow as a diffeomorphism, guarantee a **nonzero variance at every finite h and finite flow time** for any nonconstant flowed Wilson loop. This does not provide a uniform covariance lower bound; averaging the classical identity over the true vacuum requires a uniform *initial unrenormalized physical action* expectation, which is not established and may be inappropriate without quantum UV renormalization. The complete physical-time Schur/long-time gap problem remains OPEN.

**Proposed private v2.38-draft:** 132 mathematical-physics nodes, 288 typed edges, unchanged 26 original source identities, all P0–P5 YM gates and separate gravitational UV objective OPEN. [Theorem](../research/theorems/R3_NONLINEAR_CUBIC_PHYSICAL_ENERGY_DISSIPATION_2026-11-06.md) · [executable checker](../research/scripts/verify_nonlinear_energy_flow.py) · [source-pinned overlay](tools/add_nonlinear_energy_graph.py). Exact reproducibility archive and SHA-256 manifest preserved in Library → The Singular Boundary → Proof Audits → Nonlinear Cubic Physical Energy 2026-11-06. Stacked review draft on PR #71; canonical main v2.29 and public Pages untouched.
