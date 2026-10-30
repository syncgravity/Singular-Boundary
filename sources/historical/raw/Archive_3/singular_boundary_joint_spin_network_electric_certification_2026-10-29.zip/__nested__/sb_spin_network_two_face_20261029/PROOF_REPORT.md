# The Singular Boundary — Exact two-face joint spin-network block and a posteriori eight-face cap certification

**Research date:** 2026-10-29. **Program:** R3 independent reconstruction.  **Status:** exact finite Gauss-invariant SU(2) electric theorem, exact full-time pure-electric cross response, a nonperturbative gauge-invariant multiface *energy upper bound*, and a finite-volume Ritz/min–max *certification method*. **The actual full-coupling eight-face Wilson spectrum was NOT diagonalized.** No connected Penrose flat-cap theorem, regulator-uniform mass gap, or continuum reconstruction is claimed.

## 1. Model and kinematic conditional color coordinates

Consider a finite simply connected planar edge-to-edge rhombus disk with free boundary links, no more than two faces per link, and all-vertex Gauss invariance. Use 2\(G=SU(2)\), normalized Haar, \(-\Delta\chi_j=j(j+1)\chi_j\), and

\[
H=T+V,\quad T=\sum_ea_e(-\Delta_e),\quad V=\sum_{q\in F}b_q(1-p_q),\quad p_q=\tfrac12\operatorname{Tr}W_q,\ a_e>0,\ b_q\ge0.
\]

Write \(A_q=\sum_{e\in\partial q}a_e\). The target magnetic term may be deleted by setting \(b_f=0\). A primal/dual spanning-tree transformation gives independent SU(2) Haar plaquette holonomies *kinematically*, while all-vertex gauge invariance is residual simultaneous conjugation of their based holonomies. This does **not** imply independence in the interacting ground state.

For adjacent faces \(f,g\) sharing exactly one edge \(e\), put \(U=W_f,V=W_g\) at a consistent common base point. With \(U=p_f I+i\mathbf u\cdot\sigma\), \(V=p_g I+i\mathbf v\cdot\sigma\), choose the orientation so
\[
D_{fg}:=p_{\partial(f\cup g)}-p_fp_g=-\mathbf u\cdot\mathbf v,
\qquad \Gamma_e(p_f,p_g)=\frac{a_e}{4}D_{fg}.
\]

Conditional on the two individual traces, the orientation axes are independent Haar spheres. Consequently
\[
\mathbb E_0[D_{fg}\mid p_f,p_g]=0,\quad
\mathbb E_0[D_{fg}^2\mid p_f,p_g]=\tfrac13(1-p_f^2)(1-p_g^2).
\]
Haar moments: \(\mathbb E_0p^2=1/4, \mathbb E_0p^4=1/8\). The kinematic expectation \(\mathbb E_0\) is **not** the nonlinear vacuum expectation.

## 2. SN-1: exact two-dimensional electric invariant sector

Define two *normalized, physical gauge-invariant, target-center-even* vectors
\[
F=2\chi_1(W_f)p_g=2(4p_f^2-1)p_g,\qquad
Z=4\sqrt2\,p_fD_{fg}.
\]
Both are orthogonal to the constant physical vacuum, and
\[
\langle F,F\rangle_0=\langle Z,Z\rangle_0=1,\qquad\langle F,Z\rangle_0=0.
\]
The state \(F\) belongs to the complete individual-plaquette-class subspace; \(Z\) is orthogonal to that entire subspace. They span the full invariant two-face representation sector with face labels \(j_f=1\), \(j_g=1/2\) (the diagonal-conjugation invariants have angular color channels 0 and 1). Electric link Casimirs preserve each face representation label. On the shared edge, the Clebsch–Gordan fusion \(1\otimes\tfrac12=\tfrac12\oplus\tfrac32\) provides precisely two electric eigenvalues.

The product rule \(-\Delta(FG)=(-\Delta F)G+F(-\Delta G)-2\nabla F\cdot\nabla G\) and the exact six-edge gradient identity give
\[
TF=\lambda F-\sqrt2a_eZ,\qquad \lambda=2A_f+\tfrac34A_g.
\]
Orthogonality, self-adjointness and the shared-edge Casimir values \(\tfrac34,\tfrac{15}4\) then fix the other diagonal entry. In the orthonormal basis \((F,Z)\), **the full physical electric operator** (not merely its compression) is exactly
\[
\boxed{T_{FZ}=\begin{pmatrix}
\lambda&-\sqrt2a_e\\
-\sqrt2a_e&\lambda-a_e
\end{pmatrix}.}\tag{SN1}
\]
Its eigenvalues are exactly
\[
\boxed{\lambda_-=\lambda-2a_e,\qquad\lambda_+=\lambda+a_e.}\tag{SN2}
\]
For \(A_f=A_g=4,a_e=1\), this is the matrix \(\begin{psmallmatrix}11&-\sqrt2\\-\sqrt2&10\end{psmallmatrix}\) with eigenvalues 9 and 12. This is valid as a subspace of the **entire finite graph's physical electric Hilbert space**: electric operators outside the two face supports vanish on these vectors. The full magnetic potential generally couples this sector to additional joint spin-network labels, so (SN1) is **not** an invariant 2×2 block of \(H\) when retained magnetic couplings are present.

