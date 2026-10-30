# R3-IR — Probability-weighted SU(2) magnetic convex core: exact bad-area concentration and a coupled-link obstruction

**Date:** 2026-10-28. **Research status:** exact finite Wilson-Hamiltonian theorems using the previously established regional ground-state comparison and Agmon bound; geometric refinement under the explicitly declared Penrose coefficients and fixed physical collar. **Not claimed:** a source-specific Poincaré inequality, fixed-physical-support covariance `o(h)`, an interacting continuum mass gap, or source-level identity with original Stage7/Stage26 numerical actions.

## Primary dependencies and auditable provenance

Read the live `audit/2026-10-28-independent-reconstruction` branch files `R3_IR_LOCAL_VACUUM_SCORE_FORCE_2026-10-28.md` (VF-1), `R3_IR_MODERATE_CURVATURE_EFFECTIVE_DRIFT_2026-10-28.md` (DR-1/DR-8), `R3_IR_REGIONAL_GROUND_STATE_AGMON_2026-10-28.md` (AG-1/AG-2), `R3_IR_LOCAL_EXCITED_RELATIVE_ENERGY_2026-10-28.md` (ER-1), `R3_IR_SU2_VACUUM_DRIFT_ENDPOINT_AUDIT_2026-10-28.md` (interacting counterexample to global inward-drift monotonicity), and the current claim ledger. The independent deterministic verifier checks the authentic three-face Z^5 *spatial* Penrose seed (three faces, ten edges); this is **not** the original temporal Q14 construction. Original uploaded archives remain unmodified.

## Set-up

For a finite connected face-complete planar rhombus complex, with four distinct edges per face and at most two faces per edge, consider the genuine nonlinear SU(2) link Hamiltonian

\[H_h=\sum_e a_e(-\Delta_e)+\sum_f b_f d_f,\qquad d_f=1-p_f,\quad p_f=\tfrac12\operatorname{ReTr}W_f\in[-1,1].\]

On a face region D of *fixed positive physical area* (interior complete collar), suppose `a_e≤a_max`, `β_min h^(-2)≤b_f≤β_max h^(-2)`, and `c_F h^(-2)≤|D|≤C_F h^(-2)` for fixed positive constants. Let Ω_h be the actual normalized unique positive gauge-invariant ground state, ν_h=Ω_h²dHaar, `X_h=Σ_{f∈D}d_f`, `Z_h=h X_h`. The regional comparison ER-1 supplies `Δ_D:=E0(H_h)−E0(H_out)≤C_E h^(-3)`. Hence

\[\mathbb E_{\nu_h}X_h\le\frac{h^2\Delta_D}{\beta_{\min}}\le\frac{C_E}{\beta_{\min}h},\qquad \mathbb E_{\nu_h} Z_h\le C_E/\beta_{\min}.\tag{PC-0}\]

The exact regional Agmon theorem AG-1 supplies for `L_h=C_L/h` sufficiently large, `λ_h=c_λ/h` with `c_λ=√(β_min/(32a_max))`,

\[\mathbb E[X_he^{2\lambda_h(X_h-2L_h)}1_{\{X_h\ge2L_h\}}]\le \frac{64a_{\max}}{\beta_{\min}}\frac{h^2}{L_h}.\tag{AG-1}\]

The theorems below are algebraic consequences of these **true interacting vacuum** estimates; they do not introduce Gaussian, Gibbs-product, spectral-gap, or mixing assumptions.

## Theorem PC-1: explicit exponential moments of rescaled total curvature

For every fixed `θ>0` and sufficiently small `h` (so `θh≤2λ_h`), the true vacuum obeys

\[\boxed{\mathbb E_{\nu_h}e^{\theta Z_h}\le e^{2\theta C_L}\left(1+\frac{32 a_{\max}}{\beta_{\min}C_L^2}h^4\right)=:M_\theta(h).}\tag{PC-1}\]

**Proof.** On `X_h<2L_h` use `Z_h<2C_L`. On the complement, `e^{θhX}≤e^{2θC_L}e^{2λ_h(X−2L_h)}` and `X≥2L_h`, so AG-1 bounds the complement by `e^{2θC_L}(64a_max h²/(β_min L_h))/(2L_h)`. Substituting `L_h=C_L/h` proves PC-1. No assertion of a new unweighted log-Sobolev inequality is made. For every `r≥1`, this gives `||Z_h||_{L^r(ν_h)}≤C_r` and Chernoff tails `ν_h(Z_h≥t)≤M_θ(h)e^(−θt)` for arbitrary fixed `θ>0`.

