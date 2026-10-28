# R3-IR — Improved curvature-weighted f-sum at the distinguished coupling

Date: 2026-10-28. **Status: new exact finite-volume identity and conditional geometric refinement consequence.** Do not infer continuum existence or a positive mass gap. No simulations.

## Model
Finite face-complete planar rhombus complex, SU(2) full-link Hamiltonian H=Σ_e a_e(-Δ_e)+Σ_f b_f(1-p_f). Unique gauge-invariant vacuum Ω, ν=Ω²dU. The one-link fundamental character p_f=(1/2)Tr(W_f) uses electric Casimir 3/4. Assume a_e≤a_max, each face has four distinct links and every link lies in ≤2 faces. For face subset D and bounded real test φ, define the centered field F_h^(α)=h^(−α)Σ_{f∈D} h²σ_f φ(x_f)(p_f−⟨p_f⟩). D lies in a fixed physical interior ball whose mean deficit obeys MI-3: Σ_{f∈D}⟨d_f⟩≤K_R h |D_R|, d_f=1−p_f∈[0,2], with |D_R|h²≤A_R.

## Theorem FS-1: exact curvature-weighted carré du champ
On each edge e∈∂f, with the standard SU(2) bi-invariant metric fixed by -Δχ_j=j(j+1)χ_j,

|∇_e p_f|²=(1−p_f²)/4.

To verify, use p²=(χ_0+χ_1)/4, -Δ p=(3/4)p and -Δχ_1=2χ_1; the product Laplacian identity -Δ(p²)=2p(-Δp)−2|∇p|² yields the displayed expression. Thus 1−p_f²=(1−p_f)(1+p_f)≤2d_f and for the energy-weighted covariance (Dirichlet Gram) matrix D_fg=Σ_e a_e ∫∇_e p_f·∇_e p_g dν,

D_ff=(1/4)(Σ_{e∈∂f}a_e)⟨1−p_f²⟩≤2a_max⟨d_f⟩;
D_fg=0 unless f=g or f,g share an edge.

As there are at most four distinct edge-neighbors per face, Cauchy and 2|xy|≤x²+y² give the *noncircular* general matrix inequality wᵀDw≤5Σ_f w_f²D_ff for all real weights w.

## Theorem FS-2: improved first physical energy moment
The exact ground-state transform yields M1(F)=⟨FΩ,(H−E0)FΩ⟩=Σ_e a_e∫|∇_e F|²dν. Using weights w_f=h^(2−α)σ_fφ(x_f), the prior regional curvature theorem and FS-1 give

M1(F_h^(α))≤10 a_max σ_+² ||φ||_∞² K_R (|D_R|h²) h^(3−2α)
≤C_{R,φ} h^(3−2α).

This applies **at the distinguished physical coupling**, provided the upstream MI-3 Hamiltonian coefficients and geometric interior assumptions are valid. At α=1: M1=O(h), improving the historical O(1) estimate. The argument does not use the value of the magnetic coupling except through the independently proved mean curvature estimate.

## Corollary FS-3: spectral low-energy concentration and gap/variance alternative
Let μ_h be the positive vacuum-orthogonal energy spectral measure of F_h^(1)Ω. For any ε>0, μ_h((ε,∞))≤M1/ε=O(h/ε), while 0≤V_h−C_h(t)≤t M1=O(th) uniformly for fixed t≥0. If V_h stays bounded and converges to v>0 along a subsequence, then C_h(t)→v for each fixed t, and every weak limit spectral measure of finite mass is vδ_0. If the physical gap Δ_h≥m>0, then V_h≤M1/m=O(h); conversely if liminf V_h>0, then Δ_h≤M1/V_h=O(h). This is a **conditional spectral obstruction**, not proof of either variance survival or gap closure.

More generally, for α<3/2 and a nonvanishing variance liminf, Δ_h→0 at rate O(h^(3−2α)); a nontrivial uniformly gapped field of this Wilson-area type requires α≥3/2. This necessary condition supersedes the weaker α≥1 conclusion of RN-1; it does not establish α=3/2 as sufficient, and the nonlinear field normalization remains open.

## Scope and integrity
The preceding covariance-tail analysis CC-1 through CC-4 remains valid as a static statement, but a separate spatial covariance-tail estimate is *not needed* to reach FS-3. Neither FS-3 nor mean flatness decides whether the smooth physical Wilson field has nonzero limiting variance; no spectral gap of the full physical theory has been proven or disproved. All constants are for a fixed physical interior ball and do not automatically pass to infinite physical volume or to the Stage26 implementation whose coefficient identification remains separately open.

Exact deterministic symbolic and canonical three-seed checks are in verify_fsum.py and verification_output.json, no Monte Carlo.

## Next independent gate
Prove or disprove fixed-physical-coupling variance survival for an appropriate observable family; because α=1 surviving variance would force a zero-energy sector, a genuinely positive-gap continuum requires either this field to vanish, a different normalization (at least α=3/2 for this family), or a different renormalized composite observable. Separately verify source-level Stage7/26 physical coefficients, and derive genuine temporal infrared bounds for spectrally complete sources rather than assuming them.