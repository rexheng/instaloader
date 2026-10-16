export const meta = {
  name: 'sample-space-episodes',
  description: 'Produce Sample Space episodes: producer, then 2 independent harsh critics, revise until both score >= 9/10, then publish',
  whenToUse: 'Producing and reviewing Sample Space educational video episodes listed in videos/curriculum.json (args: {episodes:[ids], maxRounds})',
  phases: [
    { title: 'Produce', detail: 'research, script, animate, voice, render, self-check' },
    { title: 'Critique', detail: 'two independent harsh critics per round against videos/BAR.md' },
    { title: 'Revise', detail: 'producer applies every fix and re-renders' },
    { title: 'Publish', detail: 'commit + push the passed episode' },
  ],
}

const REPO = (args && args.repo) || '/home/user/instaloader'
const EPISODES = (args && args.episodes) || []
const MAX_ROUNDS = (args && args.maxRounds) || 5
const PASS = 9.0
const LENSES = ['craft', 'substance']

const PRODUCER_SCHEMA = {
  type: 'object',
  properties: {
    episode_dir: { type: 'string', description: 'repo-relative, e.g. videos/episodes/002-slug' },
    final_mp4: { type: 'string' },
    title: { type: 'string' },
    runtime_s: { type: 'number' },
    self_score: { type: 'number', description: 'your honest BAR score estimate' },
    changes: { type: 'string', description: 'what you built or changed this pass (<=120 words)' },
    unresolved: { type: 'array', items: { type: 'string' } },
  },
  required: ['episode_dir', 'final_mp4', 'title', 'runtime_s', 'self_score', 'changes', 'unresolved'],
}

const CRITIC_SCHEMA = {
  type: 'object',
  properties: {
    scores: {
      type: 'object',
      properties: {
        hook: { type: 'number' }, clarity: { type: 'number' }, visual: { type: 'number' },
        motion: { type: 'number' }, audio: { type: 'number' }, concision: { type: 'number' },
        originality: { type: 'number' },
      },
      required: ['hook', 'clarity', 'visual', 'motion', 'audio', 'concision', 'originality'],
    },
    weighted: { type: 'number' },
    caps: { type: 'array', items: { type: 'string' }, description: 'triggered caps with evidence + timestamp' },
    final: { type: 'number', description: 'after ceiling rule and caps' },
    pass: { type: 'boolean' },
    factual_errors: { type: 'array', items: { type: 'string' } },
    fixes: { type: 'array', items: { type: 'string' }, description: 'highest impact first; [mm:ss][Dimension] problem -> exact change' },
    keep: { type: 'array', items: { type: 'string' } },
    reaches9_if_fixed: { type: 'boolean' },
    summary: { type: 'string', description: '<=80 words' },
  },
  required: ['scores', 'weighted', 'caps', 'final', 'pass', 'factual_errors', 'fixes', 'keep', 'reaches9_if_fixed', 'summary'],
}

const pad = (n) => String(n).padStart(3, '0')

const COMMON = `Project: "Sample Space", a series of 100 short (2:30-4:00) educational videos on data science and computational social science, in the style of 3Blue1Brown (Manim, precise visual intuition), Veritasium (misconception-first narrative, real sources) and StuffMadeHere (build the naive thing, watch it fail by a measured amount, iterate). Every episode has a synthesized voiceover (local Kokoro TTS) synced to the animation.
Repository: ${REPO} (git branch claude/modest-bardeen-s6wt4b, already checked out). The quality bar and scoring rubric is videos/BAR.md. The toolkit and how-to is videos/toolkit/PRODUCTION_GUIDE.md (render.sh, review_kit.sh, the sample_space Python package with NarratedScene/style/voice). The episode plan is videos/curriculum.json. The environment is already set up (if manim or the TTS model is missing, run videos/toolkit/setup.sh). Other agents are producing other episodes concurrently on this machine: touch only your own episode directory, always render through videos/toolkit/render.sh (it queues renders so the 4 CPUs are shared), and never git commit/push (a publish step does that).`

