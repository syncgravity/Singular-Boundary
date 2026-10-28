# The Singular Boundary — Collective Wilson sources and exact soft-mode form factors

**Date:** 2026-10-28. **Scope:** finite simply connected SU(2) Wilson spatial disks, their exactly gauge-invariant based mixed-trace sources, and the *Gaussian tangent Hamiltonian* of the strong-magnetic regime. No Monte Carlo, no substitution for historical Penrose results. **No volume/refinement-uniform nonlinear gap is proved.**

## Provenance and dependency

Historical canonical Penrose fixture: `HISTORICAL_Q14_CANONICAL.json` (`seed_faces_z5`) as recovered and cross-checked in the previous report `research/theorems/R3_IR_MULTIFACE_STRONG_FIELD_DUAL_LAPLACIAN_2026-10-28.md`. Its three source spatial rhombi have the exact oriented face-edge Gram matrix

\[
L=BB^{\mathsf T}=\begin{pmatrix}4&-1&-1\\-1&4&0\\-1&0&4\end{pmatrix},\quad
\lambda_1=4-\sqrt2,\quad v_1=(1/\sqrt2,1/2,1/2)^{\mathsf T}.
\]

The earlier proof identifies, for a **fixed** simply connected finite disk, a physical SO(3)-invariant harmonic tangent Hamiltonian as `b/a -> infinity`:

\[
H_{\mathrm{harm}}=-a\sum_{fg}L_{fg}\nabla_{y_f}\cdot\nabla_{y_g}+\frac b8\sum_f|y_f|^2,
\]

where each `y_f in R^3` is the based face log at the flat connection. All statements below explicitly distinguish this **harmonic operator** from the full nonlinear SU(2) Hamiltonian. A general single-well semiclassical reference is B. Simon (1983), *Semiclassical analysis of low lying eigenvalues I*, Ann. Inst. H. Poincaré 38, 295–308, https://www.numdam.org/item/AIHPA_1983__38_3_295_0/. This report derives the harmonic matrix elements explicitly; transferring them uniformly to growing nonlinear Penrose patches remains open.

## Theorem CW-1 — globally defined, positive, gauge-invariant collective curvature source (independently proved)

Choose a spanning tree of the finite connected graph, and transport every oriented face holonomy to the same root, obtaining `W_f in SU(2)`. Under vertex gauge transformations every based `W_f` transforms by the **same** root conjugation. Let `p(U) = ReTr(U)/2`. For any real `v_f`, define the genuine finite Wilson-word observable

\[
\mathcal Q_v=2\sum_{f,g}v_fv_g\{p(W_fW_g^{-1})-p(W_fW_g)\}.
\]

Write `W_f=s_f I+i u_f·σ`, with real `s_f²+|u_f|²=1`. The exact SU(2) quaternion identity

\[
p(UV^{-1})-p(UV)=2u(U)\cdot u(V)
\]

implies

\[
\boxed{\mathcal Q_v=4\left|\sum_f v_fu_f\right|^2\ge0.}
\]

Thus `Q_v` is a globally bounded positive scalar *gauge-invariant* Wilson polynomial. For a simply connected open disk, the based face holonomies are freely and independently specified after tree gauge fixing; maximizing the quaternion vectors parallel with signs `sign(v_f)` gives the **exact operator norm**

\[
\boxed{\|\mathcal Q_v\|_\infty=4\left(\sum_f|v_f|\right)^2.}
\]

This is exact for any finite SU(2) disk and any coupling. For normalized v with `Σ v_f²=1`, the norm lies between 4 and `4F`; a delocalized mode may have an extensive norm. For the authentic three-seed `v_1`, `||Q_{v_1}||∞=6+4√2`.

Near the flat connection, write `W_f=exp(i σ·y_f/2)`. Then `u_f= (1/2)y_f+O(|y_f|³)`; hence for fixed G,

\[
\boxed{\mathcal Q_v=\left|\sum_f v_fy_f\right|^2+O_G(\|y\|^4).}
\]

