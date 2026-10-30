# Penrose rhombus-prism filling and compatible-minimum audit (2026-10-27)

## Scope
A geometric theorem for a restricted support class on a conforming rhombus-prism 3-complex, and a precise statement of what it does not imply probabilistically. No arbitrary-thin-support insertion free energy, RG contraction, or mass gap is claimed.

## 1. Linearized curvature-filling theorem
Let C^1 and C^2 be real cellular cochains (tensor su(2) for flat SU(2) linearization), D=d_1. Let P_0 be undeleted faces, Q deleted/inserted faces. Each prism 3-cell has 6 faces: a top and bottom rhombus and four temporal side faces. Assume for every p in Q an assigned prism c(p) contains p and none of its other five faces belongs to Q. Let epsilon_{cf} be the oriented incidence signs. From d_2 d_1=0,
 (DA)_p = -epsilon_{c(p),p} \sum_{f\subset \partial c(p), f\ne p} epsilon_{c(p),f} (DA)_f.
Define L_Q on undeleted 2-cochains by the right side, with zeros outside the assigned 5 faces. Then D_Q=L_Q D_0. If each undeleted face participates in <= M assigned prisms, Cauchy-Schwarz yields ||L_Q y||^2 <=5 M ||y||^2, thus ||L_Q||<=sqrt(5M). For a 3-dimensional conforming manifold cellulation, each interior face is in at most two 3-cells, and each prism can be assigned to at most one p (by the other-five-undeleted hypothesis), so M<=2 and ||L_Q||<=sqrt(10). Anisotropic/geometric weights require separate uniform equivalence; literal physical FE mass norms need not be uniformly equivalent to unweighted ones without scale factors.
For H_0=lambda D_0^*D_0+mu I, mu>0, D_Q H_0^-1 D_Q^* <= (1/lambda)L_Q L_Q^*, so Gaussian curvature covariance norm <= 10/lambda, and gaussian insertion determinant <= (3|Q|/2) log(1+10), if D in weighted units and inserted action lambda/2||D_Q A||². The bound is a *geometry-class* theorem, not all Q.

## 2. Nonabelian counterpart
For each shellable prism boundary, transported oriented plaquette holonomies multiply to I, so the holonomy of an omitted face is a product of inverses of the five other transported face holonomies, up to conjugation. Let theta(g)=arccos(tr(g)/2) in [0,pi]. Bi-invariant triangle inequality gives theta(W_p)<=sum_{f !=p} theta(W_f). Since d(g)=1-cos theta(g) <= theta(g)^2/2 and theta(g)^2 <=(pi²/2)d(g),
 d_p <=(5 pi²/4) sum_{f !=p} d_f.
Summed over p in Q, with multiplicity M<=2, sum_{p in Q} d_p <= (5 pi²/4) M sum_{f in P_0 touching assigned cells} d_f. If couplings bounded ratios, the weighted inserted action is pointwise controlled by neighboring undeleted action, but this alone gives no local Gibbs expectation at O(log lambda) because deleted/undeleted exterior normalization is still coupled.

## 3. Compatible minimum distribution: exact limits
For internal set I of m links, define S_I(u;v) as all incident plaquette terms and E_I(v)=min_u S_I. Let a_I=E_{rho_I}Z_I, F_I=-log a_I; actual exterior marginal eta_I(dv)=Z_I(v)rho_I(dv)/a_I. Because Z_I(v)<=exp(-E_I(v)), for 0<=t<=1,
 E_{eta_I} exp(t(E_I-F_I)) <=1,
 eta_I(E_I>=F_I+s)<=exp(-s).
This is a uniform *relative* tail but not an independent bound for F_I. Bound F_I<=2 c_+ lambda D m is unconditional but not logarithmic. Any claim of a uniform O(m log lambda) absolute tail requires an independent insertion free-energy or equivalent thin-support estimate. A deterministic filling d_Q<=C d_0 does not by itself give E_{rho} sum d_0 =O(|Q|log lambda/lambda) under interacting 3D cavity measure.

## 4. Inapplicability to arbitrary supports
If Q has multiple faces of a prism, the other-five-undeleted hypothesis can fail. In an isolated single prism with Q consisting of all faces, D_0=0 while D_Q=d_1 is nonzero, so no factorization D_Q=L D_0 exists. More generally, kernel obstruction: D_Q|ker D_0 !=0. Thus unrestricted uniform filling through undeleted faces is false as a general algebraic assertion; residual coarse-curvature directions must be retained.

## 5. What still must be independently proved
(i) Validate the relevant Penrose spacetime cell incidence, boundary conditions, and actual filling classes in the geometry used for R3; (ii) establish local weak-coupling Gibbs plaquette control on the five-face neighborhoods and their thin unions, or a direct logarithmic insertion comparison, without assuming it; (iii) control supports with residual curvature directions via a genuinely local correlated transport or multiscale RG. No mass-gap proof follows.
