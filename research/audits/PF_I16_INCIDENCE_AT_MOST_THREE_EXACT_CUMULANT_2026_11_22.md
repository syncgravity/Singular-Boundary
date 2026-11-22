# PF-I16 — All-orders cumulant factorization for link incidence at most three

**Date:** 2026-11-22  
**Status:** exact all-orders result for centered elementary tensor insertions when every link coordinate occurs in at most three row insertions. The proof uses the Leonov–Shiryaev product-cumulant identity and the one-link temporal cumulant estimate. It does not cover incidence four or the general PF-I16 face/pair insertion without an appropriate elementary-tensor expansion.

## 1. Setting and statement

Let (U_e(t)), indexed by link coordinates (e), be independent stationary link processes. Assume the one-link estimate
\[
|\kappa_k(f_1(U_e(t_1)),\ldots,f_k(U_e(t_k)))|
\le (2e)^k k!\,
e^{-\Delta_0(t_{\max}-t_{\min})}
\prod_{j=1}^k\|f_j\|_\infty
\tag{1.1}
\]
for bounded one-link observables and (k\ge2).

For each row (i\in[r]), let
\[
A_i(t_i)=\prod_{e\in X_i} f_{i,e}(U_e(t_i)),
\]
where every factor is centered under its one-link invariant law:
\[
\mathbb E f_{i,e}(U_e(t_i))=0.
\]
Write (I_e=\{i:e\in X_i\}) for the row-incidence set of link (e), and assume
\[
|I_e|\le3\quad\text{for every }e,
\qquad
\sum_e|I_e|=\sum_i|X_i|\le8r.
\tag{1.2}
\]
Let (G_X) be the support-overlap graph on the rows, with (ij\in E(G_X)) exactly when (X_i\cap X_j\ne\varnothing).

If some (I_e) is a singleton, then (A_i) contains a centered link factor independent of every other row and every other factor in row (i); the joint cumulant vanishes. Hence assume every nonempty (I_e) has size two or three. If the incidence hypergraph ({I_e}_e) is disconnected, the joint cumulant also vanishes.

**Claim.** If the incidence hypergraph is connected and (2\le |I_e|\le3) for every active link, then
\[
\boxed{
\kappa(A_1(t_1),\ldots,A_r(t_r))
=
\prod_e
\kappa\bigl(f_{i,e}(U_e(t_i)):i\in I_e\bigr).
}
\tag{1.3}
\]
Consequently, with
\[
\mathcal M(G_X;\mathbf t)
=
\max_{T\in\mathcal T(G_X)}
\prod_{\{i,j\}\in T}e^{-\Delta_0|t_i-t_j|},
\]
we have
\[
\boxed{
|\kappa(A_1(t_1),\ldots,A_r(t_r))|
\le
C_3^r
\left(\prod_i\prod_{e\in X_i}\|f_{i,e}\|_\infty\right)
\mathcal M(G_X;\mathbf t),
\qquad
C_3=(2e)^8 6^4.
}
\tag{1.4}
\]
The constant is deliberately coarse but exponential in the number of rows.

## 2. Exact Leonov–Shiryaev collapse

Apply the Leonov–Shiryaev product-cumulant formula to the row products (A_i). A partition block containing elementary factors from two different link coordinates has zero cumulant, because the link path processes are independent. Thus every admissible block is monochromatic in its link label, and the full partition is a union of linkwise partitions (pi_e) of (I_e).

Every singleton block vanishes because each elementary factor is centered. If (|I_e|=2), the only partition of (I_e) with no singleton blocks is the single pair block (I_e). If (|I_e|=3), the only such partition is the single triple block (I_e): a pair plus a singleton vanishes. Therefore each active link has exactly one nonzero linkwise partition,
\[
\pi_e=\{I_e\}.
\]
The join of these link blocks with the row partition is connected exactly when the incidence hypergraph ({I_e}) is connected. Under the stated connectedness assumption, there is exactly one nonzero Leonov–Shiryaev term, namely the product of the full link cumulants. This proves (1.3).

This explains why the pairwise-incidence case has an exact graph-edge product and why a triple-incidence link still causes no partition ambiguity.

## 3. Temporal support-tree extraction

For each active link (e), order its two or three incident rows by their observation times:
\[
t_{i_1}\le\cdots\le t_{i_k},\qquad k=|I_e|\in\{2,3\}.
\]
Join consecutive rows in this order. This gives a path (T_e) on the vertices (I_e), and every edge of (T_e) belongs to (G_X), since its endpoint rows share link (e). Moreover,
\[
\prod_{\{i,j\}\in T_e}e^{-\Delta_0|t_i-t_j|}
=e^{-\Delta_0(t_{\max(I_e)}-t_{\min(I_e)})}.
\tag{3.1}
\]
The union (H=\bigcup_eT_e) is connected because the link-incidence hypergraph is connected. It is a subgraph of (G_X). Choose any spanning tree (T\subseteq H). All edge weights lie in ([0,1]), so deleting the other edges can only increase their product:
\[
\prod_e e^{-\Delta_0\operatorname{span}(t_{I_e})}
\le
\prod_{\{i,j\}\in T}e^{-\Delta_0|t_i-t_j|}
\le \mathcal M(G_X;\mathbf t).
\tag{3.2}
\]

