# R3-IR — Adversarial audit of the combined full-Hessian energy inequality

**Date:** 2026-11-11  
**Status:** independent algebra/index audit of the conditional finite-strip energy closure. The displayed differential inequality passes under the explicit local geometric and scalar hypotheses listed below. This is not a theorem promotion.  
**Branch:** audit/r3-ir-h2-trace-to-k-2026-11-10; draft PR #106.  
**Scope:** finite open straight SU(2) strip, product radius-two bi-invariant metric, isolated dressing regime |g|≤10^-3. No inference to PF-I16, Penrose, a 3D regulator, physical-coupling gap, or continuum Yang–Mills.

## 1. Conventions fixed for this audit

Use
\[
\Delta=\operatorname{div}\nabla,\qquad
L=\Delta+2V^K\nabla_K,\qquad V=\nabla S_g,\qquad A=\nabla^2S_g,
\]
and the covector commutator
\[
[\nabla_I,\nabla_K]\omega_J=-R_{IKJ}{}^L\omega_L.
\]
The Hessian is \(H_{IJ}=\nabla_I\nabla_J f_t\), with \(H_{IJ}=H_{JI}\). The one-output weighted norm is
\[
\|H\|_{w,2}^2=\sum_e w_e\sum_d\|H_{ed}\|_F^2,\qquad
w_e=(6/5)^{2\operatorname{dist}(e,\mathcal S)}.
\]
Only the first Hessian link index is weighted. All weights are deterministic, positive, and parallel for the product connection.

## 2. Ordered Hessian evolution: rederived

For the drift term, differentiate in the retained order:
\[
\begin{aligned}
\nabla_I\nabla_J(V^K\nabla_Kf)
={}&(\nabla_I\nabla_JV^K)\nabla_Kf
+(\nabla_IV^K)H_{JK}
+(\nabla_JV^K)H_{IK}\\
&+V^K\nabla_I\nabla_J\nabla_Kf.
\end{aligned}
\]
Subtract \(V^K\nabla_KH_{IJ}=V^K\nabla_K\nabla_I\nabla_Jf\). Since the Hessian of a scalar is symmetric,
\[
\nabla_I\nabla_J\nabla_Kf-\nabla_K\nabla_I\nabla_Jf
=-R_{IKJ}{}^L\nabla_Lf.
\]
Symmetrizing the output slots \(I,J\), and using \(\nabla_IV^K=A_I{}^K\), gives
\[
\begin{aligned}
\nabla_I\nabla_J(V\cdot\nabla f)
={}&V^K\nabla_KH_{IJ}
+A_I{}^KH_{KJ}+A_J{}^KH_{IK}\\
&+(\nabla_{(I}\nabla_{J)}V^K)\nabla_Kf
-V^KR_{(I|K|J)}{}^L\nabla_Lf.
\end{aligned}
\]
Thus the drift contribution to \(\partial_tH\) has exactly the factor two on each of these four terms.

For the scalar Laplacian, the product metric has parallel Ricci tensor, so no \(\nabla\operatorname{Ric}\)-term remains. With the stated Riemann convention,
\[
\partial_tH_{IJ}
=\Delta^\nabla H_{IJ}+\mathcal B(H)_{IJ}
+2V^K\nabla_KH_{IJ}
+2(A_I{}^KH_{KJ}+A_J{}^KH_{IK})
+2\mathcal T_{IJ}{}^K\nabla_Kf
+2\mathcal R_{IJ},
\]
where
\[
\mathcal B(H)=-\operatorname{Ric}\circ H-H\circ\operatorname{Ric}
+2\operatorname{Rm}*H,
\]
\[
\mathcal T_{IJ}{}^K=\nabla_{(I}\nabla_{J)}V^K,\qquad
\mathcal R_{IJ}=-V^KR_{(I|K|J)}{}^L\nabla_Lf.
\]

