# Shared-link incidence bound and the unclosed transverse response
Date: 2026-10-30
Status: proved pointwise magnetic-gradient bound for finite SU(2) link lattice; uniform interacting deleted-vacuum response OPEN.

## Setup
A finite oriented link complex with SU(2) variables U_e. Each face g uses each boundary link at most once. Magnetic potential after deleting f: V_f^-(U)=sum_{g neq f} b_g(1-p_g(U)), with p_g=Tr(U_g)/2 and b_g>=0. Let a_e>0, A_f=sum_{e in boundary f} a_e, u_f=arccos p_f, and Gamma_a(F,G)=sum_e a_e <grad_e F,grad_e G>. All gradients use round-unit-S3 normalization.

## Lemma (exact local magnetic angular derivative bound)
On the regular-angle region 0<u_f<pi, define the weighted horizontal derivative X_f G=Gamma_a(u_f,G)/A_f. Since Gamma_a(u_f,u_f)=A_f, we have X_f u_f=1. Furthermore
|X_f V_f^-| <= L_f:= (1/A_f) sum_{e in boundary f} a_e sum_{g neq f: e in boundary g} b_g.
Proof: |grad_e u_f|=1 for e in boundary f; |grad_e p_g|<=1 when e occurs once in g; triangle inequality gives the expression. Edges outside boundary f contribute zero. This is an exact finite-combinatorial bound retaining all neighboring faces, without assuming link independence. It is not a bound on the derivative of the effective radial potential W_f or the signed current C_f.

## Corollary (bounded weighted local incidence)
If every boundary edge of f belongs to at most q other faces and b_g<=b_max, then L_f<=q b_max. This controls explicit magnetic variation, but not any conditional fiber kinetic-energy variation. Degenerate or repeated-edge face words require the derivative estimate to be modified.

## Distinct unresolved terms
The exact effective radial potential is W_f(u)=E_{Haar fiber}[V_f^- phi_f^2 + sum_e a_e|grad_e phi_f|^2 | u], phi_f=Omega_f^-/psi_f(u). Differentiating W_f under radial transport introduces conditional-density response and kinetic-energy response, beyond X_f V_f^-. Consequently |X_f V_f^-|<=L_f gives no estimate on W_f'(u), on the cumulative radial force int_0^u sin²(t)(W_f(t)-E_f)psi_f(t)dt, or on K_f(delta). The interacting quantum ground state cannot be replaced by classical product Haar/Gibbs samples.

## Stage 26 provenance check
Inspected uploaded penrose_seed101_stage26.zip. latest.json records kind=penrose seed=101 sweep=12000 beta_ref=3.5 nt=20 and the npz records contain direct_timeslice, direct_product, conditional, conditional_onepoint and related Monte Carlo diagnostics. They do not include the quantum deleted-vacuum conditional fiber score, psi_f, or W_f. Hence no claim about the latter follows from those archives without an additional validated bridge.

## Needed next step
Establish a uniform estimate for transverse response using the actual full Hamiltonian and geometry. A candidate route is an operator commutator/ground-state transform controlling fiber conditional transport at fixed face angle. Any bound must preserve scaling in h and f and track boundary conditions and possible topological constraints. Remains OPEN.
