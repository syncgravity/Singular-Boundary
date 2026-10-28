# R3-IR — physical Gauss-projected source bridges and strong-field one-rhombus spectral scaling

**Date:** 2026-10-28. **Scope:** exact finite-graph Gauss-projected Feynman–Kac identities and a rigorous strong-magnetic single-rhombus asymptotic. **No Monte Carlo, no historical data changes.** **The multi-Penrose continuum interacting mass gap remains OPEN.**

## 1. Why the preceding full-link finite-temperature polymer theorem cannot directly be called a physical thermal theorem

The previous report `R3_IR_SOURCE_ROOTED_LINKED_POLYMERS_2026-10-28.md` correctly restricted its independent-link Brownian-loop expansion to the **full** Hilbert-space heat trace. The physical thermal trace `Tr(P_G e^{-βH})` is different for finite β, even when H and source insertions commute with the gauge group. The physical Gauss projector `P_G=∫_{SU(2)^V}R(g)dg` correlates link endpoints at shared vertices.

**Theorem GP-1 (exact physical twisted-bridge representation).** Let G be finite and H=H_E+V with H_E=Σ_e a_e(-Δ_e), a_e>0, and V a bounded, real, gauge-invariant multiplication potential. Denote by `k_{βa_e}(u,v)>0` the link electric heat kernel and by `B_e^{u→v}` the normalized Brownian bridge with that kernel. For vertex gauge transformations `g=(g_v)` put `(g·U)_e=g_{s(e)}U_eg_{t(e)}^{-1}`. Then

`Z_phys(β)=Tr(P_G e^{-βH})=∫dg∫dU [Π_e k_{βa_e}(U_e,(g·U)_e)] E_{⊗_e B_e^{U_e→(g·U)_e}} [exp(-∫_0^β V(U(τ))dτ)]`.

For bounded gauge-invariant multiplication insertions A at 0 and D at 0<t<β, insert `A(U(0))D(U(t))` inside the bridge expectation. This is an **exact identity**, not an estimate. The product bridge law exists **conditional on (g,U)**; integrating over g generally correlates the link processes, so the preceding full-link independent-loop polymer activities cannot be substituted directly into the physical trace.

**Proof.** Gauge invariance and Haar averaging give P_G as an orthogonal projection commuting with H and invariant multipliers. In the link configuration basis write the trace of `P_G e^{-βH}` as an integral of kernels `K^H_β(U,g·U)`. Feynman–Kac expresses each kernel as the positive product electric heat kernel multiplied by the independent-link bridge expectation of the potential. For sources, insert multiplication kernels at the appropriate path times. All operations are justified on the finite compact group, where heat kernels are smooth and positive and V,A,D are bounded.

The finite-volume full/physical vacuum correlations have the same β→∞ limit because the full operator has a unique strictly positive gauge-invariant vacuum; this passage is generally **not uniform in volume or cutoff**. The physical thermal bridge identity above does not by itself yield a product polymer expansion.

**Explicit spectral check (one open rhombus, b=0).** In the full four-link tensor product, the single-link -Δ eigenvalue j(j+1) has multiplicity (2j+1)², so
`Z_full(β)=[Σ_{j∈½N₀}(2j+1)² exp(-βa j(j+1))]^4`.
The physical one-rhombus Hilbert space consists of SU(2) class functions with one basis vector χ_j per spin and energy 4a j(j+1), hence
`Z_phys(β)=Σ_{j∈½N₀} exp(-4βa j(j+1))`.
The smallest full-space excited energy is 3a/4 with multiplicity 16; the physical first excitation is 3a with multiplicity 1. The source p=χ_{1/2}/2 has exact physical electric thermal correlation
`C_phys,β,t(p,p)= [1/(4Z_phys)] Σ_{j≥0}[ exp(-(β-t)E_j-t E_{j+1/2}) + exp(-(β-t)E_{j+1/2}-t E_j) ]`
where `E_j=4a j(j+1)` and zero thermal mean by center parity. As β→∞ at fixed t, this tends to `¼ exp(-3at)`. This makes the full-versus-physical thermal distinction explicit without any statistical data.

## 2. Theorem SF-1: nonperturbative strong-magnetic harmonic-oscillator limit for the genuine SU(2) rhombus

For one open spatial rhombus with all equal electric link coefficients a>0 and Wilson magnetic coefficient b≥0, the physical Hilbert space is `L²(SU(2))^Ad`. In the SU(2) class angle θ∈(0,π), normalized Haar density is proportional to sin²θ; the physical differential Hamiltonian is
`H_{a,b}= -a (d²/dθ²+2cotθ d/dθ)+b(1-cosθ)`.
The unitary multiplication `ψ(θ)→sinθ ψ(θ)` (including a harmless Haar normalization) gives the regular Dirichlet Sturm–Liouville operator
`h_{a,b}= -a d²/dθ² -a +b(1-cosθ)` on H¹₀(0,π).
At b=0 the eigenvalues are `a n(n+2)` with n=0,1,... (integer character index n=2j), as required by the Casimir normalization.

