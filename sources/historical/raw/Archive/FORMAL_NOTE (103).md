# R3 — Compact-SU(2) weak-coupling 24-mode tail and an exact obstruction to deterministic adaptive coercivity

**27 October 2026.** Research continuation of the three branches of *Compare Continuum Mass Gaps*. The model is the exact five-dimensional cut-and-project Penrose rhombus **spatial disk** crossed with a **three-step periodic Euclidean-time circle**, with normalized product Haar SU(2) Wilson links and *homogeneous positive* coupling `lambda`. The fixed insertion contains 14 temporal faces. This is not a three-dimensional icosahedral quasiperiodic tiling. The general ambient-uniform R3 theorem remains **open**.

## Main results and quantifiers

1. **A genuine nonlinear SU(2) counterexample** proves that the existing 59-pivot adaptive contraction cannot satisfy a positive deterministic action-decrease-versus-`s_H` inequality on *all* configurations, even close to a fully flat connection. This is not a counterexample to probabilistic coercivity or to SU(2) concentration itself.
2. **A compact, non-Gaussian SU(2) weak-coupling result:** For each *fixed* finite Penrose disk `Lambda` containing the 14-face cavity, the actual Wilson law satisfies

   \[
   \boxed{\limsup_{\lambda\to\infty}\,\mathbb E_{\mu_{R,\lambda}}
       e^{\theta\lambda s_H}\ \le\ (1-\theta)^{-36},\qquad 0\le\theta<1.}
   \]

   Consequently for every fixed `t>=0`,
   \[
   \boxed{\limsup_{\lambda\to\infty}
       \Pr_{\mu_{R,\lambda}}\{\lambda s_H\ge t\}
       \le \min\{1,2^{36}e^{-t/2}\},}
   \]
   and `limsup_{lambda→infinity} lambda E s_H<=36`. These constants do not depend on the disk size, **but the limit is taken at fixed disk size first.** In particular, there is currently **no volume-independent finite threshold** `lambda_0` above which these inequalities are established. This does not complete the uniform-in-volume R3 theorem.
3. For the 62 retained plaquettes `A=A(H)` touching the original 36-link region, the actual compact model also satisfies
   \[
   \boxed{\limsup_{\lambda\to\infty}\lambda\sum_{p\in A}\mathbb E_{\mu_{R,\lambda}}d(W_p)\le 88.5}\]
   for each fixed Penrose disk, again with **no uniform-in-volume error estimate**.

## I. Rigorous deterministic no-go for the 59-pivot adaptive geodesic map

Let `H` be the 36 inserted-face links, `A` the 62 retained faces touching `H`. The optimized relative presentation selects 24 exterior links `X` and then solves 59 of the 60 links `H∪X` as SU(2) words in the unselected links; all 62 face relators in `A` become identities when the 59 solved links are set to these words. These are exact nonabelian Tietze eliminations, not linearized statements. Let `P` be the 59 solved links and `C` the 33 retained crossing faces outside `A` that meet `P`. The entire dependence of the *full retained action* on `P` is therefore in the 95 faces `A∪C`.

Choose one nonpivot spatial link `e=438` at time slice 2, with original Z^5 endpoints `[0,0,-2,-1,-1]` and `[0,0,-1,-1,-1]`. Fix all other nonpivot links to the identity and set `U_e=exp(epsilon i sigma_1)`. For each `epsilon`, choose a **global minimizer** `U_P^*(epsilon)` of the *complete retained Wilson action* over the 59 pivot links. Compactness ensures existence. At `epsilon=0`, the only solution of the 62 flat `A` relations at fixed nonpivots is `U_P=I`, due to the exact 59-pivot triangular presentation. Thus every global pivot minimizer approaches the identity as `epsilon→0`. Since the 95-face Hessian restricted to the 59 pivots has full real rank `3×59`, the implicit function theorem and compactness provide a unique smooth near-identity global minimizer for sufficiently small `epsilon`.

In the Lie-algebra tangent model, write the affected-face incidence matrix `D` with rows `A∪C`, and columns partitioned into pivots `P` and fixed links `Z`. Holding a single exterior component `z=e_438`, the exact minimized tangent pivot vector is

\[
 x_P=-(D_P^{\mathsf T}D_P)^{-1}D_P^{\mathsf T}D_Ze_{438}.
\]

`D_P` has rank 59, `D_{A,H}` has rank 35, and all matrix coefficients are integers. For the 62-face local residual `r=D_A(x_P+e_438)`, compute an **exact rational** left-null witness `w^T D_{A,H}=0` with

