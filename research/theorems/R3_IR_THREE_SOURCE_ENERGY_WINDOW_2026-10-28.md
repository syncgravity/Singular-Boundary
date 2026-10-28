# R3-IR — Curvature-weighted energy-window reduction for the nonlinear Wilson three-source response

**Date:** 2026-10-28. **Evidence:** independently proved exact finite-volume operator/Dirichlet estimate and a conditional source-response spectral-window consequence. **Not** a bound on the low/intermediate spectral response, interacting continuum reconstruction, or physical mass gap. No Monte Carlo or changes to historical source files.

## Provenance and assumptions

Input documents reviewed directly on branch \`audit/2026-10-28-independent-reconstruction\`:
- \`research/theorems/R3_IR_CURVATURE_WEIGHTED_FSUM_2026-10-28.md\` (FS-1/FS-2);
- \`research/theorems/R3_IR_MESOSCOPIC_INTERIOR_CURVATURE_2026-10-28.md\` (MI-1/MI-3);
- \`research/theorems/R3_IR_REFINED_CURVATURE_WEIGHTED_ALIGNED_RESPONSE_2026-10-28.md\` (RR-1 through RR-5);
- \`research/theorems/R3_IR_ALIGNED_RESPONSE_AND_DISTINGUISHED_POINT_2026-10-28.md\` (AR-5).

The Stage 7/Stage 26 coefficient equality to the **declared** spatial Hamiltonian remains unverified. Statements below are therefore conditional on those coefficient assumptions and a complete Penrose interior collar.

Take a finite SU(2) rhombus graph, full-link \`L²(SU(2)^E)\`, and positive Hamiltonian \`H_h(t)=Σ_e a_e(-Δ_e)+Σ_f b_f(t)(1-p_f)\`, where \`0<a_e≤a_max\`, every face has four distinct edges, incidence per edge ≤2, and all \`b_f(t)\` are positive and uniformly comparable to \`h^{-2}\` for \`|t|≤2τ\`. With compact group and positive heat kernel, \`Ω_t\` is the unique strictly positive, gauge-invariant ground state and \`K_t=H_h(t)-E_h(t)\` has compact resolvent. The physical gauge-invariant subspace is reducing; all sources below are gauge invariant.

Choose fixed real bounded smooth \`φ\` supported in a full-collar physical interior region \`D_R\`, physical face area \`h²σ_f\`, and define the parameter-independent **uncentered** multiplication source
\`A_{h,α}=h^{2-α}Σ_{f∈D_R}σ_f φ(x_f)p_f\`.
Put \`a_t=A_{h,α}-〈A_{h,α}〉_t\`, \`Q_t=I-|Ω_t〉〈Ω_t|\`, \`L_h=2σ_+||φ||∞ (|D_R|h²)\`, and \`M_h=10 a_max σ_+²||φ||∞² K_R (|D_R|h²)\`, with \`K_R\` the uniform regional mean-deficit constant. From the earlier independent estimates, for fixed physical collar and uniform comparable t-couplings:
\`\`\`
||a_t||∞ ≤ L_h h^{-α},   M1_t(a_t)=〈a_tΩ_t,K_t a_tΩ_t〉 ≤ M_h h^{3-2α}.
\`\`\`
Here \`L_h,M_h\` are uniformly bounded in h and finite graph size at fixed physical support. The second bound uses actual nonlinear interacting mean curvature and the exact SU(2) carré du champ; it is not a Gaussian calculation.

## Theorem EW-1 — All-polynomial ultraviolet inverse-energy response bound

For any integer \`n≥2\` define \`B_{n,t}=a_t^n-〈a_t^n〉_t\` and spectral projector \`P_{>Λ}(K_t)=1_{(Λ,∞)}(K_t)\`, Λ>0, acting on the physical Hilbert space. Define
\`\`\`
R_{n,>Λ}(t)=〈Q_t B_{n,t}Ω_t, K_t^{-1} P_{>Λ}(K_t) Q_t a_tΩ_t〉.
\`\`\`
Then, **exactly at finite h and all nonzero magnetic couplings**,
\`\`\`
|R_{n,>Λ}(t)| ≤ n ||a_t||∞^{n-1} M1_t(a_t)/Λ²
              ≤ n L_h^{n-1} M_h h^{3-(n+1)α}/Λ².          (EW-1)
\`\`\`
In particular, for the connected **three-source** case n=2,
\`\`\`
|R_{2,>Λ}(t)| ≤2 L_h M_h h^{3-3α}/Λ².                       (EW-2)
\`\`\`
This is a genuine *high-energy* estimate, not a control of K_t^{-1} on low spectral sectors.

**Proof.** The exact ground-state transform for bounded real gauge-invariant smooth multipliers F reads \`M1_t(F)=Σ_e a_e∫|∇_eF|²Ω_t² dU\`. Since the centered source differs from the original by a constant, the product rule on the compact SU(2) link manifold gives \`∇_e(a_t^n)=n a_t^{n-1}∇_e a_t\`. Hence
\`M1_t(B_{n,t})≤n²||a_t||∞^{2n-2}M1_t(a_t)\`.
For any vacuum-orthogonal \`v\` of finite first energy moment, the spectral theorem gives
\`||K_t^{-1/2}P_{>Λ}v||²=∫_{E>Λ} E^{-1} dμ_v(E) ≤ Λ^{-2}∫ E dμ_v(E)=M1_t(v)/Λ²\`.
Cauchy-Schwarz in the K_t^{-1/2}-weighted inner product then yields
\`|R_{n,>Λ}|≤sqrt(M1_t(B_n)M1_t(a_t))/Λ²\`, proving EW-1. Every operation is finite-volume and uses only independently stated bounds. Q commutes with K and its spectral projectors.

## Theorem EW-2 — Refined response can be restricted to a mesoscopic energy window

The source is **exactly aligned** with the magnetic deformation in RR-2:
\`\`\`
h^{4-α} V'_{h,α}(t)
   = 2 Re〈Q_t a_t² Ω_t, K_t^{-1} Q_t a_t Ω_t〉
   =2 Re(R_{2,≤Λ}(t)+R_{2,>Λ}(t)).
\`\`\`
For the first candidate normalization \`α=3/2\`, take any fixed δ>0 and \`Λ_h=h^{-1-δ}\` in fixed physical energy units. EW-2 yields
\`\`\`
sup_{|t|≤τ}|R_{2,>Λ_h}(t)| ≤ C h^{1/2+2δ}=o(h^{1/2}),     (EW-3)
\`\`\`
uniformly over the admitted finite-area Penrose regulators and deformations.

Therefore **it suffices** to establish the following *strictly smaller spectral obligation*:
\`\`\`
sup_{|t|≤τ}|R_{2,≤h^{-1-δ}}(t)|=o(h^{1/2})              (OPEN).
\`\`\`
Combined with EW-3, this would give the previously sufficient response modulus \`sup|V'_{h,3/2}(t)|=o(h^{-2})\`, so RR-4 would imply physical-point variance collapse. This is a precise reduction, **not** a proof of the low-window estimate.

**Necessary spectral response if physical variance persists.** RR-3/RR-4 proves that if \`liminf_{h→0}V_{h,3/2}(0)≥v>0\`, then for each sufficiently small h there is some \`|t_h|=O(h²)\` with \`|V'_{h,3/2}(t_h)|≥c_vh^{-2}\`. Thus \`|R_{2}(t_h)|≥c'_v h^{1/2}\`. By EW-3, for every fixed δ>0,
\`\`\`
|R_{2,≤h^{-1-δ}}(t_h)|≥(c'_v/2)h^{1/2}
\`\`\`
for small h. **A surviving physical variance therefore forces a source-aligned inverse-energy response in this intermediate-and-low energy window.** This does *not* force a zero-energy physical excitation or rule out a positive mass gap at α=3/2: the window still reaches energies diverging as h^{-1-δ}.

For \`α=1\`, EW-2 gives \`|R_{2,>Λ}|≤C/Λ²\` for **every fixed Λ>0**, whereas a persistent variance would require \`|R_2|\gtrsim h^{-1}\` at a nearby coupling. Hence its spike must have arbitrarily large three-source contribution from **any** fixed low-energy window \`[0,Λ]\`. This is consistent with the already proved stronger \`O(h)\` first-moment obstruction for α=1.

## Further limits and integrity

The cutoff \`Λ_h=h^{-1-δ}\` is a **diverging energy cutoff**, not a proof of physical infrared decay. No assertion is made that the remaining projected response is small. In particular, bounded \`M1(a)\` or a positive finite-volume gap cannot control it uniformly: the avoided-crossing toy in RR-5 remains an abstract counterexample. The estimate holds separately for each fixed n; factors \`n||a||∞^{n-1}\` do **not** control the full unbounded Wilson-word hierarchy uniformly in word length.

No spectral continuity, interacting field variance, uniform physical mass gap, or R2 continuum reconstruction follows. The exact Stage 7/26 action correspondence remains a separate source-provenance gate.

## Reproducibility

The accompanying \`scripts/audit/verify_three_source_energy_window.py\` checks the exact SU(2) one-rhombus Peter–Weyl reference moments; the spectral high-energy Cauchy inequality on rational diagonal self-adjoint examples; and the symbolic exponents and distinguished-point thresholds. It does not simulate gauge fields. Its calculations support algebraic consistency; the proof above establishes the general identities.

**Next proof task:** model-derived control of \`R_{2,≤h^{-1-δ}}\` for a fixed smooth gauge-invariant Wilson test source in the actual nonlinear vacuum. This requires independent information on low/intermediate excited states and the relative phases of the three-source matrix elements, not merely the known curvature mean or first spectral moment.