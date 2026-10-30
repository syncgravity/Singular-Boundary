# Exact spatial character RG and the 2+1D obstruction

**Date:** 26 October 2026. **Scope:** exact SU(2) Wilson-weight convolution on *simply connected planar spatial disks*; diagnostics of why it does not yet renormalize the 2+1D Hamiltonian. Does not prove R3/R2.

## 1. Exact spatial RG theorem

Let `G` be an oriented finite simply connected rhombic disk (square or Penrose), with free outer boundary. Let `D` consist of `q` faces forming a simply connected subdisk. Fix normalized Haar measure on each link, and plaquette weights `exp(beta_f p(W_f))`, where `p(W)=(1/2)Tr(W)`. Denote the outer holonomy of the subdisk by `V`, up to orientation and conjugation. After removing any redundant gauge factor, the normalized marginal `V`-density is the convolution of the `q` independent central one-plaquette densities `rho_beta(W)=exp(beta p(W))/z(beta)`, `z(beta)=2 I_1(beta)/beta` (with continuous value at zero).

SU(2) character convolution gives exactly

\[
R_D(V)=\sum_{j\in\{0,1/2,1,\dots\}}(2j+1)\left[\prod_{f\in D}r_j(\beta_f)\right]\chi_j(V),\qquad r_j(\beta)=\frac{I_{2j+1}(\beta)}{I_1(\beta)}. \tag{1}
\]

This is positive, integrates to one, and is independent of the number and couplings of faces outside D in the planar, free-boundary theory. It is a genuine **spatial** decimation: the boundary holonomy is retained; the inner face variables are integrated.

For the fundamental representation, set `u_D=prod_{f in D} r_{1/2}(beta_f)`; then

\[
\langle p(V)\rangle= u_D,\qquad R_D(V)=1+4 u_D p(V)+\sum_{j\ge1}(2j+1)\Bigl[\prod_f r_j(\beta_f)\Bigr]\chi_j(V). \tag{2}
\]

The final sum is over integer and half-integer `j>=1`, i.e. 1,3/2,2,... . **The induced action generally contains all characters and is not a one-parameter Wilson action.** The coefficient `4u_D` is the fundamental coefficient in the density, not the exact logarithmic-action coefficient unless the higher terms and logarithmic mixing are controlled.

The exact nonperturbative L2 distance to Haar is

\[
\|R_D-1\|_{L^2(dV)}^2=\sum_{j>0}(2j+1)^2\prod_{f\in D}r_j(\beta_f)^2. \tag{3}
\]

This identity is a precise, physically interpretable effective-interaction norm (at the level of a *2D Euclidean marginal*). For fixed beta>0 and q->infinity it vanishes by character-convolution mixing. It controls expectation values of unit-L2 boundary functions but not Hamiltonian spectral gaps.

Proof: gauge-fix a spanning tree. On a simply connected planar disk, independent oriented face holonomies can be chosen to be independent product-Haar variables; for a subdisk the outer holonomy is an ordered product of its face holonomies, up to conjugation. Character orthogonality says the Fourier matrix coefficient of a central probability is `r_j(beta) Id`, and convolution multiplies those coefficients. Plancherel gives (3).

## 2. Fixed physical coarse scale along the 2+1D bare-coefficient trajectory

Let every spatial plaquette coefficient in the *artificially separated 2D spatial measure* obey `beta_f(h)=c_f/(g_3^2 h)` with `0<c_-<=c_f<=c_+<infty`. Consider a block of fixed physical area `A>0`, containing `q(h)=Theta(A/h^2)` rhombi. Using the large-beta expansion

\[
\log r_j(\beta)= -\frac{2j(j+1)}\beta+O_j(\beta^{-2}),
\]

we find

\[
\log u_D(h)=-\frac32\sum_{f\in D}\frac1{\beta_f(h)} + O\left(\sum_{f\in D}\beta_f(h)^{-2}\right).
\]

