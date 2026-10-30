# R3 completion attempt: rigorous local Gibbs audit

Date: 2026-10-28.

## Verdict

No complete proof of the arbitrary nonstationary three-slab R3 insertion estimate follows from the currently available certificates. In particular, the missing volume-uniform local Wilson-energy estimate has not been established. This note records a rigorous interpolation identity, a volume-uniform **conditional** Ward estimate, and an explicit check distinguishing these results from the target.

## Setup

Finite oriented 2-complex with edge holonomies in SU(2), normalized Haar product, retained faces R. Let d(g)=1-(1/2)ReTr(g), so 0<=d<=2; S_F=sum_{p in F}d(W_p). Fix F=A_fill subset R, |F|=54, and local adjustable links H, |H|=36. Assume standard nondegenerate plaquettes, each containing a given oriented link at most once. The reported Penrose Bianchi certificate is S_Q<=44 S_F, |Q|=14.

## Exact one-link Ward theorem

For a retained-link star at link e, condition on all other edges. There are n_e staples a_i in SU(2) (unit quaternions), M=sum a_i, r=|M|, and S_e(u)=n_e-u dot M. Set m_e=n_e-r. Under the exact conditional Gibbs distribution,

  0 <= lambda E[S_e-m_e | other links] <= 3/2.

Proof. For r>0, rotate M to the north pole on S^3. In y=1-u_0, the tilted Haar density is proportional to exp(-lambda*r*y)*sqrt(y*(2-y)) dy. The derivative of y^(3/2)*(2-y)^(1/2)*exp(-t y) integrates to zero on [0,2]; rearranging gives t E y=3/2-(1/2) E[y/(2-y)] <=3/2. At r=0 the excess is zero. Thus the inequality is uniform in exterior condition and volume.

For any nonnegative fractional edge cover (w_e) of F, lambda E S_F <= (3/2)sum_e w_e + lambda sum_e w_e E m_e. In particular, if each fill face touches H, unit weights on H give

  lambda E S_F <= 54 + lambda sum_{e in H} E m_e.   (A)

The number 54 on the right is (3/2)*36.

## Exact local coupling interpolation

Fix all other couplings and define

  Z(s)=integral exp[-lambda S_{R\F}-s lambda S_F] dU, 0<=s<=1,
  Phi(s)=-log Z(s).

Then

  Phi'(s)=lambda E_s S_F,
  Phi''(s)=-lambda^2 Var_s(S_F)<=0.

Thus for 0<=s<1,

  0<=lambda E_1 S_F <= [Phi(1)-Phi(s)]/(1-s)
  = log[Z(s)/Z(1)]/(1-s).                     (B)

At s=0 one gets lambda E_1 S_F <= log[Z(0)/Z(1)]. A uniform polynomial partition-function comparison for *strengthening the 54 fill faces* would close the energy target, but no such comparison is supplied by the 14-face Bianchi inequality. This is not an independent proof of that comparison: (B) only transfers the task to a localized partition-function ratio.

Uniform elementary bound: 0<=lambda E_1 S_F <=108 lambda, since |F|=54 and d<=2. This is linear in lambda, not the required O(log(1+lambda)).

## Why a conditional star bound is insufficient

Two opposing unit-quaternion staples a_1=1 and a_2=-1 give M=0 and m_e=2. The star energy S_e(u)=2 for every u. Thus lambda E[S_e|other links]=2lambda; the exact thermal-excess bound is 0, and no improvement follows without suppressing opposing staples in the full Gibbs marginal. This is a conditional boundary datum, not a counterexample to full Wilson theory.

## Barrier implication: proven only conditionally

The existing Bianchi-and-Haar-ball argument reports

  -log E_{nu_0} exp(-lambda Delta) <=54 log(1+lambda)+C+44 lambda E S_F.

Together with (A), under the H-cover hypothesis,

  -log E_{nu_0} exp(-lambda Delta) <=54 log(1+lambda)+C+2376+44 lambda sum_{e in H}E m_e.

Neither (A) nor the interpolation identity proves the required uniform bound on the final term. The arbitrary nonstationary three-slab R3 theorem remains unproved, and a continuum Yang-Mills mass gap cannot be inferred.

## Explicit closure criterion

It suffices (but has not been shown) to prove one volume-uniform bound for the specific 54-face set:

  sup_Lambda log[Z_{Lambda}(s=0)/Z_{Lambda}(s=1)] <= C+a log(1+lambda),

or, alternatively, sup_Lambda lambda E S_F <= C+a log(1+lambda).

Equation (B) makes the first imply the second. Such a comparison requires new input about the full exterior Gibbs correlations. No global compactness or finite-volume saddle-point asymptotics can supply volume-independent constants without further argument.

## Provenance/limitations

The count |H|=36, |F|=54, Bianchi constant 44 and incidence claim come from earlier project reports; this note does not independently certify their underlying geometric matrices. The Ward theorem and interpolation identities are general for standard SU(2) Wilson plaquettes.
