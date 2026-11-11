# R3-IR — Conditional full-Hessian finite-strip semigroup proposition

**Date:** 2026-11-11  
**Status:** consolidated conditional proposition; not a promoted theorem or claim.  
**Branch:** \`audit/r3-ir-h2-trace-to-k-2026-11-10\`; draft PR #106.  
**Scope:** finite open straight SU(2) strip, product radius-two bi-invariant metric, isolated analytic dressing regime \(|g|\le 10^{-3}\).  
**Route:** full covariant Hessian / one-output weighted energy. The provisional trace-to-\(K\) three-sector calculation is not used.

## Proposition

Fix a finite open straight strip with \(N\ge1\) plaquettes and original-link set \(E\), with face supports
\[
E(f_m)=\{v_m,v_{m+1},t_m,b_m\},\qquad 1\le m\le N.
\]
Let \(M_E=\mathrm{SU}(2)^E\) carry the product of the radius-two bi-invariant metrics, let \(p_f\) be the oriented plaquette trace, and let
\[
S_g(U)=\sum_{f}s_g(p_f(U)),\qquad
d\mu_g=Z_g^{-1}e^{2S_g}\,d\mathrm{Haar},
\]
where \(s_g\) is the smooth isolated-dressing branch certified for \(|g|\le10^{-3}\). Put
\[
\Delta=\operatorname{div}\nabla,\qquad
L=\Delta+2\nabla S_g\cdot\nabla,\qquad
P_t=e^{tL}.
\]
Let \(\mathcal S\subset E\) be a nonempty reference link set and define
\[
w_e=\left(\frac65\right)^{2d(e,\mathcal S)}.
\]
For \(f_t=P_tf\), write \(G_w,H_w\) for the one-output weighted derivative seminorms
\[
G_w(t)^2=\sum_{e\in E}w_e
\|\nabla_ef_t\|_{L^2(\mu_g)}^2,
\qquad
H_w(t)^2=\sum_{e,d\in E}w_e
\|\nabla_d\nabla_ef_t\|_{L^2(\mu_g)}^2.
\]
Only the first Hessian link index is weighted.

Assume the coefficient-specific scalar derivative enclosure and the local geometric hypotheses recorded in §§2–3 below. The weighted Bochner and conditional one-link trace–Poincaré inequalities are derived there with sharpened constants from the same global scalar certificate. Then, for every \(f\in H^2(M_E)\) and every \(t\ge0\),
\[
\boxed{
G_w(t)^2+H_w(t)^2
\le e^{-2\lambda_*t}
\bigl(G_w(0)^2+H_w(0)^2\bigr),
\qquad \lambda_*>0.4955484.
}
\tag{1.1}
\]
The constants in this estimate are independent of the number \(N\) of strip faces under the stated uniform local hypotheses. The norm is the one-output weighted norm above; no claim is made that its equivalence constants with unweighted Sobolev norms are uniform in \(N\).

For \(f\in L^2(\mu_g)\), \(P_sf\in H^2(M_E)\) for every \(s>0\), and
\[
G_w(t)^2+H_w(t)^2
\le e^{-2\lambda_*(t-s)}
\bigl(G_w(s)^2+H_w(s)^2\bigr),
\qquad t\ge s>0.
\tag{1.2}
\]
No estimate in terms of the initial \(L^2\)-norm alone at \(s=0\) is asserted.

This is a **conditional finite-strip reference semigroup proposition**. The analytic Bochner and conditional trace–Poincaré inputs remain hypotheses imported from their source certificates. This proposition is not a physical-coupling gap, a volume-uniform interacting estimate, a 3D transfer result, or a continuum Yang–Mills mass-gap theorem.

## 1. Geometry, generator, and exact ordered Hessian identity

The manifold \(M_E=\mathrm{SU}(2)^E\) is compact and connected for each fixed finite \(E\). Each factor has
\[
\operatorname{Ric}_e=\frac12g_e,\qquad
\kappa=\frac14,\qquad
\operatorname{diam}(M_e)=2\pi,\qquad
\lambda_1(-\Delta_e)=\frac34.
\]
The density is smooth and strictly positive. With \(V=\nabla S_g\), the generator has divergence form
\[
Lh=e^{-2S_g}\operatorname{div}(e^{2S_g}\nabla h),
\]
so \(L\) is symmetric and nonpositive on \(L^2(\mu_g)\).

For \(H_{IJ}=\nabla_I\nabla_Jf_t\), use
\[
[\nabla_I,\nabla_K]\omega_J=-R_{IKJ}{}^L\omega_L.
\]
Write \(A=\nabla^2S_g\), and define
\[
\mathcal B(H)=-\operatorname{Ric}\circ H-\!H\circ\operatorname{Ric}
+2\operatorname{Rm}*H,
\]
\[
\mathcal T_{IJ}{}^K=\nabla_{(I}\nabla_{J)}V^K,\qquad
\mathcal R_{IJ}=-V^KR_{(I|K|J)}{}^L\nabla_Lf_t.
\]
The exact ordered evolution is
\[
\boxed{
\begin{aligned}
\partial_tH_{IJ}
={}&\Delta^\nabla H_{IJ}+\mathcal B(H)_{IJ}
+2V^K\nabla_KH_{IJ}\\
&+2(A_I{}^KH_{KJ}+A_J{}^KH_{IK})\\
&+2\mathcal T_{IJ}{}^K\nabla_Kf_t
+2\mathcal R_{IJ}.
\end{aligned}}
\tag{1.3}
\]
The derivative order in \(\mathcal T\) is retained. The only commutation of the third derivative of \(f_t\) needed in deriving (1.3) is the displayed Codazzi commutator, retained in \(\mathcal R\). No three-slot symmetry of \(\nabla\operatorname{Hess}S_g\) is assumed. The product metric has parallel Ricci tensor, so no \(\nabla\operatorname{Ric}\) term occurs.

The weighted tensor integration-by-parts identity is
\[
\int_{M_E}\langle Q,(\Delta^\nabla+2\nabla_V)Q\rangle\,d\mu_g
=-\int_{M_E}|\nabla Q|^2\,d\mu_g.
\tag{1.4}
\]
The drift cancels the weighted-divergence correction of the rough Laplacian. The deterministic weights \(w_e\) are parallel for the product connection, so the identity applies componentwise in the one-output weighted pairing.

## 2. Explicit analytic hypotheses imported from source certificates

The proposition assumes the following two analytic inputs, with no strengthening beyond their source statements.

### (A1) Weighted gradient Bochner inequality

The global positive-majorant coefficient enclosure gives
\[
\|s_g'\|_\infty<0.000333528,\qquad
\|s_g''\|_\infty<1.94619\times10^{-7},\qquad
q_*:=\|s_g'\|_\infty+\|s_g''\|_\infty<0.000333722619.
\]
Each link is incident to at most two four-link faces, and
\(\|\nabla p_f\|_\infty\le1/2\). The weighted Hessian block row and column sums in the Bochner certificate are at most
\[
8\left(\frac{q_*}{4}\right)\frac65=\frac{12}{5}q_*<0.000800934286.
\]
With \(\operatorname{Ric}=1/2\), the pointwise weighted Bakry–Émery estimate gives
\[
\Gamma_{2,w}(h)\ge
\left(\frac12-\frac{24}{5}q_*\right)\Gamma_w(h)
=c_*\Gamma_w(h),\qquad c_*>0.4983981314.
\]
After integration against \(\mu_g\),
\[
\boxed{\frac{d}{dt}G_w(t)^2\le-2c_*G_w(t)^2.}
\tag{2.1}
\]

### (A2) Conditional one-link trace–Poincaré inequality

The conditional law obtained by freezing all links except \(U_e\) is the disintegration of the same \(\mu_g\):
\[
d\mu_g(U_e\mid U_{\ne e})
=Z_e^{-1}e^{2S_g(U_e,U_{\ne e})}\,dU_e.
\]
The sharper score bound follows from at most two incident faces and \(\|\nabla_ep_f\|\le1/2\):
\[
\|\nabla_eS_g\|_\infty\le B_*:=0.000333528.
\]
The conditional log-density oscillation is at most \(4\pi B_*\). Holley–Stroock comparison with the first nonzero Haar eigenvalue \(3/4\), followed by the exact conditional-mean correction, gives
\[
\|\nabla_eH_{ee}^{\mathrm{tr}}\|_2^2
\ge c_{\mathrm{tr},*}\|H_{ee}^{\mathrm{tr}}\|_2^2
-\ell_*\|\nabla_ef_t\|_2^2,
\tag{2.2}
\]
where
\[
H_{ee}^{\mathrm{tr}}=\frac{\Delta_ef_t}{3}g_e,\qquad
c_{\mathrm{tr},*}=\frac34e^{-4\pi B_*}
=0.746863150886429\ldots,
\]
\[
\ell_*=\frac{4c_{\mathrm{tr},*}}{3}B_*^2
=1.1077566544723305\times10^{-7}.
\tag{2.3}
\]
Multiplication by deterministic \(w_e\) and summation are permitted. This is a lower bound on a parallel component of the **full tensor Dirichlet form**; it is not a closed evolution equation for the trace sector.

## 3. Local geometric and coefficient hypotheses

All constants in this section are for the specified straight strip and isolated branch \(|g|\le10^{-3}\), not arbitrary plaquette complexes.

### (G1) Scalar derivative and ordered third-tensor bound

The coefficient-specific positive majorant and global character-degree tail certificate give, uniformly over the full plaquette range and all \(|g|\le10^{-3}\),
\[
\|s_g'\|_\infty<3.335278728\times10^{-4},\quad
\|s_g''\|_\infty<1.946186426\times10^{-7},\quad
\|s_g'''\|_\infty<1.743053086\times10^{-10}.
\]
For a face trace \(p_f\), an orthonormal left-invariant frame, and fixed ordered basis indices,
\[
|D_ip_f|\le\frac12,\quad
|D_iD_jp_f|\le\frac14,\quad
|D_iD_jD_kp_f|\le\frac18.
\]
The ordered covariant third derivative includes all three connection corrections:
\[
\begin{aligned}
(\nabla_{X_i}\operatorname{Hess}p_f)(X_j,X_k)
={}&D_iD_jD_kp_f-\Gamma_{jk}{}^\ell D_iD_\ell p_f\\
&-\Gamma_{ij}{}^\ell(\operatorname{Hess}p_f)_{\ell k}
-\Gamma_{ik}{}^\ell(\operatorname{Hess}p_f)_{j\ell},
\end{aligned}
\]
and is bounded componentwise by \(3/4\). This is an ordered component bound, not a trilinear operator norm for arbitrary linear combinations. The scalar chain rule gives
\[
T_g=\frac18\|s_g'''\|_\infty
+\frac34\|s_g''\|_\infty
+\frac34\|s_g'\|_\infty
<0.000250291891.
\tag{3.1}
\]

### (G2) Exact straight-strip incidence and third-tensor Schur bound

Each face has 12 link/Lie components and 144 ordered output pairs. Every original link belongs to at most two faces. Thus a fixed output pair is supported by at most two faces and has absolute row sum at most \(24T_g\); a fixed input component has absolute column sum at most \(288T_g\). The exact strip incidence gives \(3N+1\) original links.

The Schur estimate and one-output weight transfer are
\[
\|K_g\|_{2\to2}\le\sqrt{24\cdot288}\,T_g,
\qquad
\sqrt{w_e/w_k}\le\frac65
\quad\text{whenever the entry }(e,k)\text{ is nonzero}.
\]
Including the factor two in (1.3),
\[
\boxed{C_3\le2\frac65\sqrt{24\cdot288}\,T_g
<0.049941305.}
\tag{3.2}
\]

### (G3) Hessian-of-dressing block bound

For \(A=\nabla^2S_g\), the per-face component bound is
\[
h=\frac14\|s_g''\|_\infty+\frac12\|s_g'\|_\infty
<0.000166812592.
\]
Each link has at most six distinct neighboring links across at most two incident faces. The weighted first-index action has block row/column bound \(49.2h\); the unweighted right action on the second Hessian index has bound \(42h\). Hence
\[
\boxed{
\|2(AH+HA)\|_{w,2}
\le C_H\|H\|_{w,2},\qquad
C_H=2(49.2+42)h<0.030426617.
}
\tag{3.3}
\]

### (G4) SU(2) curvature damping and symmetrized Codazzi forcing

For each radius-two SU(2) factor, \(\kappa=1/4\) and \(\operatorname{Ric}=I/2\). The curvature action is \(-H_{ed}\) on mixed-link blocks and \(-\frac32H_{ee}^{\mathrm{TF}}\) on diagonal trace-free blocks. The pure diagonal trace has no direct curvature damping. If \(K_w\) denotes the combined mixed and diagonal trace-free sector and \(T_w\) the pure diagonal trace sector, then
\[
2\langle H,\mathcal B(H)\rangle_w\le-2K_w^2.
\tag{3.4}
\]
The symmetrized Codazzi contraction on each link is
\[
\mathcal R_e=\kappa\left[
(V_e\cdot v_e)I-\frac12(v_eV_e^\top+V_e v_e^\top)
\right].
\]
Its exact Frobenius factor is at most \(\sqrt2\). With the sharpened score bound \(B_*=0.000333528\) and the factor two in (1.3),
\[
C_{R,*}\le2\kappa\sqrt2B_*
=\frac{\sqrt2}{2}B_*<0.000235840.
\tag{3.5}
\]
Thus
\[
C_{G,*}=C_3+C_{R,*}<0.050177167.
\tag{3.6}
\]

## 4. Energy closure and rate

Decompose the Hessian orthogonally in the one-output weighted space:
\[
H_w^2=T_w^2+K_w^2,\qquad
T_w^2=\frac13\sum_e w_e\|\Delta_ef_t\|_2^2.
\]
Pair (1.3) with \(2H\). Use (1.4), (3.4), the trace Dirichlet lower bound (2.2), and the forcing estimates (3.2)–(3.6). This yields
\[
\frac{d}{dt}H_w^2
\le-2K_w^2-2c_{\mathrm{tr},*}T_w^2
+2\ell_* G_w^2+2C_HH_w^2+2C_{G,*}G_wH_w.
\tag{4.1}
\]
No invariance of the trace projection is used: the trace Poincaré inequality enters only as a lower bound on part of the full tensor Dirichlet form.

Since \(0<c_{\mathrm{tr},*}<1\),
\[
K_w^2+c_{\mathrm{tr},*}T_w^2
\ge c_{\mathrm{tr},*}(K_w^2+T_w^2)
=c_{\mathrm{tr},*}H_w^2.
\]
Adding (2.1) and (4.1) gives
\[
\frac{d}{dt}(G_w^2+H_w^2)
\le-2a_*G_w^2-2b_*H_w^2+2C_{G,*}G_wH_w,
\tag{4.2}
\]
where
\[
a_*=c_* -\ell_*>0.4983980206,\qquad
b_*=c_{\mathrm{tr},*}-C_H>0.7164364596.
\]
For \(x=(G_w,H_w)^\top\),
\[
E'(t)\le-2x^\top Qx,\qquad
Q_* =\begin{pmatrix}a_*&-C_{G,*}/2\\-C_{G,*}/2&b_*\end{pmatrix}.
\tag{4.3}
\]
With the conservative constants above,
\[
\lambda_{\min}(Q_*)
=\frac{a_*+b_*-\sqrt{(a_*-b_*)^2+C_{G,*}^2}}2
>0.4955484.
\tag{4.4}
\]
Gronwall gives (1.1) for smooth initial data. The margin is the least eigenvalue of the displayed symmetric matrix, not merely a determinant test.

## 5. Common measure, smooth core, and semigroup extension

The conditional link laws in (A2) are exactly the disintegrations of \(\mu_g\), while \(L\) is symmetric in that same measure. The weighted Bochner estimate, trace–Poincaré estimate, and pointwise Hessian coefficient bounds therefore combine in one \(L^2(\mu_g)\) space.

For each fixed finite \(E\), \(M_E\) is compact without boundary and the density \(e^{2S_g}\) is smooth and strictly positive. The nonpositive symmetric realization of
\[
L=e^{-2S_g}\operatorname{div}(e^{2S_g}\nabla)
\]
is the Friedrichs realization of
\[
\mathcal E(u,v)=\int\langle\nabla u,\nabla v\rangle\,d\mu_g,
\qquad D(\mathcal E)=H^1(M_E).
\]
The smooth functions are an operator core and elliptic regularity gives \(D(L)=H^2(M_E)\). The semigroup is strongly continuous, self-adjoint, contractive, and smoothing for positive time.

Thus the differential estimate, first proved for smooth data, passes by \(H^2\) approximation and graph-norm convergence to \(f\in H^2(M_E)\), proving (1.1). For \(f\in L^2(\mu_g)\), apply the \(H^2\) result to \(P_sf\) for each \(s>0\), giving (1.2). Constants lie in the kernel and are invisible to \(G_w,H_w\); no mean-zero condition is needed for this derivative-seminorm estimate.

For each fixed finite strip the centered inverse \(R=(-L)^{-1}Q\), \(Qh=h-\mu_g(h)\), exists by compactness, connectedness, and ellipticity. For \(q\in H^2(M_E)\),
\[
\left(\|\nabla Rq\|_{w,2}^2+
\|\nabla^2Rq\|_{w,2}^2\right)^{1/2}
\le\frac1{\lambda_*}
\left(\|\nabla q\|_{w,2}^2+
\|\nabla^2q\|_{w,2}^2\right)^{1/2}.
\tag{5.1}
\]
This is an \(H^2\)-source consequence only. It is not an H¹-source Hessian resolvent estimate and does not supply a strip-length-uniform scalar \(L^2\) gap.

## 6. Source dependencies and status

The proposition is conditional on the following source records:

1. [Weighted Bochner L4 foundational audit](../theorems/R3_IR_WEIGHTED_BOCHNER_L4_FOUNDATION_AUDIT_2026-11-02.md) — pointwise weighted Bakry–Émery identity and block-Schur structure; sharpened coefficient derived in §2 using the scalar enclosure.
2. [Conditional weighted trace–gradient Bochner block](../theorems/R3_IR_CONDITIONAL_WEIGHTED_TRACE_GRADIENT_BOCHNER_BLOCK_2026-11-10.md) — conditional-disintegration and Holley–Stroock method; sharpened constants are derived in the 2026-11-11 analytic-input audit.
3. [Ordered plaquette third-tensor certificate](../theorems/R3_IR_ORDERED_PLAQUETTE_THIRD_TENSOR_CERTIFICATE_2026-11-02.md) — original ordered-tensor source.
4. [SU(2) covariant Hessian/metric audit](../theorems/R3_IR_SU2_COVARIANT_HESSIAN_METRIC_AUDIT_2026-11-02.md) — radius-two metric and curvature source.
5. [Isolated dressing and projective-drift certificate](../theorems/R3_IR_CERTIFIED_DRESSING_AND_PROJECTIVE_DRIFT_2026-11-02.md) — isolated analytic branch.
6. [Local geometry and strip-incidence source audit](R3_IR_LOCAL_GEOMETRY_SOURCE_AND_INCIDENCE_AUDIT_2026-11-11.md) — ordered connection corrections, positive-majorant global tail, exact incidence, and recomputed local constants.
7. [Adversarial full-Hessian energy audit](R3_IR_ADVERSARIAL_FULL_HESSIAN_ENERGY_INEQUALITY_AUDIT_2026-11-11.md) — independent ordered-index, curvature, energy, and quadratic-form check.
8. [Common-measure and smooth-core audit](R3_IR_COMMON_MEASURE_SMOOTH_CORE_FINITE_STRIP_EXTENSION_2026-11-11.md) — measure compatibility, tensor integration by parts, and semigroup-domain extension.

**Established within the stated source chain:** local ordered component and incidence bounds, one-output Schur transfer, Hessian-dressing block estimate, SU(2) curvature/Codazzi coefficient, sharpened weighted Bochner inequality, sharpened conditional one-link trace–Poincaré inequality, common-measure compatibility, smooth-core extension, and positive \(2\times2\) energy margin. The scalar derivative enclosure remains a certified upstream dependency.

**Not established:** nonlinear interacting fixed point; pointwise interacting Hessian bound; volume-uniform residual response; physical-coupling (\(\lambda=1\)) spectral gap; all-orders or 3D transfer theorem; continuum limit or continuum Yang–Mills mass gap; PF-I16 or Penrose conclusion.

The provisional trace-to-\(K\) three-sector calculation remains paused and is not part of this proof. No theorem/claim ID is promoted. PR #106 remains draft; the main branch is unchanged.

## 7. Numerical constant ledger

| Quantity | Conservative bound / value |
|---|---:|
| Coupling range | \(|g|\le10^{-3}\) |
| (B_*=\|\nabla_eS_g\|_\infty) | \(<0.000333528\) |
| \(T_g\) | \(<0.000250291891\) |
| \(C_3\) | \(<0.049941305\) |
| \(h\) | \(<0.000166812592\) |
| \(C_H\) | \(<0.030426617\) |
| \(C_{R,*}\) | \(<0.000235840\) |
| \(C_{G,*}=C_3+C_{R,*}\) | \(<0.050177167\) |
| \(c_*) | \(>0.4983981314\) |
| \(c_{\mathrm{tr},*}\) | \(0.746863150886429\ldots\) |
| \(\ell_*\) | \(<1.108\times10^{-7}\) |
| \(a_*=c_* -\ell_*\) | \(>0.4983980206\) |
| \(b_*=c_{\mathrm{tr},*}-C_H\) | \(>0.7164364596\) |
| \(\lambda_{\min}(Q_*)\) | \(>0.4955484\) |


## 8. Sharpened analytic-input source audit

The coarse imported (49/576) envelope has been replaced by the coefficient-specific global derivative bounds. See [sharpened weighted Bochner and conditional trace–Poincaré audit](R3_IR_SHARP_WEIGHTED_BOCHNER_AND_TRACE_POINCARE_2026-11-11.md), its [arithmetic verifier](verify_R3_IR_sharp_weighted_analytic_inputs_2026-11-11.py), and [execution log](R3_IR_SHARP_WEIGHTED_ANALYTIC_INPUTS_2026-11-11.log). The resulting conservative rate is \(\lambda_*>0.4955484\). The scalar positive-majorant enclosure remains an explicit dependency; the two analytic inequalities themselves are now derived from it rather than imported with the coarse envelope.
