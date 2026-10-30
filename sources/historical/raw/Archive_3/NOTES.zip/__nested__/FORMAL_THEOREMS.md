# The Singular Boundary — A new all-coupling, volume-uniform local spectral estimate and its spatial-refinement limit

**Date:** 26 October 2026  
**Theory:** 2+1-dimensional pure SU(2) lattice gauge Hamiltonian on finite, face-complete rhombic Penrose patches.  
**Status:** Theorems K1, K2, S1, S2 below are proved. They do **not** establish a positive vacuum-orthogonal gap or low-energy suppression of generic scalar Wilson multipliers. Spatial continuum quantum convergence remains open.

## Conventions and exact hypotheses

Take a finite spatial gauge complex `G=(V,E,F)` with simple quadrilateral faces, each edge incident to at most two faces. On the full link Hilbert space `L²(SU(2)^E,dU)` consider

\[
H=\sum_{e\in E} a_e L_e+\sum_{f\in F}b_f(1-p_f),\quad
L_e=-\Delta_e,\quad a_e>0,\quad b_f\ge0,\quad
p_f(U)=\tfrac12\operatorname{ReTr}W_f(U).
\]

Choose the SU(2) bi-invariant metric so that `L_e χ_j=j(j+1)χ_j`, in particular the fundamental Casimir is `3/4`. The finite-volume Schrödinger semigroup is positivity improving on the compact connected link configuration space. Therefore the ground state `Ω>0` is simple and gauge invariant. Write `E₀=inf spec H`, `K=(H-E₀)|_{Ω^⊥}`, and `Q=I-|Ω><Ω|`. All spectral projectors and source vectors below are restricted to the physical gauge-invariant subspace; because `Ω` and the Wilson sources are gauge invariant, the full-link calculations apply without changing the result.

For a source `A` (real gauge-invariant multiplier), let

\[
\mu_A(I)=\|P_I(K)QA\Omega\|^2,\qquad
\mathsf M_1(A)=\int_{(0,\infty)} E\,d\mu_A(E).
\]

### Theorem K1 — Uniform *local kinetic energy bound* at all positive couplings

Let `B_e=Σ_{f:e∈∂f} b_f`. Then

\[
\boxed{a_e\int |\nabla_e\Omega|^2\,dU
=\langle\Omega,a_e L_e\Omega\rangle\le B_e.}\tag{K1}
\]

The constant depends only on couplings of faces touching `e`, not on the number of vertices, links, faces, or distant boundary conditions.

**Proof.** Decompose `H=a_e L_e+H_{\neg e}+V_e`, where `H_{\neg e}` consists of all other electric terms and all plaquette terms not touching `e`, and `V_e=Σ_{f∋e}b_f(1-p_f)≥0`. `H_{\neg e}` is independent of `U_e`. Let `E_{\neg e}` be its ground energy and take a trial state equal to its normalized ground state on all other links and the constant `1` on link `e`. Since every selected face traverses `e` exactly once, Haar integration over this link gives `∫p_f\,dU_e=0`; hence the trial magnetic energy is exactly `B_e`. The variational principle yields `E₀(H)≤E_{\neg e}+B_e`. Conversely, in the actual ground state, `E₀(H)=<a_eL_e>+<H_{\neg e}>+<V_e>≥<a_eL_e>+E_{\neg e}`. Combine the two inequalities. Positivity improving makes the actual ground state physical; the variational trial may be chosen on the full link space without changing the lowest energy. QED.

**Caveat:** K1 controls *one-link gradient energy*, not its influence on a distant link or an inverse-energy resolvent.

### Theorem K2 — An explicit local low-energy Wilson-loop projection bound at arbitrary coupling

For any simple plaquette `f`, let `κ_f=(3/4)Σ_{e∈∂f} a_e` and `R_f=Σ_{e∈∂f}√(a_e B_e)`. Then

\[
\boxed{\mu_{p_f}((0,s])\le\frac{R_f^2}{(\kappa_f-s)^2},\quad 0<s<\kappa_f.}\tag{K2}
\]

More generally, `\mu_{p_f}({E>0:|E-κ_f|≥δ})≤R_f²/δ²` for every `δ>0` (spectral concentration near the electric single-loop energy).

**Proof.** The fundamental Wilson plaquette has `L_e p_f=(3/4)p_f` on each of its four edges. The product rule for the bi-invariant Laplacian gives

\[
(H-E₀)(p_f\Omega)=\kappa_f p_f\Omega
 -2\sum_{e\in\partial f}a_e\nabla_e p_f\cdot\nabla_e\Omega.
\]

With the specified SU(2) metric, `Σ_{a=1}^3 |X_e^a p_f|²=(1-p_f²)/4≤1/4`; thus `\|\nabla_e p_f\|_∞≤1/2`. Project away the vacuum. Cauchy–Schwarz, the triangle inequality and K1 show

\[
\|(K-\kappa_f)Qp_f\Omega\|
\le 2\sum_{e\in\partial f}a_e \|\nabla_e p_f\|_\infty\,\|\nabla_e\Omega\|_2
\le R_f.
\]

