# R3-IR — Canonical target-center flux and spectrally filtered Wilson cap response

**Date:** 2026-10-29. **Classification:** exact finite, fully nonlinear physical SU(2) Wilson Hamiltonian theorem. The center-filtered response holds in **arbitrary connected asymmetric** planar rhombus disks. The improved cap minorant requires the **same reflection graph and parity-gap hypotheses** as the earlier reflection-asymmetry theorem. **OPEN:** generic reflection-free polynomial cap lower bound, bulk deletion, fixed-support connected covariance, mass gap and continuum reconstruction. Complete proof and independent verification package: \`singular_boundary_center_flux_spectral_filter_2026-10-29.zip\`, SHA256 \`91b10457eb8173a0434c6b78d584f416f9d131d6cca6ec3f65e7f83ece1179bf\`.

## CS-1. Canonical target-center involution on the Gauss-invariant physical sector

For a finite simply connected planar disk, set
\[
H_f^-=\sum_e a_e(-\Delta_e)+\sum_{g\ne f}b_g(1-p_g),\qquad p_g=\tfrac12\operatorname{ReTr}W_g.
\]
Its bounded faces and links have mod-2 cellular coboundary \(d_1:C^1(E;\mathbb Z_2)\to C^2(F;\mathbb Z_2)\). Because the disk has \(H^2=0\), choose a link center-flip cochain \(s\) with \(d_1s=\mathbf 1_f\). Center-multiplication of every link with \(s_e=1\) defines an exact unitary involution \(C_f\) commuting with all electric Laplacians and every retained magnetic potential while mapping \(W_f\mapsto-W_f\). Therefore
\[
\boxed{[H_f^-,C_f]=0,\qquad C_f\chi_j(W_f)C_f=(-1)^{2j}\chi_j(W_f).}
\]
Two strings \(s,s'\) with the same face-flux pattern differ by a closed 1-cochain; \(H^1(\mathrm{disk};\mathbb Z_2)=0\) makes this difference \(d_0t\), a product of vertex-center **gauge** transformations. Hence \(C_f\) is path-independent **on the physical Gauss-invariant Hilbert space**, not necessarily on the full link Hilbert space. Uniqueness and positivity make the magnetic-deleted physical ground state \(\Omega_u\) \(C_f\)-even for all retained magnetic coupling interpolations.

## CS-2. Exact elimination of center-odd spectral contributions to cap response

For any real central positive SU(2) convolution cap source \(k_a\) supported in \(B_a(I)\), with \(a<\pi/2\), define
\[
k_a^+(U)=\tfrac12[k_a(U)+k_a(-U)],\quad k_a^-(U)=\tfrac12[k_a(U)-k_a(-U)].
\]
Along the **exact full-coupling** one-neighbor interpolation \(H_f^-(u)=H_f^-(0)+uW,\ W=b_g(1-p_g)\), the vacuum \(\Omega_u\), \(W\), the reduced resolvent \(G_u\), and all positive-excitation spectral projectors \(P_{u,J}\) preserve target-center parity. As \(Q_uW\Omega_u\) lies in center parity \(+\),
\[
\boxed{
\langle Q_uk_a\Omega_u,G_uP_{u,J}Q_uW\Omega_u\rangle
=\langle Q_uk_a^+\Omega_u,G_uP_{u,J}Q_uW\Omega_u\rangle .
}
\]
This holds for every measurable spectral window \(J\), every \(u\in[0,1]\), and **without spatial reflection, a uniform gap, or Gaussian approximation**. In particular, the earlier low-energy adverse response contains **no target-center-odd excitations whatsoever**.

Since \(k_a(U)\) and \(k_a(-U)\) have disjoint supports and the vacuum is center even, the first moments, squared moments and first spectral moments obey the exact identities
\[
\boxed{
\langle k_a^+\rangle_u=\langle k_a\rangle_u=F_a(u),\quad
\langle(k_a^+)^2\rangle_u=\tfrac12\langle k_a^2\rangle_u,\quad
m_{1,u}(k_a^+)=\tfrac12m_{1,u}(k_a).
}
\]
Consequently the proved source-weighted \(f\)-sum \(m_{1,u}(k_a)\le C_k A_faF_a(u)\) improves to
\[
m_{1,u}(k_a^+)\le\tfrac12 C_k A_faF_a(u).
\]
This gains exactly \(1/\sqrt2\) in the high-energy cap-response Cauchy bound; the \(\Lambda=Lh^{-11/8}\) cutoff exponent is **unchanged**. It does **not** bound the remaining center-even low-energy response.

## CS-3. Reflection-and-center-resolved asymmetry theorem

When in addition a reflection seam \(\mathcal R\) fixes \(f\), it sends any target center string to another with the same face coboundary. Their difference is a vertex-center gauge transformation, so
\[
\boxed{[\mathcal R,C_f]=0\quad\text{on the Gauss-invariant physical space}.}
\]
The Hilbert space splits into four invariant \((\mathcal R,C_f)\) sectors. Let the reference \(H_0\) be globally reflection-paired and its unique vacuum \(\Omega_0\) be in \((+,+)\). Define the finite strictly positive excitation gaps
\[
\Delta_{+,+}=\inf\sigma(H_0|_{\mathcal H_{+,+}\cap\Omega_0^\perp})-E_0,\quad
\Delta_{-,+}=\inf\sigma(H_0|_{\mathcal H_{-,+}})-E_0.
\]
For a bounded, self-adjoint *reflection-odd and target-center-even* perturbation \(D\), with \(\|D\|\le\epsilon\), set \(H=H_0+D\). Unequal paired **magnetic** Wilson coefficients are covered; unequal electric coefficients are not. The unique positive ground state remains center even. Writing
\(\Omega=c\Omega_0+w_{+,+}+v_{-,+}\)
and projecting the exact ground-state equation yields
\[
(H_{0,-,+}-E)v=-P_{-,+}D(c\Omega_0+w),\qquad
Q_{+,+}(H_{0,+,+}-E)w=-Q_{+,+}Dv.
\]
The trial inequality \(E\le E_0\) and the sector resolvent bounds imply
\[
\boxed{
\|v\|\le r_c:=\epsilon/\Delta_{-,+},\quad
\|w\|\le s_c:=\epsilon^2/(\Delta_{+,+}\Delta_{-,+}).
}
\]
For the reflection-invariant target cap \(B_a\), the even-odd probability cross term vanishes. The prior symmetric kernel theorem supplies \(m_0(B_a)\ge H(a/2)\), \(H(a)=(a-\frac12\sin2a)/\pi\), hence
\[
\boxed{
m_{\rm asym}(B_a)\ge
\left[\sqrt{[1-r_c^2-s_c^2]_+}\sqrt{H(a/2)}-s_c\right]_+^2 .
}
\]
The center-even sector gaps are **at least as large** as the unfiltered reflection-sector gaps in the older asymmetry theorem, so this is a genuine sharpened sufficient condition. If \(r_c\le1/2\) and \(s_c\le\sqrt{H(a/2)}/4\), then \(m_{\rm asym}(B_a)\ge H(a/2)/4\). The gaps have **no known regulator-uniform lower bound**, and this theorem **does not apply without exact reflection geometry**.

## CS-4. A universal low-energy *center-odd* physical witness in the reflected reference

The reflection-seam theorem gives \(\langle\chi_1(W_f)\rangle_{\Omega_0}\ge0\), with \(\chi_1=4p_f^2-1\). Thus \(q=\langle p_f^2\rangle_{\Omega_0^2}\ge1/4\). The gauge-invariant trial state \(\Xi=2p_f\Omega_0\) is reflection even and **target-center odd**, orthogonal to \(\Omega_0\). The exact ground-state Dirichlet identity gives
\[
\|\Xi\|^2=4q,\qquad
\langle\Xi,(H_0-E_0)\Xi\rangle=A_f(1-q),\qquad A_f=\sum_{e\in\partial f}a_e.
\]
The physical min–max principle therefore proves
\[
\boxed{
\inf\sigma(H_0|_{\mathcal H_{+,-}})-E_0
\le\frac{A_f(1-q)}{4q}\le\tfrac34 A_f.
}
\]
When the link-electric coefficients are bounded, the **unfiltered** reflection-even gap and full physical gap are thus at most \(O(1)\) even at arbitrarily large retained magnetic coupling. This is a genuine physical excitation, **but by CS-2 it has exactly zero coupling to the center-even cap-response source**. It must not be used to assert a nonzero physical *mass* gap or to infer the size of the relevant center-even response.

The same trial's spectral first-moment bound implies at least \(1-3A_f/(4\Lambda)\) of its normalized spectral weight lies below \(\Lambda\), whenever the RHS is positive. Thus low-energy center-odd weight remains present at \(\Lambda=Lh^{-11/8}\) and is *irrelevant* to the cap response.

## Deterministic audit and exact open obligation

The companion Python checks the full 3×3 cellular incidence (9 faces, 24 links, 16 vertices), \(\mathrm{rank}_{\mathbb Z_2}(d_1)=9\), \(\mathrm{rank}(d_0)=15\), two target center strings related by a vertex-center gauge transform, reflection commutation on physical states, a five-state four-sector resolvent example, and the exact SU(2) Haar Rayleigh coefficient. It does **not** diagonalize an interacting nine-face SU(2) ground state.

**PROVED:** canonical flux and exact center-even spectral filtering on arbitrary planar disks, and the conditional sharper reflected-asymmetry sector bound. **OPEN:** control the true **center-even signed low-energy cap response** uniformly for fully connected **reflection-free** Penrose deleted interiors, or otherwise obtain an \(h^{3/2}\) center-cap lower bound; full bulk magnetic deletion, fixed-support covariance, physical mass gap, quartic resolvent, and continuum reconstruction.
