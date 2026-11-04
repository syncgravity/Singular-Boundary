# Four independent PW degrees across two extended histories: fixed-three-face first-moment theorem

**2026-11-04 — exact finite original-link Gauss-invariant SU(2) three-face theorem.** The full expanded mathematical report and independently executed verifiers with SHA-256 manifest are in the companion conversation archive \`four_degree_matrix_audit_2026-11-04.zip\`. This is **not** arbitrary spatial-history width, general polymer-algebra closure, physical λ=1 convergence, or a 4D Yang–Mills mass-gap theorem.

## Theorem and correct physical scope

On the finite *open straight* three-plaquette SU(2) face-holonomy system A,B,C, use the corrected original-link generator

\[
K_3=4(C_A+C_B+C_C)+2D_{12}+2D_{23},\qquad
D_{12}=\sum_a R_A^a L_B^a,\qquad D_{23}=\sum_a R_B^aL_C^a.
\]

PW degree j corresponds to spin j/2. Let p,q,r,s≥1 be **four independently variable integers**. Let F and G have arbitrary complex trace-expansion Fourier coefficient matrices (not required to be Wilson characters) in degrees (p,q,0), (0,r,s), respectively; for physical observables restrict to the residual Gauss-invariant subspaces. Their connected histories are [1,2] and [2,3], and the **entire output** retains the union history [1,3], including low-energy sectors with zero middle spin.

The trace-expansion PW norm uses f=Tr(A_n π_n), dimensions d_n=Π_e(n_e+1), weights d_n exp(σΣ_e n_e)||A_n||_(S1), and local-first L^(1) additionally uses 1+max_e n_e **inside** the anchored sector sum, with connected-history factor exp(κ|I|), σ≥0, κ>0.

**Theorem (unrestricted four degrees, restricted three-face history configuration):**

\[
\boxed{\|\mathcal B_{\rm hist}(F,G)\|_{L^{(1)}}\le
6e^{-\kappa}\|F\|_{L^{(1)}}\|G\|_{L^{(1)}},\qquad
\mathcal B_{\rm hist}=K_3^{-1}Q\Gamma_K.}
\]

The constant 6 is conservative but **does not depend on any of p,q,r,s**. In particular the potentially dangerous q=r≫p,s fusion with middle-output degree ℓ=0 is retained and controlled. **This is not a general L^(1)×L^(1)→L^(1) boundedness claim for arbitrary long histories.**

## Direct original-link Schatten proof

Write P=p(p+2), Q0=q(q+2), R0=r(r+2), T=s(s+2). The middle-face Clebsch–Gordan outputs have ℓ=|q−r|,|q−r|+2,...,q+r. Define L=ℓ(ℓ+2), c=P+L+T≥6. In the (p,ℓ,s) block the physical operator is c id+2𝒟12+2𝒟23 on actual trace-expansion coefficient matrices, where the superoperators are

\[
\mathscr D_{12}(X)=-\sum_a J_p^a X J_\ell^a,\qquad
\mathscr D_{23}(X)=-\sum_a J_\ell^a X J_s^a
\]

(with correct tensor factors). They commute as superoperators, but their **ordinary matrix images need not commute**. Schatten row/column Cauchy gives

\[
\|\mathscr D_{12}\|_{S_1\to S_1}\le\sqrt{PL}/4,\quad
\|\mathscr D_{23}\|_{S_1\to S_1}\le\sqrt{TL}/4.
\]

With S0=(√(PL)+√(TL))/4≤c/4, the **actual** matrix-superoperator Neumann inverse has
\[
\|K_{3,\ell}^{-1}\|_{S_1\to S_1}\le(c-2S0)^{-1}\le 2/c.
\tag{1}
\]
The two-face input operators obey
\[
\|K_2F\|_{P_\sigma}\le(P+Q0+\sqrt{P Q0}/2)\|F\|_{P_\sigma}
\le\tfrac54(P+Q0)\|F\|_{P_\sigma},
\tag{2}
\]
and similarly \(\|K_2G\|_{P_\sigma}\le\tfrac54(R0+T)\|G\|_{P_\sigma}\).

**Coefficientwise CG product algebra, with no sector-count factor.** The product of trace-expansion coefficient matrices is an index-reordered tensor product, conjugated by the unitary SU(2) CG decomposition in the middle face, then block-pinched. Schatten-1 contractivity of block pinching gives \(\sum_\ell\|A_\ell\|_1\le\|A_F\|_1\|A_G\|_1\). Each output dimension \(d_{p,\ell,s}\le d_{p,q}d_{r,s}\), and ℓ≤q+r ensures exponential weight contraction. Hence \(P_\sigma(FG)\le P_\sigma(F)P_\sigma(G)\), including arbitrary off-diagonal complex matrices; the same holds for (K2F)G and F(K2G). This is an explicit fixed-interface justification, not an appeal to an unverified all-history tame bound.

All output sectors have p,s≥1, so full Haar centering Q is the identity. From the exact polarization equation
\[
\mathcal B(F,G)=\tfrac12\left\{K_3^{-1}[(K_2F)G+F(K_2G)]-FG\right\},
\]
equations (1)–(2) give the **per-output** projective multiplier
\[
\frac12+\frac54\,\frac{P+Q0+R0+T}{c}.
\tag{3}
\]

## Exact all-degree first-moment control

Set A0=1+max(p,q), B0=1+max(r,s), W=1+max(p,ℓ,s), x=√c≥√6. The relative history weight is e^(3κ)/e^(4κ)=e^(−κ). For each output ℓ, the moment-and-inverse multiplier apart from that history factor is

\[
E_{pqrs\ell}=\frac{W}{A0B0}
\left[\frac12+\frac54\frac{P+Q0+R0+T}{c}\right].
\tag{4}
\]

To bound it **for all degrees**:

1. Since c≥p²+ℓ²+s² and c≥6, we have W≤1+x.
2. ℓ≤q+r implies W≤A0+B0, hence W/(A0B0)≤1/A0+1/B0≤1.
3. Thus W(P+T)/(A0B0c)≤1 because P+T≤c.
4. CG admissibility implies q≤r+ℓ and r≤q+ℓ. As Q0=q(q+2), q≤A0 and r≤B0−1,
\[
\frac{Q0}{A0B0}\le\frac{q+2}{B0}\le1+\frac{\ell+1}{B0}\le\frac{3+x}{2}.
\]
Symmetrically \(R0/(A0B0)\le(3+x)/2\). Therefore
\[
\frac W{A0B0}\frac{Q0+R0}{c}
\le\frac{(1+x)(3+x)}{x^2}=1+\frac4x+\frac3{x^2}.
\]
Combining the outer and middle energy terms,
\[
E_{pqrs\ell}\le\frac12+\frac54
\left(2+\frac4{\sqrt6}+\frac36\right)
=\frac{29}{8}+\frac5{\sqrt6}<6.
\tag{5}
\]

The scalar bound (5) is applied to each **actual** CG output coefficient; their *sum of nuclear norms* is already contractive under pinching. One does not count output channels a second time. Equation (5) and the history ratio prove the theorem. The ℓ=0 low-energy physical output is retained.

## Independent tests and honest status

The full companion ZIP contains an exact-rational sweep of **448,512** admissible output channels with degrees 1..16 (maximum tested envelope 3/2 at p=q=r=s=1, ℓ=0) and **12 actual complex PW matrix** cases using both dense and rank-one *non-character/off-diagonal* coefficients, explicit CG matrices, the corrected original-link physical Fourier source and inverse, nuclear norms, and residual checks. All passed. An initial regression mistakenly used √6>2 at the final scalar comparison; that was too weak, and was replaced by the valid exact √6>12/5. The entire suite was rerun. The finite sweep is not the proof of the unrestricted degree quantifiers; the inequalities above are.

**Next mathematical gate: unrestricted history width and overlap combinatorics.** This is fixed three faces and one overlap, so it does not control the count of long-history nesting placements, exceptional low-energy outputs with other global degrees, or the local anchor supremum after summing arbitrary histories. It does not establish source-generated score convergence, Borel continuation, a certified 3D Penrose regulator or the 4D physical mass gap.

Related input: [prior matched-sector result](VARIABLE_HIGH_SPIN_RECOUPLED_MATRIX_SECTORS_2026-11-04.md).