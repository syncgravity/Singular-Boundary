# PF-I16 — Scope bridge from row-factor QF to the actual face/pair insertions

**Date:** 2026-11-14  
**Status:** row-factor cross-split QF is established under independent stationary link Markov hypotheses; its extension to the actual face/pair insertions is NOT established. This note prevents an invalid promotion of the joint-tree gate.

## 1. What the link-by-link interpolation proves

The whole-path interpolation audit proves a cross-split estimate for observables with an explicit tensor-product form
\[
F_i(x)=\prod_{e\in X_i}f_{i,e}(x_e).
\]
For a split \(I=J\sqcup K\), its direct conclusion is
\[
\left|\mathbb E\prod_{i\in I}F_i(t_i)
-\mathbb E\prod_{i\in J}F_i(t_i)\,
 \mathbb E\prod_{i\in K}F_i(t_i)\right|
\le 2|I|\prod_i\|F_i\|_\infty
\sum_{i\in J,j\in K}|X_i\cap X_j|e^{-\Delta_0|t_i-t_j|}.
\tag{1.1}
\]
The factorization of the row norm into one-link norms uses the product state space. The derivative at a shared link is a covariance of products of one-time functions of that one link path.

This is not a theorem for an arbitrary bounded multiplication observable on the multi-link support.

## 2. The actual face insertion has additional structure

The centered one-face insertion is
\[
v_f=-\rho_fb_fp_f,\qquad p_f=\tfrac12\operatorname{Tr}(U_1U_2U_3U_4)
\]
(up to the fixed orientation/inversion convention on the four boundary links).

The fundamental trace does admit a finite tensor decomposition:
\[
p_f=\frac12\sum_{a,b,c,d=1}^{2}
(U_1)_{ab}(U_2)_{bc}(U_3)_{cd}(U_4)_{da}.
\tag{2.1}
\]
There are 16 rank-one slot terms. Since each fundamental matrix entry has modulus at most one, this gives the crude projective decomposition cost
\[
\|p_f\|_{\pi}\le8.
\tag{2.2}
\]
Thus the face term alone can be reduced to a finite sum of row-factor observables, albeit with a factor-eight norm loss if one uses only this elementary expansion.