\[
 w^{\mathsf T}r=\frac{78127633963291163}{351032644442371316}\ne0,\qquad \|w\|_2^2=8.
\]

Therefore

\[
 \frac12\|\operatorname{proj}_{(\operatorname{im}D_{A,H})^\perp}r\|^2
 \ \ge\ \frac{(w^{\mathsf T}r)^2}{2\|w\|^2}
 =\frac{6103927188702006837944222713892569}{1971582679427268505058742227513149696}
 >0.
\]

The 35-pivot exact relative group elimination of `H` reduces the remaining 27 `A` relators to **words exclusively in frozen exterior links** (not in the one remaining local free link). The rational witness shows their first-order perturbation is nonzero along this exterior curve after the full-action-minimizing pivot response. Hence for sufficiently small `epsilon≠0`, no values of the original `H` links can make all 62 faces flat. In particular, `s_H(U_{H^c}^*(epsilon))>0`.

But the configuration has, by construction, *globally minimal full retained action among all choices of the 59 pivot variables*. Consequently **every** action-nonincreasing surgery which only changes these 59 links has zero action decrease there:

\[
 \boxed{\Delta_P(U^*(\epsilon))=0,\qquad s_H(U^*(\epsilon)_{H^c})>0.}
\]

Thus for any fixed `alpha>0` and finite `C`, the assertion

\[
 \Delta_P(U)\ge\alpha s_H(U_{H^c})-C|Q|/\lambda\quad\text{for all }U,\lambda
\]

is **false**, since `U^*(epsilon)` is fixed while the correction vanishes as `lambda→infinity`. This excludes *deterministic* coercivity for any adaptive 59-pivot-only full-action-nonincreasing surgery; it does **not** exclude the desired **Gibbs probability** tail, since the constructed configuration is not necessarily typical at high coupling.

### Nonlinear numerical realization (independent check, not the proof)

The same exact SU(2) Wilson face words were minimized over all 59 pivot links, and then independently over the original 36 `H` links. The geodesic adaptive map tried `tau={0,0.1,0.25,0.5}`. It chose the identity on all three tested points:

| `epsilon` | `s_H` from nonlinear optimization | `s_H / epsilon²` | adaptive `tau` | full action decrease |
|---:|---:|---:|---:|---:|
| 0.04 | 0.000498025 | 0.3112656 | 0 | 0 |
| 0.08 | 0.001992078 | 0.3112622 | 0 | 0 |
| 0.16 | 0.007967927 | 0.3112472 | 0 | 0 |

The smooth dependence is consistent with the tangent coefficient `0.311267...`. The rigorous no-go relies on the **exact rational witness and Tietze structure**, not on the numerical optimizer.

## II. A true compact-SU(2) asymptotic 24-mode concentration theorem

### 1. Clean compact flat locus

Fix any *finite* spatial Penrose disk `D` that contains the inserted neighborhood. The full three-periodic spacetime cell complex is `D×S¹`, with `pi_1=Z`. Choose a spanning-tree gauge. A flat connection is determined by the single unrestricted SU(2) Polyakov holonomy `b`, so its gauge-fixed flat locus is a **smooth compact copy of SU(2)**.

One direct normal-coordinate construction is: (i) set the spatial tree links and two temporal vertical slices to the identity by gauge transformations; (ii) the spatial disk's face relations solve its remaining `F` spatial chords at time 0; (iii) temporal face identities in the first two intervals solve the `2E` remaining spatial time links; (iv) the last-interval temporal identities along a spatial tree solve the remaining `V−1` vertical Polyakov links. The count `F+2E+(V−1)=3E` follows from `V−E+F=1`. Every pivot is multiplication/inversion of a unique SU(2) variable, and its normal Jacobian block is invertible at any flat holonomy.

The fourteen deleted faces are *exactly* Bianchi-fillable by neighboring retained prism relations (as audited in the earlier 14-face certificate). Therefore `R=all\Q` has **the same set of globally flat connections** as the full complex. This set is clean: the retained face-map Jacobian `J_R` has kernel exactly the tangent bundle of the above flat SU(2) manifold. Hence the retained Wilson action is Morse–Bott at its zero set, with positive normal Hessian `J_R^*J_R`. The fact that no competing nonflat zero-action configurations exist follows from `d(W)>=0` and `d(W)=0` iff `W=I`.

### 2. Uniform rank of the *local* normal quotient

The exact relative group certificates have **35 unique H-link pivots**, leaving one unsolved H link and only exterior relators, and **59 unique (H∪X)-link pivots**, leaving one unsolved local link and three trivial residual relators. Because group multiplications/inversions induce invertible `3×3` adjoint Jacobian blocks at *every* flat holonomy,

