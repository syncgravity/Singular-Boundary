# Exact conjugation-selection rule and covariant conditional force balance

**2026-10-31 | Finite original-link SU(2) theorem.** Does not close the current or continuum gap.

Consider the smooth strictly positive Gauss-invariant ground state Ω for H=-Σ_e a_e Δ_e+V, with V a sum of trace-Wilson plaquette terms and one target f deleted. Fix a target edge e, p=Tr W_f/2, and orthonormal left-invariant generators X_a on e. Write v_a=X_a log Ω, F_a=X_a V and η_a=X_a p; let ℒ=Σ_e a_e(Δ_e+2∇ logΩ·∇) and ν=Ω²μ, ρ=p_*ν.

**Selection rule.** Simultaneous global conjugation U_k↦g U_k g⁻¹ preserves p, Ω, V, μ and ν. The triples (v_a)_a, (F_a)_a and (η_a)_a transform in the adjoint three-dimensional SO(3) representation. Thus for every -1<p<1, Eν[v_a|p]=Eν[F_a|p]=Eν[η_a|p]=0. This is an exact conditional equality: averaging over all g∈SU(2) projects every adjoint vector to zero. It does not imply the invariant contraction Eν[Σ_a η_a v_a|p] vanishes.

**Covariant force balance.** The original-link score identity ℒv_a=F_a together with reversibility implies, for every smooth test φ(p),

∫φ(p) Σ_a η_a F_a dν = -∫φ'(p)Σ_a η_a Γ(p,v_a)dν -∫φ(p)Σ_a Γ(η_a,v_a)dν.

Define scalar conditional functions B(p)=Eν[Σ_aη_aF_a|p], K(p)=Eν[Σ_a η_aΓ(p,v_a)|p], L(p)=Eν[Σ_aΓ(η_a,v_a)|p]. Thus **(ρK)'=ρ(B+L)** distributionally on (-1,1). This preserves the local Wilson forcing in B=-Σ_{g≠f:e∈∂g}b_g Eν[∇_e p_f·∇_e p_g|p]. The L term carries second derivatives of the true vacuum; neglecting it would be unjustified. The identity does not close by itself because K and L are unknown conditional responses. This is a rigorously projected *original-link* identity and does not claim a sign for B, K, L, or the target signed current.

**Independent symbolic check.** For an engineered central rotor Ω∝exp(λp), V=λ²(1-p²)/4−3λp/4+C, κ=(1-p²)/4, we obtain B=κ V'(p), K=λκκ'/2 and L=λ(p²+2)/16. With ρ∝√(1-p²)exp(2λp), symbolic differentiation verifies (ρK)'−ρ(B+L)=0 identically. This model is *not* a completed Wilson cage. See verify.py and result.json.

**Open:** Wilson-specific control of K and L, one-sided center score and anti-depletion, regulator-uniform sup_f T_f,h=o(h^-1/4), and continuum Yang–Mills mass gap. This theorem adds a symmetry constraint and nontrivial covariant response equation; it does **not** provide the required numerical bound.