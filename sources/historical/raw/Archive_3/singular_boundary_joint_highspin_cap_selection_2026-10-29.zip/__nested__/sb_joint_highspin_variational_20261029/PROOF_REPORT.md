# The Singular Boundary — Constructive simultaneous high-spin packets and a cap-selection obstruction

**Date:** 2026-10-29. **Project:** R3 independent reconstruction. **Claim range proposed:** R3-IR-441–447. **Classification:** exact finite physical continuous-SU(2) Wilson variational construction, with original-link electric terms and nonabelian relative-color extension. **What is not proved:** true-ground-state eight-face center cap, full-Hilbert Ritz residual or spectral gap, Penrose volume-uniform magnetic deletion, fixed-support continuum covariance or Yang–Mills mass gap. These proposed additions are LOCAL ONLY; GitHub writing was previously declined.

## Setup

Use the exact previously verified 15-vertex, 22-link, eight-face square-rhombus disk with target `f=(1,1)` magnetically deleted. The other seven plaquettes are `Q`; coefficients are `a_e>0`, `A_q=∑_{e∈∂q}a_e`, and `b c_q>0`. The full gauge-invariant Wilson operator is

\[
 H_b=\sum_e a_e(-\Delta_e)+b\sum_{q\in Q}c_q(1-p_q),\qquad p_q=\tfrac12\operatorname{Tr}W_q.
\]

All identities use the bi-invariant SU(2) Laplacian `-Δχ_j=j(j+1)χ_j` and Haar-orthonormal characters. A planar tree-gauge change of variables turns the eight face holonomies into independent SU(2) Haar coordinates. The *projected quadratic form* on products of individual face class functions equals the Kronecker sum of radial SU(2) electric forms. It is not an invariant subspace of the **full** electric Hamiltonian; off-class mixed-gradient terms generally remain.

## JH-1. A finite, simultaneous seven-face packet with optimal-order spin resolution

For `N≥1` let

\[
 \phi_N(U)=\sqrt{\frac2{N+2}}\sum_{n=0}^{N}\sin\frac{(n+1)\pi}{N+2}\,\chi_{n/2}(U).
\]

By Haar orthogonality and the `SU(2)` fusion `p χ_{n/2}=(χ_{(n-1)/2}+χ_{(n+1)/2})/2`, one has exactly

\[
 \|\phi_N\|_2=1,\qquad \langle\phi_N,p\phi_N\rangle=\cos\frac\pi{N+2},
\quad \langle\phi_N,-\Delta\phi_N\rangle=K_N,
\]
\[
 K_N=\frac2{N+2}\sum_{n=0}^{N}\frac{n(n+2)}4\sin^2\frac{(n+1)\pi}{N+2}.
\]

Hence the finite joint-character state `Φ_N=∏_{q∈Q}φ_{N_q}(W_q)`, which **simultaneously** uses spins on all seven retained plaquettes, is exactly normalized and has exact Rayleigh quotient

\[
 \boxed{\mathcal E_{\mathbf N}(b)=\sum_{q\in Q}\left[A_qK_{N_q}+bc_q\left(1-\cos\frac\pi{N_q+2}\right)\right].}\tag{JH-1}
\]

The underlying original-link spin is bounded above by the sum of the spins of the one or two plaquettes incident to that link. Thus taking `N_q=⌈(bc_q/A_q)^{1/4}⌉` constructs an explicitly finite **physical joint** state with maximum original-link spin `O(b^{1/4})` and energy `O(√b)`. This matches the *order* of the previously proved necessary resolution but establishes only existence of a competitive leading-energy trial, **not** approximation of the physical eigenvector. The tensor-product class span is not color complete.

For the fixed asymmetric test coefficients `a_e=0.8+0.07(i mod 6)+0.013(i mod 3)` in canonical original-link ordering and `c_k=0.78+0.09k` in sorted retained-face ordering, direct minimization of the **exact** one-face expression over finite `N=1..100` gives the accompanying CSV. There is no fitted matrix element or stochastic integration.

