# The Singular Boundary — Self-absorbing nonlinear bulk magnetic-response estimate

**Date:** 2026-10-29. **Branch:** `audit/2026-10-28-independent-reconstruction`. **Status:** exact finite, genuine interacting SU(2) Hamiltonian theorem, conditional refinement consequences for declared Penrose couplings. **Not proved:** a small adverse low-energy response, a bulk magnetic-deletion estimate without that response, global spectral gap, nontrivial continuum source, quartic resolvent, Stage7/26 provenance.

## 1. Model; every interior target admits a one-neighbor bridge

Let G be a finite simply connected edge-to-edge planar rhombus disk, with four distinct links per plaquette and at most two faces incident on each link. On the Gauss-invariant physical Hilbert space use

\[
H=\sum_e a_e(-\Delta_e)+\sum_k b_k d_k,\qquad d_k=1-p_k,\quad p_k=\tfrac12\operatorname{ReTr}W_k,
\]

where `0<a_e<=a_*`, and `b_k>0`. For any interior plaquette f choose **one** adjacent plaquette g sharing an edge. In the full coupling rectangle

\[
H(u,t)=H-b_fd_f-b_gd_g+t d_f+u b_gd_g,\qquad 0\le u\le1,\quad0\le t\le b_f,
\]

the reference at u=0 has a private link of f: the link shared with g no longer appears in any magnetic term other than t d_f. The previously independently proved private-edge variational inequality applies **regardless of all other lattice cycles**:

\[
D(0):=E(0,b_f)-E(0,0)\le B_f:=\frac3{2\sqrt2}\sqrt{A_fb_f},\quad A_f=\sum_{e\in\partial f}a_e.
\]

The same argument applies to any face with a private link without removing g. This combinatorial reduction requires exactly *one* magnetic neighbor for every fully interior face. It is not an assertion that the full nonlinear system factorizes.

For each (u,t), the full compact elliptic Hamiltonian has a unique positive gauge-invariant ground state \(\Omega_{u,t}\) and analytic energy E(u,t). Write K=H(u,t)-E, Q=I-|\Omega\rangle\langle\Omega|, and physical spectral projections P_{(0,\Lambda]}, P_{>\Lambda}. Set W=b_gd_g and T_g=b_g² A_g, \(A_g=\sum_{e\in\partial g}a_e\).

## 2. Coupling-integrated target-face f-sum: theorem SA-1

For every face, the exact fundamental SU(2) class-function link derivative gives

\[
\Gamma(d_f)=\sum_{e\in\partial f}a_e|\nabla_e d_f|^2
=\frac{A_f}{4}(1-p_f^2)=\frac{A_f}{4}(2d_f-d_f^2)\le\frac{A_f}{2}d_f.
\]

Therefore, for the **actual nonlinear vacuum** at (u,t),

\[
m_1^{u,t}(d_f):=\langle Qd_f\Omega,KQd_f\Omega\rangle
=\mathbb E_{u,t}\Gamma(d_f)\le\frac{A_f}{2}\langle d_f\rangle_{u,t}.
\]

Hellmann–Feynman gives \(E_t=\langle d_f\rangle\). Consequently **at each u**, exactly without a gap assumption,

\[
\boxed{\int_0^{b_f}m_1^{u,t}(d_f)\,dt\le\frac{A_f}{2}D(u),\quad D(u)=E(u,b_f)-E(u,0).}\tag{SA-1}
\]

This is stronger than bounding the first moment at every t by its trivial O(1) maximum: it charges the integrated kinetic moment to the sought deletion cost itself.

## 3. Self-absorbing spectral ultraviolet decomposition: theorem SA-2

The Kato mixed derivative is

\[
E_{ut}=-2\operatorname{Re}\langle Qd_f\Omega,K^{-1}QW\Omega\rangle.
\]

With \(P_{>\Lambda}=1_{(\Lambda,\infty)}(K)\), Cauchy–Schwarz and \(K^{-1}P_{>\Lambda}\le\Lambda^{-2}KP_{>\Lambda}\) on spectral quadratic forms give

