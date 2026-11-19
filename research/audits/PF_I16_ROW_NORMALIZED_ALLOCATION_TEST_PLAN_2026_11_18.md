# PF-I16: row-normalized capacity allocation diagnostics

Date: 2026-11-18/19

## The sufficient allocation

For a fiber family in a fixed first-crowded-cut block (X_k), let
[
N_k(F)=N(F)cap Y_k.
]
If every (N_k(F)) is nonempty, define
[
lambda_k(F,T)=rac{delta(F)}{|N_k(F)|}
quad(Tin N_k(F)).
]
Every fiber sends exactly (delta(F)). If every target load obeys
[
L_k(T)=sum_{Finmathcal F_k:Tin N_k(F)}
rac{delta(F)}{|N_k(F)|}le1,
]
then for every fiber family (S),
[
sum_{Fin S}delta(F)
=sum_{Tincup_{Fin S}N_k(F)}
sum_{substack{Fin S\Tin N_k(F)}}
rac{delta(F)}{|N_k(F)|}
leleft|cup_{Fin S}N_k(F)ight|.
]
Thus this is a valid sufficient condition for (BQH_k). An empty same-block row also makes this particular condition fail. The condition is not necessary for Hall.

A distinct, stronger global candidate uses the full row (N(F)) and load
[
L(T)=sum_{F:Tin N(F)}rac{delta(F)}{|N(F)|}.
]
If all global loads are at most one, full split-demand Hall follows. Failure of the global criterion does not by itself refute the blockwise criterion, because the denominators and target restrictions differ.

## Implemented diagnostics

Two exact rational diagnostics are present on branch `research/pf-i16-direct-mixed-hall-2026-11-18`:

1. Global full-row test:
   - Script: `research/verification/verify_pf_i16_row_normalized_target_load.py`
   - Workflow: `.github/workflows/pf-i16-row-normalized-target-load.yml`
   - Run: [44440846425](https://github.com/syncgravity/Singular-Boundary/actions/runs/44440846425)
   - Tests n=8 and n=10, computes full (N(F)), and preserves the first overloaded target plus its incident fibers if it fails.
   - This workflow is still running. Its implementation currently uses a representative child to form each fiber row; it should be read as a diagnostic of the serialized relation primitives, not as an independent relation implementation.

2. Blockwise same-cut test:
   - Script: `research/verification/verify_pf_i16_row_normalized_split_demand.py`
   - Workflow: `.github/workflows/pf-i16-row-normalized-split-demand.yml`
   - Run: [44440991439](https://github.com/syncgravity/Singular-Boundary/actions/runs/44440991439)
   - Tests n=6, 8, and 10. It partitions fibers by their first crowded odd cut (k), restricts each row to (N_k(F)), asserts common retained rows across all child sources in a fiber, and accumulates exact rational target loads. It records empty rows and the complete incident-fiber list for a maximum overloaded target.
   - This workflow is still running.

Both runs are targeted tests of a named sufficient allocation, not all-orders proof attempts. They were launched because either outcome changes the next proof strategy: a pass would motivate proving a structural target-load bound; a failure would reject only that allocation and supply an exact witness.

## Interpretation rules

- A finite pass at n=6,8,10 is finite evidence only.
- A global-load failure rejects the full-row RNL criterion, not (BQH_k).
- A blockwise-load failure rejects the blockwise RNL criterion, not (BQH_k), split-demand Hall, or source-level Hall.
- Neither test is a max-flow test; neither can establish Hall unless its sufficient load bound passes.
- The full weighted dual (MR), equivalently arbitrary-family (BQH_k), remains the theorem.

## Proof boundary

The exact demand formula
[
delta(p,J)=rac{a(p,J)}{d(p)}+rac{b(p,J)}{d(p)+1}
]
and the all-orders noncrossing cut recursion / crossing-leaf localization remain available. No all-orders target-load estimate has been proved. No Yang--Mills mass-gap claim follows.
