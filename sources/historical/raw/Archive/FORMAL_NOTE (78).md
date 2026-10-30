# Four-prism loop: certified cellular incidence and multiport Fourier obstruction

**Scope.** A constructed 2×2 quadrilateral cell patch, extruded through one temporal interval. This verifies a *combinatorially admissible* prism loop, not provenance of four tiles in the uploaded Penrose geometry. It does not prove or disprove universal insertion free-energy bounds.

## 1. Exact signed incidence

The reproducible `verify.py` builds all signed cellular boundary matrices from oriented face cycles with integer coefficients. It gives 18 vertices, 33 edges, 20 unique faces, four prism 3-cells, ranks (17,16,4), and exact products `d1@d2=0`, `d2@d3=0`. The four shared temporal faces have the incidence pattern of a cycle on four cells and **all four share the central vertical link**. The pairwise shared-edge count matrix has diagonal 4 and off-diagonal 1. The 3-cell/4-seam submatrix is included in `certificate.json`.

## 2. Why the disk–annulus–disk argument cannot be reused

Every prism in the 2×2 loop is incident on **two adjacent** shared temporal faces; those face boundaries meet at the central vertical link. The four retained faces of such a prism are not a cylinder with two disjoint boundary cycles. Therefore the three-prism-strip factorization `F(h1,h2)=fL(h1) fM(h1^-1 h2) fR(h2)` does not follow; a loop-wide product of independent two-port cylinders is not justified either. The exact effective multivariate kernel must be constructed by integrating its original link variables, maintaining their common central-edge dependence.

## 3. Explicit multiport Fourier warning

For a fundamental SU(2) representation, define the three-variable word `f(A,B,C)=χ_{1/2}(ABC)=Tr(ABC)`. A positive-definite function on the product group must satisfy `f(g^-1)=conj f(g)`. Take `A=iσ_x`, `B=iσ_y`, `C=iσ_z` (equivalently unit quaternion i,j,k with consistent sign): `Tr(ABC)=-2` while `Tr(CBA)=+2` (or the reverse depending on the chosen quaternion convention). Thus `f(A,B,C)` is *not* positive definite on `SU(2)^3`.

The corresponding fundamental coefficient tensor is a cyclic permutation `P` on `(C²)^⊗3`. Its Hermitian part `(P+P†)/2` has eigenvalues `1` (four times) and `-1/2` (four times). Hence a three-port spin-network word is not automatically PSD despite the positive character coefficients of individual Wilson weights. In fact the Wilson factor `e^{-β(1-χ(ABC)/2)}` likewise fails the necessary Hermitian symmetry in these independent variables for any β>0.

**Caution:** This is an obstruction to *inferring* multiport positive definiteness from facewise character positivity. It is **not** a proof that the fully integrated effective boundary kernel of this four-prism patch has a negative Fourier coefficient. Other Wilson terms/integrations can restore positivity. Nor does a non-PSD coefficient alone prove a lower free-energy comparison fails.

## 4. Rigorous fallback comparison

For any selected set of `q` inserted faces, with `β_p ≤ c_+ λ`, the pointwise bound `0≤V_Q(U)≤2 c_+ λ q` yields

`e^{-2c_+ λ q} Z_0 ≤ Z_1 ≤ Z_0` and `0≤F_Q≤2c_+ λ q`.

This is **support-local** and independent of ambient volume, but is `O(λq)`, not `O(q log λ)`. A uniformly logarithmic lower comparison would require a separate *averaged* control of the fully integrated multiport interface kernel, or an independent Gibbs/transport estimate. No such general estimate has been derived here.

## 5. Open tests

(1) Compute the fully integrated kernel on an explicitly chosen set of gauge-fixed independent port holonomies, and test finite-spin Fourier matrices. (2) If a negative sector appears, show its normalized contribution is dominated by the positive sector with a factor polynomial in λ per inserted face. (3) Certify actual Penrose tile vertices/edges and repeat after attaching arbitrary neighboring prisms. None is presently verified.
