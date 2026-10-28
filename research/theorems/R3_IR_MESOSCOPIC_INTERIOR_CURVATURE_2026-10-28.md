# R3-IR — interior mesoscopic curvature via a regional SU(2) variational comparison

**2026-10-28 | Independently proved finite-Hamiltonian theorem.** No Monte Carlo. Historical source archives unchanged. This establishes interior **regional averages**, not pointwise bulk-face curvature, torque mixing, spectral separation or a continuum theory.

## Model and notation
Finite, face-complete planar rhombus complex G=(V,E,F), every magnetic face four distinct links, link-face incidence at most 2. On full Haar L2(SU(2)^E), H=Σ_e a_e(-Δ_e)+Σ_f b_f d_f, d_f=1−ReTr W_f/2, a_e>0,b_f≥0, and −Δ χ_j=j(j+1)χ_j. The full-link ground state is unique, strictly positive and invariant under vertex gauge transformations; hence it equals the physical ground state and expectations ν refer to that state. Trials below are used on the full link space and need not themselves be gauge invariant.

Fix nonempty D⊆F, S=∪_{f∈D}∂f, C(D)={g∉D: ∂g∩S≠∅}, A_S=Σ_{e∈S}a_e, B_D=Σ_{f∈D}b_f>0 and B_C=Σ_{g∈C(D)}b_g.

## Theorem MI-1 (localized mean curvature)
**Σ_{f∈D} b_f E_ν[d_f] ≤ (3/√2) √(A_S B_D)+2B_C.**

**Proof.** Scale only the D magnetic terms by t∈[0,1]. The ground energy E(t) is concave, differentiable, and satisfies Σ_D b_f E_ν[d_f]=E'(1)≤E(1)−E(0). Delete every magnetic face touching S, including D and C(D), yielding H_removed whose ground is Ω_out(U_{E\S})⊗1_S. Since the C(D) potentials are nonnegative, E(0)≥E_removed. Use the normalized full-space trial Ψκ=Ω_out∏_{e∈S}qκ(U_e), qκ=Zκ^(-1/2)exp(κ p(U)), p=ReTr U/2. Its electric energy on S is A_S kκ, where kκ=(3κ/8)rκ≤3κ/8, rκ=∫p qκ²∈[0,1]. By independent Haar factors E_Ψ p(W_f)=rκ^4 for every f∈D. Thus E_Ψ d_f=1−rκ^4≤4(1−rκ)≤3/κ. Every g∈C(D) contributes at most 2b_g, while all remaining expectations are exactly those of H_removed. Consequently E(1)−E(0)≤(3κ/8)A_S+(3/κ)B_D+2B_C. Optimize at κ=√(8B_D/A_S). QED.

No estimate of the interacting state outside S was used. Contrast the earlier private-edge lemma: individual faces in D need not have any private edge; a *regional* boundary penalty replaces the one-face neighbor penalty.

## Corollary MI-2 (inhomogeneous regional mean)
With a_e≤a_max on S and 0<b_min≤b_f≤b_max for D∪C(D), |S|≤4|D| gives

(1/|D|)Σ_D E_ν[d_f] ≤ 3√2 √(a_max b_max)/b_min + 2(b_max/b_min)|C(D)|/|D|.

For uniform a,b the bound simplifies to 3√2√(a/b)+2|C(D)|/|D|. If D=F, C is empty and the previous global mean-deficit theorem is recovered.

## Theorem MI-3 (Penrose interior-ball bound)
For a genuine face-complete Penrose rhombus tiling with edge length h, shape factors σ_-=sin(π/5), σ_+=sin(2π/5), φ=σ_+/σ_-=(1+√5)/2, let D_R be the faces with centers within Euclidean radius R of x. Suppose the closed ball B_{R+3h}(x) is inside the complete tiled patch and R>h. Every face lies within h of its center, and the centers of two edge-sharing faces differ by ≤2h. Area comparison gives

|D_R|≥π(R−h)^2/(σ_+h²),
|C(D_R)|≤8π(R/h+1)/σ_-,
|C|/|D_R|≤8φ(r+1)/(r−1)^2, r=R/h>1.

For the **declared**, not fully Stage26-source-certified, geometric trajectory a_e=g3²/(2w_e), b_f=4/(g3² h² σ_f), σ_-/2≤w_e≤σ_+ and σ_-≤σ_f≤σ_+, we obtain

**(1/|D_R|)Σ_{f∈D_R}E_ν[d_f] ≤ (3φ/√2)g3²h +16φ²(r+1)/(r−1)².**

If h→0, R(h)/h→∞, and the interior-ball condition holds, the RHS→0. One may also choose R(h)→0, e.g. R(h)=√(hℓ) for fixed positive physical length ℓ. For δ>0, Markov bounds the expected fraction of faces with d_f≥δ by the same RHS divided by δ. This is local **mesoscopic mean** flatness, not a bound at a specified face and not quantum-continuum field convergence.

## Independent deterministic verification and scope
Reproducibility: scripts/audit/verify_mesoscopic_curvature.py verifies exact κ minimization, shape coefficient identities and region/crossing-face counts of all seven nonempty subregions of the original three canonical Z5 seed rhombi (10 distinct edges). The finite fixture is **not** the full temporal Penrose Q14 archive and no historical chain or simulation is rerun.

Status: MI-1, MI-2, MI-3 **independently proved under stated Hamiltonian and geometry assumptions**. Open: uniform single interior face expectation; joint curvature and long-path connector torque expectations; a positive uniform physical spectral gap; spatial quantum continuum; exact Stage26 action identity. With D={f} for an interior face the crossing penalty remains of order one: this theorem does not settle the previously open single-face problem.
