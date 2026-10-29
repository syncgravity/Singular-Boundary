# R3-IR — Reflection-odd coefficient asymmetry and quadratic sector-gap cap stability

**Research date:** 2026-10-29. **Status:** exact finite nonlinear physical SU(2) Wilson Hamiltonian theorem, for a reflection-symmetric **graph** and exactly paired electric coefficients but *unequal paired magnetic coefficients*. The complete proof, full deterministic checker, execution log and checksums are in the archived package singular_boundary_reflection_asymmetry_stability_2026-10-29.zip (SHA256 1650a08cd3da83d318de8bea3898d328169f1af49ab88e65c710b0a401f4b8bb). This theorem does **not** settle generic asymmetric Penrose geometry, a uniform physical mass gap, or continuum reconstruction.

## AS-1 — Reflection parity resolves the exact interacting ground-state response

Let H0 be the exact finite SU(2) Wilson Hamiltonian with a deleted target magnetic term on a link-free reflection-seam graph meeting the earlier RS hypotheses. Thus a unitary involution R exchanges the two halves, [H0,R]=0, and the unique strictly positive physical ground state Omega0 is R-even. Let E0 be its energy and define the strictly positive finite-volume parity-sector gaps
\[
 \delta_+=\inf\sigma(H_0|_{\mathcal H_+\cap\Omega_0^\perp})-E_0,\qquad
 \delta_-=\inf\sigma(H_0|_{\mathcal H_-})-E_0.
\]
No regulator-uniform lower bound is assumed for these numbers. Let D be any bounded real self-adjoint perturbation satisfying R D R = -D and norm ||D||<=epsilon. Define H=H0+D, its normalized positive ground state Omega and energy E. The exact parity selection <Omega0,D Omega0>=0 and the variational principle imply E<=E0.

Decompose Omega=u+v, u=P_+Omega, v=P_-Omega, and u=c Omega0+w with w in even excited space and c=<Omega0,Omega>>0. Since D flips parity, the actual nonlinear ground-state equation gives the **exact** identities
\[
 (H_{0,-}-E)v=-P_-Du,\qquad
 Q_+(H_{0,+}-E)w=-Q_+Dv,
\]
where Q_+=P_+-|Omega0><Omega0|. As E<=E0, the first resolvent has norm <=1/delta_- and the second <=1/delta_+. Consequently, for
\[
 r=\epsilon/\delta_-,\qquad s=\epsilon^2/(\delta_+\delta_-)
\]
one obtains
\[
\boxed{\|v\|\le r,\qquad\|w\|\le s,\qquad c\ge\sqrt{[1-r^2-s^2]_+}.}
\]
The even excited-sector distortion is quadratic in the bounded *reflection-odd* magnetic mismatch. This is a direct finite-volume operator inequality, not a Taylor expansion requiring analytic continuation to full coupling.

## AS-2 — Exact asymmetric center-cap stability

For a reflection-invariant measurable event B, its multiplication projection M_B commutes with R, so
\[
m(B)=\|M_B\Omega\|^2=\|M_Bu\|^2+\|M_Bv\|^2
\ge[c\sqrt{m_0(B)}-\|w\|]_+^2.
\]
Thus
\[
\boxed{
m(B)\ge
[\sqrt{[1-r^2-s^2]_+}\sqrt{m_0(B)}-s]_+^2.
}
\]
The deleted-face SU(2) geodesic center cap B_a is invariant under seam reflection. The preceding reflection-seam theorem proves m0(B_a)>=H(a/2), H(a)=(a-sin(2a)/2)/pi. Hence
\[
\boxed{
m_{\mathrm{asym}}(B_a)\ge
[\sqrt{[1-r^2-s^2]_+}\sqrt{H(a/2)}-s]_+^2.
}
\]
In particular
\[
\boxed{r\le1/2,\qquad s\le\sqrt{H(a/2)}/4
\quad\Longrightarrow\quad m_{\mathrm{asym}}(B_a)\ge H(a/2)/4.}
\]
The last implication follows from sqrt(1-r²-s²)>=sqrt(11)/4 and (sqrt(11)-1)^2/16>1/4. At a_h=acos(1-h), H(a_h/2)=(sqrt(2)/(6pi)+O(h))h^(3/2). Thus the sufficient mismatch threshold is
\[
\epsilon\le\delta_-/2,\qquad
\epsilon\le\tfrac12\sqrt{\delta_+\delta_-}H(a_h/2)^{1/4}
=O(\sqrt{\delta_+\delta_-}h^{3/8}).
\]
This improves the naive first-order full-state closeness requirement O(delta0*h^(3/4)) when parity gaps are comparable. Under the same previous Wilson coefficient hypotheses, the cap lower bound supplies the **conditional** O(h^-1 log(1/h)) deletion-energy estimate for this near-reflection class.

