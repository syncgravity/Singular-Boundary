# P0–T2: exact four-plaquette recovery under Haar blocking

**Date:** November 5, 2026. **Scope:** kinematic SU(2) Wilson-character algebra on a subdivided planar face of a finite three-dimensional cubical lattice; no interacting state, effective Hamiltonian, Yang–Mills mass gap, or quasicrystalline/gravitational continuum claim. A mathematical follow-up to the exact one-face Haar-block magnetic-information-loss result. **Status:** finite algebraic result, source-qualified and open to independent mathematical review.

## 1. The obstruction and the recovery mechanism

The preceding record proves that for the coarse-link holonomy-product injection `J` between dyadic cubic lattices, the adjoint Haar conditional expectation annihilates **each single** refined plaquette fundamental character: `J* chi_1(U_p) J=0` for all elementary fine plaquettes `p`. Consequently `J* V_fine J` is a scalar, not the coarse magnetic Hamiltonian.

A single coarse face is nevertheless tiled by a `2×2` group of **four** refined coplanar faces. Their characters have a nonvanishing **joint** conditional expectation. The exact coefficient is **1/8**, rather than the naive independent-pairing estimate `1/16`, because the central fine vertex contributes a closed fundamental index loop of dimension two.

## 2. General planar face-block lemma

Let `B` be a simply connected, oriented rectangular union of `F=mn` elementary faces of the fine square grid, embedded in one coordinate plane of a cubical spatial lattice. Let `E_int` be its edges in the interior of `B`, and `V_int` its interior vertices; every interior edge borders two oppositely oriented face boundaries. Let `U_{∂B}` denote the ordered SU(2) holonomy around the outer boundary. Denote by `chi(U)=tr_fund(U)` the unnormalized 2-dimensional SU(2) fundamental character, with normalized Haar measure on each interior edge.

**Lemma (Haar face-block recovery).** Keeping all boundary fine-edge holonomies fixed, integrating the interior original-link variables independently with Haar gives

\[
\boxed{ \mathbb E_{E_{\rm int}}\!\left[\prod_{p\subset B}\chi(U_{\partial p})\mid U_{\partial B}\right]
 = 2^{\lvert V_{\rm int}\rvert-\lvert E_{\rm int}\rvert}\chi(U_{\partial B})
 = 2^{1-F}\chi(U_{\partial B}). }
\]

For any nonempty **proper subset** `S` of the elementary faces of `B`,

\[
\boxed{\mathbb E_{E_{\rm int}}\!\left[\prod_{p\in S}\chi(U_{\partial p})\mid U_{\partial B}\right]=0.}
\]

**Proof.** Expand each fundamental trace in matrix indices in the common face orientation. An interior link appears once in the trace of each of its two neighboring faces, with opposite link traversal. The normalized Haar matrix-element identity in the defining irreducible SU(2) representation is

\[
\int U_{ab}(U^{-1})_{cd}\,dU=\tfrac12\delta_{ad}\delta_{bc},\qquad \int U_{ab}\,dU=0.
\]

Integrating all interior edges therefore joins the face-index strands along their common boundaries, contributing a factor `1/2` for every interior edge. After these contractions there remains precisely one free closed fundamental index loop at each interior vertex, contributing a factor `2`, and one outer boundary trace, giving the first equality. For a topological disk, the cellular Euler identity `V−E+F=1`, together with equal numbers of boundary vertices and boundary edges, yields `|V_int|−|E_int|=1−F`, proving the second equality. If `S` is a proper nonempty subset of faces, some interior edge borders exactly one selected face; its integrand has one unpaired defining-representation matrix factor. Haar integration of that edge vanishes. ∎

This is an **operator identity for the Haar conditional expectation of multiplication observables**, not an interacting-state identity. Conditional expectations in the physical gauge-invariant subspace inherit it because all traced face expressions are gauge invariant. It is equally valid for a fixed product of coarse boundary holonomies because the ordered fine boundary product telescopes to the coarse loop holonomy.

## 3. Exact dyadic 2×2 corollary

For the four elementary fine faces `p_1,...,p_4` tiling a single coarse plaquette `P`, the internal fine grid has **four interior edges and one interior vertex**:

