# The Singular Boundary — Stage 4: gauge-covariant smearing and winding-flux spectroscopy

**Executed:** 11 October 2026. **Status:** Reproducible measurement-extension checkpoint, **not** a continuum Yang–Mills spectrum measurement. The 2+1D gauge configurations are exactly the 400 pre-existing Stage 3 gauge configurations; no further MCMC sweeps were run.

## 1. Scientific basis and change from Stage 3

The earlier corrected-geometry Stage 3 pilot saved 50 configurations from each of four chains, for each of the 188-vertex rational model-set M=5 torus and the 182-vertex square torus. Both have eight periodic Euclidean-time steps, approximately matched physical area, and reference bare coupling 3.5. Stage 3 diagnostics **failed** the predetermined MCMC R-hat and ESS gate, and the M=5 control **failed** the geometric local-motif admission gate. Neither physical anisotropy nor string tension was nonperturbatively matched. These deficits persist; measurement-only processing cannot eliminate them.

This checkpoint adds (i) explicitly gauge-covariant *spatial* APE smearing and SU(2) projection, (ii) a nine-operator temporal scalar correlator basis, (iii) winding-number-certified torus spatial-flux lines in both primitive-period directions, (iv) longer-available temporal Wilson rectangles (`t/a_t` = 1,2,3,4) grouped by **physical endpoint distance**, and (v) chain-stratified five-configuration-block bootstrap errors. It does not fit masses/tensions to noise.

## 2. Reproducible algorithms

### SU(2) APE projection

For each directed spatial edge `e: u → v`, every adjacent oriented quadrilateral face supplies the three-edge alternative parallel transporter `S_{e,f}: u → v`. One synchronous spatial smearing sweep is

\[
 U'_e(t)=\operatorname{Proj}_{SU(2)}\left[(1-\alpha)U_e(t)+
 \alpha\frac{\sum_{f\supset e}A_f^{-1}S_{e,f}(t)}{\sum_{f\supset e}A_f^{-1}}\right],\quad \alpha=0.4.
\]

For SU(2) represented by unit quaternions, projection is exactly normalization of the resulting quaternion. This is gauge-covariant because all terms transform as `g_u U g_v^{-1}`. **Temporal links are unchanged**, preserving the static-source transfer-matrix operator interpretation. The levels used are 0, 2, 6 synchronous spatial sweeps. The inverse-area staple weighting is an explicit operator choice, **not** an independently established physical renormalization or unique improvement prescription.

### Scalar basis and flux

Each geometry uses 3 loop-shape channels times 3 smearing levels, providing 9 gauge-invariant scalar candidate observables per time slice.

- Square reference: translational/90° rotation averages of all elementary 1×1 plaquettes, both orientations of adjacent 1×2 rectangles, and 2×2 rectangles. The previous checkerboard split is no longer used.
- Rational model-set M5 torus: sums of thin rhombi, thick rhombi, and adjacent two-rhombus boundaries. These are gauge-invariant scalar candidates. On an irregular torus, a formal continuum J^PC assignment still requires symmetry/continuum analysis.

The connected `9×9` matrix is evaluated with vacuum subtraction inside each resample and symmetrization. A GEVP is *only* attempted if the `C(t0=1)` matrix is sufficiently positive as an estimated metric; no GEVP mass is extracted from this dataset.

For the torelon channel, the code computes each directed spatial edge's **integer deck transformation** by comparing its physical projected basis displacement with the stored torus endpoint coordinates. Breadth-first search in the finite lifted graph constructs closed vertex cycles with winding `(1,0)` or `(0,1)`. Their physical displacements exactly equal the corresponding period vectors. Winding-loop traces averaged over eight anchors provide time series, and connected two-point functions are evaluated through half the temporal extent. The winding loops transform with a sign under the appropriate global Z2 center twist, while elementary plaquettes do not. Torelon energies could eventually give a closed-string scale after controlled large-length and temporal limits, but **are not estimated here**.

### Validation

The complete Stage 3 suite was rerun: **29/29 tests passed**. Ten additional Stage 4 checks passed, including spatial APE gauge covariance after two iterations, gauge invariance of enlarged scalar loops and smeared temporal Wilson rectangles, center-twist parity of winding loops, closed cycle displacement on both tori, exact SU(2) projection, preservation of all temporal links, and fail-closed GEVP diagnostics. **Combined: 39 passing tests.**

## 3. Numerical remeasurement (200 saved configurations per geometry)

