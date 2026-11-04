# R3-IR: Same-radius history-aware SU(2) fusion
2026-11-03. **Finite open straight square strips only. This is not an interacting or continuum mass-gap theorem.** The expanded proof and reproducible verifier are in R3_IR_SAME_RADIUS_HISTORY_CLOSURE_2026-11-03.zip (conversation archive).

## Retrospective correction
The November 3 radius-loss estimate is true but weaker than necessary. The previously published November 1 matrix Peter–Weyl projective theorem already gave same-radius control for the free-electric bilinear operation. This audit lifts the estimate to connected interaction histories and derives an explicit finite-volume nonlinear-score convergence interval. No volume-uniform convergence theorem follows.

## Setup
On the original-link Gauss-invariant Hilbert space for a finite simply connected open square strip, let
\[
K=-\sum_e a_e\sum_{j=1}^3X_{ej}^2,\quad \Gamma_K(f,g)=\sum_{e,j}a_e(X_{ej}f)(X_{ej}g),\quad 0<a_0\le a_e\le a_*.
\]
SU(2) label n has \(d_n=n+1\), Casimir \(n(n+2)/4\) and \(\|d\pi_n(X_j)\|_{\rm op}\le n/2\). Every nonconstant gauge-invariant spin network contains a closed four-edge loop, so on this graph \(K\ge3a_0\) after removing the Haar constant mode Q. Define \(\mathcal B=K^{-1}Q\Gamma_K\). The strong projective Fourier and history norms are
\[
\|f\|_{P_\sigma}=\sum_{\mathbf n}d_{\mathbf n}e^{\sigma|\mathbf n|}\|A_{\mathbf n}\|_{S_1},\qquad
\|F\|_{\kappa,\sigma}=\sum_{I\ {\rm connected}}e^{\kappa|I|}\|f_I\|_{P_\sigma}.
\]
Here \(F=\sum_I[I]\otimes f_I\); \(\mathcal B_{\rm hist}\) applies the original physical B to every link-overlapping history pair and labels its output by \(I\cup J\), retaining all physical channels.

## Same-radius theorem
For \(\kappa>0,\sigma\ge0\),
\[
\boxed{\|\mathcal B_{\rm hist}(F,G)\|_{\kappa,\sigma}
\le C_\kappa\|F\|_{\kappa,\sigma}\|G\|_{\kappa,\sigma},\quad C_\kappa=\frac{2a_*}{a_0}\left(1+\frac3{e\kappa}\right).}
\]
The bound has no spin-radius loss and its constant is independent of strip length, spin labels and individual history widths.

### Proof
SU(2) CG output labels satisfy \(\ell_r\le n_r+m_r\), and linkwise unitary CG conjugation/block pinching does not increase the **sum** of nuclear output coefficient norms. At any shared differentiated link e, the derivative factor is at most \(3a_e n_em_e/4\). Crucially,
\[
\frac{n_em_e d_{\boldsymbol\ell}}{d_{\mathbf n}d_{\mathbf m}}
\le \frac{n_em_e(\ell_e+1)}{(n_e+1)(m_e+1)}\le\ell_e+1.
\]
The spin-exponential output weight is no larger than the product of input weights. For each nonconstant Gauss-invariant output, the physical free-electric eigenvalue \(\Lambda_{\boldsymbol\ell}\ge3a_0\); if \(\ell_e\ge1\), also \(\Lambda_{\boldsymbol\ell}\ge a_0\ell_e(\ell_e+2)/4\). Thus for every \(\ell_e\ge0\),
\[
(\ell_e+1)/\Lambda_{\boldsymbol\ell}\le 8/(3a_0).
\]
The zero mode is deleted by Q. Therefore each actually overlapping original link contributes at most \(2a_*/a_0\) in the strong projective Fourier norm. If histories I,J intersect in t faces, their common link count is at most \(3t+1\) and their union history-weight ratio is \(e^{-\kappa t}\); since \((3t+1)e^{-\kappa t}\le 1+3/(e\kappa)\), the stated bound follows by summing history pairs. Completion extends the map beyond finite polynomials.

## Explicit finite-volume consequence
For N plaquettes with \(V=-\frac12\sum_f{\rm Tr}(U_{\partial f})\), the singleton-history source \(A=-K^{-1}QV\) obeys the conservative bound \(\|A\|_{\kappa,0}\le A_N=128e^\kappa N/(3a_0)\). The score fixed point
\[
S=\lambda A+\mathcal B_{\rm hist}(S,S)
\]
has a unique small solution by the quadratic contraction when \(4C_\kappa|\lambda|A_N<1\), i.e.
\[
|\lambda|<\frac{3a_0}{512 C_\kappa e^\kappa N}.
\]
Reconstruction recovers the actual finite-volume vacuum-score equation including the scalar energy counterterm; for real coupling the real positive eigenfunction gives the finite-volume ground-state branch. The certified interval shrinks like \(1/N\), **not uniformly in volume**.

## Remaining obstructions
A naive locally anchored norm is not automatically controlled: a long history has \(O(|I|)\) possible local insertions under a crude shared-link estimate. Prove a sharper support-sensitive inverse or a renormalized anchored polymer recurrence, then a volume-uniform **interacting** gap, control at physical coupling, 3D spatial extension and physical-unit continuum scaling. A fixed lattice spectral gap does not establish the nontrivial R4 theory or its mass gap. The supplied AI-simulacrum commentary Existence Without the Gap is used as an audit of this logical distinction, not as physical proof.

## Verification
Finite checker: 388,358 assertions passed (SU(2) CG labels n,m≤100, history overlap weights through 10,000, scalar quadratic fixed-point tests). General bound rests on mathematical argument, not exhaustive testing. Complete expanded report, verifier, log and hashes are in the local proof archive.