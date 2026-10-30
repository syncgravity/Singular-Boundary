# Canonical research state — 2026-10-30

**Read this first.** Git `main` is the canonical research record. Conversational outputs and Library ZIPs are **sources to reconcile**, not authoritative proof or completed repository imports. The historical audit branch was fast-forwarded to main; 245 additional commits were preserved without rewriting existing history.

## What the repository currently proves or records

The original archived R3-PRISM, R3-IR, D1, R2 tracks remain logically distinct. The repository contains extensive original Stage 7–35 numerical/provenance audits, many finite-volume SU(2) theorems, counterexamples, and conditional comparison arguments. None constitutes a complete nonperturbative continuum Yang–Mills mass-gap proof. Read specific statements in `research/theorems/` and their corresponding entries in `research/claims/CLAIM_LEDGER.csv`; do not infer universal results from file titles alone.

The 2026-10-30 handoff's **CI-1/CI-2** (now `research/theorems/CONDITIONAL_HAAR_INCOMPLETE_CAGE_CI1_CI2_2026-10-30.md`) is an exact finite-volume result for *incomplete* cages: the deleted target trace is Haar and independent of retained traces; bounded retained components have a conditional defect bound of order (M b^{-1/2}). It does not apply to a completed connected magnetic cage. Its source companion scripts and certificates still require archival reconciliation.

The 2026-10-30 `COMPLETED_CAGE_CUT_COMPARISON_2026-10-30.md` proves a **small perturbation** comparison under (2sbc_r<\gamma_0), with rare-cap denominator loss. It does not cover generic strong-coupling completion.

A prior branch records an **exact** signed radial-score identity and a *sufficient conditional gate* for downstream comparisons:
[
\mathfrak T_{f,h}=\frac4{A_f}\int_0^{\pi/2}\frac{[-C_{f,h}(\cos u)]_+}{\sin u}\,du,
\qquad \sup_{f\in D_R}\mathfrak T_{f,h}=o(h^{-1/4}).
]
The uniform physical interacting-vacuum estimate on the right **is open**; neither a Gaussian sign, a harmonic argument, nor a spatially averaged defect bound closes it.

## Prioritized proof dependency map

1. **Completed-cage nonlinear target response:** derive an angle-uniform or suitable one-sided score-current bound for the actual Gauss-invariant Wilson vacuum, with the target-dependent kinetic metric, low collective energy and boundary/volume constants retained. No fast-mode gap may be presumed.
2. **Bulk comparison:** only after step 1, establish the declared magnetic-deletion/cap survival bounds and fixed-support Wilson-angle comparisons with full coefficients and uniformity.
3. **Connected correlations / R3-IR:** independently control the required source-inserted low-energy sector and connected covariance. The Oct 29 repository review identifies a different low-energy spectral response gate at cutoff (Lh^{-11/8}); it has NOT been proved equivalent to the radial-current gate. Track both.
4. **R3-PRISM:** source-locate the original twelve-prism insertion and complete its fixed/integrated-boundary comparison. Its logical connection to the Hamiltonian approach is not established.
5. **D1/R2 and reconstruction:** finish production-action normalization, physical temporal/spatial limits, positivity and continuum spectral reconstruction before any continuum mass-gap claim.

## The next proof experiment

On a minimal completed-cage original-link disk, formulate the target-angle conditional quadratic form and score-current Ward identity without taking positive parts prematurely. Compare cut/open and completed support as a *finite volume* theorem and quantify exactly where the global spectral-gap cut estimate fails. Attempt a local signed comparison with constants explicit in (h), component diameter, and boundary conditions. Run deterministic tests as diagnostics, not proofs. A viable proof must address arbitrarily large complete Penrose interiors.

## Repository integrity gaps (OPEN)

