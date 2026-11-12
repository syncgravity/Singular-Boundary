# PF-I16 — Third-order SU(2) low-spin return; complete second-order source-vacuum score

**2026-11-09 research audit.** Exact finite original-link SU(2) identities on authenticated elementary accepted four-edge Penrose–Fibonacci rhombi, not a cubic/Voronoi substitute. Full derivation, rational character checker (orders 1–8), exact Jacobi/Haar verification log, and checksum archive: Library \`/The Singular Boundary/Proof Audits/PF_I16_THIRD_ORDER_LOW_SPIN_2026_11_09.zip\`. No source-selected time or physical normalization is assumed.

## Exact third-order result on any genuine simple source rhombus

Let \`A_f=sum_{e in boundary f}a_e>0\`, \`p_f=Tr U_f/2\`, and \`H_f=sum_e a_e C_e+b(1-p_f)\`. In the source electric normalization \`C_e chi_n=n(n+2)chi_n/4\`, the holonomy characters satisfy \`K chi_n=A_f n(n+2)chi_n/4\` and \`chi_1 chi_n=chi_{n+1}+chi_{n-1}\`. With the positive ground-state score defined up to a scalar,
\[
\boxed{
\log\Omega_f=
\frac{2b}{3A_f}\chi_1
-\frac{b^2}{18A_f^2}\chi_2
+b^3\left[-\frac8{81A_f^3}\chi_1+
\frac4{405A_f^3}\chi_3\right]+O(b^4)
\pmod{\mathbb R}.}
\]
For unit electric links \`A_f=4\`: \`log Ω=b χ_1/6-b² χ_2/288+b³(-χ_1/648+χ_3/6480)+O(b⁴)\` modulo constants. **The third-order fundamental spin-1/2 component is nonzero and has the same electric denominator \`3A_f/4\` as at first order.** Therefore perturbation order does not force growing electric denominators. This is an explicit low-spin recoupling obstruction to naive all-order amplitude majorants; it does NOT disprove a convergent expansion or positive gap.

Unit-coefficient rational wavefunction recurrence: write \`psi_b=1+sum_{n>=1} b^n psi_n\` (Haar mean 1) and \`E'(b)=sum_{n>=2}e_n b^n\` for \`K-b χ_1/2\`. Then
\[
K\psi_n=\tfrac12\chi_1\psi_{n-1}+\sum_{k=2}^ne_k\psi_{n-k},
\qquad e_n=-\tfrac12[\chi_0](\chi_1\psi_{n-1}).
\]
Exact coefficients: \`psi_1=chi_1/6\`, \`psi_2=chi_2/96\`, \`psi_3=-5chi_1/1728+chi_3/2880\`. Coefficients of fundamental \`chi_1\` in the **log-score** at odd orders 1,3,5,7 are respectively \`1/6,-1/648,7/124416,-311/111974400\`. We do not assert all odd-order coefficients are nonzero. All character algebra through eighth order was calculated with exact fractions and the cubic coefficients were checked independently by diagonalizing the interacting one-rhombus Jacobi matrix (36 modes) and projecting its logarithmic ground state with 1000-node SU(2) Haar quadrature at b = 0.2, 0.1, 0.05, 0.02; checks passed.

## Completeness of the full fixed-finite-graph second-order score

For the actual accepted finite complex with \`H(t)=K+t sum_f b_f(1-p_f)\`, let \`log Ω_t=t S_1+t² S_2+...\`. The exact recurrence \`K S_2=P_0 Γ_K(S_1,S_1)\` and original-link locality imply **only two classes** of second-order histories:
\[
\boxed{S_2=\sum_fS_{2;f,f}+\sum_{\{f,g\}:f\sim g}S_{2;f,g}\quad(\bmod\ \mathbb R).}
\]
Here \`f~g\` means sharing an original source link. The newly computed same-face coefficient is
\[
\boxed{S_{2;f,f}=-\frac{b_f^2}{18A_f^2}\chi_2(U_f),\qquad
\|S_{2;f,f}\|_2=\frac{b_f^2}{18A_f^2}.}
\]
This follows from \`Γ_K(p_f,p_f)=(A_f/4)(1-p_f²)\`, \`p_f²=(1+χ_2)/4\`, \`Kχ_2=2A_fχ_2\`, and \`S_1=(b_f/\lambda_f)p_f\` with \`\lambda_f=3A_f/4\`.

For distinct faces meeting exactly one edge, \`S_{2;f,g}\` is the singlet/triplet expression from the prior PF-I16 shared-link fusion theorem. The complete anchored order-two history sum is bounded, under \`a_0<=a_e<=a_*\`, \`0<=b_f<=b_0\`, and source rhombus incidence at most 28 neighbors, by
\[
\boxed{\frac{b_0^2}{288a_0^2}+\frac{49}{351}\frac{a_*b_0^2}{a_0^3}.}
\]
This is a **fixed-order**, volume-independent per-face bound, not an all-orders global norm or spectral gap estimate.

## Proof status

Low-spin return at orders 3,5,7 and second-order full decomposition are exact finite-local algebra. All-orders connected-history summability, collective source vacuum mixing, uniform interacting Poincare, source-derived kinetic/time, continuum/OS reconstruction, and physical 4D Yang–Mills mass gap remain **OPEN**. Historical source data, canonical main and Observatory proof gates unchanged.