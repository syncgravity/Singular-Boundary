# The Singular Boundary — Complete fundamental-shell winding witness and nondecaying Wilson magnetic boundary couplings

**Research date:** 2026-10-29. **Program:** R3 independent reconstruction. **Model:** finite, all-vertex Gauss-invariant continuous-SU(2) Wilson Hamiltonians on simply connected open square-rhombus disks; the concrete connected eight-face fixture is the 3×3 square disk with corner (0,0) removed and central face (1,1) magnetically deleted. **Status:** rigorous *kinematic* spin-network and full-Hamiltonian matrix-element theorems, deterministic continuous-SU(2) verification. **NOT proved:** a full 433×433 magnetic Hamiltonian diagonalization, a full-coupling eight-face vacuum cap bound, all-bulk Penrose refinement, continuum gap or reconstruction.

## 1. Geometry and the first complete physical spin-network shell

The eight-face fixture has 15 vertices, 22 primal links and eight independent planar face cycles. Its central target f=(1,1) has all four cardinal neighbors N,E,S,W. Let \(P_{1/2}\) project onto the **entire physical** spin-network space in which each original link carries spin 0 or 1/2, including all SU(2) vertex intertwiners. Occupied fundamental links must form even-degree edge configurations (\(\mathbb F_2\) cycles). Every such configuration is the XOR of a unique subset of the eight face boundaries. At an occupied four-valent vertex there are two independent fundamental intertwiners.

Exhaustive exact combinatorial enumeration gives **433** physical states, **246** target-center even and **187** target-center odd, reproducing R3-IR-420. For equal electric link coefficients \(a_e=1\), the **complete electric operator** \(P_{1/2}TP_{1/2}\) has the following exact spectrum (n is the number of occupied links and the energy is \(3n/4\)):

| occupied links n | kinetic energy | multiplicity | center even | center odd |
|---:|---:|---:|---:|---:|
|0|0|1|1|0|
|4|3|8|7|1|
|6|9/2|10|6|4|
|8|6|45|24|21|
|10|15/2|72|30|42|
|12|9|125|54|71|
|14|21/2|86|56|30|
|16|12|86|68|18|
|**Total**||**433**|**246**|**187**|

This is a complete, *exact* electric-spectrum census, **not** a spectrum of the full magnetic Hamiltonian. For nonuniform \(a_e\), each occupation has eigenvalue \((3/4)\sum_{e\text{ occupied}}a_e\), with intertwiner degeneracy unchanged.

## 2. F1 — Explicit center-even *non-Haar* physical vector in the 433-state shell

Let \(S\) be the five-face cross comprising f and its four cardinal neighbors. Its boundary is a simple 12-link outer loop, \(\partial S\), disjoint in links from the four-link inner target loop \(\partial f\). Their union consists of exactly 16 distinct primal links. Let \(U_f\) and \(U_{\partial S}\) be their SU(2) ordered holonomies, and write \(\chi_{1/2}(U)=\operatorname{Tr}(U)=2p(U)\). The *explicit physical spin-network state*

\[
\boxed{\Psi_\star(U)=\chi_{1/2}(U_f)\chi_{1/2}(U_{\partial S})}
\]

is Gauss invariant because both loops are closed Wilson traces. Since each original link appears **once or not at all**, \(\Psi_\star\in P_{1/2}\mathcal H_{\rm phys}\), with exactly 16 occupied fundamental links. At the central four-valent vertices its contraction is the product of the two loop intertwiners, an admissible vector in the full intertwiner space.

It is **target-center-even**: the canonical center-flux operation \(C_f\) flips both loops, because the outer boundary encloses f once, and their product is invariant. The loops use disjoint sets of independent product-Haar link variables, so under *kinematic* product Haar their holonomies are independent Haar SU(2) variables. SU(2) character orthogonality proves \(\|\Psi_\star\|_2^2=1\).

Writing \(p_f=\cos\theta_f\), integrating the independent *outer* holonomy proves the **exact target group marginal under \(|\Psi_\star|^2\)**:

