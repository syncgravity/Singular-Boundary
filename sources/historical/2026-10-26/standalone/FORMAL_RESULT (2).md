# Exact typical-boundary contraction for the isolated interacting two-rhombus Wilson block

**Date:** 2026-10-26. **Status:** Exact theorem for a pair of rhombi under its complete (isolated, free outer boundary) Euclidean Wilson measure; quantitative large-coupling bounds. No transfer-Hamiltonian spectral gap or Penrose infinite-volume theorem is claimed.

## 1. Exact closed-form block kernel

For two rhombi sharing a link, write `W1=AU`, `W2=U^{-1}B`, outer loop `V=AB`, `p_i=Tr(W_i)/2`, `v=Tr(V)/2`. For nonnegative couplings `t,s`, the shared-link Haar integral is

\[
Z_{t,s}(V)=\int_{SU(2)}e^{tp_1+sp_2}\,dU
=z(R),\quad R=\sqrt{t^2+s^2+2tsv},\quad z(x)=\frac{2I_1(x)}x,\ z(0)=1. \tag{1}
\]

**Proof:** Set `X=AU`. By cyclicity and `B=A^{-1}V`, `p1=Tr(X)/2`, `p2=Tr(X^{-1}V)/2`. For `SU(2)`, `Tr(X^{-1}V)=Tr(XV^{-1})`; identify unit quaternions with real 4-vectors, so `tp1+sp2` is the Euclidean dot product of the unit quaternion X with the vector `t*1+s*V` (or an isometric reflected V), of Euclidean norm `R`. Haar rotation gives the radial integral `z(R)`. This proves (1). Equivalently, choose the SU2 conjugation that aligns the four-vector. The `R=0` case is understood by continuity. The formula sums the full character series, without truncation.

The connected scalar influence at fixed boundary is the mixed derivative
\[C(V;t,s)=\partial_t\partial_s\log z(R)=\operatorname{Cov}(p_1,p_2\mid V).\tag{2}\]
In particular, at `V=-I, t=s`, `R=0` and `C=-1/4` exactly, preserving the worst-boundary obstruction.

## 2. Exact induced boundary distribution on the *isolated pair*

For a simply connected isolated two-face disk with all six exterior links free (and no additional plaquettes), elementary changes of Haar link variables show that `W1,W2` are independent under normalized product Haar measure. After introducing `e^{tp1+sp2}`, they remain independent with one-face tilted laws
\[d\rho_t(W)=\frac{e^{t p(W)}}{z(t)}dW,\qquad d\rho_s(W)=\frac{e^{s p(W)}}{z(s)}dW.\]
The outer holonomy is `V=W1 W2` (up to orientation), and its **induced boundary distribution** is
\[\boxed{d\mu_{t,s}(V)=\frac{Z_{t,s}(V)}{z(t)z(s)}dV=\frac{z(\sqrt{t^2+s^2+2tsv})}{z(t)z(s)}dV.}\tag{3}\]
This follows because its density is the convolution of the two central tilted densities and `∫Z dV=z(t)z(s)`. This is the natural *two-face* boundary measure. It is NOT necessarily the marginal law of the same V in the complete Penrose lattice: exterior magnetic plaquettes and gauge-link couplings modify that law.

## 3. Main theorem: integrated absolute covariance contracts

Let `\sigma_t^2=Var_{\rho_t}(p)=d²/dt² log z(t)`. Then **for all nonnegative t,s**,
\[\boxed{\int_{SU(2)}|C(V;t,s)|d\mu_{t,s}(V)\le\sqrt{\sigma_t^2\sigma_s^2}\le\tfrac12(\sigma_t^2+\sigma_s^2).}\tag{4}\]

**Proof:** The fixed-V covariance obeys `|Cov(p1,p2|V)| ≤ sqrt(Var(p1|V) Var(p2|V))`. Integrate and apply Cauchy–Schwarz on V. By the law of total variance, `E_V[Var(p1|V)]≤Var(p1)=σ_t²` and similarly for the second face, because the **unconditional** joint face law is the product `ρ_t⊗ρ_s`. The result follows exactly without any bound on the worst-case boundary conditional density. QED.

