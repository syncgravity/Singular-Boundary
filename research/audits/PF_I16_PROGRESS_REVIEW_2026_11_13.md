# PF-I16 progress review and proof-ledger reconciliation

**Review date:** 2026-11-13  
**Repository base:** \`325a77b2c5660a85c51a7da5b32982f293accfc3\`  
**Scope:** independent algebraic and arithmetic review of the corrected rotor, finite-order spatial-tree estimates, and the remaining all-orders gate. This note is a review record, not a new theorem.

## 1. Corrected isolated-rotor input

The radial equation recorded for $q_\beta=s_\beta'$ is
\[
q_\beta'+2\cot\theta\,q_\beta
=-4(q_\beta^2+\beta\cos\theta+\lambda_\beta),
\qquad
\lambda_\beta=-\frac{\int_0^\pi\sin^2\theta\,q_\beta^2\,d\theta}
{\int_0^\pi\sin^2\theta\,d\theta}.
\]
For a smooth regular branch, $q(0)=q(\pi)=0$. Differentiating the ODE gives
\[
q''+2\cot\theta q'-2\csc^2\theta q
=-8qq'+4\beta\sin\theta.
\]
At an interior positive maximum, $q'=0$ and the equation forces
$q''=2\csc^2\theta q+4\beta\sin\theta>0$, a contradiction. At an interior negative minimum, it forces
$q''=2\csc^2\theta q+4\beta\sin\theta\ge0$, hence
$q\ge-2\beta\sin^3\theta\ge-2\beta$. Thus
\[
-2\beta\le q_\beta\le0,\qquad \|s_\beta'\|_\infty\le2\beta.
\]

The weighted-mean identity gives $-4\beta^2\le\lambda_\beta\le0$, so
$h=q^2+\lambda_\beta$ has $\|h\|_\infty\le4\beta^2$ and weighted mean zero. With
$J(\theta)=\int_0^\theta\sin^2u\,h(u)\,du$, the nearer-endpoint estimate gives
\[
\left|\frac{\cot\theta}{\sin^2\theta}J(\theta)\right|
\le\frac43\beta^2.
\]
Substitution into the integrated radial equation yields
\[
\|s_\beta''\|_\infty\le\frac43\beta+\frac{80}{3}\beta^2,
\qquad
\left\|\frac14\cot\theta\,q_\beta\right\|_\infty
\le\frac13\beta+\frac43\beta^2.
\]
The radial bound dominates the tangential one. The linear response $q_\beta/\beta\to-\frac43\sin\theta$ shows the old unit-gradient constant is impossible. These ODE steps are sound under the stated smooth regular-branch hypothesis; they do not independently establish the face-map pullback or product Bochner comparison.

## 2. Corrected rational constants

At $x=b_0/a_0=1/50000$, the corrected blocks
\[
h_d=\frac{32}{3}b_0+\frac{1280}{3}\frac{b_0^2}{a_0},
\qquad
h_o=\frac{56}{3}b_0+\frac{1280}{3}\frac{b_0^2}{a_0}
\]
give the exact normalized margins
\[
\frac{\kappa}{a_0}\ge0.478655744,
\qquad
\frac{\lambda_{\log25}}{a_0}\ge0.048379136.
\]
The corrected residual ceilings are $\|R_e\|_\infty\le4160b_0^2/a_0$ and
$\sum_h\|D_hR_e\|_\infty\le537850b_0^2/\sqrt{a_0}$.
Using the six-term centered third-order identity and the stated conditional resolvent estimates gives the rational $\pi<22/7$ upper bound
\[
\frac{288422062500000000000000000000}{190263788491}
<1.516\times10^{18}
\]
for the normalized fixed-triple amplitude coefficient. The exact-rational regression script checks these arithmetic consequences. It does not prove the analytic estimates used as inputs.

## 3. Third-order spatial tree: conditional closure

The [Dobrushin record](../theorems/PF_I16_DOBRUSHIN_THIRD_ORDER_TREE_BOUND_2026_11_13.md) uses
$\beta_*\le1/25000$, the universal $d_e\le8$ incidence count, and the radius-two link diameter to obtain
\[
\|C\|_{\log25}\le600\tanh(4\pi\beta_*)
\le\frac{12\pi}{125}<\frac{264}{875}<1.
\]
The finite-volume Dobrushin resolvent therefore obeys
$\mathsf D_{ez}\le(875/611)25^{-d(e,z)}$. Combined with the Föllmer covariance inequality and the conditional derivative-flow kernel, this gives
\[
|T_{ijk}|\le\frac{e^{-\eta\ell_{\rm MST}(S_i,S_j,S_k)}}{\lambda^2}
\left(6591B_jM_iM_k+58976M_iM_jM_k\right),
\quad
\eta=\frac18\log\frac{25}{23}>0.
\]
The six-permutation sum inherits a finite support-tree bound. This closes the third-order spatial-decay subgoal **conditionally** for the finite dressed reference measure. It is not a result for the true interacting Wilson vacuum, and the derivative-flow input remains conditional on face-map metric/pullback and finite-product Kato–Bochner estimates.

## 4. Fourth-order spatial tree: conditional fixed-order closure

The [fourth-order cut-interpolation record](../theorems/PF_I16_FOURTH_ORDER_CUT_INTERPOLATION_TREE_BOUND_2026_11_13.md) differentiates the ground energy along a cut that decouples the four support labels. It retains the complete coefficient, so disconnected pair-partition cancellations are not discarded by taking absolute values term by term. The resulting estimate is
\[
|E_{1234}|\le\mathcal C_{1234}
\exp\left[-\frac1{24}\log\frac{25}{23}\,
\ell_{\rm MST}(S_1,S_2,S_3,S_4)\right].
\]
The prefactor is finite and volume-independent for four fixed labels under the corrected derivative-flow, uniform interpolation, and face-map metric/pullback hypotheses. No uniform growth estimate for $\mathcal C_n$ is supplied.

## 5. Separate one-link cumulant route and arithmetic correction

The joint space-time record establishes a one-link continuous-time cumulant bound and an exact link-factorization identity for the Boolean-lattice quasi-factorization variables. It also gives a fourth-order maximum-tree estimate for four elementary-tensor insertions. That finite-order statement does not control the actual PF-I16 insertion projective norms or the all-orders coefficient growth.

A small arithmetic inconsistency in the displayed crude bound for $D_{8,4}$ has been corrected in the companion source record. The coefficient
\[
a_{32}=[z^{32}]\exp\left(\frac z{1-z}\right)
\]
is exactly the rational
\[
\frac{8128355160734725467847349684342205601}
{7973661725263440308097515520000000}
<1020.
\]
Together with the elementary bound $e<2.719$, this gives
$(2e)^{32}32!a_{32}<9.2\times10^{61}$. The previously printed intermediate upper bound $a_{32}\le e^{2\sqrt{32}}$ was valid but far too coarse to imply the stated $9.2\times10^{61}$ numerical result. The new exact-rational verifier reproduces the tighter coefficient bound.

The absolute all-orders Leonov–Shiryaev envelope is superfactorial. The exact identity
\[
P_\Delta(\mathbf z)=\prod_{e:\Delta\subseteq I_e}P^e_\Delta(\mathbf z)
\]
is a valid cancellation-preserving reduction, but the analytic one-link quasi-factorization majorant and connected-subset resummation with $K_8^r$ growth remain open. The alternative projective-norm majorant has a one-face linear contribution $0.090112$ at $b_0/a_0=1/50000$; under the proposed condition $2C_{\rm st}\kappa_\pi\le1/8$, this is insufficient for any $C_{\rm st}\ge1$, before pair terms are added. This is failure of that sufficient upper-majorant route, not evidence of physical divergence.

## 6. Current proof boundary

**Conditionally established at fixed finite-model scope:** corrected isolated-rotor derivative/Hessian bounds; corrected finite-product curvature and derivative-flow arithmetic; third-order support-tree bound for the full six-permutation coefficient; fourth-order cut-interpolation support-tree bound; order-four elementary-tensor maximum-tree inequality.

**Exact combinatorial/algebraic reductions:** one-link temporal cumulant estimate; order-four LS support-tree reduction; link-factorization of Boolean quasi-factorization variables.

**Still open:** the analytic one-link quasi-factorization majorant; connected-subset $K_8^r$ resummation; uniform growth of the cut-response constants $\mathcal C_n$; actual quantum connected-resolvent/KP convergence at the intended coupling; stability in the interacting Wilson vacuum; source-derived physical kinetic/time normalization; a genuine refining physical three-dimensional regulator; continuum reconstruction; and a positive physical Yang–Mills mass gap.

No canonical P0–P5 or PF-G gate is closed by this review.


## 7. Face-map pullback and finite-product Kato–Bochner closure

The companion [closure audit](PF_I16_FACE_PULLBACK_KATO_BOCHNER_CLOSURE_2026_11_13.md) derives the corrected radial bounds, exact metric scaling in the four-link face map, diagonal/off-diagonal Hessian blocks, corrected reversible drift, and componentwise Kato–Bochner comparison. The face-map and finite-product Kato caveats are discharged for finite accepted graphs satisfying the source-uniform incidence and allocation hypotheses. At (b_0/a_0\le1/50000), the unweighted and (log25)-weighted margins are (0.478655744a_0) and (0.048379136a_0). This upgrades the third-order Dobrushin and fourth-order cut-interpolation estimates to finite dressed-reference theorems uniform in graph volume under those assumptions. All-orders quantum convergence, physical interacting-vacuum stability, source-derived physical time, the refining regulator, continuum reconstruction and the physical mass gap remain open.


## 8. One-link quasi-factorization target corrected to factorial growth

A pure (K^k\) bound for the square-free one-link quasi-factorization coefficient cannot hold uniformly in (k). The coincident-time Rademacher example has (|\kappa_{2n}|\sim2(2/\pi)^{2n}(2n-1)!\). The correct one-link input is factorial, as in (12.8)/(16.5). The new [factorial-obstruction audit](PF_I16_ONE_LINK_QUASIFACTORIZATION_FACTORIAL_OBSTRUCTION_2026_11_13.md) narrows the remaining problem to a factorial-compatible full analytic majorant and a proof that temporal integration plus (1/r!\) cancels the factorial before spatial connected-subset summation. This is not a divergence result for PF-I16 and does not alter the finite third-/fourth-order results.


## 9. Pointwise factorial versus integrated temporal tree

The one-link Rademacher example requires factorial pointwise cumulant growth. The crude full-span envelope cannot have its factorial removed by the (1/r!\) Feynman–Kac normalization alone: 
\(\int_{[0,T]^r}e^{-\Delta_0(\max t_i-\min t_i)}d\mathbf t\le r!T\Delta_0^{-(r-1)}\). The all-orders temporal projection-tree theorem already provides the sharper normalized bound (2^r r^{r-2}/r!\) times the fixed-tree integral, which is exponential. The remaining problem is to combine that temporal tree with spatial support connectivity in a single bounded-fiber tree. This is the current decisive combinatorial/analytic gate; no all-orders quantum convergence is claimed.