\[
|E_{ut}^{>\Lambda}|\le\frac{2}{\Lambda^2}\sqrt{m_1(d_f)m_1(W)}.
\]

Because at most two faces share any link, \(m_1(W)\le b_g^2 A_g/4\) for **one single face** g (rather than the 1/2 bound for a sum of potentially overlapping faces). This improves the constants but is not essential. Combining with SA-1 yields the pointwise bound

\[
\boxed{|E_{ut}^{>\Lambda}|\le\frac{b_g\sqrt{A_fA_g/2}}{\Lambda^2}\sqrt{\langle d_f\rangle_{u,t}}.}\tag{SA-2}
\]

Define the adverse physical **low-energy** susceptibility budget

\[
\mathcal N_f^{\le\Lambda}=2\int_0^1du\int_0^{b_f}dt\,
\left[-\operatorname{Re}\langle Qd_f\Omega,K^{-1}P_{(0,\Lambda]}Q(b_gd_g)\Omega\rangle\right]_+.
\]

No sign assumption is made. Define \(D_*=\max_{0\le u\le1}D(u)\), finite and nonnegative. For any u, integrating SA-2, using Cauchy–Schwarz in t and \(\int_0^{b_f}\langle d_f\rangle dt=D(u)\le D_*\), gives

\[
D(u)\le D(0)+\mathcal N_f^{\le\Lambda}+\frac{b_g\sqrt{A_fA_gb_f/2}}{\Lambda^2}\sqrt{D_*}.
\]

Set \(c_\Lambda=b_g\sqrt{A_fA_gb_f/2}/\Lambda^2\). Taking the supremum,

\[
D_*\le B_f+\mathcal N_f^{\le\Lambda}+c_\Lambda\sqrt{D_*}.
\]

Solve the quadratic exactly or use Young's inequality \(c\sqrt D\le(D+c^2)/2\) to obtain

\[
\boxed{D(1)\le D_*\le2B_f+2\mathcal N_f^{\le\Lambda}+\frac{A_fA_gb_fb_g^2}{2\Lambda^4}.}\tag{SA-3}
\]

No uniform spectral gap, nonlinear Gaussian comparison, conditional covariance, or global Poincare constant has been used. **The improvement of the energy window comes from the self-absorption of D_*.**

## 4. Uniform Penrose consequence: theorem SA-3

Suppose all selected coefficients obey \(a_e\le a_*\), \(b_f,b_g\le\beta_+ h^{-2}\). Choose

\[
\boxed{\Lambda_h=Lh^{-5/4}},\qquad L>0\ \text{fixed}.
\]

Since \(A_f,A_g\le4a_*\), the explicit fourth-power error in SA-3 satisfies

\[
\frac{A_fA_gb_fb_g^2}{2\Lambda_h^4}
\le\frac{8a_*^2\beta_+^3}{L^4}\,h^{-1}.
\]

The bridge term obeys \(2B_f\le3\sqrt{2a_*\beta_+}\,h^{-1}\). Hence for **every interior rhombus**, independent of how many faces surround it,

\[
\boxed{\Delta_f(H)\le2\mathcal N_f^{\le Lh^{-5/4}}+\left(3\sqrt{2a_*\beta_+}+\frac{8a_*^2\beta_+^3}{L^4}\right)h^{-1}.}\tag{SA-4}
\]

The earlier direct ultraviolet cutoff had to be h^(-3/2) after reducing the cycle closure to a single adjacent face (or h^(-2) for a set of h^(-2) faces). SA-4 reduces this to **h^(-5/4)** while retaining a completely interacting SU(2) physical-sector proof. This is an exact *conditional-response* reduction, **not** an unconditional O(h^-1) deletion theorem.

For a general set B of m_h cycle-closing magnetic faces, the overlapping-gradient estimate \(m_1(W)\le\frac12\sum_g c_g^2A_g\), together with the same argument, gives

\[
D(1)\le2B_f+2\mathcal N_f^{\le\Lambda}+\frac{A_fb_f}{\Lambda^4}\sum_{g\in B}c_g^2A_g.
\]

