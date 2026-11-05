# P2 — Genuine corrected collar Schatten-1 source bound, exact Hopf Haar cubature and finite-volume graph propagation

**Private audit, 2026-11-04.** Restricted corrected-original-link SU(2) finite open straight strip, genuine balanced residual-Gauss-invariant high-spin singleton source, unchanged first-moment Peter–Weyl trace-nuclear response. Full detailed proof, 3 independently executed verifiers, logs, SHA-256 manifest, and tested ZIP are in **Library → The Singular Boundary → Proof Audits**, named \`P2_COLLAR_NUCLEAR_CUBATURE_AND_FINITE_GRAPH_PROPAGATION_2026-11-04.md\` and \`p2_collar_hopf_graph_2026-11-04.zip\`. **No full physical N≈m² response asymptotic, uniform same-grade nonlinear closure, infinite-volume interacting automorphism, positive interacting gap, signed Borel/OS or 4D continuum Yang–Mills mass-gap theorem.**

## P-75 — Physical Gauss-twirled collar has a width-independent O(m²) nuclear source bound

Use the existing **genuine corrected** P-73 original-link q=0 Poisson collar identity, for alternating normalized product-vector outer source X=|u><v|, degree-m character insertion at site j, and output ell=m±1:
\[
Z_{j,\ell}=\delta_{m,\ell}B_{j,\ell}(X)
+\sum_{i\in\{j-1,j\}\cap[0,N-2]}\sum_{a=1}^3
\{J_i^a B_{j,\ell}(X)J_{i+1}^a-B_{j,\ell}(J_i^aXJ_{i+1}^a)\}.
\]
Here \(B_{j,\ell}(X)=W^\dagger(X\otimes I_{m+1})W\), with W a CG isometry, and \(\delta_{m,m-1}=m+2,\ \delta_{m,m+1}=-m\). The actual gauge-invariant source is \(Y_{j,\ell}=\mathcal T(Z_{j,\ell})\), Haar conjugation twirl. Expand the auxiliary identity into m+1 rank-one terms. The trace-norm of each compressed original product ket/bra is at most one. Each touching **output** bond generator pair has product norm ≤ell/4 (one degree ell and one degree 1); each touching original fundamental bond ≤1/4. There are at most TWO collar bonds and 3 SU2 directions each. So, by the trace-class ideal property, triangle inequality and trace-norm contractivity of the unitary Haar conjugation average,
\[
\boxed{\|Y_{j,\ell}\|_1\le\|Z_{j,\ell}\|_1
\le(m+1)\bigl[|\delta_{m,\ell}|+\tfrac32(\ell+1)\bigr]
\le A_m:=\tfrac52(m+1)(m+2).}\tag{1}
\]
**The bound is independent of strip width N and insertion j**. This source-specific estimate improves the prior P-67 use of the polynomial Gauss-source rank times its HS norm, but is not an arbitrary-input same-grade estimate.

Let \(D_\ell=3(N-1)+\ell(\ell+2)\) and use the *same actual corrected original-link induced Schatten-1 contractions* from P-67:
\[
\eta_{\rm end,\ell}=\frac{3(N-2)+\sqrt{3\ell(\ell+2)}}{2D_\ell},\qquad
\eta_{\rm int,\ell}=\frac{3(N-3)+2\sqrt{3\ell(\ell+2)}}{2D_\ell}<1/2.
\]
For the identical first-moment PW weights \(w_\ell=(\ell+1)^2/[4(m+1)^3]\), the **actual complete physical response** and q-order truncated Neumann response satisfy
\[
\boxed{0\le R_{N,m}\le
A_m\sum_{\ell=m\pm1}\frac{w_\ell}{D_\ell}
\left[\frac2{1-\eta_{\rm end,\ell}}+
\frac{N-2}{1-\eta_{\rm int,\ell}}\right],}\tag{2}
\]
\[
\boxed{|R_{N,m}-R_{N,m}^{[q]}|\le
A_m\sum_{\ell=m\pm1}\frac{w_\ell}{D_\ell}
\left[\frac{2\eta_{\rm end,\ell}^{q+1}}{1-\eta_{\rm end,\ell}}+
\frac{(N-2)\eta_{\rm int,\ell}^{q+1}}{1-\eta_{\rm int,\ell}}\right].}\tag{3}
\]
Unlike earlier spectral S2-to-S1 estimates, **no exponentially large Fourier dimension enters either formula**. For balanced even \(N=m^2+O(1)\), \(A_m\sim(5/2)m^2,\ w_{m-1}+w_{m+1}\sim(2m)^{-1},\ D_\ell\sim4m^2,\ \eta_{\rm int}\to3/8\). Consequently
\[
\boxed{R_{N,m}\le(\tfrac12+o(1))m,\quad
|R-R^{[q]}|\le(\tfrac12+o(1))m(3/8)^{q+1}.}\tag{4}
\]
**This is only an upper bound; O(m) is not O(1), so it does NOT establish uniform same-grade closure or the actual response asymptotic.** A fixed absolute error ε admits a **sufficient (not necessary)** q-depth \((\log m+\log(1/\epsilon)+O(1))/\log(8/3)\). The explicit formulas, not approximated asymptotics, provide the finite-width certificate. For ε=10⁻⁶, q=16 for m=3,4,6,10; q=17 for m=20,40; q=18 for m=80,160; q=19 for m=300; q=20 for m=1000, using N=m² with even-width correction.

### A constructive *positive*, exact O(S³) Haar cubature for product-tensor source terms

For an output degree tuple n with total twice-spin \(S=\sum_i n_i\), write SU2 in Hopf coordinates
\(g=\left(\begin{smallmatrix}\sqrt t e^{i\alpha}&\sqrt{1-t}e^{i\beta}\\-\sqrt{1-t}e^{-i\beta}&\sqrt t e^{-i\alpha}\end{smallmatrix}\right)\),
\(t\in[0,1],\alpha,\beta\in[0,2\pi)\), with normalized Haar \(dt\,d\alpha\,d\beta/(2\pi)^2\). Every fixed-sector conjugation matrix entry \(D_{\bf n}(g)ZD_{\bf n}(g)^*\) has Hopf-variable polynomial degree at most 2S. Choose **M=2S+1** equal positive phase nodes per phase, projecting exactly onto zero phase frequencies; after that projection the integrand is a polynomial in t of degree ≤S. **Q=S+1** positive Gauss–Legendre nodes integrate it exactly. Hence the **entire** fixed-degree Haar twirl is an exact finite positive weighted unitary-conjugation average with
\[
\boxed{Q M^2=(S+1)(2S+1)^2=O(S^3)\ \mathrm{nodes}.}\tag{5}
\]
Each node rotates a product ket/bra into another product ket/bra. Therefore the P-73 collar of at most 13(m+1) terms can be written as at most \(13(m+1)(S+1)(2S+1)^2\) **product rank-one** matrices, with no exponentially sized Fourier matrix or Schur-basis enumeration. This is a *constructive tensor representation*, not a statement of optimal rank or polynomial runtime for the **full electric inverse**; q corrected electric iterations may still expand as \([3(N-1)]^q\) (quasi-polynomial at q=O(log m)). Haar commutes with corrected K, so twirling can follow the explicit electric iteration. Independent numerical checks verify irrep unitarity, SU2 covariance and a two-face exact singlet/triplet twirl oracle. The analytic cubature exactness follows Fourier orthogonality and polynomial quadrature, not the numerical checks.

## P-76 — Finite-volume, all-time electric graph-form propagation; still not volume-uniform

Use the **actual** corrected original-link strip operator
\[
K_N=4\sum_i C_i+2\sum_{i=1}^{N-1}\sum_aR_i^aL_{i+1}^a,\quad H_N=K_N+\lambda V_N,\quad V_N=-\frac12\sum_i\chi_1(U_i),\ \|V_N\|\le N.
\]
By Cauchy–Schwarz on each adjacent spin link, \(2R_i\cdot L_{i+1}\ge-(C_i+C_{i+1})\) as a quadratic-form inequality. Therefore \(K_N\ge2\sum_iC_i\ge0\). The bounded magnetic potential makes H self-adjoint on the free domain. Define \(B_N=H_N+|\lambda|N\). As positive quadratic forms \(K_N\le B_N\le K_N+2|\lambda|N\); \(B_N\) is conserved under \(U_N(t)=e^{-itH_N}\). Consequently, for all \(t\in\mathbb R\) and \(\psi\in D(K_N^{1/2})\),
\[
\boxed{\|(1+K_N)^{1/2}U_N(t)\psi\|
\le\sqrt{1+2|\lambda|N}\ \|(1+K_N)^{1/2}\psi\|.}\tag{6}
\]
This proves **finite-strip all-time invariance of the global electric form domain**, despite P-72's failure of norm-C² for a protected Casimir projector. P-74's local half-Casimir-weighted double commutator, plus \(K_N\ge2\sum C_i\), permits control of the finite-strip second derivative of its Heisenberg orbit on a dense energy core (e.g. D(H_N)) in the **strong-vector** topology, with an N-dependent graph bound. It does **not** restore norm-C²; standard domain/commutator extension must be applied rather than identifying a bounded double commutator. The global propagation constant grows as √N at fixed λ, so **no infinite-volume invariant dynamical algebra, local-energy Lieb–Robinson bound, uniform generator or gap follows**. The portable numerical check uses compressed genuine SU2 first-face vacuum+fundamental and neighboring spin blocks with bounded magnetic compression, verifies K≥2(C1+C2) and (6) for λ=.25,1,2 and several times. This is not a full untruncated magnetic Hilbert-space calculation.

## Proof status

**Physical next step:** improve source-specific O(m) response control to uniform O(1), or compute actual full response asymptotic, via compressed corrected electric Krylov tensor networks, retaining the exact positive cubature and P-67 nuclear remainder. **Dynamical next step:** replace √(1+2|λ|N) global propagation by spatially localized control sufficient for the N→∞ limit. The current result is finite-volume only. **Signed Borel, interacting positive gap, OS and 4D continuum Yang–Mills existence/mass gap: OPEN.**