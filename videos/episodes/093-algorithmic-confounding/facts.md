# Episode 93 · Fact sheet

Every claim spoken or shown, how it was checked, and where it comes from.

## Real-world claims

| # | Claim (as used) | Verification | Source |
|---|---|---|---|
| 1 | Facebook's active-user graph in May 2011 had about 721 million active users | Paper, Introduction: "the entire social network of active members of Facebook in May 2011, a network then comprised of 721 million active users". "Active" = logged in during the last 28 days and had at least one friend | Ugander, Karrer, Backstrom & Marlow (2011), *The Anatomy of the Facebook Social Graph*, arXiv:1111.4503 (read in full text) |
| 2 | "The largest social network anyone had analyzed" | Paper: "To our knowledge, this is the largest social network ever analyzed." Worded as of 2011 | same |
| 3 | The degree distribution falls smoothly except a small kink near 20 friends | Paper: "nearly monotonically decreasing, except for a small anomaly near 20 friends" | same, Results / Fig. 1 |
| 4 | Facebook's own researchers explained the kink: the product pushed people with few friends to add more until they reached twenty | Paper: "This kink is due to forces within the Facebook product to encourage low friend count individuals in particular to gain more friends until they reach 20 friends." All four authors list Facebook, Palo Alto as affiliation | same |
| 5 | Hard cutoff at 5,000 because Facebook capped friend lists | Paper: "a clear cutoff at 5000 friends, a limit imposed by Facebook on the number of friends at the time of our measurements" | same |
| 6 | Users with 100 friends have average local clustering 0.14 | Paper: "for users with 100 friends, the average local clustering coefficient is 0.14" | same, Fig. 4a |
| 7 | About five times an instant-messaging network studied in 2008 | Paper: "approximately five times greater than the clustering coefficient found in a 2008 study analyzing the graph of MSN messenger correspondences, for the same neighborhood size [14]"; ref 14 = Leskovec & Horvitz (2008), "Planetary-scale views on a large instant-messaging network", Proc. WWW 2008 | same; Leskovec & Horvitz 2008 · WWW |
| 8 | Clustering of a person = links among their friends / possible pairs, k(k-1)/2 | Paper's own definition: "the percentage of possible friendships between their k friends (at most k(k-1)/2) are present" | same |
| 9 | "Algorithmic confounding" is Salganik's term; the platform shapes the data | Bit by Bit §2.3 lists "algorithmically confounded" as a characteristic of big data; uses the Ugander et al. 20-friend example ("tells us more about Facebook than about human behavior") | Salganik (2018), *Bit by Bit: Social Research in the Digital Age*, Princeton University Press, §2.3 (online open-review edition, bitbybitbook.com) |
| 10 | Facebook suggests friends of friends via "People You May Know", so transitivity in Facebook data is partly produced by the system; the theory is built in | Same section: transitivity "partly" induced by People You May Know suggesting friends of friends; performativity, "a theory changes the world in such a way that it brings the world more into line with the theory" | same |

The narration never claims a size for Facebook's own algorithmic share of clustering: it says the trace alone cannot split 0.14 into people and code.

## Simulated numbers (sim.py, deterministic, labelled "simulated" on screen)

Model: 48 people, 60 uniformly random starting friendships (seed 30, 5 isolates). Two copies. Each person, in a random order, adds exactly one new friend.
- Left, "random stranger": the new friend is a uniformly random non-friend.
- Right, "friend of a friend": pick one of your friends at random, then one of their friends who is not yet yours. (The 5 isolated people have no friend of a friend, so they get a random stranger, drawn in blue.)
No one in either copy has any preference for triangles. Metric: average local clustering (networkx `average_clustering`, nodes with < 2 friends count as 0).

| Quantity | Value | Shown/said as |
|---|---|---|
| Starting clustering (both copies) | 0.0389 | 0.04, "point oh four" |
| Random strangers, after 48 new friendships | 0.0873 | 0.09 |
| Friend-of-a-friend, after 48 new friendships | 0.4837 | 0.48 |
| Ratio | 5.5x | "more than five times" |
| Seed representativeness, 200 seeds | random mean 0.086 (5-95%: 0.044-0.138); fof mean 0.489 (0.409-0.570) | seed 30 sits at the means |
| Same rule, 5,000 people, 7,500 starting edges, 3 seeds | random 0.0006-0.0012; fof 0.389-0.395 | not used in narration |
| Same rule, 10,000 people, 15,000 starting edges | see big10k.txt | "ten thousand: 0.001 vs 0.39" only if confirmed |

Ego example (illustrative): k = 5 friends, 5*4/2 = 10 possible pairs, 2 linked: C = 2/10 = 0.2. One accepted friend-of-friend suggestion between two of them: the shared friend's k is unchanged, numerator 3: C = 3/10 = 0.3.

## Schematic curve

The opening degree curve is a schematic redraw (labelled on screen) with the qualitative features the paper reports: nearly monotone decrease with curvature on log-log axes, a small kink at 20, a cutoff at 5,000. No y-axis values are shown, so no numbers are implied.
