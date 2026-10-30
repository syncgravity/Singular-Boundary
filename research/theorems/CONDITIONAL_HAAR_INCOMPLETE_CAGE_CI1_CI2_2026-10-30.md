# Conditional Haar independence for incomplete magnetic cages (CI-1/CI-2)

**Source:** 2026-10-30 project handoff `THEOREM.md`. **Classification:** finite-volume exact theorem, source proof transcribed and indexed here; independent external peer review pending. **Does not apply to completed cages.**

## Model and hypothesis

A finite simply connected open-boundary planar rhombus disk with original-link Hilbert space (L^2(SU(2)^E)) restricted to the original full vertex Gauss group, with target face (f) magnetically deleted and Hamiltonian
[
H_f^-=sum_e a_e(-\Delta_e)+b\sum_{q\in Q}c_q(1-p_q),\quad p_q=\tfrac12\operatorname{Tr}W_q,
]
where (a_e,c_q>0) and (b\ge1). Link-Haar measure is normalized; (-\Delta\chi_j=j(j+1)\chi_j). Build the retained magnetic-support graph by joining faces sharing an **original link** (not merely a vertex). Let (E_C) be the union of links for a retained connected component (C), (S_C=E_C\cap\partial f). Hypothesis **IC:** for every component (C), (S_C\ne\partial f).

## CI-1: exact Haar and retained-trace independence

For the actual positive Gauss-invariant ground state (Omega_f^-), every bounded retained-plaquette-trace measurable (F(P)), and every nontrivial SU(2) character (chi_j), (j>0),
[
\mathbb E_{|\Omega_f^-|^2}[F(P)\chi_j(W_f)]=0.
]
Consequently (\mathscr L(p_f\mid P)=\mathscr L_{\mathrm{Haar}}(p_f)) almost surely, even in strong coupling. In particular (\mathbb E[F(P)\mid p_f\in B]=\mathbb E[F(P)]) whenever the target trace event (B) has positive Haar measure. The marginal amplitude is (psi_f\equiv1), and the **radial marginal** score current and positive budget vanish.

**Proof:** On the unreduced original-link space, retained magnetic components have disjoint link supports. The full Hamiltonian is a tensor sum of the elliptic component Hamiltonians plus free-link Casimirs. Their unique strictly positive ground-state product is invariant under the original Gauss group, hence is also the physical ground state. If a target link is free, integration over it gives target Haar even when weighted by (F(P)). Otherwise choose a component containing a nonempty proper subset of the four-link target cycle. That proper subset has a vertex with exactly one of its target links incident. A gauge rotation at that vertex **acting only on that component** preserves the component vacuum and all retained traces, but inserts one group element into (W_f). Full Haar averaging annihilates every nontrivial representation. Since the target pushforward is conjugation invariant, Peter–Weyl density of characters gives Haar conditional class law. This does not imply independence of the full based holonomy from gauge-variant observables.

## CI-2: retained component conditional defect bound

If (a_e\le a_+), (c_-\le c_q\le c_+), and (m=|C(q)|), then for any target-trace event (B) of positive Haar mass:
[
\mathbb E[1-p_q\mid p_f\in B]\le\frac{m(3a_++12c_+)}{c_-\sqrt b}.
]
Markov bounds the conditional tail at threshold (delta>0) by the RHS divided by (delta), capped at one. For a collar of (k) retained faces each in a component of at most (M) faces, the corresponding union-bound probability is at most (kM(3a_++12c_+)/(\delta c_-\sqrt b)), capped at one.

**Proof sketch with constants:** In the component use trial amplitude proportional to (\exp(\lambda\sum_{r\in C}p_r)). Free planar face-coordinate Haar and SU(2) integration by parts bound trial electric energy by (3\lambda\sum_{r\in C}A_r/4), (A_r\le4a_+), and the trial magnetic expectation by (12b\sum_{r\in C}c_r/\lambda). Taking (lambda=\sqrt b), positivity gives (bc_q\mathbb E(1-p_q)\le E_0(H_C)\le m(3a_++12c_+)\sqrt b). CI-1 transfers this **without a rare-cap denominator** to conditioning on (B). Then apply Markov and union bounds.

## Rigorous scope and verification provenance

This estimate grows with (m), so it is volume uniform only for bounded retained components. The proof does not apply to completed connected cages; no nonlinear current estimate there has been shown. The source handoff lists `verify_component_conditional.py`, `verify_su2_weighted_haar.py`, `verify_local_wilson_defect.py`, `verify_conditional_obstruction.py` and CSV certificates; these companion bytes are **not yet verified as present in Git**. Do not record those verifications as repository reproducible until imported.

**Research gate:** control the true physical nonlinear completed-cage target-dependent conditional state or signed score current, including collective modes, uniformly over Penrose bulk faces:
[
\sup_{f\in D_R}\mathfrak T_{f,h}=o(h^{-1/4}).
]
This is open. The interacting continuum mass gap and reconstruction are also open.