Consequently, `log u_D(h)=-Theta(A g_3^2/h)+O(A g_3^4)` for fixed A,g3 and controlled c_f, and thus

\[
u_D(h)\le\exp(-c A g_3^2/h) \quad \text{for all small h, with }c>0. \tag{4}
\]

This is a strong *spatial* Haar-mixing statement for the 2D reference theory. The effective fundamental density coefficient `4u_D` becomes small at fixed physical area. It is emphatically **not** a proof that the 2+1D renormalized effective ratio `b_eff/a_eff` becomes small.

To see why: a genuine 2D continuum Yang-Mills scaling has `beta~1/(g_2^2 h^2)`, whereas the spatial part of an isotropically scaled *3D* Wilson action has `beta_s~1/(g_3^2 h)`. Discarding the temporal plaquettes and then blocking the 2D spatial action changes the theory. The resulting `exp(-const A/h)` area law at the fixed-physical-A trajectory is the diagnostic of that mismatch, not a 2+1D confinement theorem.

## 3. Full 2+1D spacetime Wilson blocking

For `a_t=kappa h`, the action contains both spatial and temporal plaquettes,

\[
S_h=\sum_{f,t} \beta_{s,f}(h) [1-p_{s,f,t}] +\sum_{e,t}\beta_{t,e}(h)[1-p_{t,e,t}],
\]

with spatial and temporal coefficients both `Theta((g_3^2h)^-1)` for fixed bounded kappa and geometric weights. If `X` denotes the block-internal spatial links and `Y` the retained boundary/spacetime links, the *exact* effective interaction is

\[
S_{eff,h}(Y)=-\log\int\exp[-S_h(X,Y)]\,dX + const. \tag{5}
\]

Equation (5) induces multi-character temporal/spatial couplings. Its conditional integrand does **not** factor into independent face measures because temporal plaquettes link adjacent slices. No estimate for the Fourier/cluster norm of (5), independent of h and volume, follows from (1)–(4). A genuine *quantum* spatial RG further requires integrating the electric kinetic operator, and comparing renormalized energies via a spectral/transfer reconstruction. Simple spatial Haar convolution is not an isospectral map of the Kogut–Susskind Hamiltonian.

A physically meaningful admission condition is therefore: construct a block isometry/reconstruction `J_h` and a blocked Hamiltonian `K'_h` with controlled low-energy resolvents; show a local, summable operator/polymer norm `epsilon'_h<=epsilon_*` for the induced interactions and source map; show a lower frame bound with physical support/complexity uniform in h; and show `epsilon'_h` lies in an actual nonperturbative stable region. None is currently proved from the Wilson dynamics along the 2+1D continuum trajectory.

## 4. Cross-check and logical warnings

- Convolution is on a *spatial* Euclidean marginal; it cannot produce physical positive-time correlation decay by itself.
- The character RG is exact, but its single coefficient `u_D` is not a complete effective action (higher representations are generated).
- Sending q to infinity at fixed physical A and `beta~1/h` makes the 2D boundary holonomy Haar; this cannot be read as strong coupling of the quantum 2+1D Hamiltonian.
- From the preceding frame audit, complete interacting Wilson Gram frames at fixed regulator already exist. What is missing is a controlled, localized frame and independent dynamical gap along the continuum trajectory.
- No cutoff-uniform spatial-renormalized Hamiltonian gap, R3, or R2 continuum construction is claimed.

## References

Standard character-convolution details: *Tensor network approach to two-dimensional Yang–Mills theories*, Progress of Theoretical and Experimental Physics (2021); *Noninvertible 1-form symmetry and Casimir scaling in 2D Yang–Mills theory*, Phys. Rev. D 104, 065003 (2021). The exact SU(2) Wilson coefficients are `I_{2j+1}(beta)/I_1(beta)` with the normalization above. The existing project proof notes discuss the Feshbach spatial Hamiltonian Schur map separately.
