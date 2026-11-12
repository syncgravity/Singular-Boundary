# PF-I16 — Refined isolated-rotor Hessian and shared-link residual derivatives

**Date:** 2026-11-10  
**Status:** conditional analytic estimate. The radial SU(2) calculation and a working four-factor left/right-trivialized mixed-Hessian derivation are recorded. The pulled-back blocks, curvature and derivative-flow consequences remain conditional on the inherited isolated-rotor first-derivative estimate and the stated group-product conventions. A standalone sign/trivialization/regularization audit remains open. This record supersedes the earlier coarse rotor Hessian constants for downstream PF-I16 estimates and closes no canonical proof gate.

## 1. Scope and assumptions

Work on the authentic accepted-rhombus PF-I16 complex and its original-link product group \(\mathrm{SU}(2)^E\). For a face \(f\), allocate the electric coefficient
\[
A_f=\sum_{e\in\partial f}\frac{a_e}{d_e},\qquad
\beta_f=\frac{|b_f|}{A_f},
\]
where \(d_e\) is the number of accepted faces incident to link \(e\). Use the universal inventory
\[
d_e\le8,\qquad a_e\ge a_0>0,\qquad |b_f|\le b_0,\qquad A_f\ge a_0/2.
\]
The last inequality follows from the four boundary links and \(d_e\le8\).

