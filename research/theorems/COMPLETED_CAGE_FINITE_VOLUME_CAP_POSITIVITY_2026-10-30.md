# Nonperturbative finite-volume cap positivity for completed magnetic cages

**Date:** 2026-10-30  
**Status:** exact finite-volume positivity/comparison theorem for the actual physical SU(2) Wilson vacuum; constants are **not** uniform in volume or strong-coupling scaling. Does not close R3-IR, signed-current, or continuum gap.  
**Source:** new proof developed from original-link elliptic heat-kernel and Feynman–Kac comparison; distinguish from CI-1/CI-2 and cut-cage perturbation.

## Setting

Let \(E\) be finite and \(G=SU(2)^E\) with normalized product Haar measure \(\mu\). Work with \(T=\sum_{e\in E}a_e(-\Delta_e)\), all \(a_e>0\), and any bounded, nonnegative, continuous gauge-invariant magnetic potential \(V\) with \(0\le V\le K<\infty\). The physical Hilbert space is the subspace invariant under the **full original vertex Gauss group**. The Wilson case has \(V=b\sum_{q\in Q}c_q(1-p_q)\), \(p_q=\frac12\operatorname{Tr}W_q\), so \(K=2b\sum_{q\in Q}c_q\). The deleted-target model allows \(f\notin Q\); neither incomplete-cage nor a spectral-gap assumption is imposed.

For any \(t>0\), let \(k_t(x,y)\) be the strictly positive smooth kernel of \(e^{-tT}\) with respect to \(\mu\), and set \(m_t=\min_{G\times G}k_t>0\), \(M_t=\max_{G\times G}k_t<\infty\), and
\[
R_t=e^{tK}\frac{M_t}{m_t}.
\]
This is a finite explicit constant once finite-volume link coefficients and \(t\) are given.

## Theorem: global density comparison

Let \(\Omega>0\) be the \(L^2(\mu)\)-normalized ground state of \(H=T+V\). Then \(\Omega\) is gauge invariant and is the unique ground state in the physical subspace. Its pointwise oscillation obeys
\[
\frac{\sup_G\Omega}{\inf_G\Omega}\le R_t\qquad(t>0).
\]
Consequently, for any measurable \(A\subset G\),
\[
R_t^{-2}\mu(A)\ \le\ \nu(A):=\int_A\Omega^2d\mu\ \le\ R_t^2\mu(A).
\tag{1}
\]
For any measurable \(A,B\subset G\) with \(\mu(B)>0\),
\[
R_t^{-4}\mu(A\mid B)\le\nu(A\mid B)\le R_t^4\mu(A\mid B),
\tag{2}
\]
where conditioning is defined by normalized restriction of \(\mu\) or \(\nu\) to \(B\).

If \(B\) is a target trace event \(p_f=\cos u\), \(0\le u\le a\le\pi\), then regardless of whether its cage is complete,
\[
\nu(u\le a)\ \ge\ R_t^{-2}\,m_H(a),\qquad m_H(a)=\frac{a-\frac12\sin(2a)}{\pi}.
\tag{3}
\]
In particular every finite-volume completed-cage ground state gives positive probability to every nonempty center cap, but (3) has no regulator-uniform force without a bound on \(R_t\).

## Proof

On the connected compact group product, \(H\) is elliptic and its heat semigroup is positivity improving, hence has a unique continuous strictly positive normalized ground state. Since the Hamiltonian commutes with the full original vertex Gauss group, uniqueness makes this ground state Gauss invariant; the physical ground energy is the unrestricted one.

The bounded-potential Feynman–Kac formula, or Trotter product plus order preservation, gives the pointwise positive-semigroup comparison
\[
e^{-tK}(e^{-tT}g)(x)\le(e^{-tH}g)(x)\le(e^{-tT}g)(x)
\]
for every \(g\ge0\). Since \(H\Omega=E_0\Omega\),
\[
e^{tE_0-tK}m_t\int_G\Omega\,d\mu
\le\Omega(x)
\le e^{tE_0}M_t\int_G\Omega\,d\mu.
\]
Dividing the upper by the lower bound cancels \(e^{tE_0}\) and produces \(R_t\). Write \(m=\inf_G\Omega\) and \(M=\sup_G\Omega\); then \(M/m\le R_t\) and \(1=\int\Omega^2d\mu\) implies \(m\le1\le M\), hence \(m\ge R_t^{-1}\) and \(M\le R_t\). Integration over measurable \(A\) yields (1). Apply (1) to \(A\cap B\) and \(B\), divide and obtain (2). Under product Haar, any original-link Wilson loop with at least one link appearing exactly once has Haar-distributed based holonomy; a simple target face does, so its class angle has density \(2\sin^2u/\pi\). Integrating over \([0,a]\) gives \(m_H(a)\) and (3). QED.

## Why this does not close the proof

1. \(K=2b\sum c_q\) grows with retained magnetic volume and strong-field \(b\). The ratio \(M_t/m_t\) also depends on the dimension \(|E|\) and small link diffusion coefficients; no uniform \(R_t\) has been established.
2. Pointwise positivity of the true ground state does not control the sign of its target radial logarithmic derivative or the positive score-current budget \(\mathfrak T_{f,h}\).
3. This is a genuine completed-cage statement but its constant is deliberately **global and poor**. The missing theorem is a *local*, signed, scale-robust conditional density/energy comparison in the nonlinear interacting vacuum.
4. Formula (2) is a bound relative to unweighted full product Haar conditioning. It is **not** independence of the retained traces, nor a small-defect estimate for strongly coupled faces.

### Next mathematical step

Construct a target-fiber **local** semigroup or conditional-energy comparison whose constants depend on a bounded collar rather than \(\sum_{q\in Q}c_q\), and then control the far-field through a separately proved nonlinear mixing/response estimate. If this fails, identify the low-frequency obstruction using the exact radial-score Ward identity. Do not assume a mass gap to prove the mass gap.
