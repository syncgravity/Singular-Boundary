# The Singular Boundary — Center-even low-energy witness and exact portal spectral orthogonality

**Date:** 2026-10-29. **Program:** R3 independent reconstruction, SU(2) Wilson Hamiltonians on finite, simply connected, face-complete planar rhombus disks. **Classification:** two new exact full-nonlinear, finite-volume statements for **already established exact-Haar** deleted-face geometries (private edges, dual bridges, and open arcs); an exact, model-specific *frequency-resolved* response cancellation. The generic connected, asymmetric Penrose deleted-face probability, full physical mass gap, fixed-support connected covariance, quartic resolvent and continuum reconstruction remain **OPEN**.

## 1. Setup

Write

\[
H_f^-=\sum_{e}a_e(-\Delta_e)+\sum_{g\ne f}b_g\{1-p_g\},\qquad p_g=\tfrac12\mathrm{ReTr}(W_g),\qquad A_f=\sum_{e\in\partial f}a_e.
\]

All link Haar measures are normalized; the nonnegative electric coefficients obey the positive hypotheses from the R3 program and the magnetic coefficients are arbitrary nonnegative numbers. The unique normalized positive ground state \(\Omega\) is physical (vertex Gauss invariant); denote its energy \(E\), the nonnegative excitation operator \(K=H_f^--E\), the projection \(Q=I-|\Omega\rangle\langle\Omega|\), and spectral projectors \(P_J=\mathbf1_J(K)\). At finite volume \(K\) has discrete spectrum; there is no refinement-uniform gap assumption. The canonical deleted-target center involution \(C_f\) commutes with \(H_f^-\), fixes \(\Omega\), and acts on a spin-\(j\) face character with sign \((-1)^{2j}\), as established in the preceding center-flux theorem.

Assume \(W_f\) has the **exact normalized SU(2) Haar law** under \(|\Omega|^2\). This hypothesis is a theorem in the previously identified open-arc/dual-bridge/private-link geometries; it is **not known** for generic fully connected Penrose interiors.

## 2. CE-1: an unavoidable center-even low-energy physical excitation in the exactly-Haar class

Let \(X_f=\chi_1(W_f)=4p_f^2-1\). For Haar \(U\in SU(2)\), \(p=\cos u\), \(d\mu(u)=2\sin^2u\,du/\pi\), and the exact moments are

\[
\mathbb E_H p^2=\tfrac14,\qquad \mathbb E_H p^4=\tfrac18,
\qquad \mathbb E_H\chi_1=0,\quad\mathbb E_H\chi_1^2=1.
\]

Thus \(\Xi=X_f\Omega\) is **normalized, orthogonal to the vacuum, gauge invariant, and target-center even**. For each incident link, the SU(2) gradient identity is \(|\nabla_e p_f|^2=(1-p_f^2)/4\); therefore

\[
\Gamma(X_f)=\sum_{e\in\partial f}a_e|8p_f\nabla_ep_f|^2
=16A_f p_f^2(1-p_f^2).
\]

The exact positive-ground-state Dirichlet (Doob-transform) identity gives

\[
\boxed{\langle\Xi,K\Xi\rangle
=16A_f(\tfrac14-\tfrac18)=2A_f.}\tag{CE-1}
\]

By min–max, the **physical target-center-even excited spectral threshold** obeys

\[
\boxed{\delta_{f,+}^{\mathrm{exc}}\le 2A_f.}\tag{CE-2}
\]

For every \(\Lambda>0\), the spectral-measure first-moment Markov inequality gives

\[
\boxed{\|P_{(0,\Lambda]}\Xi\|^2
\ge [1-2A_f/\Lambda]_+.}\tag{CE-3}
\]

If \(a_e\le a_+\), then \(A_f\le4a_+\) and at the earlier low-energy cutoff \(\Lambda=Lh^{-11/8}\) the weight is at least \(1-8a_+h^{11/8}/L\), tending to one as \(h\to0\). This is true for *genuine nonlinear magnetic-deleted Wilson vacua* on every exact-Haar open-arc family, including cycle-bearing open-arc graphs. It is **not** evidence that the unknown connected Penrose vacuum itself has Haar law or a small center-even spectral gap. It demonstrates rigorously that excluding all low-energy center-even excitations cannot be a universal prerequisite for the desired cap bound.

## 3. CE-2: exact frequency-by-frequency orthogonality to a localized magnetic driver

Now assume the deleted magnetic Hamiltonian factorizes into independent magnetic-link components

\[
H_f^-=H_A\otimes I_B+I_A\otimes H_B,
\qquad\Omega=\Omega_A\otimes\Omega_B,
\]

as it does when the retained face-link adjacency splits into components (with any remaining free links absorbed into the appropriate factors). Assume an ordered proper contiguous target-boundary open arc \(U_A=U_A(\mathbf U_A)\in SU(2)\) is supported entirely in component \(A\), its complement \(U_B=U_B(\mathbf U_B)\in SU(2)\) is supported in \(B\), and the target Wilson word is cyclically equivalent to \(U_AU_B\). The independent component ground-state law makes \(U_A\) **exactly Haar** under \(\Omega_A^2\); this follows from the separate Gauss symmetry of the open-path endpoints and does not suppose that \(U_A\) is independent of *internal* component-A degrees of freedom.