- Historical `README.md` and `docs/current/STATUS.md` were frozen at 2026-10-28 and should be read as historical snapshots, not the latest proof.
- Earlier review said 75 theorem reports and 67 audit scripts. The live 2026-10-30 tree has **85 theorem files and 79 scripts across the scripts subtree** (different counting scope); counts are provenance indicators, not proof certification.
- The repository is not the complete prepared 602-source import; historical source text, binary assets, and Oct 29–30 ZIP deliverables still need verified source-by-source reconciliation.
- Source `PROJECT_HANDOFF.md` refers to a full verification bundle, but its embedded tests/certificates have not all been checked against Git.
- ChatGPT cannot assume access to every chat in a Project. Only actually surfaced transcripts, Library materials, and mounted files can be inventoried. Missing histories must be marked unavailable, not silently reconstructed.

## Rules

Every new theorem must have a precise source, hypotheses, evidence status, and claim-ledger mapping. New research changes should be committed to `main`, verified by re-reading GitHub, and mentioned by full SHA. Preserve historical records; avoid destructive renames and force-pushes. For large binary data use an explicit archival transfer and compare byte hashes.

## 2026-10-30 additional completed-cage result (R3-IR-377)

The actual Gauss-invariant Wilson ground state on **any fixed finite magnetic cage**, including completed cages, has a pointwise positive density whose oscillation is bounded by an explicit *global* heat-kernel comparison constant `R_t=exp(tK) M_t/m_t` (`K=2b sum c_q`; `m_t`, `M_t` the positive minimum and maximum of the free original-link heat kernel). Therefore the center cap has at least `R_t^-2` times its Haar mass. Full proof: [COMPLETED_CAGE_FINITE_VOLUME_CAP_POSITIVITY_2026-10-30.md](../../research/theorems/COMPLETED_CAGE_FINITE_VOLUME_CAP_POSITIVITY_2026-10-30.md). This is nonperturbative and valid at every finite coupling, **but the constant depends badly on magnetic volume, link dimension and coupling**, so it does not prove any of the required uniform signed radial-current or mass-gap estimates. It supplies a valid finite-volume baseline for a local comparison program.

## October 26–30 Paper3 / R3-IR / R2 historical archive intake

The chronological Paper3, weighted-Wilson, Penrose-J, R3-IR and R2 conversation has a [retrospective research sequence](../../sources/conversations/2026-10-26_TO_2026-10-30_PAPER3_WILSON_R3R2_RETROSPECTIVE_CHRONOLOGY.md) and [claim-level crosswalk](../../research/theorems/R3_R2_CONVERSATION_CLAIM_CROSSWALK_2026-10-30.md). This is **not an original verbatim transcript**; native conversation identifiers remain unavailable. Six narrow claims were entered as R2-003..005 and R3-IR-378..380, without modifying earlier conclusions. Local source intake identifies 90 mounted original streams, but no new remote Git LFS byte preservation is claimed. See [the 90-file source package register](../../sources/source-manifests/THIS_CONVERSATION_RECOVERED_ORIGINALS_2026-10-30.md) and [source-gaps ledger](../evidence/SOURCE_RECONCILIATION_GAPS_2026-10-30.csv).

**Correction preserved in time:** The Oct26 lack of the Stage7 action builder was superseded by the Oct28 D1 deterministic source/incidence certificate. It does not imply full production checkpoint input certification, quantum spatial continuum reconstruction or physical uniform spectral gap. All interacting center-neutral frame contraction and R2 continuum gaps remain OPEN.

## Further exact completed-cage reduction: local score Fisher contraction (R3-IR-378)

[Exact target score/Fisher theorem](../../research/theorems/R3_IR_TARGET_SCORE_FISHER_CONTRACTION_2026-10-30.md): for the true finite-volume physical Wilson vacuum and target trace p, set κ(p)=A_f(1-p²)/4 and J(p)=E[Γ(p,log Ω)|p]. The radial likelihood ratio r=ρ/w obeys κ∂p log r=2J and the one-face Fisher contraction ∫κ|∂p log r|²ρ≤4E[Σ_{e∈∂f}a_e|∇_e log Ω|²]. This replaces a global K-dependent positivity comparison by an **exact local electric-score-energy inequality**, but the radial score estimate is probability-weighted; the needed positive signed-current integral is unweighted, so the proof gate remains open. Its next step is a regulator-robust conditional lower density or signed score control, not an assumed spectral gap.

