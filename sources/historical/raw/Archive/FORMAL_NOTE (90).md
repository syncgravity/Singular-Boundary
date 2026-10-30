# R3 scalar frustration comparison: sampled nonlinear SU(2) cavity and exact linearized Gaussian model
Date 2026-10-27. Numerical experiments on constructed four-quadrilateral spatial disk × three-edge periodic time circle; 27 vertices, 63 links, 48 faces, 12 prism cells. **Not a Penrose-extracted patch.** This is finite-dimensional diagnostic, not arbitrary-volume/cutoff theorem or a continuum mass gap.

## 1. Insertion and localization

Q contains 14 selected temporal plaquettes: seven around spatial faces (0,1) in time step 0, seven around spatial faces (0,2) in time step 1. Their oriented incidence touches m=36 local links L, leaving 27 exterior links E. There are 34 retained faces. Let d(U_f)=1−Tr(U_f)/2 and take a common nonnegative coupling lambda on the retained and inserted plaquettes.

For any exterior assignment xi, write S0(u;xi)=lambda sum_{retained f}d(W_f), S1=S0+lambda sum_{f in Q}d(W_f). Define E_i(xi)=min_{u∈SU2^36} S_i and Δ_lambda(xi)=E1−E0≥0. The cavity exterior marginal ρ0 is the pushforward of the exact retained Wilson law under projection onto these 27 exterior links. The empirical quantity computed is H(lambda)≈−log E_{rho0}exp(−Δ_lambda), via sampled exteriors and *locally optimized* conditional minima. Numerical minima are not globally certified.

The previously derived uniform-local-geometry Haar-ball inequality gives Z1/Z0≥c^36 lambda^(−54) E_{rho0}exp(−Δ_lambda), lambda≥1, **if its stated smoothness/degree assumptions hold**, hence insertion free energy F_Q ≤54 log lambda + 36 log(1/c) + H(lambda). The numerical H is NOT substituted to assert a theorem.

## 2. Nonlinear cavity sampling and minimization

Reproducible code `run.py` reconstructs face cyclic words from exact d1,d2, represents SU2 links as normalized quaternions, and verifies analytic action gradient with a symmetric finite difference. Metropolis sweeps update all 63 links against **only 34 retained Wilson plaquettes**. Each exterior assignment is obtained from a complete retained-cavity configuration (no conditioning or hot/cold selection of exteriors). Full minimization uses the same 36 local links for E0 and E1 and keeps the 27 exterior quaternions fixed. SciPy L-BFGS-B with normalized unconstrained quaternions uses an analytic gradient; the cavity and inserted minimum are each tried from two different starts. A minimum of these trials is used.

The main dataset contains two chains per lambda, 60 retained exteriors per chain, after 700 complete sweeps of burn-in and 25 complete sweeps between recorded samples, at lambda 1,4,12,30,100,300. Chain 0 begins cold/flat and chain 1 begins Haar-random. Numba and NumPy RNG streams are seeded explicitly from the supplied chain seed. The main run was split into groups A (1,4,12) and B (30,100,300); group B skips six RNG seed draws to preserve the original per-chain seed sequence. `assemble.py` verifies correspondence of 720 saved sampled gauge configurations to their 720 recorded conditional minima. A separate high-coupling stress run uses lambda 1000 and 3000, 1200 burn-in and 30 intervening sweeps, 60 configurations in each of two chains. Iteration limits were reached for some of those extreme-coupling optimizations, so those values are exploratory.

`analyze.py` computes H from sample weights exp(-Δ), bootstrap uncertainty by resampling **five-consecutive-measurement blocks within each of the two chains**, 4000 bootstrap resamples. Such intervals do NOT quantify unknown MCMC thermalization bias, very long correlations, or global optimizer failure; they are indicative errors only. `audit.py` checks exact gauge covariance of 48 face holonomies on five sampled configurations (max error below 10^−15), matches raw cavity actions, and replays four conditional minimizations (energy differences <10^−8). The two-start optimizer energies agree to <~10^−9 on almost all 720 main samples; two lambda=1 cases have different inserted local minima, the maximum difference ~0.02733. The lower achieved energy is retained. At lambda≤300 all recorded selected optimizations reported success.

