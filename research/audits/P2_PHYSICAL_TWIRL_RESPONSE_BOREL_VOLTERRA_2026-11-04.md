# Physical Gauss-invariant intertwined Poisson response and Borel-plane Volterra equation
**Research audit, 2026-11-04.** Corrected original-link SU(2) operator on finite open straight-square strips; a single **face-coordinate trace-expansion PW nuclear norm** throughout. Expanded report, four independently executed scripts, logs, checksums, and archive integrity: conversation artifact \`p2_physical_twirl_borel_audit_2026-11-04.zip\`.

## Physical test inputs and outputs
For even N, the alternating rank-one coefficient \(|+,-,+,-,\ldots\rangle\langle-,+,-,+,\ldots|\) has an SU(2) residual-gauge twirl \(F_N\) satisfying \(\|A_{F_N}\|_{S_1}=1\), as proved in P-26. It is *gauge-invariant* under simultaneous conjugation. Here we test the true physical Poisson operation
\[
K=4\sum_i C_i+2\sum_{i,a}R_i^aL_{i+1}^a,\qquad \mathcal B=K^{-1}Q\Gamma_K,
\]
against **separately gauge-invariant** \(G_{j,m}=\chi_m(U_j)\) and \(H_{j,m}=\chi_m(U_jU_{j+1})\), with global Haar-constant centering Q only. The second input has a genuine non-factorized swap matrix coefficient; \(\chi_m(U_jU_{j+1})\) is an electric eigenfunction of energy \(\frac32m(m+2)\).

Using the fixed-coordinate SU(2) CG nuclear algebra, original-link face-gradient source estimate
\[
P_\sigma(\Gamma(f_\mathbf a,g_\mathbf b))
\le\frac34\sum_e w_e(\mathbf a)w_e(\mathbf b)P_\sigma(f_\mathbf a)P_\sigma(g_\mathbf b),
\quad w_e(\mathbf a)=\sum_{i\text{ incident to }e}a_i,
\]
and actual electric Fourier inverse \(\|K_\mathbf c^{-1}\|_{1\to1}\le2/\sum_ic_i(c_i+2)\), derive **for each single insertion** at any even outer width, \(m\ge2\) and all nonnegative max-spin moment grades r:
\[
\boxed{\frac{P^{(r)}_\sigma(\mathcal B(F_N,G_{j,m}))}
{P^{(r)}_\sigma(F_N)P^{(r)}_\sigma(G_{j,m})}\le\frac{9m}{m^2-1}.}\tag{1}
\]
A singleton's four edges have outer fundamental incidence sum at most 6, giving source bound \(\frac92m\); the fused output retains degree at least \(m-1\) on the inner face and hence inverse ≤\(2/(m^2-1)\). For two adjacent inner faces, their link incidence sum is at most 8m and every outer link has degree weight at most 2, so the source bound is \(12m\). Fusion retains degree ≥\(m-1\) on **both** inner faces; the inverse is ≤\(1/(m^2-1)\). Thus
\[
\boxed{\frac{P^{(r)}_\sigma(\mathcal B(F_N,H_{j,m}))}
{P^{(r)}_\sigma(F_N)P^{(r)}_\sigma(H_{j,m})}\le\frac{12m}{m^2-1}.}\tag{2}
\]
CG dimension, analytic and max-spin weights are submultiplicative. Histories add \(e^{-\kappa}\) and \(e^{-2\kappa}\), respectively. **These are single-pair O(1/m) bounds** and do not control summation over N insertion positions: taking N of order \(m^2\) may still leave an O(m) scalar majorant. They do *not* settle same-grade boundedness on the complete Gauss-invariant anchored space.

## Independent actual-matrix tests (scope is finite)
The companion executable verifiers build the even-width SU(2) total-spin projectors, compute the genuine Gauss twirl (nuclear norm 1), form all CG output coefficient blocks, construct \(K_3\) as an **actual left/right matrix superoperator**, and solve the Poisson equation with residuals. Gauge invariance of **every response block** is checked via commutators with the total SU(2) generator. For N=2,4 and central singleton m up to 10/5, and for \(\chi_m(U_jU_{j+1})\) m up to 4/3, no tested normalized r=1 response grows persistently with m. Maximum observed single-pair ratios **before history discount** were approximately 0.042101 and 0.032959 respectively. These finite observations are not an all-degree physical no-go or closure theorem. Every nonconstant output is retained.

## Actual Borel transform equation in the uniform local disk
For the formal gauge-invariant fundamental score, \(S(\lambda)=\lambda A+\mathcal B_{\rm hist}(S,S)\), put \(\widehat S(\xi)=\sum_{n\ge1}S_n\xi^n/n!\). Beta-function integration proves the exact Borel-plane Volterra equation
\[
\boxed{\widehat S(\xi)=\xi A+\frac{d}{d\xi}\int_0^\xi
\mathcal B_{\rm hist}(\widehat S(\eta),\widehat S(\xi-\eta))\,d\eta.}\tag{3}
\]
The **derivative is essential**. The already established direct graded history bound and fundamental source cap \(\|S_n\|_{L^{(2)}}\le(n+1)\|S_n\|_{L^{(1)}}\) give convergence in both L^(1) and L^(2) on the uniform disk \(|\xi|<9e^{-\sigma}/5120\) at \(\kappa=\log4\). Thus the convolution, derivative, and equation (3) are actual **Banach-analytic identities in that local disk**, not merely formal algebra. Nothing here continues the solution beyond that disk or controls it on a Laplace ray.

## Finite-volume entire Borel transform and Laplace recovery
For a **fixed** N-face strip after reconstructing histories, the prior direct pairwise theorem gives a complete-face \(P_\sigma^{(1)}\) bilinear bound \(C_N=2+6N\). The source norm is \(M_N=\frac43N e^\sigma\). The finite-volume quadratic recurrence has coefficient majorant \(\|S_{N,n}\|\le\mathrm{Cat}_{n-1}C_N^{n-1}M_N^n\le(4C_N)^{n-1}M_N^n\). Therefore:
\[
\boxed{|\lambda|<\rho_N:=\frac{3e^{-\sigma}}{16N(2+6N)}
\quad\Longrightarrow\quad
S_N(\lambda)\ \text{converges in }P_\sigma^{(1)}.}\tag{4}
\]
Its Borel transform is **entire** (in this fixed-N Banach space), with
\[
\boxed{\|\widehat S_N(\xi)\|\le\frac{e^{4C_NM_N|\xi|}-1}{4C_N}.}\tag{5}
\]
For real \(0<\lambda<\rho_N\), the absolutely convergent Laplace integral \(\int_0^\infty e^{-t}\widehat S_N(\lambda t)\,dt=S_N(\lambda)\). This is a **finite-volume small-coupling Borel–Laplace representation**, and the reconstructed real score exponentiates to a positive finite-volume eigenfunction with an accompanying scalar energy term. The bound \(\rho_N=O(N^{-2})\) **shrinks with volume**, so it proves no uniform physical continuation or infinite-volume vacuum. For a single face, the earlier sharper same-face operator constant \(2/3\) improves the convergence radius to \(9e^{-\sigma}/32\).

An exact one-face independent recursion yields \(S_1=\chi_1/6,\ S_2=-\chi_2/288,\ S_3=-\chi_1/648+\chi_3/6480\). These verify the first nontrivial terms of (3).

## Verification and remaining targets
The attached archive contains four original Python scripts, all their passing logs and SHA-256 hashes, and an integrity-tested ZIP. One script tests explicit two-face twirled PW input against \(\chi_m\) through m=19; another tests widths 2 and 4, central inner insertions, all inverse residuals and Gauss commutators; the third tests **extended** Wilson inner inputs with all CG output blocks, physical inverse and gauge commutators; the fourth independently verifies one-face rational score coefficients, Catalan identities, local Borel equation and six finite-volume analytic bounds.

**Next:** evaluate the **summed**, separately gauge-invariant nested insertion family with N growing like m², preferably with exact spin-intertwiner projections and cancellations; independently seek uniform Borel-plane continuation/ray growth for the actual score. Analytic continuation of the infinite-volume score, Borel summability there, OS reconstruction, interacting spectral gap and 4D continuum Yang–Mills mass gap remain open.