# The Singular Boundary — shape-sensitive conditional Poincaré reduction and a Wilson influence obstruction

Date: 26 October 2026. Status: **exact one-face reduction and quantitative Fisher lower bound proved**. A uniform conditional Poincaré bound and a contractive normalized influence matrix on the fully interacting Penrose continuum family remain **unproved**.

## 1. Model

One open rhombus, gauge-fixed to a class function of its loop holonomy `W ∈ SU(2)`, has

\[
H_{a,b}=4a(-\Delta_W)+b(1-p(W)),\qquad p(W)=\tfrac12\operatorname{Tr}W=\cos\theta,
\]
with electric coefficients `a>0`, magnetic coefficient `b>0`, and `-Δ p=3p/4`. Let `ω_{a,b}(W)>0` be its normalized, real and conjugation-invariant ground state. The single-rhombus full-link vacuum is `Ω(U_1,...,U_4)=ω(W)` and the density is `ν=Ω² dU`.

For an edge e, condition on the other three links. Varying `U_e` sends `W` through an isometric left/right translate (possibly inversion), which preserves Haar measure. Thus, after an isometric change of edge coordinates, **every conditional law of an edge is precisely** `ρ(W)dW=ω(W)²dW`, independent of the retained-link values up to isometry. In particular, `γ_e(y)=γ(ρ)` is constant in y. This is a genuinely shape-sensitive, interacting conditional reduction; no density comparison with Haar is invoked.

## 2. Exact one-dimensional radial/angular Poincaré representation

Parametrize `SU(2)≅S³` by `W=cosθ I+i sinθ n·σ`, `θ∈[0,π]`, `n∈S²`. Normalized Haar measure is `dW=(2/π)sin²θ dθ·dω_{S²}(n)`; `dω_{S²}` is normalized sphere measure. Since the positive ground state is conjugation-invariant, `ω(W)=w(θ)` and the conditional probability is proportional to `w(θ)²sin²θ dθ dω_{S²}`. For the metric with Casimir of spin one-half equal to `3/4`, the SU(2) Dirichlet form is `1/4` times the standard radius-one S³ gradient form.

Decompose any test function into spherical harmonics `Y_{ℓm}(n)` with `ℓ=0,1,...`. Put `dπ(θ)=Z^{-1} w(θ)²sin²θ dθ`. The exact optimal Poincaré constant is

