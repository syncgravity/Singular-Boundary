# P2: genuine corrected SU(2) local fusion-tree source and sharp critical Casimir energy weight

**Private audit — 2026-11-04.** Continuation of P-71/P-72 in the **restricted corrected original-link SU(2) finite open straight strip**, using the unchanged independent-face Peter–Weyl first-moment nuclear norm. The complete analytic report, independently executed verifiers, execution logs and SHA-256-checked ZIP are stored in Library:
\`/The Singular Boundary/Proof Audits/P2_LOCAL_FUSION_PHYSICAL_SOURCE_AND_CRITICAL_ENERGY_WEIGHT_2026-11-04.md\` and \`p2_fusion_energy_2026-11-04.zip\`. **No complete large-width N≈m² physical nuclear response, interacting infinite-volume automorphism, mass gap, Borel/OS reconstruction or 4D continuum Yang–Mills existence theorem is claimed.**

## P-73 — Actual q=0 Poisson source AND reduced original-link electric K from local SU(2) fusion tensors

For a physical output tuple \(\mathbf n=(1,\ldots,\ell,\ldots,1)\), \(\ell=m\pm1\), use left-associated SU(2) CG fusion paths \(p=(L_0=n_0,L_1,\ldots,L_{N-1}=L)\), with **twice-spin** labels and \( |L_{i-1}-n_i|\le L_i\le L_{i-1}+n_i\) of the correct parity. Coupled states \(|p,M\rangle\) are finite MPS with site tensors \(A_i=\langle L_{i-1}/2,m_{i-1};n_i/2,k_i|L_i/2,m_i\rangle\). Local generator matrix elements \(\langle r,M'|J_i^a|p,M\rangle\) are calculated by contracting the two CG MPS networks, without diagonalizing the exponential-dimensional total Casimir operator.

Normalized SU(2)-invariant matrix units are \(E_{pq}=(L+1)^{-1}\sum_M|p,M\rangle\langle q,M|\). The **actual corrected** original-link electric map
\[
K_{\mathbf n}(X)=DX-2\sum_{i=0}^{N-2}\sum_{a=1}^3J_i^aXJ_{i+1}^a,\quad D=\sum_i n_i(n_i+2),
\]
has the exact **local-transfer** reduced matrix
\[
\boxed{\mathbb K_{(r,s),(p,q)}=D\delta_{rp}\delta_{sq}
-\frac{2}{L_p+1}\sum_{i,a,M,M'}
\langle r,M'|J_i^a|p,M\rangle
\langle q,M|J_{i+1}^a|s,M'\rangle.}\tag{1}
\]
The executable \`electric_restricted_local\` computes (1) directly from local path overlaps **without allocating dense original-Fourier generator matrices or full coupled-state generator matrices**. In four-face cases, it agrees exactly in ordinary precision with a separately built dense-coupled-generator version. **Caution:** the complete reduced inverse dimension \(\sum_J(\operatorname{mult}J)^2\) can still grow exponentially in width; this is not a polynomial-width full-inverse algorithm.

For the genuine alternating outer rank-one **untwirled** \(X_N=|+,-,+,-,\ldots\rangle\langle-,+,-,+,\ldots|\), with separate inner \(\chi_m\) and actual CG output compression \(B_{j,\ell}(X)=W^\dagger(X\otimes I_{m+1})W\), the corrected Poisson source before Haar projection is precisely the **one/two-bond collar**
\[
\boxed{
Z_{j,\ell}=\frac{3+m(m+2)-\ell(\ell+2)}2 B_{j,\ell}(X_N)
+\sum_{i\in\{j-1,j\}\cap[0,N-2]}\sum_a
[J_i^a B_{j,\ell}(X_N)J_{i+1}^a-B_{j,\ell}(J_i^aX_NJ_{i+1}^a)].
}\tag{2}
\]
Every untouched original-link bond cancels *exactly*. The actual gauge-invariant source \(Y=\mathcal T Z\) can be projected into its Schur matrix units **without any numerical Haar twirl**:
\[
\boxed{y_{pq}=\sum_M\langle p,M|Z_{j,\ell}|q,M\rangle,}\tag{3}
\]
because the test matrix unit is itself SU(2)-invariant. The collar consists of at most **7(m+1)** rank-one product tensors at an endpoint or **13(m+1)** at an interior site. Compressing each local ket/bra and contracting its MPS overlap produces (3), with no dense Fourier operator.

**Full four-face regression:** The *new* pipeline constructs both (1) and (3) from local CG contractions, solves the reduced 19×19 or 20×20 invariant matrix, and sums the multiplicity singular values. Across **all four sites, both output degrees, and m=3,4** it reproduces the completely independent P-71 dense physical source/inverse results to ordinary numerical accuracy:
\[
R_{4,3}=0.129125009533998,\quad R_{4,4}\approx0.1169833273515.
\]
Selected source overlaps agree with the independently dense q=0 Gauss/CG oracle at \(10^{-15}\)–\(10^{-14}\). These are not interval-certified, rational, or N≈m² *complete inverse* results.

### First exact **actual-source** coefficients at N≈m² (up to 400 faces)

For the maximal-total-spin path, of multiplicity one, a tensor product vector \(u=\bigotimes_i u_i\) has overlap
\[
A_K(u)=\frac{[x^K]\prod_i\left(\sum_{k=0}^{n_i}
\sqrt{\binom{n_i}{k}}u_i[k]x^k\right)}
{\sqrt{\binom{S}{K}}},\quad S=\sum_i n_i.
\]
Therefore for the rank-one collar terms \(Z=\sum_tc_t|u_t\rangle\langle v_t|\), the **actual corrected source** maximal-spin trace is exactly
\[
\boxed{\operatorname{tr}(P_{\max}Y)=\sum_tc_t\sum_{K=0}^S A_K(u_t)\overline{A_K(v_t)}.}\tag{4}
\]
An independent SymPy CG/collar implementation evaluated (4) in **exact rational/radical arithmetic**, with a separate numerical symmetric-spin polynomial contraction as a check. Fourteen physical source cases at \(N=10,16,36,100,400\) passed. Examples:
- (N,m,j,ell)=(10,3,0,2): \(-23/1540\); (10,3,5,4): \(-1/132\).
- (16,4,0,3): \(-361/875160\); (16,4,8,5): \(-7/36465\).
- (36,6,0,5): \(-12587/14102760256200\); (36,6,18,7): \(-43/111926668700\).
- (100,10,0,9): \(-148349/1120902837901218187949766844514160\).
- (400,20,0,19): \(-15503/61269470221931091170701758881844885546464537288625786274605224783664337944176829919193814195427635840644583267816575608800\), ~\(-2.53\times10^{-118}\).
- (400,20,200,21): \(-421/4128395255430118762216332800848119668964158107781213694217447288994525628143343539793297480310957367357718348760021642212\), ~\(-1.02\times10^{-118}\).

These are **selected maximal-total-spin source traces only**. Their smallness does **not** establish decay of the complete source trace norm, the full Schur nuclear sum, or the inverse at N=m². The entire invariant basis remains too large to invert by brute force at N=400. The polynomial-cost statement applies to **each selected coefficient** and its explicit rank-one source factors, not the full set of exponentially many paths.

## P-74 — Sharp neighboring half-Casimir weight for the gauge-invariant double commutator

The P-72 *actual interacting two-face SU(2)* Hamiltonian is \(H=4(C_1+C_2)+2\sum_aR_1^aL_2^a+\lambda(V_1+V_2)\), with \(V_i=-\chi_1(U_i)/2\). Let \(F=P_0\otimes I\), the **gauge-invariant** first-face spin-zero Casimir projection, and \(D=[V_1,P_0]\), a bounded finite-rank operator connecting vacuum to fundamental-spin states. The **first** interacting commutator is \([H,F]=\lambda D\otimes I\), bounded. The **second** is
\[
\boxed{\operatorname{ad}_H^2(F)=
\lambda(4[C_1,D]+\lambda[V_1,D])\otimes I
+2\lambda\sum_a[R_1^a,D]\otimes L_2^a.}\tag{5}
\]
Set \(Q_\beta=(1+C_2)^{-\beta}\). Each one-face coefficient in (5) is bounded, while \(L_2\) grows as the adjacent spin. Using the row/column operator Cauchy–Schwarz inequality and \(\sum_a(L_2^a)^2=C_2\) proves the **width- and spin-independent energy-weight bound**
\[
\boxed{\|\operatorname{ad}_H^2(F)Q_{1/2}\|\le
|\lambda|(4\|[C_1,D]\|+|\lambda|\|[V_1,D]\|)
+2|\lambda|\left(\sum_a\|[R_1^a,D]\|^2\right)^{1/2}.}\tag{6}
\]
Equivalently, for finite-energy domain vectors,
\(\|\operatorname{ad}_H^2(F)\psi\|\le B_\lambda\|(1+C_2)^{1/2}\psi\|\).
At an **interior** face the same derivation includes both adjacent links and a weight \((1+C_{i-1}+C_{i+1})^{-1/2}\).

**Critical optimality:** P-72's exact highest-weight neighbor-spin-s compression implies unweighted \(\|\operatorname{ad}_H^2(F)\|\ge|\lambda|s/2-B_\lambda\). On spin-s, \(C_2=s(s+1)\), so for **every β<1/2**,
\[
\boxed{\|\operatorname{ad}_H^2(F)(1+C_2)^{-\beta}\|\gtrsim
c_\lambda s^{1-2\beta}\to\infty.}\tag{7}
\]
Thus β=1/2 is the **sharp critical exponent** for this observable and this second commutator. Spin-matrix regressions at λ=.5,1,2, neighbor twice-spin 1…64, and β=.25,.5,.75 verify the expected growth/boundedness.

**Important:** P-74 does NOT restore point-norm-C² operator motion, construct an invariant interacting dynamical C*-algebra, prove uniform-in-time energy propagation, an infinite-volume generator or a uniform spectral gap. It identifies a local **energy-weighted graph norm at time zero** that is compatible with (not a contradiction of) P-72's ordinary norm-C² no-go.

## Next research gates

**Physical:** compress the actual source and its O(log m)-depth corrected electric iterates without enumerating the full fusion-path multiplicity algebra; use P-67's dimension-free trace-ideal inverse remainder and obtain an actual complete N~m² nuclear response asymptotic.

**Interacting dynamics:** formulate a gauge-compatible representation/energy-weighted dynamical algebra controlled by the sharp half-Casimir power, establish graph-norm propagation and a common generator core, then study a uniform spectral gap.

**Borel/OS and 4D continuum Yang–Mills existence and mass gap: OPEN.**