\[
 \operatorname{rank}_{\mathbb R}J_{A,H}=3\cdot35=105,\quad
 \operatorname{rank}_{\mathbb R}J_A=3\cdot59=177.
\]

Thus the local curvature quotient has **72 real directions**, equivalently **24 three-component SU(2) tangent modes**. At identity and nontrivial Polyakov holonomies, numerical adjoint-Jacobian audits on four Penrose volumes confirm `[105,177]`. The ranks themselves follow from the group-word certificates, not from floating-point SVD.

### 3. Morse–Bott normal fluctuations and Gaussian domination of the limit

Write a gauge-fixed nearby configuration as `U=U_0 exp(x/sqrt(lambda))`, with `U_0` on the compact SU(2) flat locus and `x` orthogonal to its tangent. For each fixed ambient volume, the Wilson action has expansion

\[
 \lambda S_R(U)=\tfrac12\|J_R(U_0)x\|^2+O(\lambda^{-1/2}\|x\|^3).
\]

The normalized compact Haar Wilson measure converges in these normal coordinates, via standard finite-dimensional Morse–Bott/Laplace integration, to a mixture over flat `U_0` of Gaussian normal laws with quadratic form `J_R^*J_R`. The induced face-curvature Gaussian `Z=J_Rx` has covariance

\[
 \Pi_R=J_R(J_R^*J_R)^+J_R^*,\qquad 0\preceq\Pi_R\preceq I,
\]

which is the **orthogonal projector** onto `im J_R`. This remains true at a noncentral Polyakov flat holonomy, using the twisted SU(2) adjoint Jacobian rather than the abelian incidence matrix.

For the original `H`, choosing an `O(lambda^-1/2)` variation of its links and minimizing the leading quadratic face action gives an *upper bound* on the nonlinear conditional minimum,

\[
 \lambda s_H\ \lesssim\ \tfrac12\|P_H^\perp Z_A\|^2,\quad
 P_H^\perp=I-\operatorname{proj}_{\operatorname{im}J_{A,H}},
\]

where `Z_A` restricts the Gaussian face curvature to the 62 local retained faces. The covariance of `P_H^\perp Z_A` has eigenvalues between 0 and 1, and rank at most `177−105=72`. Therefore for `0<=theta<1`,

\[
 \mathbb E_{U_0}\exp\left(\frac\theta2\|P_H^\perp Z_A\|^2\right)
 =\det(I-\theta\mathcal C_{U_0})^{-1/2}
 \le(1-\theta)^{-36}.
\]

To justify moving the upper bound through the compact SU(2) Laplace limit, note the **global** inequality `s_H<=S_A<=S_R`, so the exponential tilt is dominated by the same Wilson action with at least `(1−theta)` of every retained face coupling. That tilted action has the **same compact clean zero manifold** and a positive normal Hessian, allowing dominated finite-dimensional Morse–Bott integration. Since the determinant bound holds pointwise on the flat manifold, it survives its nonuniform flat-holonomy weighting.

The result is the stated **actual compact-SU(2)** asymptotic moment bound and its Chernoff tail. In particular, for each finite `Lambda` there exists `lambda_0(Lambda)` such that, for all `lambda>=lambda_0(Lambda)` and all `t>=0`,

\[
 \boxed{\Pr_{\mu_{R,\lambda}}\{\lambda s_H\ge t\}
 \le \min\{1,2^{37}e^{-t/2}\}.}
\]

The prefactor `2^37` is independent of the disk **but the threshold `lambda_0(Lambda)` is not proven to be so**. The earlier fixed-volume Gaussian tangent result `2^36 e^{-t/2}` is thus recovered as an asymptotic limit of the *actual nonabelian compact Haar measure*, not adopted as a finite-`lambda` assumption.

Exactly the same limiting projector bound gives for the 62 local retained faces

\[
 \limsup_{\lambda\to\infty}\lambda\mathbb E_{\mu_{R,\lambda}}S_A\le\tfrac12\operatorname{rank}_{\mathbb R}J_A=177/2=88.5.
\]

This is a **sequential weak-coupling local-energy theorem**, not the volume-uniform high-coupling inequality needed by R3.

## III. A stronger fixed-volume weak-coupling **insertion-ratio** theorem

The same method gives a nonzero **support-dependent but ambient-size-independent lower bound on the limiting SU(2) insertion ratio**. In the tested 14-face insertion, the actual six-face prism Bianchi words can express every inserted face as a product of at most **17** conjugated retained face holonomies. The exact nonabelian multiplicity audit gives the global, configuration-wise energy estimate