**Index-order verdict:** the ordered third-dressing tensor has derivative slot \(I\), Hessian slots \(J,K\), and input-gradient slot \(K\). No derivative commutation is used to obtain it. The only reordering of the third derivative of \(f\) is the displayed Codazzi commutator, which is retained as \(\mathcal R\). The two \(A H\) terms and both forcing terms have the factors shown above. No additional \(\nabla\operatorname{Ric}\) term occurs for the product SU(2) metric.

## 3. Curvature damping: block-by-block check

For each three-dimensional SU(2) factor, \(\kappa=1/4\) and \(\operatorname{Ric}=2\kappa I=I/2\). The curvature action on a diagonal block is
\[
\mathcal B(H)_{ee}
=-H_{ee}+\frac12\big((\operatorname{tr}H_{ee})I-H_{ee}\big)
=-\frac32H_{ee}^{\rm TF}.
\]
For \(e\ne d\), the product curvature has no mixed-factor Riemann term and the two Ricci terms give
\[
\mathcal B(H)_{ed}=-H_{ed}.
\]
Consequently,
\[
2\langle H,\mathcal B(H)\rangle_w
=-2\sum_{e\ne d}w_e\|H_{ed}\|_F^2
-3\sum_e w_e\|H_{ee}^{\rm TF}\|_F^2
\le -2K_w^2,
\]
where \(K_w\) contains all mixed blocks and diagonal trace-free blocks. The pure diagonal trace has zero direct curvature damping. This verifies the coefficient \(-2K_w^2\), not a stronger coefficient on the entire Hessian.

## 4. Weighted tensor integration by parts and trace coercivity

Because the product-factor projections and the link weights are parallel, the weighted tensor pairing has
\[
\langle H,(\Delta^\nabla+2\nabla_V)H\rangle_{w,\mu_g}
=-\|\nabla H\|_{w,2,\mu_g}^2.
\]
The drift term cancels the weighted-divergence correction exactly.

The trace projection \(P_T\), which retains only \(H_{ee}^{\rm tr}=(\Delta_ef_t/3)g_e\), is parallel and orthogonal in this one-output norm. Hence
\[
\|\nabla H\|_{w,2}^2
\ge \sum_e w_e\|\nabla_e H_{ee}^{\rm tr}\|_2^2.
\]
The conditional one-link estimate from the trace–gradient record is
\[
\|\nabla_e H_{ee}^{\rm tr}\|_2^2
\ge c_{\rm tr}\|H_{ee}^{\rm tr}\|_2^2
-\ell\|\nabla_ef_t\|_2^2.
\]
Summing gives
\[
\|\nabla H\|_{w,2}^2\ge c_{\rm tr}T_w^2-\ell G_w^2.
\]
This is a lower bound on a component of the **full tensor Dirichlet form**. It is not a claim that \(T_w\) evolves autonomously. In particular, no omitted trace-to-\(K\) commutator is being set to zero.

The trace constants are
\[
c_{\rm tr}=\frac34e^{-49\pi/144}
=0.2575101249909138\ldots,\qquad
\ell=\frac{4c_{\rm tr}}3\left(\frac{49}{576}\right)^2
=0.0024847359266621\ldots.
\]

## 5. Coefficient audit

All constants below use the same \(L^2(\mu_g)\) measure, product metric, and one-output norm.

| Term | Audited bound | Required hypothesis |
|---|---:|---|
| Gradient coercivity | \(c=11/120\) | weighted Bakry–Émery block-Schur estimate |
| Trace leakage | \(\ell=0.0024847359266621\ldots\) | conditional one-link Poincaré and \(|\nabla_eS_g|\le49/576\) |
| Hessian dressing | \(C_H<0.0304266282264\) | four-link/two-face incidence and per-face component envelope \(h<0.00016681265475\) |
| Ordered third dressing | \(C_3<0.049941326676\) | archived ordered component bound \(T_g<0.000250292\), row/column counts \(24,288\), weight transfer \(6/5\), drift factor \(2\) |
| Symmetrized curvature forcing | \(C_R<0.060153181039\) | radius-two SU(2) curvature and \(|\nabla_eS_g|\le49/576\) |

