# R3-IR — Exact gauge-reduced flat magnetic Hessian and Penrose isoperimetric coercivity

**Date:** 2026-10-28. **Status:** independently proved finite-dimensional classical quadratic theorem for the declared Wilson potential, including a regulator-uniform lower bound on the **gauge-reduced flat Hessian** on bounded physical-area planar rhombus disks. Exact rank obstruction for deleting bad faces. **Not proved:** nonlinear near-flat Hessian coercivity, probability-weighted Bakry–Émery inequality for the true quantum vacuum, fixed-support variance `o(h)`, parity-resolved resolvents, continuum, or physical mass gap. Source-level Stage7/26 correspondence and Q14 temporal certificate remain separate open provenance issues.

## 1. Geometry, conventions, and boundary condition

Let `K` be a finite embedded face-complete edge-to-edge planar rhombus cell decomposition of a **topological closed disk**. Each face has four edges of common length h and Euclidean area between `sigma_- h²` and `sigma_+ h²`, with `sigma_->0`; each edge belongs to either one boundary face or two interior faces. Assume `F h² <= A0` for fixed physical area proxy A0. Let `V,E,F` be counts of vertices, oriented edges, oriented faces. Orient every face counterclockwise and each edge arbitrarily. Let `d0:R^V ->R^E` be the signed vertex-edge incidence matrix, `d1:R^E->R^F` the signed face-edge incidence matrix. On the chosen disk

`d1 d0=0`, `rank(d0)=V-1`, `rank(d1)=F`, `E=(V-1)+F`, and `ker(d1)=im(d0)`.

The **gauge quotient here allows gauge transformations at all vertices, including boundary vertices**, and the quotient norm is the minimum Euclidean edge norm in an infinitesimal gauge orbit. A fixed-boundary *non-gauge-reduced* state space would have additional directions and requires separate boundary analysis; the theorem must not be transplanted to it. A non-simply-connected surface can have additional harmonic flat directions not captured by `im(d0)`.

On `(SU(2))^E` with the metric normalized by `-Delta chi_(1/2)=3 chi_(1/2)/4`, put `p_f=(1/2)ReTr(W_f)`, `d_f=1-p_f`, and `Vmag(U)=sum_f b_f d_f`, with `b_f>=beta_min h^-2>0`. All link variations are represented by orthonormal `su(2)` triples `X_e`, using `U_e(t)=exp(t X_e)` at the identity after a flat-connection gauge transformation. The magnetic Hessian is a classical potential Hessian, **not** the logarithmic Hessian of the interacting ground-state density.

## 2. Theorem GH-1 — Exact full mixed-link Hessian at flat connection

At every flat configuration on a simply connected disk, a vertex gauge transformation sets every link to identity. Since the normalized SU(2) trace satisfies `p(exp(t Z))=1 - t²|Z|²/8+O(t^4)` for unit-speed metric vectors, the oriented face product obeys

`W_f(t)=exp(t (d1 X)_f+O(t²))`, hence

**`Hess Vmag_flat(X,X) = (1/4) sum_f b_f |(d1 X)_f|²`**. (GH-1)

The formula holds separately on each of the three Lie algebra components; full mixed-link blocks are automatically included. By cellular exactness, the kernel is exactly `im(d0) tensor su(2)`, the infinitesimal gauge transformations. Hence **after quotienting by full vertex gauge, the flat magnetic Hessian is strictly positive**. This corrects a possible overreading of the preceding two-link zero-mode witness: the witness invalidates coercivity on *unreduced* links, but does not invalidate it after gauge reduction on a disk.

## 3. Theorem GH-2 — Quantitative uniform lower bound via Euclidean isoperimetry

For consistently oriented planar faces, two adjacent faces traverse their common edge in opposite directions. Therefore, letting `Adual` be the adjacency matrix of the face dual graph (outer face represented by zero Dirichlet boundary values),

**`d1 d1* = 4 I_F - Adual =: Ldual_D`**. (GH-2)

For every `u in R^F`, put `u_outer=0`. Its Dirichlet energy is

`Q(u)=<u,Ldual_D u>=sum_{dual edges} (u_f-u_g)²`,

where an edge to the exterior contributes `u_f²`. Define `S_t={f:|u_f|²>t}`. Since the corresponding union of actual rhombi has physical area at least `sigma_- h² |S_t|` and boundary length exactly `h #partial S_t`, the Euclidean planar isoperimetric inequality (valid also for disconnected regions and regions with holes) gives

`#partial S_t >= 2 sqrt(pi sigma_- |S_t|) >= [2 sqrt(pi sigma_-)/sqrt(F)] |S_t|`.

Layer cake (discrete coarea) then yields

`W:=sum_{dual edges} ||u_f|²-|u_g|²| = int_0^infty #partial S_t dt >= [2 sqrt(pi sigma_-)/sqrt(F)] ||u||²`.

Cauchy–Schwarz and each face having four incident dual edges give

`W²<=Q(|u|) sum_{dual edges} (|u_f|+|u_g|)² <= 8 Q(u) ||u||²`.

Combining proves

**`lambda_min(Ldual_D) >= pi sigma_-/(2 F)`**. (GH-3)

The nonzero spectra of `d1* B d1` and `B^(1/2) d1 d1* B^(1/2)` coincide for the positive diagonal `B=diag(b_f)`; thus their least positive eigenvalue is at least `b_min pi sigma_-/(2F)`. Using GH-1 and `b_min>=beta_min h^-2`, `Fh²<=A0`, obtains for every `X perpendicular to im(d0) tensor su(2)`:

