# The Singular Boundary — Canonical deleted-face center flux, exact spectral filtering, and sharpened reflection-asymmetry comparison

**Date:** 2026-10-29. **Classification:** finite-volume, fully nonlinear SU(2) Wilson Hamiltonian theorems on simply connected face-complete planar rhombus disks. The symmetry filtering applies to **arbitrary connected, reflection-free interiors**, with no gap assumption. The quantitative cap lower bound in the latter part still requires exact reflection geometry and sector gap hypotheses. The reflection-free polynomial-cap estimate, full physical mass gap, and continuum reconstruction remain OPEN.

## 1. Exact face-flux symmetry on the physical gauge Hilbert space

Let a finite simply connected edge-to-edge rhombus disk have oriented vertices V, links E, and bounded faces F; all boundary link variables are integrated with normalized SU(2) Haar and all vertex Gauss transformations are imposed. Write

\[
H_f^-(\mathbf b)=\sum_{e\in E}a_e(-\Delta_e)+\sum_{g\ne f}b_g\left(1-\tfrac12\operatorname{ReTr}W_g\right),\qquad a_e>0,\quad b_g\ge0.
\]

A binary link 1-cochain \(s\in C^1(E;\mathbb Z_2)\) acts unitarily by \((C_s\Psi)(U)=\Psi((-1)^{s_e}U_e)\). It commutes with every link Laplacian. The sign of the face holonomy is \((-1)^{(d_1s)_g}\). Since a topological disk has \(H^2(D;\mathbb Z_2)=0\), the cellular coboundary \(d_1:C^1(E;\mathbb Z_2)\to C^2(F;\mathbb Z_2)\) is surjective. Thus choose a center string \(s\) with \((d_1s)_g=\mathbf1_{g=f}\). This sends \(W_f\mapsto-W_f\) and fixes **all** retained plaquette holonomies, giving an exact involutive symmetry

\[
\boxed{[C_f,H_f^-(\mathbf b)]=0,\quad C_f\chi_j(W_f)C_f=(-1)^{2j}\chi_j(W_f).}\tag{CS-1}
\]

Two choices \(s,s'\) differ by a closed 1-cochain. Since \(H^1(D;\mathbb Z_2)=0\), \(s-s'=d_0t\); its action on link variables is precisely a product of SU(2) **vertex-center gauge transformations**. Consequently \(C_f\) is **independent of the dual path on the Gauss-invariant physical Hilbert space**. It need not be path independent on the unreduced product-link Hilbert space; this distinction is essential.

The finite-volume unique positive physical vacuum \(\Omega_f^-(\mathbf b)\) is \(C_f\)-even: uniqueness and positivity force the center-invariant choice. The statement remains valid at all positive coupling strengths and all arbitrary electric coefficients, as well as under any interpolation changing only retained magnetic terms.

## 2. CS-2: exact elimination of center-odd states from cap response

Choose a positive smooth central SU(2) convolution cap source \(k_a(U)\), supported in \(B_a(I)\) for \(a<\pi/2\). Let

\[
 k_a^{+}(U)=\tfrac12[k_a(U)+k_a(-U)],\qquad
 k_a^{-}(U)=\tfrac12[k_a(U)-k_a(-U)].
\]

For the exact one-neighbor interpolation \(H_f^-(u)=H_f^-(0)+uW\), \(W=b_g(1-p_g)\), the operator \(W\), the excited-state reduced resolvent \(G_u\), its positive spectral projectors \(P_{u,J}\), and the vacuum \(\Omega_u\) all have \(C_f\)-parity even. Therefore

\[
\boxed{\langle Q_uk_a\Omega_u,G_uP_{u,J}Q_uW\Omega_u\rangle
=\langle Q_uk_a^+\Omega_u,G_uP_{u,J}Q_uW\Omega_u\rangle.}\tag{CS-2}
\]

In particular the full low-energy adverse response \(\mathcal B_{a,\le\Lambda}\) from the previous double self-weighted theorem receives **no contributions whatsoever from target center-odd excitations**, for any neighboring coupling \(0\le u\le1\). This is an exact finite physical-sector reduction, without a spectral-gap assumption and without spatial reflection symmetry.

Because the two supports \(B_a(I)\) and \(B_a(-I)\) are disjoint and the marginal is center-even, one has the exact equalities

\[
 \boxed{\langle k_a^+\rangle_u=\langle k_a\rangle_u=F_a(u),\quad
 \langle(k_a^+)^2\rangle_u=\tfrac12\langle k_a^2\rangle_u,\quad
 m_{1,u}(k_a^+)=\tfrac12m_{1,u}(k_a).}\tag{CS-3}
\]

For the previously proved self-weighted source gradient bound \(m_{1,u}(k_a)\le C_kA_fa F_a(u)\), equation CS-3 improves the constant to

\[
 \boxed{m_{1,u}(k_a^+)\le\tfrac12C_kA_faF_a(u).}\tag{CS-4}
\]

Thus the ultraviolet source estimate in the cap-response theorem improves by a factor \(1/\sqrt2\) while its \(h^{-11/8}\) cutoff exponent remains unchanged. The unknown **center-even** low-energy signed response remains the obstruction; this result does **not** bound it.

## 3. CS-5: sharpened reflection-asymmetry theorem in the *relevant* center sector

Suppose additionally that the *reference* deleted Wilson Hamiltonian \(H_0\) admits the global link-free reflection seam of the previous reflection-cone theorem, and let \(\mathcal R\) be the corresponding unitary on the **Gauss-invariant physical Hilbert space**. Since the reflection fixes the target face, \(\mathcal R C_f\mathcal R^{-1}\) acts with exactly the same face-flux sign pattern as \(C_f\). By CS-1 their difference is a vertex-center gauge transformation. Therefore

