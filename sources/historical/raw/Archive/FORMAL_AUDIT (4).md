# Scale-local Wilson free energy: rigorous benchmark, exact exterior criterion, and the remaining noncircular gap

26 October 2026. **No continuum-uniform 3D Penrose polymer estimate or Yang–Mills mass gap is claimed.**

## 1. Setup

Let a finite simply connected planar disk or a 3D Penrose-derived spacetime complex carry SU(2) Wilson probability proportional to exp[-sum_p beta_p d_p], d_p=1-(1/2)Tr W_p, with beta_p in [c_-lambda,c_+lambda], lambda>=1. For sparse selected links J, no plaquette contains two selected links. P(J) are plaquettes incident on J; |P(J)|<=D|J|. Dilute all these plaquettes as beta'_p=(1-theta)beta_p, 0<theta<1. With exterior links v fixed, for each e in J write B_e=sum_{p\ni e}beta_p, k_e=sum_{p\ni e}beta_p q_{ep}(v), kappa_e=|k_e|, F_e=B_e-kappa_e; and analogues for primed couplings. Then k'_e=(1-theta)k_e, F'_e=(1-theta)F_e, and Delta F_e=theta F_e exactly (for uniform proportional dilution on incident plaquettes). Thus the missing moment is E_eta exp[theta sum_e F_e].

The cavity exact ratio is R_e = exp[theta F_e + ell((1-theta)kappa_e)-ell(kappa_e)], where ell(x)=log z(x)-x and z(x)=2 I_1(x)/x. Integration over exterior gives E_eta prod_e R_e=Z(beta')/Z(beta). There are constants C_theta,c_theta>0 with |ell((1-theta)x)-ell(x)|<=C_theta for x>=0: indeed the difference is bounded as x->infinity because ell(x)=-(3/2)log x + O(1), and it is continuous at x=0. Therefore **for proportional dilution**:

 exp(-C_theta |J|) Z(beta')/Z(beta) <= E_eta exp[theta sum_e F_e] <= exp(C_theta |J|) Z(beta')/Z(beta).

This is sharper than the previous generic O(|J| log lambda) cavity error. Importantly, the moment estimate is equivalent, up to exp(O(|J|)), to the locally diluted free-energy comparison. It cannot be proved simply by relabeling the latter.

## 2. Exact noncircular planar benchmark

For a simply connected 2D free-boundary rhombus disk the face holonomies may be chosen as independent Haar coordinates. Therefore Z_2D(beta)=prod_p e^{-beta_p} z(beta_p). For any subset P, its proportional-dilution ratio is exactly

Z_2D(beta')/Z_2D(beta)=prod_{p in P} [exp(theta beta_p) z((1-theta)beta_p)/z(beta_p)].

The function R_theta(beta)=exp(theta beta)z((1-theta)beta)/z(beta) is uniformly bounded for beta>=1: using e^{-beta}z(beta) ~ sqrt(2/pi) beta^{-3/2}, its limit as beta->infinity is (1-theta)^{-3/2}. Continuity deals with a compact beta interval. Write Q_theta=sup_{beta>=1}R_theta(beta)<infinity. Then

log[Z_2D(beta')/Z_2D(beta)] <= |P| log Q_theta <= D|J|log Q_theta,

and the *actual exterior* frustration moment satisfies

log E_eta exp[theta sum_{e in J}F_e] <= (C_theta + D log Q_theta)|J|.

This is an unconditional, volume- and cutoff-uniform extensive-in-J result with no log lambda loss, but **only in the 2D planar reference theory**. The exterior is the genuine planar Wilson marginal. In 3D the plaquette holonomies obey cube/Bianchi constraints and this factorization is unavailable.

## 3. An exact 3D scale-local free-energy identity

In the full 3D spatial-temporal model, with proportional dilution on P(J), write f(t)=log Z(beta - t beta 1_{P(J)}), 0<=t<=theta. Differentiating under the compact group integral gives

f'(t)=sum_{p in P(J)} beta_p E_t[d_p],

f''(t)=Var_t(sum_{p in P(J)}beta_p d_p)>=0.

Therefore the full moment is bounded exactly iff the integrated *regionwise* defect expectation is bounded:

log E_eta exp[theta sum_e F_e] = int_0^theta sum_{p in P(J)} beta_p E_t[d_p] dt + O_theta(|J|).

A sufficient, noncircular new input would be sup_{t in [0,theta]} sum_{p in P(J)} E_t[d_p] <= C |J| / lambda (or <=C |J|(1+log lambda)/lambda), but **this has not been proved** for arbitrary thin P(J). The earlier bulk-boundary argument yields only O(|J|log lambda + lambda |Y(P(J))|), and |Y|=O(|J|) for thin J. In particular, neither a bounded-degree graph nor local background minimizers improve this automatically.

## 4. Connected cumulants and the necessity of decorrelation

For sources O_i coupled to parameters t_i in the exact fiber partition function, derivatives of log Z_B(Y;t) are genuine conditional connected cumulants. If |O_i|<=1, one has elementary uniform finite-order estimates (e.g., |Cov(O_i,O_j)|<=1), but no decay with spatial separation or number of connected blocks. A polymer root norm involves summing over locations and orders and cannot be controlled by these pointwise bounds. A scale-local free-energy estimate for P(J) is likewise insufficient by itself to establish high-order connected-cumulant decay. An independent covariance-localization and small-/large-field RG induction is needed.

## 5. Noncircular research gate

Needed for arbitrary sparse J in full 3D Wilson theory: uniformly in volume, h and selective dilution, prove

 log[Z(beta')/Z(beta)] <= C_theta |J|(1+log lambda)

via a **new** estimate on the actual exterior 3D Gibbs law, not by assuming the equivalent frustration moment. Next independently show a localized connected-cumulant estimate after subtracting the running background action, of the form |w_k(Gamma)|<=q^{|Gamma|} with q below the rooted-polymer threshold. The planar identity verifies the benchmark but does not imply these 3D statements. Even a successful UV polymer expansion would not by itself imply IR R3 or continuum R2 mass-gap claims.

References: Balaban, *Ultraviolet Stability of Three-Dimensional Lattice Pure Gauge Field Theories*, Commun. Math. Phys. 102 (1985), 255-275, DOI 10.1007/BF01229380; Balaban, *The Variational Problem and Background Fields in Renormalization Group Method for Lattice Gauge Theories*, ibid. 102, 277-309, DOI 10.1007/BF01229381.
