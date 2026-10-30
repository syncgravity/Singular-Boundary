# The Singular Boundary — Reflection-odd asymmetry, sector-resolvent stability, and a sign obstruction

**Date:** 2026-10-29. **Research program:** R3 independent reconstruction of spatial SU(2) Wilson Hamiltonians. **Classification:** exact finite-volume analytic theorem for perturbations of a *reflection-symmetric* deleted Wilson Hamiltonian; independently verified finite-matrix/sampled-SU(2) countermodels to unjustified global sign extension. **OPEN:** bounds for fully connected asymmetric Penrose faces without geometric reflection, uniform sector gaps, nonlinear fixed-support covariance, physical Yang–Mills gap and continuum reconstruction.

## A. The precise proof problem

The prior reflection-seam theorem (RS-1–RS-5) proves, for a link-free vertex seam whose reflection pairs all electric coefficients and corresponding half-side Wilson magnetic coefficients, that the actual strictly positive deleted-vacuum ground state has nonnegative target SU(2) characters and therefore

\[
 m_0(B_{a_h})\ge H(a_h/2),\quad H(a)=\frac{a-\frac12\sin(2a)}\pi,
 \quad a_h=\arccos(1-h),\quad H(a_h/2)\asymp h^{3/2}.
\]

For unequal half-side Hamiltonians the cone-preserving kinetic operator changes from `K -> S_t K S_t` to `K -> S_t K T_t`; the latter need not preserve positive self-adjoint kernels. Hence the previous proof, by itself, does not extend to arbitrary asymmetric coefficients. We obtain an **exact symmetry-resolved *finite-gap* perturbation estimate**, which is stronger in its asymmetry exponent than a naive ground-state overlap bound.

## B. Physical reflection-resolved Wilson model

Let \(H_0\) be a finite physical or full-link SU(2) Wilson Hamiltonian with **deleted target magnetic term** satisfying the prior global reflection-seam hypotheses. Work in the full product-link Hilbert space \(\mathcal H=L^2(SU(2)^E)\); the unique strictly positive normalized ground state \(\Omega_0\) automatically satisfies Gauss invariance. Write its ground energy \(E_0\).

Let \(\mathcal R\) be the unitary involution exchanging its reflected halves, including edge-orientation inversion, so \([\mathcal R,H_0]=0\), \(\mathcal R\Omega_0=\Omega_0\). Define even and odd projectors \(P_\pm=(I\pm\mathcal R)/2\), and the strictly positive **finite** symmetry-resolved excitation energies

\[
 \delta_+=\inf \sigma(H_0|_{\mathcal H_+\cap\Omega_0^\perp})-E_0>0,
 \qquad\delta_-=\inf\sigma(H_0|_{\mathcal H_-})-E_0>0.
\]

Let \(D\) be a bounded real self-adjoint multiplication operator such that \(\mathcal R D\mathcal R=-D\), with \(\|D\|\le\varepsilon\). Set \(H=H_0+D\) and let \(\Omega>0\) be its unique normalized ground state with energy \(E\). The physical Wilson case is **unpaired magnetic coefficients on a graph which still has the same reflection geometry, with electric coefficients exactly paired**. For every reflected pair \(q_+,q_-\), write \(b_{q+}=\bar b_q+\eta_q\), \(b_{q-}=\bar b_q-\eta_q\); the mismatch is

\[
 D=\sum_q\eta_q[d_{q+}-d_{q-}], \qquad d_q=1-\tfrac12\operatorname{ReTr}W_q\in[0,2],
 \qquad \boxed{\varepsilon\le\sum_q|b_{q+}-b_{q-}|.}
\]

This finite-volume norm bound remains independent of the coupling strength of any seam-crossing Wilson face or of the number of reflected pairs when the aggregate mismatch is fixed. If a plaquette is fixed individually by reflection (a seam-crossing face), its coefficient is unchanged; a *reflection-odd perturbation* cannot alter it. **Electric coefficient mismatch is unbounded as an operator and is not covered by this theorem.**

## C. Theorem AS-1: exact parity-resolvent suppression of even ground-state distortion

