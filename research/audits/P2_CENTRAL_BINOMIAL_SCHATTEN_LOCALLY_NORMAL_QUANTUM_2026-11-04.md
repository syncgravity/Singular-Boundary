# P2 — central-binomial Schatten envelopes and locally normal thermodynamic quantum states

**2026-11-04.** This audit extends P-52 and P-53 for the **corrected original-link finite open SU(2) straight strip**, retaining a single independent-face PW norm. An independently run, SHA-256 verified expanded proof and self-contained test archive is supplied as conversation artifact \`p2_optimized_schatten_quantum_local_2026-11-04.zip\`, with expanded report \`P2_CENTRAL_BINOMIAL_SCHATTEN_AND_LOCALLY_NORMAL_QUANTUM_STATES_2026-11-04.md\`. **No joint N≈m² physical same-grade asymptotic, infinite-volume interacting ground-state inequality, uniform gap, Borel summability, OS reconstruction, or 4D continuum Yang–Mills gap is established.**

## P-54 — Exact O(n^-1/2) Schatten-1 polynomial enclosures from Gram moments

Set \(\beta_k=\binom{2k}{k}/[4^k(2k-1)]>0\). The positive binomial expansion gives
\[
\sqrt t=\sum_{k\ge1}\beta_k[1-(1-t)^k],\qquad 0\le t\le1.
\]
Its degree-n truncation \(P_n(t)=\sum_{k=1}^n\beta_k[1-(1-t)^k]\) increases **monotonically from below** to \(\sqrt t\). Its exact uniform error is
\[
\boxed{\sup_{t\in[0,1]}[\sqrt t-P_n(t)]
=\sum_{k>n}\beta_k=\binom{2n}{n}/4^n=:c_n\sim(\pi n)^{-1/2},}
\]
with equality at t=1. The central-binomial identity follows from the coefficient recurrence \(\beta_{n+1}=c_n-c_{n+1}\). This improves the old P-52 Bernstein error bound \((4n)^{-1/4}\).

For any finite Fourier block \(X\), a **certified** \(u\ge\|X\|_\mathrm{op}>0\) and integer \(r\ge\operatorname{rank}X\), define \(L_n(X;u)=u\,\mathrm{tr}\,P_n(X^\dagger X/u^2)\). Functional calculus proves
\[
\boxed{L_n(X;u)\nearrow\|X\|_{S_1},\qquad
L_n(X;u)\le\|X\|_{S_1}\le L_n(X;u)+ru\,c_n.}
\]
\(P_n(0)=0\), so only nonzero singular values count. \(P_n\) is a degree-n polynomial with no constant term; hence it uses only \(T_{2j}=\mathrm{tr}[(X^\dagger X)^j]\), j≤n. For the **actual** corrected-original-link q-Neumann block \(X_{c,q}=UV^\dagger\) of P-38, with small tensor Gram matrices A=U†U, B=V†V, these moments equal \(\mathrm{tr}[(AB)^j]\). A legitimate upper u is \(\sqrt{\|A\|_\mathrm{op}\|B\|_\mathrm{op}}\) and r is bounded by Gram column count. A stable floating evaluation uses the Hermitian Gram product \(A^{1/2}BA^{1/2}\) and the nonnegative polynomial basis; **interval arithmetic** is still necessary for certified numerical decimal enclosures.

For the disjoint genuine gauge-invariant high-spin insertion sectors c=(j,l), l=m±1, m≥3, with normalized grade-one weights \(w_c=(l+1)^2/[4(m+1)^3]\), let \(S_{nq}=\sum_cw_c L_n(X_{c,q};u_c)\), \(E_{nq}=c_n\sum_cw_cr_cu_c\). With the already proved total physical electric inverse Neumann error \(\Delta_q\):
\[
\boxed{\max(0,S_{nq}-\Delta_q)\le R_{N,m}\le S_{nq}+E_{nq}+\Delta_q.}
\]
At each **fixed finite N,m**, first n→∞ then q→∞ yields the exact physical Schatten sum. The rank bound, Gram conditioning, and q-growth have **not** been controlled uniformly along N≈m². This is a finite-width convergent certificate, not a physical same-grade theorem. For fixed rank and operator bound, the guaranteed accuracy improves in n from an O(ε^-4) bound to O(ε^-2).

**Regression:** 200 exact rational binomial identities, plus 25 independently sampled complex tensor Gram matrices at 8 orders (200 monotone, lower and upper tests). At n=128 the exact scalar tail is 0.04981910993614015, compared with the old Bernstein bound 0.21022410381342863.

## P-55 — Locally normal quantum-state subsequences on the bilateral infinite strip

Let \(G=SU(2)\), \(\mathcal H_i=L^2(G,dg)\), and \(\mathcal H_W=\bigotimes_{i\in W}\mathcal H_i\). Use the local operator C*-algebras \(B(\mathcal H_W)\) with embeddings A↦A⊗1 and their norm-inductive quasi-local algebra. For each real coupling λ and finite N let \(\psi_{N,\lambda}\) be the **true** corrected-original-link positive normalized finite-strip ground eigenfunction from P-49. Let Ω(g)=1∈L²(G) be the normalized **constant pure wavefunction** (not a maximally mixed state).

Translate the length-N pure state \(|\psi_N\rangle\langle\psi_N|\) to the sites [1−J,N−J] for J uniform on {1,…,N} and tensor \(|\Omega\rangle\langle\Omega|\) at every exterior site. Average over J, obtaining a quantum state \(\omega_N\), whose finite-window reduction is a trace-class density operator \(\rho_{N,W}\). Their **diagonal** configuration probabilities are exactly the P-53 translated measures; these new reductions retain **off-diagonal** information.

### Trace-energy control and local trace-norm compactness

The previously proved corrected electric inequality \(K_N\ge2\sum_iC_i\), \(E_N(\lambda)\le0\), \(\|V_N\|_\infty\le N\), yields \(\sum_i\langle\psi_N,C_i\psi_N\rangle\le N|\lambda|/2\). A fixed window W of s sites samples each physical face at most s times over N anchors, and C_iΩ=0 outside the strip. Therefore the **quantum** local kinetic energy satisfies
\[
\boxed{\mathrm{tr}(\rho_{N,W}C_W)\le s|\lambda|/2,\quad C_W=\sum_{i\in W}C_i.}
\]
Since C_W has compact resolvent on compact G^W, the spectral projector \(P_\Lambda=1_{C_W\le\Lambda}\) has **finite rank** and
\[
\varepsilon_{N,W}=\mathrm{tr}[\rho_{N,W}(1-P_\Lambda)]
\le s|\lambda|/(2\Lambda).
\]
The elementary trace compression inequality gives
\[
\boxed{\|\rho_{N,W}-P_\Lambda\rho_{N,W}P_\Lambda\|_1
\le2\sqrt{\varepsilon_{N,W}}+\varepsilon_{N,W}.}
\]
The compressed operators lie in a compact finite-dimensional set. The uniform tail hence proves **trace-norm relative compactness** of the full \(\{\rho_{N,W}\}\) for each fixed W.

Diagonal extraction over W=[−L,L] produces **one subsequence** \(N_k\to\infty\) such that \(\rho_{N_k,W}\to\rho_{\infty,W}\) in trace norm for every fixed finite window. By continuity of partial trace, \(\mathrm{tr}_{W'\setminus W}\rho_{\infty,W'}=\rho_{\infty,W}\) whenever W⊂W′. Thus
\[
\omega_\infty(A):=\mathrm{tr}(\rho_{\infty,W}A),\quad A\in B(\mathcal H_W),
\]
is a positive, normalized, consistent **locally normal quantum state** on the quasi-local C*-algebra. A translation of the anchored interval changes only two among N anchor summands, so \(|\omega_N(\tau A)-\omega_N(A)|\le 2\|A\|/N\): the limit is **shift invariant**. Uniqueness/positivity of finite ground states gives residual simultaneous SU(2) conjugation invariance. All P-53 diagonal-marginal regularity and magnetic bounds persist, including for λ>0:
\[
\boxed{\omega_\infty(\chi_1(U_0))\ge[\sqrt{9+\lambda^2}-3]/\lambda>0.}
\]
The state also inherits local kinetic-energy bounds by lower semicontinuity.

**Critical distinction:** this is a **quantum state**, unlike P-53's mere diagonal probability, but is **NOT YET PROVED an infinite-volume quantum ground state for the interacting dynamics**. The algebraic positive-energy/ground-state inequality for the unbounded corrected cross-link generator remains to be established. Also **no uniqueness, connected-correlation decay, excitation gap, signed positive Borel-ray continuation, or 4D Yang–Mills continuum mass gap** follows. An abstract GNS representation exists for any state; the missing property is the *interacting ground-state condition*, not bare GNS existence.

## Executed reproducibility and next research gates

The independent package includes \`verify_square_root_hierarchy.py\` (200 rational and 200 complex Gram assertions), \`verify_local_quantum_compactness.py\` (192 spectral-tail checks, off-diagonal density consistency, translation-anchor telescoping), the expanded analytic report, logs, and SHA-256 manifest. All scripts ran; \`sha256sum -c\` and \`unzip -t\` passed.

**Physical target:** compute/interval-enclose the small tensor-Gram spectra for N≈m², with actual inverse error and effective-rank asymptotics. **Thermodynamic target:** prove the positive-energy ground-state condition for the new locally normal quantum-state limits; then uniqueness/connected correlations/volume-uniform gap. **Analytic target:** actual signed positive-ray Borel continuation. These remain open.