The processed values, full per-sample defects, and saved SU2 link configurations are in `summary.csv`, `analysis.json`, `main_720_samples.json`, and `main_720_configurations.npz`. `high_240_samples.json` and `high_240_configurations.npz` are separated to preserve their distinct settings. Results do not prove that independent chains have fully mixed or that local minima equal global minima.

## 3. Exact linearized Gaussian exterior comparison

Let D=d2 be the 63×48 oriented link-face boundary matrix, E the 27 exterior links, and L the 36 local links. For a face set S=R (34 retained faces) or S=R∪Q (all 48), let A_S=D[L,S]^T and B_S=D[E,S]^T. For each su2 color component, the quadratic approximation around a common trivial flat connection is

 S_S(u,xi)=(lambda/2)||A_S u + B_S xi||².

Eliminating the local variables gives E_S^Gauss(xi)=(lambda/2)xi^T C_S xi, with

 C_S = B_S^T (I − A_S A_S^+) B_S,

where the superscript + denotes Moore–Penrose pseudoinverse. The exact integer incidence matrix yields ranks rank(A_R)=25, rank(A_{R∪Q})=31, rank(C_R)=rank(C_{R∪Q})=5. Their exterior kernels are identical, and C1−C0 is PSD of rank four. Thus the six added local curvature constraints introduce *no new external flatness constraints in the linearized theory.*

Let g_i be the five generalized positive eigenvalues of C1 relative to C0 on the common exterior active subspace. Here

 g=(1, 1.00286171, 1.00417695, 1.30365444, 1.43277445).

Under the cavity **Gaussian** marginal (three independent su2 colors), the conditional frustration has the exact distribution

 Δ^Gauss = (1/2) sum_{i=1}^5 (g_i−1) χ²_{3,i},

so E Δ^Gauss=(3/2)∑(g_i−1)=1.1152013232791562 and

 E exp(−Δ^Gauss)=∏_{i=1}^5 g_i^{−3/2}=0.38762571335593715,
 H_Gauss=(3/2)∑ log g_i=0.9477150612383232.

These are exact consequences of **the specified linearized Gaussian model**, subject to numerical roundoff in computing pseudoinverses/eigenvalues. They are independent of lambda. Flat directions must be factored out (or regularized using a common finite volume), since the unbounded Gaussian measure is not normalizable along them. This formal local tangent model does not automatically equal the nonlinear SU2 large-lambda limit: nontrivial flat holonomy moduli, nonlinear Jacobians, global minimizers and possible stratified stationary points need separate analysis.

## 4. Uniformity criterion for the Gaussian theory

For any family of analogous complexes with the same exterior active subspace for C0 and C1, if a uniform spectral comparison C1≤M C0 holds on that subspace and rank(C1−C0)≤r_Q, then

 H_Gauss≤(3/2) r_Q log M.

This follows because all eigenvalues of C0^(−1/2) C1 C0^(−1/2) lie in [1,M], and at most r_Q of them differ from 1. For our instance r_Q=4 and M=1.43277445, giving a rigorous finite Gaussian O(1) bound. The rank and spectral constants **have not been shown uniformly independent of cavity volume or general Penrose geometry**. More importantly, controlling the nonlinear SU2 conditional exterior measure by these Gaussian modes uniformly in lambda and volume remains open.

## 5. Decision

The positive 15-state spin-network contraction remains an independently verified low-sector benchmark. The complete nonlinear scalar diagnostic and exact linearized elimination now indicate a physically/mathematically useful mechanism: the added six curvature directions can be adjusted within L while the exterior effective constraint rank stays five. The sampled frustration cost stays O(1) over tested couplings, in close numerical agreement with its tangent Gaussian prediction. This is strong finite-model evidence supporting **localized correlated rearrangement** over entrywise Fourier positivity, but it is not proof of the general support-local insertion theorem or continuum gap.
