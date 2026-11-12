# Source Conway-worm extraction, Fibonacci phase and 3D observer audit

**2026-11-12 · source replay against the authenticated predecessor archive**

## Executive disposition

The finite 34:55 parastichy count remains **established for the radial golden-angle/Delaunay construction**. It is not a count of the five original Conway-worm families, nor an exact-return count in a five-basis-step Z5 walk.

The authenticated predecessor source provides a useful bridge: its Fibonacci substitution matrix has stable-to-unstable eigenvalue magnitude ratio exactly φ⁻², the golden-angle fraction. Applying that scalar as a turn fraction in the J-plane gives a natural observer phase rule. But the source script does not itself make that scalar-to-angle identification, and the original worm extractor does not reproduce the claimed Fibonacci ratios without an additional physical-interior crop.

## 1. Authenticated source and executable behavior

The replay used the user-supplied Archive(1).zip (SHA-256 bdc3792b2f2be40736c20c4574ef72a6f1eded226fe28415a5f1c33392af2f9b) and its paper2_compute.py member (SHA-256 a8e73bb783471bed28dc062856c69101a26945ad516a8c9c06af755adcea5510).

Only the source PenroseTiling class, constants, extract_conway_worms, analyze_worm_fibonacci, and verify_substitution_invariant were AST-compiled. The pipeline entry point, plotting, output writes and unrelated spectral calculations were not executed.

The source worm extractor groups tiles by (family, grid index), orders tile centroids along the corresponding line direction, and encodes thick/thin as L/S. Its analyzer tests only whether the ratio L/S is within 15% of φ for sequences of at least ten tiles. It does not calculate 34/55 arm counts or an observer phase.

There is also a code/text cutoff mismatch: run_full_pipeline uses grid sizes [7,10,12,15,18] and selects tilings[15], while the paper text describes its largest worm sample as N_grid=25.

## 2. Replaying the original extractor

| Generator cutoff | Worms | Per family | Tiles per worm | Mean L/S | Source Fibonacci matches |
|---:|---:|---:|---:|---:|---:|
| N_grid=15, selected by pipeline | 155 | 31 | 124 for every worm | 1.000 | 0 |
| N_grid=25, manually replayed from same source class | 255 | 51 | 204 for every worm | 1.000 | 0 |

This is a reproducible failure of the un-cropped extractor to reproduce the paper's stated interior-worm ratio. The cause is visible in the implementation: every tile in the finite pentagrid crop is included, even though the five grid families have different physical extents along a fixed line. The function does not restrict each worm to a common physical interior region.

## 3. A common physical-interior crop

A corrected audit convention, not a silent edit to the original source, restricts tile centroids to the same disk ||c_t||≤20 and then applies the original family/line grouping and projection ordering.

For N_grid=25, this disk contains 1,554 tile signatures. The accepted tile set is exactly unchanged when the generator cutoff is increased from 21 to 25, so this is a stable finite interior crop.

| Diagnostic | Result |
|---|---:|
| Worm segments | 82 |
| Segments by family | 16, 16, 16, 17, 17 |
| Segments with at least 10 tiles | 75 |
| Long-segment mean L/S | 1.625489 |
| Long segments within 15% of φ | 70 / 75 (93.33%) |
| Consecutive tile pairs | 3,026 |
| Consecutive pairs sharing exactly one tile edge | 3,026 / 3,026 |
| SS bigram fraction among long segments | 7.09% |
| Maximum thick L-run / thin S-run | 4 / 2 |
| Strict proxy (no SS, L-run ≤3, S-run ≤2) | 23 / 75 |

The physical crop recovers the expected near-φ frequency ratio and yields genuine edge-connected tile chains. It does not yet certify every longest sequence as an exact Fibonacci substitution word: the strict proxy passes only for 23 of 75 long segments. This separates the frequency-ratio claim from the stronger word-structure claim.

## 4. The source Fibonacci matrix gives the golden-angle fraction

The same source function defines
\[
M_1=\begin{pmatrix}1&1\\1&0\end{pmatrix},\qquad M_2=M_1^2.
\]
Its eigenvalues are λ₊=φ and λ₋=−φ⁻¹. Therefore
\[
\rho=\left|\frac{\lambda_-}{\lambda_+}\right|=\varphi^{-2}=0.38196601125\ldots
\]
exactly.