## Theorem PC-2: high-probability magnetic convex core and bad-area fraction

Let `0<ε≤1` and set

\[\mathcal B_{h,\varepsilon}=\{f\in D:p_f\le1-\varepsilon\}=\{f:d_f\ge\varepsilon\},\qquad N_{h,\varepsilon}=|\mathcal B_{h,\varepsilon}|,\qquad A_{h,\varepsilon}=h^2N_{h,\varepsilon}.\]

Here `A_h` denotes face count multiplied by h², not the more precise shape-weighted area; the physical bad area is between `σ_-A_h` and `σ_+A_h` on Penrose rhombi. The deterministic inequality `ε N_{h,ε}≤X_h` immediately gives

\[\boxed{\|A_{h,\varepsilon}\|_{L^r(\nu_h)}\le\frac{h}{\varepsilon}\|Z_h\|_{L^r(\nu_h)}\le C_r\frac{h}{\varepsilon},\quad 1\le r<\infty.}\tag{PC-2}\]

Furthermore, for every `θ>0` and every fixed physical bad-area threshold `δ>0`, Markov's exponential inequality and PC-1 give

\[\boxed{\nu_h(A_{h,\varepsilon}\ge\delta)\le M_\theta(h)\exp\!\left(-\frac{\theta\delta\varepsilon}{h}\right).}\tag{PC-3}\]

Choosing `ε_h=h^γ` for any fixed `0<γ<1` yields

\[\boxed{\|A_{h,h^\gamma}\|_{L^r}=O(h^{1-\gamma}),\qquad \nu_h(A_{h,h^\gamma}\ge\delta)\le C_\theta\exp(-\theta\delta/h^{1-\gamma}).}\tag{PC-4}\]

Therefore the actual vacuum concentrates on configurations in which *almost all physical face area* is in the strongly flat SU(2) geodesic core `p_f>1−h^γ`. No assertion that **all** faces are good follows: with `|D|≈h^-2`, the theorem permits `O(h^-1-γ)` bad faces, diverging as h→0. Their collective amplitude may still be significant for a critically rescaled Wilson source.

For a fixed threshold `ε_0∈(0,1]`, the number of links incident to at least one bad face is at most `4N_{h,ε_0}`; consequently its h²-weighted area is `O_{L^r}(h)` and obeys an analogous stretched-exponential tail. This is an incidence statement, not a locality/independence theorem.

## Theorem PC-3: exact local magnetic Hessian and positive trace in the physical vacuum

The SU(2) bi-invariant metric is normalized by `−Δ χ_{1/2}=3χ_{1/2}/4`. Identifying SU(2) with the 3-sphere of Riemannian radius 2, every real matrix-coordinate height function `p(U)=(1/2)ReTr(CU)` or its orientation-inverse form satisfies the **full covariant Hessian identity**

\[\boxed{\operatorname{Hess}_{U_e}p_f=-\frac14 p_f g_e,\qquad \operatorname{Hess}_{U_e}d_f=\frac14 p_f g_e\quad(e\in\partial f).}\tag{PC-5}\]

Here only link e varies and all remaining links are held fixed; the face product contains e exactly once. Consequently the **diagonal link block** of the regional magnetic Hessian `V_D=Σ_{f∈D}b_fd_f` is

\[\boxed{\operatorname{Hess}_{U_e}V_D=\frac14\left(\sum_{f\in D:e\in\partial f}b_fp_f\right)g_e.}\tag{PC-6}\]

For links whose incident faces are all good with `p_f>1−ε`, the regional magnetic Hessian is strictly positive in that single-link direction, with quadratic-form lower bound `(1−ε)β_min deg_D(e)g_e/(4h²)`. For an *interior* link all of whose incident faces belong to D, this positivity applies to the corresponding diagonal block of the full magnetic potential; on boundary links, exterior face terms might change its sign.

Let `B_D=Σ_{f∈D}b_f`. Taking the trace in each of the three orthonormal link directions, and summing the incidence over the four edges of every face, gives the **exact pointwise identity**

