# R3-IR — Center-even spectral abundance and open-arc portal orthogonality

**Date:** 2026-10-29. **Status:** exact full-nonlinear finite physical SU(2) Wilson theorems for **already proven exact-Haar** deleted-face classes (private links, dual bridges, open arcs); exact spectral-cyclic characterization on any finite Wilson system. **OPEN:** fully connected, reflection-free Penrose deleted-face cap probability, uniform bulk deletion and physical continuum Yang–Mills mass gap. Full proof, verification script, logs, manifest in \`singular_boundary_center_even_portal_spectral_2026-10-29.zip\` (SHA256 \`2a8736a3ee78761b844422266313d8153ebe64ba91d7dc167103be6898f2f0ac\`).

## CE-1. Exact physical center-even low-energy Wilson witness

Let \(H_f^-=\sum_ea_e(-\Delta_e)+\sum_{g\ne f}b_g(1-p_g)\), \(p_g=\tfrac12\operatorname{ReTr}W_g\), have normalized unique positive Gauss-invariant ground state \(\Omega\) and energy \(E\). Let \(A_f=\sum_{e\in\partial f}a_e\), \(K=H_f^--E\). Assume the target group holonomy \(W_f\) is **exact Haar under \(\Omega^2\)**. This is guaranteed by the prior open-arc/dual-bridge/private-edge theorems, **not** asserted for generic connected interiors.

For \(X_f=\chi_1(W_f)=4p_f^2-1\), SU(2) Haar moments give \(\langle p_f^2\rangle=1/4\), \(\langle p_f^4\rangle=1/8\), \(\langle X_f\rangle=0\), \(\langle X_f^2\rangle=1\). Thus \(\Xi=X_f\Omega\) is a **normalized, physical, target-center-even excited vector orthogonal to the vacuum**. Link gradients obey \(|\nabla_ep_f|^2=(1-p_f^2)/4\) on each incident edge. The exact positive-ground-state Dirichlet identity gives
\[
\langle\Xi,K\Xi\rangle
=\left\langle\sum_{e\in\partial f}a_e|\nabla_e X_f|^2\right\rangle
=16A_f\langle p_f^2(1-p_f^2)\rangle
=\boxed{2A_f}.
\]
Consequently the *physical target-center-even excited spectral threshold* obeys \(\delta_{f,+}\le2A_f\), independently of total magnetic coupling, volume, cycles and the presence/absence of spatial reflection.

For every cutoff \(\Lambda>0\), spectral Markov applied to the normalized excited vector yields
\[
\boxed{\|P_{(0,\Lambda]}(K)\Xi\|^2\ge [1-2A_f/\Lambda]_+.}
\]
If \(a_e\le a_+\), the previously used cutoff \(\Lambda_h=Lh^{-11/8}\) captures at least \(1-8a_+h^{11/8}/L\) of this **center-even** physical spectral weight. Thus low-energy center-even excitations need not be rare even when the target flat-cap probability is exactly Haar. This is an exact nonlinear physical model-family witness, not evidence of a generic connected-face Haar marginal.

## CE-2. Full-coupling spectral *orthogonality* in an independent open-arc geometry

Suppose the retained magnetic-link components factorize \(H_f^-=H_A\otimes I_B+I_A\otimes H_B\) and \(\Omega=\Omega_A\otimes\Omega_B\). A proper contiguous target boundary arc in component A has group holonomy \(U_A\) exactly Haar under \(\Omega_A^2\) by **component-wise Gauss symmetry**. All remaining target boundary edges are in B with group holonomy \(U_B\), and any central target observable can be written \(O(W_f)=O(U_AU_B)\), up to cyclic order. The target open-arc Haar law is an existing full-coupling theorem; arbitrary retained nonlinear Wilson interactions are permitted within each factor.

For every bounded central \(O\), write \(\bar O=\int_{SU(2)}O(U)\,dU\). Haar invariance proves the exact conditional ground-sector projection
\[
\boxed{\Pi_A O(W_f)\Omega=\bar O\,\Omega,\qquad
\Pi_A=|\Omega_A\rangle\langle\Omega_A|\otimes I_B.}
\]

Let \(W_B\) be any bounded self-adjoint magnetic perturbation supported **entirely in component B**. Then \(QW_B\Omega=\Omega_A\otimes Q_BW_B\Omega_B\). The spectral projections and reduced resolvent of \(K\) preserve the A-ground sector. Since \(\Pi_AQO\Omega=0\), for **every** Borel positive-excitation window \(J\) and **every** time \(\tau\ge0\):
\[
\boxed{\langle QO\Omega,G P_J QW_B\Omega\rangle=0,}
\qquad
\boxed{\langle QO\Omega,e^{-\tau K}QW_B\Omega\rangle=0.}
\]
These are frequency-by-frequency and time-by-time zeroes: they do **not** depend on a large physical spectral gap or on the absence of center-even excitations. For the seven-face open-arc two-cycle geometry, a neighbor driver contained in either of the two retained components has the other component as its independent Haar portal; its full-coupling cap response vanishes in every spectral window, despite the low-energy center-even witness above.

**Scope limit:** a perturbation which *joins* A to B destroys the tensor decomposition once switched on. The theorem does **not** assert zero response across that interpolation or in the fully connected nine-face and generic Penrose interiors.

## CE-3. Exact spectral-cyclic formulation of the connected obligation

For arbitrary finite \(H_f^-\), \(v=QW\Omega\), and positive-excitation spectral projectors \(P_J\), let \(\mathcal C_W=\overline{\operatorname{span}}\{P_Jv:J\subset(0,\infty)\}\), with orthogonal projector \(\Pi_W\). Spectral functional calculus yields the **exact identity**
\[
\boxed{\langle QO\Omega,G P_JQW\Omega\rangle
=\langle\Pi_WQO\Omega,G P_JQW\Omega\rangle.}
\]
For the disconnected Haar-portal class, \(\Pi_WQO\Omega=0\) for component-supported drivers. For the **fully connected asymmetric** Penrose magnetic-deleted vacuum, no quantitative upper bound on this overlap or the signed mixed response has been established. This is a structural characterization, **not a proof of the missing inequality**.

## Verification and evidence boundaries

Deterministic checker verifies SU(2) normalized Haar \(p^2,p^4\), spin-one norm and Dirichlet coefficient; evaluates \(\int_{SU(2)}\chi_1(UV^{-1})\,dU=0\) for noncentral rotations with exact tetrahedral angular second-moment quadrature; computes a **nonlinear continuous SU(2) class-rotor driver** at couplings 1,10,100 (strictly positive self-susceptibilities) while the portal mixed response vanishes by the analytical tensor identity; and distinguishes a seven-face two-component open-arc graph from a fully connected nine-face graph. The rotor is **not** a physical eight/nine-face SU(2) Penrose Hamiltonian simulation.

**PROVED:** CE-1, CE-2 and CE-3 in the scope stated. **OPEN:** a true connected-asymmetric Wilson spectral-overlap or signed full-coupling cap-response estimate, bulk deletion, fixed-support connected covariance, regulator-uniform physical gap, nonlinear quartic resolvent, continuum reconstruction.
