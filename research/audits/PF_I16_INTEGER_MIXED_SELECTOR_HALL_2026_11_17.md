# PF-I16: integer mixed selector Hall — finite test and obstruction to the fixed-Q route

Date: 2026-11-17

## 1. Exact condition being tested

For each parent source p, choose one representative Q(p) in its canonical
parent leaf-last target neighborhood, with Q injective. For each row r=(p,J),
let E_r be the set of guarded one-switch child lifts obtained by inserting
J last into Q(p), and let
[
  \delta_r=\sum_{x\in X(p,J)}\frac1{d(x)},\qquad
  q_r=\lceil\delta_r\rceil.
]
A capacity-one selector assigning each target to one row/mark exists exactly
when
[
  |\bigcup_{r\in R}E_r|\ge\sum_{r\in R}q_r
  \quad\text{for every row family }R.                 (IMH)
]
This is the integer Hall condition proved by row cloning in
PF_I16_CANONICAL_REVERSE_MARK_SELECTOR_HALL_CRITERION_2026_11_17.md.

## 2. Exact n=6 result: Q matters

The deterministic parent matching used by the first verifier has
parent_matching=2/2, but its selector flow is 29/30. Its min-cut has two
rows, three neighboring child targets, and quota sum four. The two rows
are both over the parent source
[
 p=(((1,4),(2,3)),((0,1)))
]
with inserted intervals J=(2,6) and J=(3,6); each has demand 3/2 and quota
two. Thus this particular Q does not satisfy (IMH).

The verifier then exhausts every injective parent representative assignment:
there are exactly four. Exactly one is selector-feasible. One feasible
assignment is
[
 Q((((1,3),(2,4)),((0,1))))=((1,2),(2,3),(2,4)),
]
[
 Q((((1,4),(2,3)),((0,1))))=((1,3),(2,3),(3,4)).
]
Its total integer row demand is 30 and its max flow saturates 30/30.

Therefore the failure for the first Q is not a counterexample to selector
existence at n=6. It proves that choosing an arbitrary parent matching and
then hoping for the integer row Hall condition is invalid. The parent
matching must be selected with the child-row constraints in view.

## 3. n=8 randomized search

The second verifier searches parent representative matchings and evaluates
the exact integer row-flow condition. In 500 randomized matching trials it
found no Q with a saturated selector flow. The best observed flow was
[
  723/728,
]
with a min-cut consisting of 23 rows, 30 distinct child targets, quota sum
35, and deficiency five.

This is a finite search result only. It is **not** a proof that no n=8
parent matching Q satisfies (IMH): the matching space was not exhaustively
enumerated, and the search procedure is not a complete optimization
algorithm. The logged cut is a witness for the best Q encountered, not a
Q-independent Hall obstruction.

## 4. Exact n=8 obstruction to every injective fixed-Q selector

The search was strengthened by first enumerating, for each of the 22 parent
sources p, every canonical parent target P for which the rows belonging to
that p satisfy their own integer Hall condition. This is a necessary
condition for any global Q: restricting (IMH) to rows with one fixed p
shows that Q(p) must be one of these locally feasible representatives.

The exact census gives:

- 22 parent sources;
- 440 (p,J)-rows;
- 139 locally feasible parent-source/target choices in total;
- each parent source has between 1 and 12 locally feasible choices;
- no individual parent source is locally impossible.

Now form the bipartite graph from parent sources p to their locally feasible
representative targets P. An exact augmenting-path maximum matching has size
21/22. Its alternating-reachability Hall witness consists of four parent
sources and only three neighboring representative targets:
[
\begin{aligned}
p_1&=(((1,4),(2,6),(3,5)),((0,1),(0,2))),\\
p_2&=(((1,4),(2,6),(3,5)),((0,2),(1,2))),\\
p_3&=(((1,5),(2,6),(3,4)),((0,1),(0,2))),\\
p_4&=(((1,5),(2,6),(3,4)),((0,2),(1,2))).
\end{aligned}
]
Thus their locally feasible representative-target union has cardinality
three, strictly less than four. No injective parent representative matching
Q can choose a locally feasible target for all four sources.

This is stronger than the randomized search: it proves that **no fixed
injective parent representative map Q can satisfy the integer selector
condition (IMH) at n=8**. Indeed, if (IMH) held globally, it would hold on
the rows belonging to each p separately, forcing Q(p) to be locally
feasible. The four-source Hall obstruction then contradicts injectivity.

The obstruction is not a failure of the underlying fractional mixed
expansion. It rules out this particular reduction to one integral parent
representative per parent source and a single reverse-mark selector.

## 5. Consequence for the proof strategy

The integer selector criterion is a valid sufficient condition, but the
present evidence shows that it is a brittle strengthening:

- At n=6, one of four Q choices works and three do not.
- At n=8, 500 randomized choices failed, with a best observed deficiency
  of five.
- The established split-demand max-flow certificates at n=8 and n=10
  prove the weaker fractional quotient condition using the full canonical
  parent neighborhoods. They do not imply (IMH) for a single representative
  Q(p).

Accordingly, the selector route cannot currently be used as the proof of
mixed expansion. The mathematically appropriate fallback is the original
fractional mixed-row Hall condition
[
  \left|\bigcup_{r\in R}E_r^{\rm all}\right|
  \ge\sum_{r\in R}\delta_r,
]
where E_r^{rm all} retains all canonical parent targets and their guarded
lifts, together with the split-demand charge already verified at n=8,n=10.
That fractional statement still needs an all-orders structural proof; no
such proof is claimed here.

## 5. Reproducibility

- Initial integer selector verifier:
  `research/verification/verify_pf_i16_integer_mixed_selector_hall.py`
- Parent matching search:
  `research/verification/search_pf_i16_integer_selector_parent_matching.py`
- Workflow run exposing the fixed-Q n=6 failure and the 500-trial n=8
  search: https://github.com/syncgravity/Singular-Boundary/actions/runs/44088041155
- Workflow: `.github/workflows/pf-i16-integer-mixed-selector-hall.yml`

The workflow failure is intentional evidence of an unsatisfied conjectured
strengthening, not a passing proof certificate. The original global
cross-fiber Hall inequality and weighted one-link inequality remain open.
