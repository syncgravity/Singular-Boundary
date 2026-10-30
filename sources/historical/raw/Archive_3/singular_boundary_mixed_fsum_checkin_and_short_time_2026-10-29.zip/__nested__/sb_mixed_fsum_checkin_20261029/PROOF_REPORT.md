# The Singular Boundary — Exact SU(2) mixed Wilson spectral moment, six-edge skein, and center-even inverse-response obstruction

**Research date:** 2026-10-29. **R3 independent reconstruction.** **Status:** a new exact **finite, fully nonlinear physical SU(2) Wilson Hamiltonian** mixed spectral sum rule on arbitrary edge-to-edge planar disks; a new *nonphysical but exact* positivity-improving, target-center-even Markov countermodel showing why that sum rule alone cannot prove the low-energy cap bound. The generic connected Penrose flat-cap estimate and continuum Yang–Mills mass gap remain **OPEN**.

## 1. Hamiltonian and signed cross-spectral measure

Let the finite physical SU(2) magnetic-deleted Hamiltonian be

\[
H_f^-(u)=\sum_e a_e(-\Delta_e)+\sum_{q\ne f} b_q(u)(1-p_q),\qquad p_q=\tfrac12\operatorname{ReTr}W_q,\quad a_e>0,\quad b_q(u)\ge0.
\]

All primal links carry normalized Haar measure and all vertex Gauss constraints are imposed. At each finite coupling u, the full-space positive Perron–Frobenius ground state \(\Omega_u>0\) is automatically physical. Write \(E_u\), \(K_u=H_f^-(u)-E_u\ge0\), \(Q_u=1-|\Omega_u\rangle\langle\Omega_u|\) and reduced resolvent \(G_u=Q_uK_u^{-1}Q_u\). The spectrum is discrete at finite volume; no uniform gap is assumed.

For any two real smooth gauge-invariant link multipliers \(O\) and \(W\), let \(v_O=Q_uO\Omega_u\), \(v_W=Q_uW\Omega_u\) and define the signed (real) mixed spectral measure

\[
\sigma_{O,W}(J)=\operatorname{Re}\langle v_O,P_J(K_u)v_W\rangle,\qquad J\subset(0,\infty).
\]

Its first and inverse moments, and imaginary-time connected response, are

\[
M_1(O,W)=\int\lambda\,d\sigma=\operatorname{Re}\langle v_O,K_uv_W\rangle,\quad
M_{-1}(O,W)=\int\lambda^{-1}d\sigma=\operatorname{Re}\langle v_O,G_uv_W\rangle,\quad
C_{O,W}(t)=\int e^{-t\lambda}\,d\sigma.
\]

