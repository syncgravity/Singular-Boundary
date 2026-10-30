# The Singular Boundary — Universal SU(2) link-spin resolution and eight-face ground-state exclusion

**Research date:** 2026-10-29. **Program:** R3 independent reconstruction. **Classification:** exact, nonperturbative finite-volume, all-vertex Gauss-invariant SU(2) Wilson theorems. **Scope:** any finite simply connected rhombus disk with a retained magnetic plaquette and one of its links, *regardless of connectedness, reflection, and relative-color intertwiners*. The stronger seven-plaquette exclusion applies to the previously declared 35-state eight-face Galerkin subspace. Neither theorem computes the true eight-face cap response or establishes a Penrose continuum mass gap.

## 1. Hamiltonian and strong-field energy budget

Fix a finite planar cell complex with normalized product Haar measure on all links. Let

\[
H_b=\sum_{e\in E}a_e(-\Delta_e)+b\sum_{q\in Q}c_q(1-p_q),\quad
p_q=\tfrac12\operatorname{Tr}W_q,\quad a_e,c_q>0,
\]

where the target face may be absent from Q. The group metric is normalized by `-Delta chi_j=j(j+1)chi_j`. The finite, strictly positive all-vertex Gauss-invariant normalized ground state is \(\Omega_b\). Put \(A_q=\sum_{e\in\partial q}a_e\). The previously established simultaneous gauge-invariant Wilson exponential trial has

\[
0\le E_0(H_b)\le C_Q\sqrt b,\qquad
C_Q=\frac{3}{2\sqrt2}\sum_{q\in Q}\sqrt{A_qc_q}.\tag{U1}
\]

Since every magnetic term is nonnegative, for each retained face \(q\) and for the whole retained set,

\[
\boxed{\langle d_q\rangle_{\Omega_b^2}\le\frac{C_Q}{c_q\sqrt b},\qquad
\left\langle\sum_{q\in Q}d_q\right\rangle_{\Omega_b^2}\le\frac{C_Q}{c_{\min}\sqrt b}.}\tag{U2}
\]

These are properties of the *true interacting physical ground state*, not the 35-state Ritz vector.

## 2. Exact SU(2) Peter–Weyl small-cap concentration

Fix any link e, write U_e=x and all remaining variables y. Let \(P_{J,e}\) be the **complete** orthogonal projector onto SU(2) link irreducible representations \(j\le J\) in the x variable, retaining *every matrix coefficient and arbitrary y dependence*. It commutes with the Gauss constraints since each link Casimir commutes with left and right vertex actions. Write \(N=\lfloor2J\rfloor\) and

\[
D_J=\sum_{n=0}^N(n+1)^2=\frac{(N+1)(N+2)(2N+3)}6.\tag{U3}
\]

For fixed y, the normalized Peter–Weyl matrix coefficients \(\sqrt{d_j}D^j_{mn}(x)\) are orthonormal and the sum of their absolute squares at **every** x is precisely \(D_J\). Cauchy–Schwarz therefore proves

\[
|\varphi(x,y)|^2\le D_J\int_{SU(2)}|\varphi(z,y)|^2 dz
\quad\text{for every }\varphi=P_{J,e}\varphi.\tag{U4}
\]

Choose any retained face q incident to e, and define \(B_{q,\delta}=\{1-p_q\le\delta\}\). For each fixed y the map x↦W_q is a Haar-preserving left/right translation, possibly composed with inversion. Its cap therefore has Haar volume

\[
H(\delta)=\frac{\arccos(1-\delta)-(1-\delta)\sqrt{2\delta-\delta^2}}{\pi},\quad0\le\delta\le2.
\]

Integrating U4 over the conditional cap gives the **operator concentration inequality**

\[
\boxed{\|1_{B_{q,\delta}}\varphi\|^2\le D_JH(\delta)\|\varphi\|^2\quad(\varphi\in\mathrm{ran}\,P_{J,e}).}\tag{U5}
\]

This includes arbitrary noncommuting joint spin networks, intertwiners, and color orientations. For \(0<\delta\le1\), the exact Haar radial density gives

\[
\boxed{H(\delta)\le C_H\delta^{3/2},\quad C_H=\frac{4\sqrt2}{3\pi}.}\tag{U6}
\]

