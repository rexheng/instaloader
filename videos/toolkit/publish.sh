#!/usr/bin/env bash
# publish.sh <episode_dir> [commit message]
# Safely commit + push ONE finished episode (videos/episodes/NNN-slug) to the shared branch.
#  - serialised across agents by a global flock (only one git writer at a time);
#  - stages only that directory (respecting .gitignore: review PNGs stay local);
#  - commits only that path (other agents' staged/unstaged work is left untouched);
#  - pushes; if the remote moved: git pull --rebase (autostash fallback) and retry,
#    with 2/4/8/16/32 s backoff on network errors.
# Env: SS_BRANCH (default claude/modest-bardeen-s6wt4b), SS_GIT_LOCK, SS_CLAUDE_SESSION.
set -euo pipefail
[[ $# -ge 1 ]] || { sed -n '2,10p' "$0" | sed 's/^# \{0,1\}//'; exit 2; }
EP="$(realpath "$1")"
[[ -d "$EP" ]] || { echo "publish.sh: no such directory: $1" >&2; exit 2; }
REPO="$(git -C "$EP" rev-parse --show-toplevel)"
REL="${EP#"$REPO"/}"
BRANCH="${SS_BRANCH:-claude/modest-bardeen-s6wt4b}"
SESSION="${SS_CLAUDE_SESSION:-https://claude.ai/code/session_01CK1RUDouoVchfitJJFdJT3}"
[[ "$REL" == videos/episodes/* ]] || { echo "publish.sh: expected videos/episodes/NNN-slug, got $REL" >&2; exit 2; }

cd "$REPO"
CUR="$(git rev-parse --abbrev-ref HEAD)"
[[ "$CUR" == "$BRANCH" ]] || { echo "publish.sh: checkout is on '$CUR', not '$BRANCH' — refusing" >&2; exit 2; }

# ---- pre-flight checks on the episode
[[ -f "$EP/final.mp4" ]] || echo "publish.sh: warning: $REL/final.mp4 missing" >&2
[[ -f "$EP/review/report.md" ]] || echo "publish.sh: warning: $REL/review/report.md missing" >&2
while IFS= read -r -d '' f; do
  sz=$(stat -c %s "$f")
  if (( sz > 95 * 1024 * 1024 )); then
    echo "publish.sh: $f is $((sz / 1048576)) MB (> 95 MB GitHub limit) — re-encode or exclude it" >&2; exit 1
  fi
done < <(find "$EP" -type f -print0)

LOCK="${SS_GIT_LOCK:-/tmp/sample_space_git.lock}"
exec {LFD}>>"$LOCK"
echo "publish.sh: waiting for git lock…"
flock -w 1800 "$LFD" || { echo "publish.sh: timed out waiting for $LOCK" >&2; exit 1; }

SLUG="$(basename "$EP")"
MSG="${2:-Publish episode $SLUG}"
git add -A -- "$REL"
if git diff --cached --quiet -- "$REL"; then
  echo "publish.sh: nothing new to commit in $REL"
else
  git commit -q -m "$MSG" -m "Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: $SESSION" -- "$REL"
  echo "publish.sh: committed $(git rev-parse --short HEAD) ($REL)"
fi

delay=2
for attempt in 1 2 3 4 5 6; do
  if out="$(git push -u origin "HEAD:$BRANCH" 2>&1)"; then
    echo "$out" | tail -n 2
    echo "publish.sh: pushed $REL to origin/$BRANCH"
    exit 0
  fi
  echo "$out" | tail -n 3 >&2
  if echo "$out" | grep -qiE "rejected|non-fast-forward|fetch first|stale info"; then
    echo "publish.sh: remote moved — rebasing onto origin/$BRANCH"
    if ! git pull -q --rebase origin "$BRANCH" 2>/dev/null; then
      git rebase --abort 2>/dev/null || true
      if ! git pull -q --rebase --autostash origin "$BRANCH"; then
        git rebase --abort 2>/dev/null || true
        echo "publish.sh: rebase failed (conflict?) — resolve manually; commit is local" >&2
        exit 1
      fi
    fi
  fi
  ((attempt < 6)) && { echo "publish.sh: retry in ${delay}s"; sleep "$delay"; delay=$((delay * 2)); }
done
echo "publish.sh: push failed after retries; commit is local, re-run publish.sh later" >&2
exit 1
