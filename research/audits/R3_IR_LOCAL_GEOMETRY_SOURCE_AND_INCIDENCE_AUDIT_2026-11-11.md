# R3-IR — Local geometric certificates and straight-strip incidence: source-level audit

**Date:** 2026-11-11  
**Status:** local coefficient and incidence obligations pass for the finite open straight SU(2) strip. This closes source verification of the local inputs used by the conditional full-Hessian estimate; it does not promote a theorem or claim ID.  
**Branch:** \`audit/r3-ir-h2-trace-to-k-2026-11-10\`; draft PR #106.  
**Scope:** original-link strip with face supports \(E_m=\{v_m,v_{m+1},t_m,b_m\}\), radius-two bi-invariant SU(2) factors, isolated plaquette dressing \(|g|\le10^{-3}\), and one-output weights \(w_e=(6/5)^{2d(e,\mathcal S)}\).

## 1. Source reconciliation and provenance

The following pre-existing source records are present byte-for-byte on the PR branch (their Git blob SHAs are listed below):

1. [Ordered plaquette third-tensor certificate](../theorems/R3_IR_ORDERED_PLAQUETTE_THIRD_TENSOR_CERTIFICATE_2026-11-02.md), blob \`6d51f56e4f82a7cacc81d798e0b54a7a295e3768\`.
2. [SU(2) covariant Hessian/metric audit](../theorems/R3_IR_SU2_COVARIANT_HESSIAN_METRIC_AUDIT_2026-11-02.md), blob \`6b6d0207835b1829f323f3068605fe55121e9911\`.
3. [Isolated dressing and projective-drift certificate](../theorems/R3_IR_CERTIFIED_DRESSING_AND_PROJECTIVE_DRIFT_2026-11-02.md), blob \`8468a5d2e79bdef53dec8d75c3da5a551fd4484d\`.
4. [Exact strip geometry record](../theorems/R3_IR_STRIP_GEOMETRY_THIRD_ORDER_SUMMABILITY_2026-11-02.md), blob \`92f687f517fbc659a2c29fca25b93738f15f2238\`.
5. [Weighted Bochner foundation](../theorems/R3_IR_WEIGHTED_BOCHNER_L4_FOUNDATION_AUDIT_2026-11-02.md), blob \`0af5e47667e38770d933c05a5dc4c32353747d8f\`.
6. [Conditional weighted trace–gradient block](../theorems/R3_IR_CONDITIONAL_WEIGHTED_TRACE_GRADIENT_BOCHNER_BLOCK_2026-11-10.md), blob \`77ff4da00ee2db8063c0390aa48fe53642d26bf9\`.

The archived ordered-tensor certificate's SHA-256 was independently checked against its Library manifest:
- certificate: \`c986ee9fcfb8c4b39a70ed42a0e4490550bb4696050742f11d02d938b9248774\`;
- original verifier: \`c4aa3f64513949bb3149af03746638ae78312855ef1c02a6a53d5ab4abe67cba\`;
- original verifier log: \`3721391fc4b42f80d62a86977d41544e6160eed9554397438babfc55bbe8c383\`.

The isolated-dressing source file's SHA-256 is \`c424bd24ed4bdc4a2bb4bea2dbd6c5a6aaf7b4c803ac1811ee8604af28805ed9\). The SU(2) metric report's SHA-256 is \`b787cf9bd080f5c5c96716e6e83355293e62d53d26762ff1ec366ea381baf480\`; its archived finite-difference verifier's SHA-256 is \`81ac4724e975e7672addd47bfea75ff37b6f02756dad3e33a6f53f0da40a8ebe\`, matching its manifest.

**Important distinction:** the separate directional \(C^3/C^4\) certificate obtains a much coarser scalar \(s_g'''\) bound from the full fixed-point ball. It is valid but is not the source of the tiny \(10^{-10}\) third-derivative bound used here. That sharper value comes from the six-step coefficient-specific enclosure in the ordered-tensor certificate, strengthened below by a positive majorant valid uniformly for all \(|g|\le10^{-3}\).

## 2. Uniform scalar derivative enclosure

The isolated fixed-point record uses
\[
\|u\|_A=\sum_{n\ge1}|u_n|\,2^n(n+1)^6,\qquad R=\frac1{25},
\]
and proves the fixed-point map has Lipschitz constant
\[
L\le |g|\left(\frac{129}{6}+\frac{2R}{768}\right)
\le 0.0215001041667<1.
\]

For the derivative audit, use the positive coefficient majorant \(F^\#\): take absolute values in the character recurrence and replace the negative quadratic eigenvalue-correction term by its positive absolute-value counterpart. Its ball and Lipschitz bounds are no larger than the displayed \(R,L\) bounds. If \(u(g)\) is the signed fixed point, then coefficientwise
\[
|u(g)|\le F^\#(|u(g)|).
\]
The positive monotone iterates from zero converge by contraction to the unique majorant fixed point \(v^\#\); hence \(|u(g)|\le v^\#\) coefficientwise for every \(|g|\le10^{-3}\).

Six exact-rational majorant iterations give a residual tail
\[
\|v^\#-v_6\|_A
\le\frac{\|F^\#(v_6)-v_6\|_A}{1-L}
<4.4259206260\times10^{-24}.
\]
This is a uniform-in-\(g\) enclosure, rather than a calculation only at the endpoint coupling.

For the second-kind SU(2) characters \(U_n\),
\[
U_n^{(k)}(x)=2^k k!\,C_{n-k}^{k+1}(x),
\]
and the normalized Gegenbauer zonal bound gives
\[
\sup_{x\in[-1,1]}|U_n^{(k)}(x)|\le U_n^{(k)}(1),\qquad 0\le k\le3.
\]
The endpoint coefficients are
\[
\begin{aligned}
U_n(1)&=n+1,\\
U_n'(1)&=\frac{n(n+1)(n+2)}3,\\
U_n''(1)&=\frac{(n-1)n(n+1)(n+2)(n+3)}{15},\\
U_n'''(1)&=\frac{(n-2)(n-1)n(n+1)(n+2)(n+3)(n+4)}{105}.
\end{aligned}
\]
Dividing by the coefficient weight \(2^n(n+1)^6\), the exact global maxima for \(k=0,1,2,3\) are respectively
\[
\frac1{64},\quad\frac1{64},\quad\frac2{729},\quad\frac{24}{15625}.
\]
For \(k=1\) the ratio decreases from \(n=1\); for \(k=2\) it decreases from \(n=2\); for \(k=3\), \(r_3(4)/r_3(3)=16384/15625>1\) and it decreases from \(n=4\). These tail statements follow from the exact ratio-difference polynomials; after the shifts \(n-1,n-2,n-4\), respectively, all coefficients are positive. Thus the derivative envelope is global in character degree, not a finite cutoff check.

The reproducible artifacts and source checksums are recorded in [the SHA-256 manifest](R3_IR_LOCAL_GEOMETRY_SOURCE_AUDIT_2026-11-11_SHA256.txt).

The resulting uniform bounds are
\[
\begin{aligned}
\|u_g'\|_\infty&<3.334166864\times10^{-4},\\
\|u_g''\|_\infty&<8.335000545\times10^{-8},\\
\|u_g'''\|_\infty&<1.666944558\times10^{-11}.
\end{aligned}
\]
Using \(s_g=\log(1+u_g)\) and the exact logarithmic derivative identities gives
\[
\begin{aligned}
\|s_g'\|_\infty&<3.335278728\times10^{-4},\\
\|s_g''\|_\infty&<1.946186426\times10^{-7},\\
\|s_g'''\|_\infty&<1.743053086\times10^{-10}.
\end{aligned}
\]
These are the inputs to the ordered third-tensor estimate.

## 3. Explicit ordered SU(2) plaquette geometry

Fix an orthonormal left-invariant basis \(X_i\) on each original link, with
\[
[X_i,X_j]=\epsilon_{ij}{}^kX_k,\qquad
\nabla_{X_i}X_j=\Gamma_{ij}{}^kX_k
=\frac12[X_i,X_j].
\]
For a four-link plaquette trace \(p_f=\operatorname{Re}(q_1^{\sigma_1}\cdots q_4^{\sigma_4})\), every ordered frame derivative inserts one Lie generator of operator norm \(1/2\). Inverse orientations relocate or conjugate the insertion and preserve its norm. Therefore, for basis directions supported on the face,
\[
|D_i p_f|\le\frac12,\qquad
|D_iD_jp_f|\le\frac14,\qquad
|D_iD_jD_kp_f|\le\frac18.
\]
The independent metric audit proves the stronger covariant Hessian block estimate \(\|\operatorname{Hess}_{ed}p_f\|_{\rm op}\le1/4\); the weaker component bound \(1/2\) is sufficient for the ordered third-tensor calculation.

Writing \(H_{jk}=\operatorname{Hess}p_f(X_j,X_k)\), the ordered covariant derivative is
\[
\begin{aligned}
(\nabla_{X_i}H)(X_j,X_k)
={}&D_iD_jD_kp_f-\Gamma_{jk}{}^\ell D_iD_\ell p_f\\
&-\Gamma_{ij}{}^\ell H_{\ell k}
-\Gamma_{ik}{}^\ell H_{j\ell}.
\end{aligned}
\]
For fixed basis indices, each nonzero SU(2) connection coefficient has magnitude \(1/2\) and at most one output Lie index. Thus
\[
|(\nabla_{X_i}\operatorname{Hess}p_f)(X_j,X_k)|
\le\frac18+\frac12\frac14+\frac12\frac12+\frac12\frac12
=\frac34.
\]
This is an **ordered component estimate**; no symmetry of the three covariant slots is assumed. It is not claimed as a basis-independent trilinear operator norm for arbitrary linear combinations. If any original-link index is absent from the face, the component vanishes because the product connection does not mix link factors.

The full ordered scalar chain rule is
\[
\begin{aligned}
(\nabla_X\operatorname{Hess}(s_g\circ p_f))(Y,Z)
={}&s_g'''(p_f)\,Xp_f\,Yp_f\,Zp_f\\
&+s_g''(p_f)\big[
\operatorname{Hess}p_f(X,Y)Zp_f
+\operatorname{Hess}p_f(X,Z)Yp_f\\
&\hspace{37mm}+\operatorname{Hess}p_f(Y,Z)Xp_f\big]\\
&+s_g'(p_f)(\nabla_X\operatorname{Hess}p_f)(Y,Z).
\end{aligned}
\]
Consequently each ordered face component is bounded by
\[
T_g=\frac18\|s_g'''\|_\infty
+\frac34\|s_g''\|_\infty
+\frac34\|s_g'\|_\infty
<0.000250291891.
\]

## 4. Exact strip incidence and weighted Schur transfer

For \(N\) open straight faces,
\[
E(f_m)=\{v_m,v_{m+1},t_m,b_m\},\qquad 1\le m\le N.
\]
The links \(t_m,b_m\) occur once; each interior \(v_m\) occurs in exactly two consecutive faces; endpoint \(v\)-links occur once. Hence there are \(3N+1\) original links and every link belongs to at most two faces. This is an exact all-\(N\) incidence argument, not an extrapolation from finite graph tests.

Flatten the third-tensor map as
\[
(K_gV)_{e,a;d,b}
=\sum_{k,c}(\nabla^3S_g)_{e,a;d,b;k,c}V_{k,c}.
\]
A face has 12 link/Lie components and 144 ordered output pairs. For fixed output pair \((e,a;d,b)\), at most two faces contain both output links, so the absolute row sum is at most \(24T_g\). For fixed input \((k,c)\), at most two faces contain its link, each with 144 ordered output pairs, so the absolute column sum is at most \(288T_g\). Schur therefore gives
\[
\|K_g\|_{2\to2}
\le\sqrt{24\cdot288}\,T_g
<0.020808877.
\]

For the one-output weight \(w_e=(6/5)^{2d(e,\mathcal S)}\), a nonzero entry requires the input link \(k\) and first output link \(e\) to lie in a common face. Their link-graph distance is at most one, so
\[
\sqrt{w_e/w_k}\le\frac65.
\]
The weighted similarity therefore costs at most \(6/5\) in both row and column sums. Including the factor two in the drift Hessian evolution gives
\[
C_3\le2\frac65\sqrt{24\cdot288}\,T_g
<0.049941305.
\]
The original ordered-tensor source correctly states that its raw Schur estimate is unweighted; the \(6/5\) transfer is the additional one-output bookkeeping needed here.

## 5. Hessian-of-dressing and curvature constants

For \(A=\nabla^2S_g\), the per-face chain rule and conservative component bounds give
\[
h=\frac14\|s_g''\|_\infty+\frac12\|s_g'\|_\infty
<0.000166812592.
\]
Each link has at most six distinct neighboring links across its at most two incident faces. Every \(3\times3\) link block has Frobenius norm at most \(6h\); the unweighted block row/column sums are at most \(42h\). For the weighted first-index action, the diagonal block has weight ratio one and each of at most six off-diagonal blocks costs at most \(6/5\), giving \(49.2h\). The right action on the second Hessian index is unweighted and costs \(42h\). Therefore
\[
\|2(AH+HA)\|_{w,2}
\le2(49.2+42)h\,\|H\|_{w,2},
\qquad C_H<0.030426617.
\]
This deliberately retains the looser \(|\operatorname{Hess}p_f|\le1/2\) component envelope; the independent metric audit's \(1/4\) operator bound could only improve it.

For the radius-two SU(2) metric, the analytic quaternion calculation gives sectional curvature \(\kappa=1/4\) and \(\operatorname{Ric}=\frac12g\). The curvature action is \(-H_{ed}\) on mixed-link blocks and \(-\frac32H_{ee}^{\rm TF}\) on diagonal trace-free blocks; the pure diagonal trace has no direct curvature damping.

For the Codazzi forcing, symmetry of the Hessian output requires the symmetrized contraction
\[
\mathcal R_e
=\kappa\left[(V_e\cdot v_e)I
-\frac12(v_eV_e^\top+V_ev_e^\top)\right].
\]
Its exact Frobenius factor is
\[
\frac{\|\mathcal R_e\|_F^2}
{\kappa^2|V_e|^2|v_e|^2}
=\frac12+\frac32\frac{(V_e\cdot v_e)^2}{|V_e|^2|v_e|^2}
\le2.
\]
With the conservative local score bound \(B=49/576\) and the factor two in the evolution,
\[
C_R\le2\kappa\sqrt2B
=\frac{49\sqrt2}{1152}
<0.060153182.
\]

The archived finite-difference metric verifier was independently run: 90 random four-link configurations across all 16 orientation patterns gave maximum gradient norm \(0.499956841\), maximum Hessian-block operator norm \(0.250000013\), and maximum diagonal Hessian residual \(6.3\times10^{-8}\). These are corroboration only; the analytic quaternion argument is the proof input.

## 6. Recomputed combined margin

Using the same common measure and one-output norm as the previous energy audits,
\[
\begin{aligned}
c_{\rm tr}&=\frac34e^{-49\pi/144}
=0.2575101249909\ldots,\\
\ell&=\frac{4c_{\rm tr}}3\left(\frac{49}{576}\right)^2
=0.00248473592666\ldots,\\
a&=\frac{11}{120}-\ell
=0.0891819307400\ldots,\\
b&=c_{\rm tr}-C_H>0.2270835083,\\
C_G&=C_3+C_R<0.1100944859.
\end{aligned}
\]
The least eigenvalue of
\[
Q=\begin{pmatrix}a&-C_G/2\\-C_G/2&b\end{pmatrix}
\]
is \(>0.0699034147\). Thus the conservative statement remains
\[
\lambda_{\min}(Q)>0.0699034.
\]
This is consistent with, and slightly sharpens, the earlier rounded constants.

## 7. Audit verdict and boundaries

**Passed for the stated finite straight-strip model:**

1. The ordered third-covariant plaquette component bound, including all three SU(2) connection corrections.
2. The scalar third-derivative enclosure, now with an explicit positive majorant uniform for every \(|g|\le10^{-3}\) and a global character-degree tail bound.
3. The exact four-link face incidence and the row/column overlap counts \(24,288\).
4. The one-output \(6/5\) transfer for the third-tensor Schur map.
5. The \(A=\nabla^2S_g\) block row/column counts and weighted left/unweighted right action.
6. The radius-two SU(2) metric normalization, curvature decomposition, and symmetrized Codazzi factor.

The original ordered-tensor verifier's finite-degree assertion is not used as a proof of an infinite tail here; the global ratio argument above supplies that missing tail justification. Its source arithmetic log agrees with the independent positive-majorant recomputation to the displayed precision.

**Still conditional / not claimed:**

- The weighted Bochner and conditional one-link Poincaré inequalities are imported from their named analytic certificates and retain their exact finite-strip hypotheses.
- The common-measure and smooth-core/semigroup extension is covered by the separate 2026-11-11 audit.
- No nonlinear interacting fixed point, pointwise interacting Hessian bound, volume-uniform residual response, physical-coupling gap, 3D transfer, or continuum Yang–Mills mass gap is proved.
- This audit is not a PF-I16 or Penrose result and does not use the provisional three-sector calculation.

**Decision:** the remaining local geometric and strip-incidence source obligation is closed for the specified finite open straight SU(2) strip. The full-Hessian estimate remains a *conditional finite-strip reference semigroup proposition*. Keep PR #106 draft and do not promote a theorem/claim ID.
