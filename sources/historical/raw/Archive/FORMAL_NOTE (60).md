# Penrose rhombus-prism buffers: incidence evidence, obstruction, multiscale reduction

Date: 2026-10-27. This note distinguishes rigorous finite-complex lemmas from unverified claims about the project's full 3D Penrose spacetime incidence.

## Data inspection

- `penrose_complete_catalogue.npz`: arrays `idx` and `sign` each shape (22808,22), `length` (22808,), `cidx` and `csign` each shape (68424,16), `clength` (68424,), and planar cycle metadata. There is no explicit 3D cell-to-face incidence / 3D boundary map (`d_2`) or enumeration of rhombus-prism faces sufficient to certify every buffer.
- `penrose_seed101_stage26.zip` has `latest.json` and Wilson-chain observation NPZs, e.g. `direct_timeslice` shape (20,4), `conditional` shape (2,9,4,4); not a 3D cellular boundary operator.
- The dissertation archive consists of PDFs, not a directly machine-verifiable 3D incidence table. Its content is not used as a claimed 3D certification here.

## 1. Boundary-holonomy obstruction (fully nonlinear)

Let B be a finite simply connected oriented cellular surface composed of n plaquettes of a 3D rhombus-prism complex. Freeze link variables on its boundary ∂B so that the ordered boundary holonomy is h with SU(2) geodesic angle θ(h) in [0,π]. Let all n plaquette couplings β_p≥c_- λ. Allow all other link variables in B to vary. Nonabelian surface product with parallel transports implies

θ(h) ≤ Σ_{p∈B} θ(W_p).

Since d(W_p)=1−cos θ(W_p)≥(2/π²) θ(W_p)², Cauchy–Schwarz yields

Σ_{p∈B}β_p d(W_p) ≥ (2c_- λ/(π² n)) θ(h)².

For h=−I, minimum ≥ 2c_- λ/n. This is a lower bound for *every* interior link assignment and therefore for the compatible minimum of any local action containing those n face energies. If a fixed-width buffer has bounded n independent of λ, its minimum may be Ω(λ) for suitable fixed exterior data. Hence a uniform-over-exteriors bound M_L(w)≤C|Q|log λ cannot follow from fixed thickness or bounded incidence alone.

The surface must genuinely form a disk with frozen outer boundary in the tested local action; the statement does not assert that every buffer contains such a surface with a nontrivial boundary h. It is a counterexample to *universal* flat completion for every exterior configuration, not a proof of bad Gibbs-average behavior.

## 2. Conditional min-energy estimate (correct scope)

For n adjustable SU(2) link variables and local Wilson action S_L(u;w) with all incident plaquettes included, bounded face degree and couplings ≤c_+λ, let M_L(w)=min_u S_L(u;w). A product-geodesic ball about any minimizer yields

Z_L(w) ≥ e^{−M_L(w)−Cn}(c λ^(−3/2))^n.

Indeed the first variation at a minimizer is zero, Wilson action Hessian bounded by Cλ in link coordinates, and a ball of radius λ^(−1/2) changes action by ≤Cn. For E_A(w,u) ≤S_L(u;w),

P(E_A≥M_L(w)+(3n/2)log λ+Cn+s | w) ≤e^(−s).

This remains *relative to M_L(w)*. Integrating out w cannot replace M_L with a constant without a new probabilistic estimate.

## 3. A noncircular alternative: boundary-holonomy multiscale test

Choose nested shells B_0⊂B_1⊂⋯⊂B_R around Q, with all boundary links of each shell specified. For each shell use independent geometric data:
- n_j = count of plaquettes in an actual spanning surface for exterior cycles;
- ℓ_j = boundary loop length;
- θ_j = SU(2) geodesic angle of its ordered boundary holonomy;
- E_j = compatible minimum of its entire buffered Wilson action.

A necessary condition for E_j≤C|Q|log λ for all exterior data is n_j≥cλ/(|Q|log λ) when θ_j≈π, by Lemma 1. Thus a buffer with O(|Q|) plaquettes cannot guarantee uniform flatness for all frozen exteriors as λ→∞.

A probabilistic multiscale route would establish a uniform conditional bound for each shell of the form

P( λ θ_j²/n_j > A_j+s | geometry/outer data averaged under the true Gibbs marginal ) ≤ C_j exp(−c s)

or an estimate for the change of compatible minima upon opening a shell, with Σ_j A_j≤C|Q|log λ. These are NOT proved by the preceding local ball bound; a new true-Gibbs mixing/coupling comparison is required. The condition is an explicit independent target and is not claimed for arbitrary supports.

## 4. Exact Gibbs diagnostic on a one-holonomy toy

For one Wilson-distributed holonomy h with density e^(−λ d(h))/q(λ) relative to Haar,

P(θ(h)≥δ) ≤ q(λ)^(−1)e^(−λ(1−cos δ)) ≤ C λ^(3/2)e^(−λ(1−cos δ)).

If the plaquette constraint is deleted and h is Haar, P(θ(h)≥δ)=1−[δ−sin(2δ)/2]/π, which stays positive for fixed δ in (0,π). This proves the suppression is a *dynamical* property of which plaquettes remain, not a consequence of the prism cell incidence alone.

## Conclusion

No validated actual 3D Penrose face/cell incidence list appears in the inspected files. The geometry of a rhombus prism supports local one-missing-face Bianchi fillings, but neither certifies uniformly low-minimum fixed-size buffers for arbitrary deleted supports nor avoids the boundary-holonomy obstruction. A multiscale Gibbs estimate is needed; the arbitrary-support Wilson insertion and continuum R3/R2 mass gap remain open.
