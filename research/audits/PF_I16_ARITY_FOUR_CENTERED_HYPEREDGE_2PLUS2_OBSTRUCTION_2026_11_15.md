# PF-I16 — Minimal four-slot obstruction to the singleton-centering hyperedge formula

**Date:** 2026-11-15  
**Status:** EXACT COUNTEREXAMPLE to extending the arity-at-most-three centered active-hyperedge identity by replacing a selected four-row link with its full centered fourth moment. This does not refute the projective LS theorem or any possible arity-four tree bound; it identifies the first surviving 2+2 partition contribution.

## 1. Four-slot law

Let U,V be independent symmetric Rademacher variables and set
[
Y_1=Y_2=U,\
Y_3=Y_4=V.
]
All four variables are centered and bounded by one. Their full centered moment is
[
\mathbb E[Y_1Y_2Y_3Y_4]
=\mathbb E[U^2V^2]=1.
\tag{1.1}
]
Their only nonzero pair covariances are
[
\kappa(Y_1,Y_2)=1,\qquad
\kappa(Y_3,Y_4)=1.
\tag{1.2}
]
The fourth classical cumulant is therefore
[
\begin{aligned}
\kappa(Y_1,Y_2,Y_3,Y_4)
&=\mathbb E[Y_1Y_2Y_3Y_4]
-\kappa(Y_1,Y_2)\kappa(Y_3,Y_4)\
&\quad-\kappa(Y_1,Y_3)\kappa(Y_2,Y_4)
-\kappa(Y_1,Y_4)\kappa(Y_2,Y_3)\
&=1-1=0.
\end{aligned}
\tag{1.3}
]
Thus the 2+2 partition ({{1,2},{3,4}}) contributes the entire fourth moment and cancels the full-block fourth cumulant.

## 2. Consequence

For a selected centered hyperedge of size two or three, every nontrivial partition of its selected vertices has a singleton block intersection, which kills that partition moment. For four selected vertices, a 2+2 split has no singleton. Equation (1.3) is the smallest exact example.

Therefore the arity-at-most-three proof cannot be extended by simply defining the active four-link weight as the full centered fourth moment and asserting that connectedness kills every nontrivial row partition. A valid arity-four argument must retain the pair-pair partition terms (and, in general, the full link partition lattice), or establish a separate signed cancellation/resummation.

The example is algebraic and occurs at coincident times; it is not a counterexample to a stationary Markov temporal-tree inequality. The bounded-slot projective LS theorem remains valid under its literal multiplicity hypothesis. Unrestricted repeated-link incidence and the global mass-gap proof remain open.

The companion verifier checks (1.1)–(1.3) exactly by rational enumeration of the four-point law.
