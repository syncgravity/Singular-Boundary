# R3-IR — Localized excited-state relative energy and Penrose spectral-window Wilson flatness

**Date:** 2026-10-28  
**Classification:** Independently proved for explicitly defined finite nonlinear SU(2) Wilson Hamiltonians; Penrose refinement consequences conditional on the declared geometric coefficients and interior-collar assumptions.  
**Not established:** Stage 7–26 source-level identity, regulator-uniform physical spectral gap, fixed-physical-support renormalized Wilson variance, complete quartic resolvent control, or a quantum continuum.

## Sources and provenance

The current independent GitHub audit branch was inspected before writing. Dependencies:

- `research/theorems/R3_IR_MESOSCOPIC_INTERIOR_CURVATURE_2026-10-28.md` (MI-1–MI-3; regional vacuum trial-state estimate).
- `research/theorems/R3_IR_MESOSCOPIC_WILSON_LOOP_DENSITY_2026-10-28.md` (LW-1–LW-7; noncommutative Wilson perimeter and rooted averages).
- `research/theorems/R3_IR_EXCITED_CURVATURE_WARD_2026-10-28.md` (EX-1–EX-8; previous excited-state bound charging the entire E0).
- `research/theorems/R3_IR_QUARTIC_SPECTRAL_WARD_AUDIT_2026-10-28.md` (QR-1–QR-5; unresolved odd/even resolvents).

The only explicit original-geometry fixture checked in this report is the three-rhombus canonical Z^5 spatial seed, with ten distinct edges; it is **not** the full Penrose Q14 temporal insertion or the Stage 26 lattice. Original archives and binaries remain immutable. No Monte Carlo was rerun.

## Model and definitions

Let G=(V,E,F) be a finite, face-complete, edge-to-edge planar rhombus graph. Every face has four distinct boundary edges, each edge belongs to at most two faces. On full L²(SU(2)^E), with -Δ χ_j=j(j+1)χ_j, let

 H = ∑_e a_e(-Δ_e)+∑_f b_f d_f,   d_f=1−(1/2)ReTr(W_f),   a_e>0, b_f≥0.

H has compact resolvent, a unique strictly positive vacuum Ω, and is invariant under vertex gauges. Ω is therefore physical, and restrictions to the gauge-invariant Hilbert space are reducing. Put E0=inf σ(H), K=H−E0. Let P_≤η=1_[0,η](K), with η≥0, in either the physical subspace or the full space.

For a nonempty face set D, let S=∪_{f∈D}∂f (edge set), and C(D)={g∉D:∂g∩S≠∅}. Put A_S=∑_{e∈S}a_e, B_D=∑_{f∈D}b_f>0, B_C=∑_{g∈C(D)}b_g. Define the **cut Hamiltonian**

 H_out=∑_{e∉S}a_e(-Δ_e)+∑_{g∉D∪C(D)}b_gd_g.

The operator H_out acts trivially on the removed edges S. Denote E_out=inf σ(H_out). There is no requirement of translation invariance, weak coupling, or an assumed gap.

## Theorem ER-1 — Exact localized excitation energy budget

For every normalized ψ∈Ran P_≤η,

 **∑_{f∈D} b_f〈ψ,d_fψ〉 ≤ 3/√2 √(A_S B_D)+2B_C+η.**   (ER-1)

**Complete proof.** Since every omitted electric and magnetic term is nonnegative,

 H−H_out−∑_{f∈D} b_fd_f=∑_{e∈S}a_e(-Δ_e)+∑_{g∈C(D)} b_gd_g ≥0

as quadratic forms, hence ∑_D b_f〈d_f〉_ψ ≤〈H〉_ψ−〈H_out〉_ψ≤E0+η−E_out. The independent regional product-link trial from MI-1, applied to H itself rather than only a coupling derivative, yields

 E0−E_out≤ inf_{κ>0}[(3κ/8)A_S+(3/κ)B_D+2B_C]
 =3/√2 √(A_S B_D)+2B_C.

