# PF-I16 — Exact cumulant factorization for pairwise link incidence

**Date:** 2026-11-22  
**Status:** exact all-orders identity for centered elementary tensor insertions whose link-incidence sets all have size two. This is a restricted pairwise-incidence class, not the general PF-I16 insertion theorem.

## 1. Setting

Let (G=(V,E)) be a finite connected loopless multigraph with (|V|=r\ge2). Each edge (e=\{i,j\}\) labels a distinct link path (U_e(t)). The link paths are independent across (e), stationary, and satisfy the one-link covariance estimate
\[
|\operatorname{Cov}(f(U_e(t)),g(U_e(s)))|
\le e^{-\Delta_0|t-s|}\|f\|_\infty\|g\|_\infty
\]
for bounded observables. For every incidence (i\in e), choose a bounded centered one-link observable (f_{i,e}), with mean zero under the invariant link law. Define
\[
A_i(t_i)=\prod_{e\ni i} f_{i,e}(U_e(t_i)),
\qquad d_i=\deg_G(i).
\]
Thus every link coordinate occurs in exactly two row insertions, and every row is an elementary tensor over its incident link coordinates.

For each edge (e=\{i,j\}), put
\[
c_e=\mathbb E[f_{i,e}(U_e(t_i))f_{j,e}(U_e(t_j))],
\qquad g_e=c_e s_i s_j.
\]

## 2. Exact row-polynomial identity

Introduce
\[
Y_i(s_i)=\prod_{e\ni i}(1+s_i f_{i,e}(U_e(t_i))),
\qquad
u_\Delta(\mathbf s)=\mathbb E\prod_{i\in\Delta}Y_i(s_i).
\]
Independence of link paths and centering imply
\[
u_\Delta(\mathbf s)
=\prod_{e=\{i,j\}\in E:\,i,j\in\Delta}(1+g_e).
\tag{2.1}
\]
Indeed, a link contributes (1) if zero or one endpoint row is selected, and contributes (1+s_is_jc_e) if both endpoint rows are selected.

Let
\[
Z(\mathbf x)=\sum_{\Delta\subseteq V}u_\Delta(\mathbf s)
\prod_{i\in\Delta}x_i.
\]
Expanding (2.1) over edge subsets (F\subseteq E), and writing (V(F)) for the vertices incident to (F), gives the exact formal identity
\[
\begin{aligned}
Z(\mathbf x)
&=\sum_{F\subseteq E}\Big(\prod_{e\in F}g_e\Big)
\prod_{i\in V(F)}x_i
\prod_{i\notin V(F)}(1+x_i)\\
&=\prod_{i\in V}(1+x_i)
\sum_{F\subseteq E}\Big(\prod_{e\in F}g_e\Big)
\prod_{i\in V(F)}\frac{x_i}{1+x_i}.
\end{aligned}
\tag{2.2}
\]
Set (y_i=x_i/(1+x_i)). The coefficient of the square-free monomial (x_V=\prod_{i\in V}x_i) in \(\sum_i\log(1+x_i)\) is zero for (r\ge2), and replacing (y_i) by (x_i+O(x_i^2)) does not change a square-free coefficient. Hence
\[
[x_V]\log Z(\mathbf x)
=[y_V]\log\left(
\sum_{F\subseteq E}\Big(\prod_{e\in F}g_e\Big)y_{V(F)}
\right).
\tag{2.3}
\]

The edge-subset polynomial inside the logarithm factors uniquely over the connected components of each edge subset. Its logarithm therefore retains exactly connected edge subsets. Consequently
\[
\boxed{
[x_V]\log Z(\mathbf x)
=
\sum_{\substack{F\subseteq E:\,(V(F),F)\text{ connected}\\V(F)=V}}
\prod_{e\in F}g_e.
}
\tag{2.4}
\]
This is the connected-subgraph expansion for the pairwise-incidence model.

## 3. Top-degree extraction collapses the connected-subgraph sum

The square-free selector identity for classical cumulants gives
\[
\kappa(Y_1(s_1),\ldots,Y_r(s_r))
=[x_V]\log Z(\mathbf x).
\]
Also, by multilinearity,
\[
\kappa(A_1(t_1),\ldots,A_r(t_r))
=[s_1^{d_1}\cdots s_r^{d_r}]
\kappa(Y_1(s_1),\ldots,Y_r(s_r)).
\]
Every edge factor (g_e=c_es_is_j) contributes degree one at each endpoint. A connected spanning edge subset (F\) can contribute to the target degree (d_i=\deg_G(i)) at every vertex only if it contains every edge incident to every vertex. Thus (F=E) is the unique surviving term in (2.4). We obtain the exact identity
\[
\boxed{
\kappa(A_1(t_1),\ldots,A_r(t_r))
=\prod_{e=\{i,j\}\in E}
\operatorname{Cov}\bigl(f_{i,e}(U_e(t_i)),f_{j,e}(U_e(t_j))\bigr).
}
\tag{3.1}
\]
The covariance equals the displayed expectation because each incidence observable is centered.

## 4. Support-sensitive temporal bound

Applying the one-link gap estimate edge by edge gives
\[
|\kappa(A_1(t_1),\ldots,A_r(t_r))|
\le
\prod_{i\in V}\prod_{e\ni i}\|f_{i,e}\|_\infty
\prod_{e=\{i,j\}\in E}e^{-\Delta_0|t_i-t_j|}.
\tag{4.1}
\]
Every edge weight lies in ([0,1]). For any spanning tree (T\subseteq E), deleting the non-tree factors can only increase the product. Therefore
\[
\boxed{
|\kappa(A_1(t_1),\ldots,A_r(t_r))|
\le
\prod_i\prod_{e\ni i}\|f_{i,e}\|_\infty
\max_{T\in\mathcal T(G)}
\prod_{\{i,j\}\in T}e^{-\Delta_0|t_i-t_j|}.
}
\tag{4.2}
\]
The coefficient is exactly one and independent of (r). In particular, the identity resolves the pairwise-incidence four-cycle, triangle-with-pendant, diamond, and complete-four-vertex patterns whenever each support edge is represented by one centered link factor.

## 5. Scope and open extension

**Established here:** the all-orders exact cumulant identity (3.1) and the maximum-support-tree estimate (4.2) for centered elementary tensors with pairwise link incidence.

**Not established:** the same result when one link coordinate occurs in three or more row insertions; noncentered factors without first expanding them into centered components; general face/pair insertions with overlapping link-incidence hyperedges; the cancellation-sensitive all-orders PF-I16 bound; or the quantum Kotecký–Preiss/interacting-vacuum argument.

The next gate is the smallest genuinely higher-order incidence hyperedge: one link shared by three rows, with the remaining row-support slots arranged to make the four-row support graph connected. Its Boolean-lattice factor (P_\Delta^e) is no longer pairwise, and the exact connected-subgraph collapse above no longer applies directly.
