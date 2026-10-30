# R3 — The full 24-mode Penrose exterior collar: nonabelian gluing, Haar surgery, and a crossing-rank obstruction

**Date:** 27 October 2026. **Geometric input:** genuine direct-\(\mathbb Z^5\) cut-and-project Penrose rhombus spatial disks of radii 5, 6.5, 8, and 10, each crossed with three periodic temporal intervals. **Claim status:** an exact 24-mode quotient basis; a fully nonlinear 59-relator local flat-gluing construction; a three-color action-nonincreasing compact-Haar surgery; and a *weaker-than-desired* rigorous absolute Gibbs tail. The intended \(C^{|Q|}(1+\lambda)^{a|Q|}e^{-ct}\) bound is **not proved**.

## 1. Precise interpretation of the 24 modes

Fix the same 14-temporal-face insertion \(Q\) in all four nested Penrose disks, identified by the original five-integer labels. Let \(R\) be the remaining faces. Let \(H\) be the **36** physical links in the boundaries of inserted faces, and let
\[
A=\{p\in R:\partial p\cap H\ne\varnothing\},\qquad |A|=62.
\]
Let \(E\) be the **89** links outside \(H\) appearing in these 62 face words. Let \(D_H,D_E\) denote the exact signed face-by-link incidence matrices restricted to the 62 affected retained plaquettes.

The exact ranks **over the rationals** are
\[
\operatorname{rank}D_H=35,\qquad
\operatorname{rank}[D_H\ D_E]=59,\qquad
\operatorname{rank}[D_H\ D_E]-\operatorname{rank}D_H=24.
\]
Thus the space \((\operatorname{im}D_H+\operatorname{im}D_E)/\operatorname{im}D_H\) has dimension 24. These are 24 **abelianized face-incidence** directions, equivalent to 72 tangent components for su(2), **not** 24 separate globally gauge-invariant Wilson-loop variables. A greedy exact matroid-basis algorithm produces 24 physical exterior links \(X\subset E\) whose columns form a basis of this quotient. This basis is the same under canonical five-integer relabeling across all four radii.

The canonical basis has 14 horizontal spatial links at temporal level 0, 9 at level 1, and 1 at level 2. Its interaction graph (two basis links adjacent if they appear together in one *retained* face, including outside A) has chromatic number **at most three**, with explicitly verified color groups of **12, 10, and 2**. Each color class consists of links with pairwise disjoint affected retained-face sets. All 24 links jointly affect 73 retained faces: 35 in the original 62-face set A, and **38 crossing faces outside A**. Every selected link belongs to at most four retained faces.

A second exact quotient basis chosen to reduce crossing incidence affects just **33 crossing retained faces**. The optimization searched two deterministic link orderings, so 33 is an *achieved* count, not a proven global minimum. The shorter-word initial basis is used for the simple three-color surgery; the 33-crossing basis is used for the stronger tail estimate below.

Growing the adjustable collar changes the relative quotient: the 125-link first shell has 46 exterior directions, and the 258-link second shell has 63. These numbers refer to **different affected retained-face sets**, and should not be confused with the original 24 directions.

## 2. Exact nonabelian joint flat extension (new constructive theorem)

Use oriented **group words**, not just the incidence vectors. Treat all links outside \(J=H\cup X\) as arbitrary, immutable SU(2) letters. For either basis \(X\), there exists an explicitly recorded sequence of **59 elementary Tietze eliminations**, each replacing a selected link variable by a group word in the remaining variables. The remaining three face relators freely reduce to the identity. One of the 60 links in J remains unconstrained.

Therefore for **every fixed assignment of all links outside J**, and every choice of the one free link coordinate, the reverse substitution algorithm constructs an SU(2) assignment to the remaining **59 link pivots** such that
\[
\boxed{W_p=I\quad\text{for every }p\in A,\qquad |A|=62.}
\]
This is an **exact nonabelian** flat completion of all 24 exterior-incidence directions simultaneously, not 24 independent linear repairs. It changes **at most 59 links**, all in a geometrically fixed collar near Q. The original quotient basis has maximal one-step substitution length 9 and maximal fully expanded reduced link-word length 35 (maximum frozen-symbol overlap 36). The lower-crossing basis has one-step bound 17 and expanded bound 73 (maximum symbol overlap 73). These are **fixed-support constants**, not proven uniform bounds for arbitrary large Q.

We reran the group reduction on all four nested radii, with the optimized 24 links matched by their exact Z5 labels. The 59/3/1 counts and maximum one-step substitution lengths agree. Direct quaternion group evaluation on 24 noncommuting test configurations for each basis verifies that the 62 retained face traces all become 1, to errors below \(10^{-12}\). This finite test is supplemental; the freely reduced word equalities prove the group-theoretic claim.

