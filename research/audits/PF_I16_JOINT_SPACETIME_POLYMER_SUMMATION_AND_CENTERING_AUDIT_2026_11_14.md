# PF-I16 — Joint space-time polymer summation and centering audit

**Date:** 2026-11-14  
**Status:** local activity arithmetic verified; proposed KP criterion is not yet established. A centering-norm loss and the missing support-sensitive joint tree must be resolved.  
**Scope:** finite-volume product-rotor reference path law and its local interaction expansion. No interacting-vacuum or continuum result.

## 1. Feynman–Kac expansion and the required joint estimate

For
\[
\widehat H=K+\sum_{X\in\mathcal X}v_X,
\qquad K=\sum_e a_e(-\Delta_e),
\]
the finite-volume Feynman–Kac formula gives
\[
\log Z_T
=\sum_{m\ge1}\frac{(-1)^m}{m!}
\sum_{X_1,\ldots,X_m}
\int_{[0,T]^m}
\kappa_0\bigl(v_{X_1}(t_1),\ldots,v_{X_m}(t_m)\bigr)
\,d\mathbf t
\]
as a formal coefficient expansion near zero interaction. The reference path law is a product over links. If the support-overlap graph
\[
G_{\rm ov}(X_1,\ldots,X_m),\qquad
ij\in E(G_{\rm ov})\iff X_i\cap X_j\ne\varnothing,
\]
is disconnected, the cumulant vanishes exactly.

The established all-orders temporal estimate for centered bounded insertions has the form
\[
|\kappa_0(A_1(t_1),\ldots,A_m(t_m))|
\le 2^m\prod_i\|A_i\|_\infty\,
\mathbf1_{\{G_{\rm ov}\text{ connected}\}}
\sum_{T\in\mathcal T_m}
\prod_{ij\in T}e^{-\Delta_0|t_i-t_j|}.
\tag{1.1}
\]
The temporal tree is over the complete graph on row labels. The support information in (1.1) is only the disconnectedness indicator; it does not require the temporal tree edges to be support-overlap edges.

For a genuine joint space-time estimate, the desired form is instead a single tree carrying both constraints, for example
\[
|\kappa_0(A_1(t_1),\ldots,A_m(t_m))|
\le C_{\rm st}^{m}\prod_i\|A_i\|_\infty
\sum_{T\in\mathcal T(G_{\rm ov})}
\prod_{ij\in T}e^{-\Delta_0|t_i-t_j|},
\tag{1.2}
\]
or a rigorously derived weighted-dependency-graph/KP bound with the same combined support and temporal control. Equation (1.2) is a target, not an established theorem. The exact support-sensitive estimates at orders two and three, and the recorded degree-eight elementary-tensor order-four result, do not prove (1.2) at all orders.

## 2. The local activity arithmetic

Let \(x=b_0/a_0\le1/50000\), \(\Delta_0=3a_0/4\), and use the support weight \(e^{|X|/8}\). A link is incident to at most eight accepted face supports and at most 224 adjacent-face-pair supports. The face support has at most four links; a pair support has at most eight links. The verified uncentered local activity is
\[
\begin{aligned}
\kappa_H
&:=\sup_e\sum_{X\ni e}
\frac{\|v_X\|_\infty}{\Delta_0}e^{|X|/8}\\
&\le
\frac{8(64x+64x^2)(1.65)+224(512x^2)(2.72)}{3/4}
<0.022695.
\end{aligned}
\tag{2.1}
\]
At \(x=1/50000\), the displayed upper bound is
\[
\kappa_H\le0.0226948246187.
\]
The corresponding arithmetic used in the earlier conditional KP proposal is
\[
4\kappa_H<0.09078<\frac18.
\tag{2.2}
\]
This numerical inequality is correct. It is not, by itself, a proof of KP convergence.

## 3. Centering changes the constant when using uncentered local activities

The all-orders projection-tree theorem is stated for centered observables. For an uncentered local interaction \(v_X\), cumulant invariance permits replacing it by
\[
\bar v_X=v_X-\mathbb E_0v_X,
\]
but the only bound currently justified from the recorded sup-norm estimate is
\[
\|\bar v_X\|_\infty\le2\|v_X\|_\infty.
\tag{3.1}
\]
Thus the centered-observable coefficient \(2^m\) gives a bound with coefficient \(4^m\) when it is expressed in terms of the uncentered activities in (2.1). Equivalently, the crude centering-safe activity is at most \(2\kappa_H\). Under the proposed criterion
\[
2C_{\rm time}\kappa_H<\frac18,
\tag{3.2}
\]
this crude transfer uses \(C_{\rm time}=4\), and gives
\[
8\kappa_H<0.18156,
\]
which does **not** satisfy \(1/8=0.125\).

This is a loss in the available upper bound, not a lower bound on the true centered activity and not evidence that the expansion diverges. The local interaction may have a substantially smaller oscillation than twice its sup norm, but that sharper estimate has not been derived from the current face/pair formulas.

To recover the proposed margin at the recorded coupling, one needs one of the following:
1. Prove that the relevant local insertions are already centered (with the exact measure and parameter dependence stated).
2. Compute a sharper local centered norm \(\|v_X-\mathbb E_0v_X\|_\infty\), or a uniform oscillation estimate, and re-evaluate the weighted sum.
3. Prove a temporal cumulant theorem directly in terms of an oscillation/seminorm that avoids the factor-two centering loss.

For example, if \(\|v_X-\mathbb E_0v_X\|_\infty\le c\|v_X\|_\infty\) uniformly, then the simple activity test requires
\[
4c\kappa_H\le\frac18,
\qquad c\le\frac1{32\kappa_H}\approx1.377.
\tag{3.3}
\]
The generic bound (3.1) only gives \(c=2\).

