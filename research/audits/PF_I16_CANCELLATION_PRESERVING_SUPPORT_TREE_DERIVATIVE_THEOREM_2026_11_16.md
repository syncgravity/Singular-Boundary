# PF-I16 — Failure of the naive differentiated-cumulant cancellation

**Date:** 2026-11-16  
**Status:** proposed cancellation identity REFUTED by an exact three-row Markov example  
**Scope:** correction to the link-compressed support-graph BKAR derivative strategy. The support-graph interpolation and full-moment operator insertion estimate remain valid; the attempted cumulant cancellation does not.

## 1. The failed inference

The attempted argument was:
- a parameter \(\lambda_{ij}\) occurs in a block moment only if that block contains both \(i\) and \(j\);
- therefore, for a connected tree \(T\), a mixed derivative \(\partial_T\) of the moment-cumulant formula kills every nontrivial partition;
- hence \(\partial_T\kappa=\partial_T M_{[R]}\).

The first bullet is false. A marginal moment retaining ports on both sides of an omitted transition depends on that transition parameter through the product of intervening kernels. For consecutive full ports \(i,j\), if selected ports \(a\) and \(b\) lie respectively before \(i\) and after \(j\), then
\[
K_{a i}K_{i j}K_{j b}
=\Pi+\lambda_{ai}\lambda_{ij}\lambda_{jb}Q_{t_b-t_a}.
\]
The selected block need not contain either endpoint \(i,j\) for \(\lambda_{ij}\) to survive; it is enough to retain ports on both sides.

## 2. Exact three-row counterexample

Take one stationary two-state Markov chain \(Y_t\in\{0,1\}\) with
\[
\mu(Y=1)=p=\frac13,\qquad X_t=Y_t-p.
\]
Choose its one-step transition operator so that the centered coordinate is an eigenfunction with eigenvalue \(\rho=1/2\):
\[
P(x,\{1\})=p+\rho(x-p),\qquad x\in\{0,1\}.
\]
Thus \(P(1,1)=2/3\), \(P(0,1)=1/6\), and \(\mu\) is stationary.

Use three ports at times \(0,1,2\) on this same link, with the link-compressed interpolation
\[
K_{01}=\Pi+\lambda_{01}Q,\qquad
K_{12}=\Pi+\lambda_{12}Q,\qquad Q=P-\Pi.
\]
Let
\[
A_1=X_0,\qquad A_2=1+X_1,\qquad A_3=X_2.
\]
Set \(v=\mathbb E X^2=p(1-p)=2/9\) and
\(\mu_3=\mathbb E X^3=p(1-p)(1-2p)=2/27\).

Stationarity and the eigenfunction relation give
\[
\begin{aligned}
M_1&=M_3=0,\qquad M_2=1,\\
M_{12}&=\lambda_{01}\rho v,\\
M_{23}&=\lambda_{12}\rho v,\\
M_{13}&=\lambda_{01}\lambda_{12}\rho^2v,\\
M_{123}&=\lambda_{01}\lambda_{12}\rho^2(v+\mu_3).
\end{aligned}
\]
The third cumulant is therefore
\[
\kappa(A_1,A_2,A_3)
=M_{123}-M_{13}M_2
=\lambda_{01}\lambda_{12}\rho^2\mu_3.
\]
Consequently,
\[
\boxed{
\partial_{\lambda_{01}}\partial_{\lambda_{12}}\kappa
=\rho^2\mu_3=\frac1{54},
}
\]
whereas
\[
\boxed{
\partial_{\lambda_{01}}\partial_{\lambda_{12}}M_{123}
=\rho^2(v+\mu_3)=\frac2{27}.
}
\]
The difference is
\[
\rho^2v=\frac1{18}\ne0.
\]
It comes precisely from the nontrivial partition \(\{\{1,3\},\{2\}\}\): the block moment \(M_{13}\) depends on both transition parameters even though it omits row 2.

Thus the identity
\(\partial_T\kappa=\partial_T M_{[R]}\) is false, already for \(R=3\) and a reversible finite-state chain.

## 3. What remains valid

The following parts of the previous construction are unaffected:

1. The link-compressed interpolation is a genuine family of stationary Markov laws.
2. Omitted-port marginals are projectively consistent, with effective parameter equal to the product of the intervening \(\lambda\)'s.
3. If the positive-parameter support graph disconnects, a zero-parameter reset separates every link chain crossing the cut; hence the cumulant vanishes.
4. The support-graph BKAR forest representation is valid.
5. For the **full joint moment**, a mixed derivative along a tree can be expanded by assigning each differentiated edge to one shared link transition. There are at most \(m^{R-1}\) assignments, and each assignment is bounded by
\[
\left(\prod_{i,e\in X_i}\|f_{i,e}\|_\infty\right)
\prod_{\{i,j\}\in T}e^{-\Delta_0|t_i-t_j|}.
\]
This is a bound on \(\partial_T M_{[R]}\), not on \(\partial_T\kappa\).

## 4. Corrected remaining obstacle

A valid proof must control the differentiated moment-cumulant sum while retaining the interval structure of omitted-port marginals. The counterexample shows that one cannot discard all nontrivial partitions merely from connectivity of the differentiated support tree.

A possible combinatorial object is the *port hull* of a block: for each link, the interval between its first and last retained ports. A transition parameter contributes to a block moment whenever its port edge lies inside one of these hulls. Mixed derivatives therefore select partitions whose block port hulls cover the differentiated tree edges. The required estimate must sum these admissible partitions with their Möbius signs, rather than taking absolute values termwise.

No uniform \(C_m^R\) bound for this signed sum is established here. No support-localized cumulant-tree theorem is claimed from this route.

## 5. Scope

This is a correction to the attempted derivative-cancellation proof, not a refutation of the desired support-localized cumulant bound itself. The exact example shows only that this proposed shortcut is invalid. The Yang–Mills mass-gap proof remains open; no P0–P5 gate is promoted.
