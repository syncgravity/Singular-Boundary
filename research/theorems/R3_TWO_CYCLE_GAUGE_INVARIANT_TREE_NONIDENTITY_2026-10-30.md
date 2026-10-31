# R3-IR-535 — Gauge-invariant two-cycle tree-form nonidentity

On the oriented four-edge graph a:0->1, b:1->2, c:0->2, d:1->2, take root 0 and spanning trees T1={a,b} and T2={c,b}; these are both legitimate spanning trees. Define gauge-invariant based loops W1=a b c^-1, W2=a d c^-1 and F=(1/2)Tr(W1 W2). For source-left link generators X_j, form transported D_j=Ad(V_j)X_j, where root-to-source paths are V^(T1)=[1,a,1,a], V^(T2)=[1,c b^-1,1,c b^-1]. For fixed real positive K=I+.3(E_ad+E_da), evaluate the gauge-invariant principal quadratic energy Q_T[F]=Σ_ij K_ij (D_i F)·(D_j F).

A seeded 100-configuration finite-difference quaternion regression (h=1e-6) yields nonzero Q_T1-Q_T2, with sample 0 values 1.638349870406 and 1.500372620212 respectively, and maximum absolute sampled difference .275068474744. The difference is orders of magnitude above finite-difference error. One could obtain an algebraic exact witness by choosing specific quaternions and symbolic gradients; this result currently reports a reproducible NUMERICAL witness, not a computer-assisted certified inequality.

Unlike the single-cycle SU2 graph in R3-IR-534, the two independent cycles allow gauge-invariant Wilson word characters with gradients sensitive to relative root transports. The earlier one-cycle cancellation therefore does NOT generalize automatically to arbitrary multicycle graphs.

This demonstrates nonidentity of the quadratic-form densities on a gauge-invariant observable for the two explicitly defined rooted prescriptions with K fixed in common link labeling. It does **not** establish inequivalence of spectra or exclude a nontrivial gauge-compatible unitary intertwiner. Nor does this graph reproduce the assembled M5 inverse Whitney K; physical transport prescription and actual M5 equivalence remain open. The refinement-uniform cap estimate and continuum Yang–Mills mass gap remain open.

Reproduce using research/scripts/validate_two_cycle_tree_forms.py.
