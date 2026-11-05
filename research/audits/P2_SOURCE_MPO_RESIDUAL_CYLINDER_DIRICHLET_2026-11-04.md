# P2 — Source-adapted five-state corrected SU(2) electric MPO and smooth gauge-invariant cylinder-field positive-energy Dirichlet identity

**Private mathematical audit, 2026-11-04.** Restricted corrected original-link SU(2) open straight strip, genuine Gauss-twirled Poisson source and first-moment independent-face Peter–Weyl nuclear response. Expanded report with detailed proofs, six independently executed verification scripts, outputs, SHA-256 manifest and integrity-verified ZIP preserved under **Library → The Singular Boundary → Proof Audits**, as \`P2_SOURCE_ADAPTED_MPO_CERTIFICATES_AND_CYLINDER_DIRICHLET_2026-11-04.md\` and \`p2_mpo_cylinder_2026-11-04.zip\`. The **full** N≈m² nuclear response, invariant all-time infinite-volume dynamics, a positive interacting gap, signed positive-axis Borel reconstruction and 4D continuum Yang–Mills mass gap remain **OPEN**.

## P-77 — Genuine Poisson collar admits an exact five-state electric MPO and a posteriori nuclear enclosure

P-73/P-75 gives for every site j and physical output l=m±1 the **actual untwirled corrected original-link q=0 Poisson source**
\[
Z=\sum_{r=1}^{r_0}c_r\bigotimes_{i=1}^N|u_{i,r}\rangle\langle v_{i,r}|,\qquad r_0\le13(m+1),
\]
with true Gauss-invariant source Y=\(\mathcal T Z\), global simultaneous SU(2) conjugation Haar expectation. Actual electric coefficient map is K=DI+H, \(D=3(N-1)+l(l+2)\), \(H(X)=-2\sum_{i=1}^{N-1}\sum_{a=1}^3J_i^a XJ_{i+1}^a\). Let \(T=-H/D\).

**Exact MPO automaton (bond ≤5):** virtual states idle, pending-x, pending-y, pending-z, done; at every site idle→idle and done→done act as identity; idle→pending-a acts by left multiplication \((2/D)J_i^a\); pending-a→done acts by right multiplication \(J_i^a\). With idle left and done right boundary conditions this selects exactly one **adjacent** bond, and reproduces the actual corrected T as a local Liouville-space MPO. The genuine physical source Z is an operator-valued matrix-product state (MPS) of bond ≤r0. Powers T^p Z have exact MPS bond ≤r0 5^p; direct-summing p=0,…,q gives the genuine **untwirled corrected** q-Neumann approximation \(Z^{[q]}=D^{-1}\sum_{p=0}^qT^pZ\) with
\[
\boxed{r_q\le r_0\sum_{p=0}^q5^p=r_0(5^{q+1}-1)/4.}
\]
The P-75 fixed-absolute-error sufficient q=O(log(m/epsilon)) along even N=m²+O(1) implies an **explicit polynomial (though potentially enormous) operator-MPS bond bound** \(O(m(m/\epsilon)^\kappa)\), \(\kappa=\log5/\log(8/3)\approx1.640895\). The **exact positive** P-75 Hopf Haar cubature has G=(S+1)(2S+1)² nodes, total twice-spin S=N−1+l. Each product-unitary group conjugation preserves MPS bond and the sum increases the bound by at most G:
\[
\boxed{r_{\mathrm{phys},q}\le G\cdot13(m+1)(5^{q+1}-1)/4.}
\]
Thus the *genuine physical inverse* has a **polynomial-bond ε-nuclear approximation in the specified balanced high-spin family**. This is an **existence and representation-size theorem**, NOT an efficient method for obtaining its trace norm, a bit-complexity guarantee, actual N≈m² asymptotics or a proof of uniform same-grade closure.

**Computable independent two-sided a posteriori enclosure.** For any untwirled candidate operator MPS Z_* with local tensor matrices \(A_i^{\alpha\beta}\), form positive scalar transfer matrices \(W_i^{\alpha\beta}=\|A_i^{\alpha\beta}\|_{S_1}\) and \(\Pi(Z_*)=e_L^\top W_1\cdots W_Ne_R\). Virtual-path expansion gives \(\|\mathcal T(Z_*)\|_1\le\|Z_*\|_1\le\Pi(Z_*)\), with all local computations polynomial in the **represented bond**. Let \(\mathcal R=Z-KZ_*\). Since K commutes with global Haar twirl, P-67's **induced S1** inverse estimate gives the a posteriori, no-exponential-Fourier residual bound
\[
\boxed{\|K^{-1}Y-\mathcal T(Z_*)\|_1\le e_*:=\Pi(\mathcal R)/[D(1-\eta)].}
\]
The gauge-twirled **Hilbert–Schmidt** lower witness is an exact local **double-layer tensor transfer**, by P-75's positive finite Haar quadrature:
\[
h_*^2=\|\mathcal T(Z_*)\|_2^2
=\operatorname{tr}[Z_*^\dagger\mathcal T(Z_*)]
=\sum_gw_g\,\operatorname{tr}[Z_*^\dagger D(g)Z_*D(g)^\dagger].
\]
Therefore the *actual complete physical* nuclear inverse has an explicit two-sided a posteriori enclosure:
\[
\boxed{\max(0,h_*-e_*)\le\|K^{-1}Y\|_1\le\Pi(Z_*)+e_*.}
\]
**A narrow interval is NOT guaranteed** as q grows: source norm transfer and HS lower may have large slack and MPO bond/precision can be impractical. This is a meaningful a posteriori enclosure, not an efficient relative-error Schatten algorithm.

**Executed tests in expanded archive:** exact five-state MPO action versus independent product rank-one electric expansion and dense corrected K test oracle for genuine N=2,m=3 (both outputs), N=4,m=3 (both), and N=4,m=4 (one output). True Gauss-invariant N=2,m=3 full-inverse nuclear errors lie below MPO product-projective residual certificate at q=0,1,2 for both outputs. At q=0 the computed (ordinary precision) l=2 interval [0.016541127,0.599238126] contains actual S1=0.408950617, and l=4 interval [0,0.559566467] contains S1=0.223419540. The local Haar positive group-transfer HS exactly reproduces independent dense twirled HS values 0.139175553567226 (l=2, 196 nodes) and 0.0732008717631570 (l=4, 726 nodes). Individual **genuine** untwirled source a posteriori residual q-certificates were also evaluated at first joint widths N=10,m=3 (q=0,1; endpoint and interior, both outputs), and N=16,m=4 (q=0; both). No full N≈m² trace norm is claimed. Naive source term list already reaches 37,908 at N=10 interior q=1, illustrating why the MPO compression matters.

## P-78 — Smooth gauge-invariant local multiplication observables have uniform excitation-energy Dirichlet forms

For genuine finite-strip corrected original-link Hamiltonian H_N=K_N+lambda V_N, finite unique positive ground vector psi_N (P-49), and h_N=H_N−E_N≥0, the kinetic operator has the exact **positive sum-of-squares decomposition**
\[
\boxed{K_N=2\sum_i C_i+\sum_{i=1}^{N-1}\sum_a(R_i^a+L_{i+1}^a)^2+C_1+C_N}
\]
with \(C_i=\sum_a(R_i^a)^2=\sum_a(L_i^a)^2\). Let f,g be smooth finite-support cylinder **multiplication** functions invariant under simultaneous global SU(2) conjugation, so they preserve residual Gauss symmetry. The bounded magnetic potential commutes with f,g. The positive ground-state transform for the kinetic sum of squares gives
\[
\boxed{\langle f\psi_N,(H_N-E_N)g\psi_N\rangle
=\int\Gamma_N(f,g)|\psi_N|^2d\mathrm{Haar}^N,}
\]
where the explicit local sesquilinear carré du champ is
\[
\Gamma_N(f,g)=2\sum_{i,a}\overline{R_i^a f}R_i^a g
+\sum_{i<N,a}\overline{(R_i^a+L_{i+1}^a)f}(R_i^a+L_{i+1}^a)g
+\sum_a(\overline{R_1^a f}R_1^a g+\overline{L_N^a f}L_N^a g).
\]
For a fixed local support W away from endpoints, \(\Gamma_N(f,g)\) is bounded and independent of N; the **first excitation energy is uniformly bounded without any N-dependent global graph estimate**. The commutator \([H_N,M_f]\) is a local first-order differential operator with bounded coefficients (from smooth first/second derivatives of f), supported in W and the adjacent collar W⁺. Thus
\[
\|[H_N,M_f]\psi_N\|^2\le C_f[1+\sum_{i\in W^+}\langle\psi_N,C_i\psi_N\rangle].
\]
After P-55/P-64 uniform anchor translation averages, the local kinetic-energy bound makes **second excitation-frequency moments** uniform in N. Tight subsequences can be aligned with the P-55 locally normal quantum state and P-53 diagonal translation-invariant probability measure nu_inf. Uniform second moments give uniform integrability of the first moments; the finite ground-state transform and local convergence prove
\[
\boxed{\int_0^\infty E\,d\mu_\infty^{f,g}(E)=\nu_\infty[\Gamma(f,g)],\qquad
(C_\infty^{f,g})'(0)=-i\nu_\infty[\Gamma(f,g)].}
\]
This **extends P-66** to gauge-invariant smooth local multiplication observables, whose actual Hamiltonian commutator may be UNBOUNDED in operator norm but is locally controlled on finite-energy ground-state vectors.

For the specific **gauge-invariant fundamental character** \(f(U_0)=\chi_1(U_0)\), the one-face SU(2) S³ gradient identity and corrected electric coefficients give \(\Gamma(f,f)=4-\chi_1^2\) for all strip widths:
\[
\boxed{\int E\,d\mu_\infty^{\chi_1,\chi_1}=4-\nu_\infty[\chi_1^2]\in(0,4].}
\]
Strict positivity uses P-53 locally Haar-absolutely-continuous diagonal windows and |chi_1|<2 except the Haar-null center {±I}. **Nonzero first moment is not a positive spectral gap.** At lambda=0 the one-face excitation is a frequency-3 atom, matching K_1 chi_1=3 chi_1. Independent actual Gauss-invariant one-face SU2 Jacobi regression at lambda=0,.25,1,2,4,10 and Fourier cutoffs 12,24,48,96 reproduces the Dirichlet identity, excitation first/second moments and the correlation Hölder bound.

**Remaining gates:** P-77's polynomial representation and a posteriori interval do not prove practical compressed high-width nuclear approximation or determine the actual N≈m² physical response asymptotic. P-78's positive-energy temporal cylinder-field kernel and local Dirichlet form are **NOT** a common all-time interacting infinite-volume automorphism, unique vacuum or positive gap. Signed Borel, OS reconstruction, 4D continuum Yang–Mills existence and mass gap: **OPEN**.