For `t=s=T`, this becomes `E_{\mu_{T,T}}|C|≤σ_T²`. The Bessel-Laplace asymptotic gives
\[\boxed{\sigma_T^2=\frac{3}{2T^2}+O(T^{-3}),\quad T\to\infty.}\tag{5}\]
Thus the isolated block exhibits **typical-boundary connected-source contraction at rate O(T^-2)**, despite the exact `C(-I;T,T)=-1/4`.

**Explicit nonasymptotic bound.** For `T≥1`, set `x=1-p∈[0,2]`. Under `ρ_T`, its unnormalized density is proportional to `e^{-Tx} sqrt(x(2-x))`. Bound the denominator by `(2/(3e)) T^-3/2` using `0≤x≤1/T`, and the second-moment numerator by `sqrt(2) Γ(7/2) T^-7/2`. Since `Var(p)≤E(1-p)²`,
\[\boxed{\sigma_T^2\le\frac{3e\sqrt2\,\Gamma(7/2)}{2T^2}\ <\frac{19.2}{T^2},\qquad T\ge1.}\tag{6}\]
The explicit bound is conservative; use `min(1,19.2/T²)` if desired.

## 4. Quantitative frustrated-boundary tails

With `W1,W2` independent under the product tilted law, use the SU2 quaternion chord estimate
\[1-p(W_1W_2)\le2\big[(1-p(W_1))+(1-p(W_2))\big].\tag{7}\]
This follows by the triangle inequality for unit-quaternion chord distances and squaring. Thus for any `δ∈(0,2)`, the frustrated-boundary event `v≤-1+δ` has `1-v≥2-δ`, and Markov gives
\[\boxed{\mu_{t,s}\{v\le-1+δ\}\le\frac{2}{2-δ}\left[(1-\partial_t\log z(t))+(1-\partial_s\log z(s))\right].}\tag{8}\]
In particular, at `t=s=T`, `1-\partial_T log z(T)=3/(2T)+O(T^-2)`, so (8) is `O(T^-1)` for fixed δ. Equation (4) is sharper for the **average connected covariance** and does not require splitting good and bad boundaries.

## 5. Explicit scope limits and why this does NOT complete R3/R2

1. Equations (1)–(8) are exact identities/inequalities for a **Euclidean isolated two-face Wilson block** with free external boundary links. They are not yet the exact quantum Hamiltonian spatial Feshbach map with retained electric dynamics. The `t,s` in this calculation are Euclidean Wilson couplings, not automatically the physical Hamiltonian magnetic coefficients `b_f`.
2. The full Penrose boundary law may not equal (3) or admit a uniformly bounded Radon–Nikodym ratio to (3). Establishing a **quasilocal comparison of the actual exterior-conditioned boundary measure** is a new, nontrivial task.
3. Contraction of a single covariance does **not** prove the operator-norm contraction of the complete generated higher-character/multiloop source frame. All cumulants, noncommuting physical reconstruction and interaction-induced source normalization remain uncontrolled.
4. The one-face free-boundary geometry is independent of Penrose `C5` harmonic data; Papers 2–4 provide geometry but no quantitative substitute for item 2.
5. **No continuum-uniform physical mass gap** or OS/quantum continuum reconstruction is established by these block identities. A rigorous proof must independently control (i) exterior-conditioned boundary distribution, (ii) generated higher-character connected cumulants in a summable block norm, (iii) low-energy Wilson observability, and (iv) the continuum transfer Hamiltonian construction.

## 6. Constructive acceptance criterion for the next block

If the full conditional boundary marginal `\widetilde\mu_{t,s}` satisfies the density domination `d\widetilde\mu/d\mu_{t,s}≤D` with **D independent of volume and cutoff**, then by (4)
\[\boxed{E_{\widetilde\mu}|C|\le D\sqrt{\sigma_t^2\sigma_s^2}.}\tag{9}\]
This is a *conditional* inheritance theorem, not a claim that such a D exists. For balanced couplings T→∞, it would yield `O(D/T²)` typical-boundary contraction. Whether actual Penrose exterior dynamics supplies any such D is open; it may require a more flexible moment or boundary free-energy comparison than pointwise domination.

**Notes:** Numerical constants are verified by deterministic arithmetic in `check_constants.py`. The overall identity (1) can independently be evaluated by SU2-character Fourier series; no Monte Carlo or spectral-gap assumption was used.