**Critical distinction:** the flat-gluing map itself is **not** measure preserving (it sets 59 nontrivial group relators to the identity, collapsing degrees of freedom). It can **increase the complete retained Wilson action** because it changes crossing retained faces. We found three full-action increases in the 24 original-basis tests and five in the 24 reduced-crossing-basis tests; the total energy cannot be discarded.

## 3. Three-color, genuinely Haar-preserving action-decreasing surgery

Let \(G_8=\{\pm I,\pm i\sigma_1,\pm i\sigma_2,\pm i\sigma_3\}\subset SU(2)\), represented as the eight unit quaternions. Visit the three explicitly certified exterior-basis color groups in order. For each link in a color, select the \(g\in G_8\) minimizing the **complete retained Wilson action** under \(U_e\mapsto gU_e\), breaking ties in a fixed deterministic order. The links in a single color influence disjoint retained-face sets, so their updates commute at the level of the action; no plaquette is omitted. The identity is a candidate at every update.

**Exactly proved:**
- The complete \(S_R\) never increases;
- only the 24 exterior basis links change (at most 73 affected retained faces), and all other physical links are fixed;
- each branch of the map is a product of left SU(2) translations and hence has absolute Haar Jacobian **one**;
- the full inverse multiplicity is at most \(8^{24}\), independent of ambient volume or \(\lambda\);
- the interaction groups have cardinalities 12, 10, 2, explicitly verified at radii 5, 6.5, 8, 10.

`joint_surgery.py` implements the map and checks full retained-action monotonicity on flat, random noncommuting, and central-defect configurations. For continuous mode coverage one may replace \(G_8\) by the finite \(\lambda^{-1/2}\)-net described below. **Nonincreasing action does NOT imply an action decrement proportional to s_H.** In particular there is no proof that three passes of coordinate descent jointly eliminate all exterior frustration modes.

## 4. An explicit finite-net **59-pivot** Gibbs surgery covering the exact flat extension

For each \(\lambda\ge1\), use an explicit net \(\mathcal N_\lambda\subset SU(2)\) containing the identity, covering SU(2) at geodesic radius \(\lambda^{-1/2}\), with \(|\mathcal N_\lambda|\le4097\lambda^{3/2}\). (The previous finite-net surgery package supplies the quaternion chart construction.) Let \(P\) be the 59 solved link pivots for the **lower-crossing** basis. For every configuration U choose the first tensor-product net translation \(g\in\mathcal N_\lambda^P\) that minimizes the **complete retained Wilson action** \(S_R(gU)\); write \(T_\lambda(U)=gU\). Here all other links, including the one free local link, are held fixed.

It is a well-defined, if computationally enormous, explicit piecewise map. Each branch has Haar Jacobian one and each image has at most \((4097\lambda^{3/2})^{59}\) preimages.

For the original 62 retained faces A there exists a 59-link exact flat completion. The 59 links in the lower-crossing basis meet **33** other retained faces. By \(0\le d\le2\), the completed assignment may increase those crossing energies by at most 66, so for any U,
\[
S_R(U)-S_R(U^{\mathrm{flat}})\ge S_A(U)-66\ge s_H(U_{H^c})-66.
\]
Let \(S_R^{\min,P}(U_{P^c})\) be the minimum of the *entire* retained action over those 59 pivots. It is at most \(S_R(U^{\mathrm{flat}})\). At this full-action minimum the first variation vanishes. A net point within \(\lambda^{-1/2}\) of each pivot approximates it with Wilson action cost at most \(2\nu\cdot59/\lambda\), using the exact SU(2) second-derivative bound and incidence \(\nu\le7\).

Therefore the action-decreasing net surgery satisfies **for every configuration**
\[
\boxed{\lambda[S_R(U)-S_R(T_\lambda U)]\ge
\lambda s_H(U_{H^c})-66\lambda-826.}
\]
Gibbs change of variables across the finitely many Haar-translation branches yields the **unconditional, ambient-volume-independent fixed-support tail**
\[
\boxed{
\Pr_{\mu_R}\{\lambda s_H\ge t\}
\le\min\left\{1,\exp\left[-t+66\lambda+59\left(\tfrac32\log\lambda+\log4097+14\right)\right]\right\}.}
\]
This estimate is rigorous for this particular Penrose 14-face cavity. **However, the unwanted \(+66\lambda\) term remains.** It cannot be absorbed into a \(C^{|Q|}(1+\lambda)^{a|Q|}\) prefactor as \(\lambda\to\infty\). The estimate therefore does **not** imply the desired local R3 retained-energy inequality.

