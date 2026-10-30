# Compact-Haar replacement for Gaussian regularization: exact nonabelian results and the unresolved R3 bridge

**Date:** 27 October 2026. **Status:** mathematically exact for the two explicitly stated classes; conditional ambient-uniform Haar-orbit theorem; **NOT** a proof for arbitrary 3D Penrose prism supports or a continuum mass gap.

## Definitions

For SU(2), `d(g)=1-(1/2)Tr(g)` and `w_beta(g)=exp[-beta d(g)]`. Normalize Haar to probability measure. Set

`q(beta)=int w_beta(g) dg = 2 exp(-beta) I_1(beta)/beta` for beta>0 and `q(0)=1`.

For representation spin j, dimension `n+1=2j+1`, the normalized Wilson convolution Fourier multiplier is

`r_n(beta) = I_(n+1)(beta)/I_1(beta)` (beta>0); `r_0(0)=1`, `r_n(0)=0` for n>=1.

All r_n(beta)>=0; no matrix Fourier positivity of a gauge-reduced multiport kernel is assumed.

## Theorem 1: a compact-Haar arbitrary-face-support comparison on a planar disk

Let a finite simply connected cellular disk have a face-shelling order with an edge incident to exactly one currently remaining face at each step. All link variables are integrated over normalized Haar, and the action is a sum of independent class Wilson face weights with arbitrary nonnegative couplings beta_p. Integrate the unique edge of the first face: cyclicity of trace and the substitution `g=A u^(±1) B` imply `int w_beta(A u^(±1) B) du=q(beta)` for *every fixed assignment of other links*. Iterate the shelling. The exact partition function is

`Z_disk(beta)=prod_p q(beta_p)`.

Hence switching on any subset Q of otherwise missing plaquette interactions produces the exact ratio

`Z_insert/Z_cavity=prod_{q in Q}q(gamma_q)`.

This is nonlinear, nonperturbative, valid for all beta/gamma, and independent of ambient disk size. In particular, it applies to a finite, simply connected **2D Penrose rhombus disk with free link boundary conditions**, provided its face complex admits the stated peeling order. It does NOT apply to an arbitrary periodic surface, 3D prism assembly with internal spatial plaquettes, or fixed external boundary links.

**Verified nontrivial interior face:** `verify.py` builds a 3x3 quadrilateral disk with 16 vertices, 24 edges, 9 faces, center face ID4. All four edges of face4 initially also belong to another face: no independent link pivot for face4 exists before elimination. Nevertheless an exact peeling order removes the other eight faces first and then face4. Its retained curvature matrix has exact rank 8, whereas the completed curvature matrix has rank 9: the insertion **adds one curvature constraint** despite the absence of any individually free link. The exact Haar factorization therefore controls even an interior **rank-changing** missing face. This directly demonstrates that new curvature modes can incur the polynomial q(gamma) cost without a Gaussian eta regulator on a 2D disk.

## Theorem 2: one quadrilateral prism cell (a closed six-face sphere)

Select any one prism cell in the 2x2 spatial disk times three-edge periodic time complex. Its surface has 8 vertices, 12 edges and 6 quadrilateral faces, and signed boundary rank 5. Its *standalone surface Wilson theory* is an ordinary finite SU2 lattice gauge theory on a two-sphere: after spatial gauge fixing, five based face holonomies are independent Haar variables, and the sixth is an ordered product of their inverses/conjugates. Standard SU2 character orthogonality/convolution gives the exact sphere partition function:

`Z_sphere(beta_1,...,beta_6)=prod_{p=1}^6 q(beta_p) * sum_{n=0}^infty (n+1)^2 prod_{p=1}^6 r_n(beta_p)`.

If Q is any nonempty subset of faces missing in the cavity, at least one `beta_p=0` in the cavity, so **its normalized correction is exactly 1**. On inserting Q with arbitrary gamma_q>0, all terms in the full normalized correction are nonnegative and its trivial term equals 1. Consequently

`Z_insert/Z_cavity >= prod_{q in Q} q(gamma_q)`.

This is a true compact-Haar support-logarithmic comparison for arbitrary face subsets on a closed prism *surface*, at every coupling, no Gaussian eta regularization. Its constants are independent of the number of faces under analogous closed surface character formula assumptions. For the single prism, no support size issue arises.

**One inserted face with five retained couplings all lambda:**

`R(lambda) = q(lambda) sum_{n>=0} (n+1)^2 r_n(lambda)^6`.

Here `R(lambda)>=q(lambda)`. By the SU2 small-fluctuation limit (each normalized fundamental Wilson quaternion has logarithm sqrt(lambda) X tending to a 3-dimensional standard Gaussian), the product of five independent variables has Gaussian covariance 5I; hence

`lim_(lambda->infty) R(lambda)=E exp(-|Z|²/2), Z~N(0,5I_3) = 6^(-3/2)=0.06804138174397717`.

Thus the single-prism insertion energy actually remains `O(1)` as lambda→infty. This asymptotic can alternatively be supported by a compact-Haar small-ball bound at the group identity. `verify.py` checks rank, the exact series numerically through lambda=1000, and an independent SU2 vMF/quaternion Monte Carlo evaluation (not used as proof).

