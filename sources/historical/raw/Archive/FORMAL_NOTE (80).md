# Four-prism exterior contraction: exact positive-coupling center selection and spin-surface order audit

27 October 2026. Constructed 2×2 quadrilateral-prism complex, not authenticated Penrose tiling. Based on the exact saved signed incidence matrix `R3_looped_four_prism_2026_10_27/incidence.npz`.

## 1. The fully interacting exterior contraction

There are 33 links, 20 faces, four deleted temporal interface faces Q=(3,4,10,13), and 16 retained Wilson face factors. For positive couplings beta_p and interface-cycle holonomies h_i(U), define the *complete* four-port Peter–Weyl coefficient, with all link integrations performed:

    M_{j_1,...,j_4}(beta) = ∫_{SU(2)^33} [∏_{p∈P0} exp(-beta_p (1 - (1/2) Tr W_p(U)))] [⊗_{i=1}^4 D_{j_i}(h_i(U))^*] dU.

Gauge-fixing any interface spanning tree yields the corresponding 20-noninterface-link expression after handling gauge redundancy. This matrix is not the frozen-exterior Haar-projector calculation. All 16 positive-coupling retained face interactions are present in this definition.

This memorandum computes *exactly zero* blocks and character-expansion lower orders of the nonzero-eligible blocks; it does not evaluate their full numerical matrix entries.

## 2. Center-parity selection (exact at arbitrary positive beta)

SU(2) Wilson face weights have an absolutely convergent character series indexed by spins j=0,1/2,1,... with character factor chi_j(W_p), with coefficients nonnegative. For every edge e, changing U_e to -U_e preserves Haar measure. Under this change, a factor D_j(W_p) acquires sign (-1)^{2j} for each incidence of e in face p. A port spin-s test factor likewise acquires sign (-1)^{2s} per incidence of e in its holonomy. Hence each term of the character-expanded integral vanishes unless the vector of half-integer face spins x∈GF(2)^16 obeys the exact signed-incidence parity equation

    (abs(B2[:,retained]) mod 2) x = (abs(B2[:,Q]) mod 2) y   (mod 2),

where y∈GF(2)^4 selects the fundamental spin-1/2 representations on the four ports (trivial representations on other ports).

These conditions do not assume scalar or matrix positive definiteness. They apply to the fully integrated, positively coupled Wilson action, irrespective of the size of the beta_p.

Exact enumeration of all 2^16 possible x yields:

- y containing an odd number of fundamental ports: **no solution**. All eight such Fourier blocks are identically zero for all beta_p≥0.
- adjacent-port pairs (port bit patterns 0011, 0101, 1010, 1100): minimum four half-integer retained faces, unique mod-2 minimal surface.
- opposite-port pairs (0110, 1001): minimum eight half-integer retained faces, two minimal mod-2 surfaces.
- all four fundamental ports (1111): minimum eight half-integer retained faces, two minimal mod-2 surfaces.

The matrix at the all-trivial sector is the positive partition function Z0.

## 3. Small positive coupling consequences

For Wilson coefficients near beta=0, a face of half-integer representation j contributes at least one power of beta because its lowest permitted representation is j=1/2. Therefore with a common small coupling beta for the 16 retained faces, the full four-fundamental-port Fourier matrix satisfies, entrywise and in operator norm on its fixed 16-dimensional space,

    || M_{1/2,1/2,1/2,1/2}(beta) || = O(beta^8) as beta ↓ 0.

The adjacent pair blocks are O(beta^4), and opposite pair blocks O(beta^8). These are *upper orders* (the actual leading coefficients can cancel) not positivity or nonvanishing assertions. The all-trivial normalization is Z0=1+O(beta) as beta→0. For unequal beta_p the corresponding statement is a sum over representation surfaces, each monomial supported on ≥4 or ≥8 half-integer-face factors.

## 4. What remains unsettled

The four-fundamental Fourier block at arbitrary positive beta is an explicit 16×16 matrix integral, and its matrix entries require a full spin-network tensor contraction or controlled SU(2) quadrature. Its nonnegative eigenvalues are **not established**. In particular, nonnegative character expansion coefficients of *individual* plaquettes and conditional 4-port Haar projectors cannot be used to claim positivity after the exterior contraction. Likewise the vanishing of odd-port blocks and suppression O(beta^8) at small beta do not control the large-beta, weak-coupling regime needed for R3.

No support-local positive-coupling lower comparison is derived for simultaneous insertion of the four interfaces. R3 and continuum mass gap remain open.

## 5. Reproducibility

`verify.py`: exact GF(2) enumeration of the 16 retained-face representations using saved oriented incidence matrix, verifies the chain identities and constructs the 16 entry selection report. `selection_certificate.json`: complete enumeration of selected port patterns, minimal odd-spin face supports and their multiplicities. No Monte Carlo, finite-spin numerical extrapolation, or positivity claim is made.
