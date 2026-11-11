# Branch lifecycle and safe retirement · 2026-11-11

This is the current snapshot supplement to the November 6 lifecycle record. The older file remains unchanged as a historical record.

## Live snapshot

As of 2026-11-11, GitHub branch enumeration returned **108 refs**: main plus 107 non-main refs. Prefix counts among the non-main refs:

| Prefix | Count |
|---|---:|
| research | 52 |
| audit | 44 |
| reconcile | 3 |
| maintenance | 2 |
| architecture | 1 |
| docs | 1 |
| feature | 1 |
| fix | 1 |
| pages-public-ready | 1 |
| release | 1 |
| **Total non-main** | **107** |

There were **12 open PRs** at snapshot time: #107, #106, #103, #84, #83, #82, #81, #80, #79, #74, #56 and #55. See the [repository handoff](REPOSITORY_HANDOFF_2026-11-11.md) for titles and exact branch-name inventory.

This inventory does not infer branch ancestry, merge status or mathematical value from branch names. It is a point-in-time list. The retirement script must use live refs and current open-PR state when executed.

## Safe retirement is already installed

- Script: [safe_prune_merged_branches.sh](../../scripts/safe_prune_merged_branches.sh)
- Manual workflow: [retire-merged-branches.yml](../../.github/workflows/retire-merged-branches.yml)
- Earlier lifecycle decisions and 72 historical candidate SHAs: [November 6 record](BRANCH_LIFECYCLE_2026-11-06.md)

The script protects main, all current open PR head and base branches, and named independent research branches. It only considers a branch if its exact fetched head is an ancestor of origin/main; it rechecks ancestry immediately before deletion and uses a force-with-lease SHA guard. Thus it retires redundant branch references, not unmerged research. The merged commits and their source files remain reachable from main.

## Execution

The workflow is manual only:

1. GitHub → Actions → **Retire fully merged branch references (manual approval)**.
2. Run dry-run and inspect the candidate/withheld output.
3. If correct, run retire and enter DELETE_MERGED_BRANCHES exactly.

The connector used for this repository update has no branch-delete or workflow-dispatch action. Therefore no deletion is claimed in this update. The installed Actions workflow is the supported mechanism; do not force-update refs to simulate deletion.

## Merge vs retire

- If a branch head is already an ancestor of main, its research commits are integrated; retire the redundant ref after the dry-run.
- If a branch is protected by an open PR, retain it until that PR is deliberately merged or closed and its content is reconciled.
- If a branch head is not an ancestor of main, preserve it. Review its mathematical contribution and source dossier first. Merge only if its content belongs in the canonical source tree and conflicts/assumptions have been reconciled.
- Do not merge all historical branches into one archive branch. That would combine unrelated code histories and could silently mix distinct mathematical models.
- Do not delete non-ancestor branches simply because they look old or are named audit/ or research/.

## Invariant

The repository's proof continuity is provided by the Observatory, source dossiers, immutable commit history and this handoff—not by retaining every redundant branch name. Conversely, the Observatory must link to the source records and preserve evidence status; it cannot replace missing source content with a narrative summary.
