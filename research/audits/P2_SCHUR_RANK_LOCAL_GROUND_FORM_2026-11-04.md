# P2: Definite-magnetic Schur rank and local positive-energy thermodynamic state condition

**2026-11-04, private original-link SU(2) straight-strip audit.** Full expanded report, actual physical Fourier engine, three independent verification programs, execution logs, SHA-256 manifest and integrity-tested portable archive: conversation attachment \`p2_weight_schur_ground_2026-11-04.zip\`. **Theorems are narrower than 4D Yang–Mills, a uniform gap, or global Borel summability.**

## P-56 — Exact fixed-depth source-rank reduction by magnetic-weight Schur blocks

For any face degree tuple c of total degree S, diagonal SU(2) acts on \(V_c=\bigoplus_J(V_J\otimes M_J)\). If ket u and bra v of a rank-one coefficient each have **definite** total magnetic weights a,b, their J projections are \(|J,a\rangle\otimes u_J\) and \(|J,b\rangle\otimes v_J\). Hence Haar conjugation gives zero if a≠b; if a=b:
\[
\boxed{\mathcal T(|u\rangle\langle v|)=\bigoplus_{J\ge|a|}\frac{I_J}{2J+1}\otimes|u_J\rangle\langle v_J|}.
\]
Each multiplicity block is rank **one**, even when the SU(2) multiplicity dimension is exponential. Consequently
\[
\boxed{\mathrm{rank}\,\mathcal T(|u\rangle\langle v|)\le\sum_{J\le S/2}(2J+1)
=\lfloor(S+2)^2/4\rfloor.}
\]
The actual **gauge-invariant** physical Poisson source for balanced even N and separately invariant high-spin character chi_m, m≥3, in each corrected-original-link output channel l=m±1 is \(Y_{j,l}=\mathcal T Z_{j,l}\). The exact two-bond collar polarization of P-38/P-42 produces ≤13(m+1) rank-one tensor terms. Using
\(J_i^xXJ_{i+1}^x+J_i^yXJ_{i+1}^y
=\frac12[J_i^+XJ_{i+1}^-+J_i^-XJ_{i+1}^+]\)
and the z-term, each individual term's ket and bra retain a definite magnetic weight (the local CG projection conserves that weight). Thus:
\[
\boxed{\mathrm{rank}(Y_{j,l})\le13(m+1)\lfloor(N+l+1)^2/4\rfloor.}\tag{1}
\]
Every corrected electric mixed-link application decomposes into ≤3(N−1) weight-homogeneous terms and commutes with residual SU(2) projection. So the q-th order actual-original-link Neumann approximation \(X_{j,l,[q]}\) obeys:
\[
\boxed{\mathrm{rank}(X_{j,l,[q]})\le13(m+1)\lfloor(N+l+1)^2/4\rfloor\sum_{p=0}^q[3(N-1)]^p.}\tag{2}
\]
At fixed q along N~m², this replaces the earlier P-38 O(m N³) cubature-term envelope by O(m N²). It permits a smaller certified rank r in the P-54 two-sided central-binomial moment interval. **Not** a uniform bound on rank or trace norm of the **untruncated** inverse; q growing with m still has uncontrolled complexity. Mixed-spin Haar and true corrected physical sources at N=2,4/m=3,4 checked, for both CG output sectors and all sites. Analytical theorem covers all even N≥2 and m≥3.

## P-57 — A local ground-state-form inequality for P-55 thermodynamic quantum-state limits

P-55 constructs locally normal translation- and simultaneous-SU(2)-conjugation-invariant quantum states \(\omega_\infty\) as trace-norm finite-window subsequential limits of **anchor-averaged genuine finite-strip ground-state density operators**. At coupling real lambda the original-link kinetic estimate yields \(\operatorname{tr}(\rho_{N,W}C_W)\le |W||\lambda|/2\) for every finite W.

Let \(A\) be a **smooth finite-rank local operator** with both range and adjoint range smooth, supported in interval W (length s). Let the *local commutator quadratic form* be \(\delta(A)=[H_{W^+},A]\), where W+ is the one-neighbor collar. The infinite-volume C*-dynamics is **not** constructed in this audit; \(\delta\) is a local form on an explicit smooth core.

For each anchor with W+ wholly inside the N-strip, the finite ground-state variational identity gives:
\[
\langle\psi_N,A^*[H_N,A]\psi_N\rangle
=\langle A\psi_N,(H_N-E_N)A\psi_N\rangle\ge0.
\]
At most s+2 of N anchors straddle the strip endpoints. Smooth finite rank makes all on-window second-order commutators bounded; the remaining neighbor-crossing commutators contain only a bounded operator times one external first-order generator. Since each such generator is form-bounded by \(\sqrt{C_i}\), the **total** finite-strip kinetic-energy estimate \(\sum_i\langle C_i\rangle_{\psi_N}\le N|\lambda|/2\), Cauchy–Schwarz, and O(s) exceptional anchors imply
\[
\boxed{\omega_N(A^*\delta(A))\ge -C_A(s+2)/N-C_{A,\lambda,W}/\sqrt N.}\tag{3}
\]
The constants are finite and independent of N.

Pass to the P-55 local trace-class limit: each \(\delta(A)\) has bounded smooth finite-window terms plus finite sums \(B_jR_j^a\) involving an adjacent **external** site and bounded B_j acting on W. As \(R_j^a\) commutes with its local Casimir \(C_j\) and \(|R_j^a|\lesssim C_j^{1/2}\), its high-Casimir part is controlled by \(C_j/\sqrt{\Lambda}\). Uniform local kinetic-energy bounds make these **first-order** tails uniformly negligible, while the spectrally cut-off operators are bounded and converge under local trace-norm convergence. Thus the limiting form exists and
\[
\boxed{\omega_\infty(A^*\delta(A))\ge0\quad\text{for every smooth finite-rank local }A.}\tag{4}
\]
This is the genuine local **positive-energy/ground-state-form inequality** for a smooth observable core. It advances P-55 beyond merely a kinematic quasi-local quantum-state limit. It **does not** identify a norm-continuous infinite-volume C*-dynamical group or prove the ground-state condition for its full generator. In particular, neither uniqueness, correlation decay, volume-uniform gap, physical Borel sum, OS reconstruction nor four-dimensional Yang–Mills mass gap is established.

Independent checks: finite-dimensional interacting chain with five noncommuting local observables and N=3..7 verifies the ground variational identity; exact anchor endpoint counts and SU(2) Casimir first-order spectral tails verify boundary-error ingredients. An independently restored actual corrected-original-link SU(2) Fourier engine tests the physical q=0 rank formula. The analytic argument, not finite test samples, establishes the stated all-width results.

## Next proof gates

**Physical:** exploit rank-reduced total-spin multiplicity Gram blocks at N~m² with certified numerical intervals and a controlled inverse remainder, or derive a true full-inverse high-spin Schatten asymptotic.

**Thermodynamic:** construct a suitable infinite-volume interacting C*-dynamical algebra, prove that the local smooth core is a generator core, and promote (4) to the full algebraic ground-state condition; only then pursue uniqueness, clustering and a uniform spectral gap.

**Scientific status: four-dimensional continuum Yang–Mills existence and mass gap OPEN.**
