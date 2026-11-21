# PF-I16 — Global occurrence-level regeneration tree bound

**Date:** 2026-11-16  
**Status:** global signed-cumulant tree bound proved under the compact-link Doeblin envelope, with a finite explicit coefficient independent of repeated insertion multiplicities. The coefficient is superexponential in cumulant order and does not close the KP estimate.

## 1. Purpose and relation to the occurrence-level LS identity

For a fixed monomial tuple, write the row observables as
\[
A_i=\prod_{e\in X_i}f_{i,e}(X_e(t_i)),\qquad i=1,\ldots,R,
\]
where the link paths \(X_e\) are independent and stationary, and each \(X_i\) is a finite set of links. The original occurrence-level Leonov–Shiryaev identity is
\[
\kappa(A_1,\ldots,A_R)
=\sum_{\substack{(\pi_e)_e\\(\bigvee_e\pi_e)\vee\rho=\hat1}}
 \prod_e\prod_{B\in\pi_e}\kappa_e(Y_{i,e}:i\in B),
\]
with the original row-occurrence labels retained. No grouping of repeated rows and no replacement of the original occurrence partition is made here.

The argument below gives a different representation of the *same full cumulant*. It bypasses termwise absolute values of the LS sum, so it is not contradicted by the two-link obstruction to the absolute-value LS majorant.

## 2. Assumptions

For every link \(e\), assume its stationary Markov path has transition densities relative to its invariant probability \(\mu_e\), and a common Doeblin envelope
\[
P^e_d(x,dy)=p^e_d(x,y)\mu_e(dy),\qquad
\alpha_e(d):=\inf_{u\ge d,x,y}p^e_u(x,y)>0,
\]
\[
1-\alpha_e(d)\le C_0e^{-\Delta_0d}\quad(d>0),
\]
with \(C_0,\Delta_0\) uniform over links and regulators. Assume also the row-incidence bound
\[
|X_i|\le m
\]
for every row. In the PF-I16 face/face-pair setting, the intended value is \(m\le8\). The estimate below depends on this row-support bound, not on the number of distinct links in the whole tuple and not on how many times a support type is repeated.

Let
\[
w_{ij}=e^{-\Delta_0|t_i-t_j|},\qquad
G_X=(\{1,\ldots,R\},\{\{i,j\}:X_i\cap X_j\ne\varnothing\}).
\]

## 3. Theorem

For \(R\ge2\), define
\[
K_R=\sum_{\pi\in\Pi_R}(|\pi|-1)!.
\]
Then
\[
\boxed{
|\kappa(A_1,\ldots,A_R)|
\le K_R(mRC_0)^{R-1}
\prod_{i=1}^R\prod_{e\in X_i}\|f_{i,e}\|_\infty
\sum_{T\in\mathcal T(G_X)}\prod_{\{i,j\}\in T}w_{ij}.
}
\tag{3.1}
\]
The sum is zero if \(G_X\) is disconnected. For \(R=1\), the assertion is the elementary product sup-norm bound.

In particular, for \(m\le8\), this gives a multiplicity-uniform, support-restricted temporal tree bound with coefficient
\[
C_R^{\rm glob}=K_R(8RC_0)^{R-1}.
\]
It is independent of the total number of links, the number of repeated occurrences of any fixed support type, and the time horizon.

**Limitation.** \(K_R\) is a partition-factorial quantity, so this coefficient is superexponential in \(R\). The theorem is a genuine global occurrence-level closure at finite order, but it is not the exponential-in-\(R\) coefficient needed for the intended KP bound. It does not prove KP convergence.

## 4. Proof

### 4.1 Independent link-gap regeneration

Fix a link \(e\), and list its row ports in increasing time order:
\[
t_{i_1}<\cdots<t_{i_{n_e}},\qquad i_k\in I_e:=\{i:e\in X_i\}.
\]
For each consecutive pair \((i_k,i_{k+1})\), the Doeblin decomposition gives
\[
P^e_{t_{i_{k+1}}-t_{i_k}}
=\alpha^e_k\Pi_e+(1-\alpha^e_k)R^e_k,
\qquad
1-\alpha^e_k\le C_0w_{i_ki_{k+1}}.
\]
Use independent Bernoulli activity indicators for every link-gap pair and every replica. An inactive gap is a reset to a fresh \(\mu_e\)-sample; an active gap uses the residual stationary kernel. Initial states, link paths, and all transition innovations are independent across links.

For each row pair \(\{i,j\}\), let \(H_{ij}\) be the event that at least one link \(e\) for which \(i,j\) are consecutive ports, and at least one of the \(R\) replicas, has an active gap. Put \(\{i,j\}\in H\) on this event. The underlying indicator families for distinct unordered row pairs are disjoint, hence the edge events \(H_{ij}\) are independent. Moreover,
\[
\begin{aligned}
p_{ij}:=\Pr(H_{ij})
&\le R C_0\,w_{ij}\,
 \#\{e\in X_i\cap X_j:\ i,j\text{ consecutive in }I_e\}\\
&\le mRC_0\,w_{ij}.
\end{aligned}
\tag{4.1}
\]
The last inequality uses \(|X_i\cap X_j|\le |X_i|\le m\). If \(X_i\cap X_j=\varnothing\), then \(p_{ij}=0\).

### 4.2 Replica formula for the original cumulant

