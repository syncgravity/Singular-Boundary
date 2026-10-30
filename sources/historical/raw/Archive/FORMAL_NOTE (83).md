# Exact scalar insertion comparison by temporal transfer positivity

Date: 2026-10-27. Scope: the constructed 2×2 quadrilateral spatial complex extruded through **one Euclidean time interval** (4 prisms). This is not an actual Penrose-extracted patch. Arbitrary nonnegative temporal face couplings are allowed, but the four spatial face couplings **must agree pairwise between the two time slices**. All links are integrated with normalized Haar measure and no nontrivial fixed temporal boundary fields are imposed.

## Verified incidence

The uploaded incidence file has 18 vertices, 33 edges, 20 faces, 4 cells. There are 9 vertical edges, 12 horizontal edges in each of two slices; 4 spatial faces in each slice and 12 temporal faces (each identified with one spatial edge). Four temporal faces Q=[3,4,10,13] are missing from the cavity. The remaining 8 temporal faces have arbitrary nonnegative couplings. See verify.py/certificate.json.

## Exact temporal gauge and quadratic form

Gauge-fix all nine vertical links to the identity by vertex gauge transformations on the upper slice, leaving 12 lower horizontal links x=(x_e) and 12 upper horizontal links y=(y_e), with product Haar measure. The common spatial Wilson Boltzmann factor is

    f(x)=exp[-sum_{spatial faces a} alpha_a d(W_a(x))],

identically on the upper and lower slices. For each spatial edge e, its temporal face holonomy is conjugate to x_e y_e^{-1} (or its inverse), hence its Wilson weight is w_{t_e}(x_e y_e^{-1}) where w_t(g)=exp[-t(1-1/2 Tr g)]. Face orientations do not affect d.

Let q(t)=int_SU2 w_t(g) dg=e^{-t} 2 I_1(t)/t (q(0)=1). Define convolution operator

    (K_t phi)(x)=int_SU2 [w_t(x y^-1)/q(t)] phi(y) dy.

The normalized SU2 Wilson kernel is a central positive-definite function: its spin-j Fourier scalar is

    k_j(t)=I_{2j+1}(t)/I_1(t) >=0,

with k_0(t)=1 for t>0. At t=0 the normalized kernel is constant 1, giving K_0=P_0 (projection onto constant functions). It follows that K_t - P_0 is positive semidefinite as an operator on L²(SU2) for every t>=0. It is important that *this operator positivity* does NOT assert positive definiteness of the spatially integrated multivariable boundary function F(h).

Define the tensor product K^{(0)} = tensor_{e in spatial edges} K_{t_e}, with t_e=0 on Q, and K^{(1)} where those four t_e are replaced by gamma_e>=0. Multiplication of positive-semidefinite tensor factors is monotone in each factor, hence K^{(1)} >= K^{(0)} in quadratic-form order. The unnormalized weights satisfy

    Z_0 = (product_{e notin Q} q(t_e)) <f,K^{(0)} f>,
    Z_1 = (product_{e notin Q} q(t_e))(product_{e in Q} q(gamma_e)) <f,K^{(1)} f>.

The common positive constants cancel and <f,K^{(1)}f> >= <f,K^{(0)}f> > 0. Therefore

    Z_1/Z_0 >= product_{e in Q} q(gamma_e),
    0 <= log(Z_0/Z_1) <= sum_{e in Q}[-log q(gamma_e)].

For gamma_e ~ lambda >=1 and |Q|=4, this is 6 log lambda + O(1). For arbitrary subsets of the 12 temporal faces the same bound holds, for any spatial size, provided two slices have identical spatial face couplings and temporal interactions factor independently per spatial edge. This does **not** cover spacelike Q, multiple time intervals, temporal/spatial mixed insertions, asymmetric slice couplings, fixed temporal boundary conditions, or arbitrary interacting Penrose three-dimensional cavities.

## Interpretation of prior negative matrix result

The previous genuine gauge-fixed four-port Peter–Weyl Fourier coefficient had an indefinite beta^8 term at small beta. There is no contradiction: a nonnegative scalar function F on SU2^4 may have negative matrix-valued Fourier coefficients, even though the full time-reflection transfer operator K across the two *complete spatial slices* is a positive operator. The insertion comparison involves the positive quadratic form <f,Kf>, not Fourier positivity of the marginal F.

## Correlated exterior rearrangement

Let nu be the fully inserted Wilson law and mu0 the cavity law. The exact Gibbs identity E_nu[V_Q]+D_KL(nu||mu0)=F_Q now yields both terms separately <= sum -log q(gamma_e). This establishes an existence of a globally correlated endpoint law with support-proportional combined action-entropy cost, not a spatially supported deterministic transport map with independently small retained action and Jacobian.

## Verification

Run `python verify.py`. The script checks the 9 vertical/12+12 horizontal link decomposition; 4+4 spatial and 12 temporal face decomposition; one-to-one pairing of temporal plaquettes to spatial edges; and nonnegative numerical SU(2) Fourier multipliers. The operator inequality itself is analytically exact for all spins, not inferred solely from the finite numerical test.
