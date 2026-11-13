# PF-I16 — Exact fourth-order partition algebra and disconnected-factorization cancellation

**Date:** 2026-11-13  
**Status:** exact finite-label perturbation algebra and exact independent-subsystem cancellation. The spatial four-support tree estimate remains open. This record does not import R3-IR constants or claim that disjoint supports on a connected Penrose–Fibonacci graph are independent.

## 1. Centered reduced-resolvent recursion

Work with the finite dressed reference generator \(L=L_\Phi\), invariant probability \(\pi=\nu_\Phi\), centered projection \(Q=1-\Pi\), and self-adjoint reduced resolvent \(G=L^{-1}Q\). For distinct residual labels \(I\), perturb
\[
L(\mathbf t)=L-\sum_{i\in I}t_ir_i,\qquad \pi(r_i)=0,
\]
and normalize the eigenfunction as \(1+u(\mathbf t)\) with \(\pi(u)=0\). The exact squarefree coefficient recursion is
\[
E_I=-\sum_{i\in I}\pi(r_i u_{I\setminus\{i\}}),
\]
\[
u_I=G\left[
\sum_{i\in I}r_i u_{I\setminus\{i\}}
+\sum_{\varnothing\ne J\subsetneq I}E_Ju_{I\setminus J}
\right].
\tag{1.1}
\]
This is the finite-label recursion; no spatial estimate is used in this section.

For four distinct labels \(I=\{i,j,k,l\}\), put
\[
A_i=Gr_i,\qquad
Q_{ij}=r_iA_j+r_jA_i,\qquad
B_{ij}=GQ_{ij}.
\]
Self-adjointness gives
\[
E_{ij}=-2\pi(r_iA_j)=-\pi(Q_{ij}),
\qquad
u_{ij}=B_{ij}.
\tag{1.2}
\]
The third-order eigenfunction coefficient is
\[
u_{ijk}=G\left[
r_iB_{jk}+r_jB_{ik}+r_kB_{ij}
+E_{ij}A_k+E_{ik}A_j+E_{jk}A_i
\right].
\tag{1.3}
\]
The fourth-order energy coefficient is exactly
\[
E_{ijkl}=-\sum_{m\in I}\pi(r_m u_{I\setminus\{m\}}).
\tag{1.4}
\]

## 2. The complete 36-term expansion

Apply self-adjointness to (1.4), substituting (1.3). This gives
\[
\begin{aligned}
E_{ijkl}={}&-\sum_{m\in I}\sum_{a\in I\setminus\{m\}}
\pi\!\left[A_m r_a B_{I\setminus\{m,a\}}\right]\\
&-\sum_{m\in I}
\sum_{\substack{\{a,b\}\subset I\setminus\{m\}\\
\{c\}=I\setminus\{m,a,b\}}}
E_{ab}\,\pi(A_mA_c).
\end{aligned}
\tag{2.1}
\]
The first line has \(4\cdot3=12\) terms before expanding \(B_{cd}\). Since
\[
B_{cd}=G(r_cA_d+r_dA_c),
\]
it contributes 24 nested-resolvent monomials. The second line has \(4\cdot3=12\) pair-energy monomials. Thus (2.1) is the full 36-term expression.

Group terms by the three unordered pair partitions
\[
(ij|kl),\qquad(ik|jl),\qquad(il|jk).
\]
For a fixed partition \((ij|kl)\), the four ordered choices of \((m,a)\) are
\[
(i,j),\ (j,i),\ (k,l),\ (l,k).
\]
The corresponding nested terms combine to
\[
\pi(Q_{ij}GQ_{kl})+\pi(Q_{kl}GQ_{ij})
=2\pi(Q_{ij}GQ_{kl}),
\]
where the last equality is self-adjointness of \(G\). The pair-energy terms for the same partition combine to
\[
2E_{ij}\pi(A_kA_l)+2E_{kl}\pi(A_iA_j).
\]
Repeating for all three pair partitions yields the exact compact identity
\[
\boxed{
E_{ijkl}=-2\sum_{\{ij|kl\}}
\left[
\pi(Q_{ij}GQ_{kl})
+E_{ij}\pi(A_kA_l)
+E_{kl}\pi(A_iA_j)
\right].
}
\tag{2.2}
\]
Each channel contains eight nested monomials and four pair-energy monomials. The three channels together account for all 36 terms.

The pair-energy corrections in (2.2) are essential. It is not valid to keep only the nested-resolvent terms, nor to declare the three pair-partition channels separately zero.

## 3. Exact cancellation under independent subsystem factorization

