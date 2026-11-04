# R3-IR — Dressed residual: total-bond stability and independent three-face regression

**Research date:** November 3, 2026. **Scope:** finite open straight square SU(2) strips, corrected unit original-link electric operator, fundamental magnetic source with real individual couplings |z_i|≤3/4. A **restricted** uniform-in-N gap criterion for the full Hamiltonian, NOT a homogeneous thermodynamic interacting gap, full 3D theory, or 4D continuum Yang–Mills mass gap. Expanded proof and reproducible script: conversation archive R3_IR_DRESSED_RESIDUAL_TOTAL_BOND_STABILITY_2026-11-03.zip.

## Inputs
For \(H_N=K-\frac12\sum_i z_i\chi_1(P_i)\), use exact local one-face ground states \(\psi_i=1+u_i\), with \(\|u_i\|_{\mathcal W}\le1/2\), \(1/2\le\psi_i\le3/2\), and local eigenvalues \(E_i=-z_i a_{1,i}/2\). The preceding dressed reference theorem gives \(\operatorname{gap}(L_0)\ge1/12\) uniformly in N for \(L_0=K-2\Gamma_K(\sum_i \log\psi_i,\cdot)\), in the dressed product measure. Exact transform:
\[
\Phi^{-1}(H_N-\sum_iE_i)\Phi=L_0+W,\qquad
\Phi=\prod_i\psi_i,\quad W=-2\sum_{i=1}^{N-1}\Gamma_K(\log\psi_i,\log\psi_{i+1}).
\]

## Local residual bound
For a boundary-link Lie generator X of face i, the character bound \(|X\chi_n|\le n(n+1)/2\), and \(n\le n(n+2)/3\), imply
\[
\|X\psi_i\|_\infty\le\frac16\|K\psi_i\|_{\mathcal W}.
\]
From \(K\psi_i=(z_i/2)\chi_1\psi_i+E_i\psi_i\), \(\|\psi_i\|_{\mathcal W}\le3/2\), \(\|\chi_1\|_{\mathcal W}=2\), and \(|E_i|\le|z_i|/8\), it follows that \(\|K\psi_i\|_{\mathcal W}\le27|z_i|/16\). Thus
\[
\boxed{\|X\log\psi_i\|_\infty\le9|z_i|/16,\qquad
\|W_{i,i+1}\|_\infty\le243|z_i z_{i+1}|/128.}
\]

## Restricted full physical spectral-gap theorem
Define \(B(\mathbf z)=\sum_{i=1}^{N-1}|z_i z_{i+1}|\). The min-max principle and \(\operatorname{osc}(W)\le2\|W\|_\infty\) give
\[
\boxed{\operatorname{gap}(H_N)\ge \frac1{12}-\frac{243}{64}B(\mathbf z).}
\]
In particular \(B(\mathbf z)<16/729\) certifies a positive gap, **independent of N**. The criterion covers a uniformly bounded total number/strength of interacting neighbor bonds or alternating active faces with B=0. For homogeneous nonzero \(z_i=z\), B=(N−1)z², so this estimate becomes vacuous as N→∞. The theorem does NOT solve the dense thermodynamic interacting gap.

## Independently dressed three-face regression
Set \(\Psi=\Phi e^T\). The *dressed* correction equation is
\[
L_0T=\epsilon-W+\Gamma_K(T,T),\qquad \epsilon=E_{\mathrm{full}}-\sum_iE_i.
\]
For mixed multidegrees, solve the separate recursion
\[
KT_{\mathbf m}=Q\left[2\sum_{i\sim j}\Gamma_K(s_i,s_j)+2\Gamma_K(\sum_i s_i,T)+\Gamma_K(T,T)\right]_{\mathbf m}
\]
with \(s_i^{(1)}=\chi_1(P_i)/6\), \(s_i^{(2)}=-\chi_1(P_i)^2/288\) modulo constants, using the corrected ten-original-link trace calculus. This does **not** derive T by subtracting the previously computed undressed S. Exact rational inversions for six mixed degrees (110,011,120,021,111,121) pass their electric residuals. Quaternion Haar projection reproduces
\[
\boxed{\langle\chi_1(P_1)\chi_1(P_3),T_{121}\rangle=-1381/1261578240.}
\]
The local score has no mixed term, so this is also the full logarithmic vacuum-score coefficient. The regression is independent at the level of its dressed nonlinear recursion but shares the earlier original-link trace engine, not a completely independent operator implementation.

## Verification
The bundled deterministic checker passed **301** exact arithmetic, gap-threshold and regression assertions; the separate dressed recursion solver verified each mixed coefficient and the final exact fraction. The analytic proof above establishes the inequalities; finite checks are not formal proof. Full report, both scripts, original-link trace engine, quaternion projector, logs, and SHA256 manifest are in the attached archive.

## Next obligation
A **local-density** (not total-bond) stability theorem for arbitrarily many adjacent interactions at fixed homogeneous \(z\) is still required. Candidate techniques: conditional Poincaré/Dobrushin estimates, martingale/local-gap methods, or a convergent connected dressed-residual expansion retaining all physical fusion channels. Then extend beyond straight strips and track physical-unit mass gap through the nontrivial 4D continuum construction.
