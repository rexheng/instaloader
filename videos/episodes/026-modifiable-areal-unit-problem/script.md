# Episode 26 — Redraw the Lines, Reverse the Result

**One idea:** a correlation computed on regions only sees how the region *averages* line up, so whoever draws the regions decides how the county-level co-variation is split between "inside regions" (deleted by averaging) and "between regions" (kept); the same 99 Iowa counties can therefore give almost any regional correlation (the modifiable areal unit problem).

Target ≈ 3:20, ≈ 500 words.

## Palette (colour → one meaning, whole episode)

| Colour | Meaning |
|---|---|
| BLUE | counties: the 99 county dots, county-level r, the *within-region* term (county → its region average) |
| YELLOW | regions: region-average dots, regional r, the *between-region* term (region average → state average), region borders being judged |
| PURPLE | the benchmark: random six-region maps (histogram) |
| INK / GRAY / DIM | text, axes and map outlines, de-emphasised context |

RED and GREEN are not used.

## Beats (narration exactly as spoken; [visual] notes)

**Cold open (0:00–0:12)**
1. "Iowa's ninety-nine counties. Across them, the share of people over sixty and the Republican vote correlate at point three five." [real county outlines draw; variable labels with years; r = 0.35 in BLUE; citation Openshaw & Taylor 1979]
2. "Merge the counties into six regions and recompute. How far could that number move? [pause 1.5]" [six region borders draw in YELLOW; number line −1…+1 with the BLUE 0.35 tick and a YELLOW "?"; prediction hold]

**Stakes**
3. "Same people, same votes, just bigger boxes. Every study of places, from census tracts to voting districts, runs on boxes somebody drew." [borders trace; map shrinks left]

**Naive build (simulated Iowa)**
4. "We don't have their county file, so here is a simulated Iowa: the real county shapes, with made-up values that correlate at the same point three five." [scatter of 99 BLUE dots, "simulated" tag]
5. "First, the plainest map: six east-west bands. Average each band, and its counties collapse into one dot." [band borders; dots slide into six YELLOW dots]
6. "Six dots. Their correlation is minus point six eight. The sign flipped." [YELLOW r readout]
7. "Now six north-south strips instead. Plus point nine four." [dots re-expand and collapse to new averages]

**Fail, measured**
8. "Two plain maps of the same counties, a gap of one point six two. Neither lands near point three five." [number line: BLUE 0.35, YELLOW −0.68 and +0.94, gap bracket]

**Iterate: aim the lines**
9. "So aim. Stan Openshaw wrote a program for this: move one border county at a time, keep every region connected, keep any move that raises the correlation." [borders morph county by county; live r climbs]
10. "Plus one, to two decimals. Flip the goal, and the same counties give minus one." [climb ends at +1.00; reverse run to −1.00]

**Insight**
11. "The counties never changed, so look inside one region." [one region highlighted on the scatter; others dimmed]
12. "Each county's distance from the state average splits in two: county to region average, in blue, then region average to state average, in yellow." [BLUE arrows dot → region dot; YELLOW arrow region dot → state-average cross]
13. "Add those products over all ninety-nine counties, and the total co-variation splits the same way: within regions, plus between regions." [equation C_total = C_within + C_between built from the arrows]
14. "The six region dots carry only the between term. Averaging deletes the within term." [between flagged, within dimmed]
15. "The total is fixed by the counties. So to drag the regional correlation negative, where must the positive part go? [pause 1.5]" [prediction hold]
16. "Inside the regions. On this map, within is a hundred and thirty-nine percent of the total, and between is minus thirty-nine." [tip-to-tail arrows: BLUE within, YELLOW between, ending on the pinned total]
17. "Replay the climb, and the split slides while the total stays pinned." [arrows animate along the optimiser trajectory; regional r follows]
18. "That is the modifiable areal unit problem. The zoning sets the split, and the scale sets the room: fewer, bigger regions leave more." [term label; "zoning" and "scale" tags]

**Payoff (real data)**
19. "On the real Iowa data, Openshaw's program found six-region maps from minus point nine nine to plus point nine nine. With fifty-four regions, the range narrowed to minus point four two through plus point eight two." [two intervals on the −1…+1 line; citation Openshaw 1984, CATMOG 38, Table 11]
20. "Those extremes were hunted for. Ten thousand random six-region maps of the real counties averaged point three six, give or take point two two." [PURPLE histogram of 10,000 simulated random maps; real numbers as a label; citation Table 7]
21. "That spread is the honest yardstick. Redistricting analysts now judge a proposed map against thousands of random legal maps, and North Carolina's enacted congressional plans landed far outside them." [YELLOW marker for the hunted map far left of the PURPLE histogram; citation Herschlag et al. 2020]

**Landing**
22. "So how far could point three five move? Nearly end to end. A correlation between places describes the lines as much as the people inside them." [back to map + number line; YELLOW interval spans −0.99 … +0.99]

## Sources
- Openshaw, S. (1984). *The Modifiable Areal Unit Problem*. CATMOG 38, Geo Books, Norwich. pp. 15–23, Tables 7 and 11.
- Openshaw, S. & Taylor, P. J. (1979). A million or so correlation coefficients: three experiments on the modifiable areal unit problem. In N. Wrigley (ed.), *Statistical Applications in the Spatial Sciences*, Pion, London, 127–144.
- Herschlag, G., Kang, H. S., Luo, J., Graves, C. V., Bangia, S., Ravier, R. & Mattingly, J. C. (2020). Quantifying gerrymandering in North Carolina. *Statistics and Public Policy* 7(1), 30–38.
- County outlines: us-atlas 3.0.1 (US Census Bureau cartographic boundary files). All county values in the scatter are simulated (prep.py, seed 14).
