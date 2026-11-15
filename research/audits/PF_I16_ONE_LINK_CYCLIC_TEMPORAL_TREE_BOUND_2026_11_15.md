# PF-I16 — One-link classical cumulant to temporal-tree bound

**Date:** 2026-11-15  
**Status:** ESTABLISHED under the stationary one-link Markov $L^2$-gap hypothesis and the multivariate cyclic-permutation formula for classical/Boolean cumulants. This is a one-link result; it does not by itself prove the multi-link support-restricted cumulant tree or KP convergence.

## 1. One-link Boolean cumulants

Let $X_t$ be a stationary Markov process with
\[
P_t=\Pi+Q_t,\qquad
\|Q_t\|_{L^2_0\to L^2_0}\le e^{-\Delta_0t}.
\tag{1.1}
\]
For ordered times $s_1\le\cdots\le s_k$, the Boolean cumulant operator identity gives
\[
B_k(f_1(X_{s_1}),\ldots,f_k(X_{s_k}))
=
\langle 1,M_{f_1}(P_{s_2-s_1}-\Pi)M_{f_2}\cdots
(P_{s_k-s_{k-1}}-\Pi)M_{f_k}1\rangle.
\tag{1.2}
\]
Consequently
\[
|B_k|\le
\prod_{j=1}^k\|f_j\|_\infty
e^{-\Delta_0(s_k-s_1)}.
\tag{1.3}
\]
For $k=1$, this is the trivial expectation bound.

## 2. Cyclic-permutation conversion

The multivariate formula of Arizmendi–Hasebe–Lehner–Vargas (Theorem 1.5 in arXiv:1408.2977) states
\[
\kappa(Z_1,\ldots,Z_q)
=
\sum_{\sigma\in\mathfrak C_q}
(-1)^{\#\operatorname{runs}(\sigma)-1}
B_{\operatorname{runs}(\sigma)}(Z_1,\ldots,Z_q),
\tag{2.1}
\]
where $\mathfrak C_q$ is the set of cyclic permutations of $[q]$. Since a classical cumulant is symmetric, reorder the observations so that
\(s_1\le\cdots\le s_q\). For a cycle represented with $1$ first, its *cycle runs* are the maximal consecutive increasing subsequences. If \(\mathcal R(\sigma)\) is this set of runs, (1.3) gives
\[
|\kappa(f_1(X_{s_1}),\ldots,f_q(X_{s_q}))|
\le
\left(\prod_{i=1}^q\|f_i\|_\infty\right)
W_q(\mathbf s),
\tag{2.2}
\]
where
\[
W_q(\mathbf s):=
\sum_{\sigma\in\mathfrak C_q}
\exp\left[-\Delta_0
\sum_{B\in\mathcal R(\sigma)}
(s_{\max B}-s_{\min B})\right].
\tag{2.3}
\]

## 3. Temporal spanning-tree polynomial

Let
\[
\mathcal T_q
=\{T:T\text{ is a labelled spanning tree on }[q]\},
\qquad
\tau_q(\mathbf s)
=\sum_{T\in\mathcal T_q}
\prod_{\{i,j\}\in E(T)}
e^{-\Delta_0|s_i-s_j|}.
\tag{3.1}
\]

**Theorem.** For every $q\ge2$ and every ordered time vector (ties allowed),
\[
\boxed{
W_q(\mathbf s)\le 2^{q-2}\tau_q(\mathbf s).
}
\tag{3.2}
\]
Consequently,
\[
\boxed{
|\kappa(f_1(X_{s_1}),\ldots,f_q(X_{s_q}))|
\le 2^{q-2}\prod_i\|f_i\|_\infty
\sum_{T\in\mathcal T_q}
\prod_{\{i,j\}\in E(T)}
e^{-\Delta_0|s_i-s_j|}.
}
\tag{3.3}
\]

### Proof

For $q=2$, there is one cycle and one spanning tree, and both sides of (3.2) equal
\(e^{-\Delta_0(s_2-s_1)}\).

Assume $q\ge3$, and put
\[
r_i=e^{-\Delta_0(s_q-s_i)},\qquad 1\le i<q.
\tag{3.4}
\]
Every cycle on $[q]$, written with $1$ first, is obtained uniquely by inserting $q$ into one directed edge $a\to b$ of a cycle \(\sigma'\) on $[q-1]$. Let \(w(\sigma')\) be its summand in (2.3). If $a<b$, the insertion extends the increasing run ending at $b$, increasing the total run span by $s_q-s_b$. If $a>b$, it extends the run ending at $a$, increasing the total run span by $s_q-s_a$. Thus in either case
\[
w(\sigma)=w(\sigma')r_{\max(a,b)}.
\tag{3.5}
\]
Each vertex of \(\sigma'\) has degree two (counting the two directed edges separately when $q-1=2). Therefore
\[
\sum_{a\to b\in\sigma'}r_{\max(a,b)}
\le2\sum_{i=1}^{q-1}r_i.
\tag{3.6}
\]
Summing (3.5) over cycles and insertion positions yields
\[
W_q\le2W_{q-1}\sum_{i=1}^{q-1}r_i.
\tag{3.7}
\]

On the other hand, every tree on $[q]$ obtained by taking a tree on $[q-1]$ and attaching $q$ as a leaf to $i$ has weight equal to the old tree weight times $r_i$. These are distinct trees, so
\[
\tau_q\ge\tau_{q-1}\sum_{i=1}^{q-1}r_i.
\tag{3.8}
\]
Combining (3.7) and (3.8) with the induction hypothesis
\(W_{q-1}\le2^{q-3}\tau_{q-1}\) proves (3.2). \(\square\)

The argument is uniform in the state space and uses only the one-link Markov estimate (1.3) plus the cyclic-permutation identity. It permits interlaced time order after sorting, arbitrary bounded one-time factors, and repeated observation times.

## 4. Consequence and boundary of use

The previous max-tree estimate
\[
|\kappa_q|\le(q-1)!\prod_i\|f_i\|_\infty
\max_{T\in\mathcal T_q}\prod_{ij\in T}e^{-\Delta_0|s_i-s_j|}
\]
follows from (2.1) by bounding every Boolean block by its span and summing the absolute cyclic coefficients. The new estimate (3.3) is stronger for the one-link problem because it retains the full temporal tree sum and replaces the factorial coefficient by $2^{q-2}$.

**It does not automatically improve the multi-link Leonov–Shiryaev theorem.** After applying (3.3) to each link-block cumulant, one obtains a sum over forests of slot trees. The LS join condition makes their projection to row labels connected, but a further uniform bound on the multiplicity of the projection to a row spanning tree is required. No such multiplicity estimate is claimed here. The global support-restricted all-orders tree, marked-root sum, KP convergence, interacting-vacuum Poincare inequality, scale-setting, and continuum mass gap remain OPEN.

## 5. Finite regression

The companion verifier enumerates cycles and Prüfer trees for small $q$, uses exact rational gap weights, and checks the insertion recurrence (3.7), leaf-attachment lower bound (3.8), and final inequality (3.2). It is a finite combinatorial regression only; the proof is the induction above, while the analytic inputs (1.2)–(1.3) are separate hypotheses/results.
