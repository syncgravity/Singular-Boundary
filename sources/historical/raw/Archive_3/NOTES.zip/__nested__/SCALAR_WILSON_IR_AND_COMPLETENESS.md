# The Singular Boundary: scalar Wilson infrared suppression and physical spectral completeness

**Date:** 2026-10-26. **Theory:** finite SU(2) 2+1 Hamiltonian gauge theories on genuine finite Penrose rhombus complexes; geometric coefficients as explicitly assumed below. **Status:** Theorems H, D, F and V below are proved under specified hypotheses; the all-low-spin continuum R3 gap is NOT proved.

## 0. Assumptions and precise observables

For any finite connected graph with simple quadrilateral faces and edge-face incidence ≤2, let

\[
H=\sum_{e}a_e(-\Delta_e)+\sum_f b_f(1-p_f),\qquad p_f=\frac12\operatorname{Tr}_{1/2}(W_f),\quad a_e>0,\ b_f\ge0.
\]

The Laplacians use the SU(2) normalization `-Δ χ_j=j(j+1)χ_j`. On the physical Hilbert space `H_phys=L²(SU(2)^E)^{SU(2)^V}`, the finite-volume ground state `Ω` is unique, smooth, real, gauge-invariant and strictly positive. Let `E0` be its energy, `Q=I-|Ω><Ω|`, `K=(H-E0)|_{Ω⊥}`, and `P_{(0,s]}` the energy spectral projector. For a gauge-invariant multiplier `A`, its positive spectral measure is `μ_A(I)=||P_I Q A Ω||²`; its variance is `V_A=||QAΩ||²`, and its first moment `M_A=∫ E dμ_A(E)`.

The continuum *coefficient trajectory* assumed for Theorem H is: uniform constants `0<a_-≤a_e(h)≤a_+`, `0≤b_f(h)≤β h^{-2}`, with `h` a physical edge length, and `a_-,a_+,β` independent of the finite patch and h. This holds for the *specified* dual-area geometric weights `a_e=g_3²/(2w_e), b_f=4/(g_3² A_f)`, where boundary edges use the one-sided area weight. **It has not been source-verified for the literal Stage 26 code.**

## 1. Theorem H — all-coupling high-spin scalar infrared projection bound

Let `j=1,2,...` be an integer spin, `d_j=2j+1`, `C_j=j(j+1)`, and take the real, bounded, contractible, center-neutral Wilson **scalar** multiplier

\[
A_{j,f}(U)=\frac{\chi_j(W_f(U))}{d_j},\qquad \|A_{j,f}\|_\infty\le1.
\]

Then `(-Δ_e)A_{j,f}=C_j A_{j,f}` on each of the four face edges, and, with `B_e=Σ_{g∋e}b_g`,

\[
\|P_{(0,s]}QA_{j,f}\Omega\|²
\le \frac{4 C_j\left(\sum_{e\in\partial f}\sqrt{a_e B_e}\right)^2}{(C_j\sum_{e\in\partial f}a_e-s)^2},
\quad 0<s<C_j\sum_{e\in\partial f}a_e.\tag{H1}
\]

*Proof.* First, the exact one-link variational inequality gives `a_e||∇_eΩ||²≤B_e`, for all nonnegative magnetic couplings, because deleting that electric link and all its incident nonnegative plaquettes leaves a Hamiltonian independent of the link, and Haar averaging a replacement constant link makes the deleted Wilson traces vanish. (This is the previously proved K1 lemma.) Second, for the normalized SU(2) character, `||∇_e A_{j,f}||∞≤√{C_j}`. To see this, on the representation space of dimension d, apply Cauchy–Schwarz to `d^{-1}Tr(π_j(g)dπ_j(X_a))` and use `Σ_a -dπ_j(X_a)^2=C_j I_d`. Third, the product rule yields

\[
(H-E_0-\kappa_{j,f})(A_{j,f}\Omega)
=-2\sum_{e\in\partial f}a_e\nabla_e A_{j,f}\cdot\nabla_e\Omega,
\quad\kappa_{j,f}=C_j\sum_{e\in\partial f}a_e.
\]