The trial is Ω_out(U_{E\S})∏_{e∈S}Zκ^(-1/2)exp(κp(U_e)); the links S are independent conditional on all other links and the four-link plaquette expectation is rκ⁴. The source's non-gauge-invariant trial is permitted in the full Hilbert space because its lowest state is unique and gauge invariant. The one-link bounds kκ≤3κ/8 and 1−rκ⁴≤3/κ were previously proved and are used here. Combining the form inequality and energy increment proves ER-1. In contrast to EX-1, the entire E0 does not appear. QED.

If b_f∈[b_min,b_max] on D∪C and a_e≤a_max, |S|≤4|D| yields for all such ψ,

 **δ_{D,ψ}:=|D|⁻¹∑_{f∈D}〈d_f〉_ψ ≤3√2 √(a_max b_max)/b_min +2(b_max/b_min)|C(D)|/|D|+η/(b_min |D|).** (ER-2)

## Theorem ER-2 — Uniform low-energy Penrose interior mean flatness

Use the **declared, not yet Stage26 source-certified**, Penrose geometric coefficients

 a_e=g₃²/(2w_e),  b_f=4/(g₃²h²σ_f),  σ_-≤σ_f≤σ_+,  σ_-/2≤w_e≤σ_+,
 σ_-=sin(π/5), σ_+=sin(2π/5), φ=σ_+/σ_-=(1+√5)/2.

For D_R consisting of faces whose centers lie in an interior physical ball of radius R>h, assume B_{R+3h} lies inside the complete tiled patch. The deterministic MI-3 counting gives

 |D_R|≥π(R−h)²/(σ_+h²),   |C(D_R)|/|D_R|≤8φ(R/h+1)/(R/h−1)².

For **every** normalized ψ∈Ran P_≤η, ER-2 gives

 **δ_{R,η}(h):=sup_{ψ∈Ran P_≤η,||ψ||=1}|D_R|⁻¹∑_{f∈D_R}〈ψ,d_fψ〉**

 ≤ **(3φ/√2)g₃² h +16φ² (R/h+1)/(R/h−1)² +η g₃² σ_+²h⁴/[4π(R−h)²].**  (ER-3)

At fixed η and fixed physical R, the right side is O(h), uniformly over finite ambient patches retaining the collar. It also tends to zero for R(h)→0 with h/R(h)→0 and ηh⁴/R(h)²→0. This is **uniform over the entire fixed-energy spectral subspace**, not a claim that any nonvacuum excitation below η exists.

## Theorem ER-3 — Strong Wilson-loop flatness and all-band leakage for an unrenormalized rooted average

For each face f∈D select a topological-disk face patch Q_f⊆D containing f, with at most k faces, and let

 Wbar_D=(1/|D|)∑_{f∈D} (1/2)ReTr W_{∂Q_f},
 T_D=I−Wbar_D,  0≤T_D≤2I.

LW-1 provides the **pointwise** inequality

 T_D≤[k/|D|]∑_{f∈D}∑_{g∈Q_f}d_g≤[k M_k/|D|]∑_{g∈D}d_g,
 M_k=2·3^{k−1}−1,

because each g lies within dual-graph radius k−1 of the root and face-degree≤4. Thus for every normalized ψ∈Ran P_≤η,

 〈ψ,T_Dψ〉≤kM_k δ_{D,η},   ||T_Dψ||²≤2kM_k δ_{D,η}.

It follows that

 **|| (Wbar_D−I)P_≤η ||≤[2kM_kδ_{D,η}]^(1/2)**,
 **|| P_>Λ Wbar_D P_≤η ||≤[2kM_kδ_{D,η}]^(1/2) for every Λ≥η.** (ER-4)

This is a strong finite-regulator **all-band leakage** estimate for the averaged bounded-complexity Wilson observable. In the Penrose setting, at fixed physical R, fixed k and fixed η, it is O(√h), independent of how far above η the high band begins. It is stronger than high-energy resolvent suppression, but for a much more restricted **unrenormalized** observable.

The estimate says nothing about all excitations below η being absent; in particular no mass gap follows. As h varies, the Hilbert spaces vary, so this is not strong operator convergence on a constructed continuum Hilbert space.

## Theorem ER-4 — Mesoscopic suppression for the α=3/2 renormalized source, fixed-energy to ultraviolet transitions

Take D=D_R, with h≪R≤R_0, q_f=σ_f φ_h(x_f), |q_f|≤q_max independent of h, and

 A_{h,3/2}=h^(1/2)∑_{f∈D_R}q_fp_f.

