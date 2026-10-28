# R3-IR — Planar Cheeger coercivity and exact Gaussian three-source response

**Date:** 2026-10-28. **Scope:** independently proved geometric theorem for finite embedded Penrose rhombus patches and a complete three-source response bound for their **Gaussian tangent Hamiltonians**. This does **not** prove the nonlinear SU(2) three-source bound, physical-point variance collapse, continuum dynamics, or the mass gap. No Monte Carlo or historical file modifications.

## Provenance and upstream audit

Consulted current audit branch \`audit/2026-10-28-independent-reconstruction\`: \`R3_IR_MULTIFACE_STRONG_FIELD_DUAL_LAPLACIAN_2026-10-28.md\`, \`R3_IR_GAUSSIAN_VARIANCE_GATE_2026-10-28.md\`, \`R3_IR_CURVATURE_WEIGHTED_FSUM_2026-10-28.md\`, \`R3_IR_REFINED_CURVATURE_WEIGHTED_ALIGNED_RESPONSE_2026-10-28.md\`, and \`R3_IR_THREE_SOURCE_ENERGY_WINDOW_2026-10-28.md\`. The declared Stage 7/Stage 26 source-level action coefficients are **not** yet fully identified; application of this tangent model to that historical action remains pending.

## GC-1: exact face Laplacian lower bound

Let G be a finite patch of edge-to-edge, **nonoverlapping embedded** Penrose rhombi with edge length h and F≥1 faces. All rhombi have area at least σ_- h², σ_-=sin(π/5)>0. Let B be the oriented face–edge boundary matrix (each interior edge occurs with opposite signs for its two incident faces) and L=BBᵀ. For every real q∈R^F,

**qᵀLq ≥ [πσ_-/(2F)] ||q||₂².**

**Proof.** Extend q to zero on the exterior face. The discrete Dirichlet energy is qᵀLq=Σ_e(q_f−q_g)², counting boundary edges against zero. For any nonempty subset S of rhombi, the physical union has area ≥σ_- h²|S|, and its perimeter is precisely h times the number ∂S of edges separating S from its complement, including exterior boundary. Euclidean planar isoperimetry gives
∂S ≥ 2√(πσ_-|S|) ≥ [2√(πσ_-)/√F]|S|.

Set r_f=|q_f| and r_exterior=0. Discrete layer-cake/coarea gives
Σ_e |r_f²−r_g²| = ∫₀^∞ |∂{f:r_f²>t}|dt ≥ [2√(πσ_-)/√F]Σ_f r_f².
By Cauchy–Schwarz and degree four,
Σ_e|r_f²−r_g²|
≤ [Σ_e(r_f−r_g)²]^{1/2}[Σ_e(r_f+r_g)²]^{1/2}
≤ [qᵀLq]^{1/2}[8Σ_f r_f²]^{1/2}.
Cancellation and squaring give the stated exact constant. No infinite-volume or translation-invariance hypothesis. If Fh²≤A₀, λ_min(L)≥πσ_- h²/(2A₀).

**Comparison:** the earlier exact boundary trial λ_min(L)≤N_boundary/F remains valid; the two bounds constrain different geometric aspects and do not establish a fixed-domain nonlinear Wilson gap.

## GC-2: Gaussian vacuum covariance, with a signed-source bound

Consider the **separate tangent model**
H_quad=−Σ_fg M_fg ∇_{y_f}·∇_{y_g}+(1/8)Σ_f b_f|y_f|² on y_f∈R³,
M=B diag(a_e) Bᵀ, V=diag(b_f)/8, and 0<a_min≤a_e≤a_max, β_min/h²≤b_f≤β_max/h². The ground state is the centered Gaussian invariant under diagonal SO(3), with one-Cartesian-component covariance Σ. The matrix identity

Σ V Σ=M/4

follows from the unique positive Gaussian vacuum (or from Σ=(1/2)M^{1/2}(M^{1/2}VM^{1/2})^{-1/2}M^{1/2}). Since V≥b_min I/8 and M_ff=Σ_{e∈∂f}a_e≤4a_max, one has the Loewner inequality Σ²≤2M/b_min and hence Σ²_ff≤8a_max/b_min.

For arbitrary **signed** real coefficients c_f, let
A_c=−(1/8)Σ_f c_f (|y_f|²−3Σ_ff).
Wick's theorem gives Var(A_c)=(3/32)Σ_fg c_f c_g Σ_fg², and
|Σ_fg c_f c_g Σ_fg²|≤Σ_f c_f²(Σ²)_ff. Consequently

**Var(A_c)≤[3a_max/(4b_min)]Σ_f c_f².**

For a fixed smooth real φ, choose c_f=h^{2−α}σ_fφ(x_f), Fh²≤A₀; then

**Var(A_{h,α}) ≤ [3a_max σ_+²||φ||∞² A₀/(4β_min)] h^{4−2α}.**

This is a sharp-order bound of the full shared-link Gaussian vacuum, not of the nonlinear Wilson interacting vacuum.

## GC-3: uniform finite-area Gaussian source spectral threshold

The oscillator frequencies are ω_i=√λ_i(M^{1/2} V M^{1/2}); each one-quantum excitation costs 2ω_i. A centered quadratic source A_c acting on the vacuum creates only two-quantum excitations; it is diagonal-SO(3) invariant. Its spectral support lies above
Δ_A=4ω_min ≥√(2a_min b_min λ_min(L)) ≥√(πσ_- a_min β_min/A₀).

This is a **source-specific Gaussian spectral threshold** at fixed A₀. It says nothing about nonlinear SU(2), and its bound degenerates as A₀→∞.

## GC-4: exact Gaussian three-source response bound

A centered quadratic form in Gaussian variables can be diagonalized as A_c=Σ_k λ_k(Z_k²−1), Z_k independent standard normal. Its variance is 2Σλ_k² and fourth centered moment is 12(Σλ_k²)²+48Σλ_k⁴≤15 Var(A_c)². Thus
||Q A_c²Ω||²=Var(A_c²)≤14 Var(A_c)²,
||Q A_cΩ||²=Var(A_c).

For the Gaussian K=H_quad−E₀ and any spectral projector P≤Λ (or P=I),
R_{2,P}=〈Q A_c²Ω, K^{-1}P Q A_cΩ〉
obeys

**|R_{2,P}|≤(√14/Δ_A)[Var(A_c)]^{3/2}.**

For α=3/2, the signed-source variance estimate is O(h) uniformly over any family of positive bounded magnetic coefficient deformations and finite patches with Fh²≤A₀. Hence

**sup_{|t|≤τ}|R^{Gaussian}_{2,≤h^{-1−δ}}(t)| ≤ C(A₀,φ)h^{3/2}=o(h^{1/2})**,

for every fixed δ>0; indeed the *entire Gaussian response* is O(h^{3/2}). The Gaussian model therefore satisfies the low/intermediate spectral-window criterion needed in the earlier RR/EW **conditional mechanism**.

**Crucial non-transfer:** The actual nonlinear SU(2) vacuum has neither the Gaussian fourth-moment inequality, nor the source variance O(h), nor the source-specific inverse-energy threshold independently established. Inserting GC-4 as an estimate for the nonlinear Hamiltonian would be circular or unsupported. This is a complete proof in the tangent model and a stringent benchmark only.

## Exact computational verification

Read-only deterministic \`scripts/audit/verify_cheeger_gaussian.py\` verifies the original three canonical Penrose seed rhombi (10 edges, L eigenvalues 4−√2,4,4+√2), all seven nonempty face-subset perimeter inequalities, the Gaussian matrix equation ΣVΣ=M/4, row-sum identity, one-face variance 3a/(4b), the 15 fourth-moment ratio, and the h exponents. No historical Q14 temporal insertion or Monte Carlo was recreated.

## Dependency and next proof task

- **Independently proved:** GC-1 geometry and GC-2–GC-4 **for the explicit Gaussian tangent Hamiltonian only**.
- **Open:** the corresponding nonlinear source-variance/hypercontractive and low-window resolvent bounds at the distinguished physical coupling, a uniform non-Gaussian continuum field, and physical mass gap.
- **Potential next direct nonlinear estimate:** Establish noncircular **source-specific** control of (i) Var_{Ω_h}(A_{h,3/2}), (ii) fourth moment of the centered source, and (iii) its vacuum-orthogonal inverse-energy response. Do not assume a full gap, a log-Sobolev inequality equivalent to strong mixing, or a uniform Gaussian comparison; each would require its own proof.
- **Scope restriction:** fixed physical-area A₀; no infinite-volume gap and no 3+1D Yang–Mills inference.
