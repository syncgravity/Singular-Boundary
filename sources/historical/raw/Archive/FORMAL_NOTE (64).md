# Nonlinear SU(2) boundary-energy comparison and spatial response
Date: 2026-10-27. Scope: rigorous finite-volume variational identities and conditional localization theorem; not an arbitrary Penrose mass-gap proof.

## A. Exact nonlinear Dirichlet-to-Neumann structure
Let K be a finite Wilson cell complex with some boundary links/trace y fixed. Choose a gauge slice and a *regular smooth coordinate chart* in which the Wilson action S(x,y) is C^2 and the admissible domain for x is open. Suppose the constrained minimizer x_*(y) exists uniquely, lies in chart interior, and H(x_*,y)=partial_x^2 S >= m I >0. Then E(y)=S(x_*(y),y) is C^2 (as long as hypotheses persist). Differentiating stationarity S_x=0:
Dx_*[v]=-H^{-1} S_{xy}v.
Envelope: DE(y)[v]=S_y v.
Effective Hessian: D^2 E=S_{yy}-S_{yx}H^{-1}S_{xy}.
These are exact identities for the genuine SU(2) Wilson action restricted to a regular minimizing branch (not a quadratic approximation). For multiple minimizing branches, E is the minimum of smooth local branches and can be nondifferentiable; none of these differential identities may be used across crossings.

## B. Nonlinear minimum-energy monotonicity
If a shell enlargement extends the admissible deformation space while preserving the *same* boundary trace and the old trial configuration embeds with unchanged action (or added nonnegative terms are demonstrably zero on the embedding), the new constrained minimum is no greater than the old one. Without this precise embedding, adding Wilson plaquettes may increase the action, so ordinary geometric shell enlargement alone is not enough. Exact group-valued holonomies always respect Bianchi relations since they are computed from physical links.

## C. Spatial decay of minimizer response, conditional theorem
Partition adjustable coordinate space into link blocks indexed by vertices of a bounded-degree interaction graph. Assume the minimizer Hessian H=(H_ij) is SPD, D=diag(H_ii), diagonal blocks H_ii >= m I, and normalized off-diagonal row sum
q=max_i sum_{j != i} ||H_ii^{-1}H_ij|| <1.
Assume H_ij=0 for non-neighboring blocks. Let B=S_{xy} and assume a boundary coordinate y_b couples only to blocks at graph distance <=1 from the boundary site b, with sum of column block operator norms of B bounded by L. Stationarity gives Dx_*/Dy_b=-H^{-1}B_b. Neumann expansion of H=D(I+D^{-1}(H-D)) and finite propagation imply
||(H^{-1})_ij|| <= (1/m) q^{dist(i,j)}/(1-q).
Thus
||partial x_{*,i}/partial y_b|| <= [L/(m(1-q))] q^{max(dist(i,b)-1,0)}
(with boundary locality and column sum as stated). This gives *nonlinear* response decay on the regular branch. To bound total response over a shell with <=C (Delta-1)^r blocks at distance r, one needs q(Delta-1)<1 for the simple sum-of-block-norms estimate; this is sufficient, not necessary. A weighted spatial norm or elliptic cancellation can improve the criterion.

## D. Nonlinear effective boundary-energy comparison
E''=S_yy-S_yx H^-1 S_xy, exact. If mixed matrices B_a, B_b localized at boundary regions a,b and direct S_yy coupling vanishes beyond distance 1, then the off-diagonal effective Hessian satisfies
||partial_{y_a} partial_{y_b} E|| <= C (L_a L_b)/(m(1-q)) q^{dist(a,b)-2},
provided the same regular-branch hypotheses and uniform local mixing constants hold. Integrating the mixed derivative over a rectangle of boundary perturbations gives an interaction-energy inequality
|E(y_a',y_b')-E(y_a,y_b')-E(y_a',y_b)+E(y_a,y_b)| <= C q^{dist(a,b)-2} length(y_a,y_a') length(y_b,y_b'),
when all interpolants remain in one regular chart/branch. This is the nonlinear Dirichlet-to-Neumann spatial propagation bound, with conditions stated explicitly.

## E. Why arbitrary Penrose support is unresolved
1. The actual tree-gauge Wilson action has pure-gauge/flat low modes and no established cutoff-uniform m>0 on relevant growing blocks; Dirichlet rows need not be diagonally dominant. Strong-coupling Hessian off-diagonal magnitudes can be same order as diagonal, so q<1 is unproved and often fails in crude row-sum norm.
2. Nonflat Wilson backgrounds can have indefinite Hessian; minimizers may be nonunique, global charts fail, and crossing branch singularities prevent differentiating E globally.
3. The finite-dimensional deterministic decay estimates do not control the distribution of the backgrounds/boundary data under the true cavity Gibbs measure; no large-field tail is implied.
4. Certified 3D prism face-cell incidence and stability of geometry-weighted norms across cutoff still require verification.
5. This does not prove universal logarithmic insertion free energy, absolute thin-support tails, R3/R2, or Yang-Mills mass gap.

## F. Exact unconditional continuity (weak but always available)
On finite compact SU(2)^E, E(y)=min_x S(x,y) is continuous. If y,y' differ on b boundary links, and each such link meets at most Delta plaquettes with beta_p<=c_+ lambda, then |E(y)-E(y')|<=c_+ lambda Delta sum_{e in boundary} theta(y_e^{-1} y_e') by evaluating each minimum at the other boundary values and using |d(W)-d(W')|<=theta(W^-1 W'). This local O(lambda) Lipschitz estimate has no spatial decay and cannot replace the missing nonlinear tail.
