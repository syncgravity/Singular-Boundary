# Inverse-positive-rotor obstruction to deducing the signed flux from fiber identities alone

**2026-10-30 — status:** exact constructive counterexample *within smooth center-symmetric SU(2) scalar rotor Hamiltonians*, **not** a counterexample to the original-link completed-cage Wilson ground state. Extends the archived EF-3 qualitative rotor counterexample by proving the adverse signed-current budget can be prescribed arbitrarily while the exact eigen-equation and both half-fiber sum rules hold.

## Proposition

Fix an electric coefficient \(A>0\). For every \(L>0\), there is a smooth, bounded, nonnegative, center-even class potential \(V_L\) on SU(2) whose strictly positive unique normalized ground state has all the following properties:

1. Its radial amplitude \(\Psi_L(u)\) is smooth and positive at both SU(2) centers and symmetric under \(u\mapsto\pi-u\).
2. It solves exactly
\[
-\frac A4\left(\Psi_L''+2\cot u\,\Psi_L'\right)+V_L(u)\Psi_L=E_L\Psi_L.
\]
3. For \(D_L=V_L-E_L\), both exact half-fiber identities hold:
\[
\int_0^{\pi/2}\sin^2u\,D_L(u)\Psi_L(u)\,du=0,\qquad
\int_0^{\pi/2}\sin^2u\,D_L(u)\,du
=\frac A4\int_0^{\pi/2}\sin^2u(\partial_u\log\Psi_L)^2du\ge0.
\]
4. Its adverse one-sided budget satisfies **exactly**
\[
\mathfrak T_L=\int_0^{\pi/2}[\partial_u\log\Psi_L(u)]_+du=L.
\]

Thus positivity, center symmetry, the exact radial eigen-equation, endpoint smoothness, the two half-fiber sum rules and their cumulative-flux formulation do **not**, by themselves, imply any universal finite upper bound on the adverse score budget.

## Construction and proof

Fix \(0<a<\pi/8\), and choose \(\eta\in C^\infty([0,\infty))\) nondecreasing, equal to 0 on \([0,1]\) and equal to 1 on \([2,\infty)\), with all derivatives vanishing at the flat joins. Set \(\varepsilon=e^{-L}\). On \(0\le u\le\pi/2\), define
\[
\widetilde\Psi_L(u)=\varepsilon+(1-\varepsilon)\eta(u/a).
\]
Extend to \(\pi/2\le u\le\pi\) by \(\widetilde\Psi_L(\pi-u)\) and normalize in the SU(2) Haar radial norm \( (2/\pi)\int_0^\pi\sin^2u\,\Psi^2du=1\). The normalized \(\Psi_L\) is strictly positive, smooth, even at both center coordinate charts (it is constant near each center), and constant near the equator.

Let \(\mathcal D=\partial_u^2+2\cot u\,\partial_u\), the SU(2) class Laplacian in the convention \(-\Delta\chi_{1/2}=3\chi_{1/2}/4\) after multiplying \(\mathcal D\) by \(1/4\). Define
\[
Q_L(u)=\frac A4\frac{\mathcal D\Psi_L(u)}{\Psi_L(u)}.
\]
The quotient is smooth and bounded because the numerator vanishes near both centers, \(\Psi_L>0\), and the profile has flat joins. It obeys \(Q_L(\pi-u)=Q_L(u)\). Choose \(E_L=\max\{0,-\min Q_L\}\) and put \(V_L=Q_L+E_L\ge0\), still smooth, bounded and center even. The claimed equation holds identically.

The scalar SU(2) Schrödinger operator \(H_L=-(A/4)\mathcal D+V_L\) on class functions has \(\Psi_L\) as its strictly positive eigenfunction with energy \(E_L\). It is the **unique ground state**: for every smooth \(g\),
\[
\langle \Psi_L g,(H_L-E_L)\Psi_L g\rangle
=\frac A4\int_0^\pi\frac{2\sin^2u}{\pi}\Psi_L(u)^2|g'(u)|^2du\ge0.
\]
Positivity improving and connectedness yield uniqueness. Equivalently, extend \(V_L\) to the full SU(2) group as a central potential; the same ground-state transform for arbitrary group test functions proves the positive class eigenfunction is the unique full-group ground state.

The divergence form of the eigen-equation and endpoint/midpoint zero-flux conditions prove both half-fiber identities exactly as in FES-1 and FES-2. Finally, \(\partial_u\Psi_L\ge0\) on \(0<u<\pi/2\), and \(\Psi_L(0)=c_L\varepsilon\), \(\Psi_L(\pi/2)=c_L\), where \(c_L>0\) is the common normalization. Therefore
\[
\mathfrak T_L
=\log\Psi_L(\pi/2)-\log\Psi_L(0)
=\log(1/\varepsilon)=L.
\]
This concludes the construction.

## Logical limit and next Wilson-specific gate

This construction is **not** an SU(2) Wilson face-deleted Hamiltonian: \(V_L\) is an engineered center-even rotor potential and should not be substituted for the original plaquette interactions. The prior archived EF-3 also supplies a center-avoiding rotor; this theorem strengthens that model-class objection from a qualitative failure of a Haar-order cap estimate to arbitrary prescribed adverse current under the full set of formal fiber identities.

The only credible route to the actual completed Penrose Wilson estimate must use *additional structure of the conditional state* \(\Phi_f\) or Wilson link interactions to prove quantitative signed cumulative-flux control. Neither the abstract scalar fiber equation nor its half-interval sum rules is sufficient. In particular one must not promote the structural identities in R3-IR-384 to 386 into an unconditional \(o(h^{-1/4})\) theorem.

**Proof status:** exact constructed-model obstruction; interacting nonlinear Wilson current and physical continuum gap remain OPEN.
