# R3-IR — Sharpened weighted Bochner and conditional trace–Poincaré inputs

**Date:** 2026-11-11  
**Status:** source-derived strengthening for the finite open straight SU(2) strip; arithmetic verifier supplied.  
**Scope:** same isolated dressing branch, full plaquette range, \(|g|\le10^{-3}\), radius-two product metric, one-output weights.  
**Dependency:** the uniform coefficient-specific scalar derivative enclosure in the 2026-11-11 local-geometry audit. This note replaces the coarse \(49/576\) score/derivative envelope in the two imported analytic inputs; it does not replace the underlying isolated-dressing proof.

## 1. Sharper scalar data and local score

The positive-majorant/global-character-tail certificate gives, uniformly for all plaquette arguments and \(|g|\le10^{-3}\),
\[
S_1:=\|s_g'\|_\infty<0.000333528,\qquad
S_2:=\|s_g''\|_\infty<1.94619\times10^{-7}.
\]
Use the conservative rational ceilings
\[
\bar S_1=\frac{333528}{10^9},\qquad
\bar S_2=\frac{194619}{10^{12}}.
\]
The exact straight-strip incidence says every link belongs to at most two faces, and the ordered plaquette gradient bound is \(\|\nabla_ep_f\|\le1/2\). Therefore
\[
\boxed{
B_*:=\|\nabla_eS_g\|_\infty
\le 2\cdot\frac12 S_1
\le\bar S_1=0.000333528.
}
\tag{1.1}
\]
This improves the previous \(B=49/576\) by a factor exceeding 255. The same coefficient enclosure is uniform in \(g\), so no endpoint-only coupling assumption is introduced.

For the per-face Hessian of \(s_g\circ p_f\), use
\[
\|\operatorname{Hess}p_f\|_{\rm op}\le\frac14,\qquad
\|dp_f\|\le\frac12.
\]
Then
\[
\|\operatorname{Hess}(s_g\circ p_f)\|_{\rm op}
\le\frac14(S_1+S_2).
\]
Put
\[
q_*:=\bar S_1+\bar S_2=0.000333722619.
\tag{1.2}
\]

## 2. Independently sharpened weighted Bochner inequality

The weighted Bakry–Émery calculation in the foundational Bochner audit is pointwise and uses only:
- \(\operatorname{Ric}=1/2\) on each radius-two SU(2) factor;
- parallel, configuration-independent weights \(w_e=(6/5)^{2d(e,\mathcal S)}\);
- at most two faces incident to each link;
- a per-face Hessian operator bound \(q_*/4\);
- the same weighted block row and column Schur estimate.

The row/column bound previously written as \(8(q_g/4)(6/5)\) is now
\[
8\frac{q_*}{4}\frac65=\frac{12}{5}q_*.
\]
The weighted Bakry–Émery curvature loss is twice that Schur bound. Hence
\[
\boxed{
\Gamma_{2,w}(h)\ge c_*\,\Gamma_w(h),\qquad
c_*=\frac12-\frac{24}{5}q_*
>0.4983981314.
}
\tag{2.1}
\]
The semigroup gradient energy consequently obeys
\[
\boxed{
\frac{d}{dt}G_w(t)^2\le-2c_*G_w(t)^2.
}
\tag{2.2}
\]
This is the same weighted Bochner argument as the imported certificate, with a sharper certified coefficient envelope. No change of measure, weight convention, or geometry is made.

## 3. Independently sharpened conditional one-link Poincaré inequality

Freeze all links except \(U_e\). The conditional law remains the exact disintegration of
\[
d\mu_g=Z_g^{-1}e^{2S_g}\,d\mathrm{Haar}.
\]
The factor SU(2) has diameter \(2\pi\). By (1.1),
\[
\operatorname{osc}_{U_e}(2S_g)
\le 2(2\pi)B_*=4\pi B_*.
\]
Holley–Stroock comparison with the first nonzero Haar eigenvalue \(3/4\) therefore gives
\[
\boxed{
c_{{\rm tr},*}
=\frac34e^{-4\pi B_*}
\ge\frac34e^{-4\pi\bar S_1}
>0.7468631508.
}
\tag{3.1}
\]
The conditional mean correction is unchanged in form. Exact conditional integration by parts gives
\[
m_e=\mathbb E[\Delta_ef_t\mid U_{\ne e}]
=-2\mathbb E[\langle\nabla_ef_t,\nabla_eS_g\rangle\mid U_{\ne e}],
\]
so Jensen and (1.1) yield
\[
\|m_e\|_2^2\le4B_*^2\|\nabla_ef_t\|_2^2.
\]
Thus
\[
\boxed{
\|\nabla_eH_{ee}^{\rm tr}\|_2^2
\ge c_{{\rm tr},*}\|H_{ee}^{\rm tr}\|_2^2
-\ell_*\|\nabla_ef_t\|_2^2,\quad
\ell_*=\frac{4c_{{\rm tr},*}B_*^2}{3}
<1.108\times10^{-7}.
}
\tag{3.2}
\]
The estimate still holds after multiplication by deterministic nonnegative \(w_e\) and summation. It remains a lower bound on the parallel trace component of the full tensor Dirichlet form, not an autonomous trace evolution.

