# The Singular Boundary — Pointwise strong-coupling Wilson f-sum and all-finite-time-jet obstruction

**Research date:** 2026-10-29. **Independent audit branch:** `audit/2026-10-28-independent-reconstruction`. **Status:** two exact quantitative **finite-volume nonlinear SU(2) Wilson Hamiltonian** estimates, followed by a rigorous **non-Wilson** positive-diffusion obstruction to closing the remaining response using any prescribed finite order of short-time spectral data. The generic connected Penrose deleted-face cap lower bound, physical mass gap and continuum reconstruction remain **OPEN**.

## 1. Actual nonlinear physical model and exact coupling pinning

For a finite simply connected SU(2) rhombus disk with positive electric coefficients and at most two plaquettes per link, fix edge-sharing faces f and g, delete f's magnetic term permanently, and set

\[
H(u)=T+\sum_{q\notin\{f,g\}}b_q(1-p_q)+u b_g(1-p_g),\quad u\in[0,1],\quad p_q=\tfrac12\mathrm{ReTr}W_q.
\]

Write \(b=b_g\), \(A_g=\sum_{e\in\partial g}a_e\), \(W=b(1-p_g)\), the normalized unique positive Gauss-invariant vacuum \(\Omega_u\), its energy \(E(u)\), and excitation operator \(K_u=H(u)-E(u)\). All other magnetic interactions are retained at arbitrary nonnegative strengths. At the double-deleted endpoint u=0 the shared link is magnetically free, so g's holonomy is exactly Haar. The *previously established* gauge-invariant private-link trial gives

\[
0\le E(u)-E(0)\le c_0\sqrt{A_gbu},\qquad c_0=\frac3{2\sqrt2}.
\]

Ground-energy concavity and Hellmann–Feynman imply for every \(u>0\)

\[
0\le E'(u)=b\langle1-p_g\rangle_u\le\frac{E(u)-E(0)}{u}\le c_0\sqrt{\frac{A_gb}{u}}.
\]

Hence, with no assumption of a volume-uniform gap,

\[
\boxed{\langle1-p_g\rangle_u\le c_0\sqrt{\frac{A_g}{ub}}.}\tag{JT1}
\]

This is a **pointwise, full-coupling, non-Gaussian neighbor pinning estimate**. The interpolated coupling fraction u may depend on b and h. It does not constrain the deleted target holonomy.

## 2. New pointwise magnetic spectral moment estimate

For a real multiplication operator X, let \(m_{1,u}(X)=\langle Q_uX\Omega_u,K_uQ_uX\Omega_u\rangle\). The exact SU(2) ground-state carré-du-champ identity gives

\[
m_{1,u}(W)=\frac{b^2A_g}{4}\langle1-p_g^2\rangle_u
\le\frac{b^2A_g}{2}\langle1-p_g\rangle_u=\frac{bA_g}{2}E'(u).
\]

Using JT1 yields the **pointwise** refinement of the earlier coupling-*integrated* estimate:

\[
\boxed{m_{1,u}(W)\le c_1A_g^{3/2}b^{3/2}u^{-1/2},\qquad c_1=\frac3{4\sqrt2}.}\tag{JT2}
\]

At the fully restored endpoint u=1 and bounded electric coefficients, the source first moment is \(O(b^{3/2})\), rather than the trivial \(O(b^2)\). This concerns **energy-weighted** spectral weight, not the inverse-energy susceptibility, which remains uncontrolled pointwise.

Let \(k_a\ge0\) be the smooth positive SU(2) convolution cap from the earlier double-self-weighting theorem, supported in \(B_a(I)\), and \(k_a^+(U)=[k_a(U)+k_a(-U)]/2\). Define \(F_a(u)=\langle k_a(W_f)\rangle_u=\langle k_a^+(W_f)\rangle_u>0\). Target-center symmetry and the pointwise convolution inequality give

\[
m_{1,u}(k_a^+)\le D_k A_f a F_a(u),\qquad D_k=C_k/2,
\]

where \(C_k\) is independent of mesh, face count and u. Spectral Cauchy now bounds the **local mixed first moment**:

