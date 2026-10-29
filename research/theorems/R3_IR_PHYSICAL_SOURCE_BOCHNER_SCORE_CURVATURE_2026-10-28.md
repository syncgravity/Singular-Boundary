# R3-IR — Gauge-invariant source Bochner identity and the nonlinear score-curvature gate

**October 28, 2026. Independent theorem at every finite regulator; conditional Penrose refinement.** This report follows the live independent-reconstruction branch's joint-force, weighted-score, mixed-Hessian/Gauss, and Gaussian benchmark audits. It does **not** prove a regulator-uniform mass gap, bounded nonlinear Wilson variance, source fourth moments, or continuum existence. The original Stage 7/26 implementation is not identified with the declared Hamiltonian. There is no Monte Carlo or modification of historical archives.

## 1. Setup

Let \(G_h\) be a finite edge-to-edge rhombus disk, each face having four edges, each edge incident to at most two faces. Work on the genuine SU(2) link Hilbert space and its vertex-Gauss invariant reducing subspace. Let

\[
H_h=\sum_ea_e(-\Delta_e)+\sum_fb_f(1-p_f),\quad
p_f=\tfrac12\operatorname{ReTr}(W_f),\quad0<a_e\le a_*,
\]

where \(-\Delta_e\) has spin-1/2 Casimir \(3/4\). Let \(\Omega_h>0\) denote its normalized physical ground state and \(\nu_h=\Omega_h^2dU\). Set \(w_h=\log\Omega_h\),
\[
\mathcal L_h=\sum_ea_e(\Delta_e+2\nabla_ew_h\cdot\nabla_e),\quad
\Gamma_h(f,g)=\sum_ea_e\langle\nabla_ef,\nabla_eg\rangle.
\]

For bounded signed face weights \(|q_f|\le q_*\) on a fixed physical region \(D\), write
\[
Y_h=h\sum_{f\in D}q_f(1-p_f),\quad Z_h=h\sum_{f\in D}(1-p_f),\quad A_h=(Y_h-\nu_hY_h)/\sqrt h.
\]

Assume the prior regional energy/Agmon bound \(\mathbb E_{\nu_h}Z_h\le C_Z\) and face count \(h^2|D|\le A_0\) on the declared Penrose sequence. **Exact identities below hold without those refinement bounds.**

## 2. Theorem BW-1: full mixed-link ground-state Bochner identity

The SU(2) metric with fundamental Casimir \(3/4\) is the round three-sphere of radius two. Its Ricci tensor is \(\mathrm{Ric}_e=\frac12g_e\). On the weighted product with the real reversible generator \(\mathcal L_h\), define
\[
\Gamma_{2,h}(Y)=\tfrac12\mathcal L_h\Gamma_h(Y)-\Gamma_h(Y,\mathcal L_hY).
\]

The product-manifold Bochner formula gives **pointwise**
\[
\boxed{\displaystyle
\Gamma_{2,h}(Y)=
\sum_{e,g}a_ea_g\|\operatorname{Hess}_{eg}Y\|_{\rm HS}^2
+\frac12\sum_ea_e^2|\nabla_eY|^2
-2\sum_{e,g}a_ea_g\operatorname{Hess}_{eg}w_h(\nabla_eY,\nabla_gY).}
\tag{BW-1}
\]

The full mixed link blocks \(e\ne g\) are essential. They are not diagonal-link substitutes. Haar integration, exact stationarity \(\nu_h\mathcal L_hf=0\), and \(\nu_h\Gamma_h(Y,\mathcal L_hY)=-\nu_h(\mathcal L_hY)^2\) give
\[
\boxed{\nu_h[(\mathcal L_hY)^2]=\nu_h\Gamma_{2,h}(Y).}\tag{BW-2}
\]

All terms are physical Gauss-invariant scalars, unlike the nonphysical fixed-link derivatives in the earlier QH-1 Ward identity. The equality is valid for any real smooth Gauss-invariant multiplier Y at any fixed nonlinear Wilson coupling. There is no gap assumption.

## 3. Theorem BW-2: a uniform bound for the entire geometric Bochner contribution

Define the nonnegative geometric expression
\[
\mathcal G_h(Y)=\sum_{e,g}a_ea_g\|\operatorname{Hess}_{eg}Y\|_{\rm HS}^2+\tfrac12\sum_ea_e^2|\nabla_eY|^2.
\]

The SU(2) one-link Hessian is \(\operatorname{Hess}_{ee}p_f=-p_f g_e/4\). For distinct incident links the individual matrix entries of \(\operatorname{Hess}_{eg}p_f\) have absolute value at most \(1/4\) in orthonormal left-trivialized frames, since the fundamental generators have operator norm \(1/2\). Thus **every** \(3\times3\) face Hessian block has HS squared norm \(\le9/16\). At each ordered link pair at most two faces contribute. Cauchy–Schwarz gives the uniform pointwise bound
\[
\sum_{e,g}a_ea_g\|\operatorname{Hess}_{eg}Y_h\|_{\rm HS}^2
\le2h^2q_*^2a_*^2\sum_{f\in D}\sum_{e,g\in\partial f}\frac9{16}
=18a_*^2q_*^2h^2|D|\le18a_*^2q_*^2A_0.
\tag{BW-3}
\]

The Ricci term obeys
\[
0\le\tfrac12\sum_ea_e^2|\nabla_eY_h|^2
\le\tfrac{a_*}{2}\Gamma_h(Y_h)
\le2a_*^2q_*^2hZ_h.
\tag{BW-4}
\]

Therefore
\[
\boxed{0\le\mathbb E_{\nu_h}\mathcal G_h(Y_h)
\le18a_*^2q_*^2A_0+2a_*^2q_*^2C_Zh.}\tag{BW-5}
\]

