# R3-IR-593 — One-sided radial-score oscillation is strictly weaker than positive-current variation

Date: 2026-10-31. **Continuing the prior branch's signed radial-current theorem (claims R3-IR-289–292)**, using the supplied branch transcript as the source of its claimed exact Ward identity. This note independently establishes a sharp countermodel but does **not** independently rederive the full nonlinear conditional Ward theorem or prove its required interacting-vacuum estimate.

## Previous branch's hierarchy and open problem

For a face-deleted SU(2) class marginal dν=(2/π)sin²u ψ(u)²du, the prior branch states a Ward identity d log ψ/du = -4 C(cos u)/(A sin u), where C is the conditional vacuum-score current. It defines the one-sided log-amplitude oscillation O=sup_{0≤v≤u≤π/2}[log ψ(u)-log ψ(v)]_+ and positive current budget T=(4/A)∫_0^{π/2}[-C(cos u)]_+/sin u du, and claims 0≤O≤T≤B, with B an earlier positive effective-fiber-potential budget. That branch's crucial uniform interacting-vacuum estimate sup_f T_{f,h}=o(h^-1/4) **remains unproved**. It also claims cap probability ≥ e^{-2T} m_H(cap). We should test the potentially weaker O criterion before tackling T.

## Explicit exact countermodel

For every even integer n≥4, set k=n² and ε=n^-1/2. Define

ψ_n(u)=[1+ε cos(2ku)]/sqrt(1+ε²/2), u∈[0,π].

Because k≥2, E_Haar cos(2ku)=0 and E_Haar cos²(2ku)=1/2 for the class Haar density (2/π)sin²u du. Thus ψ_n is normalized and strictly positive, smooth, and invariant under the center transformation u↦π-u (k integer). Every measurable center ball E satisfies

P_ψ(E)/P_Haar(E)≥[(1-ε)/(1+ε)]²→1,

and likewise the upper ratio tends to one. This is an elementary uniform density comparison, not a simulation.

On [0,π/2], the cosine performs k/2 complete oscillations when k is even. The positive total variation of log ψ is therefore exactly

T_n=(k/2)log[(1+ε)/(1-ε)],

while its maximum one-sided logarithmic increase is

O_n=log[(1+ε)/(1-ε)].

As n→∞, O_n~2n^-1/2→0 but T_n~n^3/2→∞. The ratio T_n/O_n=k/2=n²/2 is exact. Consequently **a uniform current positive-variation bound is not necessary for near-Haar center caps, even for smooth positive center-symmetric SU(2) rotor ground-state amplitudes**. The previous branch already knew T is sufficient but can be excessively strong relative to B; this establishes a second strict separation O≪T.

For each n a smooth real SU2 class potential V_n can be constructed so ψ_n is the positive ground state of -Δ+V_n (set V_n=(Δψ_n)/ψ_n +constant, then shift to nonnegative). This is a regulator-dependent synthetic rotor potential, NOT a physical Yang–Mills vacuum or proof of any Penrose estimate.

## Consequence for proof strategy

The exact one-sided net-score oscillation O is the *first* analytic quantity to target if the claimed cap comparison involving O can be established with the needed center symmetry. Replacing O by positive-current variation T may discard arbitrarily large cancellations. A rigorous nonlinear Penrose closure requires verifying the original marginal Ward identity from the genuine deleted-face Gauss-invariant vacuum and proving a uniform one-sided bound on its **signed integral over intervals**. No such interacting-vacuum estimate is proved here. Do not infer continuum existence or a mass gap from the countermodel.

Reproducibility: ChatGPT Library /The Singular Boundary/Source/audit_radial_current_oscillation.py and /The Singular Boundary/Source/signed_radial_current_oscillation_countermodel_2026-10-31.json. The original previous-branch proof package was not mounted in this session; available source was the user-provided branch transcript `Branch · Read Conversation Content.txt`.