This supplies a source-motivated scalar from the Fibonacci substitution. A natural observer phase-lift rule is
\[
\boxed{\Delta\theta=2\pi\rho=2\pi\varphi^{-2}.}
\]
The additional postulate is interpreting the stable/unstable contraction magnitude as a fraction of a full turn in the J-oriented plane. The predecessor script gives the ratio, not this angular interpretation.

Once that phase rule is adopted, the already-verified golden-angle construction x_n=√n exp(2π i nρ) yields the exact finite 34, 55 and 89 residue-chain counts in the documented annuli. The 34 and 55 residual turns have opposite signs.

## 5. A natural internal-phase identification fails

I tested whether the phase rule is already present as the argument of the source internal projection of each worm tile centre. For a tile with four source integer labels m^(a), define
\[
\bar m_t=\frac14\sum_{a=1}^4m^{(a)},\qquad z_{2,t}=\sum_{j=0}^4\bar m_{t,j}\omega^{2j}.
\]
Along the 75 long, physically cropped worm sequences there are 2,977 unwrapped arg(z₂) increments. Their mean absolute circular error from 2πφ⁻² is 98.26 degrees; only 3.46% lie within 10 degrees and 7.89% within 20 degrees. The opposite orientation performs no better.

Thus the simplest proposed identification θ=arg(z₂) is not the golden-angle phase. This does not rule out the historical Stage-30 observer frame, whose phase parameter is an independent observer variable; it rules out identifying that phase naively with the tile-centre internal argument.

## 6. Five-family frame and explicit 3D observer lift

Let
\[
\rho=\varphi^{-2},\qquad \theta_n=2\pi\rho n,
\]
and define the five family weights
\[
w_j(n)=\sqrt n\cos\left(\frac{4\pi j}{5}-\theta_n\right),
\qquad j=0,\ldots,4.
\]
These weights are not an arbitrary five-vector: they lie exactly in the source's second-harmonic C5 representation. With \(\omega=e^{2\pi i/5}\), direct finite Fourier summation gives
\[
s(w(n))=\frac1{\sqrt5}\sum_jw_j(n)=0,\qquad
z_1(w(n))=\sum_jw_j(n)\omega^j=0,
\]
\[
\boxed{z_2(w(n))=\sum_jw_j(n)\omega^{2j}
=\frac52\sqrt n\,e^{i\theta_n}.}
\]
For the orthonormal Fourier coordinate \(Z_2=\sqrt{2/5}\,z_2\),
\[
Z_2(n)=\sqrt{\frac52}\sqrt n\,e^{i\theta_n}.
\]
A cyclic relabeling of the five families is exactly the phase shift \(\theta\mapsto\theta+4\pi/5\); the family frame is C5-equivariant.

This gives a direct observer-space lift without trying to map the internal plane linearly into the source physical \(z_1\) plane. Define the observer space
\[
\mathcal O=\mathbb R_s\oplus\mathbb C_{Z_2}
\]
with product Euclidean metric \(d\ell^2=ds^2+dX^2+dY^2\), independent longitudinal coordinate \(s_n=hn\), and clock \(t_n=nT\), where \(h,T>0\) are declared model scales. Then
\[
\boxed{\Gamma_n=(hn,\Re Z_2(n),\Im Z_2(n)).}
\]
This is a genuine discrete, radially expanding 3D observer curve in the declared observer space. It is not a literal embedding of the worms and does not identify \(Z_2\) with source physical \(Z_1\); the earlier no-equivariant-linear-map result is therefore not contradicted.

The radial law is \(r_n\propto\sqrt n\), so the transverse area per observer tick is constant. This is a new equal-area sampling rule; Paper 3's constant-radius circle does not contain it. The phase fraction is motivated by the source substitution contraction, while interpreting it as a full-turn fraction, choosing the radial law, and specifying \(h,T\) are explicit observer postulates.

The 34 and 55 Delaunay parastichy families are neighbour-chain families in the transverse \(Z_2\) projection. Their 3D lifts have longitudinal advances \(34h\) and \(55h\), clock advances \(34T\) and \(55T\), and opposite angular residuals:
\[
2\pi(34\rho-F_7)=-2\pi\varphi^{-9},\qquad
2\pi(55\rho-F_8)=+2\pi\varphi^{-10}.
\]
They are not exact returns of a five-basis-step Z5 walk.

The direct tile-centre test above shows that the observer phase \(\theta_n\) is not simply \(\arg z_2\) of individual worm tile centres. It is a family-level observer phase. A source-native rule connecting each observer tick to actual worm encounters remains the next open derivation.

