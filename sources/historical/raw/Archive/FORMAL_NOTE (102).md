# R3 — Joint crossing-energy law, adaptive nonlinear geodesic surgery, and a two-scale collar transport

**27 October 2026; research continuation.** Genuine direct-\(\mathbb Z^5\) Penrose rhombus spatial disk crossed with a three-step periodic temporal circle. Fixed 14-face two-interval temporal insertion \(Q\), 36 original affected links \(H\), 62 retained faces \(A\) touching \(H\), 24 independent exterior linearized modes, optimized 24 selected exterior links, 59 exact Tietze pivot links \(P\subset H\cup X\), and 33 crossing retained faces \(C\) touching \(P\) but not \(H\). In four nested patches, these counts are the same. **The absolute compact-SU(2) Gibbs tail and R3 theorem remain open.**

## 1. The exact linearized-Gaussian joint distribution: a benchmark, not a Haar theorem

Let \(D_R\) denote the real signed retained face-to-link matrix. In the exactly quadratic \(\mathfrak{su}(2)\) model, \(S_R(a)=\frac12\sum_{p\in R}\|(D_Ra)_p\|^2\) with density proportional to \(e^{-\lambda S_R}\) on link variables modulo the nullspace of \(D_R\). Equivalently, for each of the three Lie algebra components,

\[z=\sqrt\lambda D_R a\sim N(0,\Pi_R),\quad \Pi_R=D_R(D_R^TD_R)^+D_R^T,\]

where \(\Pi_R\) is the **orthogonal projector** onto \(\operatorname{im}D_R\), so \(0\preceq\Pi_R\preceq I\) for any ambient volume. This is an identity in the *quadratic tangent model only*. The actual compact noncommuting Wilson law is not Gaussian.

Write \(D_{A,H}\) for the face-by-link submatrix on the original 62 retained faces and 36 local links. \(\operatorname{rank}D_{A,H}=35\) and \(\operatorname{rank}D_A=59\). For the linearized conditional minimum, every Lie component obeys

\[\lambda s_H^{\rm lin}=\tfrac12\sum_{c=1}^3\|P_H^\perp z_{A,c}\|^2,\quad P_H^\perp=I-\mathrm{proj}_{\operatorname{im}D_{A,H}}.\]

The covariance \(P_H^\perp\Pi_{R,AA}P_H^\perp\) is dominated by identity and has **effective rank 24** (the other three directions in \(\ker D_{A,H}^T\) are Bianchi-null). Therefore

\[\boxed{\mathbb E e^{\theta\lambda s_H^{\rm lin}}\le(1-\theta)^{-36},\quad 0\le\theta<1,}\]
\[\boxed{\mathbb P\{\lambda s_H^{\rm lin}\ge t\}\le\min\{1,2^{36}e^{-t/2}\}.}\]

This is a **volume-uniform joint 24-mode distributional theorem in the exactly linearized Gaussian model**. It explicitly includes all ambient correlations via the projector, without requiring independent modes or a fixed infrared regulator. It is not the requested inequality for \(\mu_R^{SU(2)}\).

For the 59-pivot **complete flat repair**, the unique linearized pivot adjustment is \(\delta a_P=-L_A^+z_A\), with \(L_A=D_{A,P}\) rank 59, and crossing change \(\delta z_C=-L z_A\), where \(L=D_{C,P}L_A^+\). The dimensionless crossing energy change is

\[\lambda\Gamma_{\rm lin}=\tfrac12\sum_{c=1}^3\begin{bmatrix}z_{A,c}\\z_{C,c}\end{bmatrix}^{\!T}\begin{bmatrix}L^TL&-L^T\\-L&0\end{bmatrix}\begin{bmatrix}z_{A,c}\\z_{C,c}\end{bmatrix}.\]

If \(\alpha_j\) are eigenvalues of the covariance-sandwiched symmetric quadratic form, its **entire joint moment-generating function** is

\[\mathbb E e^{\theta\lambda\Gamma_{\rm lin}}=\prod_j(1-\theta\alpha_j)^{-3/2},\qquad 0\le\theta<\alpha_{\max}^{-1}.\]

A Chernoff bound follows immediately. The spectral norm of \(L\) is purely local (constant when the same Penrose support is embedded in a larger cavity), so a coarse uniform exponential-tail constant can be derived independent of ambient volume. The computed Gaussian spectra below are numerical audits using a \(10^{-7}\) normal-equation regularization to evaluate the exact projector; the theorem itself uses the Moore–Penrose projector with no regularizer.

| Penrose radius | \(\alpha_{\max}\) | \(\mathbb E[\lambda\Gamma_{\rm lin}]\) | Std \(\lambda\Gamma_{\rm lin}\) | \(\mathbb E[\lambda s_H^{\rm lin}]\) |
|---|---:|---:|---:|---:|
| 5 | 43.150 | 135.53 | 64.30 | 20.83 |
| 6.5 | 42.789 | 133.98 | 63.71 | 20.77 |

