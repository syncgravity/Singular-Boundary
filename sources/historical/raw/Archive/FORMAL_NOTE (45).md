# Constrained face coordinates and Wilson transport: rigorous local audit
27 October 2026

## Setup
Finite oriented 3D cell complex (including spatial Penrose rhombus prisms), oriented edges E, plaquettes P, normalized SU(2) Haar. S0 is Wilson action on undeleted plaquettes P0 with couplings beta_p<=c_+ lambda, V_Q is inserted plaquette action. All statements finite volume and gauge covariant where gauge invariant objects used.

## 1. Exact constrained holonomy chart
Fix a connected graph and rooted maximal tree T. Tree gauge setting tree links to identity leaves r=|E|-|V|+1 non-tree holonomy variables g_e with product Haar measure for gauge-invariant observables (ignoring residual global conjugation, or fixing basepoint gauge). Every plaquette holonomy is a word W_p(g) in the g_e and inverses. These face holonomies are NOT independent: for every oriented contractible 3-cell the ordered conjugated product of its boundary face holonomies equals identity. Thus r independent cotree variables, not |P| independent face variables, are available. This is exact, including temporal faces.

## 2. Exact entropy identity for coordinatewise radial transports
Take any specified cotree variables g_j, j in H. Fix the other g variables w. Let Phi_{lambda_j} be the SU(2) conjugation-equivariant radial Haar-to-Wilson map. Define T_w as g_j -> a_j(w) Phi_{lambda_j}(b_j(w) g_j c_j(w)) d_j(w), with SU(2) prefactors chosen so that the transformed target word is the radial transform of an associated target face holonomy (only when that word contains its pivot cotree variable once and the triangular pivot construction is invertible). Its Haar Jacobian has the exact product form J=prod_j 1/w_{lambda_j}(W_j(Tg)), provided the triangular dependence is only on preceding/untransformed coordinates. Hence -E_mu0 log J = sum_j E_mu0 log w_lambda_j(W_j(Tg)), which need not equal sum_j KL(w_lambda_j||Haar) when original conditional pivots are non-Haar. General exact variational identity:
 F_Q <= E_mu0 [V_Q(Tg)+S0(Tg)-S0(g)-log J].
This does not assume independence or provide a logarithmic estimate by itself.

## 3. A rigorous nonlinear crossing-face deformation bound
Let T be any transformation changing links g_e by right or left rotations with geodesic angles a_e(g) in [0,pi]. For each undeleted p let A_p=sum_{e in boundary p and moved}a_e(g). Bi-invariant geodesic triangle inequality for holonomy, plus |sqrt(d(W))-sqrt(d(V))| <= theta(W^{-1}V)/sqrt(2) (since sqrt(d)=sqrt(2)sin(theta/2) is 1/sqrt(2)-Lipschitz in theta), yields
 d_p(Tg) <= [sqrt(d_p(g))+A_p/sqrt(2)]^2
and hence
 S0(Tg)-S0(g) <= sum_{p in P0} beta_p [sqrt(2 d_p(g)) A_p + A_p^2/2].
Taking cavity expectations and Cauchy-Schwarz yields
 E_mu0 [S0(Tg)-S0(g)] <= sum_{p in P0} beta_p [sqrt(2 E_mu0 d_p sqrt(E_mu0 A_p^2)) + (1/2) E_mu0 A_p^2].
This is a legitimate correlation-sensitive bound; it is not O(|Q| log lambda) unless the cross-plaquette curvature and transported angular displacements are sufficiently small. It explicitly incorporates spatial and temporal crossing faces, with no fixed-exterior assumption.

## 4. Sufficient transport estimates and limitations
If a triangular constrained-face chart exists with at most C|Q| pivot links, and the constructed transport satisfies
 (i) E V_Q(Tg)<=C|Q|(1+log lambda),
 (ii) -E log J<=C|Q|(1+log lambda),
 (iii) sum_{p in P0} beta_p [sqrt(2 E d_p sqrt(E A_p^2))+(1/2)E A_p^2] <= C|Q|(1+log lambda),
then the target insertion bound follows. (iii) is NOT known for arbitrary Penrose thin supports. Bounded incidence by itself bounds the count of affected plaquettes but not E d_p or E A_p² at the required scale. Any proof using such bounds must establish them independently to avoid circularity.

## 5. Distinguishing tree coordinates and gauge-invariant curvature
The cotree variables transform under a residual root conjugation. A conjugation-equivariant radial map applied to a closed holonomy respects this residual symmetry; an arbitrary pivot map may not be equivariant under all local gauge transformations until transported back through gauge fixing. Different 3-cell Bianchi constraints can make a face-prescribing triangular chart fail globally; no assertion of a uniform such chart for arbitrary Penrose supports is justified.

## Status
Established: exact tree-gauge coordinatization, nonlinear deformation bound for all crossing Wilson plaquettes, and a quantitative sufficient transport criterion. Not established: correlated thin-support cutoff-uniform crossing-action cost, global compatible triangular charts, uniform insertion free energy, polymer convergence, mass gap.