On the spectral range `(0,s]` of `K`, `|K-κ_f|≥κ_f-s`, hence `\|P_{(0,s]}Qp_fΩ\|≤R_f/(κ_f-s)`. The second result follows from the same projector argument outside an energy window. QED.

For equal electric coefficients `a` and `b_f≤b` with face incidence at most two, `κ_f=3a`, `R_f²≤32ab`. Therefore for `s<3a`,

\[
\boxed{\mu_{p_f}((0,s])\le \min\{1,\,32ab/(3a-s)^2\}.}\tag{K2-equal}
\]

This bound is **nonperturbatively valid at every coupling**, but only useful when its right-hand side is small. At the continuum magnetic scaling `b∼h^{-2}`, its simple form becomes vacuous; K2 is not a continuum mass-gap theorem.

### Theorem S1 — A *cutoff-stable spectral-weight bound* for a physical-area average of neutral Wilson plaquettes

For the **specified** geometric action (not yet certified as the literal Stage 26 builder), let spatial edge length be `h>0`, with rhombus areas `A_f=h² sin(π/5)` or `h² sin(2π/5)`. Give interior edges the dual-area weight `w_e=(A_L+A_R)/(2h²)` and one-face boundary edges `w_e=A_f/(2h²)`. Set

\[
 a_e=\frac{g_3^2}{2w_e},\qquad b_f=\frac{4}{g_3^2A_f}.
\]

Here `g_3²>0` is fixed in physical units. Define `σ_-=sin(π/5)`, `σ_+=sin(2π/5)` and `φ=σ_+/σ_-=(1+√5)/2`. The geometric inequalities give `w_e∈[σ_-/2,σ_+]` and therefore `a_e≤g_3²/σ_-`, *uniformly in `h`, patch size, and admitted open boundaries*.

Let `D⊂F` be any nonempty face collection with total physical area `\mathcal A_D=Σ_{f∈D} A_f`. Define the **bare**, normalized, gauge-invariant spatial average

\[
\mathcal W_D=\sum_{f\in D}\frac{A_f}{\mathcal A_D}\,p_f,
\quad\|\mathcal W_D\|_\infty\le1.
\]

Then for the fully interacting vacuum at **any** nonnegative magnetic coupling,

\[
\boxed{\mathsf M_1(\mathcal W_D)
\le 2\varphi\,g_3^2\frac{h^2}{\mathcal A_D}.}\tag{S1}
\]

Hence, for every fixed physical energy `η>0`,

\[
\boxed{\mu_{\mathcal W_D}((\eta,\infty))
\le \frac{2\varphi g_3^2}{\eta}\frac{h^2}{\mathcal A_D}.}\tag{S1-hi}
\]

Writing `V_D=Var_Ω(\mathcal W_D)=\mu_{\mathcal W_D}((0,∞))`, the complementary rigorous *LOW-energy* bound is

\[
\boxed{\mu_{\mathcal W_D}((0,\eta])
\ge V_D-\frac{2\varphi g_3^2}{\eta}\frac{h^2}{\mathcal A_D}.}\tag{S1-lo}
\]

**Proof.** The interacting spectral sum rule is exact because the Wilson magnetic potential and `\mathcal W_D` are both multiplication operators:

\[
\mathsf M_1(\mathcal W_D)
=\sum_e a_e\int |\nabla_e\mathcal W_D|^2|\Omega|^2dU.
\]

Put `ω_f=A_f/\mathcal A_D`. On any edge, `|\nabla_e\mathcal W_D|≤\tfrac12Σ_{f∈D:e∈∂f}ω_f`. As at most two faces meet one edge, Cauchy–Schwarz gives

\[
\sum_e\Big(\sum_{f∈D:e∈∂f}\omega_f\Big)^2
\le 2\sum_e\sum_{f∈D:e∈∂f}\omega_f^2
=8\sum_{f∈D}\omega_f^2.
\]

Therefore `\mathsf M_1≤2 a_{max} Σ_f ω_f²`. Since `Σ_f ω_f=1` and `ω_f≤σ_+h²/\mathcal A_D`, `Σ_fω_f²≤σ_+h²/\mathcal A_D`. Substitute `a_{max}=g_3²/σ_-` to obtain `2(σ_+/σ_-)g_3² h²/\mathcal A_D=2φg_3²h²/\mathcal A_D`. Markov's spectral-measure inequality yields S1-hi; partitioning the total variance yields S1-lo. QED.

**Key directionality warning:** S1-hi says the high-energy source weight vanishes as `h→0`; **it does not suppress the low-energy weight**. Unless `V_D→0`, S1-lo instead forces spectral weight toward arbitrarily low energies. This theorem is not a mass-gap proof.

**A new necessary renormalization consequence.** If one separately had a volume- and cutoff-uniform physical spectral gap `m_*>0`, then the same sum rule would force

\[
\boxed{\operatorname{Var}_\Omega(\mathcal W_D)
\le \frac{2\varphi g_3^2}{m_*}\frac{h^2}{\mathcal A_D}.}\tag{S1-necessary}
\]

