# R3-IR — One-link charged-score control of deleted-face radial Fisher information

Date: 2026-10-31. Exact finite-volume Wilson statement. **No current-gate or continuum mass-gap claim.**

## Setting

Take the finite original-link SU(2) magnetic-deleted Hamiltonian H_f^- with normalized smooth strictly positive gauge-invariant ground state Omega, with a simple face f and its coordinate p_f=cos u. Let dnu=Omega² dmu and let the face-angle marginal be dnu_f(u)=omega_0(u)Psi_f(u)²du, omega_0=2 sin²u/pi. For any boundary link e of f take left/right normalized Lie derivatives X_(e,a), choose the orientation consistent with their gauge covariance, and set S_(0,e)=sum_a ||X_(e,a)Omega||². The exact SU(2) single-link identities are sum_a (X_(e,a)p_f)²=(1-p_f²)/4 and Delta_e p_f=-3p_f/4.

## Theorem FB-1: exact one-link Ward projection

For every smooth p in (-1,1),

  E_nu[sum_a (X_(e,a)p_f)(X_(e,a)log Omega) | p_f=p]
    = (1-p²)/4 * (d/dp log psi_f(p)),

where psi_f(p)=Psi_f(arccos p). This follows by integration by parts on only link e, testing q(p_f), comparing with the pure Haar pushforward, and using the fact that the one-link carré du champ of p_f is deterministic. **No other boundary links or conditional approximation are used.**

## Theorem FB-2: local radial Fisher bound

Conditional Cauchy-Schwarz, then integration over dnu_f, gives

  \boxed{I_ang(f):=integral_0^pi omega_0(u)Psi_f(u)² [partial_u log Psi_f(u)]² du <= 4 S_(0,e).}

To see the factor 4: let kappa=(1-p²)/4 and j_e=E_nu[eta·v|p]=kappa partial_p log psi. Since sum eta²=kappa,

  kappa [partial_p log psi]² <= E_nu[sum_a v_a²|p].

As kappa(partial_p log psi)²=(1/4)[partial_u log Psi]², integrating gives the claimed result.

With the archived exact gauge-orbit charged coercivity delta_v=2/B_v, and the local Wilson f-sum, one obtains for any differentiated source vertex v

  \boxed{I_ang(f) <= 4 S_(0,e) <= (3B_v/4) sum_(g≠f:e∈boundary g) b_g E_nu[p_g] <= (3B_v/4) sum_(g≠f:e∈boundary g) b_g.}

If one retained neighboring face g touches e this becomes I_ang(f) <= 3B_v b_g/4. The first inequality is sharp for radial amplitudes Omega=psi(p_f), when e is a simple-link derivative and the remaining conditional degrees carry no transverse score; the second is an inequality, not generally sharp.

## Theorem FB-3: collar transfer with explicitly missing density

For any measurable angular interval I⊂[0,pi], write P_f(I)=int_I omega_0 Psi_f² du. Then

  \boxed{integral_I omega_0 Psi_f² |partial_u log Psi_f|du <= 2 sqrt(S_(0,e) P_f(I)).}

Consequently, for 0<eps<pi/2, if an **independent** density lower bound m_(eps)>0 satisfies Psi_f(u)>=m_(eps) on [eps,pi/2], then

  \boxed{integral_eps^(pi/2) [partial_u log Psi_f]_+ du <= 2 sqrt(S_(0,e)) [integral_eps^(pi/2) du/(omega_0(u)m_(eps)²)]^(1/2)}

  = sqrt(2 pi S_(0,e) cot(eps))/m_(eps).

No unconditional estimate for the unweighted current follows, since the exact factor m_(eps)^(-1) may diverge with h. Combined with independently controlled endpoint positive score on [0,eps], this gives a valid, explicit conditional stitching criterion. This improves global-volume Fisher budgets to a single local charged sector but does **not** prove the separate anti-depletion estimate.

## Rigorous limitations

The theorem controls probability-weighted radial score but cannot alone bound T_(f,h)=int_0^(pi/2)[partial_u log Psi_f]_+du. Smooth positive center-even amplitudes may exhibit deep narrow interior wells while their one-link weighted Fisher need not give a uniform current bound; the previously archived full-endpoint-jet no-go is consistent with this. A bound on I_ang alone does not imply a nonvanishing m_(eps). Nor does a local bound proportional to B_v b_g prove o(h^(-1/4)) when b_g is of order h^(-2). All statements require the exact original-link Wilson eigenstate and indicated coefficient assumptions.

## Next obligation

Derive an independent **local conditional-density lower bound or an unweighted one-sided variation estimate** from the full Wilson fiber equation that is strong enough, when paired with the single-link Fisher bound, to prove sup_(f∈D_R) T_(f,h)=o(h^(-1/4)). No connected-covariance or continuum Yang–Mills mass gap is established.