# PF-I16 — Link-compressed support-graph forest interpolation

**Date:** 2026-11-16  
**Status:** exact support-graph interpolation and projective consistency ESTABLISHED; uniform differentiated-cumulant bound OPEN  
**Scope:** one-time monomial rows built from independent stationary link Markov chains. No P0–P5 gate is promoted.

## 1. Purpose

The complete-product-process interpolation loses link labels. The earlier global BKAR interpolation also assigns parameters to temporal row-pairs that need not share a link. This construction keeps the interpolation on the actual support-overlap graph and compresses each link chain to its incident rows before interpolating.

Let the rows be
\[
A_i(t_i)=\prod_{e\in X_i}f_{i,e}(X_e(t_i)),\qquad i\in[R],
\]
where the link paths \(X_e\) are independent and stationary. Put
\[
G_X=([R],E_X),\qquad
ij\in E_X\Longleftrightarrow X_i\cap X_j\ne\varnothing.
\]
For each link \(e\), list its incident rows in temporal order:
\[
I_e=\{i_1,\ldots,i_{k_e}\},\qquad
t_{i_1}\le\cdots\le t_{i_{k_e}}.
\]
Ties are broken by row index. Consecutive rows in this list share \(e\), hence form edges of \(G_X\).

Assume
\[
P_t^e=\Pi_e+Q_t^e,\qquad
Q_s^eQ_t^e=Q_{s+t}^e,\qquad
Q_t^e\Pi_e=\Pi_eQ_t^e=0,\qquad
\|Q_t^e\|_{2\to2}\le e^{-\Delta_0t}.
\]

## 2. Definition of the interpolation

For every support edge \(ij\in E_X\), introduce \(\lambda_{ij}\in[0,1]\). For each link \(e\), and each consecutive pair \(i_a,i_{a+1}\) in \(I_e\), replace its transition by
\[
K^e_{i_ai_{a+1}}(\lambda)
=\Pi_e+\lambda_{i_ai_{a+1}}Q^e_{|t_{i_{a+1}}-t_{i_a}|}
=(1-\lambda_{i_ai_{a+1}})\Pi_e+
\lambda_{i_ai_{a+1}}P^e_{|t_{i_{a+1}}-t_{i_a}|}.
\tag{2.1}
\]
This is a Markov kernel for every \(\lambda\in[0,1]^{E_X}\). Keep the stationary initial law at the first incident row. The link chains remain independent across \(e\), so (2.1) defines a genuine joint law of all row variables \(A_i^\lambda\).

Let
\[
\Phi(\lambda)=\kappa(A_1^\lambda,\ldots,A_R^\lambda).
\]
At \(\lambda=\mathbf1\), every link chain has its original transitions, so \(\Phi(\mathbf1)\) is the desired cumulant.

## 3. Projective consistency under omitted rows

The construction is not merely a collection of unrelated moment interpolations. If a moment uses only a subset \(B\subseteq[R]\) of the rows, then all omitted incident rows act as the identity in the corresponding link coordinate. For consecutive selected incident rows \(i_a,i_b\), with \(a<b\), the effective transition is the product
\[
\begin{aligned}
K^e_{i_ai_{a+1}}\cdots K^e_{i_{b-1}i_b}
&=\prod_{c=a}^{b-1}(\Pi_e+\lambda_{i_ci_{c+1}}Q^e_{d_c})\\
&=\Pi_e+
\left(\prod_{c=a}^{b-1}\lambda_{i_ci_{c+1}}\right)
Q^e_{\sum_{c=a}^{b-1}d_c}\\
&=\Pi_e+
\left(\prod_{c=a}^{b-1}\lambda_{i_ci_{c+1}}\right)
Q^e_{|t_{i_b}-t_{i_a}|},
\end{aligned}
\tag{3.1}
\]
where \(d_c=t_{i_{c+1}}-t_{i_c}\). The second equality uses
\(\Pi Q=Q\Pi=0\), \(\Pi^2=\Pi\), and \(Q_sQ_t=Q_{s+t}\).

Thus every subset moment is the marginal of the same interpolated link-chain law. In particular, if intermediate rows are omitted, the effective interpolation parameter is the product of the intervening consecutive-port parameters. This is the consistency condition that fails for an interpolation which independently assigns \(\lambda_{ij}\) to every pair of selected rows.

## 4. Disconnected-parameter vanishing on the support graph

Let \(G_\lambda\) be the graph on \([R]\) consisting of support edges with \(\lambda_{ij}>0\). If \(G_\lambda\) is disconnected, rows in different components are independent under the interpolated law.