After vacuum projection, the residual norm is ≤`2√{C_j} Σ_e √(a_e B_e)` by K1. On the energy interval `(0,s]`, `|K-κ_{j,f}|≥κ_{j,f}-s`; the spectral theorem proves (H1).

If `κ_{j,f}≥2s`, then `B_e≤2βh^{-2}`, `Σ∂f a_e≥4a_-` and `Σ∂f √(a_eB_e)≤4√(2a_+ β)h^{-1}` give the explicit **patch-independent** estimate

\[
\boxed{\mu_{A_{j,f}}((0,s])\le
\frac{32a_+\beta}{a_-^2\,h^2\,j(j+1)}.}\tag{H2}
\]

For any nonempty face collection D with nonnegative weights ω_f summing to one, the scalar average `A_{j,D}=Σ_{f∈D} ω_f A_{j,f}` satisfies the **same bound** by the triangle inequality on spectral projections; the estimate is independent of the number of faces in D.

Fix a physical reference length `ℓ_0>0` and any `δ>0`, and take `j(h)=ceil((ℓ_0/h)^{1+δ})` (integer). At each fixed physical energy threshold `s`, for sufficiently small h the condition `κ≥2s` holds, and

\[
\boxed{\mu_{A_{j(h),D}}((0,s])\le
\frac{32a_+\beta}{a_-^2\ell_0^{2+2\delta}}h^{2\delta}.}\tag{H3}
\]

This is a genuine, all-magnetic-coupling, spatial-volume-uniform **low-energy spectral-weight upper bound along the prescribed refinement trajectory** for a restricted class of gauge-invariant scalar Wilson **multipliers**. It does not require the physical spectral gap.

**Interpretation / no overclaim.** These operators use increasing SU(2) spin `j(h)≫h^{-1}`. They are ultraviolet-filtered sources, not the original fundamental Wilson plaquette and not a demonstrated nontrivial renormalized continuum scalar field. Their variance may vanish; no cutoff-independent source normalization or spectral detection lower bound has been proved. (H3) also cannot bound their **inverse-energy** susceptibility without an independent control of arbitrarily small excitation energies. For an interacting physical scalar with fixed spin j, the right side of (H2) grows like `h^{-2}` and is useless as `h→0`.

## 2. Theorem V — nonperturbative variance–spectral-moment infrared tradeoff

For any centered bounded real gauge-invariant Wilson multiplier A and every `η>0`,

\[
\boxed{\mu_A((0,\eta])\ge
\left(V_A-\frac{M_A}{\eta}\right)_+.}\tag{V1}
\]

If `M_A>0`, its truncated static diagonal susceptibility satisfies

\[
\boxed{\chi^{<\eta}_{A,A}=2\int_{(0,\eta]}E^{-1}d\mu_A(E)
\ge \frac{2}{M_A}\left(V_A-\frac{M_A}{\eta}\right)_+^2.}\tag{V2}
\]

*Proof.* Markov gives `μ_A((η,∞))≤M_A/η`. Subtract from total spectral mass V_A to get V1. Cauchy–Schwarz on `(0,η]` implies `(μ_A((0,η]))²≤(∫E dμ_A)(∫E^{-1}dμ_A)≤ M_A∫E^{-1}dμ_A`; multiply by 2 and use V1. If `M_A=0`, the source has no excited spectral weight (since every finite-volume excited energy is positive), so V_A=0.

For the previously specified area-weighted **fundamental** scalar Wilson average `W_D=Σ_{f∈D}(A_f/𝒜_D)p_f`, the proved exact oscillator-strength estimate is `M_{W_D}≤2φ g_3² h²/𝒜_D`. V1 and V2 then imply: **unless** the ground-state variance of W_D shrinks appropriately, its low-energy weight or susceptibility cannot be small. This is a rigorous diagnostic in the opposite direction from a claimed infrared suppression. For the candidate rescaled field `Φ_{h,D}=(√𝒜_D/h)(W_D-⟨W_D⟩)`, `M_{Φ}≤2φ g_3²` but no low-energy upper bound follows from that first-moment information alone.

