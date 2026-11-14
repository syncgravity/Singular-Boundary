# PF-I16 corrected reversible flow and two-point resolvent decay

**Date:** 2026-11-13  
**Scope:** finite accepted-rhombus SU(2) graph, exact single-face dressing, corrected isolated-rotor bounds, and finite-product derivative flow under the explicit source-incidence and weak-coupling hypotheses.  
**Status:** the corrected derivative-flow estimate, face-map metric pullback, and finite-product Kato–Bochner comparison are closed under the stated finite-graph hypotheses; the two-point resolvent-decay implication follows. This result is not an all-orders activity theorem, a physical-time theorem, or a mass-gap proof.

## 1. Sign reconciliation: the ground-state measure fixes the drift

Let \(K=-\Delta_{\widetilde g}\) be the positive product-link Laplacian and let \(\Phi\) be the sum of the isolated-face logarithmic dressings. The exact finite-graph conjugation in [PF-I16 exact dressing and shared-link residual](../theorems/PF_I16_LOCAL_DRESSING_SHARED_LINK_RESIDUAL_2026_11_10.md) is
\[
e^{-\Phi}He^\Phi
=L_\Phi+\text{constant}-\sum_eR_e,\qquad
L_\Phi=K-2\langle\nabla\Phi,\nabla\,\cdot\,\rangle.
\]
Thus, with the Laplacian convention \(\Delta=\operatorname{div}\nabla\),
\[
\boxed{L_\Phi=-\Delta_{\widetilde g}
-2\langle\nabla\Phi,\nabla\,\cdot\,\rangle,\qquad
\mathscr G_\Phi=-L_\Phi
=\Delta_{\widetilde g}+2\nabla_{\nabla\Phi}.}
\tag{1.1}
\]
The reversible measure is
\[
d\nu_\Phi=Z_\Phi^{-1}e^{2\Phi}\,dU.
\]
Indeed, integration by parts gives
\[
\int fL_\Phi g\,d\nu_\Phi
=\int\langle\nabla f,\nabla g\rangle_{\widetilde g}\,d\nu_\Phi.
\tag{1.2}
\]
The drift sign is therefore fixed by the exact ground-state transform; it is not a convention that can be chosen independently.

**Correction to the earlier pointwise Kato–Bochner dossier:** its displayed pair
\(L_\Phi=-\Delta+2\nabla\Phi\cdot\nabla\) and
\(\mathscr G_\Phi=\Delta-2\nabla_{\nabla\Phi}\)
has the opposite drift from the exact conjugation above. Those signs correspond to the reversible density \(e^{-2\Phi}\), not the actual dressed density \(e^{2\Phi}\). Equations below are rederived with (1.1). Because the comparison uses absolute Hessian-block bounds, the final numerical row-sum lower bounds are unchanged; the Bochner tensor itself must be written with the corrected sign.

## 2. Corrected vector Bochner identity

For \(u_t=P_tf=e^{t\mathscr G_\Phi}f\) and \(W=\nabla u_t\), the gradient commutation identity for a generator \(\Delta+Z\cdot\nabla\) is
\[
(\partial_t-\Delta^\nabla-\nabla_Z)W
=-(\operatorname{Ric}^{\sharp}-(\operatorname{sym}\nabla Z)^\sharp)W.
\]
Here \(Z=2\nabla\Phi\), so
\[
\boxed{
(\partial_t-\Delta^\nabla_{\widetilde g}
-2\nabla_{\nabla\Phi})W
=-(\operatorname{Ric}^{\sharp}_{\widetilde g}
-2(\nabla^2\Phi)^\sharp)W.}
\tag{2.1}
\]
This is the sign-corrected Bakry–Émery tensor for the actual ground-state measure.

Let \(W_e\) be the link-tangent component. Kato's inequality and the product connection give
\[
(\partial_t-\mathscr G_\Phi)|W_e|
\le-\frac{a_0}{2}|W_e|
+2\sum_g\|(\nabla^2\Phi)_{eg}\|_{\mathrm{op}}|W_g|,
\tag{2.2}
\]
where the lower bound uses
\[
\operatorname{Ric}^{\sharp}_{\widetilde g}|_{T_eM}
-2(\nabla^2\Phi)_{ee}^{\sharp}
\ge\left(\frac{a_0}{2}-2\|(\nabla^2\Phi)_{ee}\|_{\mathrm{op}}\right)I
\]
and bounds off-diagonal blocks in absolute value. The finite-product maximum principle then yields the same cooperative comparison matrix as the absolute-block calculation in the earlier dossier:
\[
D^+U_e(t)\le-\frac{a_0}{2}U_e(t)+\sum_gA_{eg}U_g(t),
\quad
A_{eg}=2\sup\|(\nabla^2\Phi)_{eg}\|_{\mathrm{op}}.
\tag{2.3}
\]
This derivation uses the corrected reversible generator, not the opposite-drift operator.

