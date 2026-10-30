# The Singular Boundary — Exact 433-state SU(2) Wilson magnetic recoupling and first-shell cap audit

**Research date:** October 29, 2026. **Program:** R3 independent reconstruction. **Geometry:** 3×3 square-rhombus disk with corner (0,0) removed, central face (1,1) magnetically deleted; 8 faces, 22 links, 15 vertices, 7 retained magnetic terms. **Classification:** exact finite-dimensional *Galerkin matrices* of the continuous-SU(2), Gauss-invariant Wilson Hamiltonian; double-precision Ritz eigensolutions and a symbolic target-character spectrum. **Important:** this is not a spectral certification for the full continuous-SU(2) Hamiltonian, nor a Penrose-refinement or mass-gap result.

## A. New calculation and full magnetic matrix

Let \(\mathcal H_{1/2}\) be the **complete physical** subspace containing all original-link irreducible representations \(j_e\in\{0,\frac12\}\), including every SU(2) intertwiner. The link occupations are precisely the \(2^8=256\) mod-2 cycles of the eight-face disk. A two-valent occupied vertex has one normalized singlet intertwiner; a four-valent occupied vertex has two. Their exact multiplicities give \(\dim\mathcal H_{1/2}=433\), with 246 target-center-even and 187 center-odd states.

For any occupation \(m\) and orthonormal vertex intertwiner label \(\alpha\), the basis wavefunction is obtained by contracting the tensors \(I_v^{(\alpha)}\) with normalized fundamental link coefficients \(\sqrt2 D^{1/2}(U_e)\). Its electric energy is exactly

\[T_{m,\alpha}=\frac34\sum_{e:m_e=1}a_e.\]

For each plaquette \(q\), the fundamental Wilson multiplier is \(p_q=\chi_{1/2}(W_q)/2\). Its **exact compressed matrix** \(M_q=P_{1/2}p_qP_{1/2}\) is obtained without Monte Carlo by contracting vertex singlets and SU(2) Haar link integrals. The only nontrivial building blocks are

\[\int (\sqrt2\,\overline U_{ab})(\sqrt2 U_{cd})\,dU=\delta_{ac}\delta_{bd},\qquad
\int(\sqrt2 U_{ab})(\sqrt2 U_{cd})\,dU=\epsilon_{ac}\epsilon_{bd}.\]

For basis occupations \(m,n\), center parity at each link gives the exact **support rule**

\[\boxed{\ (M_q)_{n,m}=0\quad\text{unless}\quad n=m\mathbin{\oplus}\partial q\ }.\]

The remaining matrix element factorizes into at most four explicit vertex contractions (plus identity inner products elsewhere). The code retains all 433 intertwiners, not just products of face traces. All seven retained \(M_q\) are real symmetric with algebraic entries in \(\mathbb Q(\sqrt3)\). Their nonzero-entry counts are respectively 420, 492, 420, 420, 492, 420, 374 (sum **3,038**); the additional target matrix contains 400 entries. The vacuum-to-single-face matrix element is exactly \(\langle\chi_{1/2}(W_q),p_q\cdot1\rangle=1/2\), and every retained matrix preserves target-center parity. The full physical **Galerkin** Hamiltonian is

\[\boxed{H_{433}(b)=\operatorname{diag}\!\left(\tfrac34\sum_{e\in m}a_e\right)+b\sum_{q\ne f}c_q(I-M_q).}\]

No assertion is made that \(P_{1/2}H P_{1/2}\) is an invariant restriction of \(H\); the magnetic terms couple it to omitted spin-one channels.

## B. Numerical Ritz spectrum and a rigorous failure test

For the same asymmetric coefficients as the earlier 35-state test, \(a_e=0.8+0.07(i\bmod6)+0.013(i\bmod3)\) in the canonical sorted-link order and \(c_q=0.78+0.09k\) in canonical sorted retained-face order, the complete 433-state matrices give:

| b | Lowest Ritz eigenvalue | Second-lowest Ritz eigenvalue | Ritz gap | Seven-channel residual lower bound | Rigorous upper bound on true \(E_0\) |
|---:|---:|---:|---:|---:|---:|
| 1 | 6.72388386 | 9.54252002 | 2.81863616 | 0.22454024 | 15.04216812 |
| 4 | 23.02060267 | 27.17157901 | 4.15097635 | 1.41030923 | 30.08433625 |
| 16 | 81.14161151 | 92.30975452 | 11.16814301 | 4.86523183 | 60.16867250 |
| 64 | 309.68796348 | 348.11226131 | 38.42429782 | 17.68372091 | 120.33734500 |

The first two numerical columns are **Ritz eigenvalues only**. For \(b=16\), the projected ground energy exceeds a rigorous variational upper bound for the true ground energy by at least \(20.97294\); at \(b=64\), by at least \(189.35062\). Hence even the **complete fundamental shell** is quantitatively inadequate for a full-Hilbert ground-state certificate at these couplings. The 35-state space and this 433-state space are **not nested** (the earlier 35-state space includes selected spin-one links), so their ground-energy ordering need not be monotone.

### Explicit true outgoing-residual lower bound