## Signed-score capacity obstruction (R3-IR-379)

[The smooth SU(2) class-amplitude capacity counterexample](../../research/theorems/R3_IR_FISHER_TO_SIGNED_SCORE_CAPACITY_OBSTRUCTION_2026-10-30.md) proves that arbitrarily small **Haar-weighted radial Fisher energy** can coexist with arbitrarily large one-sided center-score variation, by placing a deep logarithmic depletion in a shrinking target cap. It is a functional-analytic counterexample, **not** a genuine Wilson-ground-state counterexample. Thus the exact Fisher contraction in R3-IR-378 and the regional Agmon energy estimates cannot by themselves imply the desired signed-current bound. The ground-state eigenvalue equation must supply a regulator-uniform anti-depletion or signed response principle. This prevents further unsupported attempts to transfer weighted energy directly to unweighted cap variation.

## 2026-10-30 Harnack–Fisher annular reduction (R3-IR-380)

An examination of the pre-existing Oct 29 [local one-link heat-kernel theorem](../../research/theorems/R3_IR_DELETED_FACE_LOCAL_HEAT_HARNACK_2026-10-29.md) confirms it is already volume independent and stronger than the Oct 30 **global** Feynman–Kac constant. Combined with the exact marginal Fisher contraction, the [new annular bound](../../research/theorems/R3_IR_HARNACK_FISHER_ANNULAR_CURRENT_2026-10-30.md) controls positive radial-score variation on any fixed interval `0<alpha<beta<=pi/2` by `R sqrt(I_f/A_f)*sqrt((pi/2)(cot(alpha)-cot(beta)))`, where `R` is the old local Harnack constant. The factor blows up as `alpha->0`, and `R` is at best exponentially costly at the physical strong-field scale under known results. **No signed full-cap current estimate or continuum gap follows.** Record this as an exact consequence of two earlier results, not a discovery of local Harnack itself.

## Fixed-volume center endpoint regularity — R3-IR-381

The [exact true-vacuum endpoint theorem](../../research/theorems/R3_IR_TRUE_VACUUM_CENTER_ENDPOINT_REGULARITY_2026-10-30.md) proves that the target marginal ratio to SU(2) Haar extends smoothly and positively through both group center points, for each fixed finite magnetic cage. Hence the signed radial score vanishes linearly as `u→0`, and the conditional current `J_f(p)` vanishes as `1-p²` at the endpoints. The apparent annular Cauchy–Schwarz singularity is not a genuine singularity of the fixed-volume physical score. An exact split bound combines the local derivative supremum on a center collar with the previously proved annular Harnack–Fisher estimate. **The derivative constant has no proved scaling-uniform bound**, so the needed `o(h^-1/4)` signed-current estimate and mass gap remain open. Next step: physical ground-state equation controls the center-collar derivative or integrated signed current with constants uniform on complete Penrose cages.

## Independent Proof Reconstruction archival reconciliation — 2026-10-30 (historical intake only)

The separate conversation *The Singular Boundary — Independent Proof Reconstruction and Verification* has a [partial, explicitly secondary chronology](../../sources/conversations/2026-10-28_INDEPENDENT_PROOF_RECONSTRUCTION_PARTIAL_CHRONOLOGY_2026-10-30.md), a [85-file byte-source handoff register](../../sources/source-manifests/INDEPENDENT_PROOF_85_FILE_HANDOFF_REGISTER_2026-10-30.md), and an [integrity and duplicate-ID erratum](../evidence/INDEPENDENT_CONVERSATION_ARCHIVAL_AND_ID_ERRATA_2026-10-30.md). The exact 6,253-byte signed-current *assistant fragment* is archived in regular Git as a fragment, not a native full transcript. All other binary original transfers remain local **until Git LFS push and clean-clone hash verification**. The two historical duplicate IDs R3-IR-378/379 must be source-disambiguated using reserved archival aliases R3-IR-9001/9002; later R3-IR-381 is a separate genuine center-endpoint claim.