## 3. Theorem D — full Wilson-loop algebra detects every finite-volume physical state

Let `𝒜_G` be the unital complex *-algebra generated by the fundamental-representation Wilson traces of **all** closed paths in the finite spatial graph, allowing retracing, winding, products and noncontractible cycles. The uniform closure of `𝒜_G` is the continuous gauge-invariant algebra `C(SU(2)^E/SU(2)^V)` by SU(2) invariant trace theory (see Thierry Lévy, *Wilson loops in the light of spin networks*, J. Geom. Phys. 52 (2004), Thm. 3.1, https://doi.org/10.1016/j.geomphys.2004.04.003). Consequently,

\[
\boxed{\overline{\operatorname{span}\{A\Omega:A\in\mathcal A_G\}}
=\mathcal H_{\mathrm{phys}},\qquad
\overline{\operatorname{span}\{Q A\Omega:A\in\mathcal A_G\}}
=\Omega^\perp.}\tag{D1}
\]

*Proof.* The quotient is compact and the Wilson trace algebra is uniformly dense in its continuous functions. The positive continuous vacuum Ω induces `ν=|Ω|²dU` with full support. Continuous functions are dense in `L²(ν)`. Multiplication `f↦fΩ` is unitary from `L²(ν)` onto `H_phys`; therefore the Wilson algebra applied to Ω is dense. Applying Q yields the second identity. No gap or mixing hypothesis is needed.

Thus **all** Wilson traces and their products detect every nonzero physical finite-volume state in the weak sense that for some A, `⟨ψ,AΩ⟩≠0`. This is qualitative completeness, not a uniform lower bound on overlaps.

### Incompleteness of local scalar plaquette traces

(i) On a periodic torus, every contractible Wilson trace is center-neutral under nontrivial Z₂ one-form cocycles. Noncontractible Wilson traces can carry center charge; therefore contractible traces cannot generate states in those charged sectors from the neutral vacuum.

(ii) Even on a simply connected two-face region, the two elementary plaquette traces do not separate all physical configurations. Gauge-fix a spanning tree, leaving two loop holonomies U,V modulo simultaneous conjugation. Choose `U=iσ_z`; with `V=iσ_z` or `V=iσ_x`, both elementary traces are zero, but `Tr(UV)` is respectively `-2` or `0`. Any function of the two elementary traces gives the same value on the two configurations. A larger closed path carrying the mixed word UV distinguishes them. Products of just the two elementary traces are still insufficient.

(iii) Restricting an exact spatial symmetry to its scalar/trivial representation similarly misses other symmetry sectors; on the current finite M55 regulator an exact C5 automorphism is NOT certified, so no such scalar projection may be assumed without proof.

## 4. Theorem F — finite-window quantitative observability, but not uniformly controlled complexity

Fix finite G, h and energy threshold η>0. Since H has compact resolvent on the finite compact link manifold, `E=Ran P_{(0,η]}` is finite dimensional, of rank N. The density theorem implies we can find `A_1,...,A_N∈𝒜_G` with

\[
\boxed{\forall\psi\in E:\quad
\sum_{i=1}^N |\langle\psi,Q A_i\Omega\rangle|²\ge\tfrac14\|\psi\|².}\tag{F1}
\]

*Proof.* Choose an orthonormal basis ψ_i of E and pick A_i so that `||QA_iΩ-ψ_i||<1/(2√N)` by D1. For any ψ in E, the Euclidean norm of the N overlaps is within ≤√N·1/(2√N)=1/2 of the norm of its coordinates in the ψ_i basis. Thus its squared value is ≥1/4||ψ||².

**Crucial qualification:** The Wilson polynomial A_i, its norm, number of loops, loop diameters, representation degree and dependence on h, G and η are completely uncontrolled. N can grow. Hence F1 is a finite-volume existence statement, NOT the uniform physical observability or low-energy suppression estimate needed for a mass gap.

Indeed, if one had a uniform source family with `P_{≤η}(Σ_i w_i|QA_iΩ⟩⟨QA_iΩ|)P_{≤η}≥cP_{≤η}` and also `Σ_iw_i μ_{A_i}((0,s])≤C s^p` uniformly, then for a nonzero state below s, `c≤Cs^p` would force a positive gap. The second statement is precisely the nontrivial interacting infrared estimate not yet available for a uniformly observing family.

## 5. Theorem O — uniform infrared suppression of a complete normalized Wilson family *is itself* a gap inequality

Suppose one asserts that for **every** finite graph in a regulator family and **every** `A∈𝒜_G` with `||QAΩ||=1`,

\[\mu_A((0,s])\le C s^p,\qquad 0<s\le\eta,\tag{O1}\]

with `C,p,η>0` independent of graph and cutoff. Then no graph in the family can have a physical excitation energy `0<ε<min(η,C^{-1/p})`. **Proof:** given a normalized excited eigenvector ψ at energy ε, the density (D1) provides normalized Wilson-polynomial sources `QA_nΩ` converging to ψ. Therefore `μ_{A_n}((0,ε])→1`, and (O1) forces `1≤C ε^p`. The same argument works for any nonempty spectral projection below ε by approximating a unit vector in its range. Thus a uniform low-energy suppression bound over a **complete, normalized** Wilson family is already equivalent in strength to a uniform physical gap, not a genuinely weaker input. Conversely a gap ≥m forces `μ_A((0,s])=0` for every `s<m`. QED.

This exposes the essential proof-design issue: the **restricted** all-coupling bound H3 is noncircular and provable precisely because the high-spin family is *not* uniformly complete/observable in the infrared; enlarging H3 to every low-energy-detecting normalized scalar Wilson polynomial is the unresolved dynamical gap problem.

## 6. R2 and the status of the purported renormalized continuum scalar

The high-spin bound H3 is stated in fixed physical energy units for a specified `a_e(h), b_f(h)` trajectory. It is not quantum continuum reconstruction and supplies neither convergence of `A_{j(h),D}Ω_{h,L}` nor a nonzero limiting variance. The fundamental area-averaged field `Φ_{h,D}` has a uniform first spectral moment but its variance and low-energy spectral weight remain uncontrolled. No independence from boundary topology is implied beyond the local bounds and admitted edge coefficients, and the literal Stage 26 action builder has not been verified.

Completion of scalar R3 + R2 requires *all* of: (1) a nontrivial physically normalized low-spin/multiloop scalar family, with continuum distributions or spectral measures; (2) an independent IR *upper* estimate for that family, rather than a first-moment upper bound or time-derivative trick; (3) quantitative low-energy observability across all gauge-invariant sectors, with explicit treatment of winding loops, center charge, and boundary modes; (4) uniform control of constants as h→0 and L→∞. None is proved by H/V/D/F, C5 covariance, or Paper 3's J.

## Sources

- Thierry Lévy, *Wilson loops in the light of spin networks*, J. Geom. Phys. **52** (2004), 382–397, doi:10.1016/j.geomphys.2004.04.003 (Wilson trace algebra density).
- Previous project memo: `/mnt/data/R3_refinement_local_spectral_2026_10_26/FORMAL_THEOREMS.md` (K1 and first-moment S1 under the *specified* action); proofs reproduced or referenced with explicit hypotheses above.
- Previous project memo: `/mnt/data/R3_full_proof_2026_10_26/R3_THEOREM_OBSTRUCTION_AND_MULTISCALE_GATE.md` (center one-form selection and exact character mixing).

**Scientific conclusion:** A nontrivial mathematical upper estimate now exists for bounded high-spin scalar Wilson multipliers, and the full Wilson algebra is provably complete at finite volume. These facts do not jointly prove a physical gap: the infrared-suppressed family is not an established continuum scalar detector, and the complete family has no regulator-uniform quantitative infrared bound. The interacting center-neutral low-spin problem remains open.
