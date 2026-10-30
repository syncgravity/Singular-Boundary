# R3: exact compact-SU(2) link Ward identity and the 54-face local-energy obstruction

**Date:** 2026-10-28. **Status:** new exact local identities and a rigorous reduction; **the requested uniform 54-face Wilson-energy estimate is not proved**. This note does not assert an arbitrary nonstationary three-slab R3 theorem.

## 1. Scope and provenance

Let \(\Lambda\) be a finite rhombus-prism lattice gauge complex with compact SU(2) link variables, normalized Haar measure, and retained-face Wilson action
\[
S_R(U)=\sum_{p\in R}d(W_p(U)),\qquad d(g)=1-\tfrac12\operatorname{ReTr}g\in[0,2],\qquad d\mu_\lambda(U)=Z_R^{-1}e^{-\lambda S_R(U)}dU.
\]
The previously supplied project geometry reports \(|Q|=14\), \(|H|=36\), \(|A(H)|=62\), and \(|A_{\rm fill}|=54\), with an exact Bianchi estimate \(S_Q\le44S_{A_{\rm fill}}\). The exact incidence list is not included in this note, so the specialized 36-link covering conclusion is conditional on the reported inclusion \(A_{\rm fill}\subseteq A(H)\). The generic theorem below holds for any explicit edge cover and does not require that inclusion.

## 2. Exact one-link conditional law

Fix an oriented link \(e\), and condition on all other links. Assume each incident face contains \(e\) exactly once (as for ordinary nondegenerate prism plaquettes). By cyclicity of SU(2) trace and inversion invariance, write the incident face energies as
\[
S_e(u;\omega)=\sum_{i=1}^{n_e}(1-u\cdot a_i)=n_e-u\cdot M,
\quad a_i\in S^3\subset\mathbb R^4,\quad M=\sum_{i=1}^{n_e}a_i,\quad R=|M|\le n_e.
\]
Here \(u\in S^3\) is the unit-quaternion representation of the variable link; possible orientations have been absorbed into the staples \(a_i\). The exact conditional measure is
\[
d\mu_e(u\mid\omega)=\frac{e^{\lambda u\cdot M}}{F(\lambda R)}du,\quad F(t)=\int_{S^3}e^{t u_0}du=\frac{2I_1(t)}t,\quad F(0)=1.
\]
Set \(L(t)=I_2(t)/I_1(t)\), with \(L(0)=0\). Then
\[
\mathbb E[u\cdot M\mid\omega]=R L(\lambda R),\qquad
\mathbb E[S_e\mid\omega]=n_e-R+R[1-L(\lambda R)]. \tag{2.1}
\]
The local minimization residual \(m_e(\omega)=\min_u S_e(u;\omega)=n_e-R\) is the **staple-frustration energy**. It is gauge invariant under endpoint rotations.

## 3. Sharp uniform thermal-excess bound

The distribution of \(y=1-u_0\in[0,2]\) under the tilted Haar law has density proportional to \(y^{1/2}(2-y)^{1/2}e^{-ty}\). Integrating \(\frac{d}{dy}[y^{3/2}(2-y)^{1/2}e^{-ty}]\) over \([0,2]\) yields
\[
t\mathbb E_t y=\frac32-\frac12\mathbb E_t\frac{y}{2-y}\le\frac32.
\]
Consequently, for every \(\lambda>0\), every ambient lattice, every external configuration, and every link \(e\),
\[
\boxed{0\le\lambda\{\mathbb E[S_e\mid\omega]-m_e(\omega)\}\le\frac32.}\tag{3.1}
\]
The constant \(3/2\) is asymptotically sharp as \(\lambda R\to\infty\) for \(R>0\). If \(R=0\), the excess vanishes exactly.

This is stronger than the earlier logarithmic bound for thermal excess, but it concerns a **single-link star conditional on all other links**, not the complete 54-face energy.

## 4. Exact local Ward identity

On SU(2) viewed as the unit round 3-sphere, with Laplace–Beltrami operator \(\Delta_{S^3}\) (negative spectrum), the link-star action satisfies
\[
\Delta_e S_e=3(u\cdot M)=3(n_e-S_e),\qquad
|\nabla_e S_e|^2=R^2-(u\cdot M)^2.
\]
Integration by parts against the conditional Wilson measure gives
\[
\boxed{\lambda\mathbb E\bigl[|\nabla_e S_R|^2\bigr]
=3\mathbb E[n_e-S_e].}\tag{4.1}
\]
The gradient with respect to \(e\) of the total action equals the gradient of \(S_e\). Equation (4.1) is an exact gauge-covariant Ward identity and remains valid after averaging over the actual exterior Gibbs measure. Its right-hand side is not a positive multiple of \(\mathbb E S_e\), so (4.1) alone cannot establish the desired \(O(1/\lambda)\) face-energy bound.

## 5. Pairwise-staple curvature identity

For unit-quaternion staples,
\[
\boxed{m_e=n_e-R
=\frac{\sum_{i<j}|a_i-a_j|^2}{n_e+R}
=\frac{2\sum_{i<j}d(a_i a_j^{-1})}{n_e+R}.}\tag{5.1}
\]
The products \(a_i a_j^{-1}\) are based closed-loop holonomies after endpoint transport. The local obstruction is thus a weighted sum of **two-staple loop energies**, not a generic operator commutator.

If \(n_e=1\), then \(m_e=0\) and \(\lambda\mathbb E d(W_p)\le3/2\) for the sole incident face. For higher incidence, the pairwise loops need additional Gibbs control.

