# The Singular Boundary — strong-magnetic Gaussian Wilson variance and ultraviolet spectral escape

**Date:** 2026-10-28. **Classification:** independently proved exact results *for the finite-dimensional gauge-invariant tangent harmonic Hamiltonian*. No claim is made about a uniform semiclassical approximation to the actual nonlinear Penrose Wilson Hamiltonians, a nontrivial interacting continuum field, or the physical mass gap. No Monte Carlo or substitute historical samples were generated.

## 1. Why this calculation matters

The previous theorem `R3_IR_INTERACTING_VARIANCE_SPECTRAL_COMPACTNESS_2026-10-28.md` proved a *conditional* two-point compactness result if the interacting critical Wilson field with exponent α=1 has a uniform strictly positive and finite variance. It did not establish those variance bounds. Meanwhile the independent electric-only reference has a nontrivial α=1 Gaussian limit. Those facts do not authorize transferring this normalization to the strong-magnetic trajectory.

The exact collective Gaussian reference induced by shared Penrose links is a sharper nonperturbative *diagnostic*. It has an explicit field covariance and shows that its α=1 smeared Wilson field is trivial in vacuum norm along refinement. Remarkably, α=2 retains finite positive equal-time variance but loses all fixed-positive-time spectral weight. The distinction between equal-time field renormalization and finite-physical-energy excitation is essential.

## 2. Finite planar-face harmonic reference

Take a finite simply connected rhombus disk with F faces and E links, every face bounded by four distinct edges and each interior edge shared by at most two faces. Let B be its oriented F×E face-edge incidence matrix, L=BB^T, and M=B diag(a_e) B^T, with 0<a_min≤a_e≤a_max. The disk boundary makes L and M strictly positive definite. Each face has L_ff=4; the Gershgorin bound gives ||L||≤8. With 0<b_min≤b_f≤b_max, set V=diag(b_f)/8. The exact *quadratic tangent model* on 3F Lie-algebra face coordinates y_f∈R³, with the residual global SO(3) singlet restriction, is

H_quad = −Σ_fg M_fg ∇_{y_f}·∇_{y_g} + Σ_f b_f |y_f|²/8.

Its zero-mode vacuum is a normalized centered Gaussian. The quadratic approximation to the fundamental face trace is p_f^quad=1−|y_f|²/8, and the centered smeared field is

A_c = −(1/8) Σ_f c_f (|y_f|²−E|y_f|²),    c_f=h^(−α) A_f φ(x_f), A_f=h²σ_f.

A_c is invariant under global SO(3), hence is a legitimate observable of the physical singlet harmonic model. It is not an exact nonlinear Wilson multiplier away from the flat configuration. The harmonic model is exactly solvable for each finite disk but the approximation error for the growing, strongly magnetic nonlinear theory has NOT been controlled uniformly.

## 3. Theorem GV-1: exact covariance and two-sided variance bounds

Set D=M^(1/2) V M^(1/2) and Σ=(1/2) M^(1/2) D^(−1/2) M^(1/2), the covariance matrix of *one* Cartesian component of y. By three-component Wick contraction,

Var_quad(A_c)=(3/32) Σ_fg c_f c_g (Σ_fg)².  [GV-1]

In the special homogeneous case a_e=a, b_f=b, Σ=√(2a/b) L^(1/2), and

Var_quad(A_c)=(3a/(16b)) Σ_fg c_f c_g [L^(1/2)_{fg}]².  [GV-2]

The exact positive semidefinite matrix [L^(1/2)_{fg}²] has row sums Σ_g L^(1/2)_{fg}²=L_ff=4, so |Var|≤(3a/(4b))Σ_f c_f². For nonnegative c_f, off-diagonal terms are nonnegative, and (L^(1/2))_ff≥L_ff/√||L||≥√2. Hence Var≥(3a/(8b))Σ_f c_f².

The **inhomogeneous** model admits the same scaling bounds: since b_min I/8≤V≤b_max I/8 and x→x^(−1/2) is operator-monotone decreasing,

√(2/b_max) M^(1/2) ≤ Σ ≤ √(2/b_min) M^(1/2).

Since a_min L≤M≤a_max L, this yields Σ_ff≥2√(a_min/b_max) and ||Σ||²≤16a_max/b_min. Applying the Wick expression and 2|c_fc_g|≤c_f²+c_g² proves

(3a_min/(8b_max)) Σ_f c_f² ≤ Var_quad(A_c) ≤ (3a_max/(2b_min)) Σ_f c_f²,    c_f≥0.  [GV-3]

The upper bound holds for *arbitrary real* c_f. The lower bound is claimed only for nonnegative (or common-sign) weights; cancellations between signed c_f can prevent it.