**Advance:** no ill-defined branch of `log(W_f)` is required to define a physical scalar source for a collective face mode. **Restriction:** based mixed-loop words can contain long spanning-tree connectors. These are gauge invariant but **not automatically spatially local** uniformly in patch size.

## Theorem CW-2 — exact physical Gaussian source correlator (independently proved)

Let `L` be positive definite with orthonormal eigenvectors `v_i` and eigenvalues `λ_i>0`. Set `z_i=Σ_f(v_i)_f y_f` in each of three adjoint color coordinates. The Gaussian Hamiltonian splits into isotropic 3D modes

\[
H_i=-a\lambda_i\Delta_{z_i}+\frac b8|z_i|^2.
\]

Let `ν_i=√(ab λ_i/2)` be the **one-quantum** excitation energy and `s_i²=√(2aλ_i/b)` the vacuum variance in one Cartesian coordinate of mode i. Each one-quantum mode transforms in the adjoint (spin-one) representation of the common residual SO(3) and is not physical. The centered quadratic mode `|z_i|²-E|z_i|²` is a pure, physical two-quantum scalar with exact excitation energy

\[
\Delta_i^{(2)}=2\nu_i=\sqrt{2ab\lambda_i}.
\]

Its connected correlation is

\[
\boxed{\langle\overline{|z_i|^2}(t)\,\overline{|z_i|^2}(0)\rangle_{\mathrm{harm}}=6s_i^4e^{-2\nu_it}
=\frac{12a\lambda_i}{b}e^{-\sqrt{2ab\lambda_i}\,t}.}
\]

The mode `i=1` has the exact *lowest physical harmonic gap* and is observed **perfectly** by the normalized quadratic `√[b/(12aλ_1)] (|z_1|²-E|z_1|²)`. To leading order near the flat connection it is the genuine Wilson source `Q_{v_1}` from CW-1, but global finite-coupling and graph-uniform transfer of the harmonic normalization is **not** established.

For an arbitrary real weighting `w_f` of *elementary fundamental plaquette traces* `p_f≈1−|y_f|²/8`, the exact harmonic connected correlator is

\[
\boxed{
C_{w}^{\mathrm{harm}}(t)
=\frac3{32}\sum_{i,j}
\left(\sum_f w_f(v_i)_f(v_j)_f\right)^2
s_i^2s_j^2 e^{-(\nu_i+\nu_j)t}.}
\]

The matrix elements follow by Wick's theorem in the unique Gaussian vacuum; no approximation is made to the **harmonic** correlator. The lowest 2ν_1 contribution has spectral weight

\[
\boxed{W_{1}(w)=\frac{3a\lambda_1}{16b}\left(\sum_fw_f(v_1)_f^2\right)^2.}
\]

For coefficients satisfying `|w_f|≤M`, this is at most `(3aM²/(16b))λ_1`. As the harmonic dual mode becomes soft (`λ_1 -> 0`), its **unrenormalized** elementary-plaquette spectral weight tends to zero. Thus a small spectral energy and a weakly observed mode can coexist. This is an exact Gaussian statement, not an assertion of a gapless nonlinear Wilson continuum.

## Theorem CW-3 — exact all-face scalar average and authentic seed (independently proved)

For the arithmetic mean of all F fundamental face traces, `w_f=1/F`, the modal matrix is diagonal: `Σ_f w_f(v_i)_f(v_j)_f=δ_ij/F`. Therefore

\[
\boxed{C_{\bar p}^{\mathrm{harm}}(t)=\frac{3a}{16bF^2}
\sum_{i=1}^F\lambda_i e^{-\sqrt{2ab\lambda_i}\,t}.}
\]

Because `Tr L=4F` for quadrilateral faces, the equal-time variance is exactly

\[
\boxed{\operatorname{Var}_{\mathrm{harm}}(\bar p)=\frac{3a}{4bF}.}
\]

On the original three-rhombus Penrose seed, the eigenvalues are `4−√2,4,4+√2`. The lowest singlet contribution to `C_\bar p` is

