# P2/T2: Genuine coupled-vacuum non-tightness of the initial local bare curvature

**2026-11-06.** Exact finite original-link 3D cubic SU(2) theorem candidate; independently referee before certification. ALL P0–P5/T0–T5, infrared and four-dimensional mass-gap gates OPEN. This is a theorem on **zero-flow-time bare curvature**, NOT positive-time flow or quantum mass gap.

**Lineage.** Previous weighted nonlinear locality PR #91 was reviewed, its archived 201-check SU(2) noncommuting verifier and SHA manifest rerun successfully, and merged as `2c6a3a8ada0fd7d0ac6d83d508816e0f7be7363e` before this audit.

On finite open cubic SU(2) original links with h=1/n, write x_p=½Tr₂ U_p, ℓ_p=1−x_p, S=Σℓ_p. Let Ω>0 be the normalized genuinely coupled gauge-invariant ground state of H=αΣ_e(−Δ_e)+βS, α=g₀(h)²/(2h), β=2/[g₀(h)²h], with law ν=Ω² Haar. The prior **link-deletion** vacuum theorem gives per-link T_e=∫|∇_eΩ|²≤8β/α=32/g₀(h)^4, uniform in the containing volume.

## Lemma: actual coupled-vacuum plaquette anti-concentration at the positive center

Fix any plaquette p and any boundary link e. Condition on every non-e link and use the Haar isometry u_e↦A u_e^{±1} B to extract the actual plaquette holonomy marginal ρ_p on SU(2). Differentiation of the Hilbert fiber norm yields ∫|∇√ρ_p|²≤T_e≤32/g₀⁴. The Haar volume of A_δ={ℓ_p≤δ}, for 0<δ≤1, is v(δ)=(θ−sinθ cosθ)/π, θ=arccos(1−δ), and v(δ)≤[4√2/(3π)]δ^(3/2). SU(2) H¹→L⁶ Sobolev and Hölder imply for a universal constant C_*=C_S[4√2/(3π)]^(2/3):

\[
\nu(\ell_p\le\delta)\le C_*\delta(1+32/g_0(h)^4).
\]

Let t=g₀(h)^4>0 and δ_*(t)=min{1,t/[2 C_*(t+32)]}. Then, for **every** plaquette p regardless of correlations, ν(ℓ_p>δ_*)≥1/2. Furthermore δ_*(t)≥c_*min(1,t), c_*=min{1,1/(66C_*)}>0.

## Theorem: a fixed physical subcube has non-tight bare curvature

Choose fixed K=[1/4,3/4]^3 inside the unit physical cube; for n≥8, its face-center count N_h(K)≥(3/64)h⁻³. Put X=N_h(K)⁻¹ Σ_{c_p∈K} 1_{ℓ_p>δ_*}. Then 0≤X≤1 and EνX≥1/2; no independence is used. As EX≤1/4+(3/4)ν(X≥1/4), one has ν(X≥1/4)≥1/3. Consequently, with \(\mathscr E_{h,K}=(8/h)\sum_{c_p\in K}\ell_p\),

\[
\boxed{\nu_{h,R}\left(\mathscr E_{h,K}\ge\frac{3c_*}{32}\frac{\min(1,g_0(h)^4)}{h^4}\right)\ge\frac13.}
\]

This is **uniform in the size of the containing physical box**, and remains valid for an exponentially weighted action with weights ≥1 on K. If min(1,g₀(h)^4)/h⁴→∞, the initial bare local curvature laws are not tight: for any fixed M, eventually ν(𝓔_{h,K}>M)≥1/3. In particular the illustrative g₀(h)²=1/log(1/h) scaling satisfies the condition. That scaling is **not claimed** to be the uniquely correct asymptotically free bare-coupling trajectory.

Crucial: this cannot be propagated as a **lower** bound to s=τ/h² through PR #91's pathwise **upper** weighted-flow transfer inequality. Positive-time non-Abelian smoothing, renormalized/subtracted composite curvature and infrared mass gap remain independent OPEN tasks.

**Reproducibility.** Complete mathematical report, 5,795 passing deterministic checks (exact Haar caps, physical K face-count lower bound, arbitrary-correlation event fraction and coupling scale), executable Python script, execution log, SHA-256 manifest and CRC-checked ZIP uploaded to user's Library `/The Singular Boundary/Proof Audits/R3_TRUE_VACUUM_INITIAL_LOCAL_BARE_CURVATURE_NONTIGHTNESS_2026-11-06.zip` (SHA-256 `c0946da84b29715cc62b6ecd136051408f698f012e6ea601de680210b11ddf72`). This verifier does not numerically sample the coupled quantum vacuum; theorem rests on prior link-deletion and standard Sobolev inequalities. No canonical Observatory theorem/gate promotion, no Pages deployment.

**Next objective:** prove genuine *positive-physical-flow-time* smoothing on typical quantum-vacuum configurations to overcome initial non-tightness, or define and control a mathematically justified renormalized, centered, gauge-invariant flowed curvature observable; then pursue infrared spectral control separately.
