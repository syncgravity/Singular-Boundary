# The Singular Boundary — Simultaneous seven-plaquette spin occupation and higher-spin Ritz obstruction

**Research date:** 2026-10-29. **Project:** R3 independent reconstruction. **Geometry:** the connected eight-face square-rhombus disk with southwest corner absent, center target face `(1,1)` magnetically deleted; seven retained Wilson plaquettes, 22 edges and 15 vertices. **Classification:** rigorous finite, full-Haar SU(2) Wilson Hamiltonian inequalities, exact Galerkin recoupling of 433 states plus arbitrarily long *single-plaquette* spin towers, and deterministic finite-dimensional Ritz numbers. **NOT PROVED:** the physical eight-face deleted cap probability, a true-ground-state Ritz residual/gap certificate, a regulator-uniform Penrose result, or a continuum Yang–Mills mass gap.

## 1. Exact model and additional physical trial space

Let

\[
H_b=\sum_{e\in E}a_e(-\Delta_e)+b\sum_{q\in Q}c_q[1-p_q],\qquad
p_q=\tfrac12\operatorname{Tr}W_q,\quad |Q|=7,\quad a_e,c_q>0.
\]

The target center face has **no** magnetic term. Each of the seven retained faces has a distinct outer-boundary primal link \(e_q\) belonging to no other retained face. Let \(\mathcal H_{1/2}\) be the *complete* 433-state physical spin-network shell with every original link spin at most 1/2. Define the finite-dimensional, nested **single-face-tower** space

\[
\mathcal R_J=\mathcal H_{1/2}+\operatorname{span}\{\chi_j(W_q): q\in Q,\;j=1,\tfrac32,\ldots,J\},\qquad J\in\tfrac12\mathbb N,\ J\ge1.
\]

The added character vectors are gauge invariant and Haar orthonormal among themselves and orthogonal to \(\mathcal H_{1/2}\). They carry spin \(j\ge1\) on the four edges of exactly one retained face; they therefore never have high spin on more than one of the seven selected outer links. This definition is a *subspace*, not an assertion of invariance under the full Hamiltonian.

## 2. Exact 433-plus-tower matrix theorem (HT-1)

For each retained plaquette \(q\), the character fusion identity on SU(2) gives

\[
p_q\chi_j(W_q)=\tfrac12\chi_{j-1/2}(W_q)+\tfrac12\chi_{j+1/2}(W_q),\qquad
T\chi_j(W_q)=j(j+1)A_q\chi_j(W_q),\quad A_q=\sum_{e\in\partial q}a_e.
\]

Thus the added tower has electric diagonal \(A_qj(j+1)\), and neighboring tower levels couple with magnetic matrix element \(-bc_q/2\). The **only** magnetic matrix element between a tower and the original 433-state shell is

\[
\boxed{\langle\chi_1(W_q),H_b\chi_{1/2}(W_q)\rangle=-bc_q/2.}
\]

All other shell–tower entries vanish: a private outer link of \(q\) has tower spin at least 1, while every shell state carries spin at most 1/2 on that link, and the fundamental plaquette multiplier can change it by 1/2 only when the multiplier is on \(q\). Different face towers cannot couple in one Wilson insertion because each has its own private outer link. Electric Laplacians are diagonal in original-link spins and likewise cannot couple these sectors.

Consequently the **entire** \(\dim\mathcal R_J=433+7(2J-1)\) Galerkin matrix is determined by the eight verified 433 magnetic matrices, seven independent tridiagonal towers, and seven exact connecting entries. No Monte Carlo or fitted recoupling coefficients are used. The existing 433 target-center parity commutes with all added retained-face couplings. The omitted pure-character channel \(\chi_{J+1/2}(W_q)\) gives the exact residual component \(-bc_q\langle\chi_J(W_q),\varphi_J\rangle/2\), but these seven components are **not the complete off-block residual**.

## 3. Correct strong-field scale in a simultaneous seven-face class Ritz space (HT-2)

On a planar simply connected full-link disk, a gauge-fixing change of variables has independent normalized-Haar face holonomies. Products of *central* functions of the retained face holonomies are gauge invariant. For \(\psi=\prod_{q\in Q}g_q(W_q)\), mixed electric-gradient expectations between different faces vanish under the independent central face-Haar integrals: their relative-color gradient contractions are centered conditionally on the face conjugacy classes. Therefore, restricted to the product-class character span, the **exact** projected Hamiltonian is the Kronecker sum of seven individual radial SU(2) Wilson rotors:

