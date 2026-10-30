# The Singular Boundary — Shared-edge Gaussian tangent second-moment audit and corrected nonlinear proof obligation

**Date:** 2026-10-28. **Status:** new exact finite-dimensional Gaussian-tangent spectral-moment identity and asymptotic counterexample to adopting a uniform second moment as a universal physical-gap prerequisite. The interacting nonlinear Penrose SU(2) source variance, mixed force cancellation and mass gap remain **OPEN**. This document does **not** transfer Gaussian conclusions to the interacting Wilson vacuum.

## 1. Motivation and provenance

The live audit-branch `R3_IR_WEIGHTED_SCORE_SECOND_SPECTRAL_MOMENT_2026-10-28.md` (WS-1–WS-9) proves, for an actual interacting finite SU(2) vacuum and fixed physical support, `m_2(A_h) <= C h^-3`. Its recommended optional next target `||L_h Y_h||^2=O(h)` would imply `m_2(A_h)=O(1)` and nonvanishing critical-source variance, provided the previously proved macroscopic positive-test `m_1(A_h)>=m_*>0`. Earlier `R3_IR_DUAL_CHEEGER_GAUSSIAN_RESPONSE_2026-10-28.md` (GC-1–GC-4) proves a uniform *Gaussian tangent* variance upper bound and a source-specific spectral threshold, but does not calculate the exact critical-source **second energy moment** in the genuine shared-link incidence model. We fill that missing reference calculation and audit whether the O(1) second-moment target is naturally compatible with the strong-magnetic tangent theory. No claim of Stage7/26 coefficient matching is made.

## 2. Fully gauge-reduced shared-edge Gaussian tangent Hamiltonian

Let G be a finite connected, simply connected, oriented rhombus disk, F faces, E links. Let B be the F-by-E signed face-edge incidence matrix, L=BB^T. On such a disk B has rank F and L is positive definite, even with shared interior links. Quotienting the linearized gauge gradients removes `ker B`. For 3 su(2) colors in face curvature variables `w_f∈R^3`, with uniform positive electric `a` and magnetic `b`, the exact Gaussian tangent Hamiltonian is

`H_G = -a sum_{fg} L_fg (∇_{w_f}·∇_{w_g}) + (b/8) sum_f |w_f|²`.

This is the quadratic tangent reference to, **not** the nonlinear SU(2) Wilson Hamiltonian. Its unique normalized ground state has each color's covariance matrix

`Sigma=(1/2)*sqrt(8a/b)*L^(1/2) = sqrt(2a/b) L^(1/2)`.

Diagonalize L=U diag(lambda_i)U^T and put `sigma_i= sqrt(2a lambda_i/b)`. The exact ground-state diffusion generator in each color is

`mathcal L = a sum_fg L_fg ∂_f∂_g - sum_fg D_fg w_g ∂_f`, with `D=a L Sigma^(-1)=sqrt(ab/2)L^(1/2)`.

Thus `D_i=a lambda_i/sigma_i=sqrt(ab lambda_i/2)`; a centered mode-square `w_i²−sigma_i` is an eigenfunction of the vacuum diffusion with eigenvalue `−2D_i` (for the quantum excitation K the energy is `2D_i=sqrt(2ab lambda_i)`). All states and observables here are in the **linearized gauge-quotient** sector.

## 3. Theorem GS-1: exact three physical spectral moments for arbitrary signed face weights

For any real face weights q, write Q=diag(q_f), `Qtilde=U^T Q U`. Define the centered critical source

`A_h=(Y_h−E Y_h)/sqrt(h)`, `Y_h=(h/8)sum_f q_f |w_f|²`.

Let v, m1, m2 respectively denote the source variance, first and second positive Hamiltonian excitation energy moments in the Gaussian ground state. Then the exact, finite-dimensional formulas are

`v = (3h/32) sum_ij Qtilde_ij² sigma_i sigma_j;`

`m1 = (3a h/16) sum_ij lambda_i Qtilde_ij² sigma_j;`

`m2 = (3h/8) sum_ij Qtilde_ij² sigma_i sigma_j ((D_i+D_j)/2)².`

**Proof.** The vacuum is the product over the three colors of centered Gaussians with covariance Sigma. Wick's identity for a real Gaussian vector z gives `Var(z^T Q z)=2 tr(Q Sigma Q Sigma)`. Since `A_h=(sqrt(h)/8) sum_color (z^TQz−tr Q Sigma)`, summing three colors proves v. The Dirichlet identity is `m1=E Γ(A_h)`, with `∇A_h=(sqrt(h)/4)Qz`; the face kinetic matrix is a L. This gives the m1 formula. The exact ground-state generator acts on A as

`mathcal L A_h = −(sqrt(h)/4)sum_color [z^T S z − tr(S Sigma)]`, `S=(Q D+D Q)/2`.

Again applying Wick gives `m2=E|mathcal L A_h|²=(3h/8)tr(S Sigma S Sigma)`, which in the eigenbasis yields the displayed m2 formula. By the ground-state intertwiner `K A_h Omega=−(mathcal L A_h)Omega`, this is precisely the second **excitation energy** moment. No appeal to perturbation or a mass-gap assumption occurs. QED.

