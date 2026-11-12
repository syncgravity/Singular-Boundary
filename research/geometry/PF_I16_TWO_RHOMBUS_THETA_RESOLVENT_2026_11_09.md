# PF-I16 — Exact two-rhombus theta-graph electric spectrum and Hilbert–Schmidt resolvent

**2026-11-09; finite original-link SU(2) theorem.** Retains a genuine pair of accepted four-edge Penrose–Fibonacci source rhombi sharing exactly one original edge, with all six other edges distinct. This is a source graph motif, not a cubic/Voronoi replacement or a full replay of every source crop. Full proof, executable verifier, log and SHA-256 manifest in Library: \`/The Singular Boundary/Proof Audits/PF_I16_TWO_LOOP_THETA_2026_11_09.zip\`.

## Exact electric spin-network spectrum

Let \`K=sum_e a_e C_e\`, \`a_e>0\` and \`C_e\` the SU(2) Casimir. Suppressing the four degree-two vertices **only for spin labeling** gives a trivalent theta graph: two exterior paths of three original edges each and the shared edge s. Put
\[
A=\sum_{e\in\partial f\setminus\{s\}}a_e,\quad
B=\sum_{e\in\partial g\setminus\{s\}}a_e.
\]
Gauge-invariant states have unique trivalent intertwiners indexed by twice-spin labels \`(n,m,ell)\` obeying \`|n-m|<=ell<=n+m\` and even \`n+m+ell\`. This is an orthonormal complete electric spin-network basis, with eigenvalues
\[
\boxed{E_{n,m,\ell}=\tfrac14[A n(n+2)+B m(m+2)+a_s\ell(\ell+2)].}
\]
The only vacuum is (0,0,0). For unit original-link coefficients \`A=B=3,a_s=1\`: (1,0,1) and (0,1,1) have E=3, while (1,1,0) and (1,1,2) have E=9/2,13/2, matching the prior exact shared-link singlet/triplet fusion denominators.

## Volume-independent coefficient bound for this *two-cycle* inverse

Assume every original-link coefficient \`a_e>=a0>0\`. For fixed \`n,m\`, \`min(n,m)+1\` values of \`ell\` are allowed. Since \`A,B>=3a0\`,
\[
\operatorname{Tr}'K^{-2}\le
\frac{16}{9a_0^2}\sum_{(n,m)\ne(0,0)}
\frac{\min(n,m)+1}{[n(n+2)+m(m+2)]^2}.
\]
Group by \`r=max(n,m)>=1\`: there are \`2r+1\` pairs, multiplicity <=r+1, and denominator >=r²(r+2)². An exact partial-fraction sum gives
\[
\sum_{r=1}^\infty \frac{(2r+1)(r+1)}{r^2(r+2)^2}
=\frac{\pi^2}{6}-\frac3{16}.
\]
Therefore
\[
\boxed{\|K^{-1}P_0\|_{\mathrm{HS}}^2
\le\frac1{a_0^2}\bigl(\frac{8\pi^2}{27}-\frac13\bigr),\quad
\|K^{-1}P_0\|_{\mathrm{HS}}\le1.60965645298/a_0.}
\]
The exact unit-coefficient cutoff trace \`Tr'K^-2\` at twice-spin truncation \`n,m<=256\` is 0.551596110773; the analytic remaining-tail bound is \`32/(9N)\` for cutoff \`N\`. The full inverse is genuinely Hilbert–Schmidt on this gauge-invariant **overlapping two-rhombus** sector, with no spin cutoff.

## Important limitations

An Hilbert–Schmidt \`L² -> L²\` inverse is **not** an \`L¹ -> L²\` convolution estimate and does not automatically bound \`K^-1 P0 Gamma_K(F,G)\` in \`L²\` from two Dirichlet norms, or provide sufficient H¹ control for iteration. The preceding independent-two-loop full-group convolution-kernel divergence is a different operator norm and does **not** contradict this gauge-invariant Hilbert–Schmidt trace result. No volume-uniform Hilbert–Schmidt bound is claimed for arbitrary growing graphs; all-orders nonlinear score convergence, interacting Poincaré gap, source-derived physical kinetic/time normalization, OS/continuum reconstruction, and Yang–Mills mass gap remain **OPEN**. No canonical main or historical source records modified.

Verification: exact rational state energies; SU(2) triangle-rule multiplicities; electric gap; finite trace cutoffs through 256; coefficient-weighted comparison; analytic tail and shell bounds.