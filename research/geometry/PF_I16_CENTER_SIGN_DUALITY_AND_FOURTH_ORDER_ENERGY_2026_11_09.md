# PF-I16 — Independent SU(2) face-center duality and first quantum-linked energy

**Research audit: 2026-11-09.** Authentic accepted Penrose–Fibonacci \(\mathbb Z^5\) source links and triangle-tested rhombi, not a cubic/Voronoi replacement. Full proof, eight-size replay, exact fourth-order checker and hash manifest in Library: \`/The Singular Boundary/Proof Audits/PF_I16_CENTER_SIGN_DUALITY_2026_11_09.zip\`. This is a finite **auxiliary Hamiltonian** result, not a source-derived physical time or mass gap.

## Exact new theorem: independent face-sign duality

PF-I11 established free-face collapsibility; the independent PF-I16 replay in this archive reconfirms all 71,836 original faces across eight selections \(N_{\rm grid}=7,10,12,15,18,20,23,25\) and constructs three independently prescribed face-sign patterns at **each** size. Counts of successful face-edge collapses: 1468, 2886, 4145, 6800, 9646, 11879, 16138, 18874, respectively. The source selection was reconstructed from the indexed unpublished generator code, not executed from SHA-pinned source bytes in this pass.

An elementary free-face collapse all the way to a graph proves \(H^2(K;\mathbb F_2)=0\), hence the face coboundary \(d_1:C^1(K;\mathbb F_2)\to C^2(K;\mathbb F_2)\) is onto. In constructive form, for **any** prescribed independent \(\eta_f=\pm1\) choose original-link signs \(\sigma_e=\pm1\) whose product around each accepted face equals \(\eta_f\). Reverse the free-face elimination order to solve for the chosen link sign of each face.

Because \(\pm I\) is central in SU(2), replacing \(U_e\mapsto\sigma_eU_e\) preserves normalized Haar measure, the Gauss-invariant subspace and each electric Casimir \(C_e\), while it sends \(p_f=\frac12\mathrm{Tr}U_f\mapsto\eta_fp_f\). The unitary link translation therefore proves the exact all-coupling centered spectral duality
\[
\boxed{\widehat H(\mathbf b):=K-\sum_fb_fp_f
\simeq \widehat H((\eta_fb_f)_f)\quad\forall\eta\in\{\pm1\}^F.}
\]
This relates *different coupling parameters*; it is not a new fixed-coupling gauge symmetry. The uncentered \(H(\mathbf b)=K+\sum_fb_f(1-p_f)\) differs from \(\widehat H\) by the scalar \(\sum_fb_f\). The simple ground-state eigenvalue of \(\widehat H\), analytic near \(\mathbf b=0\) on a fixed finite graph, is **even separately in each face coupling**: every Taylor monomial with any odd face exponent vanishes.

PF-I11-E previously proved exact classical plaquette-only Wilson partition factorization from the same free-face collapses. The following quantum Hamiltonian perturbative result is distinct.

## Exact degree-four centered ground-state energy, including the first quantum-linked source-face term

Let \(\lambda_f=\frac34\sum_{e\in\partial f}a_e\) and \(R=K^{-1}P_0\) on the Haar-mean-zero gauge-invariant subspace. Let \(W=\sum_fb_fp_f\) act by multiplication. Standard vacuum-projected perturbation gives \(E_2=-\langle W1,RW1\rangle=-\sum_fb_f^2/(4\lambda_f)\) and
\[
E_4=\langle W1,RW1\rangle\langle W1,R^2W1\rangle-
\langle W R(W1),R\,W R(W1)\rangle.
\]
The one-face quartic coefficient is \(5/(128\lambda_f^3)\).

If two distinct faces share **no original edge**, their mixed \(b_f^2b_g^2\) coefficient vanishes exactly. If genuine simple source rhombi \(f,g\) share one original edge \(s\) with electric coefficient \(a_s>0\), define \(L=\lambda_f+\lambda_g\), \(\Lambda_0=L-\frac32a_s\), and \(\Lambda_1=L+\frac12a_s\). The actual SU(2) singlet/triplet decomposition of \(p_fp_g\) has squared norms \(1/64\) and \(3/64\) and respective electric energies \(\Lambda_0,\Lambda_1\). The exact connected coefficient is
\[
\boxed{C_{fg}=\frac{L}{16\lambda_f^2\lambda_g^2}
-\frac{L^2}{64\lambda_f^2\lambda_g^2}
\left(\frac1{\Lambda_0}+\frac3{\Lambda_1}\right)
=-\frac{3a_s^2L}{64\lambda_f^2\lambda_g^2\Lambda_0\Lambda_1}<0.}
\]
For unit electric links, \(\lambda_f=\lambda_g=3\), \(\Lambda_0=9/2\), \(\Lambda_1=13/2\), and \(\boxed{C_{fg}=-1/8424}\). The one-face quartic coefficient is \(5/3456\).

Thus, on any **fixed** original authenticated finite source complex, at small couplings,
\[
\boxed{\widehat E_0(\mathbf b)
=-\sum_f\frac{b_f^2}{4\lambda_f}
+\sum_f\frac{5b_f^4}{128\lambda_f^3}
+\sum_{\{f,g\}:f\sim g}C_{fg}b_f^2b_g^2+O_G(\|\mathbf b\|^6).}
\]
The pair sum runs over distinct rhombi with a shared *original* link. There are no other degree-four monomials by independent face-sign parity.

For coefficients \(a_0\le a_e\le a_*\) and \(0\le b_f\le b_0\), \(|C_{fg}|\le a_*^3/(8424a_0^6)\). The verified source incidence bound at most two faces per original edge implies at most four overlap neighbors per face and at most \(2F\) unordered overlapping face pairs. Hence the absolute *linked degree-four contribution per face* is bounded by \(a_*^3b_0^4/(4212a_0^6)\). This does **not** prove a uniform Taylor radius or a spectral gap.

## Independent checks and rigorous limitations

Reconstructed original-label source replay exactly matches the eight PF-I11 vertex/edge/face inventories and independently free-peels all faces; three distinct \(\mathbb F_2\) face-sign patterns per size satisfy the full incidence equations. A separate SymPy checker proves the exact quartic coefficient and its strict sign; independent SU(2) one-rhombus character-Jacobi diagonalization verifies the one-face quartic coefficient at four nonzero couplings. Both checkers passed and are archived.

**OPEN:** all-orders quantum connected-history convergence, uniform interacting Poincaré inequality, source-selected kinetic/physical time, continuum and OS reconstruction, physical four-dimensional Yang–Mills mass gap. Canonical main, historical datasets, and Observatory certification remain unchanged.