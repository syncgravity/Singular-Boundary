# PF-I16 — Link-by-link shared-path / copied-path interpolation

**Date:** 2026-11-14  
**Status:** exact whole-path interpolation and the one-link interlaced-time covariance lemma are ESTABLISHED under the stated stationary Markov L2-gap hypothesis. The many-link QF consequence is established for bounded row-factor observables. No P0–P5 gate is promoted.  
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

## 4. One-link interlaced-time covariance lemma — proved

Let \(X_t\) be a stationary Markov process whose semigroup satisfies
\[
P_t=\Pi+Q_t,\qquad \|Q_t\|_{2\to2}\le e^{-\Delta_0t}.
\tag{4.1}
\]
For arbitrary finite disjoint index sets \(J_e,K_e\), arbitrary (not necessarily ordered or contiguous) observation times, and bounded one-time multiplication functions, we prove
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

## 5. Proof of the interlaced-time covariance estimate

Write the \(n=|J_e|+|K_e|\) observation times in nondecreasing order
\[
s_1\le s_2\le\cdots\le s_n.
\]
Ties may be ordered arbitrarily; the corresponding gap is zero. Let \(h_\ell\) be the one-time factor at \(s_\ell\), and colour the index \(\ell\) by \(J\) or \(K\) according to its side. Put
\[
U=\prod_{\ell:\,c_\ell=J}h_\ell(X_{s_\ell}),\qquad
V=\prod_{\ell:\,c_\ell=K}h_\ell(X_{s_\ell}),\qquad
M=\prod_{\ell=1}^n\|h_\ell\|_\infty.
\]
The target cross-pair sum is
\[
S=\sum_{\substack{a:\,c_a=J\\b:\,c_b=K}}
e^{-\Delta_0|s_a-s_b|}.
\]

### 5.1 First-colour-change decomposition

Let \(k\) be the first index whose colour differs from \(c_1\). After exchanging the names \(J,K\) if necessary, assume
\[
c_1=\cdots=c_{k-1}=J,\qquad c_k=K.
\]
Set
\[
A=\prod_{\ell<k}h_\ell(X_{s_\ell}),\qquad
B=\prod_{\substack{\ell>k\\c_\ell=J}}h_\ell(X_{s_\ell}),\qquad
C=\prod_{\substack{\ell\ge k\\c_\ell=K}}h_\ell(X_{s_\ell}).
\]
Then \(U=AB\), \(V=C\). Crucially, \(A\) is measurable through time \(s_{k-1}\), while both \(B\) and \(C\) use only times at or after \(s_k\). The exact covariance identity
\[
\boxed{
\operatorname{Cov}(AB,C)
=\operatorname{Cov}(A,BC)
+\mathbb E[A]\operatorname{Cov}(B,C)
-\operatorname{Cov}(A,B)\mathbb E[C]
}
\tag{5.1}
\]
follows by expanding the three covariances.

### 5.2 Apply the ordinary separated-past/future estimate twice

For bounded past-measurable \(D\) through time \(s\) and bounded future-measurable \(E\) from time \(s+\delta\) onward, stationarity, the Markov property, and the L2 gap give
\[
|\operatorname{Cov}(D,E)|
\le e^{-\Delta_0\delta}\|D\|_\infty\|E\|_\infty.
\tag{5.2}
\]
Indeed, with \(\psi(x)=\mathbb E[E\mid X_{s+\delta}=x]\),
\[
\operatorname{Cov}(D,E)
=\langle D-\mathbb ED,\,
P_\delta(\psi-\nu\psi)\rangle_\nu,
\]
and both centered L2 norms are bounded by the corresponding sup norms.

Take \(\delta=s_k-s_{k-1}\). Applying (5.2) to \((A,BC)\) and \((A,B)\) in (5.1) gives
\[
|\operatorname{Cov}(U,V)|
\le 2M e^{-\Delta_0(s_k-s_{k-1})}
+\|A\|_\infty|\operatorname{Cov}(B,C)|.
\tag{5.3}
\]
The boundary pair \((k-1,k)\) has opposite colours, so its weight
\(e^{-\Delta_0(s_k-s_{k-1})}\) is one of the summands of \(S\).

If \(B=1\), the remaining covariance is zero and the proof is complete. Otherwise \(B,C\) involve a strictly smaller family of rows, all lying in the suffix \(\{k,\ldots,n\}\). Let \(S_{\rm suf}\) be its cross-pair sum. It is a sub-sum of \(S\), and the induction hypothesis applies to it.

### 5.3 Induction and constant

For \(n=2\), (5.2) directly gives
\[
|\operatorname{Cov}(U,V)|\le M S,
\]
so take \(C_2=1\). If the estimate holds at all smaller orders with coefficient \(C_{n-1}\), then (5.3), the boundary-pair observation, and \(S_{\rm suf}\le S\) yield
\[
|\operatorname{Cov}(U,V)|
\le (2+C_{n-1})MS.
\]
Thus one may take
\[
C_n=2n-3\qquad(n\ge2).
\]
In particular \(2n-3\le 2^n\), so the requested exponential form holds. We have proved the sharper bound
\[
\boxed{
|\operatorname{Cov}(U,V)|
\le (2n-3)\prod_{\ell=1}^n\|h_\ell\|_\infty
\sum_{\substack{a:\,c_a=J\\b:\,c_b=K}}
e^{-\Delta_0|s_a-s_b|}.
}
\tag{5.4}
\]
This proof permits arbitrary interlacing, arbitrary repeated times, and nonreversible stationary Markov semigroups. It uses only the stated \(L^2(\nu)\) contraction on mean-zero functions.

## 6. Consequence for the link-by-link QF interpolation

Apply (5.4) to the two groups of factors on each shared link \(e\), with \(n_e=|J_e|+|K_e|\). Since \(n_e\le |I|\), its coefficient is at most \(2|I|\). In the derivative (3.2), the other-link factors contribute only their sup norms. Integrating (2.4) and summing over shared links therefore gives the cross-split quasi-factorization (1.1), with a global coefficient bounded by \(2|I|\) times the row-factor normalization. If one prefers the original exponential notation, \(2|I|\le 2^{|I|+1}\) absorbs this into \(C^{|I|}\) for a fixed numerical \(C\).

More explicitly, for row-factor observables \(A_i=\prod_{e\in X_i}f_{i,e}\), the linkwise derivative contributes
\[
2|I|\prod_{i,e}\|f_{i,e}\|_\infty
\sum_{\substack{i\in J,j\in K\\e\in X_i\cap X_j}}
e^{-\Delta_0|t_i-t_j|}.
\]
Thus the shared-link indicator and temporal bond are obtained with no partition-fiber or tree-count loss.

## 7. Scope and remaining obligations

The one-link interlaced-time covariance lemma and the corresponding link-by-link cross-split QF estimate are now proved for bounded row-factor observables under independent stationary link paths with the uniform \(L^2\) semigroup gap. This does **not** by itself prove the all-orders support-sensitive cumulant tree, the marked-root/cluster sum, quantum connected-resolvent convergence, the interacting-vacuum Poincare inequality, or the continuum mass gap. The hypotheses must also be checked for the actual reference link processes used by the PF-I16 construction.

**Gate status:** exact path interpolation — ESTABLISHED; one-link interlaced-time covariance — ESTABLISHED; row-factor cross-split QF — ESTABLISHED under the stated product-Markov hypotheses; all P0–P5 gate statuses unchanged.
