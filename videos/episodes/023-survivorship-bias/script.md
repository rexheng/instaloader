# Episode 23: Armor Where the Bullet Holes Aren't

**One idea:** when your data contain only survivors, compare what you see with what you *should* have seen; the shortfall (holes seen ÷ hits expected) measures what killed the units that never reached the dataset.

**Simulation (labelled "simulated" on screen):** a stylised four-engine bomber, top view. 400 sorties, each plane takes exactly one hit, uniformly over the silhouette (area shares: engines 17.4 %, fuselage 25.1 %, wings 46.3 %, tail 11.1 %). Hidden per-hit survival: engines 0.59, fuselage 0.94, wings 0.97, tail 0.94 (borrowed from the worked example in Mangel & Samaniego 1984). Campaign seed 25 → 356 return, 44 lost; holes on returners: engines 42, fuselage 91, wings 181, tail 42. Next campaign (seed 121, same fire for every armor option; armor makes hits in that part survivable): no armor 40 lost, armored wings 36, armored engines 12. See facts.md.

## Palette

| Colour | Meaning (whole episode) |
|---|---|
| BLUE | holes on planes that came home (the data you see) |
| RED | planes lost, and the holes they carried (the data you never see) |
| PURPLE | hits *expected* in a part if fire were uniform |
| YELLOW | focus: the part being discussed / armored |
| GRAY, DIM, INK | plane outline and fill, axes, text |

## Narration (beat by beat)

**Cold open (0:00–0:13)**: plane, blue dots land.
1. Four hundred bombers flew out, and each was hit once. These are the holes on the ones that came home.
2. You can add armor to one part: the engines, the fuselage, the wings, or the tail. Which one? [pause 2]  *(prediction hold; each part flashes yellow as named)*

**Stakes (0:13–0:24)**
3. Armor is heavy, so armor in the wrong place slows every plane and saves no one. In the Second World War, the military's instinct was to protect the parts that came back with the most hits. *(cite Wallis, 1980 · JASA)*

**Naive build (0:24–0:52)**
4. So count them. The wings carry a hundred and eighty one holes, the fuselage ninety one, the tail and the engines forty two each. *(region dots fly into bars)*
5. The wings take the most fire, so armor the wings.
6. Then fly the next four hundred sorties. With no armor, forty planes go down. With armored wings, thirty six.

**Fail (0:52–1:08)**
7. Four planes saved out of forty. The losses are happening somewhere else.
8. If you know this story, you picked the engines. But the engines are not bare: they carry forty two holes. How much more dangerous is an engine hit?

**Insight (1:08–2:05)**
9. Every hole on this plane belongs to a survivor. The forty four planes that went down took their holes with them. *(red dots fade in)*
10. Put those holes back, and the fire covers the plane evenly, the way random shots should. The missing holes were at the engines.
11. In a real war you never see the red. But you can predict it. The engines are seventeen percent of the plane's area, so about seventy of the four hundred hits should land there. Only forty two came home.
12. Holes seen, over hits expected: forty two out of seventy. A plane hit in the engine comes home sixty percent of the time.
13. Now the wings: a hundred and eighty one seen, out of a hundred and eighty five expected. Guess the ratio. [pause 1.5] Ninety eight percent. Every other part comes home more than ninety percent of the time.
14. So armor the engines, and fly the same next campaign. Losses fall from forty to twelve.

**Payoff (2:05–2:45)**
15. Abraham Wald worked out this comparison in nineteen forty three, in memos for the Statistical Research Group at Columbia. His method also handled planes hit many times. *(cite Wald, 1943 · SRG memoranda)*
16. In the example Mangel and Samaniego worked through in nineteen eighty four, an engine hit was survived fifty nine percent of the time, a fuselage hit ninety four. My simulation borrowed those numbers. *(cite Mangel & Samaniego, 1984 · JASA)*
17. The weak point is the expected count. Wald assumed hits land evenly, and proposed firing dummy bullets at real planes to check. If fire avoided the engines, fewer hits would be expected there, and the same forty two holes would look harmless. *(purple marker slides; ratio climbs to 0.91)*

**Landing (2:45–2:58)**
18. Look at the first picture again. The bare metal around these engines was the most important data on the plane.

## Sources
- Wald, A. (1943). *A Method of Estimating Plane Vulnerability Based on Damage of Survivors.* Statistical Research Group, Columbia University, memoranda; reprinted by the Center for Naval Analyses, CRC 432 (1980).
- Mangel, M. & Samaniego, F. J. (1984). Abraham Wald's Work on Aircraft Survivability. *JASA* 79(386):259–267.
- Wallis, W. A. (1980). Rejoinder to discussion of "The Statistical Research Group, 1942–1945", *JASA* 75(370), June 1980 (main article pp. 320–330; rejoinder quoted in Casselman, "The Legend of Abraham Wald", AMS Feature Column, 2016).