Indeed, fix a link \(e\). Its incident rows \(I_e\) form a clique in \(G_X\). If \(I_e\) meets two different components of \(G_\lambda\), then somewhere in the temporally ordered list \(I_e\) two consecutive rows lie in different components. Their parameter is zero, and the corresponding transition in (2.1) is \(\Pi_e\), which resets the link chain to an independent stationary state. The link path therefore splits into independent segments, each assigned to one component of \(G_\lambda\). If \(I_e\) lies in one component, it contributes only to that component. Since link paths are independent, the full row families indexed by distinct components of \(G_\lambda\) are independent.

Consequently,
\[
\boxed{\Phi(\lambda)=0\quad\text{whenever }G_\lambda
\text{ is disconnected}.}
\tag{4.1}
\]

This is an exact factorization statement, not a covariance estimate.

## 5. Support-graph BKAR reduction

The forest formula applied to \(\Phi\) on the edge set \(E_X\), using (4.1), leaves only spanning trees of the support graph:
\[
\boxed{
\Phi(\mathbf1)=
\sum_{T\in\mathcal T(G_X)}
\int_{[0,1]^T}
(\partial_T\Phi)(\lambda^T(s))\,ds.
}
\tag{5.1}
\]
Here \(\lambda^T_{ij}(s)\) is the minimum of the edge parameters along the unique \(T\)-path from \(i\) to \(j\), for \(ij\in E_X\). Non-spanning forests vanish because their positive-parameter support graph is disconnected.

Thus the combinatorial tree index is already the correct support graph. No completion edge between rows with disjoint link supports is introduced.

## 6. What one derivative inserts

A parameter \(\lambda_{ij}\) occurs in the interpolated law only on transitions of links \(e\in X_i\cap X_j\) for which \(i,j\) are consecutive in \(I_e\). There are at most
\[
|X_i\cap X_j|\le \min(|X_i|,|X_j|)\le m
\]
such link transitions when every row has support size at most \(m\).

Differentiating one such transition replaces \(K^e_{ij}\) by
\[
Q^e_{|t_i-t_j|},
\qquad
\|Q^e_{|t_i-t_j|}\|_{2\to2}
\le e^{-\Delta_0|t_i-t_j|}.
\tag{6.1}
\]
For any fixed moment term, a mixed derivative along a tree therefore selects one of at most \(m\) link coordinates for each tree edge. The selected operator insertions carry exactly the desired support-edge temporal factors.

The remaining issue is the signed moment-cumulant sum. A derivative of \(\Phi\) is not simply a derivative of the full joint moment: the product-rule terms in the moment-cumulant formula include derivatives of lower block moments, including blocks that omit one or both row labels \(i,j\). Equation (3.1) explains these terms projectively, but does not cancel them automatically.

## 7. Exact analytic obligation

A sufficient estimate for (5.1) is
\[
\boxed{
\sup_{\lambda\in[0,1]^{E_X}}
|\partial_T\Phi(\lambda)|
\le C_m^R
\left(\prod_i\prod_{e\in X_i}\|f_{i,e}\|_\infty\right)
\prod_{\{i,j\}\in T}e^{-\Delta_*|t_i-t_j|}
}
\tag{7.1}
\]
for every support spanning tree \(T\), with \(C_m\) independent of \(R\), the number of links, and the time horizon. Inserting (7.1) into (5.1) would prove the desired support-tree-sum cumulant bound.

The direct absolute-value estimate of the differentiated moment-cumulant formula is not enough: it reintroduces the factorial partition coefficient. The missing step is a cancellation-preserving bound on the differentiated cumulant, uniform over the support-graph interpolation.

## 8. Status

Established:
- a genuine interpolated probability law on independent link chains;
- exact projective consistency for every subset of rows;
- exact vanishing of the cumulant whenever the positive-parameter support graph is disconnected;
- a BKAR spanning-tree reduction indexed only by \(\mathcal T(G_X)\);
- each differentiated support edge inserts a shared-link \(Q\)-operator with the correct temporal decay.

Open:
- the exponential-in-\(R\) differentiated-cumulant estimate (7.1);
- the resulting noncoincident-time support-tree-sum inequality;
- marked-root spatial summation and KP convergence;
- interacting-vacuum Poincaré inequality, physical scale setting, and continuum mass gap.

This is a sharper reduction than the earlier complete-graph BKAR route, but it is not yet the desired cumulant theorem. No P0–P5 gate is promoted.
