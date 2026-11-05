# P2: genuine four-face corrected physical Schur inverse; gauge-invariant Casimir projector is not norm-C² under interacting dynamics

**Private audit — 2026-11-04.** Continuation of P-69 and P-70. The full expanded report, independent verified code, logs and SHA256-checked ZIP reside in Library, \`/The Singular Boundary/Proof Audits/P2_FOURFACE_PHYSICAL_SCHUR_AND_GAUGE_CASIMIR_C2_OBSTRUCTION_2026-11-04.md\` and \`p2_fourface_schur_c2_obstruction_2026-11-04.zip\`. Scope: actual corrected original-link SU(2) finite open straight strip and protected Casimir local observables. **No N≈m² physical nuclear asymptotic, interacting infinite-volume automorphism, gap, Borel/OS or four-dimensional continuum Yang–Mills mass gap proved.**

## P-71 — Four-face actual corrected-source **full** invariant electric inverse with nontrivial multiplicities

For N=4, m=3 or 4, outer source \(F_N=\mathcal T|+,-,+,-\rangle\langle-,+,-,+|\) from independent SU(2) Haar twirl, each of four insertion sites j and each Clebsch–Gordan degree \(\ell=m\pm1\), set
\[
Y_{j,\ell}=\tfrac12\left[B_{j,\ell}(K_{\bf1}F_N)+m(m+2)B_{j,\ell}(F_N)-K_{\bf c}B_{j,\ell}(F_N)\right],
\quad {\bf c}=(1,\ldots,\ell,\ldots,1)
\]
where \(B_{j,\ell}\) is the actual isometric CG compression of \(F_N\otimes I_{m+1}\). The genuine original-link electric operator remains
\[
K_{\bf c}(X)=\bigl[\sum_i c_i(c_i+2)\bigr]X-2\sum_{i=1}^{3}\sum_{a=1}^{3}J^a_{c_i}XJ^a_{c_{i+1}}.
\]
Compute the simultaneous SU(2) total Casimir and Jz, identify each highest-weight multiplicity space, and use normalized lower-spin ladders to construct **actual invariant matrix units**
\[
E_{J,\alpha\beta}=(2J+1)^{-1}\sum_{\mu=-J}^J |J,\mu,\alpha\rangle\langle J,\mu,\beta|.
\]
The full corrected K, restricted to their span, is a complex matrix of size \(\sum_J d_J^2\). At m=3, output \(\ell=2\) has multiplicities (3,3,1) for twice-spin L=(1,3,5), giving a **19-dimensional** invariant inverse; \(\ell=4\) has (1,3,3,1) for L=(1,3,5,7), giving **20-dimensional** invariant inverse. For m=4, both channels give 20 invariant dimensions. In contrast, full Fourier block dimensions are 24/40 for m=3, 32/48 for m=4; an unrestricted matrix-entry inverse would have up to \(48^2=2304\) coordinates. The true trace norm is \(\sum_J\|C_J\|_1\) for the solved multiplicity coefficient blocks \(C_J\), not merely absolute scalar sector traces as in N=2.

**Independent direct physical calculations:** (1) Haar twirl of the actual alternating rank-one outer input, CG compression and K applied to construct the source; (2) an explicit invariant-coordinate full K solve, reconstructing each sector and checking \(\|KX-Y\|_2\lesssim2\times10^{-14}\); (3) a separate direct full-Fourier Neumann q=18 solve, with the certified P-67 S1 bond remainder, and agreement of the total direct nuclear norm with the sum of multiplicity S1 norms.

| N | m | Full invariant-solve extensive first-moment response | Direct q=18 Fourier response | Historic independent dense response |
|---:|---:|---:|---:|---:|
| 4 | 3 | 0.129125009534 | 0.129125009534 | 0.1291250095 |
| 4 | 4 | 0.116983327352 | 0.116983327351 | 0.1169833274 |

All four insertion locations, both physical output degrees and both m values pass. The two algorithms agree within 2×10⁻¹⁰ on the summed response. The full invariant matrices' residuals are ~10⁻¹⁴. **These are ordinary floating-point computations, not exact-rational or interval-certified values.** The independent N=2,m=3 exact rational physical result from P-69 is checked as a regression; the Haar implementation was corrected to conjugate the twirled bra. The outer F has nuclear norm 1 and HS norm \(1/\sqrt{N+1}\), as established independently.

**Boundary:** this is the first recorded genuine four-face full corrected physical K inverse with nontrivial 3×3 multiplicity blocks; it does **not** achieve N=m² with m increasing, nor a scalable polynomial-bit spin-coupled implementation because the invariant basis itself was formed using dense finite Fourier matrices.

## P-72 — Exact gauge-invariant **second operator-norm derivative** obstruction

Consider the actual two-face interacting rotor Hamiltonian
\[
H_2(\lambda)=4(C_1+C_2)+2\sum_{a=1}^3R_1^aL_2^a
+\lambda(V_1+V_2),\qquad V_i=-\chi_1(U_i)/2.
\]
Let \(P_0=|\Omega\rangle\langle\Omega|\) be the spin-zero Casimir spectral projector on face one, embedded as \(F=P_0\otimes I\). This operator is **SU(2)-conjugation-invariant**. All corrected electric terms commute with F, so for every real \(\lambda\), \([H_2(\lambda),F]=\lambda D\otimes I\) is bounded, with \(D=[V_1,P_0]\). This yields norm-C¹ local Heisenberg regularity as in P-62.

In normalized one-face Peter–Weyl basis, \(\chi_1\Omega=(|+,+\rangle+|-,-\rangle)/\sqrt2\). Hence
\[
\|[R_1^z,D]\Omega\|=1/4>0.
\]
Let the adjacent face have arbitrarily high left spin s, and compress the double commutator to its highest-weight vector \(|s,s\rangle\). Because \(\langle L_2^z\rangle=s\), \(\langle L_2^{x,y}\rangle=0\), the compression is
\[
2\lambda s[R_1^z,D]+\lambda[4C_1,D]+\lambda^2[V_1,D].
\]
The last two terms are bounded in the fixed low-spin face-one range, independent of s. Applying the first to \(\Omega\) yields the **rigorous unboundedness lower bound**
\[
\boxed{\|[H_2,[H_2,F]]\|\ge |\lambda|s/2-B_\lambda\to\infty\quad(\lambda\ne0)}
\]
on the natural dense operator core. Thus the second commutator has **no bounded extension**, and the actual Heisenberg orbit \(\alpha_t(F)=e^{itH_2}Fe^{-itH_2}\) **cannot be twice differentiable at t=0 in the operator norm** for any \(\lambda\ne0\). The argument uses a **gauge-invariant protected Casimir projection**, unlike P-61's non-gauge-assumed first-norm-topology counterexample.

Also \(D=[V_1,P_0]\) is spin-off-diagonal, so the *abelian* Casimir-projection C*-algebra is **not invariant under the interacting derivation**, despite the bounded first commutator. This eliminates it as an invariant norm-C² interacting generator core. It does **not** exclude an appropriate larger energy-regularized algebra or a weak/strong continuous dynamics. And it **does not contradict P-70**: ground-state time-correlation matrix elements can be C² with controlled fourth spectral moment even when the full operator orbit is not norm-C².

**Executed verification:** explicit one-face vacuum+fundamental PW matrices produce \(\|[R_z,D]\Omega\|=1/4\). Exact neighbor highest-weight compression and finite-spin numerical regressions for s=.5,1,2,5,10,25,50,500 confirm the linear blow-up. The analytic argument, not the finite examples, establishes unboundedness.

## Next gates and scientific status

**Physical:** build total-spin multiplicity spaces and actual corrected physical Poisson tensors using tensor-network/recoupling data **without** forming dense \(2^N\) Fourier matrices. Combine with the P-67 dimension-free S1 tail at logarithmic sufficient q and determine the actual N≈m² Schatten asymptotic.

**Thermodynamic:** the protected Casimir projection algebra cannot be an invariant norm-C² core. Construct a gauge-compatible enlarged algebra, energy-weighted topology, resolvent-style domain or a representation-level dynamics, and establish a common interacting generator with all-time consistency. The positive-frequency correlation kernel C² theorem is a matrix-element theorem, not a norm-C² Heisenberg theorem.

**Positive interacting infinite-volume gap, signed positive-ray Borel continuation, OS reconstruction and 4D continuum Yang–Mills existence/mass gap: OPEN.**