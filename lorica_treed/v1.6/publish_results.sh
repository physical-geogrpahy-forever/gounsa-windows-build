#!/usr/bin/env bash
# Commit a run's collected outputs to the results branch so they can be read
# with plain git (artifact blob downloads are not reachable from every client).
set -euo pipefail
SRC="$(cd "$1" && pwd)"
TAG="$2"
BR="lorica-treed-v1.6-landslide-recovery-results"
DEST="runs/${GITHUB_RUN_ID}_${TAG}"
WORK="$(mktemp -d)"
cd "$WORK"
git init -q
git config user.name "github-actions[bot]"
git config user.email "41898282+github-actions[bot]@users.noreply.github.com"
git remote add origin "https://x-access-token:${GH_TOKEN}@github.com/${GITHUB_REPOSITORY}.git"
for attempt in 1 2 3 4 5 6; do
  if git fetch -q --depth 1 origin "$BR" 2>/dev/null; then
    git checkout -q -B results FETCH_HEAD
  else
    git checkout -q --orphan results
    git rm -rfq . 2>/dev/null || true
  fi
  rm -rf "$DEST"; mkdir -p "$DEST"
  cp -r "$SRC"/. "$DEST"/
  printf 'workflow=%s\nrun_id=%s\nrun_attempt=%s\nsource_sha=%s\nsource_ref=%s\n' \
    "$GITHUB_WORKFLOW" "$GITHUB_RUN_ID" "$GITHUB_RUN_ATTEMPT" "$GITHUB_SHA" "$GITHUB_REF_NAME" > "$DEST/PROVENANCE.txt"
  git add -A
  git commit -qm "Results ${TAG}: run ${GITHUB_RUN_ID} from ${GITHUB_SHA}" || true
  if git push -q origin HEAD:"$BR"; then echo "PUBLISHED $DEST to $BR"; exit 0; fi
  sleep $((attempt * 7))
done
echo "publish failed" >&2
exit 1