**Interpretation:** the exact-flat 59-pivot repair has a **positive mean crossing-energy cost even in the tangent Gaussian model**. Its sign problem is not simply noncommutativity; it is the choice of forcing all 62 local face holonomies to identity without jointly minimizing the crossing energy.

## 2. Actual SU(2) retained Wilson measure: exploratory full joint-crossing pilot

`wilson_geodesic_probe.py` implements independent-link Haar-symmetric SU(2) Metropolis updates using **every retained face** and the 59-pivot nonabelian Tietze solution. At radius 5, two hot/cold chains at \(\lambda=8,16,32\), 100 burn-in sweeps, and ten measurements per chain separated by ten sweeps provide a deliberately modest test. No equilibration, autocorrelation, high-coupling asymptotic, or infinite-volume law is certified.

On each sampled \(U\), compute \(U^\flat\) by exact reverse free-word substitution; this always has \(W_p(U^\flat)=I\) for all 62 retained faces in A. Let \(\Gamma=S_C(U^\flat)-S_C(U)\). The 60 sampled measurements (20 per coupling) generally show \(\lambda\Gamma\) of order \(10^2\), and the **complete** flat repair often increases the full Wilson action. This is in line with the Gaussian transport benchmark. Raw data are in `wilson_crossing_geodesic_samples.json` and the quantitative summary in `adaptive_surgery_certificate.json`.

These are numerical pilot samples under the actual nonlinear SU(2) action, NOT a proof of a tail under the exact Gibbs law.

## 3. New exact Haar surgery: a 59-link **partial geodesic contraction**

The 59 exact Tietze substitutions define a target \(V^\flat_P(z)\in SU(2)^{59}\) **depending only on the unsolved link coordinates** \(z=U_{P^c}\), not on the original 59 pivot values \(U_P\). This structural independence is essential. It is verified directly by changing all initial pivot values with \(z\) held fixed and obtaining the same target. The Tietze relations imply that this target exactly flattens the 62 faces A for every frozen \(z\).

For \(0\le\tau<1\), let

\[T_\tau(U)_p=\operatorname{Geo}_{V_p^\flat}(U_p,1-\tau),\quad p\in P,\qquad T_\tau(U)_e=U_e\ (e\notin P).\]

Here \(\operatorname{Geo}_{V}(U,r)\) is the point at fraction \(r\) along the minimizing SU(2) geodesic from \(V\) to \(U\). It is unique outside the antipodal Haar-null set. For a point at geodesic distance \(\vartheta\in[0,\pi)\) from its target, the exact normalized-Haar Jacobian per link is

\[\boxed{j_\tau(\vartheta)=(1-\tau)\left(\frac{\sin((1-\tau)\vartheta)}{\sin\vartheta}\right)^2\ge(1-\tau)^3.}\]

The inequality is elementary concavity of \(\sin\) on \([0,\pi]\). Because the target is independent of the pivot values, the **full map is a conditional product diffeomorphism onto its image**, and the Jacobian is the product of these factors. It is **not volume preserving**, unlike a fixed group translation, but has an explicit volume-independent lower Jacobian bound.

Define the **adaptive surgery** by evaluating \(T_\tau(U)\) at \(\tau\in\{0,0.1,0.25,0.5\}\) and choosing the first with the least **complete retained Wilson action** (only 62 interior and 33 crossing faces can change). This is an explicit measurable piecewise map with

- **at most 59 modified links**, all confined to the original fixed Penrose 60-link collar;
- **complete retained Wilson action never increasing**, because \(\tau=0\) is an option;
- **at most four inverse images**, since each nonzero-\(\tau\) branch is injective (conditionally on frozen links);
- branchwise Haar Jacobian **at least \(2^{-177}\)**, independent of \(\lambda\) and ambient volume; no finite-net cardinality factor at all.

For its action decrease \(\Delta(U)=S_R(U)-S_R(TU)\ge0\), the exact change-of-variables/fluctuation identity gives

\[\boxed{\mathbb E_{\mu_R}\!\left[J_T(U)e^{\lambda\Delta(U)}\right]\le4,\quad\mathbb P_{\mu_R}\{\lambda\Delta\ge t\}\le\min\{1,4\cdot2^{177}e^{-t}\}.}\]

Here the first inequality follows by summing the at most four branch images under normalized Gibbs integration; it is true for **the actual compact noncommuting SU(2) measure**. This bounds the action-decrease distribution, not directly the crossing cost or the minimum frustration \(s_H\).

More generally, on the *explicitly defined coercive event* \(G_{\alpha,b}=\{\lambda\Delta(U)\ge\alpha\lambda s_H(U_{H^c})-b|Q|\}\), the same surgery gives

\[\boxed{\mathbb P_{\mu_R}\{\lambda s_H\ge t,\ G_{\alpha,b}\}\le 4\cdot2^{177}\,e^{b|Q|-\alpha t}.}\]