\[
\boxed{d\nu_{\Psi_\star}(U_f)=\chi_{1/2}(U_f)^2\,dU_f=4p_f^2\,dU_f.}\tag{F1}
\]

Thus its target-center-even spin-one Wilson character expectation is *strictly non-Haar*:

\[
\boxed{\langle\Psi_\star,\chi_1(W_f)\Psi_\star\rangle
=\int4p^2(4p^2-1)\,dU=16\cdot\tfrac18-4\cdot\tfrac14=1.}\tag{F2}
\]

In particular, \(P_{1/2,C_f=+}\chi_1(W_f)P_{1/2,C_f=+}\) is a nonzero operator, with norm at least 1. This corrects the *dangerous extrapolation* from the previous 35-state Ritz space: the complete fundamental shell is already capable of a non-Haar, center-even target response. It does **not** say the *true magnetic ground state* has this distribution.

The exact center-cap probability of this witness, for \(B_a=\{\theta_f\le a\}\), is

\[
\boxed{\Pr_{\Psi_\star}(B_a)=\frac{a-\frac14\sin(4a)}{\pi},\qquad
\Pr_{\rm Haar}(B_a)=\frac{a-\frac12\sin(2a)}{\pi},\qquad
\frac{\Pr_{\Psi_\star}(B_a)}{\Pr_{\rm Haar}(B_a)}\to 4\quad (a\downarrow0).}\tag{F3}
\]

For the smooth nonnegative convolution cap source \(k_a\) supported in \(B_a\), similarly \(\langle k_a\rangle_{\Psi_\star}/\alpha_a^2\to4\) as \(a\downarrow0\).

**Kinematic scope warning.** The witness is not a variational candidate with correct strong-field energy scaling. On every retained plaquette q the kinematic density \(|\Psi_\star|^2\) is invariant under the single-face center flip \(C_q\), while \(p_q\) changes sign, so \(\langle p_q\rangle_{\Psi_\star}=0\). The electric Casimir on each of its sixteen occupied links is exactly 3/4. Therefore its **exact full Wilson Rayleigh quotient** is

\[
\boxed{\langle\Psi_\star,H^-_f\Psi_\star\rangle
=\tfrac34\sum_{e\in\partial f\cup\partial S}a_e+\sum_{q\ne f}b_q.}\tag{F4}
\]

For uniform electric coefficients the kinetic part is 12. At \(b_q\asymp h^{-2}\), its magnetic part grows like \(h^{-2}\), while the previously proved physical variational upper bound is \(O(h^{-1})\) for a *fixed* eight-face patch. Thus F1–F3 demonstrate representation expressivity, **not ground-state cap survival**.

## 3. F2 — Seven exact outgoing Wilson spin channels for *every* finite link cutoff

Let \(P_J\) be the **complete all-vertex gauge-invariant** projection onto original-link SU(2) spins \(j_e\le J\), where \(J\ge\frac12\) is any half-integer. Let \(Q_J=1-P_J\), and retain the seven non-target magnetic plaquettes \(q\in Q\), with \(b_q>0\). Define normalized physical Wilson characters

\[
X_{q,J}=\chi_J(W_q),\qquad Y_{q,J}=\chi_{J+1/2}(W_q).
\]

Each \(X_{q,J}\) has spin precisely J on the four links of q and therefore lies in \(P_J\). Each \(Y_{q,J}\) has spin J+1/2 there and lies in \(Q_J\). Kinematic planar face-coordinate Haar factorization makes the seven X's mutually orthonormal and the seven Y's mutually orthonormal. They are all **target-center-even**, because the target flux flips only \(W_f\), not the seven retained face holonomies.

The electric Casimir T preserves every link-spin sector, so \(Q_JTP_J=0\). The SU(2) fundamental fusion identity is

\[
\chi_{1/2}(U)\chi_J(U)=\chi_{J+1/2}(U)+\chi_{J-1/2}(U),\qquad J\ge\tfrac12.
\]

Using \(p_q=\chi_{1/2}(W_q)/2\), independent face-Haar orthogonality for every *other* plaquette and the magnetic Wilson Hamiltonian \(H=T+\sum_{q\in Q}b_q(1-p_q)\) yields the **exact physical off-shell matrix**, with no approximation:

