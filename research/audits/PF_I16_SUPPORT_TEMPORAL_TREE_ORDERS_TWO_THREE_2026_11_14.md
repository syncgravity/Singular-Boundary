# PF-I16 — Support-restricted temporal cumulant tree at orders two and three

**Date:** 2026-11-14  
**Status:** ESTABLISHED for cumulant orders two and three under the independent stationary link-path hypotheses. All-orders support-restricted temporal tree remains OPEN.  
**Scope:** finite link family; independent stationary Markov link paths with \(\|P_t^e-\Pi_e\|_{2\to2}\le e^{-\Delta_0t}\). No P0–P5 gate is promoted.

## 1. Statement

Let
\[
A_i(t_i)=F_i((X_e(t_i))_{e\in X_i}),\qquad \|F_i\|_\infty\le M_i,
\]
where the link paths are independent and stationary and each link semigroup has mean-zero \(L^2\) contraction at least \(\Delta_0\). Let \(G_X\) be the row support-overlap graph. For \(r=2,3\),
\[
\boxed{
|\kappa(A_1(t_1),\ldots,A_r(t_r))|
\le 4^r\Bigl(\prod_iM_i\Bigr)
\sum_{T\in\mathcal T(G_X)}
\prod_{\{i,j\}\in T}e^{-\Delta_0|t_i-t_j|}.
}
\tag{1.1}
\]
If \(G_X\) is disconnected, the cumulant is exactly zero. The constant \(4^r\) is deliberately inherited from the already-established global product-process projection-tree estimate; it is not claimed optimal.

## 2. Proof for two rows

If the supports are disjoint, the two row processes are independent and the covariance vanishes. Otherwise \(G_X=K_2\). The global product-process tensor-gap bridge gives
\[
|\kappa(A_1(t_1),A_2(t_2))|
\le 4^2M_1M_2e^{-\Delta_0|t_1-t_2|},
\]
which is exactly (1.1).

## 3. Proof for three rows

If \(G_X\) is disconnected, independence across disjoint link-path coordinate families gives zero cumulant.

If \(G_X=K_3\), the global product-process estimate gives
\[
|\kappa(A_1,A_2,A_3)|
\le 4^3M_1M_2M_3
\sum_{T\in\mathcal T(K_3)}
\prod_{ij\in T}e^{-\Delta_0|t_i-t_j|},
\]
and \(G_X=K_3\), so this is (1.1).

It remains to consider the path graph. Relabel its vertices so that
\[
X_1\cap X_3=\varnothing,\qquad
A:=X_1\cap X_2\ne\varnothing,\qquad
B:=X_2\cap X_3\ne\varnothing.
\]
The sets \(A,B\) are disjoint. Every link in \(A\) is used by rows 1 and 2 only; every link in \(B\) is used by rows 2 and 3 only. All remaining links are private to one of the three rows.

Integrate the private link coordinates out of each row observable under their stationary one-time laws. This produces bounded functions
\[
f_1(X_A(t_1)),\quad
f_2(X_A(t_2),X_B(t_2)),\quad
f_3(X_B(t_3)),
\]
with respective sup norms at most \(M_1,M_2,M_3\). The two path processes \(X_A\) and \(X_B\) are independent. Their product semigroups inherit the same gap \(\Delta_0\): on every nonconstant tensor sector at least one link coordinate is mean-zero, so the tensor-product contraction is at most \(e^{-\Delta_0s}\).

Write \(\mu_i=\mathbb E f_i\), and set
\[
\alpha(X_A(t_2))
=\mathbb E[f_1(X_A(t_1))-\mu_1\mid X_A(t_2)],
\]
\[
\beta(X_B(t_2))
=\mathbb E[f_3(X_B(t_3))-\mu_3\mid X_B(t_2)].
\]
The stationary reverse semigroup is the adjoint semigroup and has the same \(L^2\) operator norm. Thus, whether \(t_i\) is before or after \(t_2\),
\[
\|\alpha\|_2\le e^{-\Delta_0|t_1-t_2|}M_1,
\qquad
\|\beta\|_2\le e^{-\Delta_0|t_3-t_2|}M_3.
\tag{3.1}
\]
For three variables the joint cumulant is the expectation of the product of their centered versions. Since rows 1 and 3 depend on disjoint link-path families, they are independent; consequently the \(\mu_2\) term drops. Conditioning on the two independent middle-time states gives the exact identity
\[
\kappa(A_1,A_2,A_3)
=\mathbb E\bigl[
\alpha(X_A(t_2))\,
f_2(X_A(t_2),X_B(t_2))\,
\beta(X_B(t_2))
\bigr].
\tag{3.2}
\]
Using independence of \(X_A(t_2)\) and \(X_B(t_2)\), followed by Cauchy–Schwarz,
\[
\begin{aligned}
|\kappa(A_1,A_2,A_3)|
&\le M_2\,\mathbb E|\alpha|\,\mathbb E|\beta|\\
&\le M_1M_2M_3
e^{-\Delta_0(|t_1-t_2|+|t_3-t_2|)}.
\end{aligned}
\tag{3.3}
\]
The path graph has exactly one spanning tree, with edges \(12\) and \(23\). Therefore (3.3) is stronger than (1.1), and completes the order-three case.

## 4. What this closes

- Support-restricted temporal tree estimate for \(r=2,3\): **ESTABLISHED**.
- The path-graph order-three case has coefficient 1, not merely \(4^3\).
- The triangle case follows from the established global product-process projection-tree theorem because the support graph is already complete.
- The proof handles arbitrary bounded local multiplication observables; it does not require a Peter–Weyl/projective decomposition.
- The proof uses the full product Markov path structure, not cross-split QF alone.

## 5. What remains open

For \(r\ge4\), a connected support graph can be neither a path nor complete. The preceding argument does not extend by a simple leaf induction: after conditioning or integrating out a leaf, the resulting conditional observable is generally only controlled in \(L^2\), and the higher-order cumulant does not reduce to a product of one-edge contractions. A valid induction must preserve the signed cumulant structure and avoid a factorial loss.

The remaining target is still
\[
|\kappa(A_1(t_1),\ldots,A_r(t_r))|
\le C^r\prod_iM_i
\sum_{T\in\mathcal T(G_X)}
\prod_{ij\in T}e^{-\Delta_0|t_i-t_j|},
\qquad r\ge4.
\]
The all-orders complete-graph temporal tree, arbitrary-time unweighted support-tree count, cross-split QF, and termwise support-temporal tree extraction do not by themselves prove this joint support-restricted estimate.

Marked-root spatial summation, quantum KP convergence, the interacting-vacuum Poincare inequality, and the continuum mass gap remain **OPEN**. No P0–P5 status is promoted.

## 6. Verification

The companion finite-state verifier exhausts all sign-valued functions on a two-state path-product model for several rational reset rates and time gaps. It checks the exact conditional-expectation identity and the bound (3.3). This is a regression check for the special-case calculation, not a substitute for the analytic proof above.
