# R3 genuine Penrose growing-support and retained-energy audit
Date: 2026-10-27. Scope: certified finite *two-dimensional* direct-Z5 cut-and-project Penrose rhombus disks, extruded through three periodic temporal intervals; not an icosahedral 3D Penrose tiling.

## A. Support families and exact relative-rank checks
Spatial radii 5, 6.5, 8, 10 give 70, 122, 196, 338 rhombi, or 210, 366, 588, 1014 prisms. Families:
1. `compact`: breadth-first growing connected dual-face disk of n=1,3,6,10,16,24,40,80,120,160 rhombi (subject to space).
2. `filament`: central-to-far-boundary dual-graph path of n=1,3,6,10 rhombi where available.
3. `boundary_star`: spatial-vertex-neighboring temporal plaquettes from an initial connected six-face seed near the R=5 disk boundary, expanded to n=6,8,12,20,30, embedded by exact Z5 labels into all four radii.

For compact and filament supports, define the inserted temporal plaquettes to be all temporal faces above the spatial edges of n selected rhombi at t=0, and all those of the first ceil(n/2) selected rhombi at t=1. These supports are overlapping and connected in the temporal-face incidence graph. The full complex includes 3*(F+E) faces and has rank 3E for its face-to-link boundary map. We **independently checked** the identity rank(d2)=3E and rank(d3)=3F at radii 5 and 10, consistent with a spatial disk x circle. For arbitrary inserted face Q, calculate the exact GF(1000003) rank loss using the projection of prism cell boundary vectors onto Q:

    rank(d2)-rank(d2|_R) = |Q| - rank(proj_Q im(d3)).

For a link collar L, its additional exterior rank is `global_rank_loss - (rank(d2|_L)-rank(d2|_{R,L}))`. The first radius r with zero additional exterior rank is called `minimum_exterior_rank_collar_radius`; this is a **linearized criterion only** and is not a certificate of a nonlinear Haar repair.

### Main observed results
For the radius-10 compact family, number of temporal insertions and new curvature rank:

    selected rhombi n:    1   6   16   40   80  120  160
    |Q|:                  8  27   62  145  279  399  531
    new curvature rank:   0   5   18   47  105  157  224
    additional collar:    0   0    0    0    0    0    0

Maximum tested physical diameter: 14.2913 in the original projection coordinates. The maximum transported nonabelian face-factor count among *successfully peeled Bianchi expressions* is 17. **This is not a bound for the entire Q**, because only 36 of 531 faces were peeled for n=160. The unpeeled nonzero curvature-rank modes cannot all be expressed as retained-face words by group identities; the abelianization already precludes that. They would need separate Haar coordinates or correlated transport. The peeling count is algorithm-dependent, and transport *edge*-word lengths were not bounded.

### Boundary sensitivity
For the `boundary_star` family with |Q|=6, on the radius-5 patch we obtain global curvature rank loss 1, exterior rank increase 1 at collar 0, and minimum extra collar radius **1**. With *the same exact Z5-labeled Q* embedded in radii 6.5, 8 and 10, the new global rank and collar requirement fall to zero; all six faces can be eliminated by neighboring prism boundaries. Thus the shrinking-boundary location and ambient prism attachments matter: they may change the relative constraints. A rule proved only for interior supports cannot be transplanted to arbitrary boundary placement without audit.

## B. Rigorous volume-uniform **averaged** retained-plaquette energy bound
Let R be any nonempty set of quadrilateral retained Wilson faces on any finite SU(2) link complex, with free normalized Haar links and homogeneous coupling lambda>=1:

    Z_R(lambda) = integral exp[-lambda sum_{p in R}d(W_p)] prod_e dU_e,
    d(U)=1-(1/2)ReTr(U), 0<=d<=2.

Remove links not meeting retained faces, and let M be the number of remaining links, P=|R|. Each face has four links, so M<=4P. For each active link require geodesic distance theta(U_e,I)<=a/sqrt(lambda), a=1/4. The compact SU2 Haar volume of each such ball obeys

    Haar(B_r)=(r-sin(r)cos(r))/pi >= c0 r^3,
    c0=2 sin(1)^2/(3 pi), 0<=r<=1.

The SU2 Frobenius/chord distance inequality implies `sqrt(d(UV))<=sqrt(d(U))+sqrt(d(V))`, and hence on these link balls `lambda*d(W_p)<=8*a^2` for quadrilateral faces. Therefore

    Z_R(lambda) >= exp(-8 a^2 P) (c0 a^3)^M lambda^(-3M/2).

Let f(lambda)=-logZ_R(lambda). It is nonnegative, concave, has f(0)=0, and f'(lambda)=E_lambda sum_R d(W_p). Concavity implies lambda f'(lambda)<=f(lambda). Thus, using M<=4P,

    [lambda/P] E_lambda sum_{p in R}d(W_p)
       <= 6 log(lambda) + (8 a^2 +4 log[1/(c0 a^3)])
       = 6 log(lambda) + 24.7171422794... .

**Theorem holds uniformly in volume and geometry for the AVERAGE over retained faces.** It is not a `sup_p lambda E d(W_p)<=C` result; neither local O(1/lambda) nor even local O(log lambda/lambda) for each p is obtained from the spatial average. It also does not imply the original R3 insertion theorem without a local Gibbs energy estimate. The constant is intentionally very crude.

## C. Exploratory full nonlinear SU2 retained-cavity energy probes
Using the previous quaternion Wilson Metropolis sampler on each genuine patch, omit the fixed previously studied 14-face temporal support and measure (i) average of every retained plaquette deficit and (ii) one anchored spatial-plaquette deficit and four nearby retained temporal plaquettes. For lambda 4,8 use two chains, 100 burn-in sweeps, 15 measurements each separated by six sweeps; for lambda 16,32 the burn-in was 150. Starts alternate flat/cold and Haar/hot. See energy_probe.csv and energy_probe_protocol.json. Both runs test homogeneous equal Wilson couplings. Across all radii the averaged lambda E d lies roughly between 1.04 and 1.15, with no observed growth proportional to lambda. In contrast, anchored one-face data are noisy (individual chains differ substantially), particularly at lambda 32. Neither chain autocorrelation nor equilibration was certified; this is NOT a proof of a uniform per-face bound, and no infinite-volume or continuum claim follows.

## D. What is needed for a full R3 theorem
The zero *linearized* extra collar for our center-growing families coexists with linearly growing new curvature rank and failure of elementary Bianchi peeling. Therefore a blanket bounded-complexity nonabelian filling theorem does not follow. To finish R3 one must either:
- Prove a uniformly bounded local Haar coordinate/relative presentation for those residual constraints with the curved retained Gibbs measure controlled; OR
- Establish a **local** Gibbs expectation bound for the retained plaquettes in the neighborhood of an insertion together with a compatible nonlinear Bianchi/gluing certificate; OR
- Build a probabilistic correlated repair that permits a growing collar while charging entropy and energy to |Q|.

The averaged energy theorem above alone cannot bound an arbitrary prescribed Q, because the retained Wilson energy could be unevenly distributed among plaquettes. The full arbitrary-support Penrose R3 estimate and continuum Yang–Mills mass gap remain open.

## Reproduction
`python run_supports.py` (GF(p) rank/peeling CSV and certificate); `python boundary_stress.py`; `python energy_bound_verify.py`; `python energy_probe.py` (specify two coupling batches as recorded in protocol). All data derive from the included direct-Z5 generator and nested-prism incidence. No construction is a certified 3D icosahedral quasiperiodic tiling.