**CRITICAL GEOMETRIC LIMITATION:** Although the selected prism cell belongs to a three-dimensional complex, this theorem integrates *only the six faces of its closed two-dimensional boundary*. In a multi-prism three-dimensional cavity, adjoining spatial/temporal faces share links with this boundary. Their Wilson weights invalidate the independence of the five face variables. Theorem 2 is NOT an insertion theorem for arbitrary connected 3D Penrose prism cavities.

## Theorem 3: an exact compact-Haar orbit-repair criterion (conditional structural theorem)

Let Ω be a finite SU2 link configuration space with normalized product Haar and retained action S_R. Suppose K=SU2^k acts by measurable maps `Theta_g` preserving both the Haar reference measure and the retained action *for every g*. Assume:

1. For every configuration U there exists some `g_*(U) in K` with `V_Q(Theta_g* U) <= A|Q|`, with A independent of lambda/ambient volume. For the cleanest case, all inserted face holonomies are identity at g*.
2. Every inserted holonomy varies under g according to a bounded-length SU2 word, with at most b coordinates g_i appearing per face and each coordinate appearing in at most v inserted words, uniformly in the ambient lattice. All inserted couplings are at most gamma_max<=B lambda.
3. The number of orbit coordinates satisfies k<=a|Q| and lambda>=1.

The SU2 bi-invariant distance and Wilson chordal deficit obey `d(h)<=dist(h,I)^2/2` up to a fixed normalization constant, and the group-word triangle inequality bounds the increment of each inserted holonomy from its value at g* by a sum of at most b coordinate distances. On a product of Haar balls of radius c/sqrt(lambda) about g*, the insertion action satisfies `V_Q<=2A|Q|+C k`, where C depends only on B,b,v,c. Since each ball has normalized Haar volume >=c0 lambda^(-3/2), the orbit average obeys

`int_K exp[-V_Q(Theta_g U)] dg >= (c0 lambda^(-3/2))^k exp[-2A|Q|-Ck]`.

Use invariance of the cavity law under each Theta_g to average this inequality over U. The exact nonlinear SU2 insertion ratio therefore satisfies

`Z_insert/Z_cavity >= c0^k lambda^(-3k/2) exp[-2A|Q|-Ck]`,

hence `F_Q<= C'|Q|(1+log lambda)`, independent of ambient volume. This is a rigorous compact-Haar *sufficient criterion*. It does NOT assert the existence of such an orbit action for arbitrary Penrose supports. A local group action is stronger than a bounded linearized repair operator.

Theorem 1 provides an exact realization: in peeled face holonomy coordinates, independently translate the Q coordinates, leaving the remaining face coordinates and S_R invariant.

## Explicit obstruction to inferring the orbit criterion from the Gaussian rank

Use Q=[13,18,22,25,26,29,32,37] in the 27-vertex, 63-link, 48-face three-step prism test complex. The retained face incidence is D_R. A normalized link perturbation t was constructed satisfying `D_R^T t=0` (error <1e-14) and `||D_Q^T t||=1.7862729`. Thus t is a new *linearized* curvature direction invisible to R.

Apply simultaneous SU2 quaternion link rotations `U_e -> exp(i epsilon t_e sigma_3) U_e` at epsilon=0.07. At a flat connection every retained face holonomy remains identity exactly, as expected from the linear null condition. At one reproducibly generated generic noncommuting Haar link configuration, however, the maximum change of a retained face normalized trace is **0.022402872289253084**. In other words, the naive uplift of the linear null vector does **not** preserve the nonlinear retained action. This does not rule out a more sophisticated nonlinear orbit, but it proves that the earlier rank audit is not by itself a constructive compact-Haar repair theorem.

## The uncompleted nonlinear R3 bridge

A proof for *arbitrary connected 3D Penrose prism supports* must obtain at least one of:

- a uniformly local compact-Haar orbit / gluing map with uniformly bounded distortion and retained-action cost, **or**
- a quantitative cavity measure lower bound for the good conditional frustration event, with constants proportional to |Q|, **or**
- a new nonabelian correlation/partition-function inequality dominating all multi-prism recouplings.

Neither the five-state/fifteen-state positive finite blocks nor the Gaussian determinant estimate supplies any of these. Rank-changing Q may lack a simple group orbit despite only adding one abelianized constraint, and fixed-dimensional spin truncation does not control lambda→infty. Therefore **the arbitrary-support nonlinear R3 inequality and a continuum Yang–Mills mass gap remain open**. It would be mathematically incorrect to represent Theorem 1, 2, or the conditional Theorem 3 as having completed that final bridge.

## Reproduction

Run `python verify.py`. `certificate.json` contains exact disk peeling pivots, prism incidence ranks, the one-cell Bessel formula values through beta=1000, Monte Carlo cross-checks at beta=1,3,10,30, and the nonlinear noncommutation witness. `incidence_tests.npz` contains compact incidence arrays and the rank-changing linear vector. No PDF/document creation needed.
