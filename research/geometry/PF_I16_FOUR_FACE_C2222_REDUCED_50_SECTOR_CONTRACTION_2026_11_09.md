# PF-I16 — Exact 50-sector reduction of first four-face linked SU(2) energy coefficient

**2026-11-09. Status: exact finite-order reduction and two algebraic checks; seven authentic four-face coefficients remain OPEN.** Full derivation, executable pure-Python exact-fraction checker, logs and checksum manifest: personal Library at \`/The Singular Boundary/Proof Audits/PF_I16_C2222_REDUCED_2026_11_09.zip\`. Prior original source-replay work certified seven marked graph classes among 18,900 Ngrid=7 four-face supports. No 3D cubic/Voronoi surrogate.

For any one certified original-link, four-face Hamiltonian \(\widehat H=K-\sum_{i=1}^4 b_i p_i\) with simple electric Haar vacuum, the Haar-mean-one ground state has an analytic wavefunction \(\Psi=1+\sum_{1\le|\alpha|\le4}\mathbf b^\alpha\psi_\alpha+O(\|\mathbf b\|^5)\). Rayleigh-quotient stationarity makes its eighth-order ground-energy coefficient **exact**: wavefunction error order 5 gives energy error order 10.

To extract **only** \(C_{2222}=[\mathbf b^{(2,2,2,2)}]E_0\), no wavefunction term with any exponent \(\alpha_i>2\) can contribute (all partner degrees are nonnegative). Therefore **50** coefficients \(\psi_\alpha\) suffice, instead of **70** unrestricted coefficients at total degree <=4:
\[
\boxed{\mathcal A=\{\alpha\in\{0,1,2\}^4:|\alpha|\le4\},\qquad
|\mathcal A|=1+4+10+16+19=50.}
\]
Only **19** pairings contribute to the kinetic term \(\langle\Psi_4,K\Psi_4\rangle\) at target degree eight, and exactly **52** face-insertion pairings to \(\langle\Psi_4,W\Psi_3\rangle\), where \(W=\sum_i b_i p_i\).

Define \(D_2=\langle\Psi_1,\Psi_1\rangle\), \(D_4=\langle\Psi_2,\Psi_2\rangle+2\langle\Psi_1,\Psi_3\rangle\), \(D_6=\langle\Psi_3,\Psi_3\rangle+2\langle\Psi_2,\Psi_4\rangle\), and \(N_8=\langle\Psi_4,K\Psi_4\rangle-2\langle\Psi_4,W\Psi_3\rangle\). Let \(E_j\) be homogeneous centered ground-energy polynomials. Then the exact target is
\[
\boxed{C_{2222}=[\mathbf b^{2222}]\bigl(N_8-E_2D_6-E_4D_4-E_6D_2\bigr).}
\]
The wavefunction Poisson recurrence also gives \(N_8=-\langle\Psi_4,W\Psi_3\rangle+E_2\langle\Psi_4,\Psi_2\rangle\) after degree-eight extraction.

**Independent exact rational verification 1 (deliberately disconnected control, NOT source):** four independent unit-electric SU(2) rhombi have one-face normalized character coefficients \(P_1=\chi_1/6\), \(P_2=\chi_2/96\), \(P_3=-5\chi_1/1728+\chi_3/2880\), \(P_4=(-37\chi_2+\chi_4)/138240\). Tensor-product wavefunctions yield \([\mathbf b^{2222}]N_8=-1/139968\) and \([\mathbf b^{2222}]E_2D_6=-1/139968\), hence **exactly \(C_{2222}=0\)** as required by factorization.

**Independent exact rational verification 2 (genuinely coupled original source links):** for two rhombi sharing one original SU(2) link, the exact two-loop identities \(K(xy)=(13/2)xy-(1/2)z,\ Kz=(9/2)z\) yield \(\psi_{11}=(4/39)xy+(4/351)z\). The corresponding second-order Rayleigh contraction recovers the previously independently computed **nonzero** fourth-order connected coefficient \(C_{22}=-1/8424\).

**Not completed in this continuation:** the seven authentic four-face \(\psi_\alpha\) Poisson systems and resulting seven rational \(C_{2222}\) coefficients. The reduction saves 20 wavefunction sectors and provides exact zero/nonzero controls, but does not establish connected coefficient convergence, a uniform interacting gap, source-selected physical energy/time, continuum/OS reconstruction, or 4D Yang–Mills mass gap. No canonical claim status or historical research data changed.