## 7. Resolution path

The count itself is not the remaining obstacle. The next objective is to make the observer index and phase source-native:

1. Preserve the five source worm families using the common physical crop and keep frequency-ratio evidence separate from exact substitution-word evidence.
2. Use the explicit C5 family frame w_j(n)=√n cos(4πj/5−2πρn), whose Fourier projection is pure Z₂, as the candidate observer state. Keep the conversion of ρ into a turn fraction identified as an observer postulate.
3. Recover or define the source-native rule that advances the observer tick n along or between actual worm encounters; do not insert the integer n by hand. The historical Stage-30 implementation remains to be authenticated.
4. Verify that the source-defined traversal induces the same 34/55 Delaunay parastichy graph under held-out cutoffs and mirrored/rational controls.

**Status:** finite 34:55 count — ESTABLISHED for the golden-angle construction; source Fibonacci contraction ratio — ESTABLISHED; common-crop worm frequency ratio — REPRODUCED; exact source Fibonacci words — PARTIAL; internal arg(z₂) as observer phase — REJECTED by this test; observer phase-to-worm traversal and source-native 3D metric/clock — OPEN.


**Family-frame verifier:** `research/scripts/verify_pf_family_frame_lift_2026_11_12.py` passes 12 deterministic algebraic and geometric checks. Its machine-readable output is preserved in `research/evidence/PF_FAMILY_FRAME_3D_LIFT_2026_11_12.json`. The 74-check Delaunay verifier separately establishes the finite 34:55 chain counts.


## 8. Gauge-invariant family observer operator and the Stage 26 data gate

The family frame can be coupled to actual gauge-invariant observables without treating the observer clock as Yang–Mills transfer time. For each family j, let A_j be a source-defined set of anchors and γ_{j,x} a closed spatial Wilson loop at anchor x. Define the family defect
\[
D_{\gamma_{j,x}}(U)=1-\frac12\operatorname{Tr}\operatorname{Hol}_{\gamma_{j,x}}(U)\in[0,2],
\qquad
F_j(\tau)=\frac1{|A_j|}\sum_{x\in A_j}D_{\gamma_{j,x}}(U(\tau)).
\]
Use the unit-normalized signed family weights
\[
u_j(n)=\sqrt{\frac25}\cos\left(\frac{4\pi j}{5}-2\pi\rho n\right),
\qquad \sum_j u_j(n)^2=1,\quad \sum_j u_j(n)=0.
\]
Then the observer-conditioned operator is
\[
\boxed{O_n(\tau)=\sum_{j=0}^4u_j(n)F_j(\tau),}
\]
with a separate full-family control
\[
O_{\rm full}(\tau)=\frac15\sum_{j=0}^4F_j(\tau).
\]
Because each F_j is an average of closed Wilson-loop traces, O_n is real and gauge invariant. The signed coefficients are a specified real second-harmonic family projection, not positive spatial weights. Since 0≤F_j≤2 and ||u(n)||₂=1, Cauchy–Schwarz gives |O_n|≤2√5. Cyclic relabeling of the five families together with θ→θ+4π/5 leaves the contraction invariant.

For spectroscopy, fix n at source and sink and vary the physical Euclidean transfer separation τ:
\[
C_n(\tau)=\langle O_n(\tau)O_n(0)\rangle_c.
\]
The observer phase label n and observer clock t_n=nT are not the Euclidean transfer time τ. Sweeping n together with τ would define a nonstationary, phase-conditioned correlator and must be analyzed as such; it must not be silently fit as an ordinary stationary spectral correlator.

### Uploaded Stage 26 data inventory and reconstructed incidence

The four Penrose multihit NPZs contain direct/multihit arrays of shape (4,600), lags, matched-pair and candidate-path indices, r, dx, source/target indices, and seed/geometry/checkpoint metadata. They do not contain the ordered path geometry or family labels needed to interpret candidate path IDs as worm-family Wilson loops.

The Stage 26 full ZIP contains aggregate outer snapshots and a restart archive with links of shape (1,368,480,4) and normalized plaquette_trace of shape (1,368,480). The restart alone does not include the incidence map. A separate user-supplied STAGE26_M55_GEOMETRY_RECONSTRUCTION_2026-10-31.zip provides the archived M55 reconstruction source, spatial face incidence, and full spacetime fi/sg incidence arrays. Its reconstructed graph hash matches the archived Stage7 graph hash; its source-array hash is fee7afad5b4b464537782b508402401502984947ac5caf5163a87dad8ae33e2e. The complete measurement-catalogue NPZ byte match remains unverified.

