# R3-IR — Ground-state relative-energy and curvature phase-neck theorem

Date: 2026-10-28. **Status:** exact finite SU(2) Wilson Hamiltonian variational theorem, conditional fixed-physical-area Agmon corollary. **Does not prove** continuum existence, fixed-support connected covariance collapse, or positive uniform mass gap.

Let H=sum_e a_e(-Delta_e)+sum_f b_f(1-p_f) on the finite gauge-invariant SU2 link Hilbert space, with a_e positive and bounded by a_max. Let Omega be its unique positive ground state, nu=Omega^2 dHaar, and Delta the first positive physical excitation energy. For a bounded real source |q_f|<=qmax define X=sum_D (1-p_f), Z=hX, and Y=h sum_D q_f(1-p_f). Each face has four edges and each edge belongs to at most two faces.

**NE-1 (exact Dirichlet source reduction).** The full interacting ground-state transform and the SU2 Casimir give for any real Lipschitz g:
  <g(Y)Omega,(H-E0)g(Y)Omega> = E_nu[Gamma(g(Y))],
  Gamma(Y)=sum_e a_e |nabla_eY|^2 <= 4 a_max qmax^2 h Z,
  Gamma(g(Y))=(g'(Y))^2 Gamma(Y).
If mu is the law of Y and gamma(y)=E_nu[Gamma(Y)|Y=y], this becomes int |g'(y)|^2 gamma(y) mu(dy). No mixing or gap assumption.

**NE-2 (relative energy and neck criterion).** Fix u<v with width w=v-u, let pminus=nu(Y<=u), pplus=nu(Y>=v), pbridge=nu(u<Y<v), both pminus,pplus positive. Let g be 0 up to u, linear to 1 on [u,v], and 1 above v. Then the normalized physical state psi=g(Y)Omega/||g(Y)Omega|| obeys
  <psi,(H-E0)psi> <= [4 a_max qmax^2 h/(w^2 pplus)] E_nu[Z 1_bridge].
The orthogonal state (g(Y)-E_nu g(Y))Omega has squared norm Var_nu(g(Y))>=pminus*pplus; hence
  **Delta <= [4 a_max qmax^2 h/(w^2 pminus pplus)] E_nu[Z 1_bridge].**
For q_f=1, Y=Z and E_nu[Z 1_bridge]<=v pbridge. This is an unconditional upper bound on the actual physical gap.

**NE-3 (Agmon-refined signed-source version).** Assume the independently proved finite-vacuum regional Agmon theorem for X, with b_f>=beta_min/h^2, L=C_L/h>=2h^2(E0-Eout)/beta_min, lambda=c_lambda/h, c_lambda=sqrt(beta_min/(32a_max)). For any fixed J>2C_L,
  E_nu[Z 1_bridge] <= J pbridge + [64 a_max/(beta_min C_L)]h^4 exp(-2c_lambda(J-2C_L)/h^2).
Substitute this in NE-2 to obtain a signed-test spectral-neck estimate valid for the true interacting vacuum. If pminus>=c0, pplus>=c1*h and pbridge<=C exp(-kappa/h^2) across fixed separated moderate Y-bands, then Delta<=C' exp(-kappa'/h^2) for some kappa'>0. Consequently a sharply separated rare moderate-curvature phase **would force** an exponentially soft physical excitation; the existence of this phase is **not** established. The new theorem does not establish Var_nu(Y)=o(h); unimodal O(sqrt(h)) fluctuations have no thin macroscopic probability neck.

**Independent verification:** deterministic SU2 one-rhombus Haar test for pure electric H_E=4a(-Delta_class): p=ReTr(U)/2 has density 2 sqrt(1-p^2)/pi, and first gauge-invariant gap 3a. With a=h=1 and Y=1-p, u=1/2 and v=3/2, pminus=pplus=1/3-sqrt(3)/(4pi), the explicit linear cutoff Rayleigh quotient is approximately 3.82008064759 and exceeds the true gap 3; the coarse bound is 95.6023368056. Also checks original canonical three-rhombus Z5 spatial incidence. No Monte Carlo or modification of original archives. Full detailed proof and verifier are in the derived audit package. Stage7/26 normalization remains unverified.

**Open next proof obligation:** model-derived control of the actual vacuum's moderate-source distribution or connected variance with fixed physical support, without assuming a positive gap or Gaussian mixing; thereafter quartic resolvent and continuum.
