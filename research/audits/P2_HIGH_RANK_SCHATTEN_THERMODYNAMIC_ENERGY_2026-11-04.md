# P2: higher-rank Schatten moments, one-face spectral-sector correction, and a thermodynamic ground-energy density

**2026-11-04. Private audit.** Restricted corrected original-link SU(2) finite open straight square strip, using independent face Peter–Weyl trace-class Fourier norms. Companion reproducibility artifact: p2_highrank_thermodynamic_2026-11-04.zip (full expanded proof, three scripts, logs, SHA-256 manifest). **No volume-uniform physical Schatten asymptotic, positive spectral gap, Borel summability, OS reconstruction, or 4D continuum Yang–Mills mass-gap theorem.**

## P-50. A high-rank Schatten witness computable using Gram moments

For a finite Fourier block X, let T₂=tr(X†X), T₄=tr[(X†X)²]. Schatten log-convexity at p=1,2,4 gives
\[
\boxed{\|X\|_{S_1}\ge T_2^{3/2}/\sqrt{T_4}
=\|X\|_{S_2}\sqrt{r_\mathrm{eff}(X)},\quad
r_\mathrm{eff}=T_2^2/T_4.}
\]
Zero blocks contribute zero. Unlike the previous Rayleigh witness T₂/||X||op, this detects effective singular-value rank.

For each q-th original-link electric Neumann approximation X_q=UV† in the tensor-rank decomposition P-38, define *small* Gram matrices A=U†U, B=V†V. Cyclicity gives the **exact polynomial-rank Gram formulas at fixed q**
\[
\boxed{T_2(X_q)=\operatorname{tr}(AB),\qquad T_4(X_q)=\operatorname{tr}[(AB)^2].}
\]
For the true gauge-invariant *summed* insertion, separate output tuple (j,l), l=m±1 (m≥3), use the correct first-moment Fourier weight \(w_{j,l}=(l+1)^2/[4(m+1)^3]\), and the previously certified all-sector Neumann tail \(\Delta_q\). Then
\[
\boxed{R_{N,m}\ge\max\{0,\ \sum_{j,l}w_{j,l}T_{2,j,l,q}^{3/2}/\sqrt{T_{4,j,l,q}}-\Delta_q\}.}
\]
The common history discount is applied to the whole inequality if needed. This is a rigorous lower bound **after certified evaluation** of the q-Gram moments and the tail, but neither near-optimal q nor a stable/interval-certified large-N≈m² Gram calculation has been completed. For q=O(log m) the straightforward Gram representation may be quasi-polynomial, not a certified polynomial-bit-complexity algorithm.

**Independent actual corrected original-link full Fourier tests**: Gauss-invariant alternating outer twirl, separately invariant chi_m singleton, both exact CG outputs and every site. Undiscounted ratios:

| N | m | true full S1 | full-block moment lower | full-block op-normalized Rayleigh lower | q=0 moment lower |
|---:|---:|---:|---:|---:|---:|
| 2 | 3 | .0723909692 | .0675634703 | .0621520654 | .0595530195 |
| 2 | 4 | .0612580952 | .0572607042 | .0523737450 | .0526332525 |
| 4 | 3 | .1291250095 | .0990845455 | .0847671578 | .0845729036 |
| 4 | 4 | .1169833274 | .0906677735 | .0787534080 | .0804512137 |

The **full-block** moments here use the actual small dense K inverse; they are not a scalable large-width computation. The moment lower detects 77–93% of the full response in these four tests. This does NOT prove any joint large-m trace-norm lower or upper asymptotic. A rank-sensitive moment estimate is the next physical target, not a mass-gap result.

## P-51. Real-coupling thermodynamic ground-energy density exists

