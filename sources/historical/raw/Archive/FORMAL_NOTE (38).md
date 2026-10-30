# Averaged compatibility gap: two-sided entropic comparison and non-equivalence audit

## Setup
Finite SU(2) Wilson gauge complex. Let K consist of k adjustable link variables u, w the fixed complement. Let S_Y(u;w), S_Q(u;w) be nonnegative Wilson actions with bounded plaquette incidence and face length, coefficients beta_p <= c_+ lambda, lambda>=2. Define M_Y=min_u S_Y, M_QY=min_u(S_Y+S_Q), Gamma=M_QY-M_Y >=0. Let Z_Y(w)=int exp(-S_Y)du, Z_QY(w)=int exp(-S_Y-S_Q)du and R(w)=Z_QY/Z_Y. The reference marginal of w with the Q-terms deleted is nu(dw) proportional to exp(-S_rest(w)) Z_Y(w)dw. These are not independent fields.

## Theorem: deterministic two-sided comparison
There is L_k=k((3/2)log lambda+C) such that
  -L_k <= -log R(w)-Gamma(w) <= L_k.
Proof: for either of the two nonnegative Wilson actions S, its Haar integral satisfies exp(-min S-L_k) <= int exp(-S)du <= exp(-min S), using stationarity at the compatible minimizer, bounded local second derivatives O(lambda), and product of k Haar balls radius O(lambda^-1/2). Ratio and logarithms give the claim.

## Global consequences
Let F_Q=-log E_nu R be the insertion free energy. Since e^{-Gamma-L_k} <= R <= e^{-Gamma+L_k},
  |F_Q + log E_nu exp(-Gamma)| <= L_k.
For t>=0, the lower-tail estimate
  nu(Gamma<=t) <= exp(t + L_k - F_Q)
comes from R >= exp(-Gamma-L_k), so E R >= exp(-t-L_k) nu(Gamma<=t). [Note: this is an UPPER bound on probability of low Gamma, not a useful lower bound!]
Conversely, R<=exp(-Gamma+L_k) implies F_Q >= -log E exp(-Gamma)-L_k. By splitting e^{-Gamma} at t: E e^{-Gamma} <= nu(Gamma<=t)+e^{-t}, giving
  nu(Gamma<=t) >= exp(-F_Q-L_k)-e^{-t}.
This becomes a polynomial lower-tail bound when F_Q=O(k log lambda), with t somewhat above F_Q+L_k. It does not imply E Gamma=O(k log lambda).

## Averaged gap and a strict separation
Jensen gives -log E exp(-Gamma) <= E Gamma. Hence F_Q <= E Gamma+L_k, a one-sided estimate, and no converse without control of the upper tail. For a nonnegative abstract gap taking 0 with probability 1/2 and lambda with probability 1/2, -log E exp(-Gamma)<=log2 while E Gamma=lambda/2. This example demonstrates logically that insertion control does not prove mean control; it is not asserted to be realized by a Penrose Gibbs field.

## Exact cumulative-tail formulation
  E_nu Gamma = int_0^{2 c_+ lambda |Q|} nu(Gamma>t)dt,
where Gamma<=min_u S_Q <=2 sum_{p in Q} beta_p <= 2c_+lambda |Q|. Thus sufficient is an upper-tail bound nu(Gamma>t) <= A exp(-b t/k) above t0=Ck log lambda, with constants uniform in lambda, volume, and supports. Neither positivity nor the two-sided partition ratio comparison supplies this.

## Caveats
The local Hessian lower-integral argument assumes a stationary global minimum on the SU(2)^k manifold; it holds on this compact smooth manifold, including gauge-degenerate minima. Constants require finite face length, bounded incidence, and all couplings O(lambda). The two-sided comparison does not prove averaged Gamma bounds for arbitrary Penrose thin filling sets. Its main value is distinguishing annealed insertion free energy from the quenched mean compatibility gap.

## Source context
T. Balaban, *Ultraviolet Stability of Three-Dimensional Lattice Pure Gauge Field Theories*, Commun. Math. Phys. 102 (1985), 255-275, DOI 10.1007/BF01229380, concerns Wilson ultraviolet stability in its regular-lattice setting, not the claimed Penrose thin-support estimate.