\[
\boxed{[\mathcal R,C_f]=0\quad\text{on the physical Hilbert space}.}\tag{CS-5}
\]

The physical Hilbert space has four invariant blocks \(\mathcal H_{r,c}\) for \(r,c\in\{+,-\}\), with reflection and target-center parity respectively. Let \(\Omega_0\in\mathcal H_{+,+}\) be the unique reference ground state, with energy \(E_0\). Define

\[
\Delta_{+,+}=\inf\sigma(H_0|_{\mathcal H_{+,+}\cap\Omega_0^\perp})-E_0,\quad
\Delta_{-,+}=\inf\sigma(H_0|_{\mathcal H_{-,+}})-E_0.
\]

Both are strictly positive at finite volume; their refinement-uniform lower bounds are **unknown**. Let \(D\) be any bounded self-adjoint **reflection-odd, target-center-even** perturbation, so \(\mathcal R D\mathcal R=-D\), \(C_fDC_f=D\), and \(\|D\|\le\epsilon\). This includes the previously described reflection-paired **magnetic coefficient mismatch**; unequal electric coefficients are still not covered. By CS-1 the actual perturbed positive ground state remains in center parity \(+\).

Repeating the *exact nonperturbative* reflection-sector resolvent proof exclusively in center parity \(+\) yields

\[
\boxed{\|v_{-,+}\|\le r_c:=\epsilon/\Delta_{-,+},\quad
\|w_{+,+}\|\le s_c:=\epsilon^2/(\Delta_{+,+}\Delta_{-,+}).}\tag{CS-6}
\]

The cap lower bound therefore improves to

\[
\boxed{m_{\rm asym}(B_a)\ge
\left[\sqrt{[1-r_c^2-s_c^2]_+}\sqrt{H(a/2)}-s_c\right]_+^2.}\tag{CS-7}
\]

The new spectral denominators are **at least as large as** the old reflection-only denominators (because the subspaces are smaller). Thus the result is never weaker, and may be substantially stronger when the original smallest excitations are target center-odd. For example, if \(r_c\le1/2\) and \(s_c\le\sqrt{H(a/2)}/4\), one again obtains \(m_{\rm asym}(B_a)\ge H(a/2)/4\). All earlier geometric and electric-pairing hypotheses remain required. This is **not** an extension to reflection-free Penrose patches.

## 4. CS-8: an exact low-energy physical witness that is *irrelevant* to the cap response

On the reference reflection-symmetric deleted Hamiltonian, the previous reflection-cone theorem proves every Wilson character expectation nonnegative. In particular \(\chi_1(W_f)=4p_f^2-1\) has nonnegative mean, so

\[
 q:=\langle p_f^2\rangle_{\Omega_0^2}\ge\tfrac14.
\]

The gauge-invariant trial state \(\Xi=2p_f\Omega_0\) lies in the physical reflection-even, **target-center-odd** sector \(\mathcal H_{+,-}\), and is orthogonal to \(\Omega_0\). Its exact norm and ground-state-transformed electric quadratic form are

\[
\|\Xi\|^2=4q,\qquad
\langle\Xi,(H_0-E_0)\Xi\rangle=A_f(1-q),\quad A_f=\sum_{e\in\partial f}a_e.
\]

Therefore

\[
\boxed{\inf\sigma(H_0|_{\mathcal H_{+,-}})-E_0\le
\frac{A_f(1-q)}{4q}\le\frac34 A_f.}\tag{CS-8}
\]

In the reflection-symmetric model, **the unfiltered physical spectral gap and the original reflection-even-sector gap are bounded above by \(3A_f/4=O(1)\)**, regardless of how strongly the retained magnetic plaquettes are coupled. This low-energy excitation is genuine and gauge-invariant. But by CS-2 it is **exactly decoupled** from the cap-response mixed matrix element. Hence it is inappropriate to base the proof's final low-energy obligation on an unfiltered mass-gap estimate.

Moreover, for \(\Lambda>0\), Markov's spectral-moment inequality shows the normalized state \(\Xi/\|\Xi\|\) has at least \(1-3A_f/(4\Lambda)\) of its spectral norm below excitation energy \(\Lambda\) (when this is positive). The low-energy presence of center-odd excitations at the earlier \(\Lambda=Lh^{-11/8}\) cutoff is therefore not only possible but forced in this symmetric family—and irrelevant to the source response.

## 5. Verification, rigorous scope, and remaining priority

The companion script verifies the complete 3×3 rhombus-cell incidence and binary cochain identities \(\ker d_1=\mathrm{im}\,d_0\) using ranks \(\operatorname{rank}d_1=9\), \(\operatorname{rank}d_0=15\); constructs two distinct dual paths with identical target-face sign, checks their difference is a vertex-center gauge transformation, and confirms diagonal-reflection commutation on physical states. A five-state parity-sector toy verifies the improved exact resolvent inequalities while exhibiting an unfiltered gap dominated by center-odd states. SU(2) Haar quadrature verifies the physical fundamental-character trial normalization and Rayleigh coefficient. This is **not a numerical diagonalization of the eight/nine-face physical SU(2) Hamiltonian**.

**PROVED:** CS-1 through CS-8 under their explicit hypotheses; the exact center-even filtering holds on all simply connected planar rhombus disks, including fully connected asymmetric Penrose interiors. **OPEN:** a gap-independent full-coupling estimate of the **center-even** signed mixed cap response for those Penrose interiors; a reflection-free center-cap minorant; all-bulk deletion; fixed-support Wilson-angle connected covariance; regulator-uniform physical Yang–Mills mass gap; quartic resolvent and continuum reconstruction. Center parity and spectral selection alone do not imply a quantitative small-ball lower bound.