Set `ε=(a/b)^{1/4}` when b>0 and x=θ/ε. The rescaled operator `h_{a,b}/√(ab)` is unitarily equivalent to
`L_ε= -d²/dx²+W_ε(x)-ε²`, `W_ε(x)=(1-cos(εx))/ε²`, acting with Dirichlet conditions on `0<x<π/ε`.

**Lemma (uniform confinement).** For all x in the rescaled interval,
`(2/π²)x²≤W_ε(x)≤x²/2`.
Indeed `1-cos y=2sin²(y/2)`, while `sin u≥2u/π` for `0≤u≤π/2` and `1-cos y≤y²/2`. On each compact x interval `W_ε→x²/2` uniformly.

**Theorem SF-1.** Let E_k(a,b) be the ordered physical eigenvalues, k=0,1,..., counted with multiplicity. Then
`lim_{b/a→∞} E_k(a,b)/√(ab)=(4k+3)/√2`
for every fixed k, and therefore
`lim_{b/a→∞}(E_1-E_0)/√(ab)=2√2`.

**Complete min–max/compactness proof.** The comparison `W_ε≥(2/π²)x²` makes the unit ball of each bounded-energy spectral subspace uniformly tight: `∫_{x>R}|v|²≤ C/R²`. Each such normalized eigenvector has uniformly bounded H¹₀ norm, since the kinetic term is positive and `-ε²` is harmless. Extend functions by zero from (0,π/ε) to the half-line. Rellich compactness on (0,R) plus tail tightness yields strong L² subsequential convergence. Local uniform convergence of W_ε and weak lower semicontinuity of the kinetic and potential quadratic forms imply that each limiting orthonormal family has Rayleigh quotients bounded by the corresponding liminf of the approximating energies. Conversely compactly supported smooth approximations of the first k+1 eigenfunctions of `L₀=-d²/dx²+x²/2` give a k+1-dimensional test space whose maximal Rayleigh quotient tends to the k-th L₀ eigenvalue. The min–max principle, combined with the strong L² compactness preserving orthogonality, therefore gives convergence of each ordered eigenvalue (and, after choice of phases, each simple low eigenfunction) to the half-line Dirichlet oscillator. Its eigenfunctions are the *odd* Hermite oscillator states; with frequency `ω=1/√2`, the ordered eigenvalues are `(4k+3)ω`. Subtracting consecutive eigenvalues proves the gap limit.

**Significance.** At fixed a, the one-rhombus physical gap grows as `2√(2ab)` for b/a→∞. Therefore the failure of a weak-magnetic norm criterion as b/a→∞ is not evidence of gap closure even for a genuine interacting SU(2) Wilson model. This single-plaquette theorem does **not** imply a volume-uniform multi-Penrose gap or control collective excitations.

**Renormalized one-block reference.** The rescaled Dirichlet oscillator eigenfunctions give a finite-dimensional low-energy basis at fixed number of strong-coupling-scaled eigenlevels, in contrast with the previously proved failure of any fixed finite Haar-spin cutoff. At overlapping Penrose plaquettes, shared electric links couple holonomies and prevent a naive tensor product of these one-face oscillator modes. This is an exact geometric/dynamical obstruction to using independent plaquette harmonic oscillators as a global proof without additional estimates.

## 3. R3-IR critical dependency and integrity

- Physical Gauss-projected thermal trace: **independently proved exact twisted-bridge identity**.
- Difference between full and physical finite-β free traces: **independently proved exact character spectra**.
- One-rhombus strong-magnetic eigenvalue/gap asymptotic: **independently proved** for the physical single-loop regulator.
- Finite-temperature full-link polymer convergence: remains **published-KP theorem deduction**, *not* automatically physical-temperature clustering.
- Physical interacting Penrose vacuum source-inserted time decay uniformly in graph and refinement: **OPEN**.
- Nontrivial interacting spatial continuum reconstruction: **OPEN**.

**Next sharp theorem target:** prove a gauge-consistent multi-plaquette source-rooted block estimate that uses the renormalized strong-field oscillator scale and retains control of shared-link kinetic terms and Gauss projection. A proof certificate needs a positive physical source-transfer bound with uniform time/volume/refinement constants, or a genuine independent coercivity estimate; no inference from single-plaquette gaps or finite-temperature full-link KP clustering alone is valid.

Verification: `scripts/audit/verify_radial_and_gauss.py` checks exact radial conjugation, SU(2) free Casimir levels, the first two half-line oscillator eigenfunctions/eigenvalues and distinct full/physical electric partition multiplicities. No Monte Carlo, numerical diagonalization or historical data changes.