## AS-3 — Exactly which coefficient mismatch is covered

On a graph retaining the seam involution with paired electric coefficients, let b_{q+},b_{q-} be two nonnegative reflected magnetic face coefficients. Define their average bar b_q and difference eta_q=(b_{q+}-b_{q-})/2. Retain the same seam-crossing face coefficients. Then H=H0+D with
\[
 D=\sum_q\eta_q[d_{q+}-d_{q-}],\quad
 d_q=1-\tfrac12\operatorname{ReTr}W_q\in[0,2],\quad
 \boxed{\|D\|\le\sum_q|b_{q+}-b_{q-}|.}
\]
The SU(2) interaction remains fully nonlinear and all retained magnetic couplings are at their physical strengths. However, the theorem requires **small aggregate absolute mismatch relative to the parity sector gaps**, an exact reflection of the graph, and paired electric coefficients. Unequal electric Laplacians produce an unbounded perturbation and are **not** covered by this theorem. Generic Penrose patches without a reflecting graph involution are likewise outside its scope.

## AS-4 — Positivity of crossing kernels alone does not fix asymmetric character signs

The abstract half-side cone method cannot simply replace identical half-side operators A_x+A_y with arbitrary positive halves A_x+B_y. On the two-point space s,t=+-1, choose nonnegative kinetic a[(I-X)_s+(I-X)_t], a nonnegative ferromagnetic crossing J(1-st), and nonnegative asymmetric half-potentials M 1_{s=-1}+M 1_{t=+1}. The crossing Boltzmann kernel exp(J st) is positive definite, but the positive ground state concentrates at anti-aligned (+,-) as M grows. Since the ground energy is <=2a+2J and the Hamiltonian is >=M(1-P_{+,-}), one proves
\[
 \langle st\rangle\le-1+2(2a+2J)/M<0\quad\text{when }M>2(2a+2J).
\]
This is an analytic **abstract counterexample**, not a physical Wilson lattice.

Even using the *actual SU(2) character kernels* on the sampled group points I and i sigma_3, the fundamental-trace Gram kernel has diagonal 1 and off-diagonal 0, while the spin-one-character Gram kernel has diagonal 3 and off-diagonal -1; both are positive definite. The crossing Wilson weight exp(Jp) is positive definite, yet the same asymmetric local half-potentials yield a **negative** spin-one expectation. This discrete sampled-kernel example still is **not** the continuous-Haar Gauss-invariant SU(2) Hamiltonian, and must not be represented as a counterexample to its character-positivity conjecture. It only rules out extrapolating RS-1–RS-3 from positive crossing kernels and arbitrary unmatched half-side operators.

## Verification and remaining obligations

The companion Python verifier checks reflection-parity sector gaps and both exact resolvent inequalities, asymmetric cap probability, h^(3/8) scaling, positivity of abstract and SU(2)-sampled crossing kernels, and negative asymmetric sample expectations. The models are finite comparisons and **do not diagonalize** the eight/nine-face physical SU(2) Wilson Hamiltonian. No Monte Carlo, no historical Stage26 modifications.

**PROVED under stated hypotheses:** AS-1–AS-3 and abstract comparator AS-4. **OPEN:** a gap-independent and reflection-free full-coupling deleted-face lower probability for arbitrary connected asymmetric Penrose interiors; quantitative even/odd sector gap bounds strong enough for refinement; fixed-support nonlinear covariance, physical mass gap, quartic resolvent, continuum reconstruction.