The pair insertion is different:
\[
v_{fg}=2\sum_{e\in\partial f\cap\partial g}
a_e\langle\nabla_es_f(H_f),\nabla_es_g(H_g)\rangle,
\qquad s_f(H)=\widetilde s_f(p_f(H)).
\tag{2.3}
\]
By the chain rule,
\[
\nabla_es_f(H_f)=\widetilde s_f'(p_f(H_f))\,\nabla_ep_f(H_f).
\tag{2.4}
\]
Although \(\nabla_ep_f\) is a finite sum of products of link matrix entries and Lie-algebra coefficients, the multiplier \(\widetilde s_f'(p_f)\) is a non-polynomial function of the full face holonomy. Equation (2.4) is not itself a finite product of one-link functions. A convergent character/Peter–Weyl expansion with a quantitative projective norm is needed to reduce it to the row-factor class.

## 3. Why the existing projective estimate does not close the activity gate

The current projective-insertion audit records the sufficient upper envelope
\[
\kappa_\pi(x)
\le4505.6x+2.5890\times10^7K_6^2x^2,
\qquad x=b_0/a_0,
\]
with \(K_6<9.11\). At \(x=1/50000\), the linear face term alone is
\[
4505.6/50000=0.090112.
\]
Consequently even the optimistic face-only test fails:
\[
2\kappa_{\pi,\mathrm{face}}
\ge0.180224>\frac18.
\tag{3.1}
\]
This is failure of that sufficient projective majorant, not a lower bound on the true projective norm and not evidence of divergence. It means the present projective estimate cannot be inserted into the row-factor QF proof and used to certify the proposed KP threshold.

The exact centering result for \(v_f,v_{fg}\) does not repair this by itself: centering controls the mean and sup norm of the full insertion, whereas (1.1) requires a controlled sum of one-link tensor-factor norms.

## 4. What would complete the bridge

A valid extension needs one of the following, with constants uniform in the source volume:

1. **Quantitative tensor decomposition.** Prove
   \[
   F=\sum_{\alpha}c_\alpha\prod_{e\in X}f_{\alpha,e}(x_e),
   \qquad
   \sum_\alpha|c_\alpha|\prod_e\|f_{\alpha,e}\|_\infty
   \le \mathfrak p(F),
   \]
   for each actual \(v_f\) and \(v_{fg}\), with a weighted activity sum of the resulting \(\mathfrak p(F)\)'s below the required threshold.

2. **Direct multi-link interpolation.** Extend the whole-path interpolation derivative estimate from rank-one row factors to the actual smooth local functions, controlling the relevant coordinate influence/tensor norm directly by the local centered activity. A mere \(L^\infty\) bound is insufficient for this step.

3. **A sharper function-space norm.** Identify a Banach tensor norm (or projective Sobolev norm) stable under the product Markov semigroup, prove its interpolation contraction, and evaluate it on (2.3)–(2.4).

The all-orders WDG route may then be applied only after its product quasi-factorization hypothesis is verified in that same function-space norm. The WDG theorem does not turn an \(L^\infty\) bound on a non-product local function into a tensor-factor bound.

## 5. Gate disposition

- Exact centering of \(v_f\) and \(v_{fg}\): **ESTABLISHED** under the recorded product-Haar geometry.
- One-link interlaced-time covariance: **ESTABLISHED** under the stationary Markov \(L^2\)-gap hypothesis.
- Cross-split QF for rank-one row-factor observables: **ESTABLISHED**, with link multiplicity.
- Cross-split QF for the actual face/pair insertions: **OPEN**.
- All-orders support-sensitive joint tree for the actual insertions: **OPEN**.
- Marked-root/cluster sum and quantum KP convergence: **OPEN**.
- Interacting-vacuum Poincaré inequality and continuum mass gap: **OPEN**.

No P0–P5 acceptance status is promoted.

**Next concrete calculation:** derive an explicit character expansion and projective norm for \(\widetilde s_f'(p_f)\), then contract the shared-link Lie-algebra index in (2.3) before taking absolute values. Compare the resulting *centered* face/pair tensor activities with the \(1/8\) threshold. If that norm is too costly, replace it with a semigroup-stable coordinate-influence norm and prove the interpolation estimate in that norm.


## 6. Superseding scope correction — arbitrary local observables

A subsequent re-examination of the interpolation derivative shows that the rank-one restriction in Sections 1 and 4 was unnecessary. After conditioning on all other link paths, an arbitrary bounded local observable (F_i) becomes a one-time bounded function of the single interpolated link, with norm at most (|F_i|_\infty). The one-link interlaced-time covariance lemma therefore applies directly. The complete proof and exact conditional derivative are recorded in [PF-I16 arbitrary-local-observable link interpolation](PF_I16_ARBITRARY_LOCAL_OBSERVABLE_LINK_INTERPOLATION_2026_11_13.md).

Accordingly, replace the status bullets above as follows:
- Cross-split QF for arbitrary bounded local multiplication observables: **ESTABLISHED** under the independent stationary link-path and uniform L2-gap hypotheses.
- Cross-split QF for the actual face/pair insertions: **ESTABLISHED** under those same hypotheses, with link-multiplicity bonds.
- All-orders support-sensitive joint cumulant tree: **OPEN**.
- Marked-root/cluster sum, quantum KP convergence, interacting-vacuum Poincare inequality, and continuum mass gap: **OPEN**.

The previous claim that a quantitative tensor decomposition of (s_f'(p_f)) is a prerequisite for the cross-split QF is withdrawn. The radial derivative and contracted pair calculations in the new audit sharpen the local pair activity independently, but are not needed to prove QF. No P0–P5 status is promoted.