This is a **genuine uniform geometric control for every signed physical source** on the declared fixed-area Penrose sequence. It does not use Gaussianity or a vacuum Hessian sign.

## 4. Theorem BW-3: exact directional score-curvature reduction

Set
\[
\mathcal C_h(Y_h)=-2\mathbb E_{\nu_h}\sum_{e,g}a_ea_g\operatorname{Hess}_{eg}w_h(\nabla_eY_h,\nabla_gY_h).
\]

Since \(K_h(A_h\Omega_h)=-(\mathcal L_hY_h)\Omega_h/\sqrt h\), the physical source's second spectral moment satisfies
\[
\boxed{h\,m_{2,h}=\mathbb E_{\nu_h}\mathcal G_h(Y_h)+\mathcal C_h(Y_h).}\tag{BW-6}
\]

In particular, the *independent sufficient criterion*
\[
\sup_h\mathcal C_h(Y_h)<\infty
\tag{BW-7, OPEN}
\]

would imply \(m_{2,h}=O(h^{-1})\). Conversely, because the nonnegative geometric term is uniformly bounded, \(m_{2,h}=O(h^{-1})\) **implies** BW-7. Thus the two conditions are equivalent under the present hypotheses. Neither is established for the nonlinear Penrose ground state.

There is an unconditional **one-sided vacuum Hessian stability law**:
\[
\boxed{\mathcal C_h(Y_h)\ge-18a_*^2q_*^2A_0-2a_*^2q_*^2C_Zh.}\tag{BW-8}
\]

This follows solely from \(m_{2,h}\ge0\) and BW-5. It limits the integrated *positive* log-vacuum curvature in the Wilson direction, but gives no upper bound on the negative log-vacuum curvature needed for the source's spectral second moment. In particular a large positive magnetic Hessian or integrated Fisher information cannot substitute for BW-7.

The Ward result of the preceding turn also gives a different exact reduction
\(h m_{2,h}=\mathrm{Var}(F_h)-\mathrm{Var}(D_h)-2\mathbb E\Gamma(D_h,Y_h)\). Both identities hold simultaneously and demonstrate where the unknown score variation sits: in a variance on one side, and a directional log-vacuum Hessian on the other. The latter is **not independently bounded** by the former.

## 5. BW-4: exact SU(2) interacting one-face consistency check

Take a single open four-link face with equal electric coefficient a and magnetic b>0. The physical character Hamiltonian is \(H\chi_n=[a n(n+2)+b]\chi_n-(b/2)(\chi_{n-1}+\chi_{n+1})\). The real positive vacuum is \(\Omega(p)\) with SU(2) Haar density \(\rho_0(p)=2\sqrt{1-p^2}/\pi\). Put \(Y=h(1-p)\) and \(w(p)=\log\Omega(p)\).

The exact full four-link geometric Bochner term simplifies **pointwise** to
\[
\boxed{\mathcal G_h(Y)=a^2h^2(2+p^2).}\tag{BW-9}
\]

The full score-Hessian contraction, including the twelve off-diagonal ordered link blocks, simplifies to
\[
\boxed{\mathcal C_h(Y)=-2a^2h^2\mathbb E_{\nu}[(1-p^2)^2w''(p)-p(1-p^2)w'(p)].}\tag{BW-10}
\]

Meanwhile \(\mathcal LY=h[3ap-2a(1-p^2)w'(p)]\). This furnishes a direct independent check of BW-6 using the physical Sturm–Liouville eigenfunction, not a nonphysical link derivative. With \(a=1,b=5,h=0.1\), deterministic SU(2) character diagonalization and Gauss–Chebyshev quadrature give

- \(\mathbb E[(\mathcal LY)^2]=0.0325527660401600\);
- \(\mathbb E[\mathcal G(Y)]=0.0239239854269689\);
- \(\mathcal C(Y)=0.00862878061319113\);
- equality residual below \(10^{-15}\); physical \(m_2=0.3255276604016\).

Convergence holds with 24, 36 and 48 character basis modes; this is a deterministic finite-model check and not a proof from finite numerics, nor any Penrose continuum simulation. At b=0 the exact Haar values \(\mathbb E p^2=1/4\), \(\mathcal C=0\), \(\mathbb E\mathcal G=9a^2h^2/4=\mathbb E(\mathcal LY)^2\) provide an analytic check.

## 6. Critical path

**Proved:** exact full product-link ground-state Bochner identity (BW-1/2), uniform \(O(1)\) bound for its *entire classical geometric part* (BW-3–5), one-sided integrated log-vacuum curvature law (BW-8), and exact nonlinear physical second-moment decomposition (BW-6).

**Open:** the opposite, upper bound BW-7 for the actual directional score-curvature contraction; bounded/nonzero source variance; physical regulator-uniform mass gap; quartic response; full quantum continuum; original Stage7/26 Hamiltonian provenance. BW-7 is an equivalent reformulation of the improved \(m_2=O(h^{-1})\) target and must not be advertised as an independent coercivity theorem until derived from further dynamics. The Gaussian tangent provides a benchmark but cannot be imported.

**Next noncircular route:** isolate the conditional vacuum Hessian in the gauge-invariant Wilson direction via a *new* local spectral/relative-energy estimate, or establish a model-specific comparison for the vacuum score under constrained curvature, without assuming a gap or merely renaming BW-7. Existing Agmon estimates give moments of total deficit and weighted Fisher norm but not the signed Hessian upper bound.

**Integrity:** all statements concern the declared finite SU(2) Wilson model and its explicit scaling assumptions. Authentic three-rhombus Z5 fixture serves only as geometry, not as temporal Q14. No Monte Carlo or original source modification.