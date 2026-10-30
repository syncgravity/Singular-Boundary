# The Singular Boundary — Parity-resolved second response and exact finite SU(2) certificate

Date: 2026-10-28. Branch: `audit/2026-10-28-independent-reconstruction`.

**Scope and status.** The exact fourth-source/second-coupling-response identity is independently proved on a finite compact gauge-link Hilbert space. Its nonzero coefficient is independently checked in the original three-rhombus **spatial seed** in the **electric reference model**, and continuity extends its sign to sufficiently small nonzero magnetic coupling on that fixed graph. The mixed/even-sector response is independently checked in an actual one-rhombus SU(2) Wilson model at weak positive magnetic coupling. The all-scale nonlinear Penrose estimate, physical-point variance collapse and positive continuum mass gap are **OPEN**. The seed is not the authentic full temporal Q14 cavity. Stage 7/26 identity to the declared Hamiltonian remains a separate provenance gate. No Monte Carlo or altered original artifacts.

## Inputs and convention

Independently consulted the current repository's `R3_IR_SYMMETRY_SECTOR_THREE_SOURCE_2026-10-28.md`, `R3_IR_REFINED_CURVATURE_WEIGHTED_ALIGNED_RESPONSE_2026-10-28.md`, and `R3_IR_THREE_SOURCE_ENERGY_WINDOW_2026-10-28.md`; compared the embedded three-face canonical Z^5 vertices with the archived spatial-seed fixture. We use the link Laplacian convention `-Δ χ_j=j(j+1)χ_j` and a four-equal-edge rhombus electric energy `a*n(n+2)` for `χ_(n/2)`.

## Theorem SR-1: exact first nonvanishing reflection-sector response

Let H_0 be a positive self-adjoint Hamiltonian with compact resolvent and a **simple** ground state Ω; set K=H_0−E_0, Q=I−|Ω><Ω| and G=Q K^{-1}Q (bounded at every fixed finite regulator, but not assumed uniformly bounded). Suppose an involution J satisfies JH_0=H_0J, JΩ=Ω, and JAJ=−A for a bounded self-adjoint multiplication observable A. Consider H(t)=H_0−tc A, with real c>0, possibly plus a scalar function of t. Let Ω_t be its normalized analytic ground vector near zero, and V(t)=〈Ω_t,A²Ω_t〉−〈Ω_t,AΩ_t〉². Then V'(0)=0.

Put `X=AΩ` (odd), `Y=G X` (odd), `S=Q A²Ω` (even), `v=||X||²`, and `Z=G A Y` (even). The exact **second derivative** is

**V''(0)=c² {4 Re〈S,Z〉+2〈Y,(A²−v I)Y〉−8[〈X,Y〉]²}.**        (SR-1)

All inverses in this equation are vacuum-orthogonal. The first term contains a nested odd→even inverse-energy response; the second probes the odd sector, and the third is the square of the static odd-source susceptibility. The expression need not be nonnegative or nonpositive.