At each fixed finite volume \(M_{-1}=\int_0^\infty C_{O,W}(t)dt\) and \(C'_{O,W}(0)=-M_1\). This formalism applies in the **actual cycle-rich asymmetric** SU(2) Wilson system, even though the signed spectral measure is not necessarily positive.

## 2. Theorem MS-1: exact mixed ground-state Dirichlet and local six-edge Wilson skein

The exact ground-state transform on a finite compact-link product yields, for all smooth real gauge-invariant multipliers,

\[
\boxed{M_1(O,W)=\mathbb E_{\Omega_u^2}\left[\sum_e a_e\,\nabla_e O\cdot\nabla_e W\right].}\tag{MS1}
\]

**Proof:** \(K_u\Omega_u=0\), the electric form is \(\sum_e a_e\int|\nabla_e\Psi|^2\), and polarizing the identity \(\langle O\Omega_u,K_uW\Omega_u\rangle=\int\Omega_u^2\Gamma(O,W)\) proves MS1. The retained noncommuting Wilson magnetic interactions enter through the **true** \(\Omega_u\) but do not appear in the local carré-du-champ factor.

Take two distinct plaquettes f and g that share exactly one primal edge e, traversed in opposite directions by their oriented boundary loops. By cyclicity of SU(2) trace, choose the shared variable \(U=U_e\) and fixed other-link products \(X,Y\) such that

\[
p_f=p(UX),\quad p_g=p(U^{-1}Y),\quad p_{\partial(f\cup g)}=p(XY),\quad p(V)=\tfrac12\operatorname{Tr}V.
\]

Here \(\partial(f\cup g)\) is the physical **six-edge exterior boundary** of the two-face union. Fix left-invariant SU(2) tangent generators \(\tau_k=i\sigma_k/2\), normalized so \(-2\operatorname{Tr}\tau_k\tau_\ell=\delta_{k\ell}\). The exact fundamental SU(2) Fierz identity reads

\[
\boxed{\sum_{k=1}^3(L_kp_f)(L_kp_g)=\frac14\bigl[p_{\partial(f\cup g)}-p_fp_g\bigr].}\tag{MS2}
\]

This follows directly by differentiating p(UX) and p(U^{-1}Y), then applying \(\sum_k\operatorname{Tr}(\tau_kA)\operatorname{Tr}(\tau_kB)=p(A)p(B)-p(AB)\) with the appropriate trace normalization. No small-angle expansion or Gaussianization occurs.

For any smooth target class function \(O=\kappa(p_f)\) and the neighboring magnetic multiplier \(W=b_g(1-p_g)\), MS1–MS2 give the **exact physical mixed first spectral moment**

\[
\boxed{M_1\bigl(\kappa(p_f),b_g(1-p_g)\bigr)
=-\frac{a_eb_g}{4}\,\mathbb E_{\Omega_u^2}\left[\kappa'(p_f)\bigl(p_{\partial(f\cup g)}-p_fp_g\bigr)\right].}\tag{MS3}
\]

If the link supports of f and g are disjoint, the exact first cross moment is zero. **Zero mixed first moment does not mean zero covariance, zero spectral cyclic overlap, or zero inverse-energy response.** The distinction is fundamental for the connected-bulk cap obligation.

## 3. Theorem MS-2: local center-even cap moment bound and sign freedom

Write SU(2) matrices in normalized quaternion form \(A=p(A)I+i\mathbf a\cdot\boldsymbol\sigma\), \(B=p(B)I+i\mathbf b\cdot\boldsymbol\sigma\). Since \(p(AB)=p(A)p(B)-\mathbf a\cdot\mathbf b\), we have the **sharp pointwise bound**

\[
\boxed{|p_{\partial(f\cup g)}-p_fp_g|\le\sqrt{1-p_f^2}\sqrt{1-p_g^2}.}\tag{MS4}
\]

Both signs are possible for noncommuting Wilson data; neither center parity nor positivity of the ground state fixes MS3's sign.

For the previously proved positive convolution source \(k_a(W_f)=\kappa_a(p_f)\), supported on a geodesic target cap \(B_a(I)\), with the exact group convolution gradient bound \(\|\nabla k_a\|_\infty\le C_\phi a^2\), one has

\[
\boxed{|M_1(k_a,b_gd_g)|\le C_\phi a_e b_g a^2
\mathbb E_{\Omega_u^2}\left[\mathbf 1_{B_a(I)}(W_f)\sqrt{1-p_g^2}\right].}\tag{MS5}
\]

For the target-center-even projection \(k_a^+(U)=\tfrac12[k_a(U)+k_a(-U)]\), replace the support indicator by the two-center set \(B_a(I)\cup B_a(-I)\), changing only the fixed constant. **The bound is local, gauge invariant and exact at full coupling**, but it does not bound \(M_{-1}\) or force the polynomial cap probability.

## 4. Theorem MS-3: exact center-even positivity-improving countermodel to first-moment closure

Consider the six-state path graph \(0\!−\!1\!−\!2\!−\!3\!−\!4\!−\!5\) with nearest-neighbor conductances \(c_0=c_1=c_3=c_4=1\) and \(c_2=\varepsilon>0\). Let \(L_\varepsilon\) be its symmetric graph Laplacian, \(\omega=\mathbf1/\sqrt6\), \(Q=I-|\omega\rangle\langle\omega|\). Let \(O\) be multiplication by \(\mathbf1_{\{0\}}\), and \(W\) multiplication by \(\mathbf1_{\{2\}}\). Both are bounded, nonnegative, and have **disjoint gradient-edge supports**: O changes only across 0–1, whereas W changes across 1–2 and 2–3. Thus, exactly,

\[
\boxed{M_1(O,W)=\langle QO\omega,L_\varepsilon QW\omega\rangle=0.}\tag{MS6}
\]

The finite matrix pseudoinverse can be inverted **symbolically**:

\[
\boxed{M_{-1}(O,W)=\langle QO\omega,(L_\varepsilon|_{\omega^\perp})^{-1}QW\omega\rangle
=\frac1{24\varepsilon}-\frac1{27}.}\tag{MS7}
\]

As \(\varepsilon\downarrow0\), the inverse-energy mixed response diverges **positively**, although the source and driver have bounded norms and the first mixed spectral moment vanishes identically. Their individual first moments stay bounded: \(m_1(O)=1/6\), \(m_1(W)=(1+\varepsilon)/6\).

To enforce an exact **target-center involution**, tensor this six-site reversible diffusion with a two-site flip diffusion: \(K_{12}=L_\varepsilon\otimes I_2+\frac15 I_6\otimes(I_2-\sigma_x)\). Its 12-state ground state is unique, strictly positive and invariant under \(C=I_6\otimes\sigma_x\). Both multipliers are tensored with \(I_2\) and hence strictly **center even**. All of MS6–MS7 remain true and the semigroup is positivity improving for \(\varepsilon>0\). This countermodel therefore satisfies: center parity, nonnegative local graph electric form, nonnegative bounded multipliers, bounded individual \(f\)-sums, and zero mixed \(f\)-sum, while having arbitrarily large **center-even** inverse-energy cross response.

Moreover, at the tested positive conductances, the center-even driver \(QW\omega\) has nonzero overlap with **every center-even excited eigenmode**. Its spectral cyclic projector therefore satisfies \(\|\Pi_WQO\omega\|=\|QO\omega\|\): the source's entire center-even spectral subspace is available to the driver despite \(M_1(O,W)=0\). This directly distinguishes local cross-gradient cancellation from actual portal orthogonality.

**Essential model boundary:** the 12-state graph diffusion is **not** an SU(2) gauge theory, does not use Wilson plaquette potentials, and is **not** a counterexample to the existence of the desired SU(2) bulk cap bound. It is a rigorous no-go for any attempted argument based *only* on these generic positivity, center parity and first-moment properties. Any successful connected Wilson proof must use additional dynamics, geometric connectivity and/or time-correlation cancellation.

## 5. Exact short-time versus full-time distinction

In the physical SU(2) theory, define \(C_{a,g}(t)=\langle Qk_a^+\Omega,e^{-tK}Q(b_gd_g)\Omega\rangle\). Then the two exact identities are

\[
\boxed{C'_{a,g}(0)=-M_1(k_a^+,b_gd_g),\qquad
\int_0^\infty C_{a,g}(t)dt=M_{-1}(k_a^+,b_gd_g).}\tag{MS8}
\]

MS3–MS5 control the first, local quantity. The revised connected Penrose obligation is to control the **second, time-integrated signed quantity** uniformly (or an equivalent physical spectral cyclic overlap). The earlier independent-Haar-portal theorem made \(C(t)\equiv0\) *for every t* by a genuine tensor projection. A zero first derivative \(C'(0)=0\) is far weaker; MS6–MS7 show no general implication between the two even for a positive center-even semigroup.

## 6. Independent deterministic verification and obligations

The accompanying Python script verifies the SU(2) Fierz formula with 128 deterministic noncommuting group configurations at maximum error below \(6\times10^{-17}\), both allowed local signs, the quaternion bound MS4, exact symbolic six-site inverse resolvent MS7, and the center-even 12-state finite diffusion at \(\varepsilon=1/4,1/16,1/64,1/256\), with correct source/driver \(f\)-sums. No Monte Carlo, no Stage26 manipulation, no physical eight/nine-face SU(2) ground-state diagonalization.

**PROVED:** MS-1–MS-3 and MS8 in their precise domains. **OPEN:** a Wilson-specific long-time signed response bound (or independent direct deleted-cap probability estimate) for the genuinely fully connected reflection-free Penrose interior; all-bulk magnetic deletion, fixed-support nonlinear covariance, uniform physical mass gap, quartic resolvent and continuum construction. **Do not upgrade the local mixed first-moment identity into spectral orthogonality.**
