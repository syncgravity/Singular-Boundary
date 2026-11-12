# The Singular Boundary — P0 refinement intertwining and P4 source-visible spectral-weight audit

**Research continuation; prepared November 4, 2026 (America/Denver).** The artifact filenames use the UTC archive date November 5, 2026. This is a *new, independently checked conditional research note*, not a continuum Yang–Mills theorem or a certification of the historical Penrose regulator. Its source inputs are the supplied `Sharpe_dissertation_v10.7.tar.gz`, the eight Stage 26 compact archives and eight multihit sweep files, `global_whitney_11face.npz`, and the private repository's canonical P0 specification and P-53/P-55/P-78 theorems. Tests distinguish exact integer identities and symbolic proofs from numerical SU(2) regressions. The archive does not modify historical inputs.

## A. Source-identity gate: historical geometry is not the certified 3D SU(2) family

The original dissertation, Chapter 3, explicitly decomposes `R^5 = R^2_parallel + R^2_perp + R` and distinguishes a coupled `Z^5` Laplacian from a Penrose-plane/compact-coordinate product operator. It describes `z_2` as carrying a compact direction and a proposed time identification. Appendix C lists the *3D icosahedral extension from Z6* as an open question. These are the dissertation's statements, **not** independently proved identities of four-dimensional quantum Yang–Mills theory.

The eight compact Stage 26 ZIPs have **100** recorded `outer_*.npz` checkpoints each, covering sweeps 10020 through 12000 in steps of 20; the full Penrose seed-101 ZIP contains in addition a restart state and latest-record manifest. The eight sweep-10000 NPZ files each have `dx` with shape `(600,2)` and are therefore explicitly planar spatial displacement data. Each sweep metadata `source_checkpoint_sha256` agrees with the common `source_sha256` metadata within its corresponding Stage 26 checkpoints. This is **metadata linkage**, not byte verification of an omitted sweep-10000 checkpoint; compact Stage 26 files begin at sweep 10020. The archived `global_whitney_11face.npz` contains a `30 × 30` matrix and 30 edge IDs, which by itself does not specify a 3D family of complexes. SHA-256 hashes of the exact supplied files and the ZIP CRC checks are in `attached_source_manifest.json`.

The repository's `R3_ORIENTED_PRISM_CHAIN_AND_GAUGE_HAMILTONIAN_2026-10-31.md` explicitly calls the prism model a candidate **alternative** to the nonseparable coupled-Z5 construction, and the P0 repository audit reports no certified genuine fixed-domain prism refinement. The three constructions cannot be silently identified.

**Source-certification verdict:** genuine source-certified 3D Penrose/coupled-Z5 refinement remains OPEN. The source audit below instead supplies a **cubic reference** with complete elementary refinement maps; it does not transfer historical Penrose conclusions.

## B. Exact open-cube 3D cellular refinement benchmark

Fix the spatial box `[0,1]^3` with open boundary. The standard oriented cubical cell complex `K_n` consists of integer-grid vertices `0 <= i_j <= n` with pitch `a_n=1/n`, max cube diameter `sqrt(3)/n`; positively oriented edge, face and cube cells are obtained by choosing ordered coordinate-axis subsets. Its cell counts are exactly

\[
(C_0,C_1,C_2,C_3)=\bigl((n+1)^3,3n(n+1)^2,3n^2(n+1),n^3\bigr).
\]

For a k-cell `c=(o;a_1<...<a_k)`, with face coordinates, its integer cellular boundary is

\[
\partial c=\sum_{j=1}^k(-1)^{j-1}\bigl[(o+e_{a_j};a_1,\dots,\widehat a_j,\dots,a_k)-(o;a_1,\dots,\widehat a_j,\dots,a_k)\bigr].
\]

Define `S_k:C_k(K_n)->C_k(K_{2n})` by subdividing every active coordinate interval in two and summing the resulting `2^k` positively oriented small k-cells. Then **on every individual basis cell**

\[
\boxed{\partial_{k}S_k=S_{k-1}\partial_{k},\quad k=1,2,3.}
\]