\[
  S_Q(U):=\sum_{q\in Q}d(W_q(U))\ \le\ 44\sum_{p\in A_{\mathrm{fill}}}d(W_p(U))\ \le 44S_R(U),
  \qquad |A_{\mathrm{fill}}|=54.
\]

This was independently reverified in `verify_bianchi.py` by counting group-face factors **without** abelian cancellation, using conjugation invariance of `d` and `sqrt(d(AB))<=sqrt(d(A))+sqrt(d(B))`. At every flat connection, the second-variation matrices therefore satisfy on the normal bundle

\[
 0\preceq J_Q^*J_Q\preceq44J_R^*J_R.
\]

Let `G=J_R^*J_R` on that normal bundle; the full-insertion normal Hessian is `G+J_Q^*J_Q`. The positive-semidefinite matrix

\[
 D=G^{-1/2}J_Q^*J_QG^{-1/2}
\]

has every eigenvalue at most 44 and real rank at most `3|Q|=42`. Consequently the *pointwise* ratio of Laplace normal-volume coefficients is

\[
 \frac{\det(G+J_Q^*J_Q)^{-1/2}}{\det(G)^{-1/2}}
 =\det(I+D)^{-1/2}\ \ge\ 45^{-21}.
\]

The full and retained Wilson actions have exactly the **same clean compact SU(2) flat locus**, so integrating this pointwise bound with their common positive Haar density along that locus proves

\[
 \boxed{\forall\text{ fixed finite Penrose disks }\Lambda:\quad
 \lim_{\lambda\to\infty}\frac{Z_{R\cup Q}^{(\Lambda)}(\lambda)}{Z_R^{(\Lambda)}(\lambda)}
 \ \ge\ 45^{-21}\approx1.91663\times10^{-35}.}
\]

Equivalently,

\[
 \boxed{\sup_{\Lambda}\limsup_{\lambda\to\infty}\mathcal F_Q^{(\Lambda)}(\lambda)
 \le21\log45\approx79.939913.}
\]

This is an **actual nonlinear compact-Haar fixed-volume weak-coupling theorem**, whose limiting constant is independent of the ambient Penrose disk. The limiting free-energy estimate is even `O(|Q|)` (rather than `O(|Q| log lambda)`) for this *Bianchi-fillable* support. However, the order of operations is `limsup_lambda` **before** `sup_Lambda`; nothing above proves a volume-independent finite coupling threshold. It is therefore **not the original ambient-uniform R3 statement**, and it says nothing about supports that introduce extra independent flat constraints.

## IV. The remaining genuine uniformity problem

The two findings resolve the research choice as follows:

- **Deterministic adaptive coercivity:** definitively false for the existing 59-pivot repair on this actual Penrose patch, including arbitrarily near the flat locus. Moving more than the 59 pivots or proving a probability estimate for exterior links is necessary.
- **Compact SU(2) joint 24-mode tail:** proved in the sequential limit `fixed Lambda, then lambda→∞`, with a Gaussian projector upper bound independent of the final volume in that order of limits.
- **Desired R3 bound:** still open because the argument supplies neither `sup_Lambda sup_lambda>=lambda0` concentration with one `lambda0` nor quantitative volume-independent control of the nonlinear Laplace remainder. In a growing disk, global gauge-fixed normal coordinates can become poorly conditioned, even if gauge-invariant local curvatures remain well behaved. The finite-volume proof does not justify interchanging `sup_Lambda` and `limsup_lambda`.

A valid next approach is a **uniformly local nonlinear curvature-coordinate inequality** (or a Penrose-specific spectral/transport estimate controlling the Laplace remainders without invoking a global small positive eigenvalue). A larger multiscale repair that also moves crossing plaquettes could be viable, but it must confront the deterministic no-go on the smaller pivot block.

## Reproduction and provenance

`no_go_gaussian.py` forms the exact integer face matrices and identifies link 438; `certify_rational.py` verifies the rational left-null witness and positive coefficient; `nonlinear_pivot_counterexample.py` evaluates noncommuting quaternion Wilson words and optimizes both P and H; `flat_rank_SU2.py` checks adjoint Jacobian ranks at four nontrivial Polyakov angles and four Penrose radii. The original relative Tietze scripts and the exact direct-Z5 spatial geometry generator are bundled. No Monte Carlo inference is used in the rigorous statements. Numeric optimization and adjoint SVD are cross-checks, not substitutes for the algebraic proof.