A separate *conditional good-crossing* tail is possible: define \(\Gamma(U)=S_R(U^{\mathrm{flat}})-S_R(U)+S_A(U)\), the total crossing-energy increase for the exact word repair. On \(\{\Gamma(U)\le(1-\alpha)s_H(U_{H^c})+\eta|Q|/\lambda\}\), the same finite-net map and Jacobian prove
\[
\Pr\{\lambda s_H\ge t,\ \Gamma\le(1-\alpha)s_H+\eta|Q|/\lambda\}
\le\exp\left[-\alpha t+\eta|Q|+59\left(\tfrac32\log\lambda+\log4097+14\right)\right].
\]
There is **no proven control of the complement**, so this good-crossing result cannot be called the full desired tail.

## 5. An exact rational no-go for crossing-holonomy-preserving surgery on the immediate halo

One may hope to change all 89 exterior halo links in a correlated way while **preserving** all crossing plaquette holonomies and repairing all 24 interior-compatibility directions. This is impossible already to first order at the fully flat connection.

Let C comprise the **113 retained faces outside A** that touch at least one of the 89 halo links. Let \(D_{C,E}\) be their signed 113×89 face–exterior-link incidence matrix. Exact rational (SymPy) elimination gives
\[
\operatorname{rank}_{\mathbb Q}(D_{C,E})=67,
\qquad\dim\ker D_{C,E}=22.
\]
The rank available to move the 62 interior face curvatures **modulo H-link adjustments**, while requiring the first-order crossing-face holonomies to stay fixed, is
\[
\boxed{
\operatorname{rank}_{\mathbb Q}[D_H\ \ D_E(\ker D_{C,E})]
-\operatorname{rank}_{\mathbb Q}D_H
=\mathbf1.}
\]
Thus **only one of the 24 independent exterior curvature modes** is accessible through arbitrary correlated halo-link variations that preserve **all crossing holonomies to first order**. The other **23 modes necessarily disturb some crossing curvature**, unless more links outside this immediate halo move. This is an exact *linearized no-go*, not a general no-go against a larger/multiscale or probability-controlled surgery. It does not exclude transformations that preserve the *total crossing action* without preserving each holonomy separately.

This explains concretely why the 59-pivot flat repair is not automatically a Gibbs-decreasing repair: its crossing energy is an unavoidable part of the geometry.

## 6. Final mathematical status

| Requirement | Verified result |
|---|---|
| Exact classification of 24 exterior modes for Q14 | **Proved** via two primes and exact rational ranks |
| Joint nonabelian solution of all 62 adjacent retained plaquette equations | **Proved** by 59 Tietze pivots and residual free-group identities |
| Bounded local repair/word lengths for the fixed Q14 across nested volumes | **Proved**, 59 pivots, maximal expanded word 35 (original basis) |
| Three-color full-action-nonincreasing Haar surgery on 24 mode links | **Constructed**, multiplicity ≤8²⁴ |
| Full-net action-decreasing Gibbs surgery covering simultaneous 24-mode flat extension | **Proved**, with +66λ crossing penalty |
| Crossing-holonomy-preserving smooth surgery of all 24 modes in immediate halo | **Ruled out to first order** (only one mode available) |
| Requested unconditional polynomial-prefactor exponential tail for λs_H | **Not proved** |
| Uniform local retained-energy/R3 insertion theorem for arbitrary Q | **Not proved** |

**Next mathematical obligation:** bound the *Gibbs distribution of the 33 crossing-face transport cost*, or exhibit a multiscale correlated repair that carries the 23 obstructed modes into further shells with total action price \(O(|Q|(1+\log\lambda)/\lambda)\). Simply changing the 24 representative links or flattening their 62 adjacent faces cannot close the desired result.

## Reproduction

`python classify_modes.py` generates exact quotient bases and color classes across four volumes. `python exact_crossing_rank.py` performs the exact rational no-go. `python relative_words.py` and `python verify_joint_gluing.py` construct and audit the nonabelian 59-pivot flat extension. `python optimize_basis.py` records a lower-crossing 24-link basis. `python word_length_audit.py` measures expanded word complexity. `python joint_surgery.py` performs the executable three-color Q8 full-action surgery. `python theorem_certificate.py` verifies constants and writes the 24-mode CSV. Inputs are bundled: the previous direct-Z5 Penrose generator, physical prism face word builder, and exact Q14 seed construction. All code is self-contained except for installed Python packages NumPy and SymPy.