For the *true* corrected original-link straight-strip Hamiltonian
\[
H_N(\lambda)=K_N+\lambda V_N,\quad
K_N=4\sum_{i=1}^N C_i+2\sum_{i=1}^{N-1}\sum_a R_i^aL_{i+1}^a,\quad
V_N=-\frac12\sum_{i=1}^N\chi_1(U_i),
\]
let E_N(lambda) be its lowest eigenvalue. The ground eigenfunction for each finite N and real lambda is unique, smooth, strictly positive and invariant under *simultaneous* SU(2) conjugation (P-49). As every boundary generator transforms as a nontrivial adjoint three-vector, conjugation invariance implies
\[
\langle R_N^a\rangle_{\psi_N}=0,\quad
\langle L_1^a\rangle_{\psi_M}=0.
\]
For N+M contiguous faces, the only new link cross-term between the two blocks is \(2\sum_aR_N^aL_{N+1}^a\). Its expectation in the trial product ground state \(\psi_N\otimes\psi_M\) vanishes **exactly**, so the variational principle gives **full subadditivity**
\[
\boxed{E_{N+M}(\lambda)\le E_N(\lambda)+E_M(\lambda)\qquad(\lambda\in\mathbb R).}
\]
Because \(K_N\ge0,\ |V_N|\le N\), the energy satisfies \(-N|\lambda|\le E_N(\lambda)\le0\). Fekete's lemma therefore proves a **full (not merely subsequential) thermodynamic limit**
\[
\boxed{e_\infty(\lambda)=\lim_{N\to\infty}E_N(\lambda)/N
=\inf_{N\ge1}E_N(\lambda)/N\in\mathbb R.}
\]
The actual one-face character trial subspace span{chi_0,chi_1} has lowest eigenvalue \((3-\sqrt{9+\lambda^2})/2\); the product of N copies has zero cross-link trial expectation, giving
\[
\boxed{-|\lambda|\le e_\infty(\lambda)
\le\tfrac12(3-\sqrt{9+\lambda^2})<0\quad(\lambda\ne0).}
\]
Each E_N/N is concave and 1-Lipschitz in lambda, so e_infty is concave and 1-Lipschitz; center flip U_i→−U_i maps H_N(lambda) unitarily to H_N(−lambda), hence e_infty is **even**. At every differentiability point of e_infty, concavity plus Feynman–Hellmann prove convergence of the averaged magnetic expectation:
\[
\boxed{\lim_{N\to\infty}\frac1{2N}\sum_{j=1}^N
\langle\chi_1(U_j)\rangle_{N,\lambda}=-e_\infty'(\lambda).}
\]
Nondifferentiability points of this concave real function are at most countable. The theorem constructs a genuine interacting **thermodynamic scalar energy density**, **not** a unique infinite-volume state or its gap. It gives no correlations, spatial clustering, Borel summability, continuum limit or 4D mass gap.

## Correction and separation of one-face spectral sectors (P-49)

The one-face character Jacobi matrix with off-diagonal \(-\lambda/2\) describes **only the conjugation-invariant class-function sector** ell=0. On the **unrestricted** L²(SU(2))≅L²(S³), angular momentum ell≥0 under conjugation yields Jacobi diagonal n(n+2), n≥ell, and
\[
\boxed{H^{(\ell)}_{n,n+1}=-\frac\lambda2
\sqrt{\frac{(n-\ell+1)(n+\ell+2)}{(n+1)(n+2)}}.}
\]
The normalized Gegenbauer recurrence derives this exactly. At λ=1 the first excitation on **unrestricted** L² is ell=1, whereas the Gauss-invariant **physical class-sector** first excitation is ell=0. The ell=1 n=1,2 two-state trial energy is below 3; ell≥2 sectors start above 7 by min–max; and the ell=0 second level is above 3 by a Schur-complement bound: in H^(0)−3 the n≥2 tail is ≥4, its correction on n=1 is at most 1/16, and the 2×2 Schur determinant 3t−1/4<0 shows only one class-sector eigenvalue below 3.

**Ordinary-precision convergence at λ=1**:
- E_0 = −0.081941823376.
- First unrestricted excitation ell=1: 2.966772324652; **unrestricted gap 3.048714148028**.
- First Gauss-invariant class excitation ell=0: 3.031921988128; **physical class-sector gap 3.113863811504**.

Thus P-49's numerical 3.1138638 is **correct for the class/Gauss-invariant sector**, but not as an unrestricted L² gap. The previous rigorous Δ_1(1)≥1 remains true in both. The numerical decimals are not formal interval enclosures.

## Verification and boundaries

Companion independent scripts verify: four *true* finite physical Gauss-invariant corrected-link Fourier responses and Schatten-2/4 interpolation; all-ell one-face Jacobi spectra and rigorous ordering logic; exact block-product subadditivity ingredients and negative energy-density trial bound. Scripts/logs and checksum manifest pass ZIP integrity and SHA-256 checks.

**Next physical gate:** prove or disprove high-m growth of effective rank r_eff along N≈m² using the q-truncated local tensor Gram matrices and certified Neumann tail.

**Next analytic/gap gate:** use the now-existing thermodynamic energy density to investigate uniqueness/local correlations and whether a **uniform gap** survives increasing N, or derive an actual positive-ray Borel reconstruction. None follows solely from subadditivity.

**Scientific status:** four-dimensional continuum Yang–Mills existence and positive mass gap **OPEN**.