Take \(R\) independent full replicas of the entire independent-link system. For every partition \(\pi\in\Pi_R\), assign its blocks injectively to the first \(|\pi|\) replicas, in a fixed canonical order. If \(r_\pi(B)\) is the replica assigned to block \(B\), put
\[
\Xi_\pi=
\prod_{B\in\pi}\prod_{i\in B}
A_i\bigl(X^{(r_\pi(B))}\bigr),
\qquad
\Xi=\sum_{\pi\in\Pi_R}
(-1)^{|\pi|-1}(|\pi|-1)!\,\Xi_\pi.
\]
Different blocks use independent replicas, so
\[
\mathbb E\Xi_\pi=\prod_{B\in\pi}\mathbb E\prod_{i\in B}A_i.
\]
The classical moment-partition formula gives the exact identity
\[
\mathbb E\Xi=\kappa(A_1,\ldots,A_R).
\tag{4.2}
\]
Pointwise,
\[
|\Xi|\le K_R\prod_i\|A_i\|_\infty
\le K_R\prod_i\prod_{e\in X_i}\|f_{i,e}\|_\infty.
\tag{4.3}
\]

### 4.3 Disconnected-union cancellation

Condition on the union graph \(H\). If \(H\) has components \(C_1,\ldots,C_s\), then every link transition between ports belonging to different components is a reset in every replica: otherwise the corresponding row-pair edge would be present in \(H\). Conditional on \(H\), the indicator collections for distinct unordered row pairs remain independent. The reset innovations and link paths are also independent across links. Thus the arrays of all replicas restricted to distinct components are independent.

The conditioning is invariant under permutations of the replica labels. Therefore, for each \(\pi\),
\[
\mathbb E[\Xi_\pi\mid H]
=\prod_{a=1}^s F_{C_a}(\pi|_{C_a}),
\]
where \(F_{C_a}\) depends only on the restriction of \(\pi\) to \(C_a\), not on the particular replica labels assigned to its blocks.

For any nontrivial partition \(\{C_1,\ldots,C_s\}\) of \([R]\), the partition-lattice cancellation identity is
\[
\sum_{\pi\in\Pi_R}(-1)^{|\pi|-1}(|\pi|-1)!
 \prod_{a=1}^sF_{C_a}(\pi|_{C_a})=0.
\tag{4.4}
\]
For completeness, fix all restrictions \(\sigma_a=\pi|_{C_a}\). Regard their blocks as atoms colored by \(a\). Global partitions with these restrictions are exactly partitions of the atoms into rainbow blocks, i.e. proper color-class partitions of the disjoint union graph
\[
G_\sigma=\bigsqcup_{a=1}^sK_{|\sigma_a|}.
\]
The sum of the Möbius coefficients over these partitions is
\[
\chi'_{G_\sigma}(0)
=\left.\frac{d}{dx}\prod_{a=1}^s x^{\underline{|\sigma_a|}}\right|_{x=0}=0,
\]
because \(s\ge2\). Summing over restrictions proves (4.4). Consequently,
\[
\mathbb E[\Xi\mid H]=0\quad\text{whenever }H\text{ is disconnected}.
\tag{4.5}
\]

### 4.4 Connected graph probability

By (4.2)–(4.5),
\[
|\kappa(A_1,\ldots,A_R)|
\le K_R\prod_i\|A_i\|_\infty\Pr(H\text{ connected}).
\]
Every connected graph contains a spanning tree. Since the edge events of \(H\) are independent,
\[
\begin{aligned}
\Pr(H\text{ connected})
&\le\sum_{T\in\mathcal T(G_X)}
  \prod_{\{i,j\}\in T}p_{ij}\\
&\le(mRC_0)^{R-1}
  \sum_{T\in\mathcal T(G_X)}
  \prod_{\{i,j\}\in T}w_{ij}.
\end{aligned}
\]
This proves (3.1). \(\square\)

## 5. Why this does not solve the KP coefficient problem

The proof preserves the full cumulant, hence all signed cancellations in the occurrence-level LS identity, and does not sum the absolute values of individual LS partitions. It also avoids constants depending on the number of occurrences of a support type.

However, the replica Möbius sum was bounded pointwise by
\[
K_R=\sum_{k=1}^R S(R,k)(k-1)!.
\]
That loses the finer cancellation on connected \(H\). A sparse support graph may have only one spanning tree, so its tree polynomial does not provide a general factorial multiplicity with which to absorb \(K_R\). Thus the estimate is not silently upgraded to \(C^R\).

The remaining sharp target is to estimate the *conditional connected contribution*
\[
\left|\mathbb E[\Xi\,\mathbf1_{\{H\text{ connected}\}}]\right|
\]
by an exponential-in-\(R\) coefficient times the support-restricted tree polynomial, exploiting cancellations among connected regeneration configurations. Neither the local interlaced block theorem nor (3.1) establishes that sharper estimate.

## 6. Proof ledger

Established under the uniform linkwise Doeblin envelope and \(|X_i|\le m\):

- exact regeneration representation for every link-gap occurrence;
- exact replica representation of the original \(R\)-row cumulant;
- conditional cancellation whenever the union row graph is disconnected;
- independent row-pair edge events and the bound \(p_{ij}\le mRC_0R\,w_{ij}\);
- a global occurrence-multiplicity-uniform support-tree estimate (3.1).

Still open:

- exponential-in-\(R\) control of the connected replica contribution;
- a useful KP majorant and marked-root summation;
- the interacting-vacuum Poincaré inequality, physical scale setting, and continuum mass gap.

No P0–P5 gate is promoted by this result.