\[
\boxed{\frac{|m_{1,u}(k_a^+,W)|}{\sqrt{F_a(u)}}
\le\sqrt{D_kc_1}\,A_f^{1/2}A_g^{3/4}a^{1/2}b^{3/4}u^{-1/4}.}\tag{JT3}
\]

This controls the exact initial imaginary-time derivative of the connected cap–neighbor response in the strongly restored interval. At \(a_h\asymp h^{1/2}\), \(b\asymp h^{-2}\) and u=1 it is \(O(h^{-5/4})\), *not* a small enough control of the time-integrated response.

## 3. Explicit late-interval high-frequency separation

Let \(G_u=Q_uK_u^{-1}Q_u\) and \(P_{u,>\Lambda}\) project onto excitation energies \(>\Lambda\). Define

\[
v_{>\Lambda}(u)=2\operatorname{Re}\langle Q_uk_a^+\Omega_u,G_uP_{u,>\Lambda}Q_uW\Omega_u\rangle.
\]

Spectral Cauchy and \(\lambda^{-1}\mathbf1_{\lambda>\Lambda}\le\lambda/\Lambda^2\) give

\[
\frac{|v_{>\Lambda}(u)|}{2\sqrt{F_a(u)}}\le
\frac{\sqrt{D_kA_fa\,m_{1,u}(W)}}{\Lambda^2}.
\]

JT2, integrated only over \([s,1]\) with \(0<s<1\), proves

\[
\boxed{\int_s^1\frac{|v_{>\Lambda}(u)|}{2\sqrt{F_a(u)}}\,du
\le\frac{4}{3}\sqrt{D_kc_1}\,A_f^{1/2}A_g^{3/4}
\frac{a^{1/2}b^{3/4}}{\Lambda^2}(1-s^{3/4}).}\tag{JT4}
\]

At \(s=C/b\) and \(\Lambda=Lh^{-11/8}\), JT4 is \(O(L^{-2}h^{3/2})\). This **recovers** the known correct UV scaling while making the late-interval dependence explicit; it does not improve the UV exponent or control low-frequency response. The target cap remains subject to the separate signed low-energy part of the Kato response.

## 4. Theorem: no finite jet of short-time mixed moments determines the full-time response

This section is a rigorous mathematical obstruction for *generic positive reversible dynamics*, **not** a theorem about continuous SU(2) Wilson lattices.

**For every fixed integer \(N\ge0\)** and every \(0<\varepsilon<1\), let \(m=N+2\), choose distinct positive numbers

\[
\lambda_0=\varepsilon,\quad\lambda_i=i\quad(1\le i\le N+1),\qquad
P(z)=\prod_{i=0}^{N+1}(z-\lambda_i),\quad
w_i=\frac{P'(\lambda_0)}{P'(\lambda_i)}.
\]

Lagrange interpolation gives the exact algebraic identity

\[
\boxed{\sum_{i=0}^{N+1}w_i\lambda_i^k=0,\qquad k=0,1,\ldots,N.}\tag{JT5}
\]

Construct the product-spin state space \(\{\pm1\}^{N+2}\times\{\pm1\}\), with uniform stationary distribution. Let \(K_\varepsilon\) be the sum of independent coordinate-flip generators whose nonconstant coordinate-spin eigenfunctions \(x_i\) have eigenvalues \(\lambda_i\); the last spin \(z\) flips at any fixed positive rate. All rates are strictly positive, so the diffusion is irreducible and its heat semigroup is **positivity improving**, with a unique constant positive ground state. The involution \(z\mapsto-z\) commutes with \(K_\varepsilon\).

With \(S=\sum_i\sqrt{|w_i|}\), choose bounded nonnegative, center-even multiplication observables

\[
O=\tfrac12+\frac1{4S}\sum_i\sqrt{|w_i|}x_i,\quad
W=\tfrac12+\frac1{4S}\sum_i\operatorname{sgn}(w_i)\sqrt{|w_i|}x_i.
\]

Both lie pointwise in \([1/4,3/4]\), irrespective of epsilon. Let \(v=QO\Omega\), \(w=QW\Omega\). Orthogonality of independent spins gives the **exact** connected imaginary-time cross-correlation

