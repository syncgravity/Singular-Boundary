# Executable next gate: certified physical spin-network calculation

The proof provides an **exact certification algorithm**, not a claim that it has been applied successfully to the full eight-face connected Wilson Hamiltonian.

1. Use the 15-vertex, 22-link, eight-face square-rhombus graph specified in the preceding tree-gauge theorem. Delete the central target magnetic coefficient; retain all seven other positive Wilson coefficients at physical strength. Assign non-reflection-paired positive electric/magnetic coefficients as a nontrivial asymmetric test.
2. Enumerate complete **Gauss-invariant** spin networks on all 22 primal links, with vertex intertwiners and electric eigenvalue \(T=\sum_e a_ej_e(j_e+1)\le M\). Do not keep just products of individual plaquette characters. Check that the exact two-dimensional subblock in SN-1 appears within the pure-electric representation algebra.
3. Evaluate magnetic multiplication by \(p_q=\frac12\chi_{1/2}(W_q)\) using exact SU(2) Clebsch–Gordan/Wigner recoupling. Every plaquette insertion changes its four link spins by at most \(1/2\); therefore the off-block matrix \(Q_MVP_M\) has **finite support** in a calculable boundary shell of the electric cutoff. This allows rigorous \(\rho=\|Q_MVP_M\|\) and \(r=\|Q_MV\varphi\|\) evaluation without truncating that shell.
4. Diagonalize \(H_P\) with interval arithmetic or rigorous residual enclosures to obtain certified intervals for \(e_0,e_1\), their eigenvectors, and the cap expectation \(F_a^{(M)}\). Do not take floating eigenvalues as certified without enclosing numerical errors.
5. Check \(e_1<M\) and \(d=e_1-e_0-\rho^2/(M-e_1)>0\) conservatively using interval endpoints. Only when this passes does the observable error \(2\sqrt2\nu_a r/d\) apply to the true nonlinear physical ground state. If \(F_a^{(M)}-2\sqrt2\nu_a r/d>0\), the actual center-cap lower bound follows from SN-12 at that **finite** coefficient assignment.
6. Repeat over genuinely asymmetric configurations and a declared refinement family, with constants controlled uniformly, before upgrading to the generic Penrose bulk. No finite selection of patches proves a continuum mass gap.

## Why a class-only calculation is invalid

For the normalized physical target-center-even vector \(F=2\chi_1(W_f)p_g\), the class-only truncation discards \(Z=4\sqrt2p_f[p_{\partial(f\cup g)}-p_fp_g]\). Its exact electric off-diagonal matrix element is \(-\sqrt2a_e\), and its full-time electric cross response is nonzero (SN-3 to SN-4). This is not a numerical discretization artifact.

## Why the energy-tail cutoff does not finish the proof

The estimate \(\|Q_M\Omega\|^2\le S_H/M\) controls the **projected unknown true ground state**, not the Ritz eigenvector. SN-9 to SN-12 require additional computed gap and off-block residual certificates. On a fixed eight-face refinement, the blunt cap-observable norm estimate suggests a sufficient \(M=O(h^{-4})\) to control \(F_a\) at Haar order. This very large cutoff is a **conservative sufficient scale, not a necessity theorem**. Localized/cap-weighted residual estimates might dramatically improve it, but such an improvement is not proved here.
