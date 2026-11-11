# R3-IR — Full one-output Hessian energy route: transcript reconciliation and audit

**Date:** 2026-11-10  
**Status:** candidate finite-strip energy closure; local tensor/operator identities require independent index-level verification before theorem promotion.  
**Target branch:** audit/r3-ir-h2-trace-to-k-2026-11-10 (draft PR #106).  
**Scope:** R3-IR finite open SU(2) strip only. This is not PF-I16, the Penrose \(\mathbb Z^5\) model, a certified 3D regulator, or a continuum result.

## 1. Why this audit was added

The previous discussion proposed bypassing the provisional trace-to-\(K\) Schur calculation by estimating the **entire one-output-weight Hessian energy**. The supplied project transcript and existing theorem records show that several important calculations already exist and must remain part of the dependency chain:

1. The corrected original-link SU(2) strip program established the finite-strip free-electric gap \(3\), exact low-order fusion identities, the history-aware reconstruction identity, and exact counterexamples to unrestricted fixed-grade fusion bounds.
2. Source multigrading gives parity and source-order restrictions; the first allowed disconnected-support score coefficient on three faces is nonzero:
   \[
   \left\langle\chi_1(P_1)\chi_1(P_3),S_{121}\right\rangle
   =-\frac{1381}{1261578240}.
   \]
3. The positive scalar connected-tree majorant has factorial growth even in one plaquette, while exact single-face SU(2) dressing has a convergent analytic branch for \(|z|<3/4\).
4. The exact multi-face dressing identity leaves shared-link residual interactions; the dressed reference operator has a finite-strip gap at least \(1/12\), but the all-volume residual expansion remains open.
5. The one-output weighted Hessian-resolvent estimate \(\sqrt{30/11}\) is conditional and requires a weighted source-gradient norm. The archived \(W^{2,4}\) estimate and first/second response estimates do not imply a pointwise interacting Hessian bound.
6. The Penrose signed radial-current criterion is a separate geometric route. Its exact identity and conditional consequences are recorded, but the required uniform interacting-vacuum current bound remains open.

These results are complementary, not interchangeable. In particular, the R3-IR product-strip semigroup estimate cannot be transferred to the corrected physical spin-network recurrence, the PF-I16 auxiliary model, or a Penrose refinement without a model-specific bridge.

## 2. Candidate full-Hessian estimate

Let
\[
G_w^2=\sum_e w_e\|\nabla_e f_t\|_2^2,\qquad
H_w^2=\sum_{e,d}w_e\|\nabla_d\nabla_e f_t\|_2^2,
\]
with \(w_e=(6/5)^{2d(e,\mathcal S)}\). This is the **one-output** norm: only the first Hessian link index is weighted.

Decompose the Hessian orthogonally into the pure diagonal trace sector \(T_w\) and the remaining mixed/trace-free sector \(K_w\):
\[
H_w^2=T_w^2+K_w^2.
\]
The already recorded product-manifold curvature calculation gives reference damping at least \(1\) on \(K_w\); the pure trace sector has zero direct curvature damping and is controlled by the conditional one-link Poincaré inequality.

The existing trace calculation supplies
\[
c_{\rm tr}=\frac34e^{-49\pi/144}
=0.2575101249909138\ldots,
\]
\[
B=\frac{49}{576},\qquad
\ell=\frac{4c_{\rm tr}B^2}{3}
=0.00248473592666\ldots,
\]
and the weighted gradient estimate supplies
\[
\frac{d}{dt}G_w^2\le-2cG_w^2,\qquad c=\frac{11}{120}.
\]

The local isolated-dressing bounds give
\[
h=\frac14\|s_g''\|_\infty+\frac12\|s_g'\|_\infty
<0.00016681265475.
\]
For each \(3\times3\) link block of \(A=\nabla^2S_g\), the component envelope is \(2h\), hence the Frobenius block norm is at most \(6h\). With at most six off-diagonal neighboring links per link, the unweighted block row/column sums are at most \(42h\). For neighboring links,
\[
\sqrt{w_e/w_d}\le6/5,
\]
so the weighted similarity row/column sums are at most \(49.2h\). Thus the candidate operator estimates are
\[
\|A\|_{\rm op}\le42h,\qquad
\|W^{1/2}AW^{-1/2}\|_{\rm op}\le49.2h.
\]

If the full ordered Hessian drift is indeed
\[
\mathcal D_S^{(2)}(H)=2(AH+HA),
\]
then left multiplication is controlled in the one-output norm by \(49.2h\), right multiplication by \(42h\), and
\[
\|\mathcal D_S^{(2)}(H)\|_{2,w,\mathrm{out}}
\le 2(49.2+42)h\|H\|_{2,w,\mathrm{out}}
=:C_H\|H\|_{2,w,\mathrm{out}},
\]
where
\[
C_H=182.4h<0.03042662823.
\]

The archived ordered third-dressing tensor certificate gives an unweighted gradient-to-ordered-Hessian operator norm below \(0.02081\). If every nonzero tensor entry has its input link and first output link in one common plaquette, the one-output weight transfer costs at most \(6/5\). Including the drift factor \(2\),
\[
C_3=2\cdot\frac65\cdot0.02081=0.049944.
\]

### Curvature-ordering term

For a radius-two SU(2) factor, the sectional curvature is \(\kappa=1/4\). The relevant Codazzi commutator has the constant-curvature form, up to the fixed Riemann-sign convention,
\[
S^k(\nabla_iH_{jk}-\nabla_kH_{ij})
=\kappa\big((S\cdot v)g_{ij}-S_jv_i\big),
\]
where \(S=\nabla_eS_g\) and \(v=\nabla_ef_t\) in the same link factor. In dimension three,
\[
\|(S\cdot v)I-vS^\top\|_F
\le(\sqrt3+1)|S||v|.
\]
Using the already recorded coarse bound \(|\nabla_eS_g|\le B\), and including the factor \(2\) from the drift, gives the **candidate conservative** curvature forcing
\[
C_R\le2\kappa(\sqrt3+1)B
=0.11620702220\ldots.
\]
The exact index order, sign convention, and symmetrization in the Hessian evolution must still be independently checked against the chosen left-invariant frame. This value is not promoted as a certified coefficient.

Set
\[
C_G=C_3+C_R\le0.16615102220\ldots.
\]

## 3. Conditional combined-energy diagnostic

If the preceding operator estimates and the full Hessian evolution identity are verified in the same weighted \(L^2(\mu_g)\) norm, the complete Hessian energy would satisfy
\[
\frac{d}{dt}H_w^2
\le-2K_w^2-2c_{\rm tr}T_w^2
+2\ell G_w^2+2C_HH_w^2+2C_GG_wH_w.
\]
Since \(c_{\rm tr}<1\),
\[
K_w^2+c_{\rm tr}T_w^2\ge c_{\rm tr}H_w^2.
\]
Adding the gradient inequality yields
\[
\frac{d}{dt}(G_w^2+H_w^2)
\le-2aG_w^2-2bH_w^2+2C_GG_wH_w,
\]
where
\[
a=c-\ell=0.0891819307400\ldots,\qquad
b=c_{\rm tr}-C_H=0.22708349676\ldots.
\]
The associated \(2\times2\) quadratic form is positive if
\[
C_G<2\sqrt{ab}=0.28461724940\ldots.
\]
The candidate value \(C_G\le0.16615102220\ldots\) is below this threshold. Its smaller eigenvalue is
\[
\lambda_{\rm cand}
=\frac{a+b-\sqrt{(a-b)^2+C_G^2}}2
=0.0501709102\ldots>0.
\]
Thus the **conditional candidate conclusion** is
\[
G_w(t)^2+H_w(t)^2
\le e^{-2\lambda_{\rm cand}t}
\big(G_w(0)^2+H_w(0)^2\big).
\]

This route, if verified, would avoid estimating the trace-to-\(K\) block separately: it controls the full Hessian as one tensor and uses the reference curvature damping plus the trace Poincaré inequality. It would supersede the provisional three-sector Schur diagnostic in the H2 branch. It does **not** make the provisional trace-to-\(K\) incidence count correct or unnecessary for the trace-block derivation itself; it offers a distinct route around that calculation.

## 4. Exact audit obligations before promotion

The candidate is not yet a theorem. The following must be independently checked from the ordered tensor formulas, not inferred from scalar incidence summaries:

1. **Full Hessian evolution identity:** derive every term in \(\partial_t\nabla^2 f_t\), fixing covariant derivative order and the sign convention for \(R\). Confirm that the dressing terms split exactly into \(2(AH+HA)\), the ordered third-dressing tensor applied to \(\nabla f_t\), and the stated Codazzi curvature remainder, with no additional terms.
2. **Block incidence for \(A\):** verify coincident-link and distinct-link blocks, the at-most-six off-diagonal neighbor count, the Frobenius block envelope \(6h\), and both weighted Schur sums.
3. **Ordered third tensor transfer:** verify the archived \(0.02081\) Schur certificate in the precise output/input index order used here, and prove the one-output weight transfer \(6/5\) for every nonzero component.
4. **Curvature contraction:** compute the exact SU(2) left-invariant-frame tensor, its symmetrization, and its operator norm. The displayed \(C_R\) is a candidate upper bound pending this check.
5. **Measure and norm compatibility:** verify that the gradient, trace, mixed/trace-free and full-Hessian inequalities all use the same \(\mu_g\), metric normalization, deterministic weights, and one-output norm.
6. **Initial-data and resolvent scope:** state the smooth-core assumptions and the precise semigroup/resolvent extension. This remains an \(L^2\) weighted estimate, not an \(L^\infty\) estimate.

The old H2 trace-to-\(K\) calculation remains provisional. Its candidate \(C_{TK}\), candidate curvature addition, and three-sector Schur diagnostic must not be described as a completed closure.

## 5. What this would and would not close

If all six audits pass, the result closes a **finite-strip, reference dressed-semigroup gradient–Hessian contraction** in the one-output weighted \(L^2\) norm. That is a meaningful improvement and a cleaner route than the provisional trace-to-\(K\) block.

It still does not give a pointwise Hessian bound for the nonlinear interacting ground-state score. It does not prove the bilinear fixed-point estimate for
\[
u_\lambda=-\lambda R_NQ_NW_N+
R_NQ_N\langle\nabla u_\lambda,\nabla u_\lambda\rangle,
\]
nor a volume-uniform all-orders connected residual expansion. The archived \(L^4\) estimates do not supply the missing pointwise control, and the product-weight two-index norm has a separate spatial-weight obstruction.

It also does not establish the physical original-link spin-network all-history recurrence, the PF-I16 route, a genuine Penrose 3D refinement, a uniform interacting gap at physical coupling, or the four-dimensional continuum Yang–Mills mass gap.

**Research decision:** retain PR #106 as a draft audit. Add this full-Hessian route as a candidate bypass, do not promote it to a theorem, and prioritize the exact covariant Hessian evolution/index audit before doing further scalar Schur calculations.
