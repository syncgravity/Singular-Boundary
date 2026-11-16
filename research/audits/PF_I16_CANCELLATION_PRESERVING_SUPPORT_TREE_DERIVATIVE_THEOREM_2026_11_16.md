# PF-I16 — Cancellation-preserving derivative identity and support-localized cumulant tree

**Date:** 2026-11-16  
**Status:** THEOREM ESTABLISHED under the stated independent-link \(L^2\)-gap hypotheses  
**Scope:** one-time monomial rows; this result closes the differentiated-cumulant obstacle in the link-compressed support-graph BKAR construction. It does not close the Yang–Mills mass-gap proof.

## 1. Setup and hypotheses

Let \((X_e(t))_{t\in\mathbb R}\), \(e\in\mathcal E\), be independent stationary Markov processes with invariant probabilities \(\mu_e\) and transition semigroups \(P_t^e\). Write
\[
\Pi_e f=\int f\,d\mu_e,\qquad Q_t^e=P_t^e-\Pi_e.
\]
Assume, for every link \(e\),
\[
P_s^eP_t^e=P_{s+t}^e,\quad P_t^e\Pi_e=\Pi_eP_t^e=\Pi_e,\quad
\|Q_t^e\|_{L^2(\mu_e)\to L^2(\mu_e)}\le e^{-\Delta_0t}
\tag{1.1}
\]
for all \(s,t\ge0\), with a common \(\Delta_0>0\).

For rows \(i=1,\ldots,R\), let
\[
A_i(t_i)=\prod_{e\in X_i}f_{i,e}(X_e(t_i)),\qquad
\|f_{i,e}\|_\infty<\infty,
\]
and assume the row link-incidence bound
\[
|X_i|\le m<\infty.
\tag{1.2}
\]
The support graph is
\[
G_X=([R],E_X),\qquad ij\in E_X\iff X_i\cap X_j\ne\varnothing.
\]
If \(G_X\) is disconnected, the row families in its distinct components depend on disjoint independent link paths, so the joint cumulant is zero. Hence assume \(G_X\) connected.

For each link \(e\), order its incident rows \(I_e=\{i_1,\ldots,i_{k_e}\}\) by nondecreasing \(t_i\), breaking ties by row index. Only consecutive pairs in this list receive a transition parameter. For every support edge \(ij\in E_X\), introduce one parameter \(\lambda_{ij}\in[0,1]\), shared across all links for which \(i,j\) are consecutive in \(I_e\), and set
\[
K^e_{ij}(\lambda)=\Pi_e+\lambda_{ij}Q^e_{|t_i-t_j|}
=(1-\lambda_{ij})\Pi_e+\lambda_{ij}P^e_{|t_i-t_j|}.
\tag{1.3}
\]
Each \(K^e_{ij}\) is a stationary Markov operator and an \(L^2(\mu_e)\) contraction. These transitions define independent interpolated link chains. Let \(\mathbb E_\lambda\) denote expectation under their joint law and
\[
\Phi(\lambda)=\kappa_\lambda(A_1,\ldots,A_R).
\]

## 2. The cancellation identity

For \(B\subseteq[R]\), write
\[
M_B(\lambda)=\mathbb E_\lambda\prod_{i\in B}A_i.
\]
The marginal \(M_B\) is independent of \(\lambda_{ij}\) unless \(i,j\in B\).

To see this, consider one link \(e\). If both endpoints of a parameterized transition are retained in the selected row set \(B\), that transition occurs in the compressed marginal chain. If one endpoint is omitted, integrating out that endpoint composes adjacent transitions; stationarity removes a transition before the first retained port and preservation of constants removes one after the last retained port. More explicitly, the semigroup/reset identity
\[
(\Pi+\lambda_1Q_{d_1})\cdots(\Pi+\lambda_kQ_{d_k})
=\Pi+\left(\prod_{a=1}^k\lambda_a\right)Q_{\sum_a d_a}
\tag{2.1}
\]
shows that a parameter on the transition \(i\to j\), where \(i,j\) are consecutive in the full incident-row list, survives in a selected marginal only if both \(i,j\) are selected. Since links are independent, the same is true of \(M_B\).

The moment-cumulant formula is
\[
\Phi(\lambda)=
\sum_{\pi\in\Pi([R])}
(-1)^{|\pi|-1}(|\pi|-1)!
\prod_{B\in\pi}M_B(\lambda).
\tag{2.2}
\]
Let \(T\) be any spanning tree of \(G_X\), and let
\(\partial_T=\prod_{\{i,j\}\in T}\partial_{\lambda_{ij}}\).
For a fixed partition \(\pi\), the product \(\prod_{B\in\pi}M_B\) can have a nonzero mixed derivative \(\partial_T\) only if the endpoints of every edge of \(T\) lie in one common block of \(\pi\). Because \(T\) is connected, this forces all \(R\) vertices into a single block, i.e. \(\pi=\{[R]\}\). Every other partition term has zero mixed derivative. The coefficient of the one-block partition is \(+1\). Therefore the exact identity is
\[
\boxed{\partial_T\Phi(\lambda)
=\partial_T M_{[R]}(\lambda)
=\partial_T\mathbb E_\lambda\prod_{i=1}^R A_i.}
\tag{2.3}
\]
This is the cancellation-preserving step: the differentiated cumulant has no residual partition sum.

## 3. Linkwise operator bound for a mixed derivative