## JH-2. Center-even target faces with arbitrarily high cap-vanishing order and *bounded* extra energy

For any fixed integer `m≥1`, set

\[
 v_m(W_f)=Z_m^{-1/2}(1-p_f^2)^m,\qquad
 Z_m=\int_{SU(2)}(1-p^2)^{2m}\,dU
 =\frac2\pi B\!\left(\frac12,2m+\frac32\right).
\]

The state `Φ_{m,N}=v_m(W_f)∏_qφ_{N_q}(W_q)` is smooth, gauge invariant, target-center even and jointly high spin on the retained plaquettes. Its exact energy is

\[
 \boxed{\langle\Phi_{m,N},H_b\Phi_{m,N}\rangle
 =\mathcal E_{\mathbf N}(b)+A_f\frac{m^2}{4m+1}.}\tag{JH-2}
\]

**Proof of target energy.** For class functions, `|∇p|²=(1-p²)/4` for the chosen SU(2) normalization. Differentiating `v_m` and applying Haar p-density `(2/π)√(1-p²)dp` gives

\[
 \frac{\langle (1-p^2)^m,-\Delta(1-p^2)^m\rangle}{Z_m}
 =m^2\frac{\mathbb E_H[p^2(1-p^2)^{2m-1}]}{\mathbb E_H[(1-p^2)^{2m}]}=\frac{m^2}{4m+1}.
\]

Every retained magnetic term and its target-free class expectation is unchanged. The mixed original-link electric-gradient expectations vanish under independent Haar face orientations. This is an exact *quadratic-form* identity, not a statement that the ansatz is an eigenstate.

For `a=arccos(1-h)`, its exact center cap probability is

\[
 \boxed{F_{m}(a)=\frac{2}{\pi Z_m}\int_0^a\sin^{4m+2}\theta\,d\theta
 \asymp a^{4m+3}\asymp h^{2m+3/2}.}\tag{JH-3}
\]

In particular, for `m=1`, `Z_1=5/8`, the electric cost is **exactly `A_f/5`**, and

\[
 F_1(a)=\frac{16}{35\pi}a^7+O(a^9),\qquad
 F_1(a)/F_H(a)=\frac{24}{35}a^4+O(a^6).
\]

Since `m` is fixed independently of b, **arbitrarily strong extra suppression in powers of h is possible in exact, finite, center-even physical Wilson trial states at only O(1) extra energy**, on top of an `O(√b)` joint-localization trial. This is not a counterexample concerning the actual positive ground state.

Conversely the normalized center-even target factor `u_+=(1+χ_1(W_f))/√2` has electric cost `A_f`, target density `(1+χ_1)^2/2=8p_f^4`, and center-cap/Haar ratio tending to **8**. So quite different cap marginals coexist at the same strong-field leading energy.

## JH-3. Explicit off-class SU(2) color extension with the same energy scaling

Take one target-neighbor pair `(f,g)` sharing original link `e`. Let

\[
 D_{fg}=p_{\partial(f\cup g)}-p_fp_g,\qquad R_{fg}=p_fD_{fg}.
\]

The noncommuting SU(2) quaternion identity establishes `|D|≤√(1-p_f²)√(1-p_g²)≤1`, so `|R|≤1`. The function `R` is center even under the deleted target flux and is *not* a function of individual plaquette conjugacy classes. Under independent face-Haar conditional angular distributions,

\[
 \mathbb E(R\mid p_f,p_g)=0,\qquad
 \mathbb E(R^2\mid p_f,p_g)=\tfrac13p_f^2(1-p_f^2)(1-p_g^2).
\]

Consequently the normalized, **finite** joint/color-bearing trial