## 4. Updated full-Hessian energy margin

The local ordered third-tensor and Hessian-dressing bounds do not worsen:
\[
C_3<0.049941327,\qquad C_H<0.030426692.
\]
The symmetrized SU(2) Codazzi term uses the same exact Frobenius factor \(\sqrt2\), but its score factor is now \(B_*\):
\[
\boxed{
C_{R,*}\le2\kappa\sqrt2 B_*
=\frac{\sqrt2}{2}B_*
<0.000235840.
}
\tag{4.1}
\]
Set
\[
C_{G,*}=C_3+C_{R,*}<0.050177167.
\]
The full-Hessian energy calculation is otherwise unchanged. With
\[
a_*=c_*-\ell_*,\qquad
b_*=c_{{\rm tr},*}-C_H,
\]
the symmetric energy matrix is
\[
Q_*=\begin{pmatrix}a_*&-C_{G,*}/2\\-C_{G,*}/2&b_*\end{pmatrix}.
\]
Using the conservative rational ceilings above and \(T_g<0.000250292\), \(h<0.000166813\), the independent verifier obtains
\[
a_*>0.4983980206,\qquad
b_*>0.7164364596,\qquad
\boxed{\lambda_{\min}(Q_*)>0.4955484.}
\tag{4.2}
\]
Consequently the conditional finite-strip full-Hessian reference semigroup estimate improves to
\[
G_w(t)^2+H_w(t)^2
\le e^{-2\lambda_*t}(G_w(0)^2+H_w(0)^2),
\qquad \lambda_*>0.4955484.
\]
The common-measure, smooth-core, and positive-time smoothing arguments are unchanged.

## 5. Proof status and limitations

**What is strengthened:** the two formerly imported analytic inequalities are now rederived with the coefficient-specific global derivative enclosure already proved in the local-geometry source audit. The score bound, weighted Bakry–Émery loss, conditional oscillation, conditional-mean leakage, and Codazzi forcing all use the same sharper \(S_1\) bound.

**What remains a dependency:** the scalar derivative enclosure is itself a certified consequence of the isolated plaquette fixed-point positive majorant and global character tail. The present note does not replace that source proof. The weighted block-Schur geometry and Holley–Stroock comparison are standard analytic steps, with their constants checked by the accompanying verifier.

**No broader claim:** the result remains for the isolated-dressing reference measure on each finite open straight strip, uniformly in strip length under the exact incidence and uniform local coefficient hypotheses. It is not a nonlinear interacting fixed point, pointwise interacting Hessian bound, physical-coupling gap, volume-uniform residual theorem, 3D transfer, or continuum Yang–Mills mass gap.

## 6. Three-sector route decision

The provisional trace-to-\(K\) three-sector calculation is **not the appropriate next step** for the present finite-strip reference-semigroup objective. Its role was to repair the undamped pure diagonal trace sector while the score and conditional Poincaré bounds were coarse. The sharpened conditional Poincaré input now gives nearly the Haar trace coercivity \(3/4\), while the full-Hessian route already controls the mixed/trace-free sector through product curvature. The full-Hessian \(2\times2\) energy form has a large positive margin \(>0.4955484\), so a separate \(3\times3\) closure adds work without improving the current theorem target.

Retain the three-sector computation as a dormant independent cross-check only. Do not delete its source or promote its provisional constants. Reopen it only if a later target requires a genuinely different norm, non-product geometry, loss of the exact two-face incidence, a larger coupling regime, or an interacting estimate for which the current one-output full-Hessian argument does not apply.