### 5.1 Hessian-of-dressing term

The per-face component bound is
\[
h=\tfrac14\|s_g''\|_\infty+\tfrac12\|s_g'\|_\infty
<0.00016681265475.
\]
Each \(3\times3\) link block has Frobenius norm at most \(6h\). At most six neighboring link blocks occur in a row or column, in addition to the diagonal. Thus the unweighted operator bound is \(42h\), while the one-output weighted similarity bound is
\[
6h(1+6\cdot6/5)=49.2h.
\]
Left multiplication uses \(49.2h\); right multiplication acts on the unweighted second index and uses \(42h\). Therefore
\[
\|2(AH+HA)\|_{w,2}
\le2(49.2+42)h\|H\|_{w,2}
=C_H\|H\|_{w,2}.
\]
No factor is missing in the subsequent energy estimate: pairing this term with \(2H\) gives \(2C_HH_w^2\).

### 5.2 Ordered third-dressing term

For each output pair, at most two faces contain both output links; each contributes at most 12 input link/Lie components. The row sum is at most \(24T_g\). For a fixed input component, at most two faces contain its link, each with \(12^2=144\) ordered output components; the column sum is at most \(288T_g\). Schur gives
\[
\sqrt{24\cdot288}\,T_g<0.020808887.
\]
The input/output link pair lies in a common face whenever the entry is nonzero, so the one-output transfer costs at most \(6/5\). Multiplication by the drift factor two gives
\[
C_3\le2\cdot\frac65\sqrt{24\cdot288}\,T_g
<0.049941326676.
\]

### 5.3 Symmetrized SU(2) curvature forcing

The unsymmetrized contraction is not the energy output. Symmetry of \(H\) requires
\[
\mathcal R_e=\kappa\left[(V_e\cdot v_e)I
-\tfrac12(v_eV_e^\top+V_ev_e^\top)\right].
\]
For unit \(V,v\), its squared Frobenius norm divided by \(\kappa^2|V|^2|v|^2\) is
\[
\frac12+\frac32(V\cdot v)^2\le2.
\]
Thus the exact bilinear constant is \(\sqrt2\), and the factor two in the evolution gives
\[
C_R\le2\kappa\sqrt2\,\frac{49}{576}
=\frac{49\sqrt2}{1152}
<0.060153181039.
\]
The third-dressing and curvature forcing terms therefore contribute at most \(2(C_3+C_R)G_wH_w\) to the Hessian energy derivative.

## 6. The combined differential inequality

Let \(H_w^2=T_w^2+K_w^2\). Pairing the ordered evolution with \(2H\), using the tensor integration-by-parts identity, the curvature damping, the trace Dirichlet lower bound, and the three coefficient bounds gives
\[
\frac{d}{dt}H_w^2
\le -2K_w^2-2c_{\rm tr}T_w^2
+2\ell G_w^2+2C_HH_w^2+2C_GG_wH_w,
\]
where
\[
C_G=C_3+C_R<0.110094507715.
\]
The gradient estimate is
\[
\frac{d}{dt}G_w^2\le-2cG_w^2,\qquad c=11/120.
\]
Since \(0<c_{\rm tr}<1\),
\[
K_w^2+c_{\rm tr}T_w^2\ge c_{\rm tr}(K_w^2+T_w^2)
=c_{\rm tr}H_w^2.
\]
Adding the inequalities yields
\[
\frac{d}{dt}(G_w^2+H_w^2)
\le-2aG_w^2-2bH_w^2+2C_GG_wH_w,
\]
where
\[
a=c-\ell=0.0891819307400046\ldots,\qquad
b=c_{\rm tr}-C_H>0.2270834967645138\ldots.
\]
Equivalently, with \(x=(G_w,H_w)^\top\),
\[
E'(t)\le-2x^\top Qx,\qquad
Q=\begin{pmatrix}a&-C_G/2\\-C_G/2&b\end{pmatrix}.
\]
Using the conservative endpoint constants,
\[
2\sqrt{ab}>0.2846172495169,\qquad
C_G<0.110094507715,
\]
and
\[
\lambda_{\min}(Q)>0.0699034.
\]
The numerical recomputation using the unrounded inputs gives \(\lambda_{\min}(Q)>0.0699034066\). Hence the conditional differential inequality implies
\[
G_w(t)^2+H_w(t)^2
\le e^{-2(0.0699034)t}
\big(G_w(0)^2+H_w(0)^2\big).
\]

