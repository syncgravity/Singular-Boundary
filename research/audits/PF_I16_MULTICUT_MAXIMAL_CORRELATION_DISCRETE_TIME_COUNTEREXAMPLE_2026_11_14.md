# PF-I16 — Discrete-time counterexample to the proposed multi-cut HGR bound

**Date:** 2026-11-14  
**Status:** Exact finite-state counterexample; continuous-time semigroup version remains OPEN.  
**Scope:** The proposed two-cut inequality is false for general stationary discrete-time Markov kernels. This does not refute the continuous-time Markov-semigroup formulation.

## 1. Candidate statement being tested

For ordered observations at times 0, 1, 2 with colors S,T,S, the conjecture would give
\[
\rho_{\max}(\sigma(X_0,X_2),\sigma(X_1))
\le \tanh(2\operatorname{arctanh}q)
=\frac{2q}{1+q^2},
\qquad q=\|P-\Pi\|_{L^2(\pi)\to L^2(\pi)}.
\tag{1}
\]
The one-step contraction is exactly q.

## 2. Rational stationary counterexample

Take
\[
P=\begin{pmatrix}
130/1000&539/1000&331/1000\\
52/1000&947/1000&1/1000\\
956/1000&36/1000&8/1000
\end{pmatrix},
\qquad
\pi=\frac1{308613}(26270,273302,9041).
\tag{2}
\]
Every row of P sums to one, every entry is positive, and direct rational multiplication gives \(\pi P=\pi\).

For the stationary chain \(X_0,X_1,X_2\), define the joint law of \(((X_0,X_2),X_1)\) by
\[
J_{(a,b),y}=\pi_aP_{ay}P_{yb}.
\tag{3}
\]
The maximal correlation is the second singular value of
\(D_{p_{(X_0,X_2)}}^{-1/2}J D_{p_{X_1}}^{-1/2}\).
The one-step contraction q is the largest singular value of the restriction of P to the centered \(L^2(\pi)\) subspace.

Numerical SVD of these explicitly rational matrices gives
\[
q\approx0.5898802493,\qquad
\rho_{\max}( (X_0,X_2),X_1)\approx0.8969370325,
\]
while
\[
\tanh(2\operatorname{arctanh}q)
=\frac{2q}{1+q^2}
\approx0.8752200577.
\]
Thus the proposed inequality fails by approximately 0.0217169749.

## 3. Interpretation and scope

- The counterexample refutes (1) for arbitrary stationary discrete-time Markov kernels, including strictly positive three-state kernels.
- It shows that a proof cannot use only a one-step centered-L2 contraction estimate and then apply the proposed hyperbolic-tangent addition rule.
- This matrix has a simple negative real eigenvalue, so it is not the time-one map of a finite-dimensional continuous-time Markov generator (a real matrix logarithm cannot have a single simple negative eigenvalue). Consequently this example does **not** settle the continuous-time Markov-semigroup version in the original audit.
- The continuous-time semigroup inequality remains a conjecture, not a theorem. It must be proved using genuinely continuous-time structure or replaced by a valid bound.

## 4. Disposition

- Discrete-time multi-cut HGR inequality (1): **REFUTED**.
- Continuous-time stationary Markov-semigroup multi-cut inequality: **OPEN**.
- Multi-time super-row cumulant tree with original-row support bonds: **OPEN**.
- No P0–P5 acceptance status is promoted.