## 6. A rigorous fractional-cover reduction

Let \(F\subseteq R\) be a fixed set of retained faces. Let \(C\) be a finite set of links meeting each face of \(F\), and choose nonnegative weights \(w_e\) satisfying
\[
\sum_{e\in\partial p\cap C}w_e\ge1\quad(p\in F).
\]
Since all Wilson face energies are nonnegative,
\[
S_F\le\sum_{e\in C}w_e S_e.
\]
Condition on all links except \(e\), use (3.1), and average over the **full** Gibbs measure:
\[
\boxed{
\lambda\mathbb E_{\Lambda,\lambda}S_F
\le\frac32\sum_{e\in C}w_e
+\lambda\sum_{e\in C}w_e\mathbb E_{\Lambda,\lambda}m_e.
}\tag{6.1}
\]
This is volume-uniform in its explicit constant, for every nonstationary retained-face mask. No global Morse–Bott argument is used.

**Penrose specialization.** If the reported \(A_{\rm fill}\subseteq A(H)\) incidence is correct, take \(F=A_{\rm fill}\), \(C=H\), \(w_e=1\). Then
\[
\boxed{
\lambda\mathbb E S_{A_{\rm fill}}
\le54+\lambda\sum_{e\in H}\mathbb E m_e.
}\tag{6.2}
\]
The number 54 on the right is \((3/2)|H|=(3/2)36\); it is **not** the count of fill faces entering a new independent estimate. The bound remains valid for a smaller optimized fractional cover if an exact incidence matrix is provided. Without the inclusion, choosing all edges in the boundaries of the 54 faces gives a finite local constant at most \((3/2)(4\cdot54)=324\), provided all faces are quadrilaterals.

## 7. Consequence for the exterior barrier

Assuming the earlier rigorously derived compact-Haar conditional excess bound
\[
-\log\mathbb E_{\nu_{0,\Lambda}}e^{-\lambda\Delta}
\le54\log(1+\lambda)+C_{H,\nu}+44\lambda\mathbb E S_{A_{\rm fill}},
\]
(6.2) yields
\[
\boxed{
-\log\mathbb E_{\nu_{0,\Lambda}}e^{-\lambda\Delta}
\le54\log(1+\lambda)+C_{H,\nu}+2376
+44\lambda\sum_{e\in H}\mathbb E m_e.
}\tag{7.1}
\]
Thus it suffices to prove
\[
\boxed{\sup_\Lambda\lambda\sum_{e\in H}\mathbb E_{\Lambda,\lambda}(n_e-|\sum_{p\ni e}a_{p,e}|)=O(\log(1+\lambda)).}\tag{7.2}
\]
This is a **new sufficient local loop-frustration estimate**, but (7.2) remains open. It is not a proof of the 54-face energy estimate.

## 8. Why a pointwise conditional Ward argument cannot finish

Take a link with exactly two incident faces and fixed staples \(a_1=(1,0,0,0)\), \(a_2=(-1,0,0,0)\). Then \(M=0\), \(R=0\), and
\[
S_e(u)=2\quad\text{for all }u\in SU(2).
\]
The conditional link measure is Haar at every \(\lambda\), and each face has conditional expected energy 1. Thus \(\lambda\mathbb E[d(W_p)\mid\omega]=\lambda\), unbounded. Equation (4.1) holds (both sides zero). The **full exterior Gibbs marginal** may suppress such opposing staples, but that suppression is exactly what requires proof. This example is not a counterexample to the full finite-volume pure Wilson gauge measure; it rules out a *uniform pointwise-in-exterior* Ward closure.

## 9. Local coupling interpolation: an exact identity, not an estimate

Give only \(F=A_{\rm fill}\) a coupling multiplier \(s\in[0,1]\):
\[
Z(s)=\int\exp[-\lambda(S_{R\setminus F}+sS_F)]dU.
\]
Then
\[
-\frac{d}{ds}\log Z(s)=\lambda\mathbb E_s S_F,
\quad\frac{d^2}{ds^2}\log Z(s)=\lambda^2\operatorname{Var}_s(S_F)\ge0.
\]
It follows that
\[
\lambda\mathbb E_1 S_F\le\log\frac{Z(0)}{Z(1)}.
\]
A polynomial bound on this **54-face deletion ratio** would establish the target, but proving that ratio is another local insertion comparison; the interpolation alone does not provide it.

## 10. Evidence and status

The accompanying `verify_heatbath.py` checks the exact Bessel-function mean against independent one-dimensional Haar quadrature at several couplings, tests the pairwise-staple identity for random quaternion staples, and records the opposing-staple obstruction. Numerical checks are not substitutes for the analytic proofs above. The previously supplied Phase III Penrose Wilson data use other observables and couplings; they do not certify a 54-face, uniform-in-volume weak-coupling energy bound.

**Proved:** exact one-link SU(2) conditional law, sharp \(3/2\) thermal-excess inequality, gauge-covariant Ward identity, pairwise-staple frustration identity, fractional-cover estimate (6.1), and conditional Penrose specialization (6.2).

**Not proved:** volume-uniform \(O(\log(1+\lambda))\) control of the 36-link staple frustration, 54-face Wilson energy, arbitrary nonstationary three-slab barrier, or continuum mass gap.

**Next precise task:** audit the 54-by-36 fill-face/link incidence matrix and solve the finite fractional-cover LP; then establish a Gibbs suppression inequality for the 36 local pair-staple loop energies. The latter, not the one-link Ward identity, is the missing analytic theorem.
