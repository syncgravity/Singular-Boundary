# R3-IR-598 — Conditional electric marginal Ward identity and mixed-metric radial-closure audit

Date 2026-10-31. The previous branch proposed a scalar radial score Ward identity with constant effective kinetic coefficient A_f, then R3-IR-596–597 used a scalar Sturm–Liouville equation for a positive deleted-vacuum amplitude. **This report identifies and isolates an unverified hypothesis in applying those lemmas to the actual rooted inverse-Whitney Penrose Hamiltonian.**

## General exact identity

Consider a compact SU(2) link configuration space with Haar product measure, symmetric nonpositive diffusion operator L=Σ_{e,e',a} K_{ee'}X_{e,a}X_{e',a}, for fixed symmetric positive K and divergence-free left-invariant vector fields X, and a strictly positive real vacuum Ω with density ρ=Ω². Define p=p_f∈[-1,1] and the carré du champ Γ(F,G)=ΣK_{ee'}(X_eF)·(X_e'G). Let w(p) denote the probability density of p under ρdHaar, and define the conditional quantities

a(p)=E_ρ[Γ(p,p)|p], b(p)=E_ρ[Lp|p], c(p)=E_ρ[Γ(p,log Ω)|p].

For every smooth compactly supported scalar test function φ(p), the chain rule and Haar integration by parts give ∫ρ Lφ(p)=∫ρ[φ''(p)Γ(p,p)+φ'(p)Lp] =−2∫ρ φ'(p)Γ(p,logΩ). Disintegrating with respect to p and integrating the first term once yields the **exact distributional marginal Ward relation** (a(p)w(p))'=(b(p)+2c(p))w(p). For field-dependent rooted transports, an analogous identity needs the actual self-adjoint divergence-form electric operator and associated Γ and L, not blindly the fixed-K expression.

Writing w(p)=w_Haar(p) ψ(p)² gives

2(log ψ)'(p)=[b(p)+2c(p)−a'(p)]/a(p)−(log w_Haar)'(p)

where coefficients are defined and a>0. The simpler claimed scalar radial score equation follows only if the drift/kinetic terms are separately identified and reduce in the required way.

## Explicit mixed-link obstruction to automatic radial closure

On SU(2)² take p=Re(UV), K=[[1,0.3],[0.3,1]], left invariant Lie fields with generator iσ_a/2. At configurations (U,V)=(1,i) and (i,j) (unit quaternions), both have p=0. In the first case (X_U p)·(X_V p)=+1/4 and Γ(p)=0.65; in the second case the cross gradient is −1/4 and Γ(p)=0.35. This exact elementary computation proves Γ(p) need not be determined by p alone when cross-link electric couplings are present.

**Scope limitation:** this toy two-link K is NOT the actual Penrose rooted-Whitney operator. Its mixed-link obstruction does not disprove the previous branch's exact Penrose scalar Ward claim; a special rooted transport/gauge-invariant cancellation could restore closure. It demonstrates that such a cancellation needs proof against the full actual operator, including tree-edge electric derivatives.

## Consequences

Before applying radial Harnack/integrated forcing comparison (R3-IR-596, 597), independently derive the precise face conditional carré du champ and drift for the **actual** rooted inverse-Whitney Gauss Hamiltonian. Verify whether a(p) and b(p) reduce to a constant multiple of the SU(2) class radial generator after conditioning. Otherwise replace the earlier scalar radial ODE by the variable-coefficient marginal equation, and derive appropriate one-sided score controls including a'(p), b(p), and c(p). The interacting-vacuum uniform estimate and continuum Yang–Mills mass gap remain unproved.

Reproducible exact quaternion calculation: Library /The Singular Boundary/Source/audit_mixed_electric_radial_closure.py; results /The Singular Boundary/Source/mixed_electric_radial_closure_audit_2026-10-31.json.
