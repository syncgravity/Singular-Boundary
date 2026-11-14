# PF-I16 — Multi-cut maximal-correlation conjecture for interlaced super-rows

**Date:** 2026-11-14  
**Status:** Candidate inequality isolated; finite two-state exhaustive tests PASS; general Markov-chain proof OPEN.  
**Scope:** two path functionals on disjoint finite observation-time sets of one stationary Markov chain. This is not yet a multi-row cumulant theorem and does not promote P0–P5.

## 1. Motivation

The coefficient-one minimum-distance estimate for arbitrary interlaced observation sets is false (see the companion obstruction audit). The failure does not rule out a bound that accumulates the strengths of all color-change cuts.

Let the ordered union of two disjoint finite observation sets be
\[
u_1<u_2<\cdots<u_n,
\]
and color each time according to whether it belongs to S or T. Let
\[
J(S,T)=\{j: u_j,u_{j+1}\text{ have opposite colors}\},
\qquad d_j=u_{j+1}-u_j.
\]
For a stationary Markov semigroup with
\[
\|P_t-\Pi\|_{2\to2}\le e^{-\Delta_0t},
\]
the proposed multi-cut maximal-correlation inequality is
\[
\boxed{
\rho_{\max}(\sigma(X_s:s\in S),\sigma(X_t:t\in T))
\le
\tanh\!\left(
\sum_{j\in J(S,T)}
\operatorname{arctanh}(e^{-\Delta_0d_j})
\right).
}
\tag{1.1}
\]
Here \(\rho_{\max}\) is the Hirschfeld–Gebelein–Rényi maximal correlation, equivalently the operator norm of conditional expectation between the two centered L2 subspaces.

If true, it implies for bounded path functionals
\[
|\operatorname{Cov}(F,G)|
\le
\|F-\mathbb EF\|_2\|G-\mathbb EG\|_2
\tanh\!\left(
\sum_{j\in J(S,T)}
\operatorname{arctanh}(e^{-\Delta_0d_j})
\right).
\tag{1.2}
\]
Since \(\tanh(a+b)=(\tanh a+\tanh b)/(1+\tanh a\tanh b)\le\tanh a+\tanh b\), this is in particular bounded by
\[
\|F-\mathbb EF\|_2\|G-\mathbb EG\|_2
\sum_{j\in J(S,T)}e^{-\Delta_0d_j}.
\tag{1.3}
\]
Unlike the false nearest-gap estimate, this retains every color-change interval. For one cut, (1.1) reduces to the usual one-cut L2 contraction.

## 2. Exact finite-state test

A verifier computes the full joint law of all observations for stationary binary reset chains
\[
\mathbb P(X_{u_{j+1}}=y\mid X_{u_j}=x)
=\frac{1+q^{d_j}xy}{2},
\qquad q=e^{-\Delta_0},
\]
forms the normalized joint-probability matrix for the S- and T-observation vectors, and computes its second singular value, which is their maximal correlation.

It exhausts all two-color patterns through six observation times, all gap patterns with gaps one or two, and several values of q. It checks (1.1) directly, rather than testing only selected sign functions. It also samples 128 nonreversible three-state doubly-stochastic kernels (convex combinations of permutation matrices), with four interlaced color patterns and nonuniform gaps one through three, comparing the exact finite joint law's maximal correlation to the bound computed from the kernel's L2 contraction norm. These remain finite-state regression tests, not a proof for general chains.

## 3. Why the hyperbolic-tangent form is a useful target

The addition law for \(\tanh\) is the natural composition rule for maximal-correlation channels in a chain. The proposed right side composes the cut strengths without simply multiplying them and without pretending there is only one cut.

For at most six original time ports on a lattice link, the number of color changes is at most five. Thus (1.3) has at most five temporal contributions for a two-super-row covariance. This is compatible with the previously established linear total port budget.

The conjecture is deliberately stated in terms of maximal correlation, not just covariance of a selected pair of observables. That makes it reusable under conditioning on the other independent link paths.

## 4. Critical proof obligation and possible failure modes

The one-cut data-processing inequality follows directly from the Markov property. The multi-cut statement does not follow by applying that inequality independently at each cut: the cuts are not independent channels, and conditioning on the interlaced observations can change the relevant conditional laws.

A proof must establish a valid tensorization/composition inequality for the two interlaced sigma-fields. It must cover:
- arbitrary stationary Markov kernels satisfying the stated L2 contraction, including nonreversible kernels;
- arbitrary finite, nonuniform observation-time gaps;
- arbitrary finite observation sets, with constants independent of the state-space size.

The binary exhaustive and sampled three-state nonreversible tests can falsify the conjecture in small examples but cannot certify these general points. A counterexample for a nonreversible or larger-state chain would terminate this route or force a stronger hypothesis.

Even if (1.1) is proved, a separate multi-row cumulant argument is still needed to assign its cut bonds to original row pairs and preserve the signed outer cumulant through recursive super-row merging.

## 5. Disposition

- One-cut maximal-correlation contraction: **ESTABLISHED**.
- Coefficient-one minimum-distance bound for interlaced sets: **REFUTED**.
- Multi-cut maximal-correlation inequality (1.1): **CONJECTURE; finite binary tests only**.
- Multi-time super-row cumulant tree with original-row support bonds: **OPEN**.
- Full PF-I16 face/pair support-temporal tree and all downstream gates: **OPEN**.

No P0–P5 acceptance status is promoted.