**`Hess Vmag_flat(X,X) >= [beta_min pi sigma_-/(8 A0)] ||X||²`.** (GH-4)

This bound is uniform under bounded-physical-area Penrose refinement, without translation invariance and without invoking a quantum gap. It is valid even when the face dual graph is not periodic. The bound is conservative; the authentic three-rhombus seed gives a substantially larger eigenvalue.

### Important norm qualification

The orthogonal complement and eigenvalue are computed in the **unweighted bi-invariant link tangent metric** specified above, whereas the physical kinetic form weights link derivatives by `a_e`. Under fixed positive bounds `a_min<=a_e<=a_max`, these norms are uniformly comparable, but converting GH-4 into an interacting quantum statement still requires controlling the vacuum score Hessian and the nonflat geometry. GH-4 cannot by itself establish a source Poincaré inequality or mass gap.

## 4. Theorem GH-3 — Removing bad faces creates exact additional non-gauge null modes

Let `G` be any strict subset of the full set of F faces, containing `F_g=F-N_bad` good faces, and retain only the corresponding positive flat quadratic terms:

`Hess V_G,flat = (1/4) d1_G* diag(b_f:f in G) d1_G`.

Because the full face-row system has rank F, **every subset of rows is linearly independent**; hence `rank(d1_G)=F_g`. The dimension of the kernel on one Lie algebra component is `E-F_g=(V-1)+N_bad`. After gauge reduction it has exactly **`N_bad` extra physical zero directions per Lie algebra component** (thus `3 N_bad` for SU(2)). (GH-5)

The previous probability-weighted core theorem PC-2 shows `h²N_bad` tends to zero in every fixed L^r when the good-face threshold is `1-h^gamma`, but does **not** show `N_bad=0` with high probability. It even permits `N_bad` diverging. Therefore *discarding all bad magnetic terms* cannot establish coercivity on the entire physical tangent space. The bad terms may contribute mixed and indefinite Hessian components; they cannot simply be omitted and replaced with an arbitrary positive remainder.

The nonzero eigenvalues of the good-face-only Hessian still satisfy the same isoperimetric lower bound with `F_g` in place of F, because the union of any subset of its good rhombi remains an ordinary planar region and missing faces are correctly treated as exterior Dirichlet boundaries. **Positivity on the image** is thus uniform, while the new physical kernel remains real.

## 5. Exact canonical Penrose Z^5 seed certificate

Use the three original spatial seed rhombi: `V=8,E=10,F=3`. The deterministic script constructs all face and vertex incidence matrices directly from the five-coordinate vertex labels (not from invented nearby geometries) and checks

`d1 d0=0`, `rank(d0)=7`, `rank(d1)=3`, `10=7+3`.

With consistent face orientations, the exact face Dirichlet matrix has eigenvalues

**`4-sqrt(2), 4, 4+sqrt(2)`**.

For uniform b>0, the full magnetic Hessian has exactly 3 positive edge-sector eigenvalues `b(4-sqrt(2))/4`, `b`, `b(4+sqrt(2))/4` *per Lie algebra coordinate* and 7 pure gauge zero modes per coordinate. Removing any one of the three faces produces one additional gauge-reduced zero mode per coordinate. The planar Cheeger lower bound `pi sin(pi/5)/(2F)` is verified below the actual least positive eigenvalue. This exact spatial fixture does not verify the Stage26 temporal certificate Q14.

## 6. Why the desired quantum covariance proof remains OPEN

The theorem is **at exactly flat connections** and is about the magnetic potential's second derivative. The interacting vacuum has small *average* face deficit but it has not been proved to occupy a tube uniformly close to a single flat-connection gauge orbit. Even configurations with all plaquettes individually satisfying `1-p_f<h^gamma` can accumulate nontrivial holonomy over macroscopic loops. The probability-weighted core may also contain numerous bad plaquettes; dropping them produces the additional physical zero directions of GH-5.

A Bakry–Émery or Brascamp–Lieb step for the actual vacuum would involve the Hessian of `-2 log Omega_h`, not only of `Vmag`. The vacuum eigenvalue equation alone determines a scalar Laplacian/gradient combination and does not give the needed uniform matrix lower bound on `Hess(-2 log Omega_h)`. Moreover, boundary gauge conventions, nontrivial topology, and the spectral contribution of weak exceptional modes must be treated explicitly.

The desired `Var_{Omega_h}(h sum_D q_fd_f)=o(h)`, parity-resolved quartic response, quantum continuum reconstruction, and positive physical mass gap remain **OPEN**. GH-4 is a new **classical gauge-reduced coercivity input**, not a quantum gap theorem.

**Next noncircular obligation:** derive a probability-weighted quantitative comparison of the true ground-state score Hessian with the gauge-reduced flat magnetic quadratic form, including defects and holonomy accumulation, or establish an independent covariance bound using the ground-state Dirichlet form. A possible finite check is to build the full gauge-reduced nonlinear Hessian on genuine small Penrose patches away from the flat configuration and search for low-curvature configurations with weak physical modes, using the original Hamiltonian normalization.

## 7. Reproducibility

`verify_gauge_reduced_hessian.py` constructs the exact canonical spatial seed incidence, gauge kernel, oriented dual matrix, algebraic eigenvalues and loss of rank on deleting faces. The planar Cheeger/isoperimetric result is a written mathematical proof and is **not inferred from the three-face test**. No Monte Carlo was performed, and no original user archives or source simulations were altered.