Suppose the full finite dressed system genuinely factors over independent subsystems:
\[
L=\sum_{\alpha=1}^m
1\otimes\cdots\otimes L_\alpha\otimes\cdots\otimes1,
\qquad
\pi=\bigotimes_{\alpha=1}^m\pi_\alpha,
\]
and each residual \(r_i\) acts on exactly one subsystem. The perturbed operator is then a sum of commuting subsystem operators,
\[
L(\mathbf t)=\sum_{\alpha=1}^m
\left(L_\alpha-\sum_{i\in I_\alpha}t_ir_i\right).
\]
Its lowest eigenvalue is additive:
\[
E(\mathbf t)=\sum_{\alpha=1}^m E_\alpha(\mathbf t_{I_\alpha}).
\tag{3.1}
\]
A summand on the right depends only on source variables belonging to one subsystem. Therefore, if the four labels meet more than one independent subsystem,
\[
\boxed{[t_it_jt_kt_l]E(\mathbf t)=E_{ijkl}=0.}
\tag{3.2}
\]
This proves the exact disconnected-factorization cancellation for every partition type:
\[
1+3,\qquad2+2,\qquad1+1+2,\qquad1+1+1+1.
\]
It is an algebraic consequence of tensor-product factorization and additivity of the ground energy, not an estimate.

### Explicit \(2+2\) check

Let \(i,j\) act on subsystem \(A\), and \(k,l\) on subsystem \(B\). Define
\[
A_i^A=G_Ar_i,\quad B_{ij}^A=G_A(r_iA_j^A+r_jA_i^A),
\]
and analogously on \(B\). Since each reduced-resolvent output is centered,
\[
\pi_A(A_i^A)=\pi_A(B_{ij}^A)=0,\qquad
\pi_B(A_k^B)=\pi_B(B_{kl}^B)=0.
\]
The product eigenfunction coefficients are
\[
u_{ik}=A_i^AA_k^B,\quad
u_{ij}=B_{ij}^A,\quad u_{kl}=B_{kl}^B,
\]
\[
u_{ijk}=B_{ij}^AA_k^B,\quad
u_{ikl}=A_i^AB_{kl}^B,\quad
u_{ijkl}=B_{ij}^AB_{kl}^B.
\]
For example,
\[
L(B_{ij}^AB_{kl}^B)
=(Q_{ij}+E_{ij})B_{kl}^B
+B_{ij}^A(Q_{kl}+E_{kl}),
\]
which is exactly the fourth-order recursion after the cross-component pair energies vanish. Substitution in (1.4) leaves only terms containing either \(\pi_A(B_{ij}^A)\) or \(\pi_B(B_{kl}^B)\), so \(E_{ijkl}=0\). This confirms explicitly that the pair-energy terms are required for the product recursion.

The general argument (3.1) proves the other three partition types without separate case-by-case coefficient expansions.

## 4. What the cancellation does not say

The factorization hypothesis is stronger than disjointness of residual supports. On a connected accepted Penrose–Fibonacci graph, separated supports can still communicate through intermediate face interactions and the dressed generator. Thus (3.2) does **not** imply that \(E_{ijkl}\) vanishes, or is small, merely because the four residual supports are disjoint or far apart.

Likewise, the three channels in (2.2) need not vanish separately, even in a genuinely independent \(2+2\) decomposition. Their cancellation is a property of the complete sum. Taking absolute values channel by channel can erase the only mechanism that removes the disconnected contribution.

The remaining spatial problem is therefore:

> Prove a volume-independent four-support spanning-tree estimate for the full sum (2.2), retaining cancellation among all three pair-partition channels.

The preserved branch source also records a cut-interpolation identity for the fourth-order coefficient. Its spatial estimate still requires differentiating the normalized eigenfunction, measure-centering term, and eigenvalue terms together; that step is not certified here.

## 5. Proof ledger

**Exact finite algebra:** recursion (1.1); 36-term formula (2.1); three-channel identity (2.2); exact independent-subsystem cancellation (3.2).

**Finite-dimensional verification:** the accompanying script checks the 36-term enumeration, pair-partition grouping counts, and the equality of the recursion and pair-channel formulas on random finite reversible generators. This is an algebraic regression check, not a substitute for the proof above.

**Open:** spatial four-support tree decay on the connected PF-I16 graph; cut-response estimates for the interpolation identity; all-orders connected activity summability; physical-time normalization; continuum reconstruction; Yang–Mills mass gap.

No R3-IR constants or path-cumulant estimates are imported. The preserved branch source "sources/originals/session-2026-11-11/Branch · Branch · Continue PF116 Objective (1).md" (SHA f1687cc7fb75e7b2b31139d48462932b7d68e761) is retained as historical provenance; this proof record independently restates the finite algebra and separates it from the spatial claim.
