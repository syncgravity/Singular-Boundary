# Fourth-order ground-state response and normalization audit — 2026-11-02

Let L≥0 be self-adjoint with simple normalized constant ground vector 1 and gap κ, Q=I−|1><1|, R=(L|Q)⁻¹Q. Let V=Σ t_i w_i be a bounded mean-zero multiplication perturbation. The exact single-coupling ground energy derivative is
**E⁽⁴⁾(0)=24[〈V,RV〉〈V,R²V〉−〈V,RVRVRV〉]**.
Each R contains the centered projection Q. Omitting the disconnected normalization subtraction is incorrect.

For independent bond couplings,
**E_{abcd}=−Σ_{σ∈S4}〈w_{σ1},R w_{σ2}R w_{σ3}R w_{σ4}〉+Σ_{σ∈S4}〈w_{σ1},Rw_{σ2}〉〈w_{σ3},R²w_{σ4}〉**.
This includes repeated-label multiplicities. Under prior κ=23/144 and per-bond ||w_i||∞≤v=1/1152, every *fixed* quadruple satisfies **|E_{abcd}|≤48v⁴/κ³=1/149508096≈6.688600997e−9**, independently of strip length. The bound contains no spatial decay and naive all-bond sum scales O(N⁴), not O(N). Thus **fourth-order spatial extensivity remains open**, along with the interacting λ=1 and continuum Yang–Mills mass gaps.

An independent exact 5-state reversible matrix Taylor recursion and four-variable polarization verify the fourth-order formula and repeated/independent coupling algebra (scalar tests 288/25, −48/25, 17232/25; distinct-label mixed derivative 16/25). The companion full audit, executable verifier, log, and SHA256 manifest reside at Library /The Singular Boundary/Proof Audits.