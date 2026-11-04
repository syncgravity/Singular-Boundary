# Two self-contained coefficientwise PW Poisson gates: one face and adjacent physical faces

**2026-11-04 · exact all-spin finite original-link SU(2) results, in one gauge-reduced coordinate norm.** Full local derivation, independently executed matrix verifiers, passing logs and SHA-256 manifest: conversation file \`pw_local_multiplier_audit_2026-11-04.zip\`. This proves **neither** the unrestricted all-history Poisson bound **nor** nonlinear convergence / a Yang–Mills mass gap.

## Setup and precise coordinate convention

On a finite original-link simply connected straight SU(2) square row, use independent face holonomies and the **corrected** physical operator
\[
K=4\sum_i C_i+2\sum_iD_{i,i+1},\quad D_{i,i+1}=\sum_{a=1}^3R_i^aL_{i+1}^a,\quad E_n=n(n+2).
\]
Degree n is spin n/2. The face trace-expansion projective norm is \(P_\sigma(f)=\sum_{\bf n}d_{\bf n}e^{\sigma\sum n_i}\|A_{\bf n}\|_{S_1}\), \(d_{\bf n}=\prod_i(n_i+1)\). The history-weighted \(L^{(r)}_{\kappa,\sigma}\) has \(1+\max n_i\) to the power r *inside* the anchored sum and \(e^{\kappa |I|}\) for history I. Work with \(\sigma\ge0,\kappa>0,r\in\mathbb Z_{\ge0}\). Set \(\Gamma_K(f,g)=(fKg+gKf-K(fg))/2\), \(\mathcal B=K^{-1}Q\Gamma_K\) where Q deletes **only the global constant**. Matrices are arbitrary in the stated sectors; physical observables form a gauge-invariant subspace.

## A. Same-face nonlinearity: sharp CG scalar envelope 2/3

**Theorem:** If F and G depend only on the **same one face**, then
\[
\boxed{P_\sigma(\mathcal B(F,G))\le\tfrac23P_\sigma(F)P_\sigma(G).}
\]
The same constant holds with any nonnegative integer max-spin moment r, and the singleton-history factor is exactly \(e^{-\kappa}\).

**Exact derivation.** K restricts to the one-face \(4C\); cross-link derivatives vanish on functions independent of neighboring faces. On input degrees m,n≥1 and allowed SU(2) CG output \(l=|m-n|,|m-n|+2,\dots,m+n\), the Fourier coefficient product is \(H_l=C_l^\dagger(A_m\otimes B_n)C_l\), with C_l the isometric CG embedding. The l=0 constant is deleted; for l≥1 the *exact* physical Poisson response coefficient is
\[
\mathcal B_l=\frac{E_m+E_n-E_l}{2E_l}H_l,\qquad E_j=j(j+2).
\]
The weighted one-output factor is
\[
\mu_{mnl}=\frac{l+1}{(m+1)(n+1)}\frac{|E_m+E_n-E_l|}{2E_l}.
\]
Assume m≥n. The numerator \(\alpha_l=(E_m+E_n-E_l)/2\) decreases from \(n(m+2)\) at l=m−n to −mn at l=m+n, so \(|\alpha_l|\le n(m+2)\). If l≥2, \((l+1)/E_l\le3/8\) and \(n(m+2)/[(m+1)(n+1)]\le3/2\), proving \(\mu\le9/16\). If l=1, admissibility forces m=n+1 and
\[
\mu_{n+1,n,1}=\frac{2n(n+3)}{3(n+1)(n+2)}
=\tfrac23\left(1-\frac2{(n+1)(n+2)}\right)<\tfrac23.
\]
Hence **the scalar coefficientwise multiplier envelope** has sharp supremum 2/3 (approached in the high-spin l=1 channel). This is *not* a claim that the actual bilinear operator norm attains 2/3.

Unitary CG block pinching gives \(\sum_l\|H_l\|_1\le\|A_m\|_1\|B_n\|_1\). The exponential weight is submultiplicative since l≤m+n, and \((1+l)^r\le(1+m)^r(1+n)^r\). Apply the per-channel multiplier bound before summing output blocks, then sum the input sectors. The result is independent of degree and strip length.

## B. Adjacent singleton faces: genuine shared-original-link constant 1/6

**Theorem:** For F supported only on face i and G on **adjacent face i+1**, with arbitrary complex PW coefficients,
\[
\boxed{P_\sigma(\mathcal B(F,G))\le\tfrac16P_\sigma(F)P_\sigma(G)}
\]
and the same statement holds with max-spin moments r. The two history weights cancel exactly: [i] + [i+1] produces [i,i+1].

**Proof.** The two-face input product has one output degree sector (m,n), m,n≥1, without shared-face fusion. The input electric eigenvalues are E_m,E_n, and in this output sector the **physical** original-link operator is \(K=E\,\mathrm{id}+2\mathscr D\), \(E=E_m+E_n\), with
\[
\mathscr D(X)=-\sum_aJ_m^a X J_n^a
\]
on the correct two tensor factors. The exact product identity gives \(\Gamma_K(F,G)=-\mathscr D(A_m\otimes B_n)\). By Schatten row-column Cauchy,
\[
\|\mathscr D\|_{S_1\to S_1}\le S=\sqrt{E_m E_n}/4\le E/8.
\]
Therefore the Neumann inverse of the **actual original-link** K obeys
\[
\|K^{-1}\mathscr D X\|_1\le \frac{S}{E-2S}\|X\|_1\le\tfrac16\|X\|_1.
\]
Both output degrees remain nonzero, so Q is inert. The output dimension and degree weights equal the product input weights; moments are submultiplicative. Sum all input sectors. The claim is a genuine physical shared-edge estimate and does **not** silently substitute independent free rotors for K.

## C. First interaction of two arbitrary singleton-history families

Let \(F=\sum_i [i]\otimes f_i\), \(G=\sum_i[i]\otimes g_i\) with finite singleton-history families and the local-first norm. Nonzero Γ terms arise only for equal or adjacent face labels. For fixed anchor x, the equal-face contribution costs \((2/3)e^{-\kappa}\|F\|\|G\|\), and the two neighboring history intervals each contain at most two ordered contributions bounded by 1/6. Thus for every r≥0,
\[
\boxed{\|\mathcal B_{\mathrm{hist}}(F,G)\|_{L^{(r)}}
\le \tfrac23(1+e^{-\kappa})\|F\|_{L^{(r)}}\|G\|_{L^{(r)}}.}
\]
Uniform in strip length, all representation degrees, analytic radius σ and first/higher moments. **Not closed under iteration:** adjacent singletons generate length-two histories, and this result alone gives no all-history nonlinear fixed point.

## Reproduction and limits

Independent local archive:
- \`verify_single_face_multiplier.py\`: 348,350 **exact rational** SU(2) scalar channel checks through m,n=100; 160 explicit off-diagonal/dense/rank-one matrix CG blocks from 50 coefficient-matrix input pairs.
- \`verify_adjacent_original_link.py\`: 98 two-face **actual original-link** matrix-superoperator inverse/residual/nuclear-norm regressions from complex dense and rank-one coefficient matrices, m,n≤7.
- Passing logs and per-file SHA-256 hashes are included.

These finite regressions are independent implementation tests. The proofs above establish the claimed all-spin estimates. **Outstanding** is the general same-coordinate coefficientwise Poisson estimate for overlapping/nested histories of arbitrary widths, including the physical low-energy outputs and spatial anchor summation. The earlier original-link/face norm-transport obstruction remains. The archived graded tame and local Borel disk remain conditional. No interacting λ=1 spectral-gap or continuum Yang–Mills result follows.