**Proof:** Terms on internal subfaces of an oriented subdivision occur in pairs with opposite signs; external fine subfaces sum to the subdivision of the corresponding coarse boundary face. This is an exact combinatorial chain-map identity. The usual cubical boundary cancellation also gives `partial_1 partial_2=0` and `partial_2 partial_3=0`. These two statements are distinct from nonabelian Wilson plaquette relations.

The tested cases `n=1,2,3` have cell counts `(8,12,6,1)`, `(27,54,36,8)`, `(64,144,108,27)`. Independent GF(2) boundary ranks are `(7,5,1)`, `(26,28,8)`, `(63,81,27)`, yielding homology dimensions `(1,0,0,0)`; this is consistent with the contractible cube. The checker passed **186** exact integer chain-composition assertions and **396** exact integer refinement-commutation assertions. The general chain map is proved by local cancellation, not by extrapolation from these three examples.

This supplies an actual `a_n->0` 3D cubic geometric reference. It does **not** establish a compatible Yang–Mills Hamiltonian limit.

## C. New no-go for naive *exact* SU(2) Hamiltonian intertwining

Let `G=SU(2)`, with normalized Haar measure on every oriented link and the vertex action `U_{v w} -> g_v U_{v w} g_w^{-1}`. Given `K_n -> K_{2n}`, define the cylindrical pullback `J_n` by replacing each coarse link variable with the ordered product of its **two** fine-link variables along the same segment. Coarse-edge refinement paths have mutually disjoint sets of fine edge interiors. Therefore the pushforward of the product fine-link Haar measure is product coarse-link Haar, giving an **isometry**

\[
\boxed{J_n:L^2(G^{E_n})\hookrightarrow L^2(G^{E_{2n}}),\quad\|J_nf\|_2=\|f\|_2.}
\]

Under arbitrary fine vertex gauge transformations, the internal gauge factors telescope along every coarse path; thus `J_n` sends coarse Gauss-invariant functions to fine Gauss-invariant functions.

Take the positive single-link Casimir `C_e=-sum_a X_{e,a}^2` with `C_e chi_1=3 chi_1/4` when that link enters a fundamental character. On the *unreduced original-link* gauge-invariant Hilbert spaces define the benchmark electric operators `K_n^E=alpha_n sum_e C_e`, `alpha_n>0`. For the fundamental character `W_f` around one elementary coarse face, each of the **four** boundary edges contributes `3/4`; under `J_n`, its refined perimeter has **eight** nontrivial fine-link edges. Consequently

\[
\boxed{K_n^E W_f=3\alpha_n W_f,\qquad K_{2n}^E J_nW_f=6\alpha_{2n}J_nW_f.}
\]

Hence **exact strong intertwining `K_{2n}^E J_n = J_n K_n^E` is impossible on this Gauss-invariant test vector unless**

\[
\boxed{2\alpha_{2n}=\alpha_n.}
\]

The same Casimir calculation holds for every coarse cylindrical function because a generator on either of the two fine links acts as a left or right generator on the product, and the bi-invariant Casimir acts identically from either side. Thus, in fact,

\[
K_{2n}^EJ_n =\frac{2\alpha_{2n}}{\alpha_n}J_nK_n^E
\]

on smooth coarse cylindrical functions. For the conventional Kogut–Susskind coefficient `alpha_n=g_0(a_n)^2/(2a_n)`, exact intertwining would require `g_0(a_n/2)^2=g_0(a_n)^2/4`. In a weakly running asymptotically free regime where the adjacent-scale ratio `g_0(a/2)^2/g_0(a)^2 -> 1`, the kinetic intertwining ratio instead approaches 4. This is a **no-go for a particular naive exact intertwiner**; it does not rule out renormalized embeddings or convergence of properly reconstructed continuum dynamics.

The naive magnetic intertwiner also fails. Put all fine-link holonomies on a single subdivided coarse face equal to identity, except one strictly internal fine edge with `U=diag(exp(i*pi/3),exp(-i*pi/3))`. The outer coarse Wilson boundary has trace 2, so its normalized local potential `1-(1/2)chi_1(U_outer)` equals zero, but two adjacent fine plaquettes each contribute `1-cos(pi/3)=1/2`. Thus

