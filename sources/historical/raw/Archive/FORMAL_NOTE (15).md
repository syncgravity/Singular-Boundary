# Thin-support diluted Wilson free energy: local heat-bath theorem and unresolved global estimate

Date: 2026-10-26. Status: finite-volume exact identities and conditional theorems; no claimed continuum-uniform full Penrose estimate.

## Setup
Let G be any finite bounded-incidence spatial–temporal cell complex with SU(2) link variables and Wilson action S_β=∑_p β_p d_p, d_p=1−(1/2)Tr W_p, β_p∈[c_-λ,c_+λ], λ→∞. Select a sparse set J of links, with no plaquette containing two of them. Let P(J) denote incident plaquettes, and β^(t)_p=(1−t)β_p on P(J), other couplings unchanged, 0≤t≤θ<1.

## Theorem 1: local thermal–frustration identity and inequality
Condition on all links except one link e. Write the incident action S_e(u)=B−u·k, B=∑_{p∋e}β_p, k=∑_{p∋e}β_p q_{ep}, κ=|k|, F=B−κ. Then the conditional probability density is e^{κ n·u}/z(κ), z(κ)=2I_1(κ)/κ, and
 E[S_e | exterior] = F + κ(1−m(κ)), m(κ)=I_2(κ)/I_1(κ).
Furthermore 0≤κ(1−m(κ))≤C_SU2 for a universal finite C_SU2; follows by continuity at 0, boundedness on compact intervals and its limit 3/2 as κ→∞.
Since d_p≥0,
 β_p E[d_p | exterior] ≤ F_e + C_SU2, for every incident p.
Consequently β_p E[d_p] ≤ E[F_e]+C_SU2.
This bound remains valid after any selective dilution and includes temporal plaquettes.

## Theorem 2: exact equivalence to a selectively diluted free energy
For sparse J, let η_β be the exterior marginal obtained by integrating J. Under proportional dilution by θ on all incident plaquettes,
 Z(β')/Z(β) = E_{η_β} exp(θ∑_{e∈J}F_e) · ∏_{e∈J} exp(ℓ((1−θ)κ_e)−ℓ(κ_e)) inside the expectation,
 ℓ(x)=log z(x)−x.
The quantity ℓ((1−θ)x)−ℓ(x) is nonnegative and bounded above by a finite C_θ for x≥0 (since z(x)e^{-x} is decreasing with polynomial behavior). Thus
 E_{η_β} exp(θ∑F_e) ≤ Z(β')/Z(β) ≤ e^{C_θ|J|} E_{η_β} exp(θ∑F_e).
[Here the left bound follows from the nonnegative correction; right from its upper bound.]
The exact derivative representation is
 log Z(β')/Z(β) = ∫_0^θ∑_{p∈P(J)}β_p E_{β^(t)}[d_p]dt.
Hence a uniform |J| log λ bound on the full free-energy correction is essentially equivalent to an exponential-moment bound for the correlated exterior frustration. The conditional heat-bath identity alone is not a proof of the moment bound.

## A genuine conditional thin-support theorem
If, under *every* diluted measure β^(t), the joint frustration obeys
 ∑_{e∈J} E_{β^(t)} F_e ≤ C_F |J|(1+log λ),
then the local thermal–frustration inequality and bounded incidence imply
 log[Z(β')/Z(β)] ≤ θ C'|J|(1+log λ).
To obtain the stronger defect inequality itself for all incident plaquettes, use β_p E d_p ≤ E F_e+C on each selected link e, and sum over e (incident sets disjoint):
 ∑_{p∈P(J)} E_{β^(t)} d_p ≤ (D/(c'_− λ)) (∑_{e∈J} E F_e+C|J|).
This is a conditional implication; the joint frustration bound is open for Penrose spacetime Wilson theory.

## Obstruction to uniform exterior-wise local comparison
For two incident plaquettes with equal coefficients λ and opposite preferred quaternion directions, k=0, F=2λ, and the conditional link distribution is Haar. The target plaquette defect then has conditional mean 1, independent of λ. Thus no exterior-uniform bound E[d_p | exterior] = O(log λ/λ) can hold. This does not disprove an *unconditional* Gibbs-average estimate.

## Literature boundary
Faria da Veiga and O'Carroll, 'On Yang-Mills Stability Bounds and Plaquette Field Generating Function' (Reports on Mathematical Physics 95, 2025), establish thermodynamic/UV stability and certain scaled plaquette-field generating-function bounds on hypercubic lattices using regular-lattice multireflection methods; their theorem is not directly a Penrose thin-support selective-dilution theorem. See DOI 10.1016/S0034-4877(25)00035-7.

## Honest conclusion
No noncircular cutoff-uniform regionwise diluted free-energy bound on arbitrary thin spacetime supports is proved here. The result is an exact local thermal–frustration reduction, a sharp exterior counterexample, and a precise independent joint-frustration hypothesis sufficient to close the localized estimate. Ultraviolet polymer convergence and the R3/R2 mass gap remain open.
