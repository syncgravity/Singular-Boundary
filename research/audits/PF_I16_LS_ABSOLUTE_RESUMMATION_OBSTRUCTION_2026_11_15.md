# PF-I16 — Obstruction to the absolute-value LS partition resummation

**Date:** 2026-11-15  
**Status:** The proposed multiplicity-uniform absolute-value resummation (the analogue of (3.1) in the occurrence-level LS audit) is FALSE. The counterexample is a complete-overlap family with two common independent links. This does not obstruct the actual complete-overlap cumulant tree theorem; it shows that taking absolute values term-by-term in the LS partition formula loses cancellations that are essential even in that subcase.

## 1. The proposed inequality

For each link e, let \(\pi_e\) be a partition of the row set \([R]\). The LS join condition is
\[
(\bigvee_e\pi_e)\vee\rho=\hat 1,
\]
where \(\rho\) is the singleton partition of row labels. For each block B of \(\pi_e\), the one-link temporal-tree estimate contributes the nonnegative majorant
\[
a(B):=2^{(|B|-2)_+}\sum_{T\in\mathcal T(B)}
\prod_{\{i,j\}\in E(T)}w_{ij},
\]
with the singleton convention \(a(B)=1\). The absolute-value partition sum is
\[
\mathfrak L_R(w):=
\sum_{(\pi_e):\,\bigvee_e\pi_e=\hat 1}
\prod_e\prod_{B\in\pi_e}a(B).
\tag{1.1}
\]
The proposed route sought \(\mathfrak L_R(w)\le C^R\sum_{T\in\mathcal T(G_X)}w(T)\), with C independent of repeated occurrence multiplicity.

## 2. Two-link complete-overlap counterexample

Take R rows, each supported on the same two independent links e=1,2. Thus the row support-overlap graph is \(G_X=K_R\), and every row has two one-time slots. Set all row times equal. Then every temporal edge weight is
\[
w_{ij}=e^{-\Delta_0|t_i-t_j|}=1.
\]
For a block B of size k≥2, Cayley's formula gives
\[
a(B)=2^{k-2}k^{k-2};
\qquad a(B)=1\text{ for }k=1.
\]
In particular, for the one-block partition \(\hat1=\{[R]\}\),
\[
a([R])=2^{R-2}R^{R-2}.
\]

Now restrict the sum (1.1) to the terms with \(\pi_1=\hat1\) and \(\pi_2\) arbitrary. Every such pair satisfies the LS join condition because \(\pi_1\) already connects all rows. Hence
\[
\mathfrak L_R(1)
\ge
2^{R-2}R^{R-2}
\sum_{\pi\in\Pi([R])}\prod_{B\in\pi}a(B).
\tag{2.1}
\]
For even R, restrict the last partition sum further to partitions into pairs. Each pair block has \(a(B)=1\), and the number of pair partitions is \((R-1)!!\). Therefore
\[
\boxed{
\mathfrak L_R(1)
\ge
2^{R-2}R^{R-2}(R-1)!!,
\qquad R\text{ even}.
}
\tag{2.2}
\]
On the other hand, the target support-tree polynomial is exactly
\[
\sum_{T\in\mathcal T(K_R)}1=R^{R-2}.
\]
Consequently any inequality of the proposed form would require
\[
C^R\ge 2^{R-2}(R-1)!!.
\tag{2.3}
\]
But
\[
((R-1)!!)^{1/R}\sim\sqrt{R/e}\longrightarrow\infty
\quad (R\to\infty,\ R\text{ even}),
\]
so no fixed finite C can satisfy (2.3).

This is a direct combinatorial contradiction to the **absolute-value LS majorant**, not a probabilistic counterexample to the desired cumulant estimate.

## 3. Why the actual complete-overlap result survives

When every row uses the same link set, the product process \(Z_t=(X_1(t),X_2(t))\) has the same mean-zero \(L^2\) gap as either factor. Applying the one-link Markov temporal-tree theorem directly to the bounded row observables \(F_i(Z_{t_i})\) gives
\[
|\kappa(F_1(Z_{t_1}),\ldots,F_R(Z_{t_R}))|
\le
2^{R-2}\prod_i\|F_i\|_\infty
\sum_{T\in\mathcal T(K_R)}\prod_{\{i,j\}\in E(T)}w_{ij}.
\]
At coincident times this is \(2^{R-2}R^{R-2}\prod_i\|F_i\|_\infty\), fully consistent with the actual theorem. The much larger quantity in (2.2) is an artefact of replacing the signed LS sum by the sum of absolute values of all link-partition contributions.

## 4. Consequence for the proof strategy

- The occurrence-level LS identity and its join/connectivity interpretation remain exact.
- The absolute-value resummation proposed in the occurrence-level audit cannot be proved with a multiplicity-uniform exponential coefficient; equation (2.2) disproves it.
- A successful sparse-support proof must preserve cancellations between different link partitions, or avoid expanding into independent per-link partitions at this stage.
- The complete-overlap product-semigroup proof remains valid.
- The bounded-slot-incidence projective LS theorem remains valid under its literal \(q_e\le D\) hypothesis.
- The connected, non-complete support case with unrestricted repeated labels remains open. No KP or mass-gap gate is promoted.

The companion verifier checks the exact finite combinatorial lower bound for even R. The asymptotic contradiction follows analytically from the standard double-factorial asymptotic above; it is not inferred from finite testing.
