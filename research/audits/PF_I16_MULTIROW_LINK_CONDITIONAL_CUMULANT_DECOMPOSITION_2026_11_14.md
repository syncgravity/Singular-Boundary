# PF-I16 — Conditional cumulant decomposition at a multi-row shared link

**Date:** 2026-11-14  
**Status:** Exact conditional-cumulant identity ESTABLISHED; recursive temporal support-tree closure OPEN.  
**Scope:** one link path shared by an arbitrary finite set of rows, independent of all other link paths. No P0–P5 gate is promoted.

## 1. Setup

Fix a link e and let
\[
I_e=\{i:e\in X_i\}
\]
be its incident row set. Write Z for the collection of all other link paths. Conditional on Z, each incident row is a bounded one-time function of the e-state:
\[
A_i=f_i(X_e(t_i);Z),\qquad i\in I_e,
\]
while every nonincident row is Z-measurable. The link path is independent of Z and has stationary semigroup with
\[
\|P_s^e-\Pi_e\|_{2\to2}\le e^{-\Delta_0s}.
\]

## 2. Exact law-of-total-cumulance reduction

For each nonempty block B subset I_e, define the conditional cumulant
\[
H_B(Z)=\kappa_e\bigl(f_i(X_e(t_i);Z):i\in B\mid Z\bigr),
\tag{2.1}
\]
where the cumulant is taken only over the stationary link-e path, with Z fixed.

The law of total cumulance gives the exact identity
\[
\boxed{
\kappa(A_1,\ldots,A_r)
=
\sum_{\pi\in\Pi(I_e)}
\kappa_Z\Bigl(
(H_B(Z))_{B\in\pi},
(A_j)_{j\notin I_e}
\Bigr).
}
\tag{2.2}
\]
Here the outer cumulant is over the other link paths. In the general law-of-total-cumulance partition sum over all rows, any block containing a nonincident row and at least one other row has zero conditional cumulant: the nonincident row is constant under conditioning on Z. Hence nonincident rows must remain singleton blocks, leaving exactly the partitions of I_e in (2.2).

For a singleton block B={i},
\[
H_{\{i\}}(Z)=\mathbb E_e[A_i\mid Z],
\]
so that row has had link e removed from its support. For |B|≥2, H_B is a new merged row observable supported on the union of the other-link coordinates used by rows in B.

## 3. Conditional single-link tree bound

For every fixed Z, the variables in (2.1) are bounded insertions along one stationary Markov path. The already-established global projection-tree cumulant theorem for a one-link process gives
\[
|H_B(Z)|
\le
4^{|B|}
\left(\prod_{i\in B}M_i\right)
\sum_{T\in\mathcal T(K_B)}
\prod_{\{i,j\}\in T}
e^{-\Delta_0|t_i-t_j|},
\qquad |B|\ge2.
\tag{3.1}
\]
This estimate is uniform in Z. It uses the single-link semigroup gap, not a termwise absolute sum over chronological slot partitions. For singleton B, simply \(|H_B(Z)|\le M_i\).

Thus a shared link of incidence q creates a finite partition expansion with at most Bell(q) blocks, and each nontrivial block carries a temporal tree on its incident rows.

## 4. The precise remaining obstruction

Equation (2.2) is an exact and useful first step toward the multi-row hyperedge case. It is not yet an all-orders support-tree proof.

If B contains two or more rows that also share another link e' with a row outside B, then H_B may depend on the e'-path at several distinct original times. It is therefore a path-functional super-row, not necessarily a one-time insertion on e'. The pair-incidence deletion–contraction theorem cannot yet be applied recursively to such super-rows without a new estimate for cumulants of multi-time path-functional super-rows.

The missing lemma is a **multi-time super-row contraction bound**: when several current super-rows depend on the same link path at finite sets of times, their outer cumulant must admit a temporal support-tree bound whose bonds can be assigned to actual original row pairs sharing that link. A proof must preserve the signed outer cumulant and avoid losing the desired edge-specific temporal factors.

For PF-I16 face observables, each elementary lattice link is incident to finitely many plaquette rows (six in four dimensions), and each face row has four boundary links. Thus the local partition count is bounded by Bell(6), while the total number of row-link incidences is linear in the number of rows. This suggests that the purely combinatorial partition overhead can be absorbed into an exponential-in-order constant. It does **not** by itself prove the multi-time super-row contraction estimate.

## 5. Disposition

- Pair-incidence case (each link in at most two row supports): all-orders weighted support-tree theorem ESTABLISHED in the companion pair-incidence audit.
- One-link conditional cumulant tree bound: ESTABLISHED by the product-process projection-tree theorem.
- Exact multi-row conditional cumulant decomposition (2.2): ESTABLISHED.
- Iteration of (2.2) while retaining support-restricted temporal bonds for multi-time super-rows: OPEN.
- Marked-root spatial summation, quantum KP convergence, interacting-vacuum Poincare inequality, and continuum mass gap: OPEN.

No P0–P5 acceptance status is promoted.
