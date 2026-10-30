# Graded multilocal Wilson frames: exact interacting completeness, finite-window certification, and decay/gap equivalence

**Status: rigorous finite-regulator theorems; no uniform 2+1-dimensional continuum Yang–Mills gap proved.**

## Model
On a finite connected square or Penrose rhombus graph with compact SU(2) link variables take the gauge-invariant Hilbert space \(\mathcal H=L^2(SU(2)^E)^{SU(2)^V}\), Hamiltonian \(H=\sum_e a_e(-\Delta_e)+\sum_f b_f(1-\tfrac12\mathrm{Tr} W_f)\) with \(a_e>0,b_f\ge0\), positive unique ground state \(\Omega\) and \(K=H-E_0\). Let \(\mathcal H_\mathrm{cen}\) be a closed reducing center-neutral sector containing the vacuum, and \(\mathcal X=\mathcal H_\mathrm{cen}\ominus\mathbb C\Omega\). A simply connected disk has no winding center sectors. More general Wilson traces must include winding sectors where appropriate and center-neutral products must be used to span \(\mathcal H_\mathrm{cen}\).

The elliptic finite-graph kinetic operator has compact resolvent on the compact gauge configuration quotient, and adding the bounded Wilson magnetic potential preserves compact resolvent. Hence the excited gap \(\Delta_G=\inf\mathrm{spec}(K|_\mathcal X)>0\) **at each fixed finite graph**. No uniformity in \(G,h\) is asserted.

## Theorem 1: exact interacting Wilson polynomial Parseval frame, without spectral input
Choose a countable, degree-graded enumeration of real/complex gauge-invariant Wilson trace polynomials \(A_n\), restricting to a dense subalgebra of the center-neutral sector, including products of distant connected loops. By SU(2) invariant tensor algebra, Wilson traces and their products span a dense invariant algebra (for a simply connected graph no winding qualification is needed). Let \(v_n=Q A_n\Omega\), discarding zeros and perform **ordinary Gram–Schmidt in the interacting \(L^2\) inner product**. This produces vectors \(u_n\) forming an ONB of \(\mathcal X\) and source multipliers \(\widehat A_n\) which are finite linear combinations of earlier Wilson polynomials and satisfy \(u_n=Q\widehat A_n\Omega\). The unitary synthesis \(B:\ell^2\to\mathcal X\), \(Bc=\sum_nc_nu_n\), has
\[
BB^*=I_\mathcal X,\qquad C(t)=B^*e^{-tK}B,\quad\boxed{\|C(t)\|=e^{-t\Delta_G}},\quad t\ge0.
\]
This construction is exact for the interacting ground state; the orthonormalization generally destroys localization and can have unbounded Wilson polynomial coefficients and complexity. **The time-correlation norm identity is an equivalence/re-expression of the finite-graph gap, not an independent dynamical gap bound.** It cannot be used to infer cutoff-uniform decay without independent control of \(\Delta_G\).

## Theorem 2: finite-graded, finite-window quantitative observability
Let \(P_N\) project onto the first \(N\) vectors from Theorem 1, and \(E_\eta=\mathbf1_{(0,\eta]}(K|_\mathcal X)\). Because \(P_N\to I\) strongly and \(E_\eta\) has finite rank, for any \(0<\varepsilon<1\) there exists a finite \(N=N(G,\eta,\varepsilon)\) with
\[
\|(I-P_N)E_\eta\|^2\le\varepsilon,\qquad \boxed{E_\eta P_NE_\eta\ge(1-\varepsilon)E_\eta}.
\]
For the truncated synthesis \(B_N\), \(\|B_N^*e^{-tK}B_N\|\le e^{-t\Delta_G}\), and source norm/operator norm are 1, without volume factor. **Neither** the degree/source count \(N\), nor its geographic support, nor \(\Delta_G\) is uniform in \(h,G\). This is finite-window, finite-cutoff constructive observability, not R3.

## Theorem 3: two-sided correlation-gap comparison and the sharp diagnostic
For any bounded synthesis \(B\), \(S=BB^*\), and \(C(t)=B^*e^{-tK}B\), let \(E_\eta\) project onto \((0,\eta]\). If \(E_\eta S E_\eta\ge cE_\eta\), and \(K|_\mathcal X\) has lowest eigenvalue \(\Delta\le\eta\) with normalized eigenvector \(\psi_\Delta\), then
\[
\boxed{c e^{-t\Delta}\le\|C(t)\|\le\|S\|e^{-t\Delta}},\qquad t\ge0.
\]
Proof: the upper inequality is \(\|e^{-tK/2}S e^{-tK/2}\|\le\|S\|e^{-t\Delta}\). The lower inequality is the Rayleigh quotient on \(\psi_\Delta\): \(\langle\psi_\Delta,e^{-tK/2}Se^{-tK/2}\psi_\Delta\rangle=e^{-t\Delta}\langle\psi_\Delta,S\psi_\Delta\rangle\ge c e^{-t\Delta}\). Thus any uniform upper bound \(\|C_h(t)\|\le M f(t)\to0\), with uniform lower-frame bound \(c>0\) and a sequence of gaps \(\Delta_h\to0\), is impossible: choose \(t\) large such that \(Mf(t)<c/2\), then \(h\) with \(t\Delta_h\ll1\) gives contradiction.

This characterizes the actual **missing physical dynamical content**. A uniform decay theorem and uniform low-energy observability are already essentially a gap theorem. Equal-time Wilson variance decay or the one-face character identities do not prove it.

## Theorem 4: exact Euclidean transfer matrix certification on a finite graph
When a positive, reflection-positive transfer operator \(T\) on the physical Hilbert space is defined, and \(\lambda_0\) is its unique maximal eigenvalue, set \(\widetilde T=T/\lambda_0\) and \(K_{a_t}=-a_t^{-1}\log\widetilde T\) on the positive spectrum. The exact connected matrix of the whitened Wilson family at integer time separation \(n a_t\) is
\[
C_N(n a_t)_{ij}=\langle u_i,\widetilde T^n u_j\rangle.
\]
For the complete ONB of the center-neutral excited sector \(\|C(n a_t)\|=(\lambda_1^{\rm cen}/\lambda_0)^n\); this is exact spectral equivalence, not a derived bound on the ratio. For truncated sources one obtains only a lower bound on the full transfer norm; finite matrices **cannot exclude dark states** without a separately proved lower observability inequality. Fixed-graph temporal-continuum expansion and spatial \(h\to0\) uniformity must be treated separately.

## Recommended noncircular proof gate
An admissible R3 proof would exhibit a **physically defined**, spatially controlled and source-count-normalized Wilson family \(B_{h,G}\), and show both (i) \(E_{\eta,h,G}B_{h,G}B_{h,G}^*E_{\eta,h,G}\ge cE_{\eta,h,G}\), and (ii) an independent full-dynamics estimate for \(\|B_{h,G}^*e^{-tK_{h,G}}B_{h,G}\|\), uniform in time, volume and \(h\). Theorems 1–4 show how to audit and normalize these conditions, but furnish **no** independent uniform gap input. An R2 theorem additionally needs vacuum/OS reconstruction, physical time/coupling calibration, tightness and nontriviality of renormalized Schwinger functions, and limiting lower spectral control.

**Connection to dissertation Papers 2–4:** Their cut-and-project geometry, \(C_5\) structure and graph spectral claims do not independently imply any time-correlation operator-norm estimate of the above form. The frame uses the actual interacting Hamiltonian and Wilson sources. No assertion is made that a static graph one-loop ratio establishes a Yang–Mills mass gap.
