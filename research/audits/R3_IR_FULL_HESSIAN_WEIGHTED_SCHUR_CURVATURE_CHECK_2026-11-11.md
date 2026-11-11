# R3-IR — Full-Hessian ordered tensor, weighted Schur, and SU(2) curvature audit

**Date:** 2026-11-11  
**Status:** independent index/support and norm-arithmetic audit; conditional finite-strip candidate only.  
**Target:** draft PR #106, branch audit/r3-ir-h2-trace-to-k-2026-11-10.  
**Scope:** finite straight open SU(2) strip with radius-two bi-invariant metric, \(|g|\le 10^{-3}\). No transfer to PF-I16, Penrose, a 3D regulator, or continuum Yang–Mills is asserted.

## 1. Ordered third-dressing tensor

The archived source R3_IR_ORDERED_PLAQUETTE_THIRD_TENSOR_CERTIFICATE_2026-11-02.md defines the ordered tensor by
\[
(\nabla_X\operatorname{Hess}S_g)(Y,Z),
\]
without assuming symmetry in all three slots. For one face \(f\), the exact ordered scalar chain rule is
\[
\begin{aligned}
(\nabla_X\operatorname{Hess}(s_g\circ p_f))(Y,Z)
={}&s_g'''(p_f)Xp_f\,Yp_f\,Zp_f\\
&+s_g''(p_f)\big[
\operatorname{Hess}p_f(X,Y)Zp_f
+\operatorname{Hess}p_f(X,Z)Yp_f\\
&\hspace{37mm}
+\operatorname{Hess}p_f(Y,Z)Xp_f\big]\\
&+s_g'(p_f)(\nabla_X\operatorname{Hess}p_f)(Y,Z).
\end{aligned}
\]

For orthonormal left-invariant frame basis entries whose links lie in that face, the archived geometric bounds are
\[
|dp_f|\le\tfrac12,\quad
|\operatorname{Hess}p_f|\le\tfrac12,\quad
|\nabla\operatorname{Hess}p_f|\le\tfrac34.
\]
The last estimate includes connection terms and is an ordered component estimate. In the left-invariant frame,
\[
\nabla_{X_i}X_j=\tfrac12[X_i,X_j],\qquad
|\Gamma(X_i,X_j)|\le\tfrac12.
\]
For basis directions, the ordered third frame derivative contributes at most \(1/8\); differentiating the Hessian connection correction contributes at most another \(1/8\); the two covariant-slot connection corrections contribute at most \(1/4\) each. Their sum is \(3/4\). This explains why a directional \(C^3\) estimate alone would not suffice, while the ordered component estimate does.

The archived scalar bounds
\[
\|s_g'\|_\infty<0.000333528,\quad
\|s_g''\|_\infty<1.94619\cdot10^{-7},\quad
\|s_g'''\|_\infty<1.744\cdot10^{-10}
\]
therefore give the per-face entry bound
\[
T_g=\tfrac18\|s_g'''\|_\infty+
\tfrac34\|s_g''\|_\infty+
\tfrac34\|s_g'\|_\infty
<0.000250292.
\]

### Ordered matrix-Schur incidence

Flatten the input as \((g,c)\), with \(4\cdot3=12\) possible link/Lie components per face, and the output as \((e,a;d,b)\), with ordered pairs of Lie components.

- For a fixed output pair \((e,a;d,b)\), at most two faces contain both output links. Each such face has 12 input components. Hence the absolute row sum is at most \(2\cdot12T_g=24T_g\).
- For a fixed input component \((g,c)\), at most two faces contain its link. Each face has \(12^2=144\) ordered output components. Hence the absolute column sum is at most \(2\cdot144T_g=288T_g\).

The matrix Schur test gives
\[
\|K_g\|_{\ell^2(\mathrm{gradient})\to\ell^2(\mathrm{Hessian})}
\le\sqrt{24\cdot288}\,T_g
<0.020808887<0.02081.
\]
This is the unweighted link-index operator estimate, pointwise in the configuration.

For the one-output weight \(w_e=(6/5)^{2d(e,\mathcal S)}\), a nonzero entry has \(e\) and \(g\) in one common face, so \(|d(e,\mathcal S)-d(g,\mathcal S)|\le1\). Therefore
\[
\sqrt{w_e/w_g}\le6/5.
\]
Conjugating the component matrix by the output and input weights multiplies each nonzero entry by at most \(6/5\). Thus
\[
C_3\le2\cdot\tfrac65\sqrt{24\cdot288}\,T_g
<0.049941327.
\]
The factor \(2\) is the drift coefficient in the generator. This verifies the required ordered-index transfer, conditional on the archived local component bounds and the stated original-link face incidence.

The source certificate’s SHA-256 manifest records:
- certificate: c986ee9fcfb8c4b39a70ed42a0e4490550bb4696050742f11d02d938b9248774;
- verifier: c4aa3f64513949bb3149af03746638ae78312855ef1c02a6a53d5ab4abe67cba;
- verifier log: 3721391fc4b42f80d62a86977d41544e6160eed9554397438babfc55bbe8c383.

The verifier’s stated role is to reconstruct the six scalar fixed-point iterations, certify the scalar remainder and third derivative, and check the graph-overlap Schur coefficients. The quaternion insertion and connection estimates are analytic inputs, not numerical consequences of that script.

## 2. Hessian-of-dressing block incidence

Write
\[
S_g=\sum_f s_g(p_f),\qquad A=\nabla^2S_g.
\]
For a face contribution,
\[
\nabla^2(s_g\circ p_f)
=s_g''(p_f)\,dp_f\otimes dp_f+s_g'(p_f)\nabla^2p_f.
\]
For orthonormal link-frame components, the per-face entry is bounded by
\[
\tfrac14\|s_g''\|_\infty+\tfrac12\|s_g'\|_\infty=:h
<0.00016681265475.
\]

An \(A_{ed}\) block vanishes unless \(e,d\) occur in a common face. Each link belongs to at most two faces; each such face contains only three other links. Hence each block row and column has at most six off-diagonal neighboring link blocks, plus the diagonal block. A uniform component envelope \(2h\) is valid: the diagonal block may receive two face contributions, and using \(2h\) for every neighboring block is conservative.

Each \(3\times3\) block therefore has Frobenius/operator bound \(6h\). The unweighted block row and column sums are at most
\[
7(6h)=42h.
\]
For neighboring links, \(\sqrt{w_e/w_d}\le6/5\); the diagonal ratio is one. The weighted similarity row and column sums are at most
\[
6h\left(1+6\cdot\tfrac65\right)=49.2h.
\]
Consequently,
\[
\|A\|_{\rm op}\le42h,\qquad
\|W^{1/2}AW^{-1/2}\|_{\rm op}\le49.2h.
\]

In the one-output Hessian norm, left multiplication sees the weighted bound and right multiplication sees the unweighted bound. Thus
\[
\|2(AH+HA)\|_{w,\mathrm{out}}
\le2(49.2+42)h\|H\|_{w,\mathrm{out}},
\]
and
\[
C_H=182.4h<0.0304266282264.
\]
The incidence and Schur arithmetic are verified under the stated straight-strip geometry and local component bounds. The estimate is not a statement about a general plaquette complex with higher link-face incidence.

## 3. Exact symmetrized SU(2) curvature contraction

Use the radius-two bi-invariant metric and the convention
\[
R(X,Y)Z=\kappa(\langle Z,Y\rangle X-\langle Z,X\rangle Y),
\qquad \kappa=\tfrac14.
\]
Then \(\operatorname{Ric}=2\kappa I=\tfrac12I\) on each three-dimensional link factor. The rough-Laplacian Hessian commutator in the heat evolution has the damping form
\[
\mathcal B(H)=-\operatorname{Ric}\circ H-H\circ\operatorname{Ric}
+2\operatorname{Rm}*H.
\]
It acts on distinct-link blocks as \(-H_{ed}\), and on a diagonal block as
\[
\mathcal B(H)_{ee}=-\tfrac32H_{ee}^{\rm TF}.
\]
Therefore
\[
\langle H,\mathcal B(H)\rangle
=-\sum_{e\ne d}\|H_{ed}\|_F^2
-\tfrac32\sum_e\|H_{ee}^{\rm TF}\|_F^2.
\]
The pure diagonal trace sector has zero direct curvature damping; its separate conditional one-link Poincaré estimate remains necessary.

For the drift-ordering commutator, put \(V_e=\nabla_eS_g\) and \(v_e=\nabla_ef_t\). The unsymmetrized constant-curvature contraction is, up to the fixed convention sign,
\[
\kappa\big((V_e\cdot v_e)I-v_eV_e^\top\big).
\]
Since the Hessian is symmetric, the relevant output is its symmetric part:
\[
\mathcal R_e
=\kappa\left[(V_e\cdot v_e)I
-\tfrac12(v_eV_e^\top+V_ev_e^\top)\right].
\]

The exact Frobenius norm of this bilinear map is sharper than the triangle bound used in the first candidate audit. For unit \(V,v\), let \(c=V\cdot v\) and rotate coordinates so \(V=(1,0,0)\), \(v=(c,\sqrt{1-c^2},0)\). Then
\[
\left\|(V\cdot v)I-\tfrac12(vV^\top+Vv^\top)\right\|_F^2
=\tfrac12+\tfrac32c^2\le2.
\]
Equality occurs for parallel \(V,v\). Hence the exact bilinear Frobenius operator constant is \(\sqrt2\), not \(\sqrt3+1\):
\[
\|\mathcal R_e\|_F\le\kappa\sqrt2\,|V_e|\,|v_e|.
\]
With the archived local bound \(|V_e|\le B=49/576\) and the factor \(2\) from the drift,
\[
C_R\le2\kappa\sqrt2 B
=\frac{49\sqrt2}{1152}
<0.060153181039.
\]
This is a bound on the symmetrized curvature-ordering forcing in the one-output norm. The unsymmetrized expression must not be inserted as an equality in the symmetric-Hessian energy.

## 4. Updated conditional energy margin

Using the same measure, metric, and one-output norm as the conditional trace/gradient record, take
\[
c_{\rm tr}=0.2575101249909138\ldots,\quad
\ell=0.00248473592666\ldots,\quad
c=\tfrac{11}{120}.
\]
The verified candidate constants are
\[
a=c-\ell=0.0891819307400\ldots,
\]
\[
b=c_{\rm tr}-C_H>0.2270834967645,
\]
\[
C_G=C_3+C_R<0.110094507715.
\]
The positivity threshold is
\[
2\sqrt{ab}>0.2846172495,
\]
so the updated candidate cross coefficient is below threshold. The smaller eigenvalue of the corresponding \(2\times2\) form is bounded below by approximately
\[
\lambda_{\rm cand}>0.0699034.
\]

This improves the previous candidate \(\lambda\approx0.05017\) by using the exact norm of the symmetrized SU(2) curvature contraction and the unrounded third-tensor Schur value. It remains a **conditional diagnostic**, not a theorem promotion. It depends on the common-\(\mu_g\) trace and gradient inequalities, the local dressing assumptions, and the ordered tensor geometric certificate. Smooth-core and semigroup/resolvent extension hypotheses still need to be stated in the final theorem.

## 5. Audit verdict

1. Ordered third-tensor row/column incidence: **verified from the four-link/two-face geometry**.
2. One-output weight transfer for the third tensor: **verified**, with factor \(6/5\).
3. Hessian-of-dressing \(A\) block support and weighted Schur sums: **verified conditionally on the local component envelope**.
4. SU(2) Hessian curvature damping: **verified under the stated Riemann convention**; trace-free/mixed damping does not control the pure trace sector.
5. Symmetrized Codazzi curvature forcing: **exact Frobenius constant \(\sqrt2\)**, improving the previous conservative \(\sqrt3+1\).
6. Combined positive energy margin: **recomputed and still conditional**.

No theorem/claim status is promoted. The provisional three-sector trace-to-\(K\) calculation remains paused. This audit concerns only the finite-strip reference dressed semigroup; it does not establish the nonlinear interacting fixed point, a volume-uniform residual expansion, a physical-coupling gap, or a continuum mass gap.
