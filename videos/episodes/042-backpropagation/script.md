# 042 · How a Network Learns: Passing the Blame Backward

**Idea (one sentence):** When you run the chain rule backward from the loss, the downstream work that every weight shares gets computed only once, so a million slopes cost about three runs of the network instead of a million and one.

## Palette (colour → one meaning)
- **BLUE**: forward values, the numbers a run computes from left to right
- **RED**: blame, the slope of the loss with respect to a value or weight (∂L/∂·), flowing right to left
- **YELLOW**: focus: the weight being nudged, or the stretch or term under discussion
- **PURPLE**: cost, counted in runs of the network
- INK = text, weights and symbols · GRAY = graph structure, nudge estimates · DIM = edges at rest

## Beats (narration exactly as spoken)

**Cold open (0:00–0:15)**: schematic layered network, header "N = 10⁶ weights (schematic)", one edge turns yellow, red ∂L/∂w, purple "runs = ?"
1. This network has a million weights. Training needs the same number from each one: how fast the error changes when that weight moves.
2. That's a million slopes. How many runs of the network does it take to get them all? Make a guess. [pause 1.5]

**Stakes**
3. Training repeats this step thousands of times, so this one count decides whether big networks can be trained at all.

**Naive build (toy network: x = 2 and 1, weights 1, 0.5, 2, target 3)**
4. Shrink it to three weights. Two inputs, two and one, each times a weight, then summed, passed through a ReLU, and scaled by a third weight.
5. The output is five, the target is three, and the loss, the squared miss, is four.
6. The obvious way to get a slope is to nudge. Raise w one by one hundredth and run everything again. The loss rises to four point one six one six, so the slope is about sixteen point one six.
7. Repeat for each weight. Three weights cost four runs.

**Fail**
8. Now scale back up. A million weights cost a million and one runs, for a single step. And sixteen point one six is not even the true slope.
9. Here is the waste. Every rerun recomputed this same stretch: the sum, the ReLU, the output, the loss.

**Insight: blame flows backward**
10. So ask once, from the far end, and walk backward. The loss is y minus three, squared, so its slope in y is two times y minus three, which is four. Call that y's blame.
11. At this multiply, y is v times h. Nudge h, and y moves twice as much, so h's blame is four times two, eight. And v's blame is four times h, ten.
12. The ReLU is on, so its slope is one, and the eight passes straight through. The plus node hands that same eight to both branches.
13. w two's input is one. What blame does it get? [pause 1.5]
14. Eight times one, eight. And w one gets eight times two: sixteen exactly, the value the nudging only approximated.
15. Line up the factors along w one's path: four, two, one, two. Each is one node's local slope, and their product is the chain rule, read from the loss backward.
16. The first three factors make the eight, and every weight feeding this sum shares them. Going backward, that shared part is computed once.

**Honest limit**
17. The price is memory. v's blame needed h, a value from the forward run, so training must keep every forward value until the blame comes back for it.

**Payoff**
18. In the big network, one backward sweep hands every weight its blame. That sweep costs about two forward runs, so all million slopes cost about three runs, not a million and one.
19. The method was first published by Linnainmaa in nineteen seventy, applied to networks by Werbos, and made famous by Rumelhart, Hinton and Williams in nineteen eighty six.
20. Today, the standard compute budget for a large language model counts six operations per weight per token: two forward, four backward.

**Landing**
21. So if you guessed a million, you were off by about three hundred thousand times. The loss can tell every weight its share of the blame in one trip back.

## On-screen citations
- Linnainmaa 1970 · MSc thesis, Helsinki | Werbos 1974 · PhD thesis, Harvard (NN use 1982) | Rumelhart, Hinton & Williams 1986 · Nature
- Kaplan et al., 2020 · arXiv:2001.08361 (backward ≈ 2× forward; C ≈ 6N per token)
- Toy network numbers are a worked example, labelled "toy network".

## Sources
See facts.md.
