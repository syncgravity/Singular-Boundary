# Stage 20: scalar connected-correlator vacuum-subtraction benchmark

## Status and scope

This is a **completed, data-backed estimator benchmark**, not a working gauge-theory multilevel estimator. It uses the Stage 19 15,000-sweep archives (4 chains per geometry, 490 observations per chain; t=0..7). No new gauge updates were run. Four full spatial scalar channels (3, 5, 8 face unrestricted controls and complete matched auxiliary) are analyzed separately.

## Estimators

Let `m_c` be the observed timeslice-and-configuration mean scalar for independent chain `c`; let `P(t)` be the average within-configuration timeslice product at lag t. Compare:

* Ordinary plug-in: `C_plugin(t) = P(t) - (sum_c m_c / 4)^2`.
* Cross-chain disconnected subtraction: `C_cross(t) = P(t) - sum_{c != d}(m_c * m_d)/12`.

When four chains are mutually independent, drawn from the same stationary distribution, and have finite means, the cross-chain subtraction has unbiased expectation for `mu^2` **even with within-chain autocorrelation**. This does not fix nonequilibrium or unequal chain means. By construction `C_cross(t)-C_plugin(t)` is constant in t for a given channel.

Moving-block bootstrap uses joint per-configuration timeslice means and lagged products and independently resamples each chain. Block lengths 10,20,40,80 saved observations with 300 replicates each. Monte Carlo error in estimated SE ratios is nontrivial.

## Observations: block length 40

|Geometry|Channel|Cross-chain C(2)|SNR at t=2|Cross/plug-in SE ratio at t=2|
|---|---|---:|---:|---:|
|square|3_face_full|+8.965e-08|+1.53|0.9989|
|square|5_face_full|+8.097e-08|+1.14|0.9984|
|square|8_face_full|+1.774e-07|+2.96|1.0017|
|square|strict_complete_aux|+7.493e-08|+1.01|1.0007|
|penrose|3_face_full|-2.692e-08|-0.35|1.0002|
|penrose|5_face_full|-9.643e-08|-1.14|0.9994|
|penrose|8_face_full|+1.256e-08|+0.12|0.9989|
|penrose|strict_complete_aux|+3.462e-08|+0.32|0.9986|

Across all four block sizes, **neither estimator produces one channel with three consecutive t=2..6 correlators at SNR >= 2**. The correction is small: at t=2..6, the difference between estimators is at most 0.015 times the cross-chain bootstrap SE. Cross-to-plug-in SE ratios at t=2 are approximately 1.0. Thus improved vacuum subtraction removes a formally identifiable finite-sample bias but does not cure the scalar signal-to-noise failure.

## Consequence for next experiment

The bottleneck is variance in the connected correlator itself, rather than the small bias associated with estimating the vacuum mean from the same four chains. Stage 20's next physics-engineering task must implement a **genuinely conditional gauge-field estimator**, not simply redo vacuum subtraction. An appropriate exact testbed is a small periodic SU(2) lattice with temporal slab boundaries held fixed. On each independently sampled outer field, multiple conditional interior updates estimate each timeslice scalar expectation; two separated interiors provide the product of conditional means for a connected correlator, with independently estimated vacuum means. Test direct-vs-conditional ensemble consistency, gauge covariance of the boundary treatment, actual integrated autocorrelation and cost-adjusted SE at multiple inner-update counts. Do not combine conditional replicates as independent outer gauge configurations. A stable scalar mass cannot be inferred from this benchmark.

## Caveats

* Four final Stage 19 chains descended from Stage 9 seeds and need robust stationary/independence verification.
* The periodic-time correlator is based on per-configuration time translation averages.
* Bootstrap SE values should not be treated as certified without chain mixing and block-length convergence.
* This method is not the Wilson-line exact multihit estimator and does not prove multilevel feasibility.
* The reported SNR maximum is a multiple-comparison scan, not a discovery statistic.

## Reproduction

`python benchmark.py --root /mnt/data --out /mnt/data/stage20_scalar_variance --reps 300`

Run `python -m unittest -q test_benchmark` for three estimator checks.
