# PF-I16 — Link-by-link shared-path / copied-path interpolation

**Date:** 2026-11-14  
**Status:** exact interpolation identity established; the required one-link interlaced-time covariance estimate remains OPEN. No P0–P5 gate is promoted.  
**Scope:** finite link set, finite row family, stationary independent link path processes.

## 1. Setup and target

Let \(I=J\sqcup K\) be a nontrivial row split. For each row,
\[
A_i(t_i)=\prod_{e\in X_i}f_{i,e}(X_e(t_i)),
\]
where the link paths \(X_e\) are independent stationary copies of link Markov processes. Write
\[
J_e=\{i\in J:e\in X_i\},\qquad K_e=\{i\in K:e\in X_i\},
\qquad E_\times=\{e:J_e\ne\varnothing,\ K_e\ne\varnothing\}.
\]
The desired cross-split quasi-factorization is
\[
\left|\mathbb E\prod_{i\in I}A_i(t_i)
-\mathbb E\prod_{i\in J}A_i(t_i)\,
 \mathbb E\prod_{i\in K}A_i(t_i)\right|
\le C^{|I|}\prod_{i\in I}\|A_i\|_\infty
\sum_{\substack{i\in J,\ j\in K}}
\mathbf1_{\{X_i\cap X_j\ne\varnothing\}}
e^{-\Delta_0|t_i-t_j|}.
\tag{1.1}
\]

## 2. Whole-path coupling interpolation

