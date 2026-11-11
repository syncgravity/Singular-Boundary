# R3-IR — Conditional weighted trace–gradient Bochner block on the finite open SU(2) strip

**Date:** 2026-11-10  
**Status:** conditional finite-strip calculation; not a closed Hessian contraction theorem.  
**Route:** R3_IR finite open SU(2) strip only. This record is separate from PF-I16 and does not transfer to the Penrose auxiliary route.

## 1. Scope and conventions

Let \(M=\mathrm{SU}(2)^E\) be a finite open strip with the product radius-two bi-invariant metric. On each factor,
\[
\operatorname{Ric}_e=\frac12g_e,\qquad
\operatorname{diam}(M_e)=2\pi,\qquad
\lambda_1(-\Delta_e)=\frac34.
\]
Use \(\Delta=\operatorname{div}\nabla\), with nonpositive spectrum, and
\[
L=\Delta+2\nabla S_g\cdot\nabla,\qquad
d\mu_g=Z_g^{-1}e^{2S_g}\,d\mathrm{Haar}.
\]
Then \(L\) is symmetric and nonpositive on \(L^2(\mu_g)\):
\[
\langle h,Lh\rangle_{\mu_g}=-\|\nabla h\|_{L^2(\mu_g)}^2.
\]
Set \(f_t=P_tf\), \(\partial_tf_t=Lf_t\), \(H=\nabla^2f_t\), and \(H^S=\nabla^2S_g\). For each link,
\[
\phi_e=\Delta_ef_t,\qquad H_{ee}^{\rm tr}=\frac{\phi_e}{3}g_e.
\]

The local dressing assumptions used below are
\[
\|\nabla p_f\|_\infty\le\frac12,\qquad
q_g=\|s_g'\|_\infty+\|s_g''\|_\infty\le\frac{49}{576},
\]
and each link is incident to at most two strip plaquettes. Thus
\[
\|\nabla_eS_g\|_\infty\le
2\cdot\frac{49}{576}\cdot\frac12
=:B=\frac{49}{576}.
\tag{1.1}
\]
This is a local finite-strip hypothesis, not a bound for arbitrary 3D regulators.

## 2. Conditional one-link Poincaré inequality

Freeze all links except \(U_e\). The conditional law is
\[
d\mu_e(U_e\mid U_{\ne e})
=Z_e^{-1}e^{2S_g(U_e,U_{\ne e})}\,dU_e.
\]
Its log-density has oscillation
\[
\operatorname{osc}_{U_e}(2S_g)
\le 2\pi\|\nabla_e(2S_g)\|_\infty
\le4\pi B=\frac{49\pi}{144}.
\tag{2.1}
\]
Holley–Stroock comparison with the first nonzero Haar eigenvalue \(3/4\) gives
\[
\int|\nabla_eh|^2\,d\mu_e
\ge c_{\rm tr}\operatorname{Var}_{\mu_e}(h),
\qquad
c_{\rm tr}:=\frac34e^{-49\pi/144}
\approx0.2575101249909138.
\tag{2.2}
\]

The conditional mean of \(\phi_e\) is not generally zero. Exact conditional integration by parts gives
\[
m_e:=\mathbb E_{\mu_e}[\phi_e\mid U_{\ne e}]
=-2\mathbb E_{\mu_e}
 [\langle\nabla_ef_t,\nabla_eS_g\rangle\mid U_{\ne e}],
\tag{2.3}
\]
hence
\[
\|m_e\|_2^2\le4B^2\|\nabla_ef_t\|_2^2.
\tag{2.4}
\]
Combining (2.2) with variance decomposition yields
\[
\|\nabla_e\phi_e\|_2^2
\ge c_{\rm tr}\|\phi_e\|_2^2
-4c_{\rm tr}B^2\|\nabla_ef_t\|_2^2.
\tag{2.5}
\]
Since \(\|H_{ee}^{\rm tr}\|_2^2=\|\phi_e\|_2^2/3\),
\[
\boxed{
\|\nabla_eH_{ee}^{\rm tr}\|_2^2
\ge c_{\rm tr}\|H_{ee}^{\rm tr}\|_2^2
-\frac{4c_{\rm tr}B^2}{3}\|\nabla_ef_t\|_2^2.
}
\tag{2.6}
\]

The estimate is linkwise and remains valid after multiplication by any deterministic nonnegative link weight \(w_e\), independent of \(U_e\). Define
\[
\ell:=\frac{4c_{\rm tr}B^2}{3}
\approx0.00248474.
\tag{2.7}
\]

## 3. Weighted trace and gradient energies

