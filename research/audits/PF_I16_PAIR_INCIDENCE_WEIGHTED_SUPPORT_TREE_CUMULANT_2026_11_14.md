# PF-I16 — Weighted support-tree cumulants for pair-incidence link systems

**Date:** 2026-11-14  
**Status:** ESTABLISHED for link coordinates incident to at most two rows; cyclic support graphs included. The extension to links incident to three or more rows remains OPEN.  
**Scope:** finite independent stationary link Markov paths with a uniform one-link L2 gap; arbitrary bounded row functions of their incident link coordinates. No P0–P5 gate is promoted.

## 1. Theorem

Let rows be indexed by \([r]\), with support sets \(X_i\) of independent link coordinates. Assume
\[
\boxed{\quad |\{i:e\in X_i\}|\le2\quad\text{for every link }e.\quad}
\tag{1.1}
\]
For each link e, let its stationary Markov semigroup satisfy
\[
\|P_s^e-\Pi_e\|_{2\to2}\le e^{-\Delta_0s}.
\]
Let
\[
A_i=F_i((X_e(t_i))_{e\in X_i}),\qquad \|F_i\|_\infty\le M_i,
\]
and let \(G_X\) be the simple support-overlap graph. Let \(m_{ij}=|X_i\cap X_j|\). Then
\[
\boxed{
|\kappa(A_1,\ldots,A_r)|
\le
\sum_{T\in\mathcal T(G_X)}
\prod_{ij\in T}
m_{ij}e^{-\Delta_0|t_i-t_j|}
\prod_iM_i.
}
\tag{1.2}
\]
In particular, if \(m_{ij}\le m_*\), then
\[
|\kappa(A_1,\ldots,A_r)|
\le m_*^{r-1}\prod_iM_i
\sum_{T\in\mathcal T(G_X)}
\prod_{ij\in T}e^{-\Delta_0|t_i-t_j|}.
\tag{1.3}
\]
When every pair shares at most one link, the coefficient is exactly one. The result includes cyclic support graphs.

## 2. The one-link deletion–contraction identity

The proof is formulated for a current family of super-rows. A super-row is a bounded function of finitely many independent link paths, with each external link evaluated at one specified time. Link paths internal to one super-row have already been integrated out. Every external link is incident to exactly two current super-rows.

Choose an external link \(e\) shared by super-rows \(C,D\), evaluated at times \(s_C,s_D\). Condition on all other link paths. Write the two row functions as
\[
G_C(x;Z),\qquad G_D(y;Z),
\]
where x and y are the e-states at their respective times and Z denotes the other link-path coordinates. Define the conditional e-mean and centered part
\[
\bar G_C(Z)=\int G_C(x;Z)\,d\nu_e(x),\qquad
\widetilde G_C(x;Z)=G_C(x;Z)-\bar G_C(Z).
\tag{2.1}
\]
By multilinearity,
\[
\kappa(G_C,G_D,G_{\rm rest})
=
\kappa(\bar G_C,G_D,G_{\rm rest})
+
\kappa(\widetilde G_C,G_D,G_{\rm rest}).
\tag{2.2}
\]

The first term is the **deletion branch**. The e-coordinate is now used by D alone, so it is private and can be integrated out of D. This deletes edge e from the current link-incidence multigraph and does not increase any row norm.

For the second term, condition on Z and propagate the centered C-insertion to D's time:
\[
g(y;Z)=\mathbb E[\widetilde G_C(X_e(s_C);Z)\mid X_e(s_D)=y].
\]
The forward semigroup is used when \(s_C\ge s_D\), and the stationary reverse semigroup when \(s_C<s_D\). The reverse operator is the adjoint and has the same L2 norm. Since conditional centering gives
\[
\int |\widetilde G_C(x;Z)|^2d\nu_e(x)
=\operatorname{Var}_{\nu_e}(G_C(\cdot;Z))
\le \|G_C\|_\infty^2,
\]
the one-link gap implies
\[
\|g(\cdot;Z)\|_2
\le \|G_C\|_\infty e^{-\Delta_0|s_C-s_D|}.
\tag{2.3}
\]