## 3. Gap-free overlap with the *actual* strongly coupled ground state

For every normalized \(\varphi\in\mathrm{ran}\,P_{J,e}\), split the overlap into the cap and its complement and apply Cauchy–Schwarz separately. U5 bounds the low-spin probability of the cap, while U2 and Markov bound the true ground state's mass outside it. Taking the supremum over all such \(\varphi\) yields the **exact physical** bound

\[
\boxed{\|P_{J,e}\Omega_b\|\le
\min\!\left\{1,\sqrt{D_JH(\delta)}+
\sqrt{\frac{C_Q}{c_q\delta\sqrt b}}\right\},\qquad0<\delta\le2.}\tag{U7}
\]

For every fixed J and b≥1, set \(\delta=b^{-1/5}\) and use U6:

\[
\boxed{\|P_{J,e}\Omega_b\|\le
\left(\sqrt{D_JC_H}+\sqrt{C_Q/c_q}\right)b^{-3/20}.}\tag{U8}
\]

Thus the exact nonlinear ground state becomes asymptotically orthogonal to **every fixed link-spin truncation**, even after including all its relative-color channels.

For a **quantitative necessary cutoff**, suppose \(\|P_{J,e}\Omega_b\|\ge\eta>0\), and assume b is large enough that \(\delta_\eta=4C_Q/(\eta^2c_q\sqrt b)\le1\). U7 and U6 imply

\[
\boxed{D_J\ge\frac{\eta^5}{32C_H}
\left(\frac{c_q}{C_Q}\right)^{3/2} b^{3/4}.}\tag{U9}
\]

Since \(D_J\le(N+2)^3\), this proves

\[
\boxed{N+2\ge\left[\frac{\eta^5}{32C_H}
\left(\frac{c_q}{C_Q}\right)^{3/2}\right]^{1/3}b^{1/4},\qquad J=\tfrac N2.}\tag{U10}
\]

The necessary scale \(J=\Omega(b^{1/4})\) is now proved for **any complete physical joint spin-network truncation with link-spin bound J**, not just the earlier individual-plaquette-character product truncation. It is a *necessary* condition for nonvanishing ground-state overlap, not a sufficient condition for reproducing the full spectrum or cap probability. The result extends directly to the complete electric spectral shell \(P_M=1_{T\le M}\): every state in this shell has \(j_e(j_e+1)\le M/a_e\), so retaining a fixed nonzero true-ground overlap requires \(M=\Omega(\sqrt b)\) for bounded positive a_e.

## 4. Stronger exclusion of the *specific* 35-state connected eight-face Ritz space

Use exactly the eight-face fixture from R3-IR-406–412: seven retained faces Q, 22 original links, 29 trace monomials containing at most two fundamental plaquettes and six pairwise-color vectors \(\zeta_{qr}=4D_{qr}/\sqrt3\). Their joint 35-dimensional physical space \(\mathcal V_{35}\) has an **orthonormal kinematic Haar basis** \(\psi_i\). Every basis function satisfies \(|\psi_i|\le4\) pointwise: traces of spin 1/2 have norm at most 2, and \(|D_{qr}|\le1\). Thus

\[
\sum_{i=1}^{35}|\psi_i(U)|^2\le560,
\quad \|\varphi\|_{L^\infty}\le\sqrt{560}\|\varphi\|_{L^2}
\quad(\varphi\in\mathcal V_{35}).\tag{U11}
\]

For fixed delta, let \(A_\delta=\bigcap_{q\in Q}\{d_q\le\delta\}\). Under **kinematic** product Haar, all seven based plaquette holonomies are independent SU(2) Haar, so \(m(A_\delta)=H(\delta)^7\). Hence for normalized \(\varphi\in\mathcal V_{35}\),

\[
\|1_{A_\delta}\varphi\|^2\le560H(\delta)^7.
\]

Meanwhile, U2 and Markov give \(\|1_{A_\delta^c}\Omega_b\|^2\le C_Q/(c_{\min}\delta\sqrt b)\). Take the supremum over \(\varphi\in\mathcal V_{35}\). For every delta in (0,1] this proves