Thus \(\Lambda=Lh^{-5/4}m_h^{1/4}\) suffices to keep the ultraviolet contribution O(h^-1) for any m_h, improving the previous h^(-3/2)m_h^(1/4) cutoff. The one-neighbor reduction is sharper and needs no m_h factor.

## 5. A necessary low-energy obstruction if bulk extreme defects persist: theorem SA-4

Assume in addition \(b_f\ge\beta_-h^{-2}\), and \(A_f\le4a_*\). The previously proved **single-face deletion Laplace** estimate gives, for a fixed \(0<\zeta<1\),

\[
\mathbb P_\Omega(d_f\ge\delta)
\le\exp\left[\frac{\Delta_f}{\sqrt{A_fb_f/8}}\operatorname{artanh}\zeta
-\zeta\delta\sqrt{\frac{8b_f}{A_f}}\right].
\]

For \(\delta_h=h^{3/4}\), the exponent is at most \(C_1 h\Delta_f-c_1h^{-1/4}\), with positive constants depending on \(a_*,\beta_-\), and on a **lower** positive bound for A_f or equivalently choose the ratio using the conservative A_f≤4a_* and b_f≥β_-h^-2 carefully. To avoid requiring an electric lower bound for the positive \(h\Delta_f\) coefficient, choose the fixed *common* allowed exponential parameter \(s_h=\zeta\sqrt{8\beta_-/ (4a_*)}\,h^{-1}\). Then s_h√(A_f/(8b_f))≤\zeta; the artanh factor is bounded by a constant multiple of s_h/b_f and hence <=C h times \(\Delta_f\), without an A_f lower bound. Thus

\[
\boxed{\mathbb P_\Omega(d_f\ge h^{3/4})\le\exp(C_1h\Delta_f-c_1h^{-1/4}).}\tag{SA-5}
\]

For a fixed-area face set with \(|D_R|\le C_Fh^{-2}\), if the event \(\{\max_{f\in D_R}d_f\ge h^{3/4}\}\) has probability at least \(\varepsilon>0\), at least one face has probability >=\(\varepsilon/(C_Fh^{-2})\). Rearranging SA-5 gives, for this face and small h,

\[
\Delta_f\ge (c_1/C_1)h^{-5/4}-O_\varepsilon(h^{-1}\log(1/h)).
\]

Boundary private-edge faces already have \(\Delta_f=O(h^{-1})\). For the remaining interior face, SA-4 forces

\[
\boxed{\mathcal N_f^{\le Lh^{-5/4}}\ge c_2h^{-5/4}}\qquad\text{along any such subsequence.}\tag{SA-6}
\]

**Interpretation:** persistent fixed-area extreme-defect probability in the actual interacting vacuum would require an anomalously large **adverse low-energy mixed magnetic response** involving at most **one adjacent face**. The existence of this response, or of persistent defects, is not asserted. Conversely any bound \(\sup_{f\in D_R}\mathcal N_f^{\le Lh^{-5/4}}=O(h^{-1}\operatorname{polylog}^k(1/h))\) would exclude all such defects with stretched-exponentially small probability, thereby meeting the previously proved sparse-defect source-equivalence criterion. A nontrivial continuum field or a physical gap still would not follow.

## 6. Exact checks, provenance and limitations

The companion deterministic verifier checks the exact SU(2) one-face f-sum and its integral against actual interacting character-basis ground energies; symbolic constants in SA-1 through SA-5; existence of an adjacent magnetic face at every interior face; and the original three-rhombus ten-edge Penrose **spatial** seed. Larger square-grid incidences are explicitly marked as comparison fixtures. No Monte Carlo or alteration of original Stage7/26 evidence is performed.

**Proved:** SA-1 and SA-2 at every finite nonlinear SU(2) regulator; SA-3 and SA-4 with stated coefficient assumptions; the conditional extreme-defect obstruction SA-6. **Open:** bound on \(\mathcal N_f^{\le Lh^{-5/4}}\) in the full cycle-rich Penrose vacuum; any unconditional uniform bulk deletion bound; fixed-support nonlinear Wilson-angle equivalence; physical positive gap; quartic resolvent; full continuum reconstruction and Stage7/26 source-level identification.