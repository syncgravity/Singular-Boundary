# PF-I16 — Factorial obstruction to a pure-exponential one-link quasi-factorization bound

**Date:** 2026-11-13  
**Scope:** one stationary reversible link process; the square-free coefficient in the Section 16 Boolean-lattice quasi-factorization variable. This rules out one proposed coefficient bound, not the joint space-time/KP strategy as a whole.

## 1. The coefficient in question

For a finite label set \(\Delta=[k]\), define
\[
u_\delta(\mathbf z)=\mathbb E\prod_{i\in\delta}(1+z_i f_i(U_{t_i})),
\qquad
P_\Delta(\mathbf z)=
\prod_{\delta\subseteq\Delta}
u_\delta(\mathbf z)^{(-1)^{k-|\delta|}}.
\]
The coefficient of \(z_1\cdots z_k\) in \(\log P_\Delta\) is the joint cumulant
\[
[z_1\cdots z_k]\log P_\Delta
=\kappa(f_1(U_{t_1}),\ldots,f_k(U_{t_k})).
\]
Since every nonconstant monomial in \(P_\Delta-1\) contains every \(z_i\), a product of two nonconstant monomials cannot contribute to the square-free monomial. Hence
\[
[z_1\cdots z_k](P_\Delta-1)
=[z_1\cdots z_k]\log P_\Delta
=\kappa(f_1(U_{t_1}),\ldots,f_k(U_{t_k})).
\]

## 2. Coincident-time Rademacher example

Take a single stationary random variable \(X\) with
\[
\mathbb P(X=1)=\mathbb P(X=-1)=\frac12,
\]
and set \(t_1=\cdots=t_k\), \(f_i=X\), so \(\|f_i\|_\infty=1\). Then the square-free coefficient is the repeated-variable cumulant
\[
\kappa_k(X,\ldots,X)
=\left.\frac{d^k}{dt^k}\log\mathbb E e^{tX}\right|_{t=0}
=\left.\frac{d^k}{dt^k}\log\cosh t\right|_{t=0}.
\]
For \(k=2n\), the Bernoulli-number formula is
\[
\kappa_{2n}
=\frac{2^{2n}(2^{2n}-1)}{2n}B_{2n}.
\]
Using
\[
|B_{2n}|\sim\frac{2(2n)!}{(2\pi)^{2n}},
\]
we obtain
\[
\boxed{
|\kappa_{2n}|
\sim2\left(\frac2\pi\right)^{2n}(2n-1)!.
}
\]
In particular,
\[
\lim_{n\to\infty}|\kappa_{2n}|^{1/(2n)}=\infty.
\]
Therefore no constant \(K<\infty\) can satisfy
\[
|\kappa_k(X,\ldots,X)|\le K^k
\]
for all \(k\). Since the temporal span is zero, the same counterexample rules out the proposed pure-exponential square-free coefficient bound with factor \(e^{-\Delta_0\operatorname{span}}\).

## 3. Corrected one-link target

The existing estimate
\[
|\kappa_k(f_1(U_{t_1}),\ldots,f_k(U_{t_k}))|
\le(2e)^k k!\,
e^{-\Delta_0(t_{\max}-t_{\min})}
\prod_i\|f_i\|_\infty
\]
has the correct factorial growth class. The Section 16 square-free target must retain a factor of order \(K^k k!\) (or \((k-1)!\)); a pure \(K^k\) coefficient target is impossible.

This does **not** prove that the quantum Feynman–Kac series diverges. In the time-integrated order-\(k\) coefficient, the factor \(1/k!\) and the integration of the full-span temporal decay may cancel the one-link factorial. What is still required is a joint estimate that performs that cancellation before summing spatially connected collections, while preserving the maximum-tree weight and the link-incidence structure.

## 4. Exact proof boundary

**Established:** the square-free coefficient identity; the coincident-time Rademacher counterexample; factorial asymptotics; compatibility of the existing one-link bound with the necessary growth class.

**Still open:** a factorial-compatible analytic majorant for all powers in \(P^e_\Delta\); the time-integrated cancellation with the Feynman–Kac \(1/k!\); the degree-eight product lift with at-most-exponential normalized growth; the connected-subset resummation; the all-orders joint space-time tree theorem; the actual quantum KP application and interacting-vacuum mass gap.

The obstruction is to an unnecessarily strong pure-exponential coefficient target, not to the underlying Yang–Mills construction.
