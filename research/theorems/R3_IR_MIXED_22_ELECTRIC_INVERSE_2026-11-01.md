# Exact balanced (2,2) electric inverse — original-link SU(2) pair

Date: 2026-11-01. Model: two adjacent faces in the finite open original-link SU(2) plaquette chain, with shared-link convention `K = 16 I + 2 Σ_a R_2^a ⊗ L_2^a`.

## Construction

Each degree-two harmonic sector on SU(2) is nine-dimensional. The explicit rational polynomial basis is the six off-diagonal quadratic monomials `x_i x_j` for `i<j`, together with `x_0²−x_1²`, `x_1²−x_2²`, `x_2²−x_3²`. The 9x9 left and right generator matrices are reconstructed by symbolic differentiation with imaginary quaternion generators `e_a/2`. Their Kronecker products give the 81x81 rational electric matrix. This is precisely the harmonic-basis convention used for the earlier (2,1) calculation.

## Exact verified results

- Sector dimension: 81.
- Electric spectrum: 12 (multiplicity 9), 14 (multiplicity 27), 18 (multiplicity 45).
- Inverse coefficient induced 1-norm, largest absolute column sum: **137/756 ≈ 0.1812169312**.
- Smallest absolute inverse column sum: 125/1512.
- Number of nonzero inverse matrix entries: 1,363.
- Exact matrix identity: K K^{-1} = I_81.

The result is basis-specific, not an intrinsic Peter–Weyl inverse norm. In particular, the previous (2,1) value 4/27 ≈ 0.14815 is smaller than the (2,2) coefficient norm, so the apparent decreasing pattern of the earlier sectors fails.

## Scope of the result

All basis polynomials are homogeneous of total degree four, so fixed analytic weights `exp(σ degree)` do not change this matrix's induced inverse norm. The result verifies a *finite sector* only. It does **not** prove a degree-uniform bound, a support-uniform analytic inverse, ordinary perturbative convergence, a λ=1 interacting spectral gap, the Penrose current estimate or the continuum Yang–Mills mass gap.

Run `python verify.py` with SymPy; calculations are exact rationals.