\[
\boxed{\langle Y_{q,J},Q_JHP_JX_{r,J}\rangle
=-\frac{b_q}{2}\,\delta_{qr},\qquad q,r\in Q.}\tag{F5}
\]

Therefore \(Q_JHP_J\) has at least seven independent nonzero outgoing directions. Its singular-value list **dominates** that of the seven-by-seven compression \(\operatorname{diag}(b_q/2)\) in the usual min-max sense, and in particular

\[
\boxed{\rho_J:=\|Q_JHP_J\|\ge\frac12\max_{q\ne f}b_q\quad\text{for EVERY finite }J\ge\tfrac12.}\tag{F6}
\]

This is an exact **no-decay theorem for the global magnetic off-block operator norm**, valid with all other nonlinear Wilson plaquettes present, with arbitrary electric coefficients, without spatial reflection or a physical mass gap. It applies **inside the center-even physical sector** as well.

**Implication for the earlier sufficient Ritz-gap certificate.** The global norm \(\rho_J\) is always at least order \(b\), even if J grows. Thus \(\rho_J\to0\) cannot be the convergence mechanism of a complete spin cutoff. A conservative Schur-complement test using the global \(\rho_J^2/(M_J-e_1)\) may be drastically inefficient. This does not invalidate a certificate if sufficiently large J makes \(M_J\) huge. The correct refinement is to calculate **state-dependent** outgoing residuals and structured boundary-channel couplings, while obtaining any needed lower spectral bound on the complementary subspace by a separate rigorous argument. A small Ritz residual alone does not automatically certify the true ground state without a spectral-separation theorem.

## 4. F3 — Exact Jacobi rotor makes the global-versus-state-dependent distinction concrete

For the fully nonlinear continuous-SU(2) **one-face Wilson class rotor** with four equal electric links of coefficient 1, the normalized character basis \(\chi_{n/2}\), n=0,1,..., has the exact Hamiltonian

\[
H_{nn}=n(n+2)+b,\quad H_{n,n+1}=H_{n+1,n}=-b/2.
\]

Under the cutoff n\le N (J=N/2), \(\|QH P\|=b/2\) for every N. Yet the **actual normalized Ritz ground vector** \(v^{(N)}\) has the *exact* outgoing residual

\[
\boxed{r_N=(b/2)|v^{(N)}_N|.}\tag{F7}
\]

Representative deterministic diagonalizations:

| magnetic b | cutoff J | global off-block norm | ground Ritz residual |
|---:|---:|---:|---:|
|16|2|8|0.276281|
|16|4|8|0.000078935|
|256|4|128|5.502307|
|256|8|128|0.00177552|
|4096|8|2048|54.21273|
|4096|16|2048|0.0271451|

These show how the full operator coupling persists at the **top of every cutoff** while a low-energy vector's weight at that cutoff boundary can decay strongly. This is **not** an interacting eight-face calculation and does not establish an eight-face residual bound.

## 5. Reproducibility and exact remaining proof gate

The artifact contains three deterministic checkers: (i) all 256 even-degree occupation patterns, 433 physical intertwiners, exact electric multiplicities and the 16-link target-plus-exterior witness; (ii) SU(2) Haar-character fusion and the exact seven-channel outgoing matrix; (iii) continuous-SU(2) one-face nonlinear rotor residuals. No Monte Carlo is needed or used. The full analytic proofs of F1–F7 are given above.

**PROVED:** complete fundamental-shell electric spectrum, explicit center-even non-Haar *kinematic* target state and its exact cap, magnetic-energy cost of that state, and exact nondecaying seven-channel magnetic off-block coupling for every link cutoff. **STILL OPEN:** full 433×433 Wilson magnetic recoupling and verified Ritz eigenpairs, a state-dependent off-shell residual for the *eight-face* Ritz vacuum, a true finite-volume cap certificate, uniform asymmetric Penrose deleted-face cap probability and response, fixed-support connected covariance, regulator-uniform physical gap, nonlinear quartic resolvent and continuum reconstruction.