Independence of the link paths gives the full joint moment factorization
\[
M_{[R]}(\lambda)=\prod_{e\in\cup_iX_i}M_e(\lambda),
\tag{3.1}
\]
where, if \(I_e=(i_1,\ldots,i_{k_e})\),
\[
M_e(\lambda)=
\left\langle 1,\,
M_{f_{i_1,e}}K^e_{i_1i_2}(\lambda)M_{f_{i_2,e}}
\cdots
K^e_{i_{k_e-1}i_{k_e}}(\lambda)M_{f_{i_{k_e},e}}1
\right\rangle_{L^2(\mu_e)}.
\tag{3.2}
\]
Here \(M_f\) denotes multiplication by \(f\).

Apply the product rule to \(\partial_T\prod_eM_e\). Each tree edge \(ij\) is assigned to exactly one link factor \(M_e\) on which \(\lambda_{ij}\) occurs. Such a link must satisfy \(e\in X_i\cap X_j\) and \(i,j\) consecutive in \(I_e\). There are at most
\[
|X_i\cap X_j|\le m
\tag{3.3}
\]
choices for each tree edge. Thus the number of nonzero assignments is at most \(m^{R-1}\).

For a fixed assignment, several differentiated edges may be assigned to the same link \(e\). In (3.2), differentiating with respect to \(\lambda_{ij}\) replaces the corresponding transition \(K^e_{ij}\) by
\[
Q^e_{|t_i-t_j|}.
\]
Every undifferentiated transition \(K^e_{ij}(\lambda)\) is an \(L^2(\mu_e)\) contraction, every multiplication operator has norm at most \(\|f_{i,e}\|_\infty\), and \(\|1\|_2=1\). By submultiplicativity and (1.1), the absolute value of this differentiated link factor is at most
\[
\left(\prod_{i\in I_e}\|f_{i,e}\|_\infty\right)
\prod_{\substack{\{i,j\}\in T\\\text{assigned to }e}}
e^{-\Delta_0|t_i-t_j|}.
\tag{3.4}
\]
This remains valid when multiple \(Q\)-insertions occur in the same link chain: each insertion contributes its own operator norm factor.

Multiplying (3.4) over links and summing over at most \(m^{R-1}\) assignments gives, uniformly in \(\lambda\in[0,1]^{E_X}\),
\[
\boxed{
|\partial_T\Phi(\lambda)|
\le m^{R-1}
\left(\prod_{i=1}^R\prod_{e\in X_i}\|f_{i,e}\|_\infty\right)
\prod_{\{i,j\}\in T}e^{-\Delta_0|t_i-t_j|}.
}
\tag{3.5}
\]

## 4. Support-graph BKAR and the theorem

The link-compressed interpolation has the exact disconnection property: if the graph formed by the positive parameters \(\lambda_{ij}>0\) is disconnected, every link chain crossing between two components has a zero-parameter reset between consecutive incident rows. The link paths, and hence row families, split independently across components. Therefore \(\Phi(\lambda)=0\) on every disconnected parameter graph.

Apply the BKAR forest formula on the finite graph \(G_X\). All non-spanning forests have disconnected positive-parameter support and vanish. Thus
\[
\Phi(\mathbf1)=
\sum_{T\in\mathcal T(G_X)}
\int_{[0,1]^T}
(\partial_T\Phi)(\lambda^T(s))\,ds.
\tag{4.1}
\]
Using (3.5), and the unit volume of each tree-parameter cube, yields the theorem.

### Theorem (one-time monomial support-localized cumulant tree)

Under (1.1)–(1.2), for every \(R\ge2\),
\[
\boxed{
\begin{aligned}
|\kappa(A_1(t_1),\ldots,A_R(t_R))|
&\le m^{R-1}
\left(\prod_{i=1}^R\prod_{e\in X_i}\|f_{i,e}\|_\infty\right)\\
&\quad\times
\sum_{T\in\mathcal T(G_X)}
\prod_{\{i,j\}\in T}e^{-\Delta_0|t_i-t_j|}.
\end{aligned}}
\tag{4.2}
\]
For disconnected \(G_X\), the cumulant is zero and the right-hand tree sum is interpreted as zero. For \(R=1\), the estimate is simply \(|\mathbb E A_1|\le\prod_{e\in X_1}\|f_{1,e}\|_\infty\).

The coefficient is \(m^{R-1}\), independent of the total number of links, the number of repeated support types elsewhere in the system, and the time horizon. In particular, it is exponential in \(R\) for fixed row-incidence bound \(m\).

## 5. Scope and remaining obligations

This closes the differentiated-cumulant obstacle for **one-time monomial rows** under independent stationary link paths and a uniform linkwise \(L^2\) semigroup gap. It is stronger than the earlier Doeblin-based global regeneration coefficient for this one-time setting and does not require a Doeblin minorization.

It does not directly cover arbitrary multi-time block functionals or superrows whose individual link coordinates occur at multiple times within one row. It does not itself perform the Feynman–Kac occurrence summation, marked-root spatial summation, or KP convergence. Those steps must verify that their row objects fit the one-time monomial hypothesis and that the resulting activity is summable.

The theorem is a probabilistic/cumulant input only. It does not establish the interacting-vacuum Poincaré inequality, physical scale setting, continuum limit, or Yang–Mills mass gap. No P0–P5 gate is promoted by this audit.