Scalar subtraction B=A−h^(1/2)∑q_fI leaves disjoint spectral-band transitions invariant. The exact excited-state Ward identity in EX-3, but using ER-1 in place of the **global** E0 budget, yields

 **||P_>Λ A_{h,3/2} P_≤η||² ≤ [2q_max²/(β_min Λ)] h³ [E_D+η](2a_max+η|D|),** (ER-5)

where E_D=3/√2 √(A_S B_D)+2B_C and b_f≥β_min h^-2 on D. Proof: Γ(A)=Σ_e a_e|∇_eA|²≤4a_max q_max²h Σ_Dd_f; B²≤2|D|q_max²hΣ_Dd_f. Consequently
 P_≤η B K B P_≤η=P_≤ηΓ(A)P_≤η+½{K_≤η,P_≤ηB²P_≤η},
so P_>Λ K P_>Λ≥ΛP_>Λ yields ER-5. No gap assumption occurs.

Under the Penrose geometric counting, |D_R|=O(R²/h²), |C(D_R)|=O(R/h) and E_D=O((R²+R)/h³) for R≫h and bounded R. Let R(h)=ℓ^(1−γ)h^γ with fixed physical ℓ>0 and 1/3<γ<1, and set Λ_h=ℓ^δ h^(−1−δ) in consistent fixed physical units, 0<δ<1, η fixed. Then

 ||P_>Λ_h A_{h,3/2}P_≤η||²=O(h^(1+γ+δ)+h^(3γ−1+δ)),

hence

 **||P_>h^(−1−δ) A_{h,3/2} P_≤η|| =O(h^((3γ−1+δ)/2))→0.** (ER-6)

For γ=1/2 this becomes O(h^(1/4+δ/2)). It suppresses **fixed-excitation-energy to UV** transitions of a shrinking-physical-support mesoscopic source, unlike the previous global E0 bound. This does **not** establish the needed estimate for the original fixed-physical-support smooth Wilson test (γ=0), or control the middle spectral window, odd/even resolvents or the quartic response.

## Exact limitation — Coherent amplitudes are not excluded by regional flatness

For a simply connected disk, independent based face holonomies can all be chosen with d_f=h (take W_f=diag(e^{i arccos(1−h)},e^{−i arccos(1−h)})). With |D|∼h^-2 and q_f=1, this makes Σ_Dd_f∼h^-1 although its **mean face deficit is h**; the scalar-subtracted α=3/2 source B=−h^(1/2)Σ_Dd_f has magnitude ∼h^-1/2. Hence no pointwise bound on B² of order O(1) can follow from a mere regional curvature density estimate. This is a deterministic **configuration-level obstruction**, not a claim such configurations dominate an interacting low-energy eigenstate. It explains exactly why ER-4 does not transfer immediately to a macroscopic normalized field.

## Exact verification and status

The checked verifier `scripts/audit/verify_local_excited_comparison.py` uses exact rational and symbolic arithmetic: the canonical three-face Penrose Z⁵ fixture (10 edges), all seven nonempty region/crossing-face incidence sets, the SU(2) fundamental Casimir, exact regional trial optimization, the geometric η term, and the mesoscopic transition exponent. **No Monte Carlo.** The general theorem is proved by the preceding form inequalities rather than by test counts.

**Independently proved:** ER-1, ER-2, ER-3, ER-4 at finite SU(2) regulator under stated assumptions. **Conditionally proved:** the refinement rates using the declared Penrose coefficients and full interior collar. **Open:** original Stage7/26 Hamiltonian identity; joint interacting excited-state curvature covariance; fixed-support α=3/2 low/intermediate spectral transition control; parity-sector inverse-energy resolvents; uniform infinite-physical-volume R3-IR gap; R2 nontrivial quantum continuum.

**Recommended next precise obligation:** prove a *connected/compensated* local-to-macroscopic summation estimate for the centered α=3/2 Wilson field that eliminates the coherent O(|D|) amplification, or produce a genuine nonlinear Penrose counterexample. This requires independent excited-state covariance or conditional-variance information and cannot be deduced from regional mean flatness alone. Do not assume mixing, transfer contraction, or a gap-equivalent Poincaré inequality.