Let \(O(W_f)\) be any bounded central gauge-invariant target observable and write its Haar mean \(\bar O=\int_{SU(2)}O(U)dU\). Define the operator \(\Pi_A=|\Omega_A\rangle\langle\Omega_A|\otimes I_B\). Haar invariance and the tensor factorization give the *exact conditional projection*

\[
\boxed{\Pi_A\,O(W_f)\Omega=\bar O\,\Omega.}\tag{CE-4}
\]

If the perturbation \(W_B\) is any bounded self-adjoint multiplier supported entirely in component \(B\) (in particular a restored or varied plaquette magnetic term within \(B\)), then

\[
QW_B\Omega\in\Omega_A\otimes\mathcal H_B^{\perp\Omega_B},
\quad
P_JQW_B\Omega\in\Omega_A\otimes\mathcal H_B^{\perp\Omega_B}
\]

for every Borel excitation-energy window \(J\subset(0,\infty)\); this follows because \(K=K_A\otimes I+I\otimes K_B\) preserves the \(\Omega_A\) tensor sector. The reduced resolvent \(G=QK^{-1}Q\) likewise preserves this sector. Meanwhile CE-4 implies \(\Pi_A QO\Omega=0\). Orthogonality proves

\[
\boxed{\langle QO\Omega,\,G P_J QW_B\Omega\rangle=0
\quad\text{for every }J\subset(0,\infty).}\tag{CE-5}
\]

In fact the entire **imaginary-time connected cross-correlation vanishes**:

\[
\boxed{\langle QO\Omega,e^{-tK}QW_B\Omega\rangle=0
\quad\text{for every }t\ge0.}\tag{CE-6}
\]

No full or center-even spectral gap estimate is invoked. The result holds at full positive retained Wilson couplings, for arbitrarily large component sizes and nonlinear interactions inside \(A\) or \(B\). It is a genuinely **spectral-frequency-resolved selection theorem**, stronger than merely saying the static cap expectation is Haar or the *total* susceptibility is zero.

The reflection-free geometry is allowed. For the seven-face two-cycle open-arc fixture there are two retained components meeting the target along two-edge open arcs; a magnetic driver supported in either component has the independent Haar portal in the other component. Hence every such localized driver has zero mixed response at each excitation energy, even while the source possesses the low-energy target-center-even excitation CE-1–CE-3.

**Essential limitation:** When restoring a plaquette that *joins* the two magnetic components, the tensor decomposition ceases to hold at nonzero coupling. CE-4–CE-6 then cannot be asserted. A generic fully connected Penrose deleted face has no independent proper portal component and remains outside the theorem. Avoid calling this a solution of the connected response.

## 4. CE-3: exact spectral-cyclic characterization of the surviving connected obstruction

For any finite magnetic-deleted Hamiltonian, define the **driver cyclic subspace** of \(v=QW\Omega\) by

\[
\mathcal C_W=\overline{\operatorname{span}\{P_Jv:\,J\subset(0,\infty)\text{ Borel}\}},
\qquad\Pi_W\text{ its orthogonal projector}.
\]

Because \(G\) and all \(P_J\) are spectral functions of \(K\), the mixed response depends only on the **spectral overlap** of the target source with this subspace:

\[
\boxed{\langle QO\Omega,G P_JQW\Omega\rangle
=\langle\Pi_W QO\Omega,G P_JQW\Omega\rangle.}\tag{CE-7}
\]

This identity, rather than an assumed high lower bound on every center-even excitation energy, is the structural target for future connected, asymmetric Penrose estimates. In the exact-Haar open-arc class with a component-supported driver, \(\Pi_W QO\Omega=0\) by CE-5; in the fully connected class no such overlap bound has yet been proved. CE-7 is an exact reformulation, **not a new bound** on the connected case.

## 5. Deterministic audit and boundary of evidence

The companion script verifies exact SU(2) Haar moments \(E p^2=1/4\), \(E p^4=1/8\), \(E\chi_1^2=1\), and the Dirichlet coefficient \(2A_f\); numerically confirms \(\int\chi_1(UV^{-1})dU=0\) for several noncentral, noncommuting quaternion rotations using tetrahedral directional cubature and radial Haar quadrature; diagonalizes a **nonlinear, continuous SU(2) class-rotor** magnetic driver with \(b=1,10,100\) to verify its self-susceptibility is strictly positive; and confirms the seven-face independent two-arc geometry versus the fully connected nine-face geometry. The exact spectral mixed-response nullity is analytic, not an artifact of the finite class-rotor truncation.

This checker does **not** diagonalize the complete eight/nine-face continuous SU(2) physical Hilbert space. The center-even witness is an exact physical many-link Wilson theorem under the Haar-law hypothesis; the class-rotor numbers are only independent local checks of a nontrivial driven component.

**PROVED:** CE-1–CE-7 at the explicit scopes above. **OPEN:** control the center-even spectral-cyclic overlap or the net signed one-neighbor/four-corner cap response of the fully connected *asymmetric* magnetic-deleted Penrose vacuum, so as to prove an \(h^{3/2}\) center-cap lower bound; all-bulk magnetic deletion, fixed-support connected covariance, physical uniform mass gap, quartic resolvent and continuum reconstruction. Any new uniform estimate must use actual connected Wilson dynamics and may not infer cap survival from parity filtration or the absence of low-energy center-even states alone.
