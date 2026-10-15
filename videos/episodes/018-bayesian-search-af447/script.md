# Episode 18 · How Bayes Found a Plane at the Bottom of the Ocean

**One idea:** a failed search lowers the probability where you looked by the factor (1 − d), where d is your chance of having found it there, so silence is only as strong as your chance of hearing; when d is uncertain (the beacons may be dead), the "searched" area can stay the best bet.

## Palette (one hue, one meaning)
| Colour | Meaning |
|---|---|
| BLUE | probability that the wreck is there (map brightness, the p bar, p in equations) |
| YELLOW | the listening search: the zone, the ships, the day counter |
| PURPLE | d, the share a search would have caught (the "would have been heard" slice) |
| RED | the naive error: "cleared", probability forced to zero |
| GREEN | where the wreck actually was (ring + label, never colour alone) |
| GRAY / INK | route, circle, labels, citations |

## Narration (beats; ~480 words)

**Cold open (0:00–0:15)** — map on screen from frame 1: circle, last-position dot, route.
1. In June two thousand nine, Air France flight four four seven vanished over the Atlantic, somewhere inside this circle. Ships listened along its route for thirty-one days, and heard nothing from its black boxes.
2. Your next search uses sonar. Do you send it back into this zone, or out where nobody has listened yet? [pause 1.5]

**Stakes (0:15–0:30)**
3. Two hundred and twenty eight people were aboard, and the black boxes held the only record of why. Most people pick somewhere new. In August, the sonar went to a patch the ships had not covered. Nothing. A bigger sonar search the next spring found nothing either.

**Naive build (0:30–0:55)** — simulated heat map.
4. Picking somewhere new treats the zone as cleared. On this simulated map, brighter cells are likelier places for the wreck, and the zone starts with half of all the probability.
5. Cleared means zero. Wipe every cell in the zone, then rescale the rest so it adds up to one.

**Fail (0:55–1:15)**
6. The zone now reads exactly zero, and zero can never come back: no later evidence can multiply it up. Zeroing assumes the listening was perfect. The analysts who later studied it put the chance of hearing the beacons at seventy-seven percent.

**Insight (1:15–2:10)** — the bar picture → formula.
7. So draw the zone's share as this bar: p, one half. If the wreck is in the zone, the ships hear it with chance d. That makes this slice, p times d, the part a search could catch.
8. Silence rules out that slice, and only that slice. What's left adds up to one minus p d.
9. Rescale it back to one. The zone keeps p times one minus d, over one minus p d. With these numbers, about nineteen percent: dimmer, but alive.
10. And d is a guess too: a ninety percent chance of hearing a working beacon, discounted for beacons the crash might have destroyed. Suppose both beacons died on impact. [pause 1.2]
11. Then d is zero, the slice is empty, and a month of silence moves nothing. The zone is back to one half.

**Payoff (2:10–2:45)**
12. In twenty ten, French investigators asked Lawrence Stone's team at Metron to rebuild the map with Bayes, counting every failed search. Unsure of the beacons, they also computed a map that assumed the beacons had failed.
13. In April twenty eleven, the search began near the centre. Within a week, sonar robots found the wreck, inside the zone the ships had listened to. The recovered beacon, tested with a fully charged battery, made no sound.
14. The map didn't find the plane; the robots did. It told them where to start, and it was only as good as its guess for d.

**Landing (2:45–2:55)** — back to the cold-open framing; the wreck ring sits inside the yellow zone.
15. Those thirty-one days of silence said less about the ocean than about the beacons.

## Sources
- Stone, Keller, Kratzke & Strumpfer (2014), *Statistical Science* 29(1):69–80, doi:10.1214/13-STS420 — on screen.
- WHOI press release (April 2011), "WHOI-led team locates Air France wreckage" (AUVs); wreck coordinates via Wikipedia/BEA (map marker placement only). See facts.md.