\[
 \Psi_{m,\mathbf N,\varepsilon}=
 \frac{(1+\varepsilon R_{fg})\Phi_{m,\mathbf N}}
 {\sqrt{1+\varepsilon^2\sigma_{m,N_g}^2}},
 \quad \sigma_{m,N_g}^2=\frac{4m+3}{12(2m+2)(2m+3)}\,V_{N_g},
\]

is nonclass whenever `ε≠0`, where, **exactly** for the sine packet,

\[
 V_N=\langle\phi_N,(1-p^2)\phi_N\rangle
 =\sin^2\!\frac\pi{N+2}\left(1-\frac1{2(N+2)}\right)>0.
 \tag{JH-4}
\]

The last identity follows because the truncated Jacobi p-matrix has the sine eigenvector with eigenvalue `cosθ`, while its only omitted component has squared amplitude `sin²θ/[2(N+2)]`. Therefore the off-class component has an **exact nonzero** norm for every finite b and N, although its normalized weight tends to zero as `N_g→∞` at fixed ε. The construction does not assert an order-one nonclass weight uniformly in b.

To control energy, observe for an original link in the union of the two faces that `|∇_e R|≤2` in the SU(2) kinetic metric, and zero outside. Hence `B_R=4∑_{e∈∂f∪∂g}a_e` is a valid pointwise bound on `∑_e a_e|∇_e R|²`. Splitting the product derivative with the Hilbert-space triangle inequality gives

\[
 \boxed{\langle\Psi_{m,\mathbf N,\varepsilon},H_b\Psi_{m,\mathbf N,\varepsilon}\rangle
 \le \left[(1+|\varepsilon|)\sqrt{T_{m,\mathbf N}}+|\varepsilon|\sqrt{B_R}\right]^2
 +(1+|\varepsilon|)^2V_{\mathbf N},}\tag{JH-5}
\]

where `T_{m,N}=∑_q A_qK_{N_q}+A_fm²/(4m+1)` and `V_N=b∑_qc_q(1-cos(π/(N_q+2)))`. The denominator norm is ≥1 and was safely discarded. At fixed `m,ε` and `N_q≈b^{1/4}`, this remains `O(√b)`. For `|ε|≤1`, its cap obeys the rigorous bound

\[
 \boxed{\mathbb P_{\Psi_{m,N,\varepsilon}}(d_f\le h)
 \le (1+|\varepsilon|)^2 F_m(a_h)
 =O(h^{2m+3/2}).}\tag{JH-6}
\]

The factor `1+εR` is a finite Wilson polynomial, so it adds only **bounded** original-link spin to the initial finite spin cutoffs. Thus this is a genuine finite joint high-spin **color-bearing** state with `O(b^{1/4})` maximum spin and correct `O(√b)` energy scale, but it is only a few-dimensional variational family, not a color-complete Ritz basis.

## JH-4. Independent deterministic regressions

The companion `verify_joint_packet.py` independently evaluates sine-packet Jacobi moments, SU(2) Haar/Beta target norms and Dirichlet identities, nonclass conditional variance and actual b-dependent energies for the asymmetric eight-face coefficients. `JOINT_VARIATIONAL_DATA.csv` reports exact finite trial Rayleigh values. `CAP_DATA.csv` reports evaluated SU(2) Haar cap probabilities and suppressed/enhanced trial cap probabilities. The script contains no stochastic steps. An external proof is still required before using the small packets as a certified full ground-state spectral approximation.

## Revised unresolved gate

**Newly solved:** constructive finite simultaneous high-spin `O(b^{1/4})` variational energy-scale sufficiency; exact center-even target cap-shaping cost; an explicit finite, nonclass color-bearing joint trial with energy/cap control. **New obstruction:** energy-scale correctness and joint high-spin/color *presence* do not by themselves select a Haar-order deleted-face cap. **Still open:** a genuinely color-complete, fully connected **multi-plaquette** Ritz space with complete omitted-channel residual and spectral-separation certificate for the actual ground state; Penrose-uniform cap probability; downstream fixed-support covariance and continuum gap.
