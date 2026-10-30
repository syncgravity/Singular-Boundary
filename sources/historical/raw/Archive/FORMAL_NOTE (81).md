# Four-prism four-port minimal fundamental spin-surface contraction

**Scope.** This note uses the exactly constructed 2 x 2 quadrilateral-prism complex (18 vertices, 33 links, 20 faces, four three-cells), not a provenance-certified Penrose tiling. Four interior temporal seam faces are Q={3,4,10,13}; the other 16 carry equal positive Wilson coupling beta. Every assertion is finite-dimensional and at finite coupling. The calculation evaluates the **scalar four-fundamental-character moment**, i.e. a trace contraction of the full four-port Fourier matrix, **not** the complete matrix or its positivity.

## Exact minimal eight-face contractions

Set chi(g)=Tr_fundamental(g), d(g)=1-chi(g)/2, normalized Haar measure. Define

N(beta)=int_{SU(2)^33} prod_{p notin Q} exp[-beta d(W_p)] prod_{q in Q}chi(W_q) dU.

The mod-two edge incidence equation for a fundamental line on every seam has exactly two solutions with the minimum eight retained spin-1/2 faces:

* S_03={0,1,2,5,16,17,18,19}, the non-seam faces of the two diagonal cells 0 and 3;
* S_12={6,7,8,9,11,12,14,15}, the non-seam faces of the other two diagonal cells 1 and 2.

For either solution, S union Q is the union of **two complete six-face prism boundaries**. The two resulting combinatorial spheres share *exactly one link*, the central vertical link e=10, and no other link. These properties are checked from the saved exact integer boundary matrices.

On a closed connected genus-zero oriented six-face lattice surface, with the *same* SU(2) fundamental character on each face, standard 2D lattice gauge integration with normalized product Haar gives

 int prod_{six faces} chi(W_f) dU = (dim fund)^{V-E} = 2^{2-6}=1/16.

It is important that the orientation on each face is immaterial for SU(2) fundamental characters, which are real. Conditional on the one shared link, each sphere's character integral is constant: a tree gauge transformation (equivalently a change of one of its otherwise independent links) gauges that fixed edge to identity. Thus the two sphere factors multiply exactly, with no unwarranted independence of overlapping links:

  C(S_03)=C(S_12)=(1/16)^2=1/256.

These are *positive scalar intertwiner contractions*.

## Exact leading Wilson expansion

For small beta, exp[-beta d(W)]=1 + beta*(chi(W)/2 - 1)+O(beta^2). Center-parity forces at least eight **distinct retained** faces to carry fundamental lines to match the four seam characters, and exactly the two sets above attain that number. Hence the first nonzero Taylor coefficient of the full Wilson moment is

 N(beta)=2*(beta/2)^8*(1/256)+O(beta^9) = beta^8/32768+O(beta^9).

This is an exact analytic coefficient. Since 0 <=sum_{16 retained}d(W_p)<=32 and abs(prod_4 chi)<=16, Taylor's integral remainder provides the explicit bound, valid for all beta>=0,

 |N(beta)-beta^8/32768| <= 16*exp(32 beta)*(32 beta)^9/9!.

This bound is mathematically certified but numerically loose. It is a small-coupling statement; it cannot infer weak-coupling (large-beta) positivity.

## Entire higher-representation tail at a fixed positive coupling

For d=2j+1, the unnormalized Wilson weight has an absolutely convergent SU(2) character series

 w_beta(g)=sum_{d>=1} a_d(beta) chi_{(d-1)/2}(g),
 a_d(beta)=2*d*exp(-beta)*I_d(beta)/beta >0.

At the identity, sum_d a_d d = 1. Let w_beta^{<=J} retain all spins j<=J and define

 tau_J(beta)=sum_{d>2J+1} (2d^2/beta) exp(-beta) I_d(beta).

Because |chi_j(g)|<=d, the truncation remainder is pointwise bounded by tau_J(beta), while the absolute sum of either the full or truncated series is <=1. Replacing all sixteen retained Wilson face weights with their spin-truncated series and telescoping products therefore yields the fully explicit bound

 |N(beta)-N_{<=J}(beta)| <= 16 (faces)*16 (abs four seam characters)*tau_J(beta) =256 tau_J(beta).

This is a **controlled sum of ALL higher-spin assignments** at any fixed beta>0, using exact Bessel coefficients, not a numerical guess. The certificate includes values for beta=0.5,2,10,100 and J=2,5,10,20,40. For any finite beta, tau_J->0 as J->infty, but no fixed spin cutoff is uniform when beta->infty. The bound controls the scalar moment, not the full matrix entries or a positive lower comparison to the full cavity partition function.

## What remains open

The complete matrix-valued Fourier coefficients for all four half-integer ports have not been contracted, and the higher-spin tail estimate can be too weak to retain the positive leading term except at very small beta. In particular, no positivity of the full matrix, no coupling-uniform relative correction, and no arbitrary Penrose thin-support insertion theorem follows from these results. The four-prism complex is combinatorially constructed and has no certified extraction from a Penrose tiling.