\[
\boxed{P_{\mathrm{class}}H_bP_{\mathrm{class}}=\sum_{q\in Q}\left[A_q\,j_q(j_q+1)+bc_q-\tfrac{bc_q}{2}(S_q+S_q^*)\right].}
\]

Here \(S_q\) shifts the SU(2) character spin by \(1/2\), and the finite product-class span includes all joint character products with \(0\le j_q\le J\). Thus its dimension is \((2J+1)^7\) and its **exact finite Galerkin ground energy** is the sum of the seven lowest one-face tridiagonal eigenvalues. In particular, the infinite product-class variational family supplies the valid physical upper bound

\[
\boxed{E_0(H_b)\le E_{\mathrm{prod}}(b)=\sum_qE_0(A_q(-\Delta)+bc_q(1-p))=O(\sqrt b),}
\]

for this fixed seven-face patch. This is a Ritz *upper bound*, not the true eigenvalue and not a small-ball certificate. Every product-class trial omits dependence on the deleted target face coordinate and consequently has an **exact Haar target marginal**. A correct strong-field energy scale by itself cannot prove the connected-face cap assertion.

## 4. New no-go theorem for *every* single-face tower cutoff (HT-3)

Fix one private outer link \(e_q\) for each retained face and let \(L_q=P_{\le1/2,e_q}\) be the original-link Peter–Weyl projector onto spins 0 and 1/2. These seven commuting projectors are defined on the full physical Hilbert space, commute with vertex Gauss operators, and are independent of the magnetic couplings. On \(\mathcal R_J\), the number of selected outer links with spin *above* 1/2 is at most one, **regardless of how large J is**. More generally let \(\mathcal R_k^{\rm out}\) be any physical spin-network subspace in which at most \(k<7\) of these seven outer links have spin above 1/2. For every normalized \(\psi\in\mathcal R_k^{\rm out}\),

\[
\sum_{q\in Q}\|L_q\psi\|^2\ge7-k.
\]

Let \(d_q=1-p_q\), and let \(H_{\mathrm{SU2}}(\delta)=[\arccos(1-\delta)-(1-\delta)\sqrt{2\delta-\delta^2}]/\pi\) be the Haar mass of the \(d_q\le\delta\) cap. The one-link reproducing kernel has dimension \(D_{1/2}=1^2+2^2=5\). The exactly valid one-link concentration estimate, for every physical normalized \(\psi\) and every \(\delta\in(0,2)\), is

\[
\boxed{\|L_q\psi\|\le\sqrt{5H_{\mathrm{SU2}}(\delta)}+
\sqrt{\langle\psi,d_q\psi\rangle/\delta}.}
\]

**Proof.** With other link values fixed, the target cap is a Haar translate or inversion of an SU(2) cap in the link \(e_q\). The Hilbert–Schmidt norm of the low-spin projector followed by cap restriction is exactly \(\sqrt{5H(\delta)}\), uniformly in the remaining links. Split \(\psi\) into the cap and its complement and use the operator-norm bound on the first part and \(\mathbf1_{d_q>\delta}\le d_q/\delta\) on the second. No gap or symmetry is assumed.

Set \(z_q=\|L_q\psi\|\), \(x=\sqrt{5H(\delta)}\), \(m_q=\langle d_q\rangle\). Since \(m_q\ge\delta(z_q-x)_+^2\) and \(z_q^2\le2(z_q-x)_+^2+2x^2\),

\[
\boxed{\sum_{q\in Q}m_q\ge
\delta\big[(7-k)/2-35H_{\mathrm{SU2}}(\delta)\big]_+.}
\]

Taking \(\delta=1/32\), the bracket is positive **even for k=6**. With \(c_-=\min c_q\) and \(T\ge0\), obtain the *strictly extensive in b* spectral compression bound

\[
\boxed{\inf_{\substack{\psi\in\mathcal R_k^{\rm out}\\\|\psi\|=1}}
\langle\psi,H_b\psi\rangle\ge
bc_-\,\frac1{32}\big[(7-k)/2-35H_{\mathrm{SU2}}(1/32)\big]>0,\quad k\le6.}
\]

In particular, for **every** finite or infinite tower order \(J\), the full \(433+\)single-face-character-tower Ritz energy is bounded below by \(0.0901404698\,c_- b\), whereas the true ground energy is at most \(E_{\rm prod}(b)=O(\sqrt b)\). This proves that adding arbitrarily high single-face towers **can never certify the strong-coupling ground state**. A necessary physical basis feature is **simultaneous high spin on all seven chosen outer boundary links**.