\[\boxed{\sum_{e\in S}\operatorname{tr}_{g_e}[\operatorname{Hess}_{U_e}V_D]\;=\;3\sum_{f\in D}b_fp_f.}\tag{PC-7}\]

Using PC-0, `b_f≤β_max h^-2`, `B_D≥β_min c_Fh^-4`, we obtain the unconditional interacting-ground-state expectation bound

\[\boxed{\frac{1}{3B_D}\mathbb E_{\nu_h}\!\left[\sum_{e\in S}\operatorname{tr}\operatorname{Hess}_{U_e}V_D\right]\ge1-\frac{\beta_{\max}C_E}{\beta_{\min}^2c_F}h.}\tag{PC-8}\]

The same ratio is at most 1 because `p_f≤1`. Thus **the vacuum-averaged diagonal magnetic Hessian trace approaches its flat-configuration maximum at order O(h)**, without assuming a gap. This trace identity is not a lower bound on the *smallest eigenvalue of the full coupled-link Hessian* and is not a Bakry–Émery curvature inequality for `ν_h`.

## Theorem PC-4: exact coupled-link obstruction and the missing score Hessian

Already on a two-link product embedded in one SU(2) plaquette, let `U_1(t)=exp(itσ_3/2)` and `U_2(s)=exp(isσ_3/2)` with fixed other links I, and take `V=b[1−(1/2)Tr(U_1U_2)]`. Near the flat configuration,

\[ V(t,s)=b[1-\cos((t+s)/2)],\qquad
\operatorname{Hess}_{(t,s)}V(0,0)=\frac b4\begin{pmatrix}1&1\\1&1\end{pmatrix}. \]

Both *diagonal* link Hessian entries are positive `b/4`, yet the full Hessian has an **exact zero mode `(1,−1)`**, corresponding to a compensating link variation. Therefore even **100% good plaquettes** and strictly positive diagonal link Hessians do not entail joint convexity on all link variables; gauge reduction and full mixed-link geometry must be treated separately. Gauge-invariant observables may remove some redundant modes, but a physical coercivity theorem still requires proof.

More importantly, the ground-state diffusion and its curvature depend on `−2 Hess(logΩ_h)` together with the SU(2) Ricci term, not just `Hess(V_D)`. The Schrödinger eigenvalue equation identifies the scalar combination `Σ_e a_e(Δ_e logΩ_h+|∇_e logΩ_h|²)=V−E0`; it does **not** give a sign for the full Hessian of logΩ_h from PC-6 or PC-8. Inferring a source-conditioned Poincaré constant or drift slope from the large positive magnetic Hessian *alone* would be mathematically invalid. The independent one-plaquette strong-coupling drift-endpoint theorem already shows global drift monotonicity fails on a genuine interacting SU(2) model.

## Evidence/critical path

**Independently proved for the actual finite Wilson vacuum, under prior ER-1/AG-1:** PC-1 explicit exponential curvature moments, PC-2 stretched-exponential probability that bad plaquettes occupy a fixed positive physical area, PC-3 exact SU(2) single-link magnetic Hessian and its vacuum-averaged positive trace, PC-4 exact two-link coupled-direction obstruction.

**Not proved:** the probability that *any* bad face exists tends to zero; the quantitative conditional ground-state Hessian or the signed source drift's one-sided restoring slope; the fixed-support `Var_ν(hΣ q_fd_f)=o(h)`; uniform quartic resolvent or positive interacting continuum mass gap; original Stage7/26 coefficient provenance.

**Next precise noncircular gate:** prove an *integrated, gauge-reduced core coercivity estimate* for the true vacuum's source direction, with the fraction of bad plaquettes controlled by PC-4 and the mixed-link and logarithmic-vacuum-Hessian terms explicitly bounded. Alternatively establish directly a connected covariance estimate through Hamiltonian spectral/conditional measures. Do not infer a Poincaré constant from the potential's positive diagonal Hessian trace or assume the desired physical mass gap.

## Reproducibility

The accompanying deterministic script `verify_probability_core.py` verifies the polynomial and exponential scaling, SU(2) radius-2 geodesic Hessian, coupled-link null Hessian, trace incidence constant 3, and the authentic three-rhombus ten-edge Z^5 **spatial** seed. No Monte Carlo or temporal Q14 verification is claimed. Original uploaded archives have not been modified.