For the H2 spatial weights
\[
w_e=(6/5)^{2d(e,\mathcal S)}
\]
(or any deterministic positive weights for which the stated weighted gradient estimate holds), set
\[
G_w^2=\sum_e w_e\|\nabla_ef_t\|_2^2,\qquad
T_w^2=\frac13\sum_e w_e\|\phi_e\|_2^2.
\tag{3.1}
\]
The trace energy identity below and (2.5) imply
\[
-\frac23\sum_e w_e\|\nabla\phi_e\|_2^2
\le-2c_{\rm tr}T_w^2+2\ell G_w^2.
\tag{3.2}
\]
Here the full gradient Dirichlet term dominates its \(e\)-link component, to which (2.5) is applied.

The established H2 weighted Bochner hypothesis is
\[
\frac{d}{dt}G_w^2\le-2cG_w^2,\qquad c=\frac{11}{120}.
\tag{3.3}
\]
Equations (3.2)–(3.3) define the coercive diagonal skeleton only; they do not yet include the trace commutator.

If all trace commutator terms were absent, the triangular comparison system would give
\[
T_w(t)^2\le e^{-2c_{\rm tr}t}T_w(0)^2
+\frac{\ell}{c_{\rm tr}-c}
 \big(e^{-2ct}-e^{-2c_{\rm tr}t}\big)G_w(0)^2,
\tag{3.4}
\]
with
\[
\frac{\ell}{c_{\rm tr}-c}\approx0.01498244.
\]
It would also yield
\[
G_w(t)^2+T_w(t)^2
\le e^{-2(c-\ell)t}\big(G_w(0)^2+T_w(0)^2\big),
\quad c-\ell\approx0.08918193.
\tag{3.5}
\]
These are **skeleton estimates**, not conclusions for the full dressed trace evolution.

## 4. Exact trace-block commutator

Since product-factor Laplacians commute,
\[
\partial_t\phi_e=L\phi_e+C_e,\qquad
C_e=[\Delta_e,L]f_t
=2\sum_d[\Delta_e,\nabla_dS_g\cdot\nabla_d]f_t.
\tag{4.1}
\]

For \(d\ne e\), product geometry gives
\[
\begin{aligned}
&\Delta_e\langle\nabla_dS_g,\nabla_df_t\rangle
-\langle\nabla_dS_g,\nabla_d\Delta_ef_t\rangle\\
&\quad=
\langle\nabla_d\Delta_eS_g,\nabla_df_t\rangle
+2H^S_{ed}:H_{ed}.
\end{aligned}
\tag{4.2}
\]
For \(d=e\), the covariant product rule and
\(\Delta_e^\nabla\nabla_eh=\nabla_e\Delta_eh+
\operatorname{Ric}_e^\sharp\nabla_eh\) give
\[
\begin{aligned}
&\Delta_e\langle\nabla_eS_g,\nabla_ef_t\rangle
-\langle\nabla_eS_g,\nabla_e\Delta_ef_t\rangle\\
&\quad=
\langle\nabla_e\Delta_eS_g,\nabla_ef_t\rangle
+2\operatorname{Ric}_e(\nabla_eS_g,\nabla_ef_t)
+2H^S_{ee}:H_{ee}.
\end{aligned}
\tag{4.3}
\]
There are **two** Ricci contributions in (4.3), one from each differentiated gradient field. Multiplying (4.2)–(4.3) by the drift factor \(2\) yields the exact identity
\[
\boxed{
C_e=
4\sum_d H^S_{ed}:H_{ed}
+2\sum_d\langle\nabla_d\Delta_eS_g,\nabla_df_t\rangle
+4\operatorname{Ric}_e(\nabla_eS_g,\nabla_ef_t).
}
\tag{4.4}
\]
For radius-two \(\mathrm{SU}(2)\), \(\operatorname{Ric}_e=\frac12g_e\), so the last term is
\[
2\langle\nabla_eS_g,\nabla_ef_t\rangle.
\tag{4.5}
\]
This coefficient is retained; it is not halved.

The weighted trace-energy identity is therefore
\[
\boxed{
\frac{d}{dt}T_w^2
=-\frac23\sum_e w_e\|\nabla\phi_e\|_2^2
+\frac23\sum_e w_e\langle\phi_e,C_e\rangle.
}
\tag{4.6}
\]

## 5. Quantified commutator remainder