## 4. Why separate spatial and temporal trees are insufficient

The temporal estimate (1.1) has a complete-graph tree sum. Exact spatial cancellation says only that disconnected support families vanish. If one independently applies a spatial tree-graph bound to enforce connected support and then multiplies by the temporal tree sum, the two Cayley factors give growth of order
\[
\frac{m^{m-2}m^{m-2}}{m!},
\]
which is superexponential in \(m\). The Feynman–Kac \(1/m!\) normalization does not absorb this product. This is the specific obstruction already identified in the connected-resolvent frontier.

Consequently, the inequality (2.2) cannot be promoted to an actual KP criterion by multiplying a spatial tree estimate and a temporal tree estimate. The proof needs a single joint tree such as (1.2), or a different connected-subset resummation whose complete combinatorics are bounded by \(C^m m!\) before the time integration/normalization.

The product-process tensor-gap bridge is compatible with (1.1) and explains why signed row-product cumulants can be bounded before taking absolute values over link-slot partitions. It gives a complete-graph temporal tree, however, and does not supply the missing support-sensitive tree in (1.2).

## 5. Marked roots and the projective-norm alternative

The existing weighted local arithmetic records
\[
\kappa_a<0.022863,\qquad
\kappa_{ab}<0.023199,
\]
for first- and second-cut marked-root families. The source observables have support size at most 25, hence the support-weight factor is bounded by \(e^{25/8}<23\). These are finite per-link marked-root bounds, not background activities. A uniform anchored sum for the full family of higher mixed-cut roots, with its dependence on the number of cuts and its source-support multiplicity, is still required.

The alternative projective-tensor estimate gives
\[
\kappa_\pi(x)
\le4505.6x+2.5890\times10^7K_6^2x^2.
\]
At \(x=1/50000\), its linear face term alone is \(0.090112\). It therefore cannot certify the candidate condition \(2C_{\rm st}\kappa_\pi\le1/8\) for the relevant temporal constants, even before the pair term and the unknown \(K_6\). This is a failure of that sufficient upper majorant, not a lower bound on the true projective norm. The direct tensorized \(L^\infty\) route remains preferable if the centered-norm and joint-tree issues can be resolved.

## 6. Exact next obligations

1. Derive a centered local activity bound from the explicit \(v_f\) and \(v_{fg}\) formulas; do not silently identify \(\|v_X\|_\infty\) with \(\|v_X-\mathbb E_0v_X\|_\infty\).
2. Prove the all-orders support-sensitive joint tree estimate (1.2), or an equivalent WDG/quasi-factorization theorem for the actual product insertions. The auxiliary row-sum quasi-factorization variables do not encode row products; the nilpotent row-diagonal identity is exact but its weighted connected-log norm is open.
3. Sum all marked cut/source roots with an anchored support convention and explicit order dependence.
4. Only after 1–3, insert the resulting constants into the space-time polymer/KP criterion and prove uniform Feynman–Kac/ground-energy convergence.

**Conclusion.** The per-link uncentered activity arithmetic (2.1) is verified, and the centered temporal tree theorem is available with its stated hypotheses. The current combination does not yet establish a KP condition: the crude centering-safe constant misses the proposed threshold, and the all-orders support-sensitive joint tree remains open. No P0–P5 gate is promoted.


## 7. Superseding results — QF closed; projective pair tail sharpened

Two former inputs in Sections 5–6 are now superseded.

First, actual-insertion cross-split QF is **ESTABLISHED** for arbitrary bounded local multiplication observables under independent stationary link paths with a uniform one-link \(L^2\) semigroup gap. The proof conditions on all other link paths and applies the interlaced-time one-link covariance lemma to the remaining shared link. See
[PF-I16 arbitrary-local-observable link interpolation](PF_I16_ARBITRARY_LOCAL_OBSERVABLE_LINK_INTERPOLATION_2026_11_13.md). The QF estimate carries the exact link multiplicity \(|X_i\cap X_j|\). It does not yet imply the support-restricted all-orders tree (1.2).

Second, the previous \(K_6^2\)-dependent projective pair majorant is superseded by the all-orders character-tail and Casimir-block estimate in
[PF-I16 all-orders radial character tail and face/pair projective norm](PF_I16_ALL_ORDERS_RADIAL_CHARACTER_TAIL_AND_FACE_PAIR_PROJECTIVE_NORM_2026_11_14.md):
\[
\mathfrak p(v_f)\le256b_0,\qquad
\mathfrak p(v_{fg})\le20000\,b_0^2/a_0,
\]
and the resulting per-link support-weighted activity satisfies
\[
\kappa_\pi\le0.096611
\quad\text{at }b_0/a_0=1/50000.
\]
This is a substantial improvement over the former pair majorant, but \(2\kappa_\pi\le1/8\) is still not certified; the improved upper majorant gives \(2\kappa_\pi\le0.193222\). This remains a failure of a sufficient upper test, not a lower bound on the true norm.

The current boundary is therefore:
- Actual-insertion cross-split QF: **ESTABLISHED** under the stated product-Markov hypotheses.
- All-orders radial character tail and full face/pair projective tensor bounds: **ESTABLISHED** under the recorded rotor and incidence/allocation hypotheses.
- Support-restricted all-orders space-time cumulant tree: **OPEN**.
- Marked-root sum, quantum KP convergence, interacting-vacuum Poincare inequality, and continuum mass gap: **OPEN**.

No P0–P5 gate is promoted.
