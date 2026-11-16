# PF-I16 — Markov path-block cumulant tree for separated temporal hulls

**Date:** 2026-11-15  
**Status:** ESTABLISHED for a fixed finite number q of bounded path-block observables whose temporal hull intervals are pairwise disjoint and ordered. The constant depends only on q, not on the number of sample times inside a block, the interval lengths, or the gaps. This is a restricted case of the local block-functional cumulant-tree target. Interlaced/overlapping hulls remain open.

## 1. Setup

Let (X_t) be a stationary reversible Markov process with semigroup (P_t), invariant law (pi), and
[
\|P_t-\Pi\|_{L^2(\pi)\to L^2(\pi)}\le e^{-\Delta_0t},
\qquad \Pi f=\pi(f)\mathbf1.
\tag{1.1}
]
Let (S_1,\ldots,S_q) be finite nonempty time sets, with ordered disjoint hulls
[
J_a=[u_a,v_a]=[\min S_a,\max S_a],
\qquad v_a<u_{a+1},\quad a=1,\ldots,q-1.
]
Let (G_a) be any bounded measurable function of the path coordinates ((X_s)_{s\in S_a}). Write (M_a=\|G_a\|_\infty) and (g_a=u_{a+1}-v_a>0).

## 2. Transfer-operator representation

For each block a, define its path transfer operator (K_a) from (u_a) to (v_a) by
[
(K_af)(x)=\mathbb E_x[G_a f(X_{v_a})],
]
where the conditional expectation includes all path coordinates in (S_a). If the block observable is absent from a moment, use (K_a^{(0)}=P_{v_a-u_a}); if present, use (K_a^{(1)}=K_a). Positivity and domination by the Markov semigroup imply
[
\|K_a^{(1)}\|_{2\to2}\le M_a,
\qquad \|K_a^{(0)}\|_{2\to2}\le1.
\tag{2.1}
]
For every (B\subseteq[q]), the joint moment is
[
m(B)=\mathbb E\prod_{a\in B}G_a
=
\langle\mathbf1,
K_1^{(\mathbf1_{1\in B})}P_{g_1}
K_2^{(\mathbf1_{2\in B})}\cdots
P_{g_{q-1}}K_q^{(\mathbf1_{q\in B})}
\mathbf1\rangle_\pi.
\tag{2.2}
]
Write each gap transition as (P_{g_j}=\Pi+R_j), with
[
\|R_j\|_{2\to2}\le e^{-\Delta_0g_j}.
\tag{2.3}
]

## 3. Exact gap-cancellation lemma

The classical cumulant is
[
\kappa(G_1,\ldots,G_q)
=
\sum_{\pi\in\Pi([q])}
(-1)^{|\pi|-1}(|\pi|-1)!
\prod_{B\in\pi}m(B).
\tag{3.1}
]
In each product indexed by π, there is one copy of every gap operator (P_{g_j}) for every block (B\in\pi). Expand every copy as (\Pi+R_j).

**Lemma.** In the fully summed expansion (3.1), all terms in which a fixed gap j uses (\Pi) in every block-copy cancel.

**Proof.** Replace (P_{g_j}) by (\Pi) in every moment (2.2). Since (\Pi) is the rank-one stationary projection, each such moment factors exactly into a left moment involving only (G_1,\ldots,G_j) and a right moment involving only (G_{j+1},\ldots,G_q). The resulting moment functional is the moment functional of two independent families. Its full joint cumulant is zero. This is an identity as a polynomial in all the other gap operators, so after expanding those other operators into (\Pi+R_k), cancellation holds coefficient by coefficient. \(\square\)

It follows that every nonzero monomial in the cumulant expansion contains at least one (R_j) for every gap j. Thus every surviving monomial carries the factor
[
\prod_{j=1}^{q-1}e^{-\Delta_0g_j}.
\tag{3.2}
]

## 4. Uniform block-functional tree estimate

For a partition π, the product of the operator norms of all local block operators in its moment factors is at most (prod_a M_a), because each G_a occurs in exactly one block. The expansion of the (|\pi|) copies of the (q-1) gap operators has at most (2^{(q-1)|\pi|}) terms. Therefore
[
\boxed{
|\kappa(G_1,\ldots,G_q)|
\le C_q
\left(\prod_{a=1}^qM_a\right)
e^{-\Delta_0\sum_{j=1}^{q-1}g_j},
\quad
C_q:=\sum_{\pi\in\Pi([q])}(|\pi|-1)!\,2^{(q-1)|\pi|}.
}
\tag{4.1}
]
This constant is finite for each q and independent of the number of time coordinates in each (S_a).

Now define the port-pair weight
[
W_{ab}=\sum_{s\in S_a,t\in S_b}e^{-\Delta_0|s-t|}.
]
Because the hulls are disjoint and ordered, (W_{a,a+1}\ge e^{-\Delta_0g_a}), using the last port of (S_a) and first port of (S_{a+1}). The path on block labels is a spanning tree of the complete graph (K_q). Hence
[
\boxed{
|\kappa(G_1,\ldots,G_q)|
\le C_q\left(\prod_aM_a\right)
\sum_{T\in\mathcal T(K_q)}
\prod_{\{a,b\}\in T}W_{ab}.
}
\tag{4.2}
]
This proves the desired block-level cumulant-tree form for pairwise disjoint temporal hulls, with a constant independent of each block's number of ports.

## 5. Boundary

- Arbitrary bounded path functionals on pairwise disjoint ordered hulls: **ESTABLISHED**.
- The number of sample times in each block and the horizon: unrestricted.
- The number q of blocks: fixed; in the PF-I16 application it is at most the distinct-support incidence cap (232), so (C_q\le\max_{1\le s\le232}C_s<\infty).
- Interlaced port sets whose hulls overlap: **OPEN**. Compressing them to their hull intervals loses the finer port-pair weights; the parity/HGR obstruction prevents replacing the missing higher-order argument by pairwise conditional correlation alone.
- The general repeated-support local block-functional theorem, cyclic hyperedges of arity at least four, KP convergence, interacting-vacuum Poincaré, scale setting, and the continuum mass gap remain open.

The companion verifier uses exact rational finite-state Markov paths to check the operator-gap reset cancellation and the resulting cumulant decay for several multi-time block functions. It is a regression for the algebraic cancellation mechanism, not a proof of the infinite-dimensional semigroup norm bound. No P0–P5 gate is promoted.
