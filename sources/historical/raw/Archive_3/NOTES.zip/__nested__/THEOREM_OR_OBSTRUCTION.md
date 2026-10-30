# The Singular Boundary: Is there a J-to-transfer spectral constraint?
26 October 2026. Formal theorem/obstruction audit grounded in Paper 3 and the known Stage 26 architecture.

## Source basis
Paper 3 (`Sharpe_Paper3_J_Operator_Hidden_Domain`, extracted text `paper3_audit.txt`) §2.1–2.3 defines `σ(z1,z2)=(ω z1,ω² z2)` and `J(z1,z2)=(i z1,i z2)` with `ω=e^(2πi/5)`; §7 defines `z2(τ)=A exp(2πipτ)`, p=3/13,5/13,8/13, and explicitly distinguishes kinematics from dynamics in Remark 6. Its identification `Im(z2)=ict` and Wick-rotation discussion are claims of the paper, not an established quantum reconstruction. The Stage 26 source delegates Wilson couplings and incidence to `stage7_checkpointed.setup_geometry`; that defining source has not been verified in this audit.

## Theorem 1: the C5 generator differs from exp(2πJ/5)
On C², `J=J1 ⊕ J2` acts with identical rotation angles on z1 and z2: `exp(θJ)(z1,z2)=(exp(iθ)z1,exp(iθ)z2)`. The C5 generator is `σ(z1,z2)=(ω z1,ω² z2)` and equals `exp((2π/5)J1) ⊕ exp((4π/5)J2)`, **not** exp((2π/5)J). Consequently `[σ,J]=0` does not identify its generator with J. Distinct character weights matter for any proposed physical lift.

## Theorem 2: no continuous nontrivial automorphism of a fixed integer lattice
Let Λ⊂R^d be a full-rank lattice, R: R→GL(d,R) a continuous homomorphism, and R(θ)Λ=Λ for every θ. In a lattice basis, R(θ) is in discrete GL(d,Z). The continuous image of connected R in a discrete space is constant, so R(θ)=I. Therefore no continuous nontrivial J rotation preserves the fixed Z5 lattice as a lattice automorphism. It may act on continuum parent coordinates, on a tiling hull, or via a separate physical representation, but that is additional structure and not a fixed finite-regulator symmetry.