This variance bound is a *testable necessary condition*, not a result established without the gap. A centered candidate with nonvanishing `h^{-1}` fluctuations is

\[
\widetilde{\mathcal W}_D=(\sqrt{\mathcal A_D}/h)(\mathcal W_D-\langle\mathcal W_D\rangle),
\quad \mathsf M_1(\widetilde{\mathcal W}_D)\le2\varphi g_3^2.
\]

This is cutoff-uniform oscillator-strength control for that normalization; existence of its quantum continuum limit is still open.

### Theorem S2 — Genuine infrared suppression for a restricted class of time-derivative gauge observables

Let `\mathcal D_D=i[H,\mathcal W_D]` on its natural dense domain. It is a gauge-invariant *local first-order dynamical source*, not a bounded Wilson multiplier, and is **not** Paper 3's geometric complex structure `J`. In the ground state `\mathcal D_D\Omega=iKQ\mathcal W_D\Omega`. For every physical-energy threshold `η>0`,

\[
\boxed{\mu_{\mathcal D_D}((0,\eta])
\le\eta\,\mathsf M_1(\mathcal W_D)
\le 2\varphi g_3^2\eta\frac{h^2}{\mathcal A_D}.}\tag{S2-weight}
\]

Moreover, the truncated inverse-energy *diagonal susceptibility* satisfies

\[
\boxed{2\int_{(0,\eta]} E^{-1}\,d\mu_{\mathcal D_D}(E)
\le 2\mathsf M_1(\mathcal W_D)
\le4\varphi g_3^2\frac{h^2}{\mathcal A_D}.}\tag{S2-IR}
\]

For two regions `D,D'`, polarization and Cauchy–Schwarz give

\[
\boxed{|\chi_{\mathcal D_D,\mathcal D_{D'}}^{<\eta}|
\le4\varphi g_3^2\frac{h^2}{\sqrt{\mathcal A_D\mathcal A_{D'}}}.}\tag{S2-cross}
\]

**Proof.** The spectral measure of `\mathcal D_D\Omega=iKQ\mathcal W_D\Omega` is `d\mu_{\mathcal D_D}(E)=E²d\mu_{\mathcal W_D}(E)`. On `(0,η]`, `E²≤η E`, yielding S2-weight; inverse-energy integration gives `2∫E d\mu\le2\mathsf M_1`, yielding S2-IR. Cauchy–Schwarz applied to the weighted cross measure proves S2-cross. QED.

The rescaled source `\widetilde{\mathcal D}_D=(\sqrt{\mathcal A_D}/h)\mathcal D_D` has cutoff-independent bounds `\mu_{\widetilde{\mathcal D}_D}((0,η])≤2φg_3²η` and `|\chi_{\widetilde{\mathcal D}_D,\widetilde{\mathcal D}_{D'}}^{<η}|≤4φg_3²` for analogous size normalization. Again: **this does not bound arbitrary center-neutral Wilson multipliers or the whole physical gap.**

## Why these theorems do not solve the requested uniform gap

* **K1** supplies a local all-coupling ground-state gradient estimate without inverse-energy control. **K2** supplies a low-energy *upper* projection bound for each individual Wilson plaquette; along the physical scaling `b_f∝h^{-2}`, its right-hand side diverges and loses content.
* **S1** gives a robust *spatial-refinement* moment and high-energy estimate for bare plaquette averages, and a complementary low-energy **lower**, not upper, bound. It is compatible with both a positive gap plus shrinking variance, and gapless infrared modes with persistent variance.
* **S2** proves cutoff-uniform infrared suppression for the time-derivative source `i[H,\mathcal W_D]Ω`; the suppression arises from a factor of excitation energy and therefore cannot be extended to `\mathcal W_DΩ` by dividing out the factor without a gap.
* None proves `inf_{h,L} gap(H_{h,L})>0`, or a neutral Wilson-loop estimate `\mu_A((0,s])≤C s^{1+α}` at arbitrary magnetic coupling with `C` uniform in spatial refinement.
* All Penrose-specific constants use the *specified* dual-area Wilson action. Literal Stage 26 `stage7_checkpointed.setup_geometry` remains unavailable for action-level certification. No attempt at further Stage 26/35 Monte Carlo is justified.

## R2: what is and is not controlled

The `h`-uniform bounds above are **finite-cutoff spectral sum rules in physical Hamiltonian units**, and do not require construction of a limiting continuum Hilbert space. They are valid *along* the declared coefficient trajectory for every `h>0`. They do not prove convergence of states, spectra, or Schwinger functions as `h→0`. The earlier exact fivefold-isotropy of the geometric tensor and fixed-spatial-graph continuous-time semigroup limit remain separate established facts; neither is a quantum continuum reconstruction.

## Source and verification notes

* Spatial rhombi: 36° thin, 72° thick, areas `h²sin36°`, `h²sin72°` (standard Penrose geometry).
* Hamiltonian and weights: as specified in the prior user's derived action from `penrose_2p1_study.py`. Repeated here as an **assumption for this theorem**, not claimed as certified literal Stage 26 code.
* All K/S proofs are provided above; no literature theorem on an unproven interacting mass gap is imported.