## 4. Theorem GS-2: exact trace formulas and non-uniform strong-field second moment

Choose the nonnegative constant macroscopic test q_f=1. Then Q=I commutes with L, and the exact formulas reduce to

`v_h = (3a h/(16b)) tr(L) = (3a h F)/(4b);`

`m1_h = (3a h/16) sqrt(2a/b) tr(L^(3/2));`

`m2_h = (3 a² h/8) tr(L²).`

For a rhombus disk, `tr L=4F`, `tr L²=16F+sum_f deg_dual(f)` and therefore `16F<=tr L²<=20F`. The eigenvalues obey `0<lambda_i<=8`; Jensen's inequality with average lambda=4 gives `8F <= tr L^(3/2) <= 8sqrt(2) F`.

At strong magnetic coupling `b=beta/h²`, for a family of bounded-positive-physical-area patches satisfying `0<c_F<=h² F<=C_F<∞` one therefore obtains **matching sharp orders**

`v_h = Theta(h) ->0`, `m1_h=Theta(1)`, `m2_h=Theta(h^-1) ->∞`.

In particular, the candidate universal improvement `m2_h=O(1)` is **false in the natural Gaussian tangent model with fully coupled shared-edge kinetic energy**. The Gaussian theory also has a strictly positive finite-area gauge-quotient gap by the previous GC-3 Cheeger theorem, since all two-quantum source excitations have energies `sqrt(2ab lambda_i)>=c>0`. Thus positive spectral gap and `m2_h ->∞` coexist with a vanishing source variance. This is NOT a counterexample to a statement restricted specifically to the nonlinear SU(2) Hamiltonian, because the tangent model is a distinct theory.

The **first spectral moment cannot be inferred from the second alone**: here it remains O(1) because a vanishing variance carries spectral energy predominantly at UV scales of order 1/h. The exact Cauchy lower bound `v_h>=m1_h²/m2_h` has the correct h power but cannot establish a nonzero continuum variance.

## 5. Original three-rhombus spatial Penrose fixture

The authentic 3-face, 10-edge Z^5 spatial fixture (not temporal Q14) has dual face matrix eigenvalues `4−sqrt(2),4,4+sqrt(2)`. It satisfies `tr L=12` and `tr L²=52`, while the Cheeger lower bound is separately valid. The exact formulas become `v_h=9 a h/(4b)`, `m2_h=39 a² h/2`; and `m1_h=(3ah/16)sqrt(2a/b)[(4−sqrt2)^(3/2)+8+(4+sqrt2)^(3/2)]`. These are *finite fixture* identities, not the positive-area refinement limit. The verifier reconstructs the signed face-edge incidence and checks exact eigenvalues/ranks and formulas.

## 6. Theorem GS-3: exact nonlinear force-cancellation gate, not an assumed conclusion

For the **actual** finite nonlinear SU(2) ground state (not tangent), take `A_h=(Y_h−EY_h)/sqrt(h)` and the existing exact decomposition `mathcal L Y_h = D_h+F_h` into geometric and vacuum-score forces. Then

`m2_h = (1/h) [E D_h²+2 E D_h F_h+E F_h²]`.

The previous WS-1 gives only the bound `m2_h=O(h^-3)`. The Gaussian shared-link benchmark instead has `m2_h=Theta(h^-1)`, arising from substantial cancellation within the square. To obtain `m2_h=O(h^-1)` in nonlinear SU(2) would require an independently proved estimate `E(D_h+F_h)²=O(1)`; to obtain `m2_h=O(1)` would require the considerably stronger `E(D_h+F_h)²=O(h)`. **Neither cancellation has been established for the nonlinear Penrose ground state**. The formulas above do not assume that the nonlinear vacuum resembles the tangent reference in any norm uniform in h.

A separate field-construction gate is required: the Gaussian α=3/2 variance **collapses**, despite the tangent model being gapped. The user's ultimate goal of a nontrivial interacting continuum requires testing other renormalized composites/normalizations and proving bounded nonzero variance, rather than declaring an O(1) second spectral moment necessary for a positive gap.

## 7. Evidence classification and next proof obligation

**Exactly proved:** GS-1 and GS-2 for the shared-edge SU(2) *Gaussian tangent* on any disk, with exact signed-source spectral moments; GS-3 is a tautologically exact nonlinear force decomposition but does not close an interacting estimate. The deterministic verifier checks incidence, Gaussian Wick/OU identities and trace bounds; no Monte Carlo or user-provided historical simulation alteration.

**Still open:** nonlinear SU(2) `E(D_h+F_h)²=O(1)` (the weaker, Gaussian-compatible cancellation benchmark), nonlinear critically normalized source variance classification, higher-source physical resolvents, source-level original Stage7/26 equivalence, infinite-volume spectrum, nontrivial quantum continuum and a positive physical mass gap.

**Recommended next direct proof task:** bound the interacting **joint force covariance** `2E D_hF_h` using the Wilson eigenstate equation or a source-weighted commutator Ward identity, without importing the Gaussian cancellation. If impossible from existing information, produce a counterexample to the proposed inference and keep the ledger open. Verify nontriviality independently of gap positivity.