\[
\boxed{ J^*\!\left[\prod_{i=1}^4\chi_1(U_{p_i})\right]J
=\frac18\chi_1(U_{\partial P}) }
\]

as multiplication operators on coarse-cylinder functions. Any product of distinct `chi_1(U_{p_i})` over a nonempty proper subset has zero Haar compression. The identity provides an **explicit gauge-invariant face-aware observable** whose coarse Wilson content survives the same kinematic projection that annihilates the individual refined plaquettes. In particular, normalized product Haar gives the exact two-scale overlap `⟨J chi_1(U_{∂P}), ∏_i chi_1(U_{p_i})⟩ = 1/8`, because the coarse Wilson character itself has Haar squared norm one.

For a general `m×n` face block, its all-face product survives with coefficient `2^{1-mn}`. Thus a unit-coefficient bare reconstruction through this particular scalar-character product requires multiplying by `2^{mn-1}`. This may be a strongly ill-conditioned observable normalization under repeated refinement. It is **not** a derived Yang–Mills coupling flow: the actual interacting effective action, vacuum measure, and renormalization need not coincide with this reference-Haar calculation.

An alternative exact cylinder representative of `chi_1(U_{∂P})` is the ordered product of **parallel-transported face holonomy matrices**, using connectors to a common basepoint (a nonabelian lattice Stokes identity). Unlike the untransported scalar-character product, that based matrix construction yields the coarse trace with coefficient one, but the connector choice and fine-link information must be retained explicitly. Neither representation proves effective-action or physical-time correlation compatibility.

## 4. Exact deterministic regression

`verify_fine_plaquette_cluster.py` independently checks this identity for `1×2`, `1×3` and `2×2` oriented fine-face patches, with five distinct boundary assignments in each geometry. It computes **all** nonempty proper squarefree subset products. The checker integrates every interior edge over the finite quaternion group `Q8={±1,±i,±j,±k}` and uses rational arithmetic for the averaged fundamental traces.

This finite sum is an **exact check of the relevant SU(2) Haar first and mixed second matrix moments**, not an approximation: the restriction of the two-dimensional defining SU(2) representation to `Q8` is an irreducible complex representation, so its Schur orthogonality relations have the same `1/2` matrix-element coefficient. Each interior edge occurs at most twice, once in each adjacent face trace. Therefore the `Q8` integration reproduces precisely the Haar contractions needed for these polynomials, for every fixed boundary assignment. The **proof for arbitrary face grids** is the preceding index-contraction argument, not the finite enumeration.

The checker reports 15 exact cases and verifies coefficient `1/8` on each `2×2` patch. All nonempty proper subsets of the four faces vanish under the conditional expectation, including cases with noncommuting boundary group variables.

## 5. Consequence for the actual P0/P2 program

Together the two verified results distinguish **magnetic Hamiltonian compression** from **magnetic observable recovery**:

- **Naive bare-generator compression fails:** `J* V_fine J` is a scalar. Refinement of bare dynamics does not commute with Haar holonomy blocking.
- **A face-block observable survives:** `J*(product of 4 fine Wilson characters)J=(1/8) chi(coarse Wilson)`. The constituent elementary magnetic characters separately vanish.
- **Still missing:** a physically justified interacting conditional measure/action, compatible coarse block observables and vacuum centering, an **interacting** two-scale physical-time correlation estimate with constants uniform under further refinement and large spatial boxes, and ultimately a nontrivial OS continuum reconstruction with a positive gap.

A useful subsequent investigation is to test this four-plaquette operator with the finite **interacting heat-kernel-transfer** measure at two resolutions and explicitly calculate its connected correlation, counterterms, and leading source orders, before proposing a uniform multiscale theorem. The kinematic `1/8` coefficient by itself does not grant any infrared or continuum estimate.

**Scientific status:** P0 kinematic source/geometry, this exact face-block identity, and finite transfer positivity are documented. P0 physical renormalization, P2 uniform interacting multiscale dynamics, P4 nonzero physical gap, P5 continuum existence, Penrose transfer and quantum-gravity UV finiteness all remain **OPEN**. No updates to the canonical claim ledger or historical data are implied by this draft.