**No bound on the complementary event is established.** An absolute R3 tail cannot be obtained by discarding it.

### Actual nonlinear pilot comparison

For the 60 short retained-Wilson MCMC observations, the adaptive map selected the following mean complete-action reductions (multiplied by \(\lambda\)):

| Coupling \(\lambda\) | Observations | Mean \(\lambda\Delta\) | Fraction strict decrease |
|---:|---:|---:|---:|
| 8 | 20 | 18.70 | 0.85 |
| 16 | 20 | 24.86 | 1.00 |
| 32 | 20 | 20.18 | 0.95 |

The **complete flat repair** on the same samples often *increased* action. The partial geodesic repair avoids this on every configuration by construction. These empirical numbers establish neither ergodic convergence nor coercivity on all bad-frustration events.

## 4. Two-scale collar extension with explicit conditional Jacobian and multiplicity

Let \(B\subset K\) be any local link blocks, \(k=|K|\), and \(\nu\) the maximal retained face incidence. Fix the exterior links \(b=U_{K^c}\) and a deterministic SU(2) angular net of radius \(\delta/\sqrt\lambda\) for some fixed \(0<\delta<1\). Among the finite product-net candidates, choose the first minimizing the entire local retained action \(S_K(v;b)\). **This net-selected target depends only on \(b\)**, not on the current \(K\) links; it is completely explicit but exponentially expensive to enumerate as \(|K|\) grows.

Apply conditional geodesic contraction toward that target by

\[1-\tau=\frac{1}{\pi\sqrt\lambda}.\]

Every resulting link is within angular distance \((1+\delta)/\sqrt\lambda\) of an exact minimizer. The Wilson second-variation bound yields

\[\lambda\left[S_K(TU;b)-s_K(b)\right]\le 2\nu k(1+\delta)^2.\]

Choose the lower full-action candidate between this contraction and the identity. The resulting **second-stage** surgery is full-action-nonincreasing, has at most two inverse branches, and has Haar Jacobian at least \((\pi\sqrt\lambda)^{-3k}\) on each branch. Consequently

\[\boxed{\mathbb P_{\mu_R}\{\lambda(s_B-s_K)\ge t\}\le\min\{1,2(\pi\sqrt\lambda)^{3k}e^{2\nu k(1+\delta)^2-t}\}.}\]

This is an explicitly constructed nonabelian, bounded-multiplicity **collar-increment** surgery, with no global partition-function ratio and no ambient-volume factor. Composing the first 59-pivot surgery with the second 125-link collar contraction gives a two-scale map changing at most 125 physical links, with at most eight inverse branches and a product lower Jacobian bound.

**However**, the second-stage estimate still concerns only \(s_B-s_K\). In the 14-face Penrose cavity, the rank audit shows the outer conditional minimum \(s_K(b)\) need not vanish for arbitrary exterior assignments. Its actual Gibbs distribution is not controlled by this construction. This is the same terminal obstruction as in the preceding branch.

## 5. Why the absolute 3D compact-Haar estimate remains open

The Gaussian proof uses linear curvature coordinates and orthogonal-projector covariance domination. For SU(2), exact curvature is noncommutative, compact, and subject to nonlinear Bianchi identities; the Gibbs law is *not* a projected Gaussian and no dimension-free nonabelian Brascamp–Lieb domination has been established here.

The new partial geodesic surgery is a useful **actual-Haar** construction with a far smaller multiplicity/Jacobian cost than the earlier 59-fold finite-net surgery, and it often avoids the crossing-energy increase. But a proof of the desired

\[\Pr_{\mu_R}\{\lambda s_H\ge t\}\le C^{|Q|}(1+\lambda)^{a|Q|}e^{-ct}\]

would still require **either** (a) a uniform high-probability lower bound on the adaptive full-action decrease in terms of \(s_H\), including the complement of the good event, **or** (b) a genuinely nonabelian curvature concentration principle comparable to the projected-Gaussian estimate.

Neither is derived by the present calculation. Thus the requested absolute local R3 energy bound and the continuum mass-gap theorem remain open.

## Reproduction

Run `python gaussian_joint_audit.py` for numerical Gaussian spectral checks (NumPy/SciPy), `python wilson_geodesic_probe.py --radii 5 --lambdas 8 16 32 --burn 100 --stride 10 --samples 10` for the short genuinely noncommuting retained-Wilson diagnostic (Numba), `python adaptive_surgery.py` for the explicit SU(2) map/Jacobian/multiplicity audit, and `python multiscale_collar.py` for the second-stage constants. The source geometry, face-word builder, full Q14 seed, and optimized 24-mode basis are bundled so computations do not rely on earlier directories. Numerically computed eigenvalues in `gaussian_joint_certificate.json` use a vanishing small ridge as a numerical solver convenience **only for the linearized benchmark**, and no SU(2) Gibbs theorem is inferred from that solver.