function producerPrompt(id) {
  return `${COMMON}

You are the writer, director and animator of episode ${id}. Make it a video that a harsh critic holding it to 3Blue1Brown/Veritasium standards scores >= 9.0 under BAR.md. Two independent critics (a motion-design/craft critic and a science+story editor who fact-checks everything) will score it; both must give >= 9.0.

1. Read videos/BAR.md in full, videos/toolkit/PRODUCTION_GUIDE.md in full, videos/toolkit/demo/ (scene + how it uses the API), and the curriculum.json entry with id ${id}. If any episode under videos/episodes/ already has a REVIEW.md marked PASS, skim its script.md and scene.py for the house style (do not copy its content).
2. Create your episode directory videos/episodes/${pad(id)}-<slug from curriculum>/. If it already exists with files from an earlier, interrupted attempt (script.md, facts.md, scene.py, final.mp4, review/), do NOT start over: read them, keep what is good, and continue from where it stopped (re-render only if needed).
3. Research and fact-check first (use web search/fetch tools via ToolSearch, e.g. WebSearch/WebFetch or the Firecrawl tools). Verify the hook, every number, and the real-world anchor (authors, year, venue, finding). Recompute every number you will show with a quick numpy simulation or exact calculation. Write facts.md: each claim, its verification, its source. Never fabricate; if something cannot be verified, cut it or state it with appropriate uncertainty. Mark simulated data as "simulated" on screen.
4. Write script.md following BAR §6 (cold open by 0:12 that makes the viewer commit to a likely-wrong prediction, naive build, measured failure, the one visual insight with the formula emerging from the picture, a real cited payoff, a landing that re-sees the opening). Target 2:45-3:30 at ~150 wpm (roughly 410-520 words). Include a palette block (colour -> one meaning). Write for the ear: say numbers and symbols the way a person would ("a hundred and twenty", "p less than point oh five"). Zero BAR §4 banned phrases/patterns. Every sentence must point at something visible. One idea only.
5. Write scene.py (class Episode(NarratedScene)) implementing the script: objects persist and transform (TransformFromCopy / TransformMatchingTex / ValueTracker-driven updates), deictic words ("this bar") land via beat.until("word"), equations built from their visual referents, a planned prediction pause, on-screen citation(s), no prose paragraphs, nothing outside the safe area, nothing overlapping, nothing static > 4 s, nothing too fast to read. Aim for frames people would screenshot to teach from: a clear focal point, generous negative space used deliberately, consistent semantic colour. Avoid generic looks (title card + bullets, icons, decorative motion).
6. Iterate with --preview renders, then render the 1080p master to <episode_dir>/final.mp4 via render.sh; fix every [sample_space] WARNING. Run videos/toolkit/review_kit.sh <episode_dir>/final.mp4 <episode_dir>/review --narration <episode_dir>/narration.json and read review/report.md, then actually LOOK at every contact sheet and at least 8 keyframes with the Read tool. Be your own harshest critic: fix overlaps, cramped or unbalanced layouts, tiny text, mistimed deictics, flags in the report, mispronunciations (whisper mishears = mispronounced; add a pronunciation override), slack beats. Re-render and re-check until you honestly believe it scores >= 9 on every BAR dimension. Be efficient: typically 2-4 master renders.
7. Return the structured result (repo-relative paths).`
}

function criticPrompt(id, prod, lens, round) {
  const lensText = lens === 'craft'
    ? 'You are a veteran motion designer and 3Blue1Brown-style animator. Your emphasis: visual design (composition, typography, hierarchy, colour semantics, safe area, overlaps, clutter, negative space), motion and animation craft (do transforms carry meaning? pacing, easing, reading time, static stretches), and audio/visual sync (do spoken references land on what is visible?). You still score every dimension.'
    : 'You are a science editor and story editor at a top educational channel (think Veritasium\'s research team). Your emphasis: factual and mathematical correctness (independently recompute every number, re-derive every formula, and verify every citation with web search: author, year, venue, finding), the hook and narrative tension, clarity of the explanation, concision, originality, and AI-slop detection (BAR §4) in the transcript. You still score every dimension.'
  return `${COMMON}

${lensText}
You are an independent, harsh critic for episode ${id} ("${prod.title}"), review round ${round}. You did not make this video and owe its makers nothing. The bar is 3Blue1Brown and Veritasium at their best. A 9 means "I would believe a top educational channel's small team made this; only nitpicks remain". When in doubt, score lower. But be fair: every deduction must cite evidence (timestamp/frame), and do not invent defects your evidence cannot show.

Episode directory: ${prod.episode_dir} (final video: ${prod.final_mp4}; also script.md, facts.md, scene.py, narration.txt).
1. Read videos/BAR.md in full and follow its §7 critic protocol exactly, including its scoring computation (weighted, ceiling rule, hard caps).
2. Evidence: if ${prod.episode_dir}/review/metrics.json is older than final.mp4 or missing, generate your own pack: videos/toolkit/review_kit.sh ${prod.final_mp4} ${prod.episode_dir}/review/r${round}-${lens} --narration ${prod.episode_dir}/narration.json ; otherwise use ${prod.episode_dir}/review. Read report.md, EVERY contact sheet, and at least 10 full-resolution keyframes with the Read tool (more where something looks off; you may extract extra frames with ffmpeg at specific timestamps into /tmp). Read the transcript and script.
3. Write your review in the BAR §7 output format to ${prod.episode_dir}/reviews/round${round}-${lens}.md (create the folder). Do not modify any other file.
4. Return the structured result. Fixes must be specific and executable (timestamp, dimension, problem, exact change), highest impact first. If even all fixes would not reach 9, say what structural change is needed.`
}

