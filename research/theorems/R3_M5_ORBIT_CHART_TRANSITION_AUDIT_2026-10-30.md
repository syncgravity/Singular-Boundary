# R3-IR-541 — Actual M5 natural spanning-tree gauge-chart transition does not identify fixed-metric forms

2026-10-30. Original Whitney NPZ SHA-256 d7bd716dcfa5ef640aabb824099ad614b4d64bfb781a3cbf4cc484bb8e902fbf. Source and binary stored in ChatGPT Library `/The Singular Boundary/Source/`.

For M5 extracted eleven-face graph, root=0, T1 BFS tree containing e4 and T2=T1-{4}+{13}, explicitly gauge-fix each tree with vertex transport h_v(U)=parallel product from root to vertex, using U_e^T=h_source U_e h_target^-1. In each tree chart every tree edge becomes identity. The two chart representatives are gauge transforms of the SAME original link configuration. Hence they lie on the same physical gauge orbit, and the gauge-invariant observable F(U)=p_face0(U)p_face10(U) is unchanged.

Using the **same original K=M^-1**, for the seeded configuration used in a fresh check:
Q_T1(U)=1.4565527946630905; Q_T2(U)=1.4995617051075518.
After their respective gauge-fixing transformations: Q_T1(U^{T1})=1.456552794723016 and Q_T2(U^{T2})=1.4995617051122145. The gap of ≈0.0430089104 remains. The consistency of each gauge-invariant quadratic energy under its own gauge transform was checked over five independent random configurations with tolerance 2e-8. These are floating-point finite-difference checks, not interval-certified inequalities.

Therefore the *canonical tree gauge-fixing chart transition acting by vertex gauge changes* does not identify these two fixed-K rooted quadratic forms on a gauge-invariant Wilson observable. This is expected given R3-IR-538 and R3-IR-540; its significance is explicit construction of the orbit-chart representatives, not exclusion of a general intertwiner.

This DOES NOT rule out a nontrivial diffeomorphism of orbit space, a nonlocal unitary, a change of metric K under the chart transition, or a different physical canonical discretization. Spectral inequivalence is unproved. Nor does this establish refinement-uniform deleted-face center-cap estimates or the continuum Yang–Mills mass gap. No binary data are to be committed to Git.

Reproducer `research/scripts/validate_m5_orbit_chart_change.py`, with dependencies from Library listed in the source-recovery manifest.
