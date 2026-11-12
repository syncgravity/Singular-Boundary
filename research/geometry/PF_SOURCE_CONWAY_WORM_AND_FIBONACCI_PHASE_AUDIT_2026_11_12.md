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
