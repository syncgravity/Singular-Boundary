# PF-I16 — Pointwise Kato–Bochner comparison and derivative-flow locality

**Date:** 2026-11-10  
**Status:** conditional finite-graph analytic estimate. The componentwise Kato–Bochner and Duhamel comparison are derived below from the product diffusion and the refined face-Hessian blocks. The latter still depend on the isolated-rotor first-derivative estimate and the four-factor holonomy Hessian calculation; the latter receives a working left/right-trivialized derivation here but awaits a standalone sign-and-regularization audit. This record closes no canonical continuum gate.

## 1. Finite-graph setup and metric conventions

Let
\[
M=\prod_{e\in E}\mathrm{SU}(2)_e,\qquad
\widetilde g=\bigoplus_{e\in E}a_e^{-1}g_e,
\]
where each \(g_e\) is the radius-two bi-invariant metric, \(a_e\ge a_0>0\), and \(E\) is finite. Write \(\nabla\), \(\Delta_{\widetilde g}\), and \(\Delta^\nabla_{\widetilde g}\) for the product Levi-Civita connection, scalar Laplacian, and connection Laplacian, with \(\Delta=\operatorname{div}\nabla\) (nonpositive spectrum).

For the dressed potential \(\Phi=\sum_f s_f\circ H_f\), the nonnegative operator and its Markov generator are
\[
L_\Phi=-\Delta_{\widetilde g}
       +2\langle\nabla\Phi,\nabla\,\cdot\,\rangle,
\qquad
\mathscr G=-L_\Phi
=\Delta_{\widetilde g}-2\nabla_{\nabla\Phi}.
\]
Set \(P_t=e^{-tL_\Phi}=e^{t\mathscr G}\). The product metric is essential: its connection preserves every link tangent bundle \(T_eM\).

The radius-two three-sphere has \(\operatorname{Ric}_{g_e}=\frac12g_e\). Constant scaling by \(a_e^{-1}\) leaves the Levi-Civita connection unchanged and scales the Ricci endomorphism by \(a_e\). Thus
\[
\operatorname{Ric}^{\sharp}_{\widetilde g}|_{T_eM}
=\frac{a_e}{2}I\ge\frac{a_0}{2}I.
\tag{1.1}
\]

## 2. Four-factor holonomy Hessian and refined face blocks

For an oriented face word
\[
H=x_1x_2x_3x_4,\qquad x_i=U_i^{\epsilon_i},\quad
\epsilon_i\in\{\pm1\},
\]
use original-link left-trivialized variations \(\dot U_i=U_i\xi_i\). The corresponding face-factor variation \(\dot x_i=x_iX_i\) is
\[
X_i=
\begin{cases}
\xi_i,&\epsilon_i=+1,\\
-\operatorname{Ad}_{U_i}\xi_i,&\epsilon_i=-1,
\end{cases}
=
\epsilon_i\operatorname{Ad}_{U_i^{(1-\epsilon_i)/2}}\xi_i.
\tag{2.1}
\]
This conversion is norm preserving for the bi-invariant metric.

Put \(T_i=x_{i+1}\cdots x_4\), \(T_4=1\), and
\[
\eta_i=\operatorname{Ad}_{T_i^{-1}}X_i.
\]
Then \(H^{-1}\dot H=\sum_i\eta_i\). For distinct factor variations, differentiating the transported left-trivialized components gives
\[
D_i\eta_j=
\begin{cases}
0,&i<j,\\
-[\eta_i,\eta_j],&i>j.
\end{cases}
\]
The target Levi-Civita connection in left trivialization is
\[
(\nabla_{\dot H}W)_{\rm left}
=D_{\dot H}w+\frac12[\eta,w].
\]
The resulting working mixed covariant derivative is
\[
(\nabla dH)(X_i,Y_j)=
\begin{cases}
\frac12[\eta_i(X_i),\eta_j(Y_j)],&i<j,\\
-\frac12[\eta_i(X_i),\eta_j(Y_j)],&i>j,\\
0,&i=j.
\end{cases}
\tag{2.2}
\]
The same-factor term vanishes because varying one factor acts by a target left/right translation (and inversion is an isometry). For radius-two \(\mathrm{SU}(2)\), the orthonormal basis \(e_1=\mathbf i/2,e_2=\mathbf j/2,e_3=\mathbf k/2\) has \([e_a,e_b]=\epsilon_{abc}e_c\), so \(\|[X,Y]\|\le\|X\|\|Y\|\), and each distinct-factor mixed term in (2.2) has norm at most \(\frac12\|X_i\|\|Y_j\|\).