Define
\[
H_D(Z)=\mathbb E_{X_e(s_D)}
[g(X_e(s_D);Z)G_D(X_e(s_D);Z)].
\tag{2.4}
\]
Then
\[
\|H_D\|_\infty
\le \|G_C\|_\infty\|G_D\|_\infty
e^{-\Delta_0|s_C-s_D|}.
\tag{2.5}
\]
Moreover, the exact cumulant identity is
\[
\boxed{
\kappa(\widetilde G_C,G_D,G_{\rm rest})
=
\kappa(H_D,G_{\rm rest}).
}
\tag{2.6}
\]
To verify it, use the multivariate moment-generating function. For source variables u,v and the remaining sources \(\mathbf z\), differentiate \(\log\mathbb E e^{u\widetilde G_C+vG_D+\mathbf z\cdot G_{\rm rest}}\) first in u at u=0. At v=0 the numerator is zero because \(\mathbb E_e[\widetilde G_C\mid Z]=0\) and all remaining rows are independent of e. Differentiating in v at zero replaces the numerator by \(\mathbb E_e[g(X_e(s_D);Z)G_D\mid Z]\). This is precisely the first-source derivative of the log moment-generating function with H_D in place of the pair. Taking the remaining derivatives proves (2.6).

The second term is therefore the **contraction branch**: merge C and D, remove all link coordinates internal to their union (they are now private to the merged row), and retain the remaining external links. The merged row norm gains the factor in (2.5).

The argument remains valid when a link is evaluated at different original row times inside a super-row: the external links of a super-row each come from exactly one constituent original row, so each such link still has one well-defined endpoint time.

## 3. Weighted spanning-tree recurrence

Represent the current system by a multigraph whose vertices are current super-rows and whose labeled edges are links shared by exactly two super-rows. Give edge e the weight
\[
w_e=e^{-\Delta_0|s_C-s_D|}.
\]
Parallel edges are retained. Let
\[
\mathfrak T(H)=\sum_{T\text{ spanning tree of }H}\prod_{e\in T}w_e
\]
be its weighted spanning-tree polynomial.

For any non-loop edge e, the standard deletion–contraction identity is
\[
\mathfrak T(H)=\mathfrak T(H-e)+w_e\mathfrak T(H/e).
\tag{3.1}
\]
Equations (2.2)–(2.6), induction on the number of labeled link edges, and the fact that a cumulant vanishes when the current incidence graph is disconnected give
\[
|\kappa(G_1,\ldots,G_k)|
\le \left(\prod_{C}\|G_C\|_\infty\right)\mathfrak T(H).
\tag{3.2}
\]
The base case is one super-row, whose first cumulant is its expectation and is bounded by its sup norm. If H is disconnected, its link-coordinate families split into independent nonempty groups, so its joint cumulant is zero.

Initially, H has one vertex per original row and one labeled edge per shared link. Its weighted spanning-tree polynomial is
\[
\mathfrak T(H)
=
\sum_{T\in\mathcal T(G_X)}
\prod_{ij\in T}
\left(\sum_{e\in X_i\cap X_j}e^{-\Delta_0|t_i-t_j|}\right),
\]
which is exactly the right side of (1.2).

## 4. Scope and remaining obstruction

- The estimate is all-orders and noncoincident-time.
- It is support-restricted and applies to cyclic simple support graphs.
- It is exact with coefficient one when each adjacent row pair shares at most one link.
- If pairwise overlap multiplicity is bounded by \(m_*\), the simple-graph estimate has coefficient \(m_*^{r-1}\).
- The proof uses critically that each link path is incident to at most two current rows. If a link is incident to three or more original rows, there is no pairwise deletion–contraction edge: the centered branch contains a multi-row cumulant on that link, and (2.6) no longer applies. The corresponding hyperedge contraction/partition identity remains OPEN.

The 4D elementary plaquette family does not satisfy (1.1): a lattice link belongs to more than two plaquette boundaries. Therefore this theorem is a rigorous structural subcase, not yet the required PF-I16 face/pair insertion theorem. In particular, it does not close the actual degree-six-or-higher link-incidence problem, marked-root spatial summation, quantum KP convergence, interacting-vacuum Poincare inequality, or continuum mass gap.

No P0–P5 acceptance status is promoted.
