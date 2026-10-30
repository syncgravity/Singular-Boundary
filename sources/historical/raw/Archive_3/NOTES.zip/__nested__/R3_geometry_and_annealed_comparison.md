# R3: geometry admissibility and annealed / collar-relaxed comparison
28 October 2026. Status: a new conditional exact identity, not unrestricted R3 closure.

## Source inspection
- The uploaded `Branch · Branch · Compare Continuum Mass Gaps.txt` describes a four-plaquette spatial model, 15-state shared-edge recoupling, and a three-step 12-prism complex; it does not furnish an oriented incidence table for the target insertion/cavity pair.
- `penrose_complete_catalogue.npz`: keys `idx, sign, length, roots, distance, target, faces, cidx, csign, clength, ckind, F, graph_hash, threshold, coverage_version`; `F=22808`, path entries `(22808,22)`, cycles `(68424,16)`.
- `square_strict_catalogue.npz` has analogous path-cycle arrays and `F=22801`. Neither catalogue, by itself, identifies the specific three-step prism insertion support, temporal faces, gauge-fixed independent edge set, or oriented cell complex boundary operator.
- The `stage26` archives and sweep arrays concern spectral simulations; they do not establish that the R3 prism insertion has a free edge or a bounded admissible collar.

## Normalization
Let the normalized Wilson plaquette factor be `w_lambda(H)=exp(lambda(c(H)-1))`, with `c(H)=Tr(H)/2`, so `0<w<=1`. Let `Z_cavity=integral exp(S_cavity) dHaar` and `Z_inserted=integral exp(S_cavity) product_{p in Q}w_lambda(H_p) dHaar`. The ratio equals the cavity Gibbs expectation of the product of normalized insertions. Different unnormalized Wilson conventions change ratios by explicit `exp(lambda |Q|)` factors.

## Theorem 1 (exact conditional Haar-leaf comparison)
Suppose a finite oriented SU(2) lattice complex has a set `Q={p_1,...,p_m}` of inserted plaquettes with distinct edge variables `e_1,...,e_m`, each `e_i` occurs in the holonomy of `p_i` exactly once and in no other inserted plaquette, and **none** of these edge variables occurs in `S_cavity` (or in any other reference-density factor). Integrate these edge variables with independent normalized Haar measure, without fixed conditions on them. Then **for every other environment and arbitrary cavity Gibbs measure**,

`Z_inserted/Z_cavity = a(lambda)^m`, where

`a(lambda)=int_SU(2) exp(lambda(c(U)-1))dU=exp(-lambda)*2 I_1(lambda)/lambda`.

Proof: fix all other variables. Each inserted holonomy equals `A_i U_{e_i}^{eps_i} B_i` with fixed `A_i,B_i`. Bi-invariance and inversion invariance of Haar give `int w_lambda(A_i U^{eps_i}B_i)dU=a(lambda)`. Since each `e_i` is absent from the reference density and from all other insertion factors, integrate sequentially and apply Fubini. There is no Jacobian, multiplicity, boundary-condition dependence, or spatial-volume dependence. QED.

For lambda>=1, positivity and continuity of `a(lambda)(1+lambda)^{3/2}` on `[1,infinity)` together with `a(lambda)~sqrt(2/pi)lambda^{-3/2}` give `a(lambda)>=c(1+lambda)^{-3/2}` for a universal c>0. Hence the desired support-local logarithmic-cost bound on this explicitly defined class. This is conditional on the special free-edge geometry and may not apply to R3!

## Theorem 2 (single annealed boundary holonomy)
Let `U` have **any** cavity Gibbs law, and let `V` be an independent Haar SU(2) boundary holonomy. Then `E[w_lambda(VU) | U]=a(lambda)`. Therefore `E[w_lambda(VU)]=a(lambda)` regardless of how strongly U is favored in the cavity. In contrast, fixed `V=-I` with U distributed according to density proportional to `exp(lambda c(U))` gives `E[exp(lambda(c(VU)-1))]=exp(-lambda)*lambda/(2 I1(lambda))`, exponentially small in lambda (and differs from the previous audit's unnormalized insertion ratio by `exp(-lambda)`). Thus genuine annealing removes this toy obstruction **only when the relevant holonomy is independently Haar distributed**, not merely because one integrates a correlated Gibbs boundary.

## Failure of automatic extension
For shared inserted edges, an edge participates in several insertion factors and the sequential Haar factorization fails. For a boundary holonomy V with non-Haar Gibbs law, the average is no longer `a(lambda)` in general. A bounded collar of edges alone does not imply a polynomial lower bound: boundary frustration may remain. An arbitrary boundary-conditioned comparison is not proved here.

## Necessary geometry/admissibility tests
1. Export the **actual R3 three-step prism**: oriented edges, vertices, spatial and temporal face boundary words, prism adjacency and orientation, boundary-condition convention, and the exact list Q of inserted Wilson factors.
2. Build the oriented edge-face incidence matrix. For each p in Q, search a distinct edge variable that belongs to p, to no other inserted p, and to no cavity factor. Check whether gauge fixing or exterior constraints remove its independent Haar integration. A matching is not enough if those edges appear in the cavity action.
3. If the strict leaf condition fails, enumerate a radius-r collar and test whether enough independent interior edge freedoms can be exposed by a gauge-covariant map while controlling all existing face factors. Check for cycles/frustrated constraints.
4. If no valid repair exists, form the actual cavity marginal law on the boundary holonomies and derive an averaged conditional small-ball estimate; an assertion of Gibbs averaging alone is insufficient.
5. Only after this derive the multi-slab transfer estimate; no continuum spectral-gap conclusion follows from the theorems above.

## Numeric certificate
Run `python verify.py` to check the analytic SU(2) Haar factor against direct Weyl quadrature. These tests verify the scalar identity, **not the geometric hypotheses**.
