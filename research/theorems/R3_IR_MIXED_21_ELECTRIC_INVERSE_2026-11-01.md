# R3 — Exact mixed-degree SU(2) electric inverse (2,1) sector

Date: 2026-11-01. Model: finite original-link straight open chain SU(2) of two plaquettes, positive kinetic electric operator. This calculation adds a mixed representation sector to the prior fundamental multilinear (1,1) audit.

## Construction

Take the nine-dimensional space of traceless quadratic harmonic polynomials in four real quaternion coordinates on face A, with basis: six off-diagonal monomials x_i x_j (i<j) plus x_0²−x_1², x_1²−x_2², x_2²−x_3². These are linearly independent modulo the SU(2) unit-sphere relation. On face B take four coordinate functions y_0,...,y_3. The 36 basis products represent the (degree 2, degree 1) Peter–Weyl sector. For this convention, the single-face electric eigenvalues are 8 and 3. The original-link interaction is +2Σ_{k=1}³ R_A^k L_B^k, with quaternion generators e_k/2 as in the earlier physically reconciled audit, and the full matrix is K=11I_36+2Σ R_A^k⊗L_B^k.

All generators are assembled by differentiating the exact degree-two polynomials and solving rational linear equations back in the nine-dimensional harmonic basis; the fundamental generators are taken from the previous exact multilinear verifier.

## Exact results

- The matrix is 36×36 with rational entries.
- Spectrum: eigenvalue 9 of multiplicity 12 and 12 of multiplicity 24.
- The inverse exists and its largest absolute column sum in the **specified polynomial coefficient basis** is exactly 4/27.
- For comparison, the earlier (1,1) fundamental sector inverse coefficient norm was 2/9 (in its own basis). These norms are not canonical representation-invariant numbers.

## Scope and limits

This certifies one new mixed-degree sector and its inverse at equal coefficient analytic radius (all polynomials have homogeneous total degree three). It does not establish any degree-uniform or interval-uniform inverse bound; it does not show that the coordinate coefficient norm descends to an intrinsic analytic norm without choosing harmonic representatives. The verification does not reach balanced mixed sectors (2,2) or higher spins, and does not prove convergence of the connected score, an interacting λ=1 spectral gap, or a continuum Yang–Mills mass gap.

Run `python verify.py` with SymPy for exact reconstruction, spectrum, inverse norm and K K^{-1}=I.