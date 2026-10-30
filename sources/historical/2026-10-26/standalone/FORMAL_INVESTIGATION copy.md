# The Singular Boundary — Conditional Poincaré constants from interacting Wilson dynamics

**26 October 2026. Research status:** An explicit all-coupling finite-volume lower bound and an exact conditional-influence identity are proved. A strictly positive lower bound **uniform in Penrose patch volume and spatial refinement** is **not proved**. The result does not solve R3/R2 or establish a continuum mass gap.

## Model and normalization

Let `G=(V,E,F)` be a finite spatial Penrose rhombus gauge complex. Work initially on the full product group `M=SU(2)^E` with normalized product Haar measure; its finite-graph ground state is automatically gauge invariant. Let `L_e=-Delta_e`, normalized so that the fundamental Casimir is `3/4`, and

\[
H=\sum_{e}a_eL_e+V,\qquad V(U)=\sum_{f}b_f(1-p_f(U)),\quad p_f(U)=\tfrac12\mathrm{ReTr}\, W_f(U),\quad a_e>0,\ b_f\ge0.
\]

Since `-1≤p_f≤1`, `0≤V≤2B` where `B=Σ_fb_f`. The ground state `Omega>0` is unique, continuous/smooth, and normalized. Define `nu=Omega² dU`, `K=Omega^{-1}(H-E0)Omega`, and for each edge e disintegrate `nu_e(du|y)` with the other edges fixed. Its optimal Poincaré constant is `gamma_e(y)`, with `gamma_e^inf=essinf_y gamma_e(y)`.

## Theorem 1. Explicit lower bound from the Wilson Feynman–Kac kernel

Let `k_s(g)>0` be the normalized heat kernel of `-Delta` on SU(2) at time `s>0`, so `e^{s Delta}f(x)=∫ k_s(xy^{-1})f(y)dy`. Write

\[
m(s)=\min_{g\in SU(2)}k_s(g)>0,\qquad M(s)=\max_{g\in SU(2)}k_s(g)<\infty.
\]

Then for **every** time `t>0`, every spatial edge e, and every finite Wilson model above,

\[
\boxed{\gamma_e^{\inf}\ge\frac34\exp(-4Bt)\prod_{g\in E}\left[\frac{m(a_gt)}{M(a_gt)}\right]^2.}\tag{1}
\]

The right side is explicit from the link electric coefficients and the plaquette Wilson couplings and is strictly positive at every finite graph and cutoff. Optimizing over `t>0` gives a valid (possibly very weak) numerical lower bound.

**Proof.** Let `H0=Σ_e a_e L_e`. For nonnegative bounded Wilson potential `0≤V≤2B`, Feynman–Kac with independent SU(2) Brownian motions gives the pointwise semigroup comparison, for each nonnegative `f`,

\[
e^{-2Bt}e^{-tH_0}f\le e^{-tH}f\le e^{-tH_0}f.
\]

The free product heat kernel is strictly positive: `h_t(U,V)=Π_e k_{a_et}(U_eV_e^{-1})`. Hence for any positive `f`,

\[
\left(\prod_e m(a_et)\right)\int f\,dU\ \le\ e^{-tH_0}f(U)\ \le\ \left(\prod_e M(a_et)\right)\int f\,dU.
\]

Apply these bounds to `f=Omega`, and use `e^{-tH}Omega=e^{-tE0}Omega`. The factor `e^{tE0}` cancels when taking maximum/minimum ratios, yielding

\[
\frac{\inf_U\Omega(U)}{\sup_U\Omega(U)}\ge e^{-2Bt}\prod_e\frac{m(a_et)}{M(a_et)}.
\]

For each fixed collection y, the conditional density `Omega(u,y)^2` relative to Haar thus has minimum/maximum ratio at least the square of the right side. Comparing a weighted SU(2) Poincaré inequality to the Haar Poincaré constant `3/4` proves (1). QED.

**Precise limitation:** The bound is global in `B=Σ b_f` and the heat-kernel product over **all** edges, so its useful lower estimate can go to zero rapidly with volume or h. It does **not** establish a uniform lower bound from local incident coupling strengths. Taking `t` large improves heat-kernel mixing but amplifies `e^{-4Bt}`; taking `t` small does the reverse. No size- and cutoff-independent optimization is supplied.

## Theorem 2. Exact influence identity for adapted spatial blocking

Let `P_e f(y)=E_{nu_e(·|y)}[f(·,y)]` be the adapted conditional projection. Fix another link `g≠e` and take any smooth right- or left-invariant differentiation `X_g` in a fixed local group coordinate. Write

