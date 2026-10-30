# Physical-resolvent bound for the four-neighbor eighth mixed response

**Date:** 2026-10-30. **Status:** exact finite-volume quantitative **gap-dependent** upper bound in the genuine Gauss-invariant Wilson Hamiltonian. This is a conditional finite-volume result and **does not** close the full-coupling mixed-response sign estimate or the continuum mass gap.

## Model

Use the archived four-neighbor setup: a deleted interior rhombus \(f\) with four distinct neighboring faces \(g_1,\ldots,g_4\), coefficients \(b_i>0\), and
\[
H(t)=H_{\rm rest}+\sum_{i=1}^4t_i b_i(1-p_{g_i}),
\qquad t\in[0,1]^4.
\]
All nonselected retained Wilson terms are in \(H_{\rm rest}\). Let \(P(t)\) be the rank-one spectral projection onto the unique positive **physical** ground state, with energy \(E(t)\), and let \(\delta(t)>0\) be the separation from all other eigenvalues on the full Gauss-invariant Hilbert space. Compact finite-link ellipticity yields \(\delta(t)>0\) and continuity on the coupling cube; hence
\[
\delta_*:=\min_{t\in[0,1]^4}\delta(t)>0.
\]
No regulator-uniform lower bound on \(\delta_*\) is assumed or claimed.

Let \(k_a(W_f)\ge0\) be the existing positive central convolution cap observable, \(0\le k_a\le\nu_a\), and define
\[
F_a(t)=\operatorname{Tr}[k_a(W_f)P(t)].
\]

## Theorem: explicit eighth mixed derivative bound

For every real \(t\in[0,1]^4\),
\[
\boxed{
\big|\partial_1^2\partial_2^2\partial_3^2\partial_4^2F_a(t)\big|
\le64\,\nu_a\,16^8\,\frac{\prod_{i=1}^4b_i^2}{\delta_*^8}.
}\tag{MR-1}
\]

Thus the previously archived negative mixed response
\[
N_a=\int_{[0,1]^4}\prod_{i=1}^4(1-s_i)
\left[\,-\partial_1^2\partial_2^2\partial_3^2\partial_4^2F_a(s)\,\right]_+ds
\]
satisfies the explicit but generally inadequate estimate
\[
\boxed{
N_a\le4\,\nu_a\,16^8\frac{\prod_{i=1}^4b_i^2}{\delta_*^8}.
}\tag{MR-2}
\]

### Proof

Fix a real \(t\). The scalar \(\sum t_i b_i\) does not affect eigenprojections; the complex perturbation of the nontrivial Hamiltonian is \(-\sum_i(z_i-t_i)b_i p_{g_i}\), with norm bounded by \(\sum_i|z_i-t_i|b_i\). Choose complex polydisk radii \(r_i=\delta_*/(16b_i)\). On the distinguished-boundary polydisk, the perturbation norm is at most \(\delta_*/4\).

Take the ground-energy contour \(|\zeta-E(t)|=\delta(t)/2\ge\delta_*/2\). The unperturbed resolvent has norm at most \(2/\delta(t)\le2/\delta_*\). A Neumann-series argument therefore gives complex perturbed resolvent norm at most \(4/\delta_*\) on this contour and everywhere in the polydisk. The Riesz projector
\[
P(z)=\frac1{2\pi i}\oint(\zeta-H(z))^{-1}d\zeta
\]
is analytic, has rank one throughout, and satisfies the conservative operator norm bound \(\|P(z)\|\le (2\pi\cdot\delta(t)/2)(4/\delta_*)/(2\pi)\); to obtain a uniform constant independent of \(\delta(t)/\delta_*\), use the **local radius** instead:
\[
r_i(t)=\delta(t)/(16b_i).
\]
Then the perturbation bound is \(\delta(t)/4\), the contour norm at most \(4/\delta(t)\), and \(\|P(z)\|\le2\). Since rank-one projections need not be orthogonal for complex couplings, their trace norms equal their operator norms. Therefore \(|F_a(z)|\le2\nu_a\) throughout the local polydisk.

Multivariable Cauchy estimates give
\[
|\partial_1^2\cdots\partial_4^2F_a(t)|
\le (2!)^4\,2\nu_a\prod_i r_i(t)^{-2}
=32\nu_a16^8\frac{\prod_i b_i^2}{\delta(t)^8}.
\]
In particular this implies MR-1 with the stated more conservative factor \(64\). Finally \(\int_0^1(1-s_i)ds_i=1/2\) for each of the four variables, so integrating MR-1 and dividing by \(16\) proves MR-2. QED.

## Comparison with the required cap survival

The archived FN-5 gate requires \(N_{a_h}\le\alpha_{a_h}^2/2\), with \(\alpha_a=\int\phi_a\), \(\nu_a=\int\phi_a^2\), and a fixed-shape bump of radius \(a_h\asymp\sqrt h\). Here \(\alpha_a^2\asymp a^6\), \(\nu_a\asymp a^3\). MR-2 would require the extremely strong condition
\[
\frac{\prod_i b_i^2}{\delta_*^8}=O(a_h^3)
\]
with a small enough constant, whereas the existing physical private-link trial estimate provides an **upper**, not a lower, bound on the finite-volume gap near a coordinate hyperplane, \(\delta(0)\lesssim A_f=O(1)\), while \(b_i\asymp h^{-2}\). Thus the available resolvent bound has the wrong scaling to prove full-coupling cap survival.

This is a precise failure of this *absolute-value, gap-dependent* technique. It does not show that the physical signed mixed response is adverse, nor preclude cancellations or Wilson-specific sign estimates. The eighth mixed derivative's negative part at full coupling remains open.

## Important dependencies and scope

The four-neighbor mixed Taylor formula, positive convolution observable and selection are from \`research/theorems/R3_IR_FOUR_NEIGHBOR_SPIN_SELECTION_AND_MIXED_RESPONSE_2026-10-29.md\`. The physical private-link trial upper gap is from \`research/theorems/R3_IR_WILSON_BRIDGE_SPIN_SELECTION_AND_GAP_OBSTRUCTION_2026-10-29.md\`. The new calculation supplies explicit **physical** multivariable resolvent bounds rather than assuming a gap uniform in the regulator; it does not independently verify historical source archives, nor does it establish R3-IR or R2 continuum.
