# R3-IR — Mesoscopic Wilson-loop flatness in density, not temporal mixing

**Date:** 2026-10-28. **Evidence status:** elementary SU(2) discrete-holonomy theorem independently proved, combined with the previously established *conditional-on-declared-coefficients* interior regional curvature estimate MI-3. No Monte Carlo, historical-data regeneration, or spectral-gap claim.

## 1. Exact pointwise nonabelian Wilson deficit inequality (LW-1)

For any SU(2) matrix U, define \(d(U)=1-\frac12\operatorname{ReTr}U\in[0,2]\). The Hilbert–Schmidt identity \(\|I-U\|_{HS}^2=4d(U)\), together with \(I-UV=(I-U)+U(I-V)\), proves for every finite sequence \(U_1,\ldots,U_m\in SU(2)\)

\[
\sqrt{d(U_1\cdots U_m)}\le\sum_{i=1}^{m}\sqrt{d(U_i)},\qquad
\boxed{d(U_1\cdots U_m)\le m\sum_{i=1}^m d(U_i).} \tag{LW-1}
\]

This is invariant under replacing each factor by an arbitrary conjugate or inverse. For an embedded simply connected union Q of m rhombi that is a topological disk with a simple oriented boundary, the discrete nonabelian Stokes/van Kampen identity expresses its boundary holonomy, up to conjugacy, as an **ordered** product of m individually transported face holonomies (and inverses). Apply LW-1 to conclude

\[
\boxed{d(W_{\partial Q})\le m\sum_{f\in Q}d(W_f).} \tag{LW-2}
\]

There is no assertion that noncommuting plaquette matrices multiply without the necessary transports or ordering. The bound is exact for *all* configurations and does not assume near-identity holonomies, a particular gauge, an interacting ground state, or Wilson dynamics.

## 2. Rooted finite-patch averaging theorem (LW-2)

Let D be a nonempty finite face subset of an edge-degree-at-most-four rhombus disk. For each root face f in D, choose any topological disk \(Q_f\subseteq D\) containing f, with at most k faces. The choice can vary arbitrarily with f, provided k≥1 is common. Let

\[\delta_D=|D|^{-1}\sum_{g\in D}\mathbb E_{\nu_G}d(W_g),\qquad
\bar W_D=|D|^{-1}\sum_{f\in D}\tfrac12\operatorname{ReTr}W_{\partial Q_f}.\]

If g occurs in Q_f, the dual face-graph distance from f to g is at most k−1. The maximum face-graph degree is four, so at most

\[M_k=1+4\sum_{j=0}^{k-2}3^j=2\cdot3^{k-1}-1\]

root faces can contain any fixed g. Summing LW-2 over roots therefore gives

\[
\boxed{0\le\mathbb E_{\nu_G}(1-\bar W_D)\le kM_k\delta_D.} \tag{LW-3}
\]

Since \(0\le1-\bar W_D\le2\), the same model's interacting ground state satisfies the **vacuum mean-square bound**

\[
\boxed{\| (\bar W_D-I)\Omega_G\|^2\le2kM_k\delta_D,\quad
\operatorname{Var}_{\nu_G}(\bar W_D)\le2kM_k\delta_D.} \tag{LW-4}
\]

Here \(\bar W_D\) is the *multiplication operator* by the gauge-invariant average trace, and \(I\) denotes the constant multiplier. The Hilbert spaces depend on the regulator, so this is not a claim of strong operator convergence on one fixed continuum Hilbert space.

If a root f is chosen uniformly from D, independently of U~ν_G, the Markov estimate is

\[\mathbb P\{d(W_{\partial Q_f})>\epsilon\}\le kM_k\delta_D/\epsilon. \tag{LW-5}\]

For arbitrary q rooted disk families \(Q_{f,1},\ldots,Q_{f,q}\), each with at most k faces and containing f, and arbitrary positive integer powers \(m_j≥1\), each deficit is between 0 and 2. Thus

\[
\frac1{|D|}\sum_f\mathbb E\prod_{j=1}^q d(W_{\partial Q_{f,j}})^{m_j}
\le2^{\sum_jm_j-1} kM_k\delta_D. \tag{LW-6}
\]

This is a **density-averaged finite joint moment bound** and is valid without any correlation decay. It gives neither bounds at a prescribed root nor a decay estimate as the distance between roots increases.

## 3. Penrose interior mesoscopic consequence (LW-3)

Under the **declared, not yet Stage26-source-certified** geometric coefficients and the interior-ball assumptions of MI-3, let D_R be the faces whose centers lie in a physical ball of radius R, set r=R/h>1 and \(\varphi=(1+\sqrt5)/2\). The prior theorem provides

\[\delta_{D_R}\le\Delta(h,R):=\frac{3\varphi}{\sqrt2}g_3^2h+16\varphi^2\frac{r+1}{(r-1)^2}.\]

Therefore for each uniformly bounded patch size k,

\[
\boxed{\| (\bar W_{D_R}-I)\Omega_{h,G}\|^2
\le2k(2\cdot3^{k-1}-1)\Delta(h,R).} \tag{LW-7}
\]

If h→0 with h/R(h)→0 and the complete interior collar assumption persists, the right side tends to zero even if R(h)→0. Thus **unrenormalized bounded-complexity contractible Wilson loops become trivial in location-averaged vacuum L²**, and their finite joint deficit moments vanish in the same sense.

A slowly increasing complexity k(h) is permissible whenever \(k(h)3^{k(h)}\Delta(h,R(h))\to0\). For R(h)=√(hℓ) with fixed ℓ>0, \(\Delta=O(\sqrt{h/\ell})\); choosing \(k(h)=\lfloor c\log(\ell/h)\rfloor\) with \(0<c<1/(2\log3)\) suffices. All such contours shrink in physical diameter under this construction. This is a **necessary renormalization warning** for R2, not a nontrivial continuum field construction.

## 4. Selection and reproducibility

The exact read-only checker \`scripts/audit/verify_mesoscopic_wilson.py\` uses the three original canonical spatial seed rhombi (10 distinct edges) and verifies that all six nonempty connected subsets have simple boundaries of length 4, 6, or 8. It checks the noncommutative SU(2) boundary deficit inequality under seven deterministic rational-quaternion link assignments, for **42 exact rational comparisons**, together with one rooted k=2 patch cover whose maximum multiplicity is three. These finite checks support, but do not replace, the general algebraic proof.

External context for ordered/nonabelian discrete Stokes: Phys. Rev. D **62**, 025019 (2000), DOI 10.1103/PhysRevD.62.025019 (specifically distinguishes path ordering from naive abelian-style products). The proof above uses only the elementary group word peeling/van Kampen relation and the matrix-norm triangle inequality.

### Consequences and limitations

- **Independently proved:** pointwise contractible Wilson boundary-deficit inequality, rooted average/moment bounds, conditional mesoscopic L²-vacuum flatness as an inference from MI-3.
- **Not proved:** pointwise interior face flatness; vacuum covariance decay with physical separation; nontrivial source renormalization; long-connector torque control; regulator- and volume-uniform interacting spectral gap; R2 quantum continuum.
- **Provenance:** the three-face spatial seed is **not** the authentic temporal Q14 cavity. No historical simulations, saved chains, or certificates were modified.

**Next noncircular obligation:** determine whether a suitably renormalized bounded-physical-support Wilson source has **nonvanishing continuum variance** and a dynamical first/low-energy spectral bound. Spatial flattening in density alone does not create the missing temporal mixing estimate.