function revisePrompt(id, prod, crits, round) {
  const fb = crits.map((c, i) => `--- Critic ${LENSES[i] || i} (final ${c.final}; ${c.pass ? 'pass' : 'FAIL'}) ---
Scores: ${JSON.stringify(c.scores)}
Caps: ${c.caps.join(' | ') || 'none'}
Factual errors: ${c.factual_errors.join(' | ') || 'none'}
Fixes:
${c.fixes.map((f, k) => `${k + 1}. ${f}`).join('\n')}
Keep: ${c.keep.join(' | ')}
Reaches 9 if fixed: ${c.reaches9_if_fixed}. Summary: ${c.summary}`).join('\n\n')
  return `${COMMON}

You are the writer, director and animator of episode ${id} ("${prod.title}"), in ${prod.episode_dir}. Round ${round} of independent review did not pass (both critics must give >= 9.0). Their full reviews are in ${prod.episode_dir}/reviews/round${round}-*.md. Feedback:

${fb}

Revise the episode so that fresh, independent critics will score it >= 9.0:
1. Read videos/BAR.md and videos/toolkit/PRODUCTION_GUIDE.md again, then your script.md, facts.md, scene.py and the reviews.
2. Treat every factual-error claim seriously: re-verify with sources. If the critic is right, fix it everywhere (narration, on-screen, facts.md). If the critic is wrong, keep it but strengthen the on-screen sourcing and record the evidence in facts.md.
3. Apply every fix (or a better solution to the same problem). If a critic says the structure cannot reach 9, restructure rather than polish. Preserve the "keep" items.
4. Re-render the master to ${prod.final_mp4} via render.sh, regenerate ${prod.episode_dir}/review with review_kit.sh (--narration ${prod.episode_dir}/narration.json), then LOOK at every contact sheet and the keyframes around every fixed timestamp with the Read tool. Verify each fix landed and nothing new broke. Iterate until it is >= 9 by your honest reading of BAR.md.
5. Append a short "Round ${round} revisions" section to ${prod.episode_dir}/CHANGELOG.md. Return the structured result.`
}

function publishPrompt(id, prod, history) {
  const rows = history.map(h => `| ${h.round} | ${h.scores.join(' / ')} | ${h.pass ? 'PASS' : 'fail'} |`).join('\n')
  return `In ${REPO}: write ${prod.episode_dir}/REVIEW.md containing exactly this (fill nothing else in):

# Episode ${id}: ${prod.title}

**Status: PASS** (independent critics, both >= 9.0 under videos/BAR.md)

| Round | Critic scores (craft / substance) | Result |
|---|---|---|
${rows}

Full critic reviews: reviews/

Then run: videos/toolkit/publish.sh ${prod.episode_dir}
If publish.sh fails, read its output, fix the cause (only within ${prod.episode_dir}, e.g. a file too large or a stray untracked file), and retry. Return one line: the commit hash pushed, or the error.`
}

async function runEpisode(item) {
  // item is either an episode id, or {id, dir, title, startRound} to resume an episode that already
  // has a master render and earlier critic rounds (skips the producer; round numbers continue).
  const id = typeof item === 'object' ? item.id : item
  const startRound = (typeof item === 'object' && item.startRound) || 1
  let prod
  if (typeof item === 'object' && item.dir && startRound > 1) {
    prod = { episode_dir: item.dir, final_mp4: `${item.dir}/final.mp4`, title: item.title || `Episode ${id}`, runtime_s: 0, self_score: 0, changes: 'resumed', unresolved: [] }
  } else {
    prod = await agent(producerPrompt(id), { label: `produce:${id}`, phase: 'Produce', schema: PRODUCER_SCHEMA })
  }
  if (!prod) return { id, status: 'producer_failed' }
  const history = []
  for (let round = startRound; round < startRound + MAX_ROUNDS; round++) {
    const crits = await parallel(LENSES.map(lens => () =>
      agent(criticPrompt(id, prod, lens, round), { label: `critic:${id}:${lens}:r${round}`, phase: 'Critique', schema: CRITIC_SCHEMA, effort: 'high' })))
    const ok = crits.filter(Boolean)
    const scores = crits.map(c => (c ? c.final : 'n/a'))
    if (ok.length < LENSES.length) {
      log(`ep ${id} round ${round}: a critic did not return (likely usage limit) -> interrupted`)
      return { id, status: 'interrupted', stage: `critique r${round}`, history, dir: prod.episode_dir, title: prod.title }
    }
    const pass = ok.length === LENSES.length && ok.every(c => c.pass && c.final >= PASS)
    history.push({ round, scores, pass })
    log(`ep ${id} round ${round}: craft ${scores[0]} / substance ${scores[1]} -> ${pass ? 'PASS' : 'revise'}`)
    if (pass) {
      const pub = await agent(publishPrompt(id, prod, history), { label: `publish:${id}`, phase: 'Publish', effort: 'low' })
      return { id, status: 'passed', rounds: round, history, dir: prod.episode_dir, title: prod.title, publish: pub }
    }
    if (round === startRound + MAX_ROUNDS - 1) break
    const next = await agent(revisePrompt(id, prod, ok, round), { label: `revise:${id}:r${round}`, phase: 'Revise', schema: PRODUCER_SCHEMA })
    if (!next) return { id, status: 'interrupted', stage: `revise r${round}`, history, dir: prod.episode_dir, title: prod.title }
    prod = next
  }
  return { id, status: 'not_passed', history, dir: prod.episode_dir, title: prod.title }
}

const results = await pipeline(EPISODES, runEpisode)
const passed = results.filter(r => r && r.status === 'passed').length
log(`${passed}/${EPISODES.length} episodes passed`)
return results