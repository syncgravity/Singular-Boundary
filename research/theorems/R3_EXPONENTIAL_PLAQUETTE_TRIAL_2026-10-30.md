# R3-IR-512 — Exponentially tilted plaquette trial for the full inverse-Whitney Hamiltonian

Date: 2026-10-30.

Let H(b)=H(0)-b p_f be a finite open-disk SU2 Hamiltonian with inverse-Whitney electric form H_E=(g2_squared/2)D* K D, K=M^-1, and remaining bounded plaquette potential fixed. Assume normalized positive ground state Omega0 for H(0) and free-boundary center flip Z with ZH(0)Z=H(0), Zp_f Z=-p_f. Define Z0(t)=<e^(2t p_f)>_Omega0 and tilted expectation E_(0,t)[F]=<F e^(2t p_f)>_Omega0/Z0(t). Use Psi_t=e^(t p_f)Omega0/sqrt(Z0(t)). Ground-state transform gives the EXACT kinetic excess

<Psi_t,(H(0)-E(0))Psi_t> = (g2_squared/2) t² E_(0,t)[(Dp_f)*K(Dp_f)].

The SU2 four-link identity sum_boundary |D_e p_f|²=1-p_f² and SPD block principal bound yield excess <= C_f t² E_(0,t)[1-p_f²], where C_f=(g2_squared/2)lambda_max(K_boundary,boundary). Rayleigh-Ritz for H(b), combined with concavity and Hellmann–Feynman m(b)>= [E(0)-E(b)]/b, implies, for b>0 and every t>=0,

**m(b)>= E_(0,t)[p_f] - (C_f t²/b) E_(0,t)[1-p_f²].**

Taking the supremum over t gives an optimized local variational response estimate. No total magnetic strength occurs explicitly. The zero-coupling *environment-dependent* tilted law remains. This is not a uniform conditional density estimate and not a continuum theorem.

For the independent Haar SU2 rotor H=a(-Delta)+b(1-p), the same state with Omega0=1 and C_f=a/4 gives a rigorously parametrized lower bound. SU2 Haar p distribution is (2/pi)sqrt(1-p²) dp on [-1,1]. At t=sqrt(b/a) and a=1, numerical Gauss-Jacobi quadrature gives lower bounds 0.270704642 (b=1), 0.682335358 (10), 0.891263208 (100), 0.988787512 (10000). Since E_(0,t)[p]->1 and E_(0,t)[1-p²]=O(1/t), these lower bounds tend to 1 as b/a grows. The numerical decimals are NOT certified interval enclosures. This removes the earlier two-state trial saturation at sqrt(v0)=1/2 for the Haar rotor.

In the interacting Penrose system, one needs a quantitative lower bound on the tilted near-center mass of the b=0 conditional plaquette distribution. Positive analytic ground-state density at fixed volume ensures nonzero near-center mass, but no volume/refinement uniform lower bound is known. The trial inequality alone therefore neither bounds the local center moment uniformly nor proves shrinking double-center cap probability or the continuum 3+1 Yang-Mills mass gap.