## 3. Corrected local blocks and comparison rate

Use the corrected rotor estimates
\[
\|\nabla s_f\|_\infty\le2\beta_f,\qquad
\|\nabla^2s_f\|_{\mathrm{op}}
\le\frac43\beta_f+\frac{80}{3}\beta_f^2,
\qquad \beta_f=\frac{|b_f|}{A_f},
\]
from [the isolated-rotor obstruction and repair](../audits/PF_I16_ISOLATED_ROTOR_FIRST_DERIVATIVE_OBSTRUCTION_2026_11_11.md). Combine them with the independently audited four-factor mixed covariant derivative signs in [the four-factor audit](../audits/PF_I16_FOUR_FACTOR_MIXED_COVARIANT_DERIVATIVE_AUDIT_2026_11_11.md).

Under the universal source bounds
\[
d_e\le8,\quad a_e\le8A_f,\quad A_f\ge a_0/2,\quad
0\le b_f\le b_0,
\]
the corrected provisional face-pullback block bounds are
\[
h_d\le\frac{32}{3}b_0+\frac{1280}{3}\frac{b_0^2}{a_0},
\qquad
h_o\le\frac{56}{3}b_0+\frac{1280}{3}\frac{b_0^2}{a_0}.
\tag{3.1}
\]
The diagonal bound is \(8A_f\|\nabla^2s_f\|\). The off-diagonal bound adds the mixed-map term
\(\frac12\|\nabla s_f\|\sqrt{a_ea_g}\); this is why its linear coefficient is \(56/3\), rather than \(32/3\).

Each link has at most eight incident faces, each face has three other boundary links, and hence the link-overlap graph has degree at most \(24\). The unweighted row bound gives the conditional curvature lower bound
\[
\kappa\ge\frac{a_0}{2}
-\frac{3200}{3}b_0
-\frac{81920}{3}\frac{b_0^2}{a_0}.
\tag{3.2}
\]
For the weighted row norm with \(\mu=\log25\),
\[
\|A\|_\mu\le16(h_d+3e^\mu h_o),
\]
so the derivative-flow rate is bounded below by
\[
\lambda\ge\frac{a_0}{2}
-\frac{67712}{3}b_0
-\frac{1556480}{3}\frac{b_0^2}{a_0}.
\tag{3.3}
\]
At \(b_0/a_0\le1/50000\), the exact rational margins are
\[
\boxed{\kappa\ge\frac{1869749}{3906250}a_0
=0.478655744\,a_0,}
\]
\[
\boxed{\lambda\ge\frac{188981}{3906250}a_0
=0.048379136\,a_0.}
\tag{3.4}
\]
The face-map pullback and finite-product Kato comparison are derived in the companion [closure audit](../audits/PF_I16_FACE_PULLBACK_KATO_BOCHNER_CLOSURE_2026_11_13.md). The resulting derivative-flow theorem is uniform in finite graph volume under the stated source-incidence and coupling hypotheses. These constants are not physical coefficients or physical time.

## 4. Conditional spatial derivative flow

With \(\mathsf D_e\) denoting the link derivative in the orthonormal product metric, the cooperative comparison gives
\[
\boxed{
\|\mathsf D_eP_tf\|_\infty
\le e^{-\lambda t}
\sum_g e^{-(\log25)d(e,g)}
\|\mathsf D_gf\|_\infty.}
\tag{4.1}
\]
This is a finite-graph estimate with no total-volume factor, conditional on (3.1) and the stated incidence bounds.

For centered \(f\), let
\[
Gf=L_\Phi^{-1}f=\int_0^\infty P_tf\,dt.
\]
Since \(\mathsf D_e\) annihilates constants, integrating (4.1) gives
\[
\boxed{
\|\mathsf D_eGf\|_\infty
\le\frac1\lambda
\sum_{a\in S_f}e^{-(\log25)d(e,a)}
\|\mathsf D_af\|_\infty,}
\tag{4.2}
\]
where \(S_f\) is the link support of \(f\). The positive lower bound \(\kappa\) in (3.2) supplies the centered inverse \(G\); \(\lambda\) supplies the derivative integral.

## 5. Two-point resolvent-decay theorem

Let \(f,g\) be centered local functions supported on \(S_f,S_g\). Define
\[
M(f)=\sum_{a\in S_f}\|\mathsf D_af\|_\infty,\qquad
M(g)=\sum_{b\in S_g}\|\mathsf D_bg\|_\infty.
\]
The Dirichlet identity and Cauchy–Schwarz in the link sum give
\[
\begin{aligned}
|\nu_\Phi(fGg)|
&=|\nu_\Phi[\Gamma(Gf,Gg)]|\\
&\le\sum_e\|\mathsf D_eGf\|_\infty
             \|\mathsf D_eGg\|_\infty\\
&\le\lambda^{-2}
\sum_{a\in S_f,b\in S_g}
M_a(f)M_b(g)
\sum_e e^{-(\log25)(d(e,a)+d(e,b))}.
\end{aligned}
\tag{5.1}
\]
Here \(M_a(f)=\|\mathsf D_af\|_\infty\), and similarly for \(g\).