Applying (1.1) to each factor in (1.3), then using (3.2), gives the temporal factor in (1.4).

## 4. Order-uniform coefficient

Let (m) be the number of active links and (k_e=|I_e|\in\{2,3\}). The product of the one-link constants is bounded by
\[
\prod_e (2e)^{k_e}k_e!
\le
(2e)^{\sum_e k_e}6^m
\le
(2e)^{8r}6^{4r}
=
\bigl((2e)^8 6^4\bigr)^r,
\tag{4.1}
\]
because (sum_e k_e\le8r) and (2m\le\sum_e k_e). This proves (1.4).

## 5. Proof boundary and next gate

**Established:** exact all-orders product-cumulant factorization and an exponential-in-(r) support-maximum-tree estimate for centered elementary tensors with link-incidence sizes two or three.

**Not established:** incidence size four or greater; noncentered elementary factors without a separate centered decomposition; actual face/pair insertion projective norms; the full PF-I16 insertion class; the all-orders quantum connected-resolvent/KP theorem; or an interacting-vacuum Poincaré inequality.

The first unresolved local incidence is (|I_e|=4). A centered four-variable link cumulant has at least two nonzero Leonov–Shiryaev partitions on that link:
\[
\{I_e\}
\quad\text{and}\quad
\{\{i_1,i_2\},\{i_3,i_4\}\}
\]
(and the other pairings). Thus the unique-partition collapse fails. The next calculation must retain the signed sum between the four-block cumulant and the pair-pair products, and determine whether that linkwise resummation can be made before the global connectedness selector.


## 6. First four-incidence connector: exact surviving partition family

The first failure of uniqueness can be seen with four rows and two independent links. Let link (e) occur in all four rows, with centered factors (f_1,f_2,f_3,f_4). Let a second link (h) occur only in rows (2,3), with centered factors (g_2,g_3). Take
\[
A_1=f_1(U_e(t_1)),\quad
A_2=f_2(U_e(t_2))g_2(U_h(t_2)),\quad
A_3=f_3(U_e(t_3))g_3(U_h(t_3)),\quad
A_4=f_4(U_e(t_4)).
\]
The (h)-link has only its pair block ({2,3}). On the (e)-link, the only nonzero partitions without singleton blocks are the full four-block and the three pair-pair partitions. The global join condition retains the full four-block and exactly two of the three pair-pair partitions: the pairing ({1,4}\mid\{2,3\}) is disconnected after adjoining the (h)-block, while ({1,2\}\mid\{3,4\}) and ({1,3\}\mid\{2,4\}) are connected. Thus the exact product-cumulant identity is
\[
\boxed{
\begin{aligned}
\kappa(A_1,A_2,A_3,A_4)
={}&\kappa_h(g_2,g_3)\\
&\times\Big[
\kappa_e(f_1,f_2,f_3,f_4)
+\kappa_e(f_1,f_2)\kappa_e(f_3,f_4)\\
&\hspace{2.6em}
+\kappa_e(f_1,f_3)\kappa_e(f_2,f_4)
\Big].
\end{aligned}
}
\tag{6.1}
\]
All cumulants are evaluated at their row-specific times.

Because the factors are centered, the fourth raw moment identity is
\[
\mathbb E_e[f_1f_2f_3f_4]
=
\kappa_e(f_1,f_2,f_3,f_4)
+\kappa_e(f_1,f_2)\kappa_e(f_3,f_4)
+\kappa_e(f_1,f_3)\kappa_e(f_2,f_4)
+\kappa_e(f_1,f_4)\kappa_e(f_2,f_3).
\]
Therefore the bracket in (6.1) is the raw fourth moment **minus the pairing excluded by the global connectivity selector**:
\[
\mathbb E_e[f_1f_2f_3f_4]
-\kappa_e(f_1,f_4)\kappa_e(f_2,f_3).
\tag{6.2}
\]
This is the smallest explicit example showing why a four-incidence link cannot be resummed independently of the other link supports: the global connectedness condition selects which pair-pair terms survive. A local replacement of the entire (e)-link partition sum by its raw moment would incorrectly include the disconnected pairing.

At coincident times with (f_1=f_2=f_3=f_4=Z) a Rademacher variable, (kappa_4(Z)=-2) and every pair covariance is (1), so the bracket in (6.1) is (-2+1+1=0). The cancellation is exact and is lost by taking absolute values term by term. This four-row calculation identifies the first required resummation: retain the global join selector while grouping the four-incidence link's block and pair-pair contributions.