Decompose the true perturbed ground state into reflection parity sectors,

\[
 \Omega=u+v,\quad u=P_+\Omega,\quad v=P_-\Omega,
 \qquad u=c\Omega_0+w,\quad w\in\mathcal H_+\cap\Omega_0^\perp,
 \quad c=\langle\Omega_0,\Omega\rangle>0.
\]

Because \(\langle\Omega_0,D\Omega_0\rangle=0\) by parity, the variational principle gives \(E\le E_0\). The exact ground-state equation, projected to odd and even excited sectors, is

\[
 (H_{0,-}-E)v=-P_-Du,
 \qquad Q_+(H_{0,+}-E)w=-Q_+Dv,
 \quad Q_+=P_+-|\Omega_0\rangle\langle\Omega_0|.
\]

Since \(E\le E_0\), the first resolvent has operator norm at most \(1/\delta_-\); the second is at most \(1/\delta_+\). Therefore

\[
\boxed{\|v\|\le r:=\varepsilon/\delta_-,\qquad
\|w\|\le s:=\varepsilon^2/(\delta_+\delta_-).}\tag{AS-1}
\]

No complex analytic continuation or assumption of a uniform gap in refinement is used. This is a **nonperturbative finite-volume bound**, exact for arbitrary bounded reflection-odd D (the bound becomes vacuous when r,s are large). In particular, the *even excited-sector* distortion is quadratic in magnetic asymmetry, whereas the full state can change at first order through odd excitations.

## D. Theorem AS-2: sharpened cap stability for the actual asymmetric Wilson vacuum

Let \(B\) be **any measurable configuration event invariant under reflection**, and let \(M_B\) denote its multiplication projector. In particular, \(B=B_a(f)=\{U_f:\arccos(\frac12\mathrm{ReTr}W_f)<a\}\) is reflection invariant because reflection sends the target holonomy to its conjugate/inverse inside its trace. As \(M_B\mathcal R=\mathcal R M_B\), odd/even cross terms vanish:

\[
 m(B)=\|M_B\Omega\|_2^2=\|M_Bu\|_2^2+\|M_Bv\|_2^2\ge\|M_Bu\|_2^2.
\]

By orthogonality, \(c^2=1-\|v\|^2-\|w\|^2\), so \(c\ge\sqrt{[1-r^2-s^2]_+}\). The reverse triangle inequality gives

\[
\boxed{
 m(B)\ge \left[
\sqrt{[1-r^2-s^2]_+}\,\sqrt{m_0(B)}-s
\right]_+^2.
}\tag{AS-2}
\]

Since the symmetric deleted-vacuum cap obeys \(m_0(B_a)\ge H(a/2)\) by the preceding reflection-seam character theorem, we obtain the genuinely **asymmetric full-coupling** finite-volume bound

\[
\boxed{m_{\rm asym}(B_a)\ge
 \left[
 \sqrt{[1-r^2-s^2]_+}\,\sqrt{H(a/2)}-s
 \right]_+^2.}\tag{AS-3}
\]

A concrete sufficient condition for at least one-quarter of the earlier Haar cap lower bound is

\[
\boxed{r\le\tfrac12,\qquad s\le\tfrac14\sqrt{H(a/2)}
\ \Longrightarrow\ m_{\rm asym}(B_a)\ge\tfrac14 H(a/2).}\tag{AS-4}
\]

Indeed \(H\le1\) implies \(\sqrt{1-r^2-s^2}\ge\sqrt{11}/4\), and \((\sqrt{11}/4-1/4)^2>1/4\).

For the physical center deficit \(a_h=\arccos(1-h)\), \(H(a_h/2)\sim\frac{\sqrt2}{6\pi}h^{3/2}\). Thus the sufficient mismatch threshold is

\[
\boxed{\varepsilon\le\tfrac12\sqrt{\delta_+\delta_-}\,H(a_h/2)^{1/4}
 =O(\sqrt{\delta_+\delta_-}\,h^{3/8}),\quad
 \varepsilon\le\delta_-/2.}\tag{AS-5}
\]