Define the non-trace Hessian energy
\[
K_w^2=
\sum_{e,d}w_e\|H_{ed}\|_2^2-T_w^2\ge0.
\tag{5.1}
\]
It includes the diagonal trace-free and mixed blocks. Define the local Hessian row bound
\[
A_2=
\operatorname*{ess\,sup}_{U}\sup_e
\left(\sum_d\|H^S_{ed}(U)\|_F^2\right)^{1/2}.
\tag{5.2}
\]
Define the third-derivative contraction operator
\[
(\mathcal M_S(U)v)_e
=\sum_d\langle\nabla_d\Delta_eS_g(U),v_d\rangle,
\tag{5.3}
\]
and its weight-compatible norm
\[
A_{3,w}:=
\operatorname*{ess\,sup}_{U}
\left\|W^{1/2}\mathcal M_S(U)W^{-1/2}\right\|_{\rm op},
\qquad W=\operatorname{diag}(w_e).
\tag{5.4}
\]
The operator maps the direct sum of link tangent spaces to link-indexed scalars; (5.4) is the required weighted \(\ell^2\)-operator norm, not merely a supremum of individual third derivatives.

Cauchy–Schwarz in the link index and configuration variable gives
\[
\left|\sum_e w_e\left\langle\phi_e,
\sum_dH^S_{ed}:H_{ed}\right\rangle\right|
\le\sqrt3 A_2T_w\sqrt{T_w^2+K_w^2},
\tag{5.5}
\]
\[
\left|\sum_e w_e\left\langle\phi_e,
\sum_d\langle\nabla_d\Delta_eS_g,\nabla_df_t\rangle\right\rangle\right|
\le\sqrt3 A_{3,w}T_wG_w,
\tag{5.6}
\]
and
\[
\left|\sum_e w_e\langle\phi_e,
2\langle\nabla_eS_g,\nabla_ef_t\rangle\rangle\right|
\le2\sqrt3 B T_wG_w.
\tag{5.7}
\]
Combining (3.2), (4.4), and (4.6) gives
\[
\boxed{
\begin{aligned}
\frac{d}{dt}T_w^2\le{}&
-2c_{\rm tr}T_w^2+2\ell G_w^2\\
&+\frac{8A_2}{\sqrt3}T_w\sqrt{T_w^2+K_w^2}\\
&+\frac{4(A_{3,w}+B)}{\sqrt3}G_wT_w.
\end{aligned}}
\tag{5.8}
\]
Using \(\sqrt{T_w^2+K_w^2}\le T_w+K_w\),
\[
\boxed{
\begin{aligned}
\frac{d}{dt}T_w^2\le{}&
-2\left(c_{\rm tr}-\frac{4A_2}{\sqrt3}\right)T_w^2
+2\ell G_w^2\\
&+\frac{8A_2}{\sqrt3}T_wK_w
+\frac{4(A_{3,w}+B)}{\sqrt3}G_wT_w.
\end{aligned}}
\tag{5.9}
\]

Thus the previous two-variable trace–gradient subsystem is not the full system: the \(T_wK_w\) term is real and must be absorbed by a dissipative estimate for the trace-free/mixed Hessian sector.

If \(K_w\) were absent, the two-variable quadratic-form test would be
\[
\boxed{
(c-\ell)\left(c_{\rm tr}-\frac{4A_2}{\sqrt3}\right)
>\frac{(A_{3,w}+B)^2}{3},
\quad
c-\ell>0,\quad c_{\rm tr}-\frac{4A_2}{\sqrt3}>0.
}
\tag{5.10}
\]
This is only a diagnostic threshold, not a closure result, because \(K_w\) has not been eliminated and \(A_2,A_{3,w}\) have not yet been evaluated.

## 6. Remaining coupled-system obligation

A full closure requires a compatible estimate for
\[
\frac{d}{dt}K_w^2
\le-2\gamma_KK_w^2
+2r_{KG}G_wK_w+2r_{KT}T_wK_w
+2r_{GG}G_w^2+2r_{TT}T_w^2,
\tag{6.1}
\]
with constants uniform in strip length and compatible with the same spatial weights. One must then verify positive definiteness of the resulting \(3\times3\) quadratic form.

The local plaquette evaluation of \(A_2\), the ordered third-derivative operator \(A_{3,w}\), and the trace-free/mixed Hessian evolution (6.1) remain open. No numerical values for these constants are asserted here.

### Non-claims

- No pointwise Hessian estimate is proved.
- No full weighted Hessian semigroup contraction is proved.
- No uniform interacting Hessian bound at \(\lambda=1\) is proved.
- No interacting spectral gap at \(\lambda=1\), 3D regulator transfer, continuum reconstruction, or Yang–Mills mass gap follows.
- This R3_IR strip calculation is not a PF-I16 theorem and does not alter any canonical P0–P5 or PF-G0–G5 acceptance status.