Combining the covariant chain rule
\[
\nabla^2(s_f\circ H_f)(X,Y)
=\nabla^2s_f(dH_fX,dH_fY)
+\langle\nabla s_f,\nabla dH_f(X,Y)\rangle
\]
with the isolated-rotor estimate
\[
\|\nabla s_f\|_\infty\le\beta_f,\qquad
\|\nabla^2s_f\|_{\rm op}
\le\frac43\beta_f+\frac{20}{3}\beta_f^2,
\]
and \(a_e\le8A_f,\ A_f\ge a_0/2,\ \beta_f\le2b_0/a_0\), gives the working pulled-back block bounds
\[
h_{\rm d}:=\|(\nabla^2(s_f\circ H_f))_{ee}\|_{\rm op}
\le\frac{32}{3}b_0+\frac{320}{3}\frac{b_0^2}{a_0},
\tag{2.3}
\]
\[
h_{\rm o}:=\|(\nabla^2(s_f\circ H_f))_{eg}\|_{\rm op}
\le\frac{44}{3}b_0+\frac{320}{3}\frac{b_0^2}{a_0},
\quad e\ne g.
\tag{2.4}
\]
These are conditional on the inherited isolated-rotor first-derivative bound and on the four-factor calculation (2.1)–(2.2), whose complete standalone sign/trivialization audit remains pending.

## 3. Vector Bochner equation and componentwise Kato inequality

For \(f_t=P_tf\) and \(W=\nabla f_t\), the gradient commutation identity for the generator \(\mathscr G=\Delta-2\nabla_{\nabla\Phi}\) gives
\[
\left(
\partial_t-\Delta^\nabla_{\widetilde g}
+2\nabla_{\nabla\Phi}
\right)W
=-\left(\operatorname{Ric}^{\sharp}_{\widetilde g}
       +2(\nabla^2\Phi)^\sharp\right)W.
\tag{3.1}
\]
The sign is fixed by the drift \(-2\nabla\Phi\): the Bakry–Émery endomorphism is \(\operatorname{Ric}^{\sharp}+2(\nabla^2\Phi)^\sharp\).

Let \(W_e\) be the \(T_eM\) component and \(u_e(t,x)=|W_e(t,x)|_{g_e}\). Since the product connection and connection Laplacian preserve \(T_eM\), Kato's inequality, (1.1), and the block decomposition of \(\nabla^2\Phi\) imply, wherever \(u_e>0\),
\[
(\partial_t-\mathscr G)u_e
\le-\frac{a_0}{2}u_e
+2\sum_g\|(\nabla^2\Phi)_{eg}\|_{\rm op}\,u_g.
\tag{3.2}
\]
At zeros this is interpreted in the upper-Dini/viscosity sense, obtained by applying the smooth Kato calculation to
\[
u_{e,\varepsilon}=(|W_e|^2+\varepsilon^2)^{1/2}
\]
and passing to \(\varepsilon\downarrow0\). No integrated Bochner inequality is used to infer (3.2).

Define the configuration-independent nonnegative matrix
\[
A_{eg}=2\sup_{x\in M}
\|(\nabla^2\Phi(x))_{eg}\|_{\rm op}.
\tag{3.3}
\]
Compactness of finite \(M\) and the scalar maximum principle applied to \(u_e\) give, for
\[
U_e(t)=\sup_{x\in M}u_e(t,x),
\]
the cooperative upper-Dini differential inequality
\[
D^+U_e(t)\le-\frac{a_0}{2}U_e(t)+\sum_gA_{eg}U_g(t).
\tag{3.4}
\]
The supremum step uses that at a spatial maximum of \(u_e\), \(\mathscr G u_e\le0\), while \(u_g(x)\le U_g\) for every \(g\). Thus it is a pointwise-to-supremum argument, not a volume-integrated estimate.

## 4. Explicit comparison matrix and Duhamel iteration

Each link belongs to at most eight accepted faces, and each incident four-link face contributes three other links. A nonnegative dominating matrix can therefore be chosen with
\[
A_{ee}=16h_{\rm d},\qquad
A_{eg}=2h_{\rm o}\#\{f:e,g\in\partial f\}\quad(e\ne g).
\]
For the link-overlap graph distance \(d(e,g)\), its weighted row norm obeys
\[
\|A\|_\mu:=
\sup_e\sum_gA_{eg}e^{\mu d(e,g)}
\le16(h_{\rm d}+3e^\mu h_{\rm o}).
\]
Consequently
\[
\|A\|_\mu\le
\left(\frac{512}{3}+704e^\mu\right)b_0
+\left(\frac{5120}{3}+5120e^\mu\right)\frac{b_0^2}{a_0}.
\tag{4.1}
\]
At \(\mu=\log25\),
\[
\|A\|_{\log25}\le
\frac{53312}{3}b_0+\frac{389120}{3}\frac{b_0^2}{a_0}.
\tag{4.2}
\]

Finite-dimensional cooperative comparison applied to (3.4) yields
\[
U(t)\le e^{-a_0t/2}e^{tA}U(0).
\]
The triangle inequality for graph distance gives
\[
\sum_g(A^n)_{eg}e^{\mu d(e,g)}
\le\|A\|_\mu^n.
\]
Hence, with
\[
\lambda=\frac{a_0}{2}-\|A\|_{\log25}
=\frac{a_0}{2}
-\frac{53312}{3}b_0
-\frac{389120}{3}\frac{b_0^2}{a_0},
\tag{4.3}
\]
the derivative-flow estimate follows with kernel prefactor exactly one:
\[
\boxed{
\|D_eP_tf\|_\infty
\le e^{-\lambda t}
\sum_g e^{-(\log25)d(e,g)}\|D_gf\|_\infty.
}
\tag{4.4}
\]
Here \(D_e\) denotes the link derivative in the same normalization as the product metric used above. At \(b_0/a_0\le1/40000\),
\[
\lambda\ge\frac{26087}{468750}a_0
>0.0556522a_0.
\tag{4.5}
\]
This is a finite-graph estimate uniform in the number of links under the stated local coefficient/incidence bounds.