\[
\boxed{\|P_{35}\Omega_b\|\le
\sqrt{560}\,C_H^{7/2}\delta^{21/4}
+\sqrt{C_Q/c_{\min}}\,b^{-1/4}\delta^{-1/2}.}\tag{U12}
\]

Setting \(\delta=b^{-1/23}\) yields the **quantitative strong-field ground-space exclusion**

\[
\boxed{\|P_{35}\Omega_b\|\le
\bigl(\sqrt{560}C_H^{7/2}+\sqrt{C_Q/c_{\min}}\bigr)b^{-21/92}
\longrightarrow0.}\tag{U13}
\]

Thus the Ritz-space ground-state **overlap** fails, not merely its energy approximation: \(\|P_{35}\Omega_b\|^2=O(b^{-21/46})\). At the refinement convention b=h^-2, \(\|P_{35}\Omega_h\|=O(h^{21/46})\). These are exact bounds with explicit fixed eight-face constants, and they hold for *all* normalized vectors in the 35-state subspace, not just the computed Ritz minimum.

The seven-face event argument uses kinematic face-coordinate Haar independence, not independence in the **true interacting ground state**. Its valid use is only to bound the L2 mass of fixed finite-dimensional Ritz vectors.

## 5. Verification and limits of applicability

The executable verifier computes the exact Peter–Weyl diagonal \(D_J\), checks cap concentration for arbitrary normalized finite SU(2) character combinations by deterministic radial Haar quadrature, and diagonalizes a **true nonlinear continuous-SU(2) Wilson class rotor** over magnetic couplings b=16,...,16384. For each coupling it checks the ground-state magnetic-energy bound and rigorous link-bandlimited overlap upper bound. It separately checks U9–U13 algebraically with the exact declared eight-face coefficients, runs the previous actual eight-face 35-state matrix regression, and verifies the old package checksums. The rotor is only a local numerical benchmark, **not** a connected eight-face SU(2) spectral computation.

**PROVED:** U1–U13 under the explicitly stated finite-model and fixed-coefficient hypotheses. **NOT PROVED:** an eight-face full-electric-shell diagonalization or validated cap expectation, a uniform reflection-free Penrose deleted-face probability, the late signed center-even mixed response, full bulk magnetic deletion, fixed-support covariance, regulator-uniform physical mass gap, quartic resolvent or continuum reconstruction.

## 6. Universal magnetic compression bound (all joint intertwiners)

The previous link-bandlimited cap concentration U5 also gives a **direct form lower bound** for every normalized physical or unreduced state with \(j_e\le J\) on some link \(e\in\partial q\), entirely independently of the ground state. Take

\[
\delta_J=(2C_HD_J)^{-2/3}\in(0,1),
\quad D_J=\sum_{j\le J}(2j+1)^2.
\]

By U5–U6, at most one half of the state's probability lies in the face cap \(\{d_q\le\delta_J\}\). Thus

\[
\langle d_q\rangle_\varphi\ge \delta_J\mathbb P_\varphi(d_q>\delta_J)
\ge\tfrac12(2C_HD_J)^{-2/3}.\tag{U14}
\]

Let \(P_J^{\rm all}\) denote the **complete physical** projection onto spin-network links with \(j_e\le J\) for every link, including *all admissible vertex intertwiners*. Every retained plaquette may use any of its four links in U14. Adding the positive magnetic terms gives the **universal nonclass form estimate**

\[
\boxed{P_J^{\rm all}H_bP_J^{\rm all}
\ \ge\ \frac{b\sum_{q\in Q}c_q}{2(2C_HD_J)^{2/3}}P_J^{\rm all}.}\tag{U15}
\]

This also holds for every smaller subspace within the complete link-spin cutoff. The bound is independent of reflection, the number of color channels, recoupling details, connectedness, or magnetic frustrations. Since \(D_J\asymp(J+1)^3\), U15 grows at least as \(b/(J+1)^2\) for a fixed finite patch. Combining with the **true** full-Wilson variational energy upper bound U1 shows directly: if a sequence of complete link-cutoff Ritz energies is to approach the true \(O(\sqrt b)\) energy scale, it is necessary that \(J=\Omega(b^{1/4})\). This is an independent energy-based proof of U10 and extends the earlier product-character Jacobi-matrix necessity to **all** joint spin-network bases.