## 4. Theorem GV-2: exact finite-energy and positive-time suppression

Diagonalize D=O diag(ν_i²) O^T with ν_i>0. The physical quadratic excitations created by A_c have energies E_ij=2(ν_i+ν_j). Put R=D^(−1/2)M^(1/2), C=diag(c), and K=O^T R C R^T O. The exact identity R^T R=V^(−1) implies ||K||_HS²≤(8/b_min)² Σ c_f².

The positive spectral measure of A_c in the harmonic vacuum is

μ_c(dE)=(3/128) Σ_ij ν_iν_j |K_ij|² δ_{2(ν_i+ν_j)}(dE).  [GV-4]

For every Λ,t>0, using ν_iν_j≤Λ²/16 whenever E_ij≤Λ and νe^(−2tν)≤1/(2et),

μ_c([0,Λ]) ≤ (3Λ²/(32 b_min²)) Σ_f c_f²,  [GV-5]

C_c(t)=∫e^(−tE)dμ_c(E) ≤ (3/(8e²t²b_min²)) Σ_f c_f².  [GV-6]

These bounds are **independent of F, the spectrum of L, and the smallest dual-graph eigenvalue**. They are exact harmonic-model estimates at arbitrary positive b_f, not perturbative word-level truncations.

## 5. Theorem GV-3: the strong-magnetic Penrose tangent field has no finite-variance nontrivial positive-time limit under a single power normalization

For a fixed compact physical support with nonzero **nonnegative** smooth φ, assume a_e∈[a_min,a_max] independent of h, b_f∈[b_0/h²,b_1/h²], and shape factors σ_-≤σ_f≤σ_+. Then

Σ_f c_f² = h^(2−2α) Σ_f A_f σ_f φ(x_f)².

Since a face-complete Penrose rhombus mesh has bounded aspect ratios and diameters O(h), the area sum converges to a positive finite quantity for nonzero φ as h→0. GV-3 implies

0<c_φ h^(4−2α) ≤ Var_quad(A_c) ≤ C_φ h^(4−2α).  [GV-7]

Thus α<2 forces variance→0, α=2 produces uniformly positive and finite equal-time variance, and α>2 makes the equal-time variance diverge. Meanwhile GV-5/GV-6 give

μ_c([0,Λ]) ≤ C_{φ,Λ} h^(6−2α),   C_c(t)≤ C_{φ,t} h^(6−2α).  [GV-8]

At α=2, low physical-energy spectral weight and fixed-positive-time correlation both tend to **zero as O(h²)** even though the equal-time variance remains nonzero. All spectral mass escapes to high excitation energies. For α=1, even the equal-time harmonic variance vanishes as O(h²). The α=2 normalization is *not* a nontrivial physical-time continuum field; at α≥3 the equal-time variance diverges. This is a fully controlled **Gaussian tangent-model obstruction** to a naive single-power scalar-field normalization with finite variance and nonzero fixed-time dynamics.

**Square-lattice exact control:** with uniform a and b=b_0/h² on a unit square of F=h^(−2) faces and c_f=1 (α=2), the exact trace identity gives Var_quad=3a/(4b_0) for every mesh; nevertheless μ([0,Λ])≤3Λ²h²/(32b_0²) and C(t)≤3h²/(8e²b_0²t²). No random sampling or numerical diagonalization is involved.

## 6. Limits and next genuine interacting obligation

The previous R3-IR physical-time theorem remains intact: if the **nonlinear** α=1 interacting Wilson field has two-sided variance and uniformly bounded first moment, it has a nonzero finite-energy subsequential two-point measure. Our new harmonic reference shows that this premise is *not* implied by strong-field quadratic localization. It does **not** disprove the premise for the exact Wilson theory, because replacing the nonlinear interacting dynamics on a growing Penrose patch by the Gaussian tangent model is not uniformly justified.

The next theorem must be an independently justified comparison of the nonlinear interacting Wilson spectral measure to a reference **at the physical scaling**, at least for bounded physically supported test sources. The comparison must control source renormalization, large-holonomy tails, nonlinear shared-link couplings, and excited-state energy transport simultaneously. An equal-time variance bound alone is not enough; a positive-time two-point lower bound or uniform spectral tightness is also needed. Alternatively, a rigorous upper variance bound o(1) for the true α=1 source would close a negative result and force reconsideration of the field choice.

**Evidence ledger:** GV-1/GV-2/GV-3 independently proved *for the separate Gaussian tangent Hamiltonian*. Applicability to nonlinear Penrose quantum continuum: open. No physical positive mass gap established or refuted.
