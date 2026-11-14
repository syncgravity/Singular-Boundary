# PF-I16 — Radial character coefficients and exact shared-link Casimir contraction

**Date:** 2026-11-14  
**Status:** exact low-order perturbative coefficients and an exact representation-theoretic contraction identity. This is a useful reduction of the pair-insertion problem, but it is NOT an all-orders projective-norm estimate. No QF, WDG, KP, or proof gate is promoted.

## 1. Radial variable adapted to the pair insertion

For the radius-two SU(2) isolated-face rotor, let \(p=\cos\theta=\frac12\operatorname{Tr}H\), \(q_\beta(\theta)=s_\beta'(\theta)\), and define the regular class function
\[
R_\beta(p):=-\frac{q_\beta(\theta)}{\sin\theta}.
\]
Then
\[
\nabla s_\beta(H)=R_\beta(p(H))\,\nabla p(H)
\]
(up to the fixed metric/trivialization convention already used for the face gradient). This is the radial factor that actually occurs in the pair insertion.

The recorded radial equation
\[
q'+2\cot\theta\,q=-4(q^2+\beta\cos\theta+\lambda_\beta)
\]
becomes
\[
(1-p^2)R_\beta'(p)-3pR_\beta(p)
=-4\{(1-p^2)R_\beta(p)^2+\beta p+\lambda_\beta\}.
\tag{1.1}
\]
The weighted-mean identity is
\[
\lambda_\beta
=-\frac{\int_{-1}^{1}(1-p^2)^{3/2}R_\beta(p)^2\,dp}
{\int_{-1}^{1}(1-p^2)^{1/2}\,dp}.
\tag{1.2}
\]

## 2. Exact first and second perturbative coefficients

At \(\beta=0\), \(R_0=0\). The simple isolated ground eigenvalue gives an analytic small-\(\beta\) branch. Write
\[
R_\beta(p)=\beta R_1(p)+\beta^2R_2(p)+O(\beta^3),\qquad
\lambda_\beta=\beta^2\lambda_2+O(\beta^3).
\]
The absence of a linear term in \(\lambda_\beta\) follows directly from (1.2).

At order \(\beta\), (1.1) gives
\[
(1-p^2)R_1'-3pR_1=-4p.
\]
The regular solution is
\[
R_1(p)=\frac43.
\]
At order \(\beta^2\), (1.2) and
\[
\frac{\int_{-1}^{1}(1-p^2)^{3/2}\,dp}
{\int_{-1}^{1}(1-p^2)^{1/2}\,dp}=\frac34
\]
give
\[
\lambda_2=-\frac34\left(\frac43\right)^2=-\frac43.
\]
The order-\(\beta^2\) equation is
\[
(1-p^2)R_2'-3pR_2
=-4\left\{\frac{16}{9}(1-p^2)-\frac43\right\}
=-\frac{16}{9}+\frac{64}{9}p^2.
\]
Since the left-hand operator sends \(p\) to \(1-4p^2\), the regular solution is
\[
R_2(p)=-\frac{16}{9}p.
\]
Thus
\[
\boxed{R_\beta(p)=\frac43\beta-\frac{16}{9}\beta^2p+O(\beta^3),\qquad
\lambda_\beta=-\frac43\beta^2+O(\beta^3).}
\tag{2.1}
\]
The remainder is a perturbative remainder on the compact one-face rotor; this note does not supply an explicit numerical bound for it at \(\beta\le2/50000\). In particular, (2.1) must not be substituted into a global activity estimate without a proved remainder bound.

### 2.1 A quantitative uniform remainder on the admissible rotor interval

The perturbative remainder in (2.1) can be made explicit in the sup norm. Define
\[
\langle h\rangle_w:=\frac{2}{\pi}\int_{-1}^1\sqrt{1-p^2}\,h(p)\,dp,\qquad
\lambda(R):=-\langle(1-p^2)R^2\rangle_w.
\]
For weighted-mean-zero \(F\), the regular inverse of
\[
L R:=(1-p^2)R'-3pR=F
\]
is
\[
(TF)(p):=(1-p^2)^{-3/2}
\int_{-1}^p\sqrt{1-u^2}\,F(u)\,du.
\]
The zero-mean condition permits replacing the integral by minus the tail integral from \(p\) to \(1\). The elementary inequality
\[
\min\left\{\int_{-1}^p\sqrt{1-u^2}\,du,\,
\int_p^1\sqrt{1-u^2}\,du\right\}
\le\frac{\pi}{4}(1-p^2)^{3/2}
\]
follows by differentiating the difference on each half-interval. Hence
\[
\|TF\|_\infty\le\frac{\pi}{4}\|F\|_\infty.
\tag{2.2}
\]
The fixed-point equation is
\[
R=T\left[-4\{(1-p^2)R^2+\beta p+\lambda(R)\}\right].
\tag{2.3}
\]
On the ball \(\|R\|_\infty\le r\), the nonlinear part has Lipschitz constant at most \(4\pi r\): indeed
\[
\|(1-p^2)(R^2-S^2)+\lambda(R)-\lambda(S)\|_\infty
\le4r\|R-S\|_\infty.
\]
The already-proved maximum-principle bound \(0\le R_\beta\le2\beta\) places the physical solution in the ball \(r=2\beta\); also \(\|P_\beta\|_\infty\le\frac43\beta+\frac{16}{9}\beta^2<2\beta\) throughout the stated coupling interval.

Now take the second-order polynomial
\[
P_\beta(p)=\frac43\beta-\frac{16}{9}\beta^2p.
\]
Its weighted mean parameter is exactly
\[
\lambda(P_\beta)=-\frac43\beta^2-\frac{32}{81}\beta^4.
\]
A direct polynomial calculation gives the residual
\[
F(P_\beta)-LP_\beta
=\frac{128}{81}\beta^3
\left(8\beta p^4-8\beta p^2+\beta-12p^3+12p\right),
\]
so
\[
\|F(P_\beta)-LP_\beta\|_\infty
\le\frac{128}{81}(24+17\beta)\beta^3.
\]
Using (2.2), the Lipschitz constant \(8\pi\beta\) on the ball \(r=2\beta\), and \(T(LP_\beta)=P_\beta\), we obtain
\[
\boxed{
\|R_\beta-P_\beta\|_\infty
\le
\frac{32\pi}{81}\,
\frac{24+17\beta}{1-8\pi\beta}\,\beta^3.
}
\tag{2.4}
\]
The allocation \(A_f\ge a_0/2\) and \(b_0/a_0\le1/50000\) imply
\(\beta_f\le2b_0/a_0\le4\times10^{-5}\). On this interval the coefficient in (2.4) is less than \(30\), giving the explicit bound
\[
\boxed{
\left\|R_{\beta_f}
-\frac43\beta_f+\frac{16}{9}\beta_f^2p\right\|_\infty
<30\beta_f^3.
}
\tag{2.5}
\]
Thus the displayed two-mode expansion is now controlled in \(L^\infty\) at the PF-I16 coupling scale, rather than being only asymptotic.

**Scope:** (2.5) is not a character-coefficient \(\ell^1\) bound. A small \(L^\infty\) remainder can still have a large Peter–Weyl/projective coefficient sum. The all-orders character-tail norm required by the row-factor interpolation remains open.

## 3. Character form of the vector-valued face gradient

Let \(\chi_m\) denote the SU(2) character of spin \(m/2\), so
\[
\chi_0=1,\qquad \chi_1(p)=2p,\qquad \chi_2(p)=4p^2-1.
\]
Since \(\nabla\chi_1=2\nabla p\) and \(\nabla\chi_2=8p\nabla p\), (2.1) yields
\[
\boxed{
R_\beta(p)\nabla p
=\frac23\beta\,\nabla\chi_1(p)
-\frac29\beta^2\,\nabla\chi_2(p)
+O(\beta^3)\nabla p.
}
\tag{3.1}
\]
Equivalently, each exact character mode obeys
\[
\chi_m(p)=\operatorname{Tr}\pi_{m/2}(H),\qquad
D_e\chi_m(H)[X]
=\operatorname{Tr}\!\left(
\pi_{m/2}(A)\pi_{m/2}(U_e^{\epsilon})
\,d\pi_{m/2}(X_e^{(\epsilon)})
\pi_{m/2}(B)\right),
\tag{3.2}
\]
with the usual unitary inverse-link conversion when \(\epsilon=-1\). Expanding the trace indices gives a finite tensor over the four boundary links for every fixed \(m\). The number and coefficient sum of those tensor terms grow with \(m\); (3.2) alone is not a summable projective-norm estimate.

## 4. Contract the shared-link Lie-algebra index exactly

Use the radius-two SU(2) basis \(T_a\), \(a=1,2,3\), with
\[
[T_a,T_b]=\epsilon_{abc}T_c,\qquad
-\sum_a d\pi_j(T_a)^2=j(j+1)I.
\]
For two character modes of spins \(j,k\), the shared-link derivative contraction is the invariant operator
\[
\Omega_{jk}:=\sum_{a=1}^3d\pi_j(T_a)\otimes d\pi_k(T_a).
\]
On the Clebsch–Gordan summand of total spin \(J\in\{|j-k|,\ldots,j+k\}\),
\[
\Omega_{jk}
=\frac12\{C_j+C_k-C_{\rm tot}\}
\]
where each positive Casimir is (C=-\sum_a d\pi(T_a)^2); hence its eigenvalue is
\[
\omega_{jkJ}
=-\frac12\{J(J+1)-j(j+1)-k(k+1)\}.
\]
Therefore the exact operator norm is
\[
\boxed{
\|\Omega_{jk}\|_{\rm op}
=\frac12\max_{J=|j-k|,\ldots,j+k}
\left|J(J+1)-j(j+1)-k(k+1)\right|.
}
\tag{4.1}
\]
In particular,
\[
\|\Omega_{1/2,1/2}\|_{\rm op}=\frac34,\qquad
\|\Omega_{1/2,1}\|_{\rm op}=1,\qquad
\|\Omega_{1,1}\|_{\rm op}=2.
\tag{4.2}
\]
The orientation signs and adjoint transports for inverse links conjugate the generators unitarily and do not change these norms.

This is the exact contraction-before-absolute-values requested in the previous scope audit. It replaces a blind sum over three Lie-algebra components by a Casimir-coupling operator. It is an operator-norm statement on the representation tensor product; it is NOT, by itself, the coefficient \(\ell^1\) projective norm of the four-link matrix-entry expansion.

## 5. Consequence for the first pair-insertion orders

For a shared link \(e\), write \(W_f=R_{\beta_f}(p_f)\nabla_ep_f\). The pair term is
\[
v_{fg}=2a_e\langle W_f,W_g\rangle
\]
summed over shared links. Its leading character-mode contraction is spin \(1/2\) against spin \(1/2\), with the exact Casimir factor \(3/4\). The next cross-mode contractions are spin \(1/2\) against spin \(1\), with factor \(1\), and spin \(1\) against spin \(1\), with factor \(2\).

At the level of the scalar coefficients in (3.1), the first terms are therefore explicitly identified:
\[
2a_e\left(\frac23\beta_f\right)\left(\frac23\beta_g\right)\Omega_{1/2,1/2},
\]
followed by the two mixed terms with coefficient
\[
2a_e\left(\frac23\right)\left(-\frac29\right)
\beta_f\beta_g^2
\quad\hbox{and}\quad
2a_e\left(-\frac29\right)\left(\frac23\right)
\beta_f^2\beta_g,
\]
and the spin-\(1\)/spin-\(1\) term with coefficient
\[
2a_e\left(\frac{2}{9}\right)^2\beta_f^2\beta_g^2.
\]
These formulas specify the contracted representation modes; to turn them into a projective activity one must still expand the unshared link matrix coefficients, keep the shared-link contraction as a block (rather than taking its entrywise absolute values too early), and sum the full character tail.

## 6. Remaining quantitative obligation

A complete bridge still requires all of the following:

1. A proved uniform bound on the character coefficients of \(R_\beta\), with an explicit weighted sum strong enough to control the four-link tensor projective norm at the PF-I16 activity scale.
2. A tensor-norm estimate for the contracted pair mode that preserves the Casimir block \(\Omega_{jk}\) and controls the remaining private-link matrix coefficients.
3. A rigorous remainder estimate for (2.1) over the full admissible interval, not merely a formal or asymptotic expansion.
4. A recomputation of the centered face/pair activity using that norm, followed by an actual-insertion cross-split QF proof.
5. Only then, the support-sensitive all-orders tree and marked-root cluster summation.

The crude corrected global estimate \(\|q_\beta\|_\infty\le2\beta\) remains valid but does not bound the required projective character tail. The previous sufficient projective majorant failure remains a failure of that majorant, not a lower bound on the true tensor norm.

## 7. Gate disposition

- First two radial character coefficients: **DERIVED**.
- Shared-link Casimir contraction identity: **ESTABLISHED**.
- Uniform all-orders character/projective norm for \(R_\beta\): **OPEN**.
- Actual face/pair tensor activity below \(1/8\): **OPEN**.
- Actual-insertion cross-split QF and support-sensitive all-orders tree: **OPEN**.
- Marked-root sum, quantum KP convergence, interacting-vacuum Poincaré inequality, and continuum mass gap: **OPEN**.

No P0–P5 status is promoted.