\[
\boxed{\frac{a(4-\sqrt2)}{48b}
 e^{-\sqrt{2ab(4-\sqrt2)}\,t}},
\]

and its full equal-time harmonic variance is `a/(4b)`. The first seed face on its own has lowest-mode weight `3a(4−√2)/(64b)`. The **mode-adapted** `Q_{v_1}` has harmonic lowest-mode weight `12a(4−√2)/b`, a larger and spectrally cleaner response before bounded-source normalization.

## Lemma CW-4 — why tree-based source bounds are not automatically local (independently proved)

If an edge occurs in a connector for a based loop `W_f=T_f H_f T_f^{-1}` but not in the local boundary word `H_f`, its variation acts through **conjugation**: under `T_f -> e^{tX}T_f`, `dW_f/dt=[X,W_f]` in the corresponding gauge convention. This derivative vanishes at `W_f=I` but need not vanish at nonflat configurations. For two based face holonomies whose imaginary unit vectors initially point along orthogonal axes, rotating only the second by angle t about a third axis gives the exact two-face source

\[
\mathcal Q(t)=4(1-\sin t),\qquad \mathcal Q'(0)=-4.
\]

A connector edge remote from either original plaquette can therefore affect a mixed collective Wilson observable at nonflat fields. One cannot apply an original-plaquette-local kinetic/mixing bound to Q_v **without** controlling connector derivatives and nonabelian transports. A common conjugation of *all* based words cancels through gauge invariance; the countertest rotates only a proper subset.

## Research consequences and next genuinely noncircular obligation

1. CW-1 **closes the algebraic existence problem** for a gauge-invariant, globally bounded collective-curvature Wilson source on each finite disk. It is already a single-trace polynomial source, requiring no logarithm or arbitrary source invention.
2. CW-2 and CW-3 give the **exact vacuum spectral measures** of harmonic sources. In particular, normalized elementary scalar averages can lose overlap with a soft collective mode; a uniform mass gap cannot be inferred from their apparent decay at finite times.
3. The physically observing normalizations `sqrt(b/(aλ_1))` and the global source norm `4||v_1||_1²` may diverge with magnetic coupling or volume. This is the precise observability/complexity barrier, not a proof that the nonlinear gap closes.
4. CW-4 exposes the large-field, based-transport derivative cost which a uniform nonlinear Dirichlet or transfer estimate must control.

**Next open theorem:** For the actual interacting SU(2) Penrose Hamiltonian and the explicit source `Q_v`, derive a **noncircular, graph/refinement-uniform** bound on its ground-state variance and Dirichlet form (or directly on its time-separated spectral measure), including connector cost and nonabelian large-field holonomies. The exact variational inequality

\[
\operatorname{gap}(H_G)\le\frac{\sum_e a_e\int|\nabla_e\mathcal Q_v|^2|\Omega_G|^2dU}{\operatorname{Var}_{\Omega_G}(\mathcal Q_v)}
\]

holds whenever the variance is nonzero. It is an **upper bound**, not a mass-gap proof. Any attempt to transfer the Gaussian low-mode rate uniformly must confront the possibility of nonperturbative mass generation, the very phenomenon at issue; it cannot assume a scale-independent Gaussian approximation. A separate **lower** coercivity argument is required to prove a positive mass gap.

**Status ledger:** CW-1 independently proved exact finite SU(2) source identity and norm; CW-2/CW-3 independently proved harmonic spectral measures and finite authentic seed specialization; CW-4 independently proved connector-locality caveat; interacting nonlinear multiface low-energy form factors and regulator/volume-uniform mass gap **OPEN**.

## Integrity and reproducibility

Read-only deterministic script `scripts/audit/verify_collective_wilson.py`, exact certificate and SHA-256 manifest in accompanying derived audit package. No original R3 or Stage 7–35 archive changes, simulations, or new historical results. Verification fixtures are the three original spatial Q14 seed labels, not a reconstruction of the complete temporal Q14 or the older twelve-prism problem.