| Diagnostic | Square torus (13×14) | Rational M5 model-set torus |
|---|---:|---:|
| Saved gauge configurations remeasured | 200 | 200 |
| Scalar operators per time slice | 9 | 9 |
| Noncontractible flux operator channels | 2 × 3 smearing levels | 2 × 3 smearing levels |
| Primitive winding lengths | 7.5698, 8.1520 | 7.4833, 8.2462 |
| Smallest eigenvalue of scalar `C(1)` | −2.37×10⁻⁶ | −2.15×10⁻⁶ |
| Smallest eigenvalue of scalar `C(2)` | −1.20×10⁻⁴ | −8.73×10⁻⁵ |
| Fraction of 160 bootstraps with positive-definite scalar `C(2)` | 0% | 0% |
| Largest positive scalar-diagonal signal/SE at `t=2`, across 9 channels | 0.014 | 0.597 |
| Largest positive winding-diagonal signal/SE at `t=2`, across 6 channels | 0.309 | 1.872 |

A negative eigenvalue of an estimated noisy Euclidean correlator does **not** mean the underlying transfer matrix has a negative-norm state. It means this finite-sample GEVP cannot be trusted. Search across 9 channels also incurs multiple-comparison concerns; none reaches a useful, robust multi-time mass plateau.

### Physically binned temporal Wilson rectangles

The last common physical-distance bin is `1.5 ≤ r < 2.0` (mean square r=1.747, M5 r=1.718), and the temporal separation is **t=4 lattice steps**, the largest distinct separation on the saved 8-slice periodic time circle:

| Model | Spatial smearing | `W(r,t=4)` ± chain-block bootstrap SE | Nominal signal/SE |
|---|---|---:|---:|
| Square torus | Unsmoothed | 0.03194 ± 0.00542 | 5.89 |
| Square torus | APE 2 sweeps | 0.04527 ± 0.00508 | 8.91 |
| Square torus | APE 6 sweeps | 0.04144 ± 0.00552 | 7.51 |
| Rational M5 torus | Unsmoothed | 0.01121 ± 0.00677 | 1.65 |
| Rational M5 torus | APE 2 sweeps | 0.01269 ± 0.00648 | 1.96 |
| Rational M5 torus | APE 6 sweeps | 0.00911 ± 0.00567 | 1.61 |

Thus smearing **demonstrably improves the nominal long-distance short-time Wilson-loop signal on the square reference** in this bin (the two-sweep basis is best of the three tested). The signal improvement is *not* reproduced decisively on the small rational M5 control. The bootstrap is exploratory because the underlying Stage 3 chains failed their convergence gates; raw signal/SE is not evidence of a plateau. Physical radial binning also mixes paths with different orientations and shapes, requiring additional controls.

## 4. Admission decisions and next production design

**Admitted as software results:** gauge-covariant SU(2) APE smearing, area-weighted spatial staples, larger scalar loop bases, explicit winding paths on both periodic meshes, physical-distance binning, remeasurement of all 400 Stage 3 saved configurations, and chain-aware exploratory uncertainty propagation.

**Not admitted as physics results:** scalar `m_{0++}`, torelon energy, string tension `sigma`, nonperturbative anisotropy matching, continuum ratio `m_{0++}/sqrt(sigma)`, or an M5-vs-square quasicrystal effect. The earlier failed R-hat and ESS criteria remain; no new independent configurations were generated. The rational M5 torus remains inadmissible as a Penrose-specific causal reference.

**Next production step:** (1) use a larger temporal extent (e.g., at least 16–24 sites at the chosen bare scale), with demonstrably adequate physical Euclidean time separation; (2) increase independent thermalized chain lengths until observable-level ESS/MCSE gates pass; (3) use larger separation/orientation pools, more winding-loop anchors and, if needed, multilevel variance reduction; (4) prespecify covariance/GEVP plateau tests and winding-energy fit windows; (5) tune the physical anisotropy and extract `sigma` before claiming a common scale; (6) only after controls are admitted, move from M5 to independently validated locally convergent Penrose approximants and at least four continuum spacings. Finite-volume and approximation-scale limits must also be assessed.

## 5. Reproduction and provenance

`stage4_remeasure.py` consumes the Stage 3 `*_configs.npz` files **without modifying them**. Each Stage 4 JSON report contains the source configuration SHA-256 and spatial graph hash. Source code and output arrays are bundled with this checkpoint; the 53 MB Stage 3 original archive is retained separately rather than duplicated.

Run from this directory with single-threaded BLAS:

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python -m unittest discover -q
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python stage4_remeasure.py \
  --stage3 ../ym_stage3/outputs --out outputs --per-chain 50 --block 5 --bootstrap 160
```

`outputs/*_stage4_measurements.npz` contains the complete new nine-operator and winding time series, temporal rectangles at all three smearing levels, and connected C matrices. `outputs/*_stage4.json` contains operator labels, source fingerprints, winding paths, physical-distance bins, bootstrap uncertainties and rejection gates. `outputs/physical_bins_t4_summary.csv` enables direct comparisons across smear levels.
