# The Singular Boundary — Full-time Wilson neighbor susceptibility and a physical autocorrelation no-go

**Research date:** 2026-10-29. **Program:** R3 independent reconstruction. **Status:** proved, finite nonlinear Gauss-invariant SU(2) Wilson theorems; an exact private-edge Wilson counterexample to a *proof strategy*, **not** to the desired Penrose flat-cap estimate. The fully connected, reflection-free Penrose deleted-face response, continuum mass gap and reconstruction remain **OPEN**.

## 1. Setup and what is being estimated

Let \(G\) be a finite simply connected edge-to-edge rhombus disk, with at most two faces per primal edge, electric coefficients \(a_e>0\) and retained magnetic coefficients \(b_q\ge0\). Choose edge-sharing faces \(f,g\), and permanently delete the magnetic term of \(f\). Let \(p_q=\frac12\mathrm{ReTr}(W_q)\), \(d_q=1-p_q\), and \(A_q=\sum_{e\in\partial q}a_e\). Interpolate one neighbor:

\[
H(u)=T+\sum_{q\notin\{f,g\}}b_qd_q+u b_gd_g,\quad W=b_gd_g,\quad 0\le u\le1.
\]

Write \(E(u)\), \(\Omega_u>0\), \(K_u=H(u)-E(u)\), \(Q_u=1-|\Omega_u\rangle\langle\Omega_u|\), and \(G_u=Q_uK_u^{-1}Q_u\) on the finite-volume physical Gauss-invariant Hilbert space. Uniqueness, positivity, analyticity and a finite positive excitation gap hold at each fixed finite volume; **no regulator-uniform physical gap is assumed**.

For any bounded real multiplier \(A\) let \(\chi_{AA}(u)=\langle Q_u A\Omega_u,G_u Q_u A\Omega_u\rangle\). This is the integrated imaginary-time autocovariance, **not** the mixed cap response \(\langle Qk_a\Omega_u,G_uQW\Omega_u\rangle\).

## 2. Theorem FT-1 — Exact integrated full-time neighboring-plaquette susceptibility

**Statement.** For every finite nonlinear Wilson system above,

\[
\boxed{\quad\int_0^1 \chi_{WW}(u)\,du
  =\frac{b_g}{2}\langle p_g\rangle_{u=1}.\quad}\tag{FT1}
\]

Moreover, using the previously established exact private-edge variational comparison,

\[
\boxed{\quad \max\!\left(0,\frac{b_g}{2}-\frac{3}{4\sqrt2}\sqrt{A_gb_g}\right)
\le \int_0^1\chi_{WW}(u)\,du\le\frac{b_g}{2}.\quad}\tag{FT2}
\]

**Proof.** When \(u=0\), the edge shared by \(f,g\) lies on no magnetic plaquette. The ground state is independent of that link, hence \(W_g\) is Haar and \(\langle p_g\rangle_0=0\). The exact Hellmann–Feynman and Kato identities are

\[
 E'(u)=\langle W\rangle_u=b_g[1-\langle p_g\rangle_u],\qquad
 E''(u)=-2\chi_{WW}(u)\le0.
\]