\[
\boxed{\textstyle\sum_{p\subset f} [1-\tfrac12\chi_1(U_p)]=1\ne0=1-\tfrac12\chi_1(U_{\partial f}).}
\]

This is independent of the coefficient normalization and does not assume Abelianization of SU(2). Numerical regressions using random SU(2) matrices verify gauge covariance of the refined coarse Wilson loop at error < `5e-16` and the explicit potential witness. The underlying analytic group identities are exact.

**Consequences:** the geometric chain map and isometric gauge-compatible embedding are legitimate, but neither implies operator intertwining, an effective action identity, renormalization, or a positive continuum gap. A P0 regulator *acceptance criterion should distinguish topology, kinematics, and the actual scale-comparison theorem*.

## D. Conditional P4 advance: explicit source-visible spectral weight away from zero

This is a corollary within the **corrected finite straight-strip** model, not an assertion about the cubic benchmark. For every finite strip, take `H_N=K_N+lambda V_N`, the normalized positive ground vector `psi_N`, and the local gauge-invariant multiplier `f=chi_1(U_j)`. Let `mu_N` be the nonnegative excitation-energy spectral measure of `f psi_N` for `H_N-E_N`. The P-78 ground-state transform proves `m_1=∫E dmu_N=4-<chi_1^2>`. The independent f-sum audit supplies a common lower bound `m_1 >= c(lambda)` in the *anchor-averaged* states and their thermodynamic subsequential limits, where

\[
\boxed{c(\lambda)=\frac{6+2|\lambda|-\sqrt{4|\lambda|^2+6|\lambda|}}{2+|\lambda|}>0.}
\]

We now make the local second-frequency moment explicit. The finite-strip corrected electric operator has the P-78 **sum-of-squares** form

\[
K_N=2\sum_i C_i+\sum_{i<N,a}(R_i^a+L_{i+1}^a)^*(R_i^a+L_{i+1}^a)+C_1+C_N,
\]

where the notation for `C_i` is the positive single-site Casimir. Choosing first-order skew-derivative operators `D_alpha` with their square-root coefficients, we have `K_N=sum D_alpha^*D_alpha`, the derivation identity and, for interior `j`, `K_N f=3f`, `||K_Nf||_infty<=6`, and the pointwise carré du champ `sum_alpha |D_alpha f|^2=4-f^2<=4`. Since magnetic multiplication commutes with `f`,

\[
(H_N-E_N)f\psi_N=[K_N,M_f]\psi_N,
\]

and the product rule yields

\[
\|[K_N,M_f]\psi_N\|_2^2\le 2\|K_Nf\|_\infty^2+8\|\Gamma(f,f)\|_\infty\,\mathcal E_{N,j}
\le72+32\mathcal E_{N,j},
\]

where `E_(N,j)` is the energy of the sum-of-squares terms differentiating site `j`. The elementary inequalities `||R_j+L_(j+1)||^2 <= 2(||R_j||^2+||L_(j+1)||^2)` imply

\[
\boxed{\mathcal E_{N,j}\le 6\langle C_j\rangle+2\langle C_{j-1}\rangle+2\langle C_{j+1}\rangle,}
\]

with exterior-site energies zero; for endpoints this inequality remains conservative. The P-55 translation-anchor average and `sum_i <C_i> <= N|lambda|/2` imply `overline{<C_j>}<=|lambda|/2` for any fixed location. Therefore the anchor-averaged second spectral moment obeys the uniform quantitative bound

\[
\boxed{m_2:=\int_0^\infty E^2\,d\mu(E)\le72+160|\lambda|=:M_2(\lambda).}
\]

The bound survives weak subsequential limits by lower semicontinuity; the first moment is uniformly integrable because of the second-moment estimate. Also `m_0<=||f||_infty^2<=4`. For `epsilon=c(lambda)/8`, split the first moment into `E<epsilon` and `E>=epsilon`. The first portion is at most `epsilon*m_0<=c/2`, whence

