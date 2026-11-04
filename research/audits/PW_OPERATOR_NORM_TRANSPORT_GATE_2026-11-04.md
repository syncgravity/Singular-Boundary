# Peter–Weyl operator audit: exact norm-transport obstruction and certified face-sector estimates

**2026-11-04 | Independent exact finite original-link SU(2) audit.** No theorem of unrestricted nonlinear history closure, interacting gap or 4D continuum Yang–Mills mass gap is claimed. Full report, two runnable independent verifiers, passing logs and SHA-256 manifest: companion archive \`pw_operator_transport_audit_2026-11-04.zip\`.

## I. Exact norm non-equivalence across original links and gauge-fixed faces

For one SU(2) representation of integer degree n≥1 and dimension d=n+1, fix the **trace-expansion nuclear** norm
\[
P_\sigma(f)=\sum_{\mathbf a}d_{\mathbf a}e^{\sigma|\mathbf a|}\|A_{\mathbf a}\|_{S_1},\quad
d_{\mathbf a}=\prod_i(a_i+1).
\]
For L independent SU(2) group variables, \(W_L=\chi_n(U_1\cdots U_L)\) has a unique nonzero Fourier block in multidegree \((n,\ldots,n)\). Its coefficient matrix is a cyclic permutation on \((\mathbb C^d)^{\otimes L}\), hence has exactly \(d^L\) singular values equal to one. Thus **exactly**
\[
\boxed{P_\sigma(W_L)=d^{2L}e^{\sigma n L}.}
\]
For the outer Wilson rectangle of N straight open plaquettes, its boundary has \(L_{\rm link}=2N+2\) **original physical links**, whereas the same gauge-invariant observable in the independent face-holonomy realization is a product of \(L_{\rm face}=N\) face matrices (up to orientation inversions/conjugations that preserve the coefficient singular values). Consequently
\[
\boxed{\frac{P_{\sigma,\rm original}(W_N)}{P_{\sigma,\rm face}(W_N)}
=d^{\,2N+4}e^{\sigma n(N+2)}.}
\]
At σ=0 and n=1, the ratio is \(4^{N+2}\): the two prescribed PW projective norms are **not uniformly equivalent in volume**. Importing an original-link projective inequality into a face-coordinate local-first Banach space by identifying the norms is an invalid inference without a separately proved norm-transport or renormalization theorem. This says nothing against valid direct estimates in either representation.

## II. Certified coefficientwise results **within one fixed coordinate system**

**Multiplication algebra.** In one declared tensor-product PW representation, \(f=\mathrm{Tr}(A\pi_{\mathbf a})\) and \(g=\mathrm{Tr}(B\pi_{\mathbf b})\). Reorder their tensor indices, apply unitary linkwise Clebsch–Gordan decomposition on shared variables, then pinch onto individual output degree blocks. Block pinching is Schatten-1 contractive:
\[
\sum_{\mathbf c}\|P_{\mathbf c}U(A\otimes B)U^*P_{\mathbf c}\|_1
\le\|A\otimes B\|_1=\|A\|_1\|B\|_1.
\]
Output dimensions satisfy \(d_{\mathbf c}\le d_{\mathbf a}d_{\mathbf b}\) and degree \(|\mathbf c|\le|\mathbf a|+|\mathbf b|\). Therefore for all σ≥0,
\[
\boxed{P_\sigma(fg)\le P_\sigma(f)P_\sigma(g).}
\]
The proof covers arbitrary complex/off-diagonal coefficient matrices, not just central characters. It applies **separately** in original-link and independent-face coordinates; it does not equate their norms.

**Original-link gradient in face coordinates.** Every original-link vector field affects at most two incident face holonomies in the corrected open-strip realization. On a fixed face multidegree \(\mathbf a\), a single face derivative acts by a spin-\(a_i/2\) generator with nuclear multiplier norm at most \(a_i/2\). Let \(w_e(\mathbf a)=\sum_{i:\text{face }i\text{ incident to }e}a_i\). For a fixed-sector input,
\(\|X_{e,j}f_{\mathbf a}\|_{P_\sigma}\le w_e(\mathbf a)\|f_{\mathbf a}\|_{P_\sigma}/2\).
Using three SU(2) directions and multiplication algebra,
\[
\boxed{P_\sigma(\Gamma_K(f_{\mathbf a},g_{\mathbf b}))
\le\frac34\sum_{e\in E(f)\cap E(g)}
 a_e w_e(\mathbf a)w_e(\mathbf b)
 P_\sigma(f_{\mathbf a})P_\sigma(g_{\mathbf b}).}
\]
This is a **source** estimate, not yet an energy-normalized local Poisson theorem.

**Free inverse in face coordinates.** On a nonconstant fixed face-degree sector \(\mathbf a\), put \(c_i=a_i(a_i+2)\), \(D=\sum_ic_i\ge3\). For the corrected original-link electric generator
\[
K_{\mathbf a}=D\,\mathrm{id}+2\sum_{i=1}^{N-1}\mathscr D_{i,i+1},
\quad \|\mathscr D_{i,i+1}\|_{S_1\to S_1}\le\sqrt{c_ic_{i+1}}/4.
\]
By AM–GM and path edge incidence, \(2\sum_i\|\mathscr D_{i,i+1}\|\le D/2\). Thus the Neumann inverse exists directly on the coefficient matrices and
\[
\boxed{\|K_{\mathbf a}^{-1}X\|_1\le(2/D)\|X\|_1,\qquad
P_\sigma(K^{-1}Qh)\le(2/3)P_\sigma(h).}
\]
This is uniform in finite strip length. The sharp intrinsic Haar-Hilbert bound 1/3 is a **different** norm and must not be silently substituted here.

## III. What does *not* follow yet

The projective product algebra, gradient estimate, and free inverse alone do **not** yield a universal \(\|K^{-1}Q\Gamma(f,g)\|_{P_\sigma}\le C_0\,(\mathrm{link\ overlap})\|f\|_{P_\sigma}\|g\|_{P_\sigma}\) with constant independent of spins and history width. Near-singlet middle-face fusion can eliminate large input spin energy in an output block. The coefficientwise CG dimension suppression, surviving outer energy and exact history bookkeeping have to be combined in a proof **in one fixed norm convention**. Existing direct finite-sector family results are compatible with this missing general step. The recent weighted exception theorem is explicitly conditional on the local coefficientwise operator bound, so its formal Gevrey/Borel consequences remain conditional.

**Next proof gate:** certify all-output-degree weighted CG/inverse estimates on arbitrary nested histories in a single defined gauge-reduced PW Banach norm, or prove explicit transport-loss factors from original-link coefficients. Do not equate original-link and face coefficient norms. This audit does not solve physical λ=1 convergence, P0 regulator transport, OS reconstruction or a four-dimensional positive Yang–Mills mass gap.

## Verification

The companion ZIP contains two **independent** executable scripts:
- \`verify_transport.py\`: 14 cyclic-permutation Fourier nuclear/reconstruction tests using explicit noncommuting unitary matrices; 900 exact integer norm-ratio checks.
- \`verify_free_inverse.py\`: 126 random complex matrix fixed-sector three-face original-link free-inverse residual and nuclear-bound regressions, all passing.
The algebraic arguments prove the asserted statements for all integer degrees and finite strip lengths; finite checks only test implementations.