## 5. Kernel sums, convolution, and oscillation

For \(K_\mu(e,g)=e^{-\mu d(e,g)}\), the link-overlap graph has degree at most \(24\), hence
\[
|S_r(e)|\le24\cdot23^{r-1},\qquad r\ge1.
\]
At \(\mu=\log25\), both row and column sums satisfy
\[
\sup_e\sum_gK_\mu(e,g)
=\sup_g\sum_eK_\mu(e,g)\le
1+\frac{24/25}{1-23/25}=13.
\tag{5.1}
\]
For \(0<\nu<\mu-\log23\), the triangle inequality and shell sum give
\[
\sum_zK_\mu(e,z)K_\mu(z,g)
\le C_{\mu,\nu}K_\nu(e,g),\qquad
C_{\mu,\nu}=1+
\frac{24e^{-(\mu-\nu)}}{1-23e^{-(\mu-\nu)}}.
\tag{5.2}
\]
For \(\nu=\frac12\log(25/23)\), \(C_{\mu,\nu}<25.511\). Repeated convolution loses spatial exponent; it must not be treated as preserving \(\mu\).

The radius-two \(\mathrm{SU}(2)\) diameter is \(2\pi\). Changing product coordinates one at a time gives, for \(f\) supported on a finite link set \(S\),
\[
\operatorname{osc}(P_tf)
\le26\pi e^{-\lambda t}
\sum_{g\in S}\|D_gf\|_\infty.
\tag{5.3}
\]
The local version is
\[
\operatorname{osc}_e(P_tf)
\le2\pi e^{-\lambda t}
\sum_{g\in S}e^{-(\log25)d(e,g)}\|D_gf\|_\infty.
\tag{5.4}
\]
Neither estimate carries a total-volume factor.

## 6. Status and non-claims

- The vector Bochner identity, Kato projection, finite-product maximum principle, cooperative Duhamel comparison, weighted matrix estimate, and kernel shell sums are derived for each finite graph under the stated metric and coefficient conventions.
- The derivative-flow estimate (4.4) is **not currently certified**. The four-factor group-product signs in (2.1)–(2.2) have passed the independent audit recorded in [the mixed-derivative audit](../audits/PF_I16_FOUR_FACTOR_MIXED_COVARIANT_DERIVATIVE_AUDIT_2026_11_11.md). However, the inherited isolated-rotor estimate \(\|s_f'\|_\infty\le\beta_f\), used to obtain the Hessian blocks (2.3)–(2.4), is contradicted by the radial equation's exact linear response, which has coefficient \(4/3\). See [the perturbative obstruction](../audits/PF_I16_ISOLATED_ROTOR_FIRST_DERIVATIVE_OBSTRUCTION_2026_11_11.md). The Hessian blocks, comparison matrix, decay rate and downstream constants must be rederived; do not use the displayed numerical rate as an established PF-I16 estimate.
- The comparison-matrix estimate is not an all-orders connected-activity bound. The convolution estimate explicitly loses spatial exponent.
- The finite-graph estimate does not establish a source-derived physical kinetic/time normalization, a genuinely refining physical three-dimensional regulator, continuum reconstruction, or a Yang–Mills mass gap.
- All canonical P0–P5 and Penrose PF-G0–G5 gates remain OPEN.


## 7. 2026-11-11 rotor-input correction

The original face blocks (2.3)–(2.4), comparison constant (4.2), and decay rate (4.3) used the false inherited estimate \(\|s_f'\|_\infty\le\beta_f\). The radial equation instead gives the exact linear response \(\|s_\beta'\|_\infty/\beta\to4/3\), and the corrected maximum-principle bound is \(\|s_\beta'\|_\infty\le2\beta\). With the corrected radial Hessian bound, the provisional face blocks become
\[
h_d\le\frac{32}{3}b_0+\frac{1280}{3}\frac{b_0^2}{a_0},\qquad
h_o\le\frac{56}{3}b_0+\frac{1280}{3}\frac{b_0^2}{a_0}.
\]
Consequently the weighted comparison at \(\mu=\log25\) is
\[
\lambda_{\log25}\ge\frac{a_0}{2}
-\frac{67712}{3}b_0-\frac{1556480}{3}\frac{b_0^2}{a_0}.
\]
For \(b_0/a_0\le1/50000\), this lower bound exceeds \(0.0483a_0\). These corrected constants remain conditional on the finite-product Bochner/Kato comparison and the face-map metric calculations. The old numerical rate and \(1/40000\) threshold are superseded, not certified.