This improves the naive \(O(\delta_0 h^{3/4})\) **operator-norm mismatch threshold** to \(O(\sqrt{\delta_+\delta_-}h^{3/8})\) when the two finite sector gaps are comparable. The proof is stronger because reflection-invariant cap probability is insensitive to first-order **odd** wavefunction response. The gap quantities must actually be controlled; this is not regulator-uniform without a new lower bound on them. The estimate applies to full magnetic couplings within its small aggregate **asymmetry** hypothesis, not just small overall gauge coupling.

Combining AS-4 with the previously established deleted-vacuum cap-to-deletion trial theorem gives the same conditional \(O(h^{-1}\log(1/h))\) magnetic-deletion estimate for this near-reflection class. Generic asymmetric Penrose bulk disks usually have **no exact reflection graph involution**, so AS-1–5 do not apply to them.

## E. Theorem AS-3: positivity of crossing kernels alone does **not** imply asymmetric character positivity

There is a sharp abstract obstruction. Let each half-space consist of a **two-point configuration space** indexed by \(s=\pm1\), equipped with nonnegative electric generators \(a(I-\sigma_x)\), \(a>0\). Let the positive **ferromagnetic** crossing potential be \(J(1-st)\), \(J>0\); its crossing Boltzmann kernel is \(e^{Jst}\), with two eigenvalues \(2\cosh J\) and \(2\sinh J\), both positive. Add nonnegative but asymmetrically selected half-potentials \(M1_{s=-1}\) and \(M1_{t=+1}\), with \(M>0\). Thus the total operator is a real symmetric irreducible stoquastic Hamiltonian with a unique strictly positive ground state and positive-definite crossing semigroup factors. However its ground state concentrates on the **anti-aligned** configuration \((s,t)=(+,-)\) as \(M\to\infty\), so \(\langle st\rangle\to-1\), contradicting any supposed sign theorem from crossing positivity alone.

This can be proved without diagonalization: the ground energy is bounded by the anti-aligned basis-vector trial energy \(E\le 2a+2J\), while \(H\ge M(1-P_{+,-})\), hence the probability outside \((+,-)\) is at most \((2a+2J)/M\), and
\[
\boxed{\langle st\rangle\le-1+\frac{2(2a+2J)}M<0\quad(M>2(2a+2J)).}\tag{AS-6}
\]

A second comparator samples the **actual SU(2) characters** at the two group elements \(I\) and \(i\sigma_3\), where fundamental \(p\) has Gram matrix \(\begin{pmatrix}1&0\\0&1\end{pmatrix}\) and the spin-one character has Gram matrix \(\begin{pmatrix}3&-1\\-1&3\end{pmatrix}\), still positive definite. A crossing Wilson factor \(e^{Jp}\) is positive definite. With the asymmetric half-side nonnegative potentials above, the unique positive finite-matrix ground state has a **negative spin-one character expectation**, approaching \(-1\) as \(M\to\infty\). This SU(2)-sampled two-state system is **not** the continuous product-Haar, Gauss-invariant Wilson Hamiltonian. It disproves only an unjustified *abstract cone argument* without reflection pairing, not the possibility that the genuine Wilson Hamiltonian enjoys an additional favorable inequality.

## F. Verification, scope and exact next obligation

The companion deterministic Python file verifies the exact finite-dimensional symmetric and asymmetric ground states, crossing-kernel positive definiteness, the two parity-sector resolvent bounds \(r,s\), the cap lower inequality AS-2, the \(h^{3/8}\) refinement exponent, and the SU(2)-character-sampled sign obstruction. It uses no Monte Carlo, does not diagonalize an eight-face SU(2) Wilson patch, and makes no Penrose numerical or physical-mass-gap claim.

**PROVED:** AS-1–AS-5 and the *abstract* obstruction AS-6 under stated assumptions. **OPEN:** a gap-independent, reflection-free Wilson positivity or small-ball theorem for genuinely asymmetric fully connected Penrose interiors; reliable finite-volume even/odd gap lower bounds sufficient for uniform near-reflection stability; fixed-support connected covariance, physical time source survival, quartic resolvent and continuum Yang–Mills reconstruction.