Let \(\varphi_b\) be the normalized lowest eigenvector of \(H_{433}(b)\) and let \(X_q=\chi_{1/2}(W_q)\), \(Y_q=\chi_1(W_q)\) for each of the seven retained faces. The \(Y_q\) are mutually orthonormal and lie outside the J=1/2 link-spin shell. The previous exact Wilson fusion identity gives

\[\langle Y_q,(1-P_{1/2})H\varphi_b\rangle=-\frac{bc_q}{2}\langle X_q,\varphi_b\rangle.\]

Thus, **rigorously for the computed Ritz vector** (up to the displayed numerical eigensolution tolerance),

\[\boxed{\ \|(1-P_{1/2})H\varphi_b\|\ \ge\ \frac b2\left[\sum_{q\ne f}c_q^2|\langle X_q,\varphi_b\rangle|^2\right]^{1/2}.\ }\]

The bound is nonzero at every tested coupling. It is not the *complete* outgoing residual, and neither it nor the projected Ritz gap supplies a full-Hilbert spectral-separation certificate.

## C. Exact target spin-one compression and Haar cap formula

A second, independent SU(2) Haar contraction computes \(C=P_{1/2}\chi_1(W_f)P_{1/2}\) from the **fourth** fundamental-link moment. The rank-four Haar projector has two invariant intertwiner channels. The formula \(\chi_1=\chi_{1/2}^2-1\) then produces a 433×433 real-symmetric matrix with only 144 nonzero entries, supported on the **81 states occupying all four target boundary links**.

The entries lie in \(\mathbb Q(\sqrt3)\). The companion **symbolic** calculation checks an exact annihilating polynomial

\[\boxed{\ x(x-1)(3x+1)(9x-1)(27x+1)(81x-1)\ }\]

on every nonzero occupation block. The resulting **exact spectrum**, including the 352-dimensional nullspace, is

| Eigenvalue | Multiplicity |
|---:|---:|
| \(-1/3\) | 32 |
| \(-1/27\) | 8 |
| 0 | 352 |
| \(1/81\) | 1 |
| \(1/9\) | 24 |
| 1 | 16 |

so \(\|C\|=1\) exactly. A reconstructed state \(\chi_{1/2}(W_f)\chi_{1/2}(W_{\partial S})\) is unit normalized and has \(\langle C\rangle=1\) exactly, reproducing the previously proved non-Haar witness in the full 433-state basis.

For **any** target-center-even state \(\varphi\in\mathcal H_{1/2}\), the target holonomy marginal is central and its only possible nonconstant character is spin one: higher integer-spin characters cannot have matrix elements between link spins 0 and 1/2. Writing \(c_1=\langle\varphi,C\varphi\rangle\) gives the *exact* density and cap probability

\[\frac{d\nu_\varphi}{dU_f}=1+c_1\chi_1(U_f),\]
\[\boxed{\ \Pr_\varphi(B_a)=H(a)+\frac{c_1}{\pi}\left(\frac12\sin2a-\frac14\sin4a\right),\quad H(a)=\frac{a-\frac12\sin2a}{\pi}.\ }\]

Let \(w_f(\varphi)\) denote its squared projection onto the 81 states with all four target edges occupied. The support property and exact \(\|C\|=1\) yield the **rigorous finite-shell bound**

\[\boxed{\ |c_1|\le w_f(\varphi),\qquad \Pr_\varphi(B_a)\ge [1-3w_f(\varphi)]_+H(a).\ }\]

For the four Ritz ground vectors, the respective \(w_f\) values are \(3.46961\times10^{-7}\), \(4.82871\times10^{-4}\), \(0.00606225\), and \(0.01143670\). The **numerically computed** spin-one coefficients are smaller than \(10^{-17}\) in every tested case, so these Ritz target marginals are Haar **to the accuracy of the finite calculation**. This is not a proven exact zero for arbitrary coefficients and, crucially, **not a claim about the true strongly coupled ground state**. Tests with several additional randomly asymmetric couplings reproduced this numerical cancellation; the separately constructed non-Haar winding state shows that it is not enforced merely by basis membership.

## D. Reproducibility and formal limitation

The package includes (1) a generator of the exact 433-dimensional matrix using SU(2) normalized Haar two-point contractions and a complete orthonormal intertwiner basis; (2) a generator of the target spin-one matrix using four-point Haar projectors; (3) an independent verifier of the saved matrices, SU(2) Haar second moments via the quaternion subgroup's exact degree-two cubature, center parity, Ritz residuals, and the seven outgoing channels; (4) a symbolic \(\mathbb Q(\sqrt3)\) proof certificate of the target spin-one operator spectrum; (5) all eight plaquette matrices, target spin-one matrix, spin-network occupation basis, Ritz vectors, numerical output logs and SHA-256 manifest. No stochastic simulation is used.

**What is completed:** the **actual full 433×433 fundamental-shell Wilson magnetic recoupling** and its Ritz spectrum; explicit first-state outgoing residual lower bounds; exact projected spin-one/cap formula and its symbolically certified spectrum. **What remains open:** a higher-spin, genuinely full-coupling eight-face **true-ground-state** spectral gap and cap certificate, quantitative signed response for arbitrary connected asymmetric Penrose deleted faces, regulator-uniform gap, fixed-support covariance, quartic resolvent and continuum reconstruction. The eight-face square test disk is not an actual Penrose tiling fixture.