**Proof.** Fix the real/parallel phase of Ω_t. Analytic perturbation of the simple ground eigenvector gives `Ω'_0=cY`, `〈Ω,Ω''_0〉=−c²||Y||²`, `QΩ''_0=2c² G A Y`, because E'(0)=〈Ω,−c A Ω〉=0. Thus `Ω''_0=2c² Z−c²||Y||²Ω`. Also `μ(t)=〈Ω_t,AΩ_t〉` satisfies μ(0)=0 and `μ'(0)=2c〈X,Y〉`. Differentiating 〈A²〉−μ² twice yields (SR-1). Parity makes V'(0)=0 but does not cancel the two-resolvent contributions.

**Exact scaled obligation.** For the source-aligned geometric deformation of the historically proposed Wilson model, `c=h^(α−4)`. For α=3/2, `c²=h^(−5)`. The earlier coupling-average and symmetry argument shows that `sup_{|t|≤τ}|V''(t)|=o(h^(−4))` would suffice to force the physical-point variance to zero **on a genuinely reflection-symmetric family**. At t=0, (SR-1) therefore requires its brace expression to be `o(h)`; this exact requirement is not established. Bounds at t=0 alone do not imply uniform t-control. Generic Penrose approximants need not admit the assumed involution.

## Theorem SR-2: exact second response on authentic three-rhombus spatial seed

The recovered canonical face labels are:
`f0=[z,z+e0,z+e3,z+e0+e3]`, `f1=[z,z+e2,z+e3,z+e2+e3]`, `f2=[z,z+e0,z+e1,z+e0+e1]`, with `z=(-1,-1,-1,-1,-1)` and corresponding ordering inherited from the prior ledger. The permutation of Z^5 coordinates `(0 3)(1 2)` fixes f0 and swaps f1,f2; the union has exactly 10 edges, and f1,f2 share no edge.

Take the **actual finite-link SU(2) Hamiltonian** `H_E=a Σ_e(-Δ_e)` on that ten-edge spatial graph and `B=p_{f1}−p_{f2}`. Its reflection is odd. Because f1,f2 are edge-disjoint, the character functions generated from B form a (generally infinite-dimensional) product-character subspace invariant under the electric operator, with one-face energies `E_n=a n(n+2)` and character multiplication `p|n>= (|n−1>+|n+1>)/2`, deleting n=−1.

The exact Haar moments are `〈B〉=0`, `〈B²〉=1/2`, `〈B⁴〉=5/8`. The vector `X=BΩ` is a 3a eigenvector with norm² 1/2. Moreover, `S=Q B²Ω` has orthogonal components with norm² 1/8 at energy 8a and norm² 1/4 at energy 6a. Substitution into (SR-1) for the family `H(t)=H_E−tc B` gives

- `4 Re〈S,Z〉=11/(144a²)`;
- `2〈Y,(B²−(1/2)I)Y〉=1/(12a²)`;
- `−8〈X,Y〉²=−2/(9a²)`;

and hence **V''(0)=−c²/(16a²)**, strictly negative. The full three-source response at t=0 is zero by reflection, while its next derivative is not. This is an exact SU(2) result on the genuine three-face *spatial* seed, not a numerical fit and not a statement about all Penrose regulators.

Now add an exactly reflection-symmetric **positive** Wilson magnetic potential `b Σ_{i=0}^2(1−p_{fi})`, with b>0. Since each potential is bounded and H_E has a simple ground state with compact resolvent, finite-graph analytic perturbation theory makes V''(0;b) continuous at b=0. There exists **some** b_*(a,c)>0 so that V''(0;b)<0 for every `0<b<b_*` (for sufficiently small |t| with positive deformed face couplings). No explicit positive threshold or strong-field uniformity is asserted. This is a genuine weak-magnetic **nonlinear SU(2)** continuation, not a physical spatial-continuum result.

## Theorem SR-3: even-source response is genuinely nonzero in SU(2)

For one four-edge SU(2) rhombus, let `H_b=4a(-Δ_class)+b(1−p)` with `p=χ_(1/2)/2`. This source is geometric-reflection **even**. Its electric-reference variance is 1/4; direct finite character perturbation gives `d²/db² Var_{Ω_b}(p)|_{b=0}=−1/(32a²)`. The exact aligned response identity `d/db Var_{Ω_b}(p)=2〈Q(p−〈p〉)²Ω_b, (H_b−E_0)^{-1} Q(p−〈p〉)Ω_b〉` therefore yields

**R_2^{even}(b)=−b/(64a²)+O(b²)** as b→0+.

Thus the first nonzero even-source three-point response is nonzero for all sufficiently small positive b. The selection rule of SR-1 is not a general cancellation of interacting three-source response. This is an exact one-plaquette SU(2) weak-coupling theorem; it does not prove a nonzero result in the strong-magnetic Penrose continuum.

## SR-4: no sign-definite fourth-source bound from symmetry alone

As a separate exact **abstract** three-level witness, take `H_0=diag(0,Δ_1,Δ_2)`, `J=diag(1,−1,1)` and `A=[[0,1,0],[1,0,q],[0,q,0]]`, Δ_1,Δ_2>0, q real. Then JAJ=−A and

`V''(0)/c² = 4q²/(Δ_1 Δ_2)+2(q²−4)/Δ_1²`.

With Δ_1=1, Δ_2=2, the result equals −8 for q=0 but +28 for q=3. This toy is not a Wilson Hamiltonian. It proves that parity, positivity of the inverse-energy resolvent and a unique vacuum alone do not give a sign to the required quartic response.

## Evidence ledger and next proof gate

**Independently proved:** SR-1 general parity-resolved Kato formula; SR-2 authentic seed electric SU(2) coefficient and local analytic extension to sufficiently small b>0; SR-3 one-rhombus even-source weak-positive-magnetic response; SR-4 exact abstract sign obstruction. All finite, source-specific results.

**Still open:** an all-scale nonlinear Wilson bound on the even/mixed-sector nested-resolvent terms or `sup_{|t|≤τ}|V''_{h,3/2}(t)|=o(h^-4)` across a **genuinely reflection-symmetric** geometrically scaled Penrose regulator family; a generic nonsymmetric low-window response estimate; interacting continuum field normalization; physical volume/refinement-uniform mass gap. An exact zero at one isolated finite symmetric seed cannot supply uniformity as the graph grows.

**Recommended next proof:** investigate **localized source-specific quartic resolvent estimates**, including separate controls of the odd-sector susceptibility `〈X,G_-X〉`, the even-sector nested term `〈S,G_+ A G_-X〉`, and `〈G_-X,(A²−v)G_-X〉`. Any proposed bound must be derived from actual nonabelian Wilson dynamics, with explicit dependence on the mesh, geometry and physical time; it cannot assume a mixing or spectral gap strong enough to imply itself.

## Reproducibility

`verify_second_response.py` uses exact Z^5 incidence, Peter–Weyl character algebra, and symbolic rational resolvents; the second derivative is reproduced from a 9-dimensional finite-order character truncation (not claimed invariant under the full magnetic multiplication operator). It also checks the sign-indefinite 3-level witness. No Monte Carlo simulations, spectral fits, or historical sample replacements.