\[
\boxed{\gamma(ρ)=\min\{\gamma_{\rm radial},\inf_{\ell\ge1}\gamma_\ell\},}\qquad
\gamma_{\rm radial}=\inf_{v:\int v dπ=0}\frac{\tfrac14\int |v'|²dπ}{\int v²dπ},
\]
\[
\gamma_\ell=\inf_{v\ne0}\frac{\tfrac14\int\left(|v'|²+\frac{\ell(\ell+1)}{\sin²θ}v²\right)dπ}{\int v²dπ}.
\]
Since the angular potential increases in `ℓ`, `inf_{ℓ≥1}γ_ℓ=γ_1`. Hence only **two one-dimensional weighted Sturm–Liouville problems** need to be controlled: the mean-zero radial channel and the `ℓ=1` channel. These are exact, nonperturbative Wilson-ground-state functionals, not a uniform positive lower estimate yet. In particular, concentration of the density does not by itself force `γ` to zero.

## 3. A new quantitative no-go theorem for raw conditional Fisher influence

Let `e≠g` be any two edges of the unique rhombus. For the conditional density of edge e, define

\[
\mathcal I_{eg}:=\operatorname*{ess\,sup}_{y}\int_{SU(2)}|\nabla_g\log ρ_e(u|y)|² ρ_e(u|y)du.
\]
Because the normalization of the conditional density is independent of retained link variables and varying either e or g transports the holonomy by a group isometry,

\[
\boxed{\mathcal I_{eg}=4\int_{SU(2)}|\nabla\omega(W)|²dW.}\tag{I0}
\]
This is a gauge-invariant one-face identity in the fixed Casimir metric.

**Theorem I (Fisher influence grows in the strong magnetic limit).** Let `m=E_{ω²}[1-p]`. The interacting variational argument with trial `e^{λp}` gives `m≤2\sqrt{2a/b}`. For `b/a≥32`,

\[
\boxed{\mathcal I_{eg}\ge\frac9{64\sqrt2}\sqrt{\frac ba}.}\tag{I1}
\]

**Proof.** On SU(2), integration by parts gives `(-Δ)p=3p/4` and `|∇p|²=(1-p²)/4≤(1-p)/2`. Write `ω` real and normalized. Then

\[
\frac34 E_{ω²}[p]=\int(-Δ p)ω²dW=2\int ω\nabla p\cdot\nabla ω\,dW.
\]
Cauchy–Schwarz yields

\[
\int|\nabla ω|²dW\ge\frac9{64}\frac{E[p]²}{E[|\nabla p|²]}.
\]
Multiply by four and use `E[|∇p|²]≤m/2` to get

\[
\mathcal I_{eg}\ge\frac98\frac{(1-m)²}{m}.
\]
For `b/a≥32`, `m≤2\sqrt{2a/b}≤1/2`, hence `(1-m)²≥1/4`. Therefore

\[
\mathcal I_{eg}\ge\frac9{32m}\ge\frac9{64\sqrt2}\sqrt{b/a},
\]
as stated. QED.

For the physical Wilson coefficient trajectory `a=O(g_3²)`, `b=O((g_3² h²)^{-1})`, one has `b/a ≍ (g_3²h)^{-2}`. In this exact one-face submodel, at least one off-diagonal raw Fisher influence **diverges at least like** `1/(g_3²h)`. A uniform bound `sup_{h,e}\sum_{g≠e}\mathcal I_{eg}<∞` for **all positive-coupling Wilson lattices** is therefore false. This does not strictly disprove such a bound for a more restricted family of many-face Penrose ground states, and does not disprove a normalized influence criterion.

## 4. What normalization could do, and what remains unresolved

The commutator estimate from the previous note is

\[
\|[\nabla_g,P_e]f\|_{L²(ν)}\le\sqrt{\mathcal I_{eg}/\gamma_e}\,\|\nabla_e f\|_{L²(ν)}.
\]
Theorem I rules out a **uniform raw** `\mathcal I_{eg}` bound. It does **not** imply the ratio `\mathcal I_{eg}/\gamma_e` diverges: a concentrated density can have a conditional gap `\gamma_e` that also grows with `b/a`.

Therefore the more appropriate quantity is an energy-weighted, scale-dependent influence matrix, for example

\[
\mathsf B_{eg}=\sqrt{\frac{a_g\mathcal I_{eg}}{a_e\gamma_e}},\qquad g\ne e,
\]
where the denominator and weights must be checked for the exact derivative/Dirichlet-form convention of the chosen block scheme. A sufficient contraction criterion would bound an appropriate weighted operator norm `\|\mathsf B\|<1` (or block version), together with a uniform conditional gap and control on retained effective interactions. **No such bound is proved here.** Even `\|\mathsf B\|<1` would not by itself close the full R3 without a retained-sector estimate, and any theorem extending to all regulator sizes would have to handle gauge constraints and topological sectors.

The original conditional-density Haar-comparison bound is true but extremely weak in the magnetic regime because `osc logω²` diverges. The exact radial/angular reduction above is a suitable starting point for a shape-sensitive one-face gap analysis; extending it to a many-face conditional measure is nontrivial because those conditional measures are not one-face class densities.

## 5. Conclusions and evidence levels

- **Proved:** one-face conditional measure is an isometric translate of the interacting gauge-invariant ground-state density.
- **Proved:** exact weighted Sturm–Liouville formula for its conditional Poincaré constant.
- **Proved:** nonperturbative Fisher influence bound `\mathcal I_{eg}≥(9/(64√2))√(b/a)` for `b/a≥32`.
- **Disproved for the all-coupling class:** a cutoff-independent bound on *raw* conditional Fisher influence sums.
- **Not proved:** a positive conditional Poincaré bound uniform along the many-face Penrose continuum trajectory.
- **Not proved:** contraction of a normalized influence matrix at continuum coupling, spatial Schur closure, R3 and R2.

No additional Monte Carlo is needed for these algebraic statements.
