#!/usr/bin/env bash
# The Singular Boundary: safe retired-branch cleanup. Dry-run by default.
# Never deletes unmerged heads, the default branch, open PR heads/bases, or independent work.
set -euo pipefail
mode="${1:---dry-run}"
case "$mode" in --dry-run|--delete) ;; *) echo "Usage: bash scripts/safe_prune_merged_branches.sh [--dry-run|--delete]" >&2; exit 2;; esac
[[ "$(git rev-parse --is-inside-work-tree 2>/dev/null || true)" == true ]] || { echo 'Run in a Git checkout' >&2; exit 2; }
remote="$(git remote get-url origin)"
case "$remote" in
 *github.com*syncgravity/singular-boundary|*github.com*syncgravity/singular-boundary.git) ;;
 *) echo 'REFUSING: origin is not syncgravity/singular-boundary' >&2; exit 2;;
esac
if [[ "$mode" == '--delete' ]]; then
 [[ "$(git branch --show-current)" == main ]] || { echo 'Switch to main' >&2; exit 2; }
 git diff --quiet && git diff --cached --quiet || { echo 'Working tree is modified' >&2; exit 2; }
 echo "Type DELETE to permit deleting only SHA-verified merged branches: "
 read -r answer
 [[ "$answer" == DELETE ]] || { echo 'Cancelled'; exit 0; }
fi
git fetch origin '+refs/heads/*:refs/remotes/origin/*' --prune --quiet
main_ref=refs/remotes/origin/main
git show-ref --verify --quiet "$main_ref" || { echo 'Cannot verify origin/main' >&2; exit 2; }
echo "main $(git rev-parse "$main_ref")"
declare -A open_pr_branches=()
if command -v gh >/dev/null 2>&1 && gh auth status >/dev/null 2>&1; then
 while IFS= read -r name; do [[ -n "$name" ]] && open_pr_branches["$name"]=1; done < <(gh pr list --repo syncgravity/singular-boundary --state open --limit 500 --json headRefName,baseRefName --jq '.[] | .headRefName, .baseRefName')
elif [[ "$mode" == '--delete' ]]; then
 echo 'REFUSING deletion without authenticated gh PR status; install/login gh or run via GitHub Actions.' >&2
 exit 2
fi
declare -a eligible=() withheld=()
while IFS= read -r remote_branch; do
 name="${remote_branch#origin/}"
 [[ "$name" != "$remote_branch" ]] || continue
 case "$name" in
   HEAD|main) continue;;
   audit/2026-11-04-quantitative-local-fsum|audit/2026-11-05-p0-refinement-p4-source-visible|audit/2026-11-06-nonabelian-tube-complete-theorem-index|audit/2026-11-06-nonabelian-homogeneous-and-theorem-index)
      withheld+=("$name"); continue;;
 esac
 if [[ -n "${open_pr_branches[$name]:-}" ]]; then withheld+=("$name"); continue; fi
 if git merge-base --is-ancestor "refs/remotes/origin/$name" "$main_ref"; then
   eligible+=("$name")
 else
   withheld+=("$name")
 fi
done < <(git for-each-ref --format='%(refname:short)' refs/remotes/origin)
echo "Merged/ancestry verified: ${#eligible[@]}"
echo "Protected or unmerged: ${#withheld[@]}"
printf 'ELIGIBLE %s\n' "${eligible[@]}"
printf 'WITHHELD %s\n' "${withheld[@]}"
if [[ "$mode" == '--dry-run' ]]; then echo 'DRY RUN ONLY: no refs deleted'; exit 0; fi
fail=0
for name in "${eligible[@]}"; do
 sha="$(git rev-parse "refs/remotes/origin/$name")"
 git merge-base --is-ancestor "$sha" "$main_ref" || { echo "SKIP (not merged): $name"; continue; }
 if git push --porcelain "--force-with-lease=refs/heads/$name:$sha" origin ":refs/heads/$name"; then
   echo "RETIRED $name $sha"
 else
   echo "FAILED to retire $name" >&2
   fail=1
 fi
done
if [[ $fail != 0 ]]; then exit 1; fi
echo 'Complete. Unmerged/protected research refs retained. Merged commits remain in main.'
