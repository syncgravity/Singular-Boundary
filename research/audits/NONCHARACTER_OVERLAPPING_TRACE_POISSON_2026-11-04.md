# Non-character overlapping Wilson traces: exact physical three-face Poisson response

**2026-11-04 | Finite exact original-link Gauss-invariant SU(2) theorem.** This record concerns two overlapping **non-factorized trace** inputs, not an arbitrary-spin or general tame estimate. The full independent polynomial verifier, report, and SHA-256 manifest are in the companion conversation ZIP \`noncharacter_overlap_audit_2026-11-04.zip\`.

## Operator and exact inputs

For three consecutive face holonomies \(A,B,C\in SU(2)\), with quaternionic left/right infinitesimal generators \(L,R\) normalized by \(i\sigma_a/2\), use the **corrected physical original-link** operator
\[
K=-4\sum_{X=A,B,C}\sum_a(L_X^a)^2+
2\sum_a(R_A^a L_B^a+R_B^aL_C^a).
\]
Take two extended-history residual-Gauss-invariant, *recoupled non-character* trace words
\[
F=\operatorname{Re}(AB)=\tfrac12\operatorname{tr}(AB)\quad [I=[1,2]],\qquad
G=\operatorname{Re}(BC)=\tfrac12\operatorname{tr}(BC)\quad [J=[2,3]].
\]
This is not a product \(\chi_1(A)\chi_1(B)\): the matrix indices are contracted across the two faces. The output history remains the **connected union** \(I\cup J=[1,3]\), with overlap-discount \(e^{-\kappa}\).

Direct quaternion differentiation confirms \(KF=9F/2\), \(KG=9G/2\). For \(T=\Gamma_K(F,G)=(FKG+GKF-K(FG))/2\), two **independent** constructions (the electric product identity and the complete original-link left/right derivative product rule) agree identically as rational polynomials in the twelve quaternion coordinates. In the directly evaluated source, there are 24 monomials.

## Exact two-eigenvalue Krylov closure

The source satisfies the literal polynomial identity
\[
\boxed{(K^2-16K+60)T=0=(K-6)(K-10)T.}
\]
Therefore the complete, centered, original-link Poisson response is given **without numerical truncation** by
\[
\boxed{\mathcal B_{\rm hist}(F,G)=K^{-1}T=(16T-KT)/60,}
\]
with \(K\mathcal B=T\) verified as a literal quaternion polynomial (28 monomials). The source projections \(T_6=(10T-KT)/4\), \(T_{10}=(KT-6T)/4\) have electric eigenvalues 6 and 10 respectively, and \(\mathcal B=T_6/6+T_{10}/10\). The entire source has degree one in both outer face variables, so no global Haar constant occurs and the centered projection \(Q\) is inert.

## Exactly retained disconnected-minimal-support physical mode

Let \(P_{B,0}\) denote Haar averaging **only over the middle face** \(B\). As \(\mathbb E[b_i b_j]=\delta_{ij}/4\) for unit quaternion coordinates, the exact projections are
\[
\boxed{P_{B,0}T=\tfrac38\operatorname{Re}(AC^{-1}),\qquad
P_{B,0}\mathcal B=\tfrac1{16}\operatorname{Re}(AC^{-1}).}
\]
Here \(K\operatorname{Re}(AC^{-1})=6\operatorname{Re}(AC^{-1})\), the \(K=10\) source channel has zero \(B\)-average, and \(\operatorname{Re}(AC^{-1})\) is **nonconstant and physical** (invariant under the simultaneous residual gauge conjugation). Although it has disconnected minimal face support on the outer two faces, it must retain the connected interaction-history label \([1,3]\). This is an exact non-character witness that discarding such output changes the physical Poisson equation.

## Verification, limitations, and next gate

The companion executable independently tests: same original-link \(K\) and signs as prior operator re-audits; \(KF=KG=9F/2\); direct versus polarization \(\Gamma\); the exact \(K\)-minimal polynomial; the complete inverse residual; 6/10 spectral projections; middle Haar marginals; and the surviving energy-6 physical output. It uses exact SymPy polynomials, not random samples. The standalone original script SHA-256 is \`377c8b701a7a3ca52431822b968fafa12391bab37d7e93dcf8c9c3bbbc67113f\`.

**No general trace-norm estimate** for arbitrary off-diagonal PW coefficient matrices, high representation degrees, arbitrary gauge intertwiners, or long histories is proved here. In particular the inherited local-first tame theorem and the Borel-disk corollary remain conditional. Next: repeat this recoupled trace-word construction in variable high-spin representations while controlling the coefficient-matrix trace norm with the **same** normalization as the character-family audits.