**No change to the mathematical verdict:** actual interacting completed-cage uniform signed current, fixed-support connected covariance, regulator-uniform physical spectral gap, R2 quantum continuum reconstruction and 3+1D Yang–Mills remain OPEN. See the original proof ledger for precise finite-model hypotheses, and do not promote packaged assistant claims to independently reverified mathematics based on their ZIP filenames alone.

## 2026-10-30 center-fiber eigen-equation reduction (R3-IR-382)

[The exact original-link center-jet identity](../../research/theorems/R3_IR_CENTER_SLICE_EIGEN_EQUATION_JET_2026-10-30.md) expresses the endpoint derivative of the true radial likelihood ratio as a smooth conditional fiber integral of the original-link Wilson eigen-equation. In particular, the other-link electric operator must be evaluated **before** fixing the moving holonomy slice; it cannot be integrated by parts as if that slice fixed the chosen link. The identity holds for a complete magnetic cage at fixed finite volume, but gives neither the sign nor a Penrose-uniform estimate. Its required continuation is a signed center-collar variation bound, not another formal endpoint identity. The archival claim-ID collision audit elsewhere in this status remains in force; R3-IR-382 is the new center-jet row, and does not resolve the earlier duplicate IDs.

## Optimized completed-cage center-collar criterion (R3-IR-383)

The [optimized splitting calculation](../../research/theorems/R3_IR_OPTIMIZED_CENTER_COLLAR_CRITERION_2026-10-30.md) combines the existing annular Harnack–Fisher estimate and fixed-volume endpoint differentiability. For center-collar derivative envelope M and B=R sqrt(pi I/(2 A_f)), it proves the conditional current bound `T_f <= inf_{0<a<=a0} [M a^2/2 + B a^(-1/2)]`. When `a*=(B/(2M))^(2/5)<=a0`, this becomes `T_f <= (5/2^(9/5))* M^(1/5) B^(4/5)`. Thus `sup_f M R^4 (I/A_f)^2=o(h^(-5/4))`, together with optimizer validity, would suffice for the earlier `o(h^(-1/4))` gate. **Neither the joint product nor the required polynomial/subexponential Harnack improvement is proved.** The known `R <= exp(C/h)` is still too costly; the interacting spectral and continuum obligations remain independent and open.

## 2026-10-30 direct nonlinear Riccati current inequality (R3-IR-384)

Crucially, the repository already proved the exact **nonadiabatic fiber Schrödinger equation** in [EF-1 (October 29)](../../research/theorems/R3_IR_DELETED_FACE_EXACT_FIBER_HAAR_MASS_2026-10-29.md). The [new signed Riccati estimate](../../research/theorems/R3_IR_RICCATI_POSITIVE_FIBER_EXCESS_CURRENT_2026-10-30.md) uses that actual nonlinear equation to show `T_f <= (4/A_f) integral_0^(pi/2) sin(u)cos(u)[U_f(cos u)-E0]_+ du`, without Harnack constants or rare-center-cap division. The benefit is the nonlinear negative square of the logarithmic score. This genuinely changes the proof target: independently bound the *weighted positive nonadiabatic fiber-energy excess*, retaining full environment and collective modes. No such Penrose-uniform estimate has been proved. The stronger EF-2 single-crossing hypothesis would force `T_f=0`, but its sign is also open. This is a **conditional sufficient route**, not a completed current or mass-gap theorem.

## 2026-10-30 model-class signed-flux obstruction (R3-IR-387)

[Inverse smooth SU(2) rotor construction](../../research/theorems/R3_IR_INVERSE_ROTOR_SIGNED_FLUX_OBSTRUCTION_2026-10-30.md) produces center-even nonnegative smooth class potentials whose strictly positive ground states obey the **exact** radial eigen-equation, endpoint regularity, both half-fiber excess-energy sum rules, and two-sided cumulative flux identities, yet have any prescribed adverse one-sided score budget `L`. This is a constructive **non-Wilson rotor** counterexample, not a failure of the physical Penrose Hamiltonian. It establishes that the formal fiber identities and center symmetry alone cannot imply a bound on the completed-cage current. The next proof must derive an additional Wilson-specific inequality on the actual normalized conditional state or signed flux; the continuum gap remains open.