\[
\int_{E\ge\epsilon}E\,d\mu(E)\ge c/2.
\]

Cauchy–Schwarz then gives **a strictly positive *source-visible spectral mass above a positive threshold***:

\[
\boxed{\mu([\epsilon,\infty))\ge\frac{c(\lambda)^2}{4(72+160|\lambda|)},\qquad \epsilon=\frac{c(\lambda)}8.}
\]

At `|lambda|=1`:

\[
\boxed{\epsilon\approx0.20157176416,\qquad\mu([\epsilon,\infty))\ge0.0028021500763.}
\]

**Scope and caveat:** These are lower bounds on *a high-energy portion of the measured positive-frequency spectral weight*, not a lower bound on the bottom of the spectrum. The measure may additionally have arbitrary weight at every energy near zero, and an atom at E=0 is not excluded. The bound neither establishes a common infinite-volume dynamics nor a positive gap. It is an explicitly quantified P4 source-visibility statement conditional on the recorded P-53/P-55/P-78 hypotheses. The nontrivial infrared mass-gap bound remains OPEN.

## E. Next noncircular proof steps

1. **P0:** Recover source-level generating code for the coupled-Z5 geometry and produce a *single* source-certified genuine three-dimensional refinement with 3-cells, exact incidence, gauge-covariant link transport, and electric/magnetic coefficients from a common action. For the cubic control model, study a legitimate renormalization / cylindrical scale-comparison map instead of requiring naive exact Hamiltonian intertwining.
2. **P2:** Continue the P-77 source-adapted five-state MPO and gauge-twirl program, but resolve genuine `N~m^2` nuclear response with usable two-sided certificates. A polynomial MPS representation is not a trace-norm estimate.
3. **P4:** Prove a true *upper* bound on connected correlation support at low energies, or a spectral inequality that excludes all excitation weight in `(0,Delta)` for source-complete gauge-invariant observables, with proper infinite-volume dynamics. The current positive-frequency lower mass is only a consistency diagnostic.
4. **P5:** Track the physical energy normalization and show any gap survives both volume and lattice-spacing limits in a rigorously reconstructed 4D theory. Do not equate either cubic benchmark or straight strip with the historical coupled-Z5 candidate without an explicit intertwiner and action-level identity.

### Provenance and verification

- Private repository sources: `docs/research/REPOSITORY_REVIEW_AND_P0_OBJECTIVE_2026-11-04.md`, `docs/research/PROOF_DEPENDENCIES.md`, `research/theorems/R3_ORIENTED_PRISM_CHAIN_AND_GAUGE_HAMILTONIAN_2026-10-31.md`, `research/theorems/R3_IR_REPOSITORY_REVIEW_3D_PERIODIC_CURL_SPECTRUM_2026-11-04.md`, `research/audits/P2_BERNSTEIN_SCHATTEN_THERMODYNAMIC_LOCAL_MEASURES_2026-11-04.md`, `research/audits/P2_CENTRAL_BINOMIAL_SCHATTEN_LOCALLY_NORMAL_QUANTUM_2026-11-04.md`, and `research/audits/P2_SOURCE_MPO_RESIDUAL_CYLINDER_DIRICHLET_2026-11-04.md`.
- New exact integer/GF2 checker: `verify_p0_refinement.py`, output `verification.log` and `p0_refinement_verification.json`.
- Source read-only provenance checker: `audit_attached_sources.py`, output `attached_source_audit.log` and `attached_source_manifest.json`.
- New symbolic source-visible spectral mass checker: `verify_source_visible_spectral_weight.py`, output `spectral_weight_verification.log`.
- File integrity manifest: `SHA256SUMS.txt`, with unmodified uploaded source files **not bundled into this package**.

**Research ledger handling:** This is a draft proposal for independent mathematical review; does not overwrite any historical claim ledger, alter archived numerical data, renumber the Observatory proof paths, or represent a P0/P5 closure.