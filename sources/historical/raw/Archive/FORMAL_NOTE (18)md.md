# Local SU(2) Wilson surface repair: a gauge-compatible lemma and a mesoscopic obstruction

Date: 2026-10-26. Scope: finite 2+1-dimensional spacetime plaquette complexes with bounded link incidence, including bounded-incidence Penrose rhombus extrusions. All estimates are finite-volume identities; no mass gap is presumed.

## 1. Local Wilson rotation lemma

Let a link e be oriented from vertex v to w, and let its variable transform under gauge transformations as U_e -> g_v U_e g_w^{-1}. Let R be a prescribed SU(2) matrix at v, transforming R -> g_v R g_v^{-1}. The substitution U_e -> R U_e is Haar-measure preserving, equivariant and changes only plaquettes incident to e. For R independent of U_e (it may depend on other, frozen links), this is a legitimate conditional change of variables.

Put p(W)=Tr W/2 and d(W)=1-p(W). For SU(2) unit quaternions R=(r0,r), W=(w0,w), p(RW)=r0w0-r·w. Since |r|^2=d(R)(2-d(R))<=2d(R) and |w|^2<=2d(W),

    |d(RW)-d(W)|<=d(R)+2 sqrt(d(R)d(W)).

Conjugation and inversion do not alter d. For Wilson action S(U)=sum_p beta_p d(W_p(U)), beta_p>=0,

    |S(U^{e,R})-S(U)| <= sum_{p contains e} beta_p [d(R)+2 sqrt(d(R)d_p(U))]. (1)

Here spatial and temporal p occur on equal footing. The support of the change is the plaquette star of e, no total-volume factor. If the maximum plaquette incidence per link is D and beta_p<=c_+ lambda, (1) also gives <= D c_+ lambda [d(R)+2 sqrt(2 d(R))], using d_p<=2. These bounds are not generally O(log lambda).

For any measurable nonnegative f depending on all links, conditioning on the other links yields the exact local Ward/change-of-variable identity

    int f(U_e,rest) exp(-S(U_e,rest)) dU_e
     = int f(R^{-1} U_e,rest) exp(-S(R^{-1}U_e,rest)) dU_e,

with R independent of the integrated U_e. Choosing R as a function of U_e itself invalidates this Haar-Jacobian assertion unless the map is independently shown measure preserving. In particular, collapsing W_p to I is not a bijective change of variables.

## 2. Quantitative energy cost at the large-field threshold

For a target defect d_p=delta=lambda^{-1/2}, a rotation of geodesic size theta~sqrt(delta) has d(R)~delta. The first term beta d(R) is of order sqrt(lambda) at beta~lambda; even if neighboring defects are O(lambda^-1), the cross term beta sqrt(delta/lambda) is O(lambda^1/4). Thus locality of the repair does not produce logarithmic energy control. Frozen-exterior competing staples provide concrete counterexamples to pointwise O(log lambda) repair costs.

## 3. Nonabelian surface energy lower bound

Let D be a simply connected cellular disk consisting of N plaquettes. Fix boundary holonomy V. Write theta(V)=arccos(Tr V/2) in [0,pi]. A disk shelling expresses V as an ordered product of conjugates of the face holonomies. The bi-invariant SU(2) geodesic metric obeys theta(V)<=sum_{p in D}theta(W_p). Furthermore, for theta in [0,pi], 1-cos theta >= (2/pi^2)theta^2. Consequently, with beta_p>=beta_min,

    S_D(U)>= (2 beta_min/pi^2) sum_p theta(W_p)^2
           >= (2 beta_min/(pi^2 N)) theta(V)^2. (2)

The inequality is gauge invariant, valid for all noncommuting configurations, and independent of the ambient volume. It is a LOWER bound on the action required to accommodate a prescribed boundary holonomy.

There is a matching upper bound for the minimum on a free disk: choose all face holonomies in a common U(1) subgroup with equal angle theta(V)/N; a disk with free interior link variables admits this face assignment. Then

    inf_{U: boundary holonomy V} S_D(U)
         <= beta_max N (1-cos(theta(V)/N))
         <= beta_max theta(V)^2/(2N). (3)

The upper bound is an existence statement for the compatible background, NOT a comparison of Gibbs partition functions or Jacobians. If external links or additional transverse plaquettes are frozen, (3) need not apply without charging their action changes.

For beta~lambda and theta(V)^2~lambda^-1/2, the minimized disk action scales like sqrt(lambda)/N. A disk containing N>=C sqrt(lambda)/log lambda faces can have a compatible background with action O(log lambda). Conversely a fixed number of cells in this setup cannot be assured logarithmic cost by the surface bounds. This illustrates a mesoscopic scale for redistributing curvature; it is not a thin-contour probability theorem.

## 4. What remains to be proved

A sufficient step toward the previously proposed continuum polymer bound would be an exterior-uniform or Gibbs-averaged comparison for a mesoscopic collar D(X), with action and integration-Jacobian cost O(|X| log lambda), after retaining temporal plaquette constraints and compatible coarse boundary holonomies. Equations (1)-(3) establish locality, algebraic surface bounds, and a feasible compatible background for a free disk, but not such a Gibbs comparison.

The unconditional thin-support diluted free-energy bound, arbitrary connected large-field contour suppression, uniformly summable background-subtracted activities, R3 and R2 remain open.