## 3. SN-2: exact full-time electric relative-color transfer

Because (SN1) is a genuine invariant block of \(T\),
\[
\boxed{\langle Z,e^{-tT}F\rangle_0
=\frac{\sqrt2}{3}\left(e^{-(\lambda-2a_e)t}-e^{-(\lambda+a_e)t}\right)>0,\quad t>0.}\tag{SN3}
\]
Both eigenvalues are positive under the face-edge hypotheses. Hence
\[
\boxed{\langle Z,T^{-1}F\rangle_0
=\frac{\sqrt2a_e}{(\lambda-2a_e)(\lambda+a_e)}>0.}\tag{SN4}
\]
This is a *nonzero, exact full-time relative-color cross-response in the physical SU(2) electric theory*, and provides a direct regression target for joint spin-network codes. It is **not** the desired cap–magnetic-plaquette mixed response in the strongly coupled deleted ground state.

## 4. SN-3: simultaneous nonlinear Wilson trial state gives extensive ground-energy bound

Take the strictly positive physical gauge-invariant trial state
\[
\Psi_{\boldsymbol\kappa}(U)=Z^{-1/2}\exp\left(\sum_{q:b_q>0}\kappa_q p_q(U)\right),\qquad\kappa_q>0.
\]
Under kinematic product Haar, its squared probability factors as independently exponentially tilted *class* SU(2) face distributions. The radial mean is \(r_q=\langle p_q\rangle_{\kappa_q}\in(0,1)\). The local SU(2) identity
\[
\langle1-p_q^2\rangle_{\kappa_q}=\frac{3r_q}{2\kappa_q},
\qquad\langle1-p_q\rangle_{\kappa_q}\le\frac{3}{4\kappa_q}
\]
holds for every \(\kappa_q>0\). Every cross electric gradient term between distinct faces integrates to zero under this class-only weight by the conditional color-axis average. Thus the trial **kinetic energy is exactly**
\[
\langle\Psi_\kappa,T\Psi_\kappa\rangle=\sum_{q:b_q>0}\frac{A_q\kappa_q^2}{4}\langle1-p_q^2\rangle_{\kappa_q}
=\sum_q\frac{3A_q\kappa_q r_q}{8}.
\]
Adding the magnetic expectation and taking \(\kappa_q=\sqrt{2b_q/A_q}\), the finite-volume variational principle proves
\[
\boxed{0\le E_0(H)\le S_H:=\frac{3}{2\sqrt2}\sum_{q:b_q>0}\sqrt{A_qb_q}.}\tag{SN5}
\]
No reflection, disconnectedness, spectral gap, Gaussian approximation, or small coupling is assumed. For a fixed eight-face patch with seven retained coefficients \(b_q=O(h^{-2})\) and bounded \(A_q\), \(S_H=O(h^{-1})\). For a growing full physical Penrose disk, the sum is extensive; (SN5) **does not** supply a volume-uniform local bound by itself.

## 5. SN-4: uniform-in-state electric cutoff tail, without a physical gap

Let \(P_M=\mathbf1_{[0,M]}(T)\) be the finite-rank spectral projection of the *physical electric operator* and \(Q_M=1-P_M\). Since \(H=T+V\) and \(V\ge0\), for the actual normalized interacting ground state \(\Omega\),
\[
\boxed{\|Q_M\Omega\|^2\le \frac{E_0(H)}{M}\le\frac{S_H}{M}.}\tag{SN6}
\]
More generally, every normalized vector \(\xi\) in the actual spectral range \(\mathbf1_{(-\infty,E_0+\Lambda]}(H)\) obeys
\[
\boxed{\|Q_M\xi\|^2\le\frac{S_H+\Lambda}{M}.}\tag{SN7}
\]
The norm is the physical Hilbert norm, and (SN7) is **uniform over every vector in that low-excitation spectral subspace**, not just each eigenvector separately. It does not assume a regulator-uniform mass gap. On an eight-face patch, preserving the \(\Lambda_h=Lh^{-11/8}\) spectral window with fixed norm leakage requires \(M\gtrsim h^{-11/8}\), while source accuracy can require a much larger cutoff.