The isolated-face ground-state logarithm is radial on the radius-two \(S^3\simeq\mathrm{SU}(2)\). The previously inherited first-derivative estimate \(\|s_f'\|_\infty\le\beta_f\) is now contradicted by the linear response of the radial equation: \(\|s_\beta'\|_\infty/\beta\to4/3\) as \(\beta\downarrow0\). See [the 2026-11-11 perturbative obstruction](../audits/PF_I16_ISOLATED_ROTOR_FIRST_DERIVATIVE_OBSTRUCTION_2026_11_11.md). Accordingly, every Hessian, residual-derivative and derivative-flow constant below that uses \(\|s_f'\|_\infty\le\beta_f\) is provisional and must be recomputed from a corrected bound. No commuting-link approximation is used.

## 2. Exact weighted-mean cancellation in the radial equation

Suppress \(f\), take \(\beta\ge0\) (the opposite sign is reduced by \(\theta\mapsto\pi-\theta\)), and put \(q=s'\). The radius-two radial equation is
\[
q'+2\cot\theta\,q=-4(q^2+\beta\cos\theta+\lambda).
\]
Multiplying by \(\sin^2\theta\), integrating from \(0\) to \(\pi\), and using regularity at both endpoints gives
\[
\lambda=-\frac{\int_0^\pi\sin^2\theta\,q(\theta)^2\,d\theta}
{\int_0^\pi\sin^2\theta\,d\theta}.
\]
Thus \(-\beta^2\le\lambda\le0\). With \(h=q^2+\lambda\), one has
\[
\int_0^\pi\sin^2\theta\,h(\theta)\,d\theta=0,\qquad
\|h\|_\infty\le\beta^2.
\]

Set
\[
J(\theta)=\int_0^\theta\sin^2u\,h(u)\,du.
\]
Then \(J(\pi)=0\), and the nearer-endpoint representation yields
\[
\frac{|\cot\theta|}{\sin^2\theta}|J(\theta)|
\le\frac{\beta^2}{3}.
\]
For example, on \(0<\theta\le\pi/2\), this follows from
\[
\int_0^\theta\sin^2u\,du
\le\frac{\sin^3\theta}{3\cos\theta};
\]
the other half follows by integrating from \(\pi\).

The integrated radial equation and its derivative are
\[
q=-\frac43\beta\sin\theta-\frac{4J(\theta)}{\sin^2\theta},
\]
\[
q'=-\frac43\beta\cos\theta-4h(\theta)
+8\frac{\cot\theta}{\sin^2\theta}J(\theta).
\]
Therefore
\[
\boxed{\|s''\|_\infty\le\frac43\beta+\frac{20}{3}\beta^2.}
\]
The tangential Hessian eigenvalue for the radius-two sphere is
\[
\frac14\cot\theta\,q
=-\frac13\beta\cos\theta-\frac{\cot\theta}{\sin^2\theta}J(\theta),
\]
whose absolute value is at most \(\beta/3+\beta^2/3\). Hence
\[
\boxed{\|\nabla^2s\|_{\mathrm{op}}
\le\frac43\beta+\frac{20}{3}\beta^2.}
\]
This improves the earlier coarse \(12\beta^2+24\beta\) estimate under the same first-derivative hypothesis and radius-two normalization.

## 3. Conditional pullback Hessian blocks

For the oriented face holonomy
\[
H_f=U_{e_1}^{\epsilon_1}U_{e_2}^{\epsilon_2}
U_{e_3}^{\epsilon_3}U_{e_4}^{\epsilon_4},
\qquad \epsilon_j\in\{\pm1\},
\]
the covariant chain rule is
\[
\nabla^2(s_f\circ H_f)(X,Y)
=\nabla^2s_f(dH_fX,dH_fY)
+\langle\nabla s_f,\nabla dH_f(X,Y)\rangle.
\]
For the four-factor word write \(x_i=U_i^{\epsilon_i}\), \(\dot U_i=U_i\xi_i\), and \(\dot x_i=x_iX_i\). Then
\[
X_i=\xi_i\quad(\epsilon_i=+1),\qquad
X_i=-\operatorname{Ad}_{U_i}\xi_i\quad(\epsilon_i=-1),
\]
or \(X_i=\epsilon_i\operatorname{Ad}_{U_i^{(1-\epsilon_i)/2}}\xi_i\); this is norm preserving. With \(T_i=x_{i+1}\cdots x_4\), \(T_4=1\), and \(\eta_i=\operatorname{Ad}_{T_i^{-1}}X_i\), one has \(H^{-1}\dot H=\sum_i\eta_i\). For distinct factors,
\[
D_i\eta_j=0\ (i<j),\qquad D_i\eta_j=-[\eta_i,\eta_j]\ (i>j).
\]
Using \((\nabla_{\dot H}W)_{\rm left}=D_{\dot H}w+\frac12[\eta,w]\), the working mixed covariant derivative is
\[
(\nabla dH)(X_i,Y_j)=
\begin{cases}
\frac12[\eta_i(X_i),\eta_j(Y_j)],&i<j,\\
-\frac12[\eta_i(X_i),\eta_j(Y_j)],&i>j,\\
0,&i=j.
\end{cases}
\]
The same-factor term vanishes by the isometric left/right translation form of a one-factor variation. The ordered suffix derivative, inverse-link conversion, and all 16 orientation words have since received an independent quaternion finite-difference audit (3,840 ordered-pair checks); see [the 2026-11-11 sign audit](../audits/PF_I16_FOUR_FACTOR_MIXED_COVARIANT_DERIVATIVE_AUDIT_2026_11_11.md) and its deterministic verifier. This closes the group-product sign/trivialization sub-obligation, but not the inherited rotor-gradient hypothesis or the downstream analytic estimates. In the radius-two basis \(e_a=(\mathbf i,\mathbf j,\mathbf k)/2\), \([e_a,e_b]=\epsilon_{abc}e_c\), so \(\|[X,Y]\|\le\|X\|\|Y\|\) and each distinct-factor mixed term has norm at most \(\frac12\|X_i\|\|Y_j\|\). This records the working derivation and its orientation conversion; the fully self-contained independent sign/trivialization audit remains open.

In the pulled-back metric \(\widetilde g=\bigoplus_e a_e^{-1}g_e\), the resulting working per-face block bounds are
\[
\boxed{
H^{(f)}_{ee}\le\frac{32}{3}b_0+
\frac{320}{3}\frac{b_0^2}{a_0},\qquad
H^{(f)}_{eg}\le\frac{44}{3}b_0+
\frac{320}{3}\frac{b_0^2}{a_0}\quad(e\ne g).
}
\]
They use \(a_e,\sqrt{a_ea_g}\le8A_f\), \(A_f\ge a_0/2\), and the mixed term \(\beta_f/2\) for distinct factors.

Summing at most eight incident faces and at most 24 off-diagonal incidences per link, and retaining the factor two in the gradient equation, gives the comparison-matrix row estimate
\[
\|B\|_\mu\le
\left(\frac{512}{3}+704e^\mu\right)b_0+
\left(\frac{5120}{3}+5120e^\mu\right)\frac{b_0^2}{a_0}.
\]
At \(\mu=\log25\),
\[
\lambda_{\log25}\ge
\frac{a_0}{2}-\frac{53312}{3}b_0
-\frac{389120}{3}\frac{b_0^2}{a_0}.
\]
Thus \(b_0/a_0\le1/40000\) is a simple sufficient condition for positive derivative-flow decay. This is conditional on the mixed product estimate above and the inherited Bochner/Kato comparison.

The corresponding block row estimate for the dressed-reference curvature gives
\[
\kappa_{\rm BE}\ge
\frac{a_0}{2}-\frac{2624}{3}b_0
-\frac{20480}{3}\frac{b_0^2}{a_0}.
\]
At \(b_0/a_0\le1/40000\), this is \(>0.478a_0\).

## 4. Shared-link residual and its derivatives

For
\[
R_e=a_e\left(
\left|\sum_{f:e\in\partial f}v_{fe}\right|^2
-\frac1{d_e}\sum_{f:e\in\partial f}|v_{fe}|^2
\right),\qquad v_{fe}=\nabla_es_f,
\]
and \(R_e=0\) when \(d_e=0\), the first-derivative estimate
\(\|v_{fe}\|\le\beta_f\), together with \(a_e\le8A_f\) and \(A_f\ge a_0/2\), gives
\[
a_e\max_{f:e\in\partial f}\beta_f^2
\le16\frac{b_0^2}{a_0}.
\]
Using \(d_e\le8\),
\[
\boxed{\|R_e\|_\infty\le1040\frac{b_0^2}{a_0}=:R_*.}
\]
This magnitude bound is unchanged by the sharper Hessian estimate.

For a link \(h\), let \(q_{eh}\le8\) be the number of faces containing both \(e\) and \(h\). Differentiating covariantly,
\[
D_hR_e=2a_e\left[
\left\langle\sum_fx_f,\sum_fD_hx_f\right\rangle
-\frac1{d_e}\sum_f\langle x_f,D_hx_f\rangle
\right],\quad x_f=v_{fe}.
\]
Under the pulled-back block convention above,
\[
\|D_hx_f\|_{g_e}\le H_*/\sqrt{a_e},\qquad
H_*=\frac{44}{3}b_0+\frac{320}{3}\frac{b_0^2}{a_0}.
\]
Also \(\sqrt{a_e}\beta_f\le4b_0/\sqrt{a_0}\). Hence
\[
\|D_hR_e\|_{\widetilde g^*}
\le576H_*\frac{b_0}{\sqrt{a_0}}.
\]
At \(b_0/a_0\le1/40000\), \(H_*\le(5501/375)b_0\), so
\[
\boxed{\|D_hR_e\|_{\widetilde g^*}
\le8450\frac{b_0^2}{\sqrt{a_0}}.}
\]
The support has at most \(1+3d_e\le25\) links, giving
\[
\boxed{
\left(\sum_h\|D_hR_e\|^2\right)^{1/2}
\le42250\frac{b_0^2}{\sqrt{a_0}},\qquad
\sum_h\|D_hR_e\|
\le211250\frac{b_0^2}{\sqrt{a_0}}.
}
\]
These residual derivative bounds inherit the mixed-holonomy geometric condition in Section 3.

## 5. Status, supersession, and non-claims

- The exact weighted-mean identity and radial estimate in Section 2 are an explicit one-face derivation, conditional on the inherited \(\|s'\|_\infty\le\beta\).
- The face-holonomy Hessian blocks, derivative-flow rate, curvature estimate, and residual derivative constants are **working conditional estimates**. The four-factor mixed covariant derivative and orientation conversion now have an explicit working derivation, but the self-contained sign/trivialization/regularization audit remains open.
- The former coarse rotor Hessian estimate \(12\beta^2+24\beta\), and the former \(72b_0/38b_0\) face-block estimates, must not be used in downstream PF-I16 calculations when this refinement is adopted.
- The third-order coefficient has now been recalculated with the refined constants; see [the updated third-order record](PF_I16_DRESSED_THIRD_ORDER_COEFFICIENT_2026_11_10.md). Its bound remains conditional on the same curvature, derivative-flow and resolvent estimates.
- The fourth-order spatial tree estimate remains conditional on the corrected derivative flow, residual estimates, and path-block covariance/cumulant argument.
- No all-orders activity summability, physical kinetic/time normalization, genuine refining physical three-dimensional regulator, continuum reconstruction, or Yang–Mills mass gap is established.
- All P0–P5 and PF-G0–G5 gates remain OPEN.
