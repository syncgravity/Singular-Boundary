# P2: explicit Wigner-Gram projector, corrected two-face norm obstruction, and protected Casimir observables

**Private proof audit, 2026-11-04.** Corrected original-link SU(2) electric Hamiltonian on finite open straight strips with one fixed independent-face Peter–Weyl Fourier trace norm. Three separate mathematical results continuing P-58 and P-59. Expanded proof, three independently executed self-contained Python verifiers, logs, and SHA-256-tested ZIP are preserved in Library at \`/The Singular Boundary/Proof Audits/p2_next_dual_2026-11-04.zip\` with its expanded Markdown report. **No actual N≈m² high-spin response asymptotic, interacting infinite-volume automorphism group, uniform spectral gap, OS reconstruction or four-dimensional continuum Yang–Mills mass gap follows.**

## P-60 — Explicit SU(2) projected-Gram overlaps without exponential multiplicity spaces

In a fixed unitary SU(2) decomposition \(V=\bigotimes_i V_{n_i/2}=\bigoplus_J (V_J\otimes M_J)\), take tensor-product vectors \(u=\bigotimes_i u_i\), \(v=\bigotimes_i v_i\) with total magnetic weights \(a,b\). Their projected multiplicity factors \(\mu_{u,J},\mu_{v,J}\) satisfy
\[
\boxed{\langle\mu_{u,J},\mu_{v,J}\rangle=(2J+1)\int_{SU(2)}\overline{D^J_{ab}(g)}\,
\prod_i\langle u_i,D^{n_i/2}(g)v_i\rangle\,dg.}\tag{1}
\]
Proof: write \(\langle u,U(g)v\rangle=\sum_J D^J_{ab}(g)\langle\mu_{u,J},\mu_{v,J}\rangle\), then use Wigner orthogonality. **Different magnetic weights are aligned automatically through the single Wigner coefficient**. The previous P-58 required but did not give this explicit aligned-overlap construction.

Put \(S=\sum_i n_i\), \(L=2J\) and use Haar Hopf coordinates \(g=\begin{psmallmatrix}z&v\\-\bar v&\bar z\end{psmallmatrix}\), \(z=\sqrt t e^{i\phi},v=\sqrt{1-t}e^{i\psi}\), with \(t\) uniform on [0,1] and \(\phi,\psi\) independent uniform angles. The integrand is a polynomial of degree at most S+L in \(z,v,\bar z,\bar v\). Angular trapezoid quadrature with M>S+L points **per angle** exactly isolates the zero Fourier mode. For the permitted parity L≡S (mod 2), the surviving t dependence is a polynomial of degree at most (S+L)/2, so Gauss–Legendre with Q>(S+L)/4 nodes integrates it exactly. The independent executable conservatively uses M=Q=S+L+3.

Each local symmetric-spin matrix element has a finite binomial expansion with at most n_i+1 terms. Therefore the Gram overlaps of R product terms across O(S) spin sectors admit a **polynomial unit-cost arithmetic-work** algorithm at fixed Neumann depth q (naive conservative O(R² S^5) operations). This statement does **not** certify the bit complexity, numerical interval widths, cancellation, or q-depth required to make the full corrected physical inverse tail \(\Delta_q\) small at N≈m². Inserting certified Grams into the P-58 multiplicity-norm formula yields the previously established finite-depth enclosure \( \max(0,T_q-\Delta_q)\le R_{N,m}\le T_q+\Delta_q\).

**Independent tests:** nine Hopf-integral versus exact **direct total-Casimir spectral projector** calculations covering fundamental N=2,3,4 and the mixed tuples (1,2,1), (1,3,1), including cross-weight overlaps. Two tensor-only additional N=6,9 cases avoid constructing the 2^N Fourier matrix. Ordinary numerical tolerance 1e−9, not interval certification.

## P-61 — Corrected electric cross-link already prevents point-norm continuity on full local B algebra for some rank-one observables

The corrected open two-face electric Hamiltonian contains \(K_2=4(C_1+C_2)+2\sum_{a=1}^3R_1^aL_2^a\). Restrict to Peter–Weyl factors with face-1 right spin 1/2, face-2 left spin s (arbitrarily high), and fixed spectator indices, so the onsite Casimirs are scalars. On this sector the cross term is \(2\mathbf S_1\cdot\mathbf S_2\). Take the **one-face finite-rank** operator \(A=|\downarrow\rangle\langle\uparrow|\) in face-1 right spin, including a finite-rank projection on spectator indices, and embed it as A⊗I on two faces.

The input \(|\uparrow,s\rangle\) has cross energy s; A maps it to \(|\downarrow,s\rangle\). The total M=s−1/2 block on \(\{|\downarrow,s\rangle,|\uparrow,s-1\rangle\}\) is exactly
\[
H_{\mathrm{cross}}=\begin{pmatrix}-s&\sqrt{2s}\\\sqrt{2s}&s-1\end{pmatrix},
\quad \operatorname{spec} H_{\mathrm{cross}}=\{s,-(s+1)\}.
\]
The \(|\downarrow,s\rangle\) fractions in these two eigenspaces are \(1/(2s+1)\) and \(2s/(2s+1)\). For \(t_s=\pi/(2s+1)\to0\), the Heisenberg matrix-element jump gives
\[
\boxed{\|\alpha_{t_s}^{K_2}(A)-A\|\ge\frac{4s}{2s+1}\longrightarrow2.}\tag{2}
\]
For real fixed λ the bounded two-face magnetic \(V_2=-(\chi_1(U_1)+\chi_1(U_2))/2\) satisfies \(\|V_2\|\le2\). Duhamel yields
\[
\|\alpha_t^{K_2+\lambda V_2}(A)-\alpha_t^{K_2}(A)\|\le4|\lambda|\|A\||t|,
\]
so the discontinuity survives bounded magnetic coupling. This is a **specific full local B(L²SU2) norm-topology obstruction** even for an initially finite-rank local A; the example A is *not assumed gauge invariant*. It does not refute point-norm dynamics on a narrower gauge-invariant algebra, or strong Hilbert-space unitarity, or P-57's local positive-energy form. It strengthens P-59's free one-face Wilson-multiplication obstruction.

**Independent tests:** explicit 2×2 spin-coupling matrix spectra and phases at twice-spin 1,2,4,10,20,50,200,1000; exact formula matched at 5e−12, with the interacting λ=1 Duhamel lower bound included.

## P-62 — Width-uniform norm-Lipschitz *seed* of Casimir-diagonal local observables

For the same corrected original-link straight strip \(K_N=4\sum_i C_i+2\sum_{i,a}R_i^aL_{i+1}^a\), every local Casimir C_i commutes with every R/L generator on all faces. Hence, for any bounded local joint spectral function \(F=f(C_i:i\in W)\), **exactly**
\[
[K_N,F]=0.
\]
The real magnetic onsite terms \(V_i=-\chi_1(U_i)/2\) satisfy \(\|V_i\|\le1\). Therefore
\[
\boxed{\|[H_N(\lambda),F]\|\le2|\lambda|\,|W|\,\|F\|,
\quad\|\alpha_t^{H_N(\lambda)}(F)-F\|
\le2|\lambda|\,|W|\,|t|\,\|F\|.}\tag{3}
\]
The bounds are **independent of ambient strip width N and of all spin cutoffs**. They include local Casimir spectral projections, with a rigorous bounded commutator and uniform finite-volume time modulus. This is not an **invariant** algebra under the interaction: the evolved F need not remain a Casimir function, so it does **not** by itself construct an infinite-volume C*-dynamics or identify the full generator core.

**Independent tests:** exact finite-spin SU2 generators for first-site spin degrees 1 and 2, neighbors with degrees 1,2,4,8,16, and a bounded onsite mixing potential verify vanishing corrected electric commutator and bounded magnetic commutator.

## Remaining mathematical gates

1. **Actual high-spin physical response:** use the formula (1) on the P-56/P-58 corrected source tensor expansion at joint N≈m² with certified cancellation and Neumann remainder; prove an actual trace-nuclear asymptotic, not merely a fixed-q arithmetic result.
2. **Interacting thermodynamic dynamics:** construct an invariant gauge-compatible/energy-regularized dynamical algebra, using (2) to exclude inappropriate full B norm topology and (3) as a protected seed. Prove thermodynamic evolution, an actual generator-core theorem, and an algebraic ground-state condition extending P-57.
3. **Long-range and continuum:** volume-uniform interacting spectral gap, locality/clustering, signed Borel continuation, OS reconstruction and four-dimensional continuum Yang–Mills mass gap remain **OPEN**.

The companion archive was independently checked by \`sha256sum -c SHA256SUMS.txt\` and \`unzip -t\`; all three test scripts executed.