\[
C_{N,\varepsilon}(t)=\langle v,e^{-tK_\varepsilon}w\rangle
=\frac1{16S^2}\sum_{i=0}^{N+1}w_i e^{-\lambda_it}.
\]

By JT5,

\[
\boxed{C_{N,\varepsilon}^{(k)}(0)=0\quad (0\le k\le N).}\tag{JT6}
\]

**Strict sign for every positive time:** the sum is \(P'(\lambda_0)\) times the divided difference of \(z\mapsto e^{-tz}\) at the ordered nodes \(\lambda_0<\cdots<\lambda_{N+1}\). Since \(P'(\lambda_0)\) and the \((N+1)\)-st derivative of \(e^{-tz}\) have the same sign, the Hermite–Genocchi formula gives

\[
\boxed{C_{N,\varepsilon}(t)>0\quad\text{for all }t>0.}\tag{JT7}
\]

Finally the full-time mixed inverse resolvent is

\[
\boxed{\int_0^\infty C_{N,\varepsilon}(t)dt
=\frac1{16S^2}\sum_i\frac{w_i}{\lambda_i}
=\frac{1}{16S_0^2}\frac1\varepsilon+O_N(1),}\tag{JT8}
\]

where \(S\to S_0\in(0,\infty)\) as \(\varepsilon\downarrow0\). The two **individual** first moments are bounded uniformly in epsilon:

\[
m_1(O)=m_1(W)=\frac1{16S^2}\sum_i |w_i|\lambda_i\le\frac{N+1}{16}.
\]

Therefore **even knowing any prescribed finite number of exactly vanishing mixed short-time derivatives, center symmetry, bounded positive observables, a positivity-improving semigroup and bounded individual f-sums does not control the signed inverse-energy response**. In fact the response is strictly adverse at every positive time in this example and diverges as the slow eigenvalue vanishes. The target and perturbation are finite-spin observables, **not SU(2) Wilson holonomies**; JT5–JT8 only rule out logical arguments relying *solely* on this list of generic properties. They do not refute a specifically Wilson-dependent late-response bound.

## 5. What is (and is not) accomplished

**Proved in actual finite nonlinear SU(2) Wilson Hamiltonians:** JT1–JT4, under the previous private-edge comparison and the previously proved cap-source Dirichlet bound. Their constants are volume independent if the electric coefficients are uniformly bounded. **Proved in a separate reversible diffusion:** JT5–JT8 for every preset N. **Not proved:** a uniform sign, cancellation or magnitude estimate of the center-even late-coupling inverse-energy mixed response

\[
\mathfrak L_{a,g}(s)=\int_s^1\frac{\left[\operatorname{Re}\langle Q_uk_a^+\Omega_u,G_uQ_uW\Omega_u\rangle\right]_+}{\sqrt{F_a(u)}}du,
\qquad s=C/b_g.
\]

Existing early-layer Harnack yields \(\sqrt{F_a(s)}\ge q_C\alpha_a\); proving \(\mathfrak L_{a_h,g}(s)\le\frac12q_C\alpha_{a_h}\) (or direct final cap minorization) would complete this local cap obligation. JT4 removes only the **UV** part; JT5–JT8 explain why a finite-order Taylor expansion at time zero cannot remove the remaining low-frequency dependence without **additional model-specific structure**. Uniform bulk magnetic deletion, fixed-support nonlinear covariance, regulator-uniform physical mass gap, quartic resolvent and continuum reconstruction remain open.

## 6. Numerical validation and evidential scope

The companion deterministic checker constructs the divided-difference coefficients as *exact rational numbers* for N=0,1,2,4,6 and epsilon=1/100,1/1000, verifies all moments 0,...,N vanish exactly, and verifies strict positivity at sampled positive times using 70-digit arithmetic. It evaluates the diverging inverse response and individual first-moment bounds. Separately it diagonalizes the **continuous SU(2) class-rotor Wilson Hamiltonian** in a 160-character truncation at b=25,100,400 and u=4/b, 1/4, 1, verifying JT1–JT2. The rotor checks SU(2) algebra and is **not** an interacting eight-face/fully connected Penrose simulation. The 160-character truncation is numerically converged at the checked parameters; it does not constitute a proof of JT1–JT4, which are analytic.
