# R3-IR-423 — Exact finite-character blindness at the shrinking SU(2) cap scale

2026-10-30. Rigorous SU(2) quadrature counterexample for strictly positive smooth center-symmetric probability densities. This is not an example of a physical Wilson vacuum, and it does not negate the cap Fourier expansion R3-IR-422.

Let J>=1 and set N=2J+1. For l=1,...,N define theta_l=pi*l/(N+1) and weights w_l=2 sin(theta_l)^2/(N+1). The weights sum to one. Let mu_N be the conjugation-invariant probability measure obtained by placing weight w_l uniformly on the SU(2) conjugacy class of class angle theta_l. Since theta_(N+1-l)=pi-theta_l with equal weights, mu_N is invariant under U->-U.

THEOREM (FC-1). For all integer spins j=1,...,J,
int chi_j(U) dmu_N(U)=0 = int chi_j(U) dHaar(U),
yet mu_N(B_a(I))=0 whenever 0<a<pi/(N+1)=pi/(2J+2).

Proof. At theta, the SU(2) character is chi_j(theta)=sin((2j+1)theta)/sin(theta). Thus
int chi_j dmu_N=2/(N+1) sum_(l=1)^N sin(theta_l) sin((2j+1)theta_l).
Discrete sine orthogonality says this sum is zero when 2j+1 is an integer between 2 and N; in the chosen N=2J+1 this includes all 1<=j<=J. The nearest support class has angle theta_1=pi/(N+1), so the identity cap of smaller radius has zero mass. Center symmetry follows from reflection of the nodes. QED.

SMOOTHING. Let K_tau be the strictly positive central SU(2) heat kernel. Convolve mu_N with K_tau, obtaining a smooth strictly positive center-symmetric central probability density rho_(N,tau). Character Fourier convolution multiplies the j-th character expectation by exp[-tau j(j+1)] in the normalization -Delta chi_j=j(j+1)chi_j. Therefore the first J integer-spin moments remain EXACTLY zero. As tau goes to zero, rho_(N,tau) weakly approaches mu_N, hence for any a<pi/(2J+2) its cap mass tends to zero. In contrast Haar(B_a)>0.

COROLLARY. No inequality based solely on the first J integer-spin expectations, even with center symmetry, can certify a fixed positive fraction of the Haar probability of every identity cap of radius a<pi/(2J+2), uniformly over strictly positive smooth central laws: the above laws have the same first J moments as Haar but arbitrarily small cap probability. Consequently, any character-moment-only method that is universally valid for such laws must resolve J of order at least 1/a; under a_h proportional to sqrt(h), this is of order at least h^-1/2. This is an INFORMATION-RESOLUTION obstruction, not a lower bound on the cost of a Wilson-specific method exploiting extra physical dynamics.

Relation to R3-IR-422: a finite-J Fourier certificate with a rigorous tail can of course detect this problem through a large uncontrolled tail. The present theorem proves that no low-spin-only replacement for such tail control can work at the small-cap scale on the whole center-symmetric class. It also directly preserves the exact Haar benchmark in the low moments while defeating cap survival, clarifying why the physical Wilson environment is indispensable.

No physical completed-cage Wilson counterexample or positive cap theorem, infrared spectral bound, or continuum Yang-Mills mass gap is claimed.
