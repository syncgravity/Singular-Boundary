# PF-I16 — All-orders temporal tree bound when the support graph is a tree

**Date:** 2026-11-14  
**Status:** ESTABLISHED for every finite tree support graph under independent stationary link paths with a uniform one-link L2 gap. The general connected support-graph tree-sum theorem remains OPEN.  
**Scope:** arbitrary bounded local multiplication observables; finite link set; stationary independent link Markov processes. No P0–P5 gate is promoted.

## 1. Theorem

Let \(T=([r],E_T)\) be a tree. Suppose the row supports \(X_i\) have support-overlap graph exactly \(T\):
\[
X_i\cap X_j\ne\varnothing
\quad\Longleftrightarrow\quad
ij\in E_T.
\]
For independent stationary link paths with
\[
\|P_t^e-\Pi_e\|_{2\to2}\le e^{-\Delta_0t},
\]
and bounded row observables
\[
A_i(t_i)=F_i((X_e(t_i))_{e\in X_i}),\qquad
\|F_i\|_\infty\le M_i,
\]
we have the exact tree-product bound
\[
\boxed{
|\kappa(A_1(t_1),\ldots,A_r(t_r))|
\le
\Bigl(\prod_{i=1}^rM_i\Bigr)
\prod_{ij\in E_T}e^{-\Delta_0|t_i-t_j|}.
}
\tag{1.1}
\]
The coefficient is 1. This is an all-orders support-restricted temporal tree theorem for acyclic support-overlap graphs.

## 2. Leaf-contraction lemma

Let \(i\) be a leaf of \(T\), with unique neighbor \(j\), and put
\[
L=X_i\cap X_j.
\]
Because \(i\) is a leaf, every link in \(L\) is used by rows \(i,j\) only. All other links in row \(i\) are private to that row. Let \(Z_L(t)=(X_e(t))_{e\in L}\) be the product Markov process on the shared link set.

Integrate the private coordinates of row \(i\) under their stationary one-time laws. This replaces \(A_i(t_i)\), in every joint moment with the other rows, by a bounded function \(f_i(Z_L(t_i))\), with \(\|f_i\|_\infty\le M_i\). Define
\[
g(Z_L(t_j))
=\mathbb E[f_i(Z_L(t_i))\mid Z_L(t_j)],
\qquad
g_0=g-\mathbb E f_i.
\]
The conditional expectation is the forward semigroup if \(t_i\ge t_j\) and the stationary reverse semigroup (the adjoint) if \(t_i<t_j\). Both have the same mean-zero L2 contraction. Tensorization over the links in \(L\) preserves the gap \(\Delta_0\), so
\[
\boxed{
\|g_0\|_2
\le M_i e^{-\Delta_0|t_i-t_j|}.
}
\tag{2.1}
\]

No other row uses a link in \(L\). Thus all rows other than \(i,j\) are independent of the entire path \(Z_L\), while row \(j\) uses it only through \(Z_L(t_j)\). The following exact cumulant-contraction identity applies:
\[
\boxed{
\kappa(A_i,A_j,A_{k_1},\ldots,A_{k_{r-2}})
=
\kappa(H_j,A_{k_1},\ldots,A_{k_{r-2}}),
}
\tag{2.2}
\]
where
\[
H_j(W)
=
\mathbb E_{Z_L(t_j)}
\big[g_0(Z_L(t_j))F_j(Z_L(t_j),W)\big],
\tag{2.3}
\]
and \(W\) denotes the remaining link coordinates of row \(j\). In particular, \(H_j\) is a bounded observable supported on \(X_j\setminus L\), and
\[
\begin{aligned}
\|H_j\|_\infty
&\le M_j\,\mathbb E|g_0(Z_L(t_j))|\\
&\le M_j\|g_0\|_2\\
&\le M_iM_j e^{-\Delta_0|t_i-t_j|}.
\end{aligned}
\tag{2.4}
\]

### Proof of the contraction identity

One direct proof uses the multivariate moment-generating function. Let
\[
M(s_1,s_2,\mathbf s)
=\mathbb E\exp\left(s_1g_0(Z_L(t_j))
+s_2A_j+\sum_k s_kA_k\right).
\]
The variables \(A_k\), \(k\ne i,j\), are independent of \(Z_L\), and \(\mathbb E g_0=0\). Therefore, at \(s_1=0\),
\[
\left.\partial_{s_1}\log M\right|_{s_1=0}
=
\frac{\mathbb E[g_0e^{s_2A_j+\sum_ks_kA_k}]}
{\mathbb E[e^{s_2A_j+\sum_ks_kA_k}]}.
\]
At \(s_2=0\), the numerator vanishes. Differentiating once in \(s_2\) at zero gives
\[
\frac{\mathbb E[H_j(W)e^{\sum_ks_kA_k}]}
{\mathbb E[e^{\sum_ks_kA_k}]},
\]
which is the derivative in the source variable of the log moment-generating function for \((H_j,A_{k_1},\ldots)\). Taking the remaining derivatives at zero proves (2.2). This argument is valid for bounded variables in a neighborhood of the origin; it is an identity of formal cumulant coefficients as well.

## 3. Induction on the support tree

After replacing rows \(i,j\) by \(H_j\), remove leaf \(i\) and delete the links \(L\) from row \(j\)'s support. Since no other row uses \(L\), the new support-overlap graph is exactly \(T\setminus\{i\}\), again a tree. The new row norm obeys (2.4).

Apply the same operation recursively. Each tree edge \(ij\) contributes exactly one factor \(e^{-\Delta_0|t_i-t_j|}\), and each original row norm appears exactly once. At the final single row, the order-one cumulant is its expectation, bounded by its sup norm. This proves (1.1) for every \(r\).

## 4. Why this does not yet prove the general graph theorem

If the support-overlap graph has cycles, a leaf row may share one link with its chosen tree neighbor and additional links with other rows. Those additional shared links are not private to the leaf-neighbor pair, so the contraction identity cannot eliminate all of the leaf's dependence while preserving the other rows' joint moments.

Thus (1.1) proves the desired estimate whenever the support graph itself is a tree. It does not imply
\[
|\kappa(A_1(t_1),\ldots,A_r(t_r))|
\le C^r\prod_iM_i
\sum_{T\in\mathcal T(G_X)}
\prod_{ij\in T}e^{-\Delta_0|t_i-t_j|}
\]
for graphs with cycles. The remaining task is to resum cyclic overlap redundancies into the spanning-tree sum without losing the leaf-contraction decay factors or the cumulant signs.

The previous order-two/order-three result is a special case of this theorem for tree support graphs; the triangle case still follows separately from the global product-process temporal tree theorem. The finite-state verifier is a regression test, not a substitute for the analytic proof.

Marked-root spatial summation, quantum KP convergence, the interacting-vacuum Poincare inequality, and the continuum mass gap remain **OPEN**. No P0–P5 status is promoted.