Crucially, the reconstructed incidence is now validated against the actual restart links: multiplying the four oriented SU(2) link quaternions for **all 1,368,480 spacetime faces** reproduces the stored normalized plaquette_trace with maximum absolute error 5.56×10⁻¹⁶ and zero entries above 10⁻¹². The first 22,808 spatial faces per timeslice are in the source generator's face order. Their two basis-direction labels (a,b) provide exact five-family *plaquette* labels; each face belongs to two directional families.

### Actual Stage 26 family-plaquette diagnostic

For each family j, define the spatial plaquette defect at timeslice t by
\[
F_j^{\mathrm{plaq}}(t)=\operatorname{mean}_{f:\,j\in\{a_f,b_f\}}
\left(1-\frac12\operatorname{Tr}U_f(t)\right).
\]
This is a family-labelled, gauge-invariant closed-loop observable computed from the actual Stage 26 restart configuration, not a synthetic SU(2) test.

| Family j | Mean defect over 20 slices | Slice standard deviation | Number of faces |
|---:|---:|---:|---:|
| 0 | 0.32968420 | 0.00266265 | 9,072 |
| 1 | 0.33234256 | 0.00351840 | 9,152 |
| 2 | 0.33236883 | 0.00313631 | 9,120 |
| 3 | 0.33194860 | 0.00275874 | 9,120 |
| 4 | 0.33212504 | 0.00261038 | 9,152 |

The full-family control has mean 0.33169385 and slice standard deviation 0.00214334. The second-harmonic family amplitude
\[
A(t)=\sqrt{\frac25}\left|\sum_{j=0}^4F_j^{\mathrm{plaq}}(t)\omega^{2j}\right|
\]
has mean 0.00287180, maximum 0.00551889, and mean amplitude equal to 0.866% of the full-family control. Its phase circular spread over the 20 slices is 1.212 radians. Thus this one restart shows a small family-direction plaquette contrast, but not a stable phase-selection law.

For observer phases n=0,…,1000, the computed
\[
O_n^{\mathrm{plaq}}(t)=\sum_j u_j(n)F_j^{\mathrm{plaq}}(t)
\]
ranges from −0.00551889 to +0.00551888. Its dependence on n is exactly the single second-harmonic projection, with maximum algebraic identity error 5.3×10⁻¹⁴. This does **not** mean the 34:55 arm counts have been measured in the gauge field: those counts are the Delaunay parastichy structure of the observer trajectory, while this is a phase-conditioned family-plaquette diagnostic.

Scope is deliberately narrow: one restart configuration at sweep 12000 and its 20 periodic spatial slices. The slices are not an independent ensemble. This is not a transfer-matrix correlator, not a long-worm Wilson-loop measurement, and not a mass-gap estimate.

Reproduce this result with research/scripts/analyze_stage26_family_plaquettes_2026_11_12.py and inspect research/evidence/PF_STAGE26_FAMILY_PLAQUETTE_OPERATOR_2026_11_12.json.

### Reconstructed M55 worm strips and boundary Wilson loops

The M55 source generator gives every rhombus face its two basis-direction labels (a,b). For each family j, connect two faces when they share an edge of direction j. Every face in that family has two such edges, so the local dual graph has degree at most two. Cropping the periodic M55 cell by a disk of radius 40 (strictly inside its 42.9127 inradius) turns the components into finite worm segments. Retaining segments of at least 10 tiles gives:

| Family j | Segments | Mean tiles/segment | Mean L/S | Segments within 15% of φ |
|---:|---:|---:|---:|---:|
| 0 | 50 | 122.88 | 1.61825 | 50/50 |
| 1 | 50 | 123.78 | 1.61790 | 50/50 |
| 2 | 51 | 121.41 | 1.63720 | 51/51 |
| 3 | 51 | 121.14 | 1.63353 | 51/51 |
| 4 | 50 | 123.78 | 1.61237 | 50/50 |

