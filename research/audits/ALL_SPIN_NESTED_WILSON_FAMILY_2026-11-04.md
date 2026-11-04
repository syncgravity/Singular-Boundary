# Arbitrary-spin two-face nested Wilson family — exact coefficientwise PW control (2026-11-04)

**Exact family-level theorem in a finite, corrected original-link, open two-plaquette SU(2) strip. Not arbitrary-history local-first closure, interacting coupling convergence, or a continuum mass gap.**

## Operator and physical inputs

Use adjacent face holonomies A,B with the *original-link* free electric operator K=4(C_A+C_B)+2D, D=∑_a R_{A,a}L_{B,a}, C=-∑_a R_a²; generators are iσ_a/2. The independent face holonomies are a representation of the original-link Gauss-invariant open-strip model, not an independently substituted rotor Hamiltonian.

For every integer n≥1 set F_n=χ_n(A)χ₁(B) with outer history [1,2] and G=χ₁(A) with nested inner history [1]. Put W_l=χ_l(A)χ₁(B), T_l=D W_l, Γ_K(f,g)=(fKg+gKf-K(fg))/2, B=K⁻¹QΓ_K.

## Exact source

The character identities χ_nχ₁=χ_(n+1)+χ_(n−1) and χ_n R_aχ₁=(R_aχ_(n+1)−R_aχ_(n−1))/(n+1) follow from the Chebyshev identity U'_(n+1)−U'_(n−1)=2(n+1)U_n. Therefore

**Γ_K(F_n,G)=−n W_(n+1)+(n+2)W_(n−1)−(T_(n+1)−T_(n−1))/(n+1).**

The source has no Haar constant because it carries B-spin 1. Both channels are physical and cannot be discarded on connected-minimal-support grounds.

## Exact electric inversion and matrix trace norms

At degree pair (l,1), D=J_(l/2)·J_(1/2) has eigenvalue d_+=l/4 with multiplicity l+2 and d_−=−(l+2)/4 with multiplicity l (the second channel is absent for l=0). The positive electric energies are k_±=l(l+2)+3+2d_±.

For l=n+1 take (α,β)=(-n,-1/(n+1)), and for l=n−1 take (α,β)=(n+2,+1/(n+1)). The *exact PW coefficient matrix* is C_l=(αI+βD)[(l(l+2)+3)I+2D]⁻¹. Its nuclear norms simplify to:

b_+(n)=(n+2)(8n³+32n²+39n−3)/[(2n²+7n+9)(2n²+9n+13)];

b_−(n)=n(8n³+16n²+7n+17)/[(2n²−n+3)(2n²+n+3)].

They hold for all integers n≥1. At n=1, b_+=19/36 and b_−=2, agreeing with research/audits/NESTED_PW_COEFFICIENTWISE_AUDIT_2026-11-04.md.

## Exact nested local-first norm ratio

With projective PW norm Pσ(f)=∑_l d_l e^{σ|l|}||A_l||_(S1) and local-first L^r using spin moment (1+max_l n_l)^r, we have Pσ(F_n)=4(n+1)²e^{σ(n+1)}, Pσ(G)=4e^σ. With history e^{κ|I|}, ||F_n||_(L1)=4(n+1)³ e^{2κ+σ(n+1)}, ||G||_(L2)=16e^{κ+σ}.

For n≥2, the exact ratio of the output L1 norm to input L1×L2 is

R_n(σ,κ)=e^{-κ}[2(n+2)² b_+(n)+2n²e^{-2σ}b_−(n)]/[64(n+1)³].

The n=1 lower block (degree (0,1)) has moment factor 2, not 1, giving R_1=e^{-κ}[19/2+8e^{-2σ}]/512.

**For all n≥1, κ>0, σ≥0: 0<R_n(σ,κ)≤e^{-κ}/16.**

All-degree proof: b_+≤2 because 2den_+−num_+=16n³+111n²+269n+240>0; b_−≤3 because (3den_−−num_−) at n=m+1 equals 4m⁴+2m²+3m+24>0. For n≥2, e^{-2σ}≤1 and 4(n+2)²+6n²≤4(n+1)³ because the difference 4n³+2n²−4n−12 is positive for integers n≥2. The n=1 expression is ≤35/1024<1/16. In particular,

**lim_(n→∞) n e^κ R_n(σ,κ)=(1+e^{-2σ})/16** for any fixed σ,κ.

This is a family-level **high-spin gain**, not a general norm theorem. The projective trace-class sum and the original shared-link cross derivative are essential.

## Verification and open obligations

The independent SymPy checker [verify_all_spin_nested_family_2026_11_04.py](../tests/verify_all_spin_nested_family_2026_11_04.py) evaluates 512 exact-rational coupling blocks, checks closed polynomial bounds and asymptotics, and directly re-evaluates the corrected quaternion-source and K-inverse equations for n=1..5, reducing modulo both SU(2) sphere constraints. PASS. These finite checks supplement, not replace, the all-n character/Casimir proof.

The calculation tests **one structured family only**. The arbitrary-spin, arbitrary-width coefficientwise local-first tame estimate, three-face nested recoupling, the conditional Borel disk's inherited hypotheses, and physical interacting spectral/continuum obligations remain OPEN. Next evaluate three-face histories with both shared-link D12 and D23 terms and preserve disconnected-output channels.
