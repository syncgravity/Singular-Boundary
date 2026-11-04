# P2 — One-Haar physical source dual numerator and Gaussian source-order Banach closure

**2026-11-04.** Corrected original-link SU(2) open straight strips, represented consistently in independent face Peter–Weyl trace-class coefficients. Two distinct theorems: (A) an exact polynomial-arithmetic **Hilbert–Schmidt numerator** for a legitimate physical q=0 Schatten response dual, with width N=10,m=3 and N=16,m=4 evaluations beyond the previous dense Fourier tests; (B) a **bounded source-order-graded nonlinear Banach algebra** retaining the original exponential spatial-history weight. **Neither theorem establishes the full physical trace-norm asymptotic at N~m², actual score convergence at λ=1, Borel summability, an interacting vacuum, or 4D continuum Yang–Mills existence/mass gap.** Expanded complete proof, three executable regression checks plus a portable physical Fourier engine, full logs and SHA-256 integrity: conversation artifact \`p2_onehaar_sourceorder_audit_2026-11-04.zip\`.

## A. Exactly one Haar integral for each physical source Hilbert–Schmidt norm

Let N≥2 be even, m≥3 and j a face index. Let X_N=|v><w| be the **untwirled** alternating extremal rank-one coefficient, T_N the residual simultaneous-SU(2)-conjugation Haar projection, and F_N=T_N X_N the genuine **gauge-invariant** balanced input. The second input is the **separately** gauge-invariant χ_m(U_j). Retain both physical CG output degree sectors c_i=1 for i≠j, c_j=l∈{m−1,m+1}, with D_c=3(N−1)+l(l+2).

Write P_{j,l} for local CG compression, B_i(X)=Σ_a J_i^a X J_{i+1}^a in the **appropriate input or output degree representation**, and H=P_{j,l}(X_N⊗I_{m+1}). The corrected physical centered Poisson **untwirled** source is exactly
\[
Z_{j,l}=\frac{3+m(m+2)-l(l+2)}2 H+
\sum_{i\in\{j-1,j\}\cap[1,N-1]}
\big[B_i^{out}(H)-P_{j,l}(B_i^{in}(X_N)\otimes I_{m+1})\big].
\]
All shared-link terms outside the insertion's two-bond collar cancel **identically** because P_{j,l} commutes with those original-link actions. The actual physical source is Y_{j,l}=T_cZ_{j,l}, since the corrected K and the Poisson bilinear operation commute with global residual gauge conjugation when the inner character is invariant.

The untwirled Z has at most 13(m+1) rank-one **tensor-product** terms for an interior insertion, at most 7(m+1) for an endpoint, and **identical rank-one local spectator factors at every untouched face**. Since T_c is an orthogonal projection for the Hilbert–Schmidt scalar product,
\[
\boxed{\|Y_{j,l}\|_2^2=\langle Z_{j,l},T_cZ_{j,l}\rangle
=\int_{SU(2)}\operatorname{tr}(Z_{j,l}^\dagger\pi_c(g)Z_{j,l}\pi_c(g)^\dagger)\,dg.}\tag{A1}
\]
For Z=Σ_α z_α⊗_i|u_{αi}><v_{αi}|, the integrand is the **single-Haar, tensor-local** sum
\[
\boxed{\sum_{\alpha,\beta}\bar z_\alpha z_\beta\prod_i
\langle u_{\alpha i},\pi_{c_i}(g)u_{\beta i}\rangle
\langle\pi_{c_i}(g)v_{\beta i},v_{\alpha i}\rangle.}\tag{A2}
\]
All non-collar factors collapse to a single scalar product. The **exact** SU(2) Hopf cubature P-34 uses Q=ceil((S+1)/2) radial nodes and (2S+1)^2 angular nodes, S=N−1+l. The evaluation requires only a polynomial number of local-spin and scalar algebra operations in N,m; it does **not** construct the 2^(N−1)(l+1)-dimensional output matrix. Numerical conditioning, interval certification and bit complexity for very large m remain separate.

**Physical q=0 dual certificate.** The q=0 inverse output block is Y_{j,l}/D_c. Haar twirl contracts operator norm, so ||Y||op≤||Z||op. Moreover Z factors as a three-face collar operator tensor an untouched-spectator rank-one ket–bra; thus ||Z||op is computable in dimension at most 4(l+1), independently of N for an interior insertion. The valid Schatten dual W=Y/||Z||op gives
\[
\boxed{\|Y_{j,l}/D_c\|_1\ge\frac{\|Y_{j,l}\|_2^2}{D_c\|Z_{j,l}\|_{op}}.}\tag{A3}
\]
For grade r=1, σ=0, the normalized **physical** sector factor is \((l+1)^2/[4(m+1)^3]\). These lower bounds sum over the exact disjoint insertion sectors (m≥3), but the P-36 Neumann error \(\Delta_0\) must be **subtracted** before inferring a lower bound on the full actual electric inverse. It is not small enough in the tested cases to settle the high-spin asymptotic.

Independent exact-cubature **numerical** results (rational numbers below are reconstructions of numerical values, *not symbolic-rational proofs*):
| N | m | site j (zero-based) | output l | rank-one factors | physical source ||Y||2² |
|---:|---:|---:|---:|---:|---:|
| 2 | 3 | 0 | 2 | 28 | 2.343750000000 |
| 2 | 3 | 0 | 4 | 28 | 3.906250000000 |
| 4 | 3 | 1 | 2 | 52 | 1.597916666667 |
| 4 | 3 | 1 | 4 | 52 | 2.472916666667 |
| 10 | 3 | 4 | 2 | 52 | 0.685101010101 |
| 10 | 3 | 4 | 4 | 52 | 1.116919191919 |
| 16 | 4 | 7 | 3 | 65 | 0.983960784314 |
| 16 | 4 | 7 | 5 | 65 | 1.439843137255 |

The 2/4-face cases reproduce the **fully twirled corrected original-link dense physical source** with residual error below 1e−8. The width 10 and 16 tests use local tensor overlaps only. The local 3-face operator-norm certificate gives illustrative **q=0 interior-site-only lower contributions**, before history discount, ≈0.0117683670 for N=10,m=3 and ≈0.0100285339 for N=16,m=4; those numbers are **not** lower bounds on the full true response without subtracting \(\Delta_0\). Both interior index parities were separately checked at widths 4 and 10.

## B. Source provenance excludes ungraded low-order nonminimal tags

In the fundamental magnetic-source expansion, retain the full finite-support source-count multiindex m_i at each face. For a nonzero coefficient of source order n=Σ_i m_i with exactly the connected source-history I=supp m, SU(2) CG parity/degree and corrected K-inverse degree preservation imply
\[
\boxed{0\le c_i\le m_i,\qquad c_i\equiv m_i\pmod 2.}\tag{B1}
\]
Thus, at each i∈I with final spin degree zero, m_i≥2, while with degree c_i≥1 we have m_i≥c_i. In particular
\[
\boxed{n\ge\sum_{i\in I}(c_i\text{ if }c_i\ge1\text{ else }2).}\tag{B2}
\]
The P-41 abstract long-tag gauge-invariant \([I_L]\chi_1(U_1)\) witness **cannot occur below source order 2L−1** in a fundamental-source history family. This condition is necessary, **not sufficient** for nonzero source-generated coefficients.

## C. A source-order graded Banach algebra retaining original spatial weights

Let \(\mathscr L_n\) be the source-provenance degree-n, Gauss-invariant history-family space with the **original** anchored face-PW \(L_{\kappa,\sigma}^{(1)}\) norm, face representation degree cap≤n, history length≤n, and optionally the stronger source-count parity restrictions (B1). Both provenance and history union are additive under the quadratic physical Poisson operation. For a>0, ρ>0 define the complete \(\ell^1\) Banach space
\[
\boxed{\mathfrak X_{a,\rho}=\{F=(F_n)_{n\ge1}:\ \|F\|_{a,\rho}=\sum_{n\ge1}\rho^ne^{-an^2}\|F_n\|_{L^{(1)}_{\kappa,\sigma}}<\infty\}.}\tag{C1}
\]
The previously *independently established* P-23 graded all-history theorem and source-order spin cap give, for grades n,m≥1,
\[
\|\mathcal B(F_n,G_m)\|_{L^{(1)}}\le
[C_{\rm same}+24e^{-\kappa}(n+m+2)]\|F_n\|_{L^{(1)}}\|G_m\|_{L^{(1)}}.
\]
Because output order=n+m and \((n+m)^2-n^2-m^2=2nm\), the original exponential spatial norm is untouched while the Gaussian source-order ratio gains e^(-2anm):
\[
\boxed{\|\mathcal B(F,G)\|_{a,\rho}\le H_a\|F\|_{a,\rho}\|G\|_{a,\rho},\
H_a=\sup_{n,m\ge1}[C_{\rm same}+24e^{-\kappa}(n+m+2)]e^{-2anm}<\infty.}\tag{C2}
\]
At κ=log4 (t=1/4), C_same=88/3 and the moment-loss constant 24t=6. Since n+m+2≤2nm+2, for every a≥1/8, \(H_a=(160/3)e^{-2a}\), attained at n=m=1. The fundamental source's weighted norm is \(\rho e^{-a}(16/3)e^\sigma\). The usual quadratic ball contraction criterion at **formal** λ=1, σ=0, ρ=1, a=3 becomes
\[
\boxed{4H_3\|A\|_{3,1}=\frac{10240}{9}e^{-9}=0.14041293265\ldots<1.}\tag{C3}
\]
This certifies a bounded-bilinear fixed point of the **source-order-labelled formal recurrence in a deliberately weak source-order topology**. The evaluation/forgetful map \(F\mapsto\sum_{n\ge1}\lambda^nF_n\) is **not continuous** in this space for nonzero λ, because e^(-an²) suppresses high orders faster than n! or |λ|^n. The contraction therefore **does not** produce the physical score at λ=1, a positive infinite-volume measure, any Borel–Laplace representation or an interacting spectral gap. Its value is that the formal nonlinear recurrence is directly and rigorously bounded while retaining physically motivated **spatial** history weights rather than the unbounded weakened spatial-history algebra of P-41.

## Independent tests and next proof gates

Companion archive: complete expanded report; independent dense corrected-original-link Fourier engine; one-Haar three-face tensor source verifier through widths 2,4,10,16; a local operator-norm dual check; **7,376 exact** face-parity/source-order checks and 22,500 integer graded estimates, plus 70-digit contraction arithmetic; verification logs, SHA-256 manifest and ZIP integrity checks. All passed.

**Next physical gate:** derive joint m,N≈m² asymptotics for the one-Haar scalar and its local op-norm denominator, then make a q-th-order dual **strictly positive after subtracting** the independently certified Neumann tail. **Next reconstruction gate:** find a source-reachable norm with a **continuous** evaluation/Laplace map and appropriate positive-ray growth; source-order Gaussian algebra closure by itself does not suffice. Unrestricted gauge-invariant same-grade control, infinite-volume Borel summability, interacting gap and 4D continuum Yang–Mills mass gap remain OPEN.
