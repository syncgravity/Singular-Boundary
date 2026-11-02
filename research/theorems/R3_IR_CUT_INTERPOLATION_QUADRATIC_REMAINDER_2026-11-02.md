# Cut interpolation quadratic response and spatial limitation — 2026-11-02

Under the earlier certified uniform cut-interpolation gap δ=609/4000 and multiplication perturbation norm c=269/72000, for H_t=L0+tV_cut let h_t be normalized real positive ground vector, E_t its ground energy, R_t the reduced resolvent. Derivative identities imply Q_t h_t''=−2 R_t(V_cut−E_t')h_t' and <h_t,h_t''>=−||h_t'||². Thus ||h_t''||≤5(c/δ)². For a bounded self-adjoint O, |μ_t''(O)|≤12(c/δ)²||O||∞ and therefore |μ_t(O)−μ0(O)−t μ0'(O)|≤6(c/δ)²t²||O||∞, all uniform in volume.

Combine with prior endpoint localized first-order susceptibility for a right residual bond w_k, k≥j+2, across a cut after face j: μ0(w_k)=0 and |μ0'(w_k)|≤0.002401716(5/6)^max(0,k−j−2). The new **two-scale bound** is |μ_t(w_k)|≤0.002401716 t (5/6)^max(0,k−j−2) + (72361/23071765248)t², with quadratic coefficient ≈3.136344325e−6.

**Limitation:** quadratic error lacks distance decay, so this is *not* all-t localization or fourth-order extensivity. No interacting λ=1 or continuum Yang–Mills mass gap is established. Complete audit, rational verifier, log and SHA256 manifest archived in Library /The Singular Boundary/Proof Audits.