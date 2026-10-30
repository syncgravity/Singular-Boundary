# R3 — Gibbs-probability conversion of correlated bad staples

Date: 2026-10-26. Scope: finite SU(2) Wilson spatial–temporal complexes, including bounded-incidence Penrose extrusions. No mass-gap claim.

## Definitions

Let `d_p(U)=1-(1/2)Tr(W_p(U)) in [0,2]`, `S_beta(U)=sum_p beta_p d_p(U)`, `Z(beta)=int exp(-S_beta(U)) dU`, `mu_beta=Z(beta)^{-1}exp(-S_beta)dU`. Assume `c_- lambda <= beta_p <= c_+ lambda` and plaquette incidence at each link bounded by `D`. For link `e` fix other links; the incident action is `S_e(u)=B_e-u.k_e` in SU(2) quaternion coordinates, `B_e=sum_{p contains e} beta_p`, `k_e=sum_{p contains e} beta_p q_{p,e}`. Its minimum `F_e=B_e-|k_e|` depends only on other links. For a chosen target plaquette and good-staple parameters as in the previous note, bad-staple `G_e^c` implies `F_e >= f_lambda := c_* sqrt(lambda)` once lambda is sufficiently large.

Let `J` be a set of links with no plaquette containing two links in `J`, and `S=P(J)={p: some e in J belongs to boundary p}`. Then sets of incident plaquettes are disjoint, so pointwise `sum_{e in J}F_e <= sum_{p in S} beta_p d_p(U)`.

## Theorem 1 — Exact Gibbs comparison

For every `0<theta<1`,

`mu_beta(intersection_{e in J} G_e^c) <= exp(-theta f_lambda |J|) Z(beta^{(theta,S)})/Z(beta)`,

where `beta_p^{(theta,S)}=(1-theta)beta_p` on S and `beta_p` otherwise. This is an unconditional full Gibbs-probability estimate, including all spatial and temporal interactions.

Proof: Pointwise inclusion into `{A_S >= f_lambda |J|}`, where `A_S=sum_{p in S}beta_p d_p`. Exponential Markov yields `P(A_S>=fn) <= exp(-theta fn) E exp(theta A_S)`. The expectation equals the displayed partition-function ratio.

The logarithmic ratio also has the exact thermodynamic identity

`log[Z(beta^{(theta,S)})/Z(beta)] = integral_0^theta sum_{p in S} beta_p <d_p>_{beta^{(t,S)}} dt`.

Hence if independently established `sum_{p in S} beta_p <d_p>_{beta^{(t,S)}} <= q_lambda |J|`, uniformly for t in [0,theta], the bad-staple pattern has probability at most `exp[-(theta f_lambda-theta q_lambda)|J|]`. This last locality hypothesis is NOT derived here.

## Theorem 2 — Unconditional boundary-corrected Gibbs estimate

Let `Y(S)` consist of plaquettes outside S that contain at least one link in a plaquette of S. Then there are constants C1,C2 depending only on c_+, c_-, theta and local incidence such that, for lambda>=1,

`log[Z(beta^{(theta,S)})/Z(beta)] <= C1 |S| (1+log lambda) + C2 lambda |Y(S)|`.

Consequently

`mu_beta(intersection_{e in J} G_e^c) <= min{1, exp[-theta c_* sqrt(lambda)|J| + C1 D |J|(1+log lambda) + C2 lambda |Y(P(J))|]}`.

Proof of ratio bound: Condition on links outside E(S), the union of plaquette support links. In the original conditional integral, all S and touching Y(S) contributions are nonnegative. For every interior link restrict Haar to a ball of radius r/sqrt(lambda) about identity. Each S plaquette has defect <=C/lambda, regardless of exterior, since all its links are inside E(S). Each touching Y plaquette has defect <=2 regardless of exterior. The restricted Haar volume is >= (c lambda^{-3/2})^{|E(S)|}. The conditional denominator is therefore >=exp[-C|S|-2 c_+lambda|Y(S)|-C|E(S)|(1+log lambda)]. The conditional numerator under selective dilution is <=1, whence a bound on their ratio that is uniform in conditioned exterior links. Since |E(S)|<=4|S|, the result follows upon integrating over exterior links, including plaquettes wholly outside E(S), which cancel in the conditional ratio.

Caution: for typical thin J on a bounded-degree spacetime graph, |Y(P(J))| is O(|J|), not O(|J|/sqrt(lambda)); the positive lambda boundary penalty dominates the negative sqrt(lambda) energy term. Therefore this estimate is quantitatively vacuous for thin bad-staple clusters. It does NOT prove unconditional exponential bad-staple suppression or convergence of the connected polymer gas.

## Independence pitfall

The pointwise frustration cost `F_e` compares each exterior configuration against an independently aligned reference cavity. Those cavity optima generally cannot be realized by a single exterior link field, so `e^{-F_e}` cannot be interpreted as a Gibbs probability. The partition-function ratio in Theorem 1 is essential and cannot be discarded.

## Next required improvement

Prove an exterior-compatible local transport/repair inequality that bounds `log(Z(beta^{(theta,S)})/Z(beta))` by `O(|S| log lambda)`, uniformly for arbitrary thin connected S, OR prove a multi-region probability via a different localized flow/reflective argument. For Penrose tilings additional issues include non-periodicity, anisotropic temporal plaquettes, boundary gauge fixing, and source reconstruction. Even a sharp contour bound alone would not imply a mass gap.