This is a topological worm extraction from the M55 incidence, not the earlier line-index heuristic. For each segment, sum its oriented face boundaries. Shared interior edges cancel, leaving one simple closed boundary loop of length exactly \(2L+2\). The resulting reconstructed catalogue has 252 closed spatial Wilson loops, lengths 22–314. Its canonical SHA-256 is 5e080f13d5491f0aa37d1eb33591fada06e41d5e51fcdcdd4109cdee457d3857; the downloadable pretty-printed JSON file has SHA-256 1220d3ba0b2b69d0cbba7767133889adfc30d28e5752038bc63377ef1930cb66.

These loops have now been evaluated on the actual Stage 26 seed-101 restart at sweep 12000. The script applies the family phase weights to the mean defect of the worm-strip boundary loops in each family. It also applies independent random SU(2) gauge transformations at every vertex and timeslice: the maximum change in all spatial plaquette traces is \(1.44\times10^{-15}\), and the maximum change in any worm-loop defect is \(7.77\times10^{-15}\).

| Family j | Mean worm-boundary defect | Slice SD |
|---:|---:|---:|
| 0 | 0.98900353 | 0.07667630 |
| 1 | 0.99381754 | 0.07080612 |
| 2 | 0.99011248 | 0.04072105 |
| 3 | 1.01603838 | 0.07317351 |
| 4 | 0.98760378 | 0.06054185 |

The full-family control is 0.99531514 (slice SD 0.02790160). The mean second-harmonic amplitude is 0.08429661, or 8.469% of the full control. Its circular phase spread over the 20 slices is 2.074 radians. This is a measurable family contrast, but its phase is not stable across these slices. It does not establish a physical handedness or a selection law.

This is the first source-geometry-derived, gauge-invariant long-loop family observable in the current record. It is still one restart configuration and 20 periodic slices, not an ensemble correlator. It is not a mass-gap estimate. The 34:55 parastichy count remains the Delaunay arm count of the golden-angle observer trajectory; it is **not** the number of M55 worm segments, which are 50–51 per family in this crop.

Reproduce the extraction, loop construction, Stage 26 evaluation and gauge-covariance check with research/scripts/analyze_stage26_worm_boundary_loops_2026_11_12.py. Its path-catalogue output is generated with --catalogue-output; the summary evidence is research/evidence/PF_STAGE26_M55_WORM_BOUNDARY_LOOPS_2026_11_12.json.

### Remaining provenance and ensemble gap

A reconstructed path catalogue is now available and has been evaluated. The remaining catalogue question is historical identity: a Project file named penrose_complete_catalogue.npz (about 1.96 MB) appears in the Project index, but the current file-access route did not expose its raw bytes. Its contents and hash remain unverified. It may be the original measurement catalogue; compare it against the reconstructed M55 worm-boundary catalogue if its bytes can be made available. The multihit NPZ candidate_path_indices are still only indices, and their mapping to the reconstructed worm loops has not been established. The separate global_whitney_11face NPZ contains a 30×30 matrix, edge IDs and eigenvalues, not the full worm-loop catalogue.

The principal data limitation is now ensemble coverage. The Stage 26 full ZIP has one restart configuration at sweep 12000 and aggregate outer snapshots, not raw link configurations for every outer sample. The 20 timeslices of the restart are not an independent Monte Carlo ensemble. Therefore the measured family worm-loop operator is a single-configuration diagnostic, not a transfer-matrix correlator or a spectral estimate.

### Minimum data contract for the next run

1. If available, inspect and hash penrose_complete_catalogue.npz and compare its path ordering against the reconstructed M55 catalogue. If not, retain the reconstructed catalogue hash as the explicit path definition.
2. For multiple outer configurations, retain raw link configurations or per-loop holonomies/defects for every reconstructed worm-boundary loop, with family, segment ID, anchor, loop length and path-catalogue hash.
3. Store F_j(τ), O_n(τ) for predeclared observer phases, and O_full(τ) as a control; do not aggregate away family and loop identity before forming these operators.
4. Keep observer phase n, observer clock t_n, and Euclidean transfer separation τ as distinct fields. Fix n at source and sink for ordinary stationary spectroscopy.
5. Preserve the nested outer-chain and inner-multihit error structure, autocorrelation, effective sample size, matched-pair identity and cost diagnostics.

The separate synthetic SU(2) loop verifier (450 deterministic checks) validates the gauge covariance of the proposed family contraction. The Stage 26 plaquette script validates the actual restart link/face incidence and computes the first family-labelled plaquette diagnostic. Neither supplies the missing long-worm Wilson-loop correlator or a Yang–Mills mass-gap result.

