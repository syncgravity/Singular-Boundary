# The Singular Boundary — Quantitative local SU(2) excitation f-sum lower bound

**Independent continuation, 2026-11-04.** Intended as a narrowly scoped follow-on to P-53/P-55 and P-78 of the corrected original-link SU(2) *finite open straight strip* program. No assertion about a 3D Penrose regulator, an interacting infinite-volume spectral gap, Borel summability, or the 4D Yang–Mills mass gap is made. The estimates below are established from the earlier stated local kinetic bound and f-sum identity; the upstream source theorems are used as inputs rather than re-proved here.

## Hypotheses and conventions

1. The single face holonomy is SU(2), identified with the **unit round three-sphere** S³; write \(x=\operatorname{Re}U\in[-1,1]\), \(\chi_1(U)=2x\), \(q(U)=1-x^2\).
2. The positive one-face electric Casimir is \(C=-\tfrac14\Delta_{S^3}\), so \(C\chi_1=\tfrac34\chi_1\). Normalized Haar probability is the Riemannian probability volume on S³.
3. \(p\,dU\) is a one-site diagonal marginal from a P-53/P-55 translation-averaged finite-volume ground-state construction or a corresponding thermodynamic subsequential limit, with \(\phi=\sqrt p\in H^1(S^3)\), \(\int\phi^2\,dU=1\), and
   \[\langle\phi,C\phi\rangle\le |\lambda|/2.\]
4. For the spectral interpretation only, use the genuine P-78 local Dirichlet/f-sum identity for \(f=\chi_1\):
   \[m_1:=\int_0^\infty E\,d\mu^{\chi_1,\chi_1}(E)=4-\nu(\chi_1^2).\]
   Here \(\mu\) is the nonnegative excitation-frequency measure of the P-78 *anchor-averaged limit*, not an independently established spectral measure of a common infinite-volume Hamiltonian.

## New theorem

For every normalized \(\phi\in H^1(S^3)\), with \(T=\int_{S^3}|\nabla\phi|^2\,dU\) and \(Q=\int_{S^3}q\phi^2\,dU\),
\[
\boxed{4Q\ \ge\ b(T):=\frac{2\bigl(6+T-\sqrt{T(T+3)}\bigr)}{4+T}.}
\]
This holds without radiality or conjugation-invariance assumptions on \(\phi\). The function \(b(T)\) is positive and strictly decreasing for \(T>0\), with \(b(0)=3\).

Applying the P-53/P-55 local kinetic-energy estimate \(T=4\langle\phi,C\phi\rangle\le2|\lambda|\), we obtain the **uniform, explicitly quantitative local excitation-energy sum rule**
\[
\boxed{\begin{aligned}
\int_0^\infty E\,d\mu_\infty^{\chi_1,\chi_1}(E)
&=4-\nu_\infty[\chi_1(U_0)^2]\\
&\ge b(2|\lambda|)\\
&=\frac{6+2|\lambda|-\sqrt{4|\lambda|^2+6|\lambda|}}{2+|\lambda|}>0.
\end{aligned}}
\]
The bound is independent of finite strip length and choice of anchor-averaged thermodynamic subsequence, under the stated antecedent bounds. At \(\lambda=0\), equality holds for Haar. At \(|\lambda|=1\), the bound is \((8-\sqrt{10})/3\approx1.612574113277\).

### Proof

On the unit round S³, the radial Laplacian acting on \(F(x)\) is
\[\Delta_{S^3}F=(1-x^2)F''-3xF'.\]
Consequently,
\[
\Delta_{S^3}q=6-8q,\qquad|\nabla q|^2=4q(1-q).
\]
As \(q\) is smooth and \(\phi\in H^1\), weak integration by parts yields
\[
6-8Q=\int(\Delta q)\phi^2
=-2\int\phi\,\nabla\phi\cdot\nabla q.
\]
Cauchy–Schwarz and Jensen give
\[
|6-8Q|
\le 2\sqrt{T\int|\nabla q|^2\phi^2}
=4\sqrt{T\int q(1-q)\phi^2}
\le4\sqrt{TQ(1-Q)}.
\]
If \(Q\ge3/4\), the displayed theorem is immediate because its right-hand side is at most 3. Otherwise \(6-8Q>0\) and squaring yields
\[
(4+T)Q^2-(6+T)Q+9/4\le0.
\]
The lower root of this quadratic is
\[
Q_- = \frac{6+T-\sqrt{T(T+3)}}{2(4+T)},
\]
so \(Q\ge Q_-\) and \(4Q\ge b(T)\). Direct differentiation shows
\[
b'(T)= -\frac{4\sqrt{T(T+3)}+5T+12}{\sqrt{T(T+3)}(T+4)^2}<0,\quad T>0.
\]
Substitute \(T\le2|\lambda|\) and the P-78 exact f-sum identity. QED.

## Spectral meaning and limitations

This proves **nonvanishing positive first excitation-frequency moment** quantitatively. It is not a lower bound on the bottom of the positive spectral support. In particular, spectral weight can accumulate arbitrarily close to energy zero while this first moment remains bounded below. The estimate does not prove any finite-volume or infinite-volume spectral gap, a common interacting time-evolution group, uniqueness of the thermodynamic state, or spatial clustering. The one-dimensional straight-strip model is also not a source-certified 3D spatial regulator or a 4D continuum construction.

The result strengthens the P-78 qualitative \(m_1>0\) theorem and is robust under every P-55 subsequential locally normal state carrying the P-53 diagonal kinetic bound. It does not resolve P-77's extensive Gauss-invariant Schatten response or the P0 model-identification gate.

## Independent verification

`verify_quantitative_fsum.py` checks symbolically the S³ differential identities, quadratic root, derivative sign, and exact coupling special cases. It also performs 24 high-precision Gauss-Jacobi quadrature regression checks on positive smooth nonconstant radial densities. The symbolic proof above, not the finite regression tests, establishes the general inequality.

**Research classification:** new conditional corollary of recorded P-53/P-55/P-78 results, with a self-contained intrinsic S³ inequality. No new continuum theorem.

**Primary cited research records:**
- `research/audits/P2_BERNSTEIN_SCHATTEN_THERMODYNAMIC_LOCAL_MEASURES_2026-11-04.md` (P-53)
- `research/audits/P2_CENTRAL_BINOMIAL_SCHATTEN_LOCALLY_NORMAL_QUANTUM_2026-11-04.md` (P-55)
- `research/audits/P2_SOURCE_MPO_RESIDUAL_CYLINDER_DIRICHLET_2026-11-04.md` (P-78)