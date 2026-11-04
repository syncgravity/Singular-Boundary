# R3-IR — Parity-resolved source-connected tree majorant and factorial no-go

**Research date:** November 3, 2026. **Scope:** formal finite open straight-strip original-link SU(2) score coefficients, NOT volume-uniform interacting convergence or mass gap. The full mathematical audit, exact checker, log and SHA256 manifest are available in the conversation artifact R3_IR_PARITY_RESOLVED_CONNECTED_TREE_MAJORANT_2026-11-03.zip.

## Source-parity electric denominator

With independent fundamental plaquette source counts \(\mathbf m=(m_p)\), define \(d_e(\mathbf m)=\sum_{p:e\in\partial p}m_p\) and \(q_{\mathrm{odd}}(\mathbf m)=\#\{e:d_e(\mathbf m)\text{ odd}\}\). Every original-link output irrep label obeys \(\ell_e\equiv d_e(\mathbf m)\pmod2\). The corrected unit original-link free-electric operator K therefore has, on nonconstant gauge-invariant output sectors, the quantitative lower bound
\[
\boxed{\Lambda_\ell\ge D(\mathbf m)=\max(3,3q_{\mathrm{odd}}(\mathbf m)/4).}
\]
For electric coefficients >=a0, multiply by a0. For the three-face (1,2,1) coefficient, eight original links have odd incidence, giving D=6, the exact electric eigenvalue of the disconnected benchmark \(H=\chi_1(P_1)\chi_1(P_3)\).

## A source-connected positive majorant valid at each finite order

Assume the previously reported strong matrix Peter–Weyl projective Fourier multiplication bound \(\|fg\|_{P_0}\le\|f\|_{P_0}\|g\|_{P_0}\). An input with source degree \(\mathbf a\) has link irrep labels \(n_e\le d_e(\mathbf a)\). The generator estimate \(\|d\pi_{n_e}(X_{ea})\|\le n_e/2\), together with the parity-refined inverse and the three generator axes, gives
\[
\|\mathcal B(S_{\mathbf a},S_{\mathbf b})\|_{P_0}
\le\frac{3\sum_e d_e(\mathbf a)d_e(\mathbf b)}{4D(\mathbf a+\mathbf b)}
\|S_{\mathbf a}\|_{P_0}\|S_{\mathbf b}\|_{P_0}.
\]
For the normalized sources \(V_p=-\chi_1(P_p)/2\), the first-order strong projective Fourier norm is 64/3. Define the nonnegative majorant recursively by \(U_{\mathbf e_p}=64/3\), and for \(|\mathbf m|\ge2\),
\[
\boxed{U_{\mathbf m}=\sum_{\substack{\mathbf a+\mathbf b=\mathbf m\\|\mathbf a|,|\mathbf b|>0}}
\frac{3\sum_ed_e(\mathbf a)d_e(\mathbf b)}{4D(\mathbf m)}
U_{\mathbf a}U_{\mathbf b}.}
\]
Then \(\|S_{\mathbf m}\|_{P_0}\le U_{\mathbf m}\) for every finite source multiindex, conditionally on the Fourier multiplication theorem. This bound carries exact source-incidence linking and retains all physical fusion channels.

The exact deterministic checker obtains \(U_{121}=4194304/9\), about 466,033.78. By contrast, independently rerunning the previous physical ten-link three-face calculation gives the single normalized Haar projection \(\langle H,S_{121}\rangle=-1381/1261578240\), roughly -1.09466e-6. The values differ by a factor about 4.26e11, although they are not the same norm: U bounds the entire projective coefficient, while the benchmark is one projection.

## Structural no-go for the scalar majorant

For the genuine **single-plaquette** source series, all four links have incidence n and \(D(n)=3\), so
\[
U_n=\sum_{i=1}^{n-1}i(n-i)U_iU_{n-i},\qquad U_1=a=64/3.
\]
Set \(U_n=a^nb_n\). Then \(b_1=1\), \(b_n=\sum_{i=1}^{n-1}i(n-i)b_ib_{n-i}\), whose two endpoint terms imply \(b_n\ge2(n-1)b_{n-1}\), hence
\[
\boxed{b_n\ge2^{n-2}(n-1)!\quad(n\ge2).}
\]
Therefore the **positive scalar tree majorant** has zero power-series radius of convergence, even for a single face and with the exact source-parity electric denominator. This does NOT imply that the actual SU(2) one-face score diverges; it proves the specific absolute majorization scheme cannot prove convergence.

## Next objective

Retain exact output-spin Casimir denominators through character-resolved recurrence, and/or dress the single-plaquette Hamiltonian nonperturbatively before expanding the inter-face residual interactions. Verify that local repeated insertions are genuinely resummed and keep the exact nonzero (1,2,1) disconnected end-loop channel as a regression benchmark. Physical \(\lambda=1\) gap, infinite volume, 3D spatial geometry and the nontrivial R4 continuum mass gap remain open.

**Reproducibility:** exact Fraction verifier for incidence/parity, source-recursion coefficients and factorial lower bound; the previous original-link three-face verifier was rerun independently and passed all 62 assertions. The full operator proof depends on the named Peter–Weyl multiplication lemma and is not a formal machine proof.