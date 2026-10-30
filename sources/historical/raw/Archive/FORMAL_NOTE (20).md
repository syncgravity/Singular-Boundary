# Relative fluctuation-entropy cancellation and compatible Wilson background shifts

Date: 2026-10-26. Full SU(2) Wilson action on a finite bounded-incidence 2+1D Penrose/square spacetime complex. No mass-gap hypothesis.

## 1. Exact conditional variational decomposition

Let Q be an internal link set, v the exterior links, and
S_beta(u;v)=sum_{p:p meets Q} beta_p [1-(Tr W_p(u,v))/2].
Put E_beta(v)=min_u S_beta(u;v), A_beta(v)=int exp[-(S_beta(u;v)-E_beta(v))]du, Z_beta(v)=exp[-E_beta(v)] A_beta(v).
For beta'<=beta,
log(Z_beta'(v)/Z_beta(v))=E_beta(v)-E_beta'(v)+log(A_beta'(v)/A_beta(v)).
This is exact, gauge invariant and compatible with fixed exterior temporal links. It does not bound either term.

## 2. Nonperturbative cancellation for sparse selected link cavities

Choose J such that each Wilson plaquette contains at most one selected link. Conditional on exterior v, all selected link integrals factor. For each e, S_e(u)=B_e-u.q_e (unit quaternions), kappa_e=|q_e|, F_e=B_e-kappa_e, and
Z_e=exp[-F_e] A(kappa_e), A(k)=exp[-k]z(k), z(k)=2 I_1(k)/k, z(0)=1.
For proportional dilution of every incident plaquette, beta'_p=a beta_p for p incident on J, a in (0,1), the exterior field is fixed, so kappa'_e=a kappa_e and F'_e=aF_e.
Therefore log(Z'_J/Z_J)=(1-a)sum_e F_e + sum_e log[A(a kappa_e)/A(kappa_e)].
Since A(k)>0 continuous on [0,infinity), A(k)~sqrt(2/pi)k^(-3/2) as k->infinity, the ratio A(ak)/A(k) is continuous and strictly positive and tends to a^(-3/2). Hence absolute logarithmic ratio <= C_a |J|, with C_a independent of couplings, cutoff, volume, exterior gauge field. In particular the naive (3/2)|J|log(lambda) loss is an artifact in these cavities.

## 3. Full Gibbs exterior comparison

Let eta_beta be the exterior marginal after integrating selected links and let beta' mean proportional dilution on incident plaquettes. Then
Z_full(beta')/Z_full(beta)=E_eta_beta[exp((1-a) F_J) R_a(v)],
F_J=sum_{e in J} F_e, R_a(v)=prod_e A(a kappa_e)/A(kappa_e).
Thus
| log[Z_full(beta')/Z_full(beta)]-log E_eta_beta exp((1-a)F_J)| <= C_a |J|.
The exterior frustration moment is not bounded by this identity. The exact free-energy derivative formula is
log Z_full(beta')/Z_full(beta)=int_a^1 dt sum_{p in P(J)} beta_p E_{beta(t)} d_p.
Consequently a uniform O(|J|log(lambda)) frustration bound is equivalent up to O(|J|) to a local diluted free-energy estimate. This is a circularity warning, not a proof of the latter.

## 4. Relative determinant identity and its limits

For positive definite finite-dimensional matrices H,H',
(1/2)log(det H/det H')=(1/2)int_0^1 tr[(H'+t(H-H'))^{-1}(H-H')]dt.
If (1-eps)H <= H' <=(1+eps)H, eps<1, and both are positive, then
|(1/2)log(det H/det H')| <= (n/2) max{-log(1-eps),log(1+eps)}.
This cancels all overall lambda^(n/2) determinants, but n is the number of gauge-fixed genuine Gaussian fluctuation coordinates. Gauge zero modes must be removed first and positivity/form comparability must be independently shown. A determinant identity alone does not compare nonlinear Wilson fluctuation integrals nor imply polymer decay.

## 5. Exact source interpolation

For beta(t)=beta'+t(beta-beta'), with t in [0,1],
(d/dt)log Z_{beta(t)}=-E_{beta(t)}[sum_p (beta_p-beta_p')d_p],
(d^2/dt^2)log Z_{beta(t)}=Var_{beta(t)}(sum_p (beta_p-beta_p')d_p) >=0.
These identities hold for the full interacting measure and quantify the missing dynamical local defect/correlation estimates. They do not bound the first derivative.

## 6. Status

PROVED: exact minimizer/fluctuation decomposition; cutoff- and volume-uniform cancellation of relative cavity entropy for sparse link sets; full Gibbs frustration/free-energy equivalence; finite-matrix relative determinant identity.
NOT PROVED: scale-uniform nonlinear relative entropy on arbitrary Penrose spacetime collars; Gibbs-averaged compatible background energy shifts O(|J| log lambda); thin connected contour suppression; convergent background-subtracted polymer activities; R3 and R2 mass gap.