For any nonnegative central convolution cap multiplier \(0\le k_a\le\nu_a\mathbf1_{B_a}\), write \(\alpha_a=\int\phi_a\asymp a^3\), \(\nu_a=\int\phi_a^2\asymp a^3\). By expanding \(\Omega=P_M\Omega+Q_M\Omega\),
\[
\boxed{
\left|\langle\Omega,k_a\Omega\rangle-
\langle P_M\Omega,k_aP_M\Omega\rangle\right|
\le2\nu_a\sqrt{S_H/M}+\nu_aS_H/M.}\tag{SN8}
\]
To force this **simple universal error bound** below \(\alpha_a^2/4\), it is sufficient to take \(M\ge S_H(16\nu_a/\alpha_a^2)^2\) for sufficiently small caps. At \(a\asymp\sqrt h\), this is \(M=O(h^{-4})\) as a sufficient cutoff for a fixed eight-face patch. **This is a conservative method threshold, not a proven necessary cutoff**, and the projected *unknown* true ground state in SN8 is not automatically the Ritz ground state.

## 6. SN-5: rigorous finite-volume Ritz gap and cap certificate

Let \(B=\|V\|\le2\sum_qb_q\), \(P=P_M\), \(Q=1-P\). Form the *genuine physical joint-spin-network* finite matrix \(H_P=PHP\), with ordered lowest two Ritz eigenvalues \(e_0<e_1<M\) and normalized Ritz ground vector \(\varphi\in\mathrm{ran}\,P\). Denote
\[
\rho=\|QVP\|\le B,\qquad r=\|QVP\varphi\|\le\rho,
\qquad\theta=\frac{\rho^2}{M-e_1}.
\]
The full block operator has \(QHQ\ge M\) and off-diagonal coupling \(QHP=QVP\). Young's inequality gives, as quadratic forms,
\[
H\ \ge\ (H_P-\theta P)\ \oplus\ (M-\rho^2/\theta)Q,
\]
with the interpretation by continuity when \(\rho=0\). Hence min–max proves
\[
\boxed{E_1(H)\ge e_1-\theta,\quad E_0(H)\le e_0.}\tag{SN9}
\]
If the **computable finite-matrix condition** \(d:=e_1-e_0-\theta>0\) holds, the true physical ground gap is \(\ge d\). Its exact Ritz residual is \(\|(H-e_0)\varphi\|=r\). The spectral theorem and \(e_0<E_1(H)\) then give
\[
\boxed{\|(1-|\Omega\rangle\langle\Omega|)\varphi\|\le r/d.}\tag{SN10}
\]
For any bounded self-adjoint observable \(O\), a compatible phase choice yields
\[
\boxed{|\langle\Omega,O\Omega\rangle-\langle\varphi,O\varphi\rangle|
\le 2\sqrt2\,\|O\|\,r/d.}\tag{SN11}
\]
Therefore, a **genuine finite-volume SU(2) cap certificate** can be obtained by computing \(e_0,e_1,\rho,r\) and the Ritz cap value \(F_a^{(M)}=\langle\varphi,k_a\varphi\rangle\):
\[
\boxed{\mathbb P_{\Omega}(W_f\in B_a)\ge
\frac{[F_a^{(M)}-2\sqrt2\nu_a r/d]_+}{\nu_a}.}\tag{SN12}
\]
This requires actual joint spin-network matrices and a passing numerical certification condition; **none have yet been computed for the eight-face full Wilson patch**. The bounds are finite-regulator and *a posteriori*: they do not presume a uniform gap, but they may become too expensive to certify at the physical refinement scale. The finite-rank spectral cutoff includes all shared-edge and relative-color channels, unlike the invalid class-only truncation.

## 7. Executed verifications and precise next gate

1. 2`verify_spin_network_two_face.py`: deterministic SU(2) Haar integration on independent group face variables using 10-point Chebyshev-U radial quadrature and a 12-point icosahedral angular spherical 5-design, verifying \(F,Z\) orthonormality to machine precision, exact Clebsch–Gordan electric block, eigenvalues and full-time cross response for three coefficient triples. It also checks conservative cap truncation scales.
2. `verify_multiface_trial_and_tail.py`: direct SU(2) radial Haar quadrature for the tilted class moments, the exact kinetic/Bessel identity, seven-face variational energy upper bound, gap-free tail and an elementary finite-dimensional block energy enclosure.
3. `verify_ritz_certification.py`: positivity-preserving finite matrix comparisons validate the min–max gap bound, Ritz ground-state residual and cap observable error. **This test is not a numerical SU(2) eight-face diagonalization.**
4. The original full SU(2) color-leakage and eight-face Q8 gauge-fixing checks were re-executed unchanged.

**PROVED:** SN-1 through SN-5 as stated. **OPEN:** calculate and certify the nontrivial full-coupling eight-face SU(2) spin-network spectrum and actual center-even cap response; extend a valid bound over all connected asymmetric Penrose interiors; uniform bulk deletion, fixed-support connected covariance, nonzero continuum mass gap, nonlinear quartic resolvent and full reconstruction. No historical Stage26 data or dissertation files were modified.