**Quadratic-form verdict:** the factors of two, cross-term normalization, trace leakage, and eigenvalue arithmetic are consistent. The positivity test is not merely a determinant check: it is the least eigenvalue of the explicitly displayed symmetric \(2\times2\) matrix.

## 7. Adversarial findings and residual assumptions

### Passed in this audit

1. Ordered derivative bookkeeping for the drift, including the Codazzi commutator.
2. Curvature damping coefficients on mixed and diagonal trace-free blocks.
3. The projection/Dirichlet-form step that supplies pure-trace coercivity without assuming trace-sector invariance.
4. The one-output weighted Schur factors and the distinction between left-weighted and right-unweighted action of \(A\).
5. The symmetrized curvature forcing constant and its evolution factor two.
6. The final \(2\times2\) quadratic-form arithmetic.

### Still conditional, not independently certified here

1. The archived per-face ordered geometric estimate \(|\nabla\operatorname{Hess}p_f|\le3/4\), including its connection corrections.
2. The scalar fixed-point derivative bounds and their applicability uniformly on the full plaquette range for every strip under consideration.
3. The precise straight-strip incidence hypotheses (four links per face, at most two incident faces per link, and the stated overlap counts).
4. The conditional one-link Poincaré input and the weighted Bakry–Émery estimate, as imported from their separate certificates.
5. The radius-two metric and Riemann-sign convention matching the actual implementation of the product strip.

These are explicit dependencies; this audit does not replace their source certificates or broaden their geometry.

### Non-claims

- No pointwise Hessian estimate is established.
- No nonlinear interacting fixed point or volume-uniform residual response is established.
- No physical-coupling spectral gap, PF-I16 result, Penrose transfer, 3D regulator theorem, or continuum mass gap is established.
- The provisional trace-to-\(K\) three-sector calculation remains paused and is not used.

**Decision:** the combined full-Hessian differential inequality passes the adversarial algebra/index audit under the enumerated local hypotheses. The result may be stated as a *conditional finite-strip reference semigroup proposition* after the source certificates are attached and the strip hypotheses are made explicit. Keep PR #106 draft; do not promote a theorem or claim ID.


## Source-level dependency closure addendum (2026-11-11)

The dependencies listed in §7 have now been checked against their original source artifacts in [the local geometry and strip-incidence audit](R3_IR_LOCAL_GEOMETRY_SOURCE_AND_INCIDENCE_AUDIT_2026-11-11.md). In particular, the ordered \(3/4\) plaquette component bound is expanded with all three connection corrections; the scalar \(s_g'''\) tail is bounded by a positive majorant uniformly for \(|g|\le10^{-3}\); and the exact straight-strip face supports establish the row/column incidence counts for every finite strip length. The radius-two metric and curvature conventions agree with the analytic quaternion source.

The independent verifier gives the slightly sharpened values \(C_3<0.049941305\), \(C_H<0.030426617\), \(C_R<0.060153182\), and \(\lambda_{\min}>0.0699034\). Thus the local coefficient and incidence dependencies are no longer left open for the stated finite straight-strip model. The weighted Bochner and conditional trace-Poincaré inequalities remain explicit imported source hypotheses, as does the finite-strip reference scope. No theorem or claim ID is promoted.