**Volume-uniform necessary resolution in bounded-geometry refinements.** If a growing Penrose disk has \(F\) retained faces, all satisfying \(A_q\le4a_+\) and \(c_-\le c_q\le c_+\), then \(\sum_qc_q\ge Fc_-\) whereas the exact nonlinear variational coefficient satisfies \(C_Q\le rac{3}{\sqrt2}F\sqrt{a_+c_+}\). Therefore the ratio of the extensive lower bound U15 to the extensive upper bound U1 eliminates \(F\). Any complete link-spin-bounded trial space whose Ritz energy lies at or below the known \(C_Q\sqrt b\) energy scale still requires \(J=\Omega(b^{1/4})\) with a constant **independent of total face count**. This is a volume-uniform **necessary computational spin resolution**, not a volume-uniform lower bound on deleted cap mass or the physical spectral gap. In contrast, the *single-face ground-overlap* bound U7–U10 uses \(C_Q\) and its coefficient deteriorates with growing \(F\), unless a separate local energy budget is proved.

The compression bound is a **necessary resolution theorem**, not a sufficient Ritz-gap or center-cap certificate. It gives no sign information about the deleted-face connected low-energy response.

## 7. Complete low-link-spin Hilbert-space enumeration for the eight-face graph

For the 15-vertex, 22-link, eight-face simply connected open square-rhombus graph, restrict every original link to \(j_e\in\{0,1/2\}\). SU(2) Gauss invariance at each vertex requires an even number of incident fundamental links. Such a link occupation is an Eulerian \(\mathbb F_2\) 1-cycle. Because the cell complex is a disk, its cycle space has exact dimension \(E-V+1=8\), and all occupations are the distinct XOR sums of its eight face boundaries: **256 configurations**.

At each vertex incident to exactly two fundamental edges, the singlet intertwiner is unique. At a vertex with four occupied fundamental edges, the intertwiner multiplicity is exactly two, because the SU(2) invariant space in \((1/2)^{\otimes4}\) has dimension two. For a cycle occupation x with \(n_4(x)\) four-occupied vertices, its full physical intertwiner multiplicity is \(2^{n_4(x)}\). Exact exhaustive graph enumeration gives

| Number of four-occupied vertices | Edge-spin occupations | Multiplier | Physical states |
| ---: | ---: | ---: | ---: |
| 0 | 161 | 1 | 161 |
| 1 | 68 | 2 | 136 |
| 2 | 22 | 4 | 88 |
| 3 | 4 | 8 | 32 |
| 4 | 1 | 16 | 16 |
| **Total** | **256** | | **433** |

The canonical target-center-flux transformation acts on each occupation by \((-1)^{s_f}\), where \(s_f\in\mathbb F_2\) is the coefficient of the central face boundary in its unique face-cycle decomposition. Keeping intertwiner multiplicities, the complete physical \(j_e\le1/2\) space splits into

\[
\boxed{\dim\mathcal H_{J=1/2}=433,
\quad\dim\mathcal H_{J=1/2,C_f=+}=246,
\quad\dim\mathcal H_{J=1/2,C_f=-}=187.}\tag{U16}
\]

These are **exact spin-network basis dimensions**, not approximations to the full SU(2) Hilbert space. All original links and vertex constraints are counted. The fundamental cutoff is already a tractable finite matrix size, but its magnetic action reaches omitted spin-1 edges. The older 35-state space is **not literally a subspace of this fundamental cutoff**, because some of its pairwise relative-color vectors have link spin 1 on their shared edge. It is nevertheless dramatically smaller and lacks globally connected response channels. The 433-dimensional complete \(j_e\le1/2\) sector can serve as the first **genuine** joint-intertwiner matrix benchmark once its exact electric Casimirs and Wilson plaquette recoupling coefficients are implemented. No such full 433×433 Hamiltonian was diagonalized in this turn.

**Revised next mathematical gate:** construct exact plaquette-fusion (Wigner-symbol) matrices on the 433-state full fundamental shell and an explicit surrounding spin-1 shell; certify the magnetic off-shell couplings, then grow the original-link spin cutoff according to U9–U15. A genuine signed cap and mass-gap result still requires the spectral and connected-geometry estimates absent from these shell dimensions.
