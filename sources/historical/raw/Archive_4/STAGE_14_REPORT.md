# Stage 14 — Cost-adjusted temporal-transporter benchmark

## Scope and evidence

Reproducible paired pilot on the **5×5 square torus, Nt=15, beta_ref=3.5**, with a **10-slice rectangular Wilson loop**. The test uses four nominally independent chains (seeds 101, 211, 307, 419), 240 initial sweeps per chain, and 12 configurations per chain spaced by 12 sweeps. These short chains **are not certified equilibrated**. The direct Wilson estimator and conditional estimator are evaluated on the exact same outer configurations; 48 paired backgrounds total. Conditional inner warm-up is 32 sweeps, spacing 2 sweeps, and depths 8 and 32; fixed temporal boundary links are retained. The Stage 13 identity and random-field exact transporter contractions are independently tested. **This experiment is not conducted on the large M55 production ensemble** and cannot establish a physical scale.

## Paired numerical results

| Indicator | Direct | Conditional depth 8 | Conditional depth 32 |
|---|---:|---:|---:|
| Outer configurations | 48 | 48 | 48 |
| Mean normalized Wilson rectangle | 0.083254 | -0.025074 | 0.005781 |
| Across-outer raw standard deviation | 0.506781 | 0.148179 | 0.041793 |
| SD reduction relative to direct | 1× | 3.42× | 12.13× |
| Additional measurement time per outer (seconds) | 0.000254 | 0.0934 | 0.1313 |
| Nominal variance×time efficiency ratio vs direct, excluding shared outer-update cost | 1× | 0.0318× | 0.284× |

The large naive reduction in raw variance does **not** translate into an advantage on a variance×CPU-time basis when the direct estimator is measured on already-available configurations. This timing ratio is exploratory: direct and conditional share the cost of generating their outer configurations, Numba warm compilation is excluded from most recorded times, and a proper independent-outer-replication analysis needs much longer chains.

The paired mean differences are -0.1083 and -0.0775 for depths 8 and 32; corresponding **naive** paired standard errors (treating 48 outer configurations as independent) are 0.0797 and 0.0731. These are not independent-chain-valid uncertainties. Chain-wise direct means (101/211/307/419) are 0.1251, -0.0400, 0.0409, 0.2070, indicating the ensemble is too small for a precise benchmark. Sample depth 32 is insufficient to certify conditional-inner convergence. An attempted depth-128 full replication did not complete within the execution budget; it is excluded entirely.

## Critical scientific controls before promotion

- Prove stationarity and perform inner-separation and warm-up checks at several depths (e.g. 32/128/512) on genuinely decorrelated outer backgrounds.
- Check paired **outer-chain** block-bootstrap agreement of direct and conditional estimates and compare *total* CPU cost per accepted uncertainty, including inner and outer simulation work.
- Validate gauge covariance with arbitrary local gauge transformations of the complete tensor estimator and allow nontrivial path orientations and separations.
- Compare several spatial distances (including physically matched orientation families) and temporal lengths within Nt=20 without wrapping into the same terminal spatial slice.
- Validate conditional-slab factorization and all required fixed boundary links, and show stable positive Wilson signals and correlated effective-potential plateaus.
- Extend only after success on a representative larger square torus, and then test M55 geometry without claiming canonical Penrose admission.
- Require renormalized anisotropy, finite-volume, multiple beta and long-string corrections to infer sigma. Glueball mass and continuum ratio remain separate unresolved steps.

## Scientific decision

**Operator reconstruction passes. Raw estimator fluctuations decrease with inner depth. Cost-adjusted statistical efficiency and physical-scale extraction are not established. Do not deploy expensive large-volume multilevel production from this pilot alone.**

## Reproduction

From the directory containing `ym_stage13` and `ym_stage14`:

```bash
cd ym_stage14
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python stage14_benchmark.py
OPENBLAS_NUM_THREADS=1 python -m unittest -q test_stage14
```

Full original 48-row paired observations, timing measurements, and the exploratory summary are saved in `BENCHMARK.json`.
