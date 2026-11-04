# R3-IR-563: Papers 2–6 source and 3D action coefficient audit (2026-10-31)

**Complete report** `R3_IR_563_papers_2_6_gauge_action_audit.md`, executable `audit_prism_action_coefficients.py`, and JSON `prism_action_coefficient_audit_2026-10-31.json` are stored in ChatGPT Library `/The Singular Boundary/Source/`. This Git checkpoint records the findings, provenance and blocking obligations.

**Sources:** Papers 2,3,4,5 were read from `Sharpe_dissertation_v10.7.tar.gz`; Paper 6 was **absent** from that archive and was not located by Library search. Paper 2 describes C5 and the coupled Z5 physical plane z1 and compact coordinate Re(z2), not an independently extruded 3D prism. Paper 3 develops complex structure J; Paper 4 studies acceptance-window failure bands and spectral effects; Paper 5 applies the hierarchy to a Fibonacci microtubule cavity. None derives a prism SU(2) kinetic or magnetic coefficient. The prism remains a distinct candidate, NOT the coupled Z5 geometry.

Define a *proposed model* in temporal gauge with rooted, mutually transported angular velocities and 3D Whitney masses M1 (1-form), M2 (2-form):

`L=(1/(2g²)) ωᵀM1 ω −(4/g²) Σ_f (M2)_ff (1−p_f)`; `p_f=Tr(U_f)/2`.

Formal Legendre transform gives `H=(g²/2) Πᵀ M1^{-1} Π +(4/g²)Σ_f(M2)_ff(1−p_f)`. The Wilson factor 4 matches the *diagonal quadratic magnetic mass* because `1−cos(|Φ|/2)=|Φ|²/8+O(Φ⁴)`; **off-diagonal M2 contributions are omitted by the declared mass-lumping approximation**. Full gauge covariance of rooted mixed electric derivatives, operator domain, and action-to-continuum convergence remain **unverified**. No paper supplies these normalizations.

For each six independent prism candidates M=5,7,9,11,13,15, the full conforming tensor-product 3D 2-form mass M2 was assembled by affine 2-form Piola transform, 2x2x2 Gaussian quadrature, and tested SPD. The two retained chord faces have total Wilson coefficient `B_e=4(w_horizontal+w_vertical)/g²`. The protected sector perturbation ratio is `rho=32 M1_ee(w_horizontal+w_vertical)/(3g⁴)`, which is *not* the arbitrary ~1e-4 earlier b scenario.

| M | h | M1 chord diagonal | horizontal M2 diagonal | vertical M2 diagonal | B_e (g²=1) | rho (g²=1) |
|---:|---:|---:|---:|---:|---:|---:|
|5|.2|.04704556|4.28534684|3.52841664|31.25505|3.92110|
|7|.142857|.03445817|6.65102331|5.06535114|46.86550|4.30640|
|9|.111111|.03135971|10.85254706|7.62040968|73.89183|6.17927|
|11|.090909|.02159502|10.07870264|7.83899094|71.67077|4.12728|
|13|.076923|.01759319|10.88691981|8.91974714|79.22667|3.71693|
|15|.066667|.01939508|19.42528859|13.09168090|130.06788|6.72714|

**New obstruction:** All six rho values exceed 1 even at g²=1, so prior R3-IR-556 small-forcing protected cap lower bound is **vacuous** for this newly action-normalized model. The geometric product M1*M2 is scale-neutral (M1~h, M2~1/h); decreasing g² would worsen rho as g^-4 in this convention. This does **not** refute cap positivity; it refutes applicability of this sufficient condition to these numerical parameters. These are candidate patch comparisons, NOT physically calibrated 3+1D Yang–Mills.

**Required next:** independently audit full Gauss-law covariance of mixed electric form, derive full finite-element canonical non-Abelian action with no arbitrary mass lumping, construct genuinely coupled Z5 native 3D cells, obtain Paper 6, and establish physically meaningful refinement with running couplings. The continuum mass gap remains open.

Executable source SHA256 `499a750c3fc10b23e9b5f1dae605fc0f71971bca4d144527d5d8ab2c4fcd6f2f`; JSON SHA256 `0347ae9fc5e3d4e5921fee679920727334d70e76f475b3675380c048e4b7359f`. Binary M1 stays in Library, none in Git.
