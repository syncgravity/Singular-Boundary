# Independent local insertion free-energy estimates: scope and obstruction

Date: 2026-10-26

## Model
Finite oriented cell complex, compact normalized SU(2) Haar link measure. Plaquette action S=Σ_p β_p d(W_p), d(W)=1-(Tr W)/2 ∈[0,2], 0≤β_p≤b λ. I set of m internal links, P(I) incident plaquettes, N=|P(I)|≤D m. S=S_out(v)+S_I(u;v). Z_I(v)=∫_I exp(-S_I(u;v))du, a=E_{ρ_I} Z_I(v), ρ_I(dv)=Z_cav^{-1}e^{-S_out(v)}dv, insertion free energy F_I=-log a.

## Theorem 1: unconditional universal local insertion bound
Because 0≤S_I≤2 Σ_{p∈P(I)}β_p, Z_I(v)≥exp[-2 Σ β_p] for all v. Hence 0≤F_I≤2 Σ_{p∈P(I)}β_p≤2b λD m. No dependence on ambient volume. Also F_I≤E_{ρ_I}[-log Z_I(v)] (Jensen), but this is not a useful absolute improvement without input on exterior backgrounds.

## Theorem 2: localized variational improvement by compatible minimizer
Let E_I(v)=min_u S_I(u;v). At a minimizing configuration u_*(v), all internal link directional first derivatives vanish. Bounded incidence and β_p≤bλ imply quadratic upper bound S_I(u_* exp X;v)≤E_I(v)+C b λ Σ_{e∈I}|X_e|² for |X_e|≤r_0 and all v; can also obtain weaker bound with r∼1/λ without stationarity. Integrating product SU(2) balls radius c λ^-1/2 (λ≥1) gives Z_I(v)≥c_0^m λ^-3m/2 exp[-E_I(v)-C_0 m]. Consequently
 a ≥ c_0^m λ^-3m/2 e^-C_0m E_{ρ_I} exp[-E_I(v)]
 and
 F_I ≤ (3m/2)log λ+C_1m -log E_{ρ_I}exp[-E_I(v)].
 In particular if there exists event B of exterior fields with ρ_I(B)≥e^-αm and sup_{v∈B}E_I(v)≤ε m(1+log λ), then
 F_I≤(3m/2)log λ+(C_1+α)m+ε m(1+log λ).
 Conditions do not assume any Gibbs insertion ratio, but proving such a cavity-exterior event is nontrivial for arbitrary thin I. In the exact flat extension case E_I(v)=0 for ρ_I-a.e. v, obtains F_I≤(3m/2)log λ+C_1m.

## Theorem 3: relative free-energy bound with an external collar
Let Q⊇I have M links and P(Q) all incident plaquettes. For the same cavity rho construction based on I, suppose every exterior field in a set B has a compatible repair u on I with total incident action ≤E0 (irrespective of how the exterior was generated). Then as above F_I≤E0+(3/2)m log λ+C m -log ρ_I(B). This makes explicit the energy/entropy tradeoff. Replacing I with an enlarged collar Q requires controlling the associated new cavity probability and does not on its own prove logarithmic scaling.

## Exact nonlinear contour corollary
For X⊆P(I), all incident couplings ≥c_-λ, and δ=λ^-1/2, P_full(d_p>δ all p∈X)≤exp[-c_-√λ |X|+F_I]. With universal bound, exponent is -c_-√λ|X|+2bλD m, insufficient when m≈|X|. Under Theorem 2 hypothesis with F_I≤C m(1+logλ), m≤K|X| yields exponential exp[-c√λ|X|] for sufficiently large λ.

## Critical distinction and research status
Uniform local boundedness of the insertion cost (order λm) is proved noncircularly. The stronger O(m logλ) for arbitrary thin interior supports is not proved. Local gauge covariance or bounded incidence alone does not turn -log E_{ρ_I}e^{-E_I} into O(m logλ). One needs an independent cavity-exterior compatible-extension probability, a genuine local weak-coupling plaquette estimate, or a multiscale RG bound. No continuum R3 or R2 gap follows.