## Wilson selected-link affinity versus effective fiber response (R3-IR-388)

[Exact original-link quaternion-affine restriction](../../research/theorems/R3_IR_SELECTED_LINK_WILSON_AFFINE_CONSTRAINT_2026-10-30.md): with all other links frozen, the incident SU(2) Wilson magnetic potential is `C_e(y) - x dot B_e(y)` with `|B_e| <= sum_{g contains e} b_g`; only link representations 0 and 1/2 appear. For a magnetic-deleted target face, a boundary edge meets at most one retained face. Consequently the previously engineered nonconstant center-even inverse-rotor potential cannot itself be the *bare frozen-link* Wilson potential. **This does not exclude its adverse behavior from the true marginal**, because eliminating the conditional environment generates higher-spin and center-even effective terms. The new theorem is a structural constraint only; the necessary Wilson-specific bound on full-coupling conditional mixed response or signed fiber current remains open. The archived four-neighbor spin-selection theorem has stronger selection information but no full-coupling sign bound.

## Four-neighbor mixed response: physical resolvent estimate (R3-IR-389)

[Explicit finite-volume response bound](../../research/theorems/R3_IR_FOUR_NEIGHBOR_PHYSICAL_RESOLVENT_RESPONSE_BOUND_2026-10-30.md) proves an eighth mixed derivative estimate using the true Gauss-invariant Hamiltonian's rank-one Riesz projector and its minimum finite-volume spectral gap `delta_*` over the four-dimensional coupling cube. The resulting negative mixed-response integral obeys `N_a <= 4 nu_a 16^8 (product_i b_i^2)/delta_*^8`. This is a **valid finite-volume gap-dependent upper estimate**, not the required Wilson sign control. With strong coupling `b_i ~ h^-2` and only upper bounds known for the physical gap near a coordinate hyperplane, it cannot prove the archived `N_a <= alpha_a^2/2` cap survival criterion (`alpha_a^2/nu_a~a^3`). Next task remains a cancellation-sensitive or sign-sensitive, nonperturbative control of the physical full-coupling eightfold response; do not assume a regulator-uniform gap to obtain it.

## Euclidean nine-point formulation of the four-neighbor sign gate (R3-IR-390)

[Exact physical finite-volume cumulant theorem](../../research/theorems/R3_IR_EUCLIDEAN_NINE_POINT_MIXED_RESPONSE_2026-10-30.md): the mixed eightfold derivative of the positive Wilson cap observable is the zero-temperature limit of the **connected nine-variable Euclidean cumulant** consisting of one cap insertion and two integrated neighboring plaquette insertions for each of four neighbors, using the physical Gauss-projected heat trace. This converts the abstract Riesz-projection response into a signed Euclidean connected-correlation obligation. It neither proves sign nor supplies the required uniform bound: positive path measure does not make ninth-order cumulants nonnegative; a regulator-uniform connected cluster estimate would itself need proof without assuming the desired gap. Claim R3-IR-390 is an exact finite-volume representation only. The cap-response, spectral, and continuum gates remain OPEN.

## First-order cap-biased Wilson coupling transport (R3-IR-391)

[Exact finite-volume log transport](../../research/theorems/R3_IR_CAP_BIASED_EUCLIDEAN_LOG_TRANSPORT_2026-10-30.md) replaces the eighth-order response by an identity for the signed difference of integrated neighboring plaquette expectations in cap-biased and ordinary **physical Gauss-projected Euclidean** path ensembles. Along any coupling path `log F(end)/F(start)` is the integral of the first-order signed difference. With the private-link Haar baseline, `F(1)=alpha_a^2 exp(A_a,h)`. A uniform lower bound on `A_a,h` would prove polynomial center-cap survival but is **OPEN**. No sign, mass gap, or infrared spectral estimate follows from positivity alone. The [append-only claim R3-IR-391](../../research/claims/append_only/R3-IR-391.md) records this result because the full CSV ledger update was blocked by the write filter.