For each \(e\in E_\times\), let \(\Gamma_{e,\lambda_e}\) be the probability law on a pair of paths \((X_e^J,X_e^K)\):
\[
\Gamma_{e,\lambda}
=\lambda\,\mathcal L(X_e,X_e)
 +(1-\lambda)\,\bigl(\mathcal L(X_e)\otimes\mathcal L(X'_e)\bigr),
\qquad 0\le\lambda\le1.
\tag{2.1}
\]
The mixture selector is sampled once for the entire path. It is not resampled at each observation time. Both coordinate marginals are the original stationary Markov path law for every \(\lambda\), and the temporal dependence within either coordinate path is unchanged.

For links outside \(E_\times\), only the path used by the side on which the link occurs is needed. Define
\[
\begin{aligned}
\mathcal F(\boldsymbol\lambda)
=\mathbb E_{\otimes_{e\in E_\times}\Gamma_{e,\lambda_e}}
\Bigg[
&\prod_{i\in J}\prod_{e\in X_i}f_{i,e}(X_e^J(t_i))\\
&\times\prod_{j\in K}\prod_{e\in X_j}f_{j,e}(X_e^K(t_j))
\Bigg].
\end{aligned}
\tag{2.2}
\]
All other link paths are integrated under their original independent stationary laws.

At the endpoints,
\[
\mathcal F(\mathbf1)=\mathbb E\prod_{i\in I}A_i(t_i),\qquad
\mathcal F(\mathbf0)=
\mathbb E\prod_{i\in J}A_i(t_i)\,
\mathbb E\prod_{j\in K}A_j(t_j).
\tag{2.3}
\]
The second identity uses independence of all link copies across links and between the two sides at \(\boldsymbol\lambda=\mathbf0\).

Fix any ordering \(E_\times=\{e_1,\ldots,e_q\}\). The coordinatewise fundamental theorem of calculus gives the exact telescoping formula
\[
\boxed{
\mathcal F(\mathbf1)-\mathcal F(\mathbf0)
=\sum_{k=1}^{q}\int_0^1
\partial_{\lambda_{e_k}}
\mathcal F(1,\ldots,1,\underbrace{s}_{e_k},0,\ldots,0)\,ds.
}
\tag{2.4}
\]
This is a finite algebraic identity. No mixing estimate has yet been used.

## 3. Exact form of one interpolation derivative

Fix a link \(e\) and condition on every other link path. All factors from links other than \(e\) become scalar coefficients. Put
\[
U_e(x)=\prod_{i\in J_e}f_{i,e}(x(t_i)),\qquad
V_e(x)=\prod_{j\in K_e}f_{j,e}(x(t_j)).
\tag{3.1}
\]
Differentiating the affine path-law mixture (2.1) gives
\[
\begin{aligned}
\partial_{\lambda_e}\mathcal F
&=\mathbb E_{\text{other links}}\!\left[
C_{\ne e}\left\{
\mathbb E_{\nu_e}[U_e(X)V_e(X)]
-\mathbb E_{\nu_e}U_e(X)\,\mathbb E_{\nu_e}V_e(X)
\right\}\right]\\
&=\mathbb E_{\text{other links}}\!
\left[C_{\ne e}\operatorname{Cov}_{\nu_e}(U_e(X),V_e(X))\right],
\end{aligned}
\tag{3.2}
\]
where
\[
|C_{\ne e}|
\le\prod_{i\in I}\prod_{\substack{e'\in X_i\\e'\ne e}}
\|f_{i,e'}\|_\infty.
\tag{3.3}
\]
In particular, the derivative does not involve a cumulant over the other links. The other links enter only through a bounded multiplier.

Thus (1.1) follows if one proves the following one-link lemma with a constant independent of the link state space and time horizon.

## 4. The precise one-link lemma still required

Let \(X_t\) be a stationary Markov process whose semigroup satisfies
\[
P_t=\Pi+Q_t,\qquad \|Q_t\|_{2\to2}\le e^{-\Delta_0t}.
\tag{4.1}
\]
For arbitrary finite disjoint index sets \(J_e,K_e\), arbitrary (not necessarily ordered or contiguous) observation times, and bounded one-time multiplication functions, prove
\[
\boxed{
\left|\operatorname{Cov}\left(
\prod_{i\in J_e}f_i(X_{t_i}),
\prod_{j\in K_e}g_j(X_{t_j})
\right)\right|
\le C_1^{|J_e|+|K_e|}
\left(\prod_i\|f_i\|_\infty\right)
\left(\prod_j\|g_j\|_\infty\right)
\sum_{\substack{i\in J_e\\j\in K_e}}
e^{-\Delta_0|t_i-t_j|}.
}
\tag{4.2}
\]
The times may be interlaced in any order. A proof only for two separated time blocks is insufficient.

If (4.2) holds, substituting it into (2.4), using (3.3), and summing first over links gives (1.1), with a changed exponential constant. Indeed, each cross pair \((i,j)\) is counted once for each shared link; this is exactly the multiplicity represented by the sum over \(e\in X_i\cap X_j\).

## 5. Why this is a real reduction, not yet a proof

1. **Whole paths are essential.** Replacing (2.1) by independent mixture selectors at each time changes the joint path law and does not interpolate between the two desired endpoints while preserving each side's Markov path law.

2. **The two-block mixing inequality does not immediately apply.** If all \(J_e\)-times precede all \(K_e\)-times, (4.2) follows from the usual \(L^2\) semigroup contraction across the separating time gap. For interlaced times, both products depend on observations on both sides of every temporal cut. Conditioning at one cut does not make either whole product measurable on just one side.

3. **The global projection-tree estimate is not enough pointwise.** Its complete-graph tree sum has \(n^{n-2}\) labeled trees. Extracting one cross edge termwise leaves a superexponential tree-count factor, not the \(C_1^n\) coefficient in (4.2). The normalized time-integrated bound from the projection-tree theorem is useful for the Feynman–Kac coefficient, but it does not imply this pointwise cross-split estimate.

4. **The interpolation is still useful without (4.2).** It proves that all spatial dependence across the row split is mediated by shared links, and it isolates the entire temporal difficulty in a single-link path covariance. It also avoids taking absolute values of Leonov–Shiryaev slot-partition fibers.

## 6. Current conclusion and next proof obligation

The link-by-link interpolation (2.1)–(2.4) and derivative identity (3.2) are exact. They reduce the many-link QF claim to (4.2). The one-link interlaced-time covariance lemma is **not** established in this audit. No support-sensitive joint tree, all-orders QF, KP convergence, interacting-vacuum inequality, or continuum mass gap follows until (4.2) is proved (or a counterexample identifies a necessary stronger hypothesis).

**Gate status:** exact interpolation — established; one-link interlaced-time covariance — OPEN; cross-split QF — OPEN; all P0–P5 gates unchanged.