## Theorem 3: weighted gauge-graph isomorphism induces a transfer equivalence
Suppose finite spatial gauge complexes (G,β_s,β_t) and (G',β_s',β_t') have a bijection φ of vertices, oriented edges, spatial faces, and temporal ribbons, preserving incidences and all weights, including the periodic temporal seam. Relabel SU(2) link coordinates by φ and reverse orientation using inversion as necessary. Haar measure and closed-loop trace are invariant under this change of variables; thus there is a unitary pullback U_φ on gauge-invariant L² configuration Hilbert spaces. For transfer operators constructed from the same factorized Wilson action, `T_{G'} U_φ = U_φ T_G`. Therefore their eigenvalue multisets and normalized transfer excitation energies coincide. If G'=G this gives a commuting physical symmetry and selection rules. If G' differs this gives isospectral covariance between regulators, **not** symmetry on a fixed fibre. It does not yield a positive lower bound.

Caveat: a mere ambient geometric rotation without an exact weighted graph/complex isomorphism fails this theorem's hypotheses. Existing M55 finite-isometry audit did not certify nontrivial C5 graph automorphisms. This theorem neither requires nor proves a physical J lift.

## Theorem 4: symmetry/covariance does not force a gap
Let Hε=diag(0,ε) on a two-dimensional Hilbert space, ε>0, and let Rθ=diag(1,e^{iθ}); then `[Hε,Rθ]=0` for all θ yet gap(Hε)=ε→0. A nontrivial complex-structure action exists on a realified Hilbert space, and may be arranged in larger invariant representations, without changing this conclusion. More generally, exact finite group representation determines invariant sector decomposition, not a sector-independent lower spectral bound. To bound a gap one needs an *additional* uniform form inequality for H−E0 or a suitable connected-correlator estimate.

## Theorem 5: helical sampling is not Hamiltonian spectral evolution
For A>0 real, z2(τ)=A exp(2πipτ) has u=Acos(2πpτ), v=Asin(2πpτ). Thus `du/dv=-tan(2πpτ)` wherever defined, not the constant p. The mathematical parameter p is angular winding rate per τ, not a constant Cartesian velocity ratio. For static F(re^{iθ})=cos(mθ), `F(z2(τ))=cos(2πmpτ)`. This periodic frequency is present even for H=0, so cannot be identified with a transfer-Hamiltonian energy without a dynamical intertwiner and compatible time variable. This tightens Paper 3 §7's kinematic/dynamic separation in Remark 6.

## Theorem 6: lifted covariant family on symmetry-related gauge theories
Let a group Γ act on a family of (possibly distinct) weighted spatial complexes {G_x} with exact weighted isomorphisms φ_{g,x}:G_x→G_{gx}, compatible under composition. For each fibre define H_x=L²(SU(2)^{E_x})^gauge with transfer T_x. The pullbacks U_{g,x} satisfy `T_{gx}U_{g,x}=U_{g,x}T_x`. Thus Γ acts unitarily on an appropriate direct-integral Hilbert space, provided a Γ-invariant measure on the parameter family exists and measurability of pullbacks is established. This is a physically meaningful covariance statement that can hold without fixed-regulator C5 symmetry. It implies spectra are equal along Γ-orbits, but it does not imply a common strictly positive gap or any specified gap value. For Penrose hull applications one must prove that each group action preserves *the chosen coupling prescription* and corresponding gauge complexes.

## Conditional transfer positivity and actual Stage 26 implementation
For `S=Σ_tf β_s(f)(1−½ReTrW_f(t)) + Σ_te β_t(e)(1−½ReTr W^time_e(t))` on a finite time-periodic spatial graph, with β_t(e)>0, time-independent couplings and standard ribbons, use `T=P exp(−V/2) C_K exp(−V/2) P`. Wilson central factors have strictly positive SU(2) character Fourier coefficients for β>0; hence T≥0. Gauge-singlet correlators then have transfer spectral expansions. Full identification with Stage 26 **requires** verification of `stage7_checkpointed.setup_geometry` plaquette incidences, coupling positivity, time-independence and seam. Stage 26 scalar measurement definitions alone cannot verify D1.

## Spectral bridge sufficient to be genuinely gap-relevant (not yet proved)
Let H_x=−a_t^−1 log(T_x/λ0,x) on the vacuum-orthogonal physical sector. One would need a dimensionally consistent, volume-uniform, scale-aware quadratic-form bound `⟨ψ,H_x ψ⟩≥c(a)⟨ψ,A_x ψ⟩` for a positive operator A_x with inf spec A_x≥κ(a)>0, such that liminf_{a→0} c(a)κ(a)>0 after all limits, or a direct transfer contraction bound `||T_x/λ0,x||_{Ω⊥}≤exp(−a_t m*)`. A geometric J alone supplies neither A_x nor c(a); the auxiliary fundamental-representation connection Laplacian is not automatically A_x on pure-glue physical states.

## Nontrivial falsifiable alternative
A weaker meaningful target than a mass bound is to build a family of gauge-invariant scalar operators O(z) indexed by geometric z∈C² and prove `U_{g,x} O_x(z) U_{g,x}^{−1}=O_{gx}(gz)` and transfer covariance. This yields equality constraints on properly corresponding correlation matrices across symmetry-related regulators, and selection rules where actual fixed-fibre symmetry exists. The helix itself then selects a path z(τ), but the Euclidean time argument remains the transfer time; no kinematic phase is interpreted as an excitation energy.

## Decision gates
1. **D1, source**: obtain stage7_checkpointed.py; mechanically certify spatial/timelike plaquette classification and all β signs, t-translation and periodic seam. No new gauge-field sampling.
2. **Geometric action**: test φ_{g,x} is an actual isomorphism of weighted complexes; for M55, expect only conditional/cross-regulator covariance unless disproved.
3. **Observer intertwiner**: give explicit Φ mapping Paper 3 parent-space observables into gauge-invariant Wilson observables, preserving covariance; compare to existing Stage 30/35 operational choice without claiming uniqueness.
4. **Gap inequality**: construct/prove (or obstruct) a form comparison on the *physical* Hilbert space with controlled constants as volume and cutoff vary.
5. **Numerical work**: no additional Monte Carlo time before these mathematical gates; Stage 26 currently does not supply an admitted scalar mass or continuum ratio.

## Prior art
- K. Osterwalder and E. Seiler, “Gauge Field Theories on a Lattice,” Ann. Phys. 110 (1978) 440–471, DOI 10.1016/0003-4916(78)90039-8.
- P. Menotti and A. Pelissetto, “General Proof of Osterwalder-Schrader Positivity for the Wilson Action,” Commun. Math. Phys. 113 (1987) 369–373, DOI 10.1007/BF01221251.
- M. Creutz, “Gauge Fixing, the Transfer Matrix, and Confinement on a Lattice,” Phys. Rev. D 15 (1977) 1128.

All Theorems 1–6 above are general elementary deductions under specified assumptions and are not asserted to be novel. New physical claims would require satisfying their conditions for the original Penrose gauge model and proving the missing gap comparison.