## 5. Quantitative true-ground overlap exclusion (HT-4)

Let \(\Omega_b\) be the normalized *true* finite SU(2) ground state. Its positive magnetic energy satisfies

\[
\sum_qc_q\langle d_q\rangle_{\Omega_b}\le E_0(H_b)/b\le C/\sqrt b.
\]

Hence for each selected outer link and \(\delta=b^{-1/5}\), the one-link concentration estimate and \(H(\delta)\le C_H\delta^{3/2}\) imply

\[
\boxed{\|L_q\Omega_b\|=O(b^{-3/20})}\quad(q\in Q).
\]

Let \(P_{\rm not\ all\ high}\) be the projector onto the physical span of spin networks where **at least one** of the seven selected outer links has spin at most 1/2. Since the seven link-spin projectors commute,

\[
\boxed{\|P_{\rm not\ all\ high}\Omega_b\|^2
\le\sum_{q\in Q}\|L_q\Omega_b\|^2=O(b^{-3/10}).}
\]

Thus the true strong-field wavefunction becomes asymptotically orthogonal to **every** subspace with at most six of the seven selected links at spin above 1/2, including the entire infinite union of the spaces \(\mathcal R_J\). This is a much stronger exclusion than any particular Ritz energy comparison. More generally, for link cutoff \(J_b\) satisfying \((J_b+1)^4/b\to0\), applying the same argument with \(D_{J_b}\asymp(J_b+1)^3\) and \(\delta=b^{-1/5}(J_b+1)^{-6/5}\) shows that all seven selected outer links have spin **greater than** \(J_b\) with probability \(1-o(1)\).

**Uniformity limit:** the displayed constants use the **fixed seven-face** variational constant C. They are not automatically uniform over a growing Penrose disk or sufficient to bound a deleted-face center cap.

## 6. Deterministic numerical checks, coefficients, and limitations

The exact 433 magnetic matrices and basis are reused from the preceding verified archive; no new recoupling integrals are fitted. Electric coefficients are in canonical sorted original-link order: \(a_e=0.8+0.07(i\bmod6)+0.013(i\bmod3)\); retained magnetic ratios are \(c_k=0.78+0.09k\). The standalone checker builds the nested 440-, 454-, 482- and 538-dimensional **exact continuous-SU(2)** Galerkin matrices, diagonalizes them, checks their in-subspace eigenvector residuals, and computes the seven finite product-rotor upper bounds from exact SU(2) character Jacobi matrices.

| b | 433 Ritz energy (prior) | 538 Ritz energy (new J=8) | 12-character-per-face product Ritz upper bound |
|--:|--:|--:|--:|
| 1 | 6.723884 | 6.717895 | 6.693490 |
| 4 | 23.020603 | 22.877763 | 20.862870 |
| 16 | 81.141612 | 80.575011 | 51.036975 |
| 64 | 309.687963 | 307.681249 | 111.255836 |

The 538-state basis and the product-class trial space are **not nested**. These are Ritz variational comparisons, not rigorous full-eigenvalue enclosures. The last column uses \(12^7\) class-character products implicitly through an exact Kronecker-sum factorization; no huge matrix is materialized. The target holonomy is Haar in the product-class trial, so the last column is an energy bound only.

The seven outgoing top-tower channels have explicitly computed *partial* residual norms. These can become tiny at large J while the Ritz energy remains much higher than an independently proven true-energy upper bound; a small residual restricted to seven channels does **not** certify the full physical residual or the ground-state identity.

## 7. Revised exact gate

**Proved:** (HT-1) exact nested single-face-tower Galerkin matrix; (HT-2) exact tensor class Ritz variational bound; (HT-3) all-J no-go for any subspace omitting simultaneous high spin on one of seven outer links; (HT-4) asymptotic true-ground overlap exclusion and all-seven joint high-spin requirement. **Still OPEN:** construct and certify a physical **joint** high-spin/color-complete Ritz space that simultaneously localizes all retained plaquettes and resolves the target-center-even connected winding response, with full omitted-channel residual and full-Hilbert spectral separation. A finite eight-face certificate would not by itself prove the Penrose-uniform deleted cap lower bound, fixed-support covariance, quartic resolvent or continuum mass gap.
