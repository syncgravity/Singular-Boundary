# R3-IR-405 — Stage-26 artifact admissibility audit for the physical cap-moment certificate

**Date:** 2026-10-30. **Classification:** source-data verification and a negative evidentiary result. No Wilson cap inequality is established.

## Inspected original artifacts

Locally inspected all eight archived Stage-26 seed datasets (Penrose and square, seeds 101, 211, 307, 419), together with all eight 10,000-sweep multihit arrays, using Python zipfile and numpy with allow_pickle=False. The short Stage-26 archives each contain exactly 100 outer checkpoint NPZ records; sampled checkpoint arrays have 15 keys. Each multihit NPZ has 13 keys and array shapes including `direct=(4,600)`, `multihit=(4,600)` and `lags=(4,)` in the inspected Penrose seed 101. The examined Stage-26 record (Penrose seed 101 at sweep 12000 in the full archive) contains `direct_timeslice`, `direct_product`, `conditional`, `conditional_onepoint`, `pair_counts`, `inner_seconds`, `cache_error`, and metadata. The accompanying `latest.json` describes `beta_ref=3.5`, `nt=20`, and sweep 12000.

Across each of the eight short-archive sampled checkpoint records and eight multihit file key sets, **no keys `X` or `O` were present**. More importantly, the records supply no identified sample-level Gauss-projected Feynman–Kac seam variables, physical last-neighbor integrated plaquette path source `X=b integral p_g dt`, target cap insertion `O=k_a(W_f)`, and jointly weighted path observations sufficient to form `E_0^O[P_N(X)]`. The files describe a different stage/observable workflow. Their `direct` and `multihit` correlation outputs cannot be silently re-labelled as physical source moments.

## What the R3-IR-404 test actually needs

At a specified finite rhombus disk, regulator, physical Wilson coefficients, last-neighbor reference H(1,1,1,0), Euclidean inverse temperature beta, and cap radius a, obtain from a **provably matched physical reference measure** paired samples or exact integrals of
- `O=k_a(W_f(q_0)) >=0`,
- `X=b_g integral_0^beta p_g(q_s) ds`,
- the physical gauge-seam measure and sampling/importance weights.

Only then compute ordinary `M_N=E[P_N(X)]` and cap-biased `M_N^O=E[O P_N(X)]/E[O]`, together with a deterministic remainder `r_N(beta b_g)` and defensible numerical uncertainty bounds. The sufficient certificate is `2 M_N^O-M_N >= r_N`; the condition is not an identity and cannot be tested from correlations alone.

## Conclusion

No R3-IR-404 numerical test has been completed from the supplied Stage-26 files. The present data are valuable historical evidence for their stated correlation calculations, but do not authenticate the original-link Gauss-projected Wilson cap/cosh ensemble. Reusing them to claim a favorable or unfavorable cap bias would be a provenance error.

A reproducible physical reference-chain construction and a measurement of paired O and X, with gauge seam accounted for, is the immediate outstanding experimental obligation; analytic refinement-uniform control remains independently OPEN. This audit does not challenge the original Stage-26 outputs on their own defined terms.