Integrating the second identity gives \(2\int_0^1\chi_{WW}=E'(0)-E'(1)=b_g\langle p_g\rangle_1\), proving FT1. Since \(0\le d_g\le2\) and \(\chi_{WW}\ge0\), \(0\le\langle p_g\rangle_1\le1\). The energy \(E\) is concave, so \(E'(1)\le E(1)-E(0)\). At the double-deleted endpoint the shared edge is magnetically private to \(g\), and the positive gauge-invariant one-face variational trial proves

\[
 0\le E(1)-E(0)\le\frac{3}{2\sqrt2}\sqrt{A_gb_g}.
\]

Thus \(0\le E'(1)\le\frac3{2\sqrt2}\sqrt{A_gb_g}\), which substituted into FT1 yields FT2. The proof is **full-coupling**, **volume-independent**, **gap-independent**, and retains all other cycle-rich Wilson magnetic interactions. If \(A_g\le A_+\) and \(b_g\asymp h^{-2}\), then

\[
\boxed{\ \int_0^1du\int_0^\infty dt\, \langle Q_uW\Omega_u,e^{-tK_u}Q_uW\Omega_u\rangle
=\frac{b_g}{2}+O(\sqrt{A_gb_g})
=\frac{b_g}{2}+O(h^{-1}).\ }
\]

This *forces* a large integrated **driver self-susceptibility**. It says **nothing about the sign or magnitude of the corresponding mixed cap–driver response**.

## 3. Theorem FT-2 — A gap-free but too-strong Cauchy cap criterion

Choose the previously established smooth positive central cap convolution \(k_a=\phi_a*\phi_a^\vee\), where \(\phi_a=\zeta_a^2\), \(\zeta_a\equiv1\) on \(B_{a/4}\), \(\mathrm{supp}\,\zeta_a\subseteq B_{a/2}\), and \(|\nabla\zeta_a|\le C/a\). Let \(\alpha_a=\int\phi_a\asymp a^3\), \(\nu_a=\int\phi_a^2\asymp a^3\), and set \(k_a^+(U)=\frac12[k_a(U)+k_a(-U)]\). Target-center symmetry implies the exact equality \(F_a(u)=\langle k_a(W_f)\rangle_u=\langle k_a^+(W_f)\rangle_u>0\). We have \(F_a(0)=\alpha_a^2\).

Define the positive self-susceptibilities

\[
 S_a(u)=\langle Q_uk_a^+\Omega_u,G_uQ_uk_a^+\Omega_u\rangle,
 \qquad S_W(u)=\chi_{WW}(u).
\]

The exact derivative of \(y_a(u)=\sqrt{F_a(u)}\) is

\[
 y_a'(u)=-\frac{\operatorname{Re}\langle Q_uk_a^+\Omega_u,G_uQ_uW\Omega_u\rangle}{\sqrt{F_a(u)}}.
\]

The reduced resolvent is positive, so its Cauchy inequality and FT1 imply

\[
\boxed{\quad\sqrt{F_a(1)}\ge\alpha_a
-\sqrt{\tfrac{b_g}{2}\langle p_g\rangle_1}\left[\int_0^1\frac{S_a(u)}{F_a(u)}du\right]^{1/2}.\quad}\tag{FT3}
\]

A *sufficient* condition for retaining \(\sqrt{F_a(1)}\ge3\alpha_a/4\) is

\[
\boxed{\quad\int_0^1\frac{S_a(u)}{F_a(u)}du\le\frac{\alpha_a^2}{8b_g}.\quad}\tag{FT4}
\]

This is valid and makes no uniform-gap assumption, but it is **not a necessary condition for cap survival**. In fact FT-3 below proves FT4 can fail by a diverging factor **inside the true Wilson model even when the target cap probability is exactly Haar at all couplings**.

## 4. Theorem FT-3 — Actual SU(2) Wilson no-go for replacing signed response by source-only inverse susceptibility

Consider a **connected two-rhombus disk** with edge-sharing faces \(f,g\). Delete \(f\)'s magnetic term and restore \(g\)'s term at any positive \(b_g\). The target \(f\) has three private boundary links; choose one. For **every** \(u\in[0,1]\) the Hamiltonian factorizes over this free electric link, its positive vacuum is link-Haar, and the group holonomy \(W_f\) has the exact Haar law. Therefore

\[
F_a(u)=\alpha_a^2\quad\text{for every }u;\qquad
\langle Q_uk_a^+\Omega_u,G_uP_JQ_uW\Omega_u\rangle=0
\quad\text{for every spectral window }J.
\]

The second equality follows because \(W\) is independent of the private link, the free-link ground-sector projection is preserved by both the resolvent and its spectral projections, and averaging \(k_a^+(W_f)\) over that link gives the constant \(\alpha_a^2\). **This is exact frequency-by-frequency spectral orthogonality**, not a cancellation of divergent positive and negative terms.

Nevertheless, let \(V_a=\mathrm{Var}_{\Omega_u^2}[k_a^+(W_f)]\). Exact target Haar measure, the cap support, and convolution positivity give, for all sufficiently small \(a\),

\[
 \boxed{V_a\ge c_1a^9.}\tag{FT5}
\]

**Detail:** if \(U\in B_{a/8}\), then for \(V\in B_{a/8}\) both \(V\) and \(V^{-1}U\) lie in \(B_{a/4}\), where \(\phi_a=1\). Hence \(k_a(U)\ge\mathrm{Haar}(B_{a/8})\ge c a^3\). On \(B_{a/8}\), \(k_a^+(U)\ge k_a(U)/2\), giving \(\int(k_a^+)^2\,dU\ge ca^9\), whereas its squared Haar mean equals \(\alpha_a^4=O(a^{12})\).

The proved self-weighted carré-du-champ estimate and exact Haar expectation give

\[
 m_{1,u}(k_a^+)\le\frac12C_kA_f a F_a(u)
 =\frac12C_kA_fa\alpha_a^2\le C_2 A_f a^7.\tag{FT6}
\]

The spectral Cauchy/Markov inequality \(\langle v,K^{-1}v\rangle\langle v,Kv\rangle\ge\|v\|^4\) (with \(v=Qk_a^+\Omega_u\)) proves

\[
\boxed{\quad S_a(u)\ge \frac{V_a^2}{m_{1,u}(k_a^+)}
\ge\frac{c_3}{A_f}a^{11},\qquad
\int_0^1\frac{S_a(u)}{F_a(u)}du\ge\frac{c_4}{A_f}a^5.\quad}\tag{FT7}
\]

All constants depend only on the fixed scaled bump and SU(2) Haar metric. These inequalities hold **for every coupling \(u\)** and require no positive spatial reflection or spectrum gap. At the regulator scale \(a_h\asymp\sqrt h\), \(b_g\asymp h^{-2}\), and bounded \(A_f\), the ratio between the FT7 lower bound and the FT4 sufficient threshold is at least order

\[
 \boxed{\frac{(a_h^5/A_f)}{(\alpha_{a_h}^2/b_g)}\asymp \frac{b_g}{A_fa_h}\asymp h^{-5/2}\longrightarrow\infty.}\tag{FT8}
\]

**Interpretation:** This is a rigorous *in-model obstruction* to the strategy “bound cap inverse self-susceptibility, then apply absolute-value Cauchy–Schwarz”. The method fails by a divergent refinement factor even when the **actual cap mass stays exactly Haar and its true cross response vanishes in each spectral window**. It is NOT a counterexample to the sought polynomial flat-cap theorem; rather it demonstrates why exploiting the relative geometry and the *signed cap–driver cyclic overlap* is essential. In particular, the largeness of \(S_W\) and \(S_a\) must not be mistaken for a large mixed response.

## 5. Exact rotor/character diagnostics and evidential limits

For a free SU(2) class rotor with electric coefficient \(A_f\), the center-even cap source has the orthonormal integer-character expansion \(k_a^+(U)=\alpha_a^2+\sum_{j\in\mathbb N_{\ge1}}\gamma_j\chi_j(U)\), \(\gamma_j=\beta_j^2/(2j+1)\), \(\beta_j=\int\phi_a\chi_j\). Its exact source self-susceptibility is

\[
 \boxed{S_a^{\mathrm{rotor}}=\sum_{j\ge1}\frac{\gamma_j^2}{A_fj(j+1)},\qquad
 F_a^{\mathrm{rotor}}=\alpha_a^2,\qquad S_a^{\mathrm{rotor}}/F_a^{\mathrm{rotor}}\asymp a^5/A_f.}
\]

The full proof of FT7 **does not** rely on this free-rotor equality; the latter is an independent check of the sharp power \(a^5\). The companion deterministic quadrature verifies \(S_a/Fa^{-5}\to\text{nonzero constant}\) for four shrinking radii. It separately diagonalizes a nonlinear SU(2) one-face rotor at \(b_g=4,25,100,400\) to test FT1–FT2 with \(A_g=4\). None of these tests is a diagonalization of the fully connected eight/nine-face Penrose Wilson model.

## 6. Remaining proof gate

The physical connected asymmetric Penrose deleted face has neither a known independent Haar portal nor a uniform reflection positivity certificate. Its relevant full-coupling quantity is still the signed, center-even **mixed** inverse spectral response

\[
 \mathcal C_{a,g}(u)=\operatorname{Re}\langle Q_uk_a^+\Omega_u,G_uQ_u(b_gd_g)\Omega_u\rangle.
\]

The new theorem establishes that bounding the two autocorrelation magnitudes separately cannot be a generally viable route; it must be the **relative spectral-cyclic overlap, signed cancellation, or a genuinely direct Wilson cap-mass lower bound**. The generic Penrose bulk estimate, fixed-support centered covariance, uniform physical mass gap, nonlinear quartic resolvent and continuum reconstruction remain open. No historical Stage26 datasets were modified.