\[
\rho_e(u|y)=\frac{\Omega(u,y)^2}{\int_{SU(2)}\Omega(u',y)^2du'}
\]

for the conditional density relative to Haar. Differentiating under the integral gives the exact identity

\[
\boxed{X_g(P_ef)-P_e(X_gf)=\mathrm{Cov}_{\nu_e(·|y)}(f,X_g\log\rho_e).}\tag{2}
\]

The conditional score has zero expectation: `E_e[X_g log ρ_e]=0`. If `gamma_e^inf>0`, let the **conditional Fisher influence** be

\[
\mathcal I_{eg}=\operatorname*{esssup}_{y}\int_{SU(2)}|\nabla_g\log\rho_e(u|y)|^2\,d\nu_e(u|y).
\]

For full gradient-vector norms on the edge g, the same argument with Cauchy–Schwarz, conditional Poincaré, and disintegration gives

\[
\boxed{\|\nabla_gP_ef-P_e\nabla_gf\|_{L^2(\nu)}\le\sqrt{\frac{\mathcal I_{eg}}{\gamma_e^{\inf}}}\,\|\nabla_ef\|_{L^2(\nu)}.}\tag{3}
\]

**Proof.** The conditional derivative is `X_g P_ef = E_e[X_g f]+E_e[f X_g log ρ_e]`. Since the normalization of `ρ_e` is 1 for each y, the latter score has zero conditional mean. Applying conditional Cauchy–Schwarz gives `|Cov_e(f,score)|≤sqrt(Var_e(f))sqrt(E_e |score|²)`. The conditional Poincaré inequality bounds `Var_e(f)≤(gamma_e^inf)^{-1}E_e|∇_ef|²`. Integrate over retained y and sum gradient components to obtain (3). QED.

**Interpretation.** (3) is the *exact* cross-link influence term encountered in repeated ground-state-adapted spatial elimination. Its magnitude measures how much differentiation of an effective retained observable fails to commute with eliminating a link. A volume-uniform `gamma_*` alone does not show (3) is small: the matrix `\mathcal I_{eg}` must have a summable/small operator norm across spatial scales. A useful noncircular program would bound `\mathcal I_{eg}` directly from the interacting Wilson ground-state PDE or a constructive, source-inserted Euclidean RG. This has **not** been done at arbitrary magnetic coupling.

## Theorem 3. The earlier log-oscillation sufficient condition is not uniform in the strong-magnetic one-face limit

Consider one isolated rhombus with equal electric weights `a>0`, magnetic weight `b>0`, physical holonomy `W`, `p=Tr(W)/2`, and positive ground state `Omega_{a,b}(W)`. The previous variational estimate shows

\[
E_0(a,b)\le 2\sqrt{2ab},\qquad E_{\Omega²}[1-p]\le 2\sqrt{2a/b}=:\varepsilon.
\]

Let `D_δ={W:p(W)≥1-δ}`. Then the ground-state probability of `D_δ` is at least `1-ε/δ`. Haar probability of `D_δ` is at most `C δ^{3/2}`, for all sufficiently small δ, since SU(2) is the unit three-sphere. Set `δ=2ε` for `ε<1/4`; then the conditional density `ρ(W)=Omega(W)^2` satisfies

\[
\sup_W\rho(W)\ge \frac{1/2}{C(2\varepsilon)^{3/2}}.
\]

Since `∫ρdW=1`, `inf ρ≤1`. Therefore

\[
\boxed{\log\frac{\sup_W\rho(W)}{\inf_W\rho(W)}\ge\frac34\log\frac ba-O(1),\qquad b/a\to\infty.}\tag{4}
\]

On a one-face gauge-invariant model, the conditional measure on any chosen edge (with the other links fixed) is an SU(2) translate of `Omega(W)^2dW`, so (4) directly applies to the conditional oscillation `\mathcal L_e` in the previous memorandum.

**Important distinction:** (4) disproves any *uniform bounded-log-oscillation* strategy for this model along strong magnetic scaling. It does **not** disprove a uniform conditional Poincaré lower bound: concentrated, unimodal measures may have **larger** spectral gaps than Haar. The density comparison in the previous note is a sufficient bound, not a necessary condition.

## Gate status

- Wilson Feynman–Kac all-coupling lower bound (1): **PROVED at every finite graph**; constants globally volume- and cutoff-dependent.
- Exact cross-link conditional influence identity (2)–(3): **PROVED**; no dynamical estimate of the influence matrix supplied.
- Failure of uniform bounded-log-density-oscillation in the strong magnetic one-face model: **PROVED**.
- Uniform lower bound `inf_{h,G,e} gamma_e^inf>0` for the physically scaled interacting Penrose system: **OPEN**.
- Bound on accumulated Schur/source corrections through infinitely many spatial blocks: **OPEN**.
- Continuum R2 construction and mass-gap coercivity: **OPEN**.

**Mathematical inference:** The next potential mechanism is not pointwise control of the peak-to-trough ground-state density. It is a shape-sensitive one-link Poincaré estimate together with a summable conditional Fisher-influence estimate. Without both, the proposed conditional projection does not provide a controlled multiscale Wilson RG.