For a graph of maximum degree \(24\), shell counting gives
\[
\sum_e e^{-\mu(d(e,a)+d(e,b))}
\le C_{\mu,\gamma}e^{-\gamma d(a,b)}
\]
whenever \(0<\gamma<\mu-\log23\), with
\[
C_{\mu,\gamma}
=1+\frac{24e^{-(\mu-\gamma)}}{1-23e^{-(\mu-\gamma)}}.
\]
Choose
\[
\mu=\log25,\qquad \gamma=\frac12\log\frac{25}{23}.
\]
Then
\[
C_{\mu,\gamma}
=1+\frac{24}{5\sqrt{23}-23}
<25.511,\qquad
\gamma=0.0416908044695\ldots.
\]
Consequently
\[
\boxed{
|\nu_\Phi(fGg)|
\le\frac{C_{\mu,\gamma}}{\lambda^2}
e^{-\gamma d(S_f,S_g)}M(f)M(g).}
\tag{5.2}
\]
This bound is uniform in the number of links. It is a conditional finite-graph spatial decay estimate for the dressed reference resolvent, not yet for the actual interacting vacuum.

For the second-order residual energy coefficient
\[
E_{ij}=-2\nu_\Phi(r_iGr_j),
\]
where \(r_i,r_j\) are centered residuals, (5.2) gives
\[
|E_{ij}|
\le\frac{2C_{\mu,\gamma}}{\lambda^2}
e^{-\gamma d(S_i,S_j)}M(r_i)M(r_j).
\tag{5.3}
\]
Using the corrected residual derivative estimate
\[
M(r_i)\le537850\,\frac{b_0^2}{\sqrt{a_0}}
\]
and (3.4), for \(b_0/a_0\le1/50000\) this yields the explicit conditional bound
\[
\boxed{
|E_{ij}|
<6.307\times10^{15}
\frac{b_0^4}{a_0^3}
e^{-\gamma d(S_i,S_j)}.}
\tag{5.4}
\]
The exponent is small but strictly positive and independent of graph size.

## 6. Exact scope and next obstruction

**Derived here:** the drift sign forced by the exact ground-state transform; the corresponding reversible integration-by-parts identity; the corrected vector Bochner tensor; the corrected absolute-block comparison; and the two-point resolvent-decay implication.

**Conditional inputs:** corrected face-pullback block bounds, finite-product Kato comparison, and the residual derivative estimate. The numerical margins in (3.4) are exact arithmetic under those inputs.

**Not proved:** the third-order spatial tree bound; fourth-order spatial connected-support cancellation for coupled Penrose subsystems; an all-orders activity majorant; stability of the extensive residual perturbation at the physical coupling; source-derived physical kinetic/time; a refining physical three-dimensional regulator; continuum reconstruction; or a positive physical mass gap.

The next mathematical task is to obtain a genuinely three-support tree estimate for the exact third-order coefficient. The two-point estimate (5.2) is one input, but it cannot be multiplied naively to claim a tree bound: the nested product contains an undifferentiated resolvent factor, and the required connected cancellation/derivative control must be proved explicitly.


## 7. Exact arithmetic reproduction

The exact rational margins, algebraic shell-convolution upper bound, and rounded pair coefficient are checked by
[verify_pf_i16_two_point_resolvent_decay.py](../verification/verify_pf_i16_two_point_resolvent_decay.py).
The script uses only Python's standard-library Fraction arithmetic; it verifies the square-root comparison by integer squaring and does not use floating-point arithmetic for the inequalities.

Expected output:

    PASS: corrected curvature margin 1869749/3906250
    PASS: corrected weighted derivative-flow margin 188981/3906250
    PASS: shell-convolution constant C < 25.511
    PASS: residual pair coefficient < 6.307e15 * b0^4/a0^3


## 8. Finite-product analytic closure (2026-11-13)

The face-map metric pullback and Kato–Bochner comparison used in Sections 2–4 are derived in [the companion closure audit](../audits/PF_I16_FACE_PULLBACK_KATO_BOCHNER_CLOSURE_2026_11_13.md). The derivative-flow estimate is therefore a proved finite-accepted-graph result under the explicit source-incidence, allocation, and weak-coupling hypotheses, not an unresolved analytic input. The result remains separate from physical-time normalization and the interacting-vacuum/continuum problem.
