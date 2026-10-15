# Sample Space: Episode Guide

100 short (2.5-4 minute) videos on data science and computational social science.
Each episode is one idea: a true, surprising cold open (Veritasium), a central Manim animation (3Blue1Brown),
and a build-it, watch-it-fail, fix-it-and-measure segment (StuffMadeHere).
Episode numbers give the suggested viewing order; later episodes build on earlier ones.
Full production fields (core insight, key visual, build/fail/iterate, real-world anchor, accuracy pitfalls)
are in `curriculum.json`.

## Areas

| Area | Episodes | IDs |
|---|---:|---|
| [Probability & Randomness](#probability--randomness) | 8 | 1-8 |
| [Statistical Inference](#statistical-inference) | 11 | 9-19 |
| [Data Traps & Measurement](#data-traps--measurement) | 10 | 20-29 |
| [Machine Learning](#machine-learning) | 18 | 30-47 |
| [Causal Inference & Experiments](#causal-inference--experiments) | 11 | 48-57, 66 |
| [Networks](#networks) | 8 | 58-65 |
| [Contagion & Collective Behavior](#contagion--collective-behavior) | 8 | 67-74 |
| [Agent-Based Models & Inequality](#agent-based-models--inequality) | 6 | 75-80 |
| [Text as Data](#text-as-data) | 8 | 81-88 |
| [Surveys & Digital Traces](#surveys--digital-traces) | 5 | 89-93 |
| [Privacy, Fairness & Ethics](#privacy-fairness--ethics) | 7 | 94-100 |
| **Total** | **100** | |

## Probability & Randomness

| # | Title | Hook |
|---:|---|---|
| 1 | Three Right Answers to One Probability Question | Pick a 'random' chord of a circle: is it longer than a side of the inscribed equilateral triangle? Three perfectly reasonable methods give 1/3, 1/2 and 1/4, and none of them is wrong. |
| 2 | When a 99% Accurate Test Says You're Sick | A disease affects 1 in 1,000 people, and a test catches 99% of cases with a 1% false-positive rate. If you test positive, the chance you actually have the disease is about 9%. |
| 3 | Randomness Looks Clumpier Than You Think | During the 1944 flying-bomb attacks on London, many people believed the bombs were targeting particular neighborhoods because the hits seemed to cluster. A statistician showed the clusters were just what pure chance predicts. |
| 4 | The Hidden Bias That Hid the Hot Hand | Flip a fair coin four times and record the fraction of heads that immediately follow a heads. Averaged over all possible sequences, that fraction is not 50%; it is about 40.5%. |
| 5 | Why Random Darts Beat Grids in 100 Dimensions | To integrate a function in 20 dimensions with just 10 grid points per axis, you would need 10^20 evaluations. Random sampling gets a usable answer with thousands, and its error shrinks at the same rate in any dimension. |
| 6 | Seven Shuffles: When a Deck Suddenly Becomes Random | Riffle-shuffle a deck four times and it is still far from random; a magician can exploit what is left. Around seven shuffles the deck becomes close to random, and the distance to randomness drops off a cliff rather than fading smoothly. |
| 7 | How Much Information Is in a Letter? | With 26 letters, each one should carry log2(26), about 4.7 bits. Shannon estimated that printed English carries only around one bit per letter: most of what you read is predictable. |
| 8 | The Distance That Isn't Symmetric | KL divergence is often called a 'distance' between probability distributions, yet the divergence from A to B can differ wildly from B to A. Which direction you minimize decides whether a model covers every possibility or confidently picks one. |

## Statistical Inference

| # | Title | Hook |
|---:|---|---|
| 9 | Why Bell Curves Are Everywhere, and When They're Not | Collecting more data does not make your data look more normal. What becomes normal is the average, and for some ordinary-looking distributions even the average never settles down. |
| 10 | Why the Best Schools Are Small, and So Are the Worst | Rank schools by average test score and the smallest schools crowd the top of the list, an observation that helped fuel big investments in small schools. But the smallest schools also crowd the bottom. |
| 11 | How Serial Numbers Counted Germany's Tanks | In World War II, Allied intelligence estimated German tank production at around 1,400 a month. Statisticians working only from serial numbers on captured equipment estimated about 250, and postwar German records showed they were almost exactly right. |
| 12 | What '95% Confident' Actually Means | Most researchers asked about a 95% confidence interval endorse at least one false interpretation, such as 'there is a 95% chance the true value lies in this interval'. The 95% belongs to the method, not to any single interval. |
| 13 | p < 0.05 Doesn't Mean You're 95% Sure | If a field mostly tests long-shot ideas, a large share of its 'significant' results can be false even when everyone uses p < 0.05 honestly. With 1 in 10 tested hypotheses true and 80% power, over a third of discoveries are wrong. |
| 14 | Why Small Studies Find Huge Effects | When an underpowered study finds a statistically significant effect, the reported effect is almost guaranteed to be exaggerated, often several-fold. Passing the significance filter is what inflates it. |
| 15 | The Dead Fish That Lit Up an fMRI Scanner | Researchers put a dead Atlantic salmon in an fMRI scanner, showed it photos of people in social situations, and found 'significant' brain activity. The fish was not thinking; the statistics were. |
| 16 | The Lady Who Could Taste Milk-First Tea | One of statistics' most famous experiments began with a scientist who claimed she could taste whether milk or tea had been poured first. The test Fisher designed for her needs no formulas at all, just counting arrangements. |
| 17 | The Bootstrap: Error Bars From Your Own Data | You have one sample and no formula for the uncertainty of your statistic, say a median or a correlation. Resampling your own data with replacement, thousands of times, gives a remarkably good answer. |
| 18 | How Bayes Found a Plane at the Bottom of the Ocean | Air France 447 vanished into the Atlantic in 2009, and two years of searching found nothing. A Bayesian reanalysis that treated every failed search as evidence pointed to where the wreck was found about a week after the search resumed. |
| 19 | How to Sample From a Shape You Can't Normalize | Bayesian posteriors usually contain an integral nobody can compute. In 1953, scientists at Los Alamos found a way around it: a random walker that only ever compares heights and never needs the total. |

## Data Traps & Measurement

| # | Title | Hook |
|---:|---|---|
| 20 | A Dinosaur Hiding in Your Summary Statistics | A cloud of points shaped like a dinosaur and a cloud shaped like a star can share the same means, standard deviations and correlation to two decimal places. Summary statistics can hide everything that matters. |
| 21 | When Every Part Says Yes but the Whole Says No | In 1973, UC Berkeley's graduate admissions looked biased against women: about 44% of men were admitted versus 35% of women. Yet department by department, women were admitted at similar or higher rates. |
| 22 | How Selection Creates Correlations Out of Nothing | Among hospital patients, two completely unrelated diseases can look negatively correlated, as if having one protects you from the other. Nothing about the biology changed; the hospital's front door did it. |
| 23 | Armor Where the Bullet Holes Aren't | Returning WWII bombers had bullet holes clustered on the wings and fuselage, so the obvious move was to armor those spots. The statistical insight: planes hit elsewhere, such as the engines, mostly did not come back to be counted. |
| 24 | Why Praise Seems to Fail and Punishment Seems to Work | Israeli flight instructors told Daniel Kahneman that praising a great landing made the next one worse, while shouting after a bad one made the next one better. They were seeing pure statistics. |
| 25 | The Correlation That Flips When You Zoom In | In 1930 U.S. census data, states with more immigrants had higher literacy rates. Yet individually, immigrants were slightly less likely to be literate than native-born Americans. |
| 26 | Redraw the Lines, Reverse the Result | Take the same 99 Iowa counties and group them into six regions. Depending on where the borders go, the correlation between the elderly share of the population and the Republican vote can be pushed from about -0.99 to +0.99. |
| 27 | When Missing Data Isn't Missing at Random | Deleting rows with missing values feels like the cautious choice. But if high earners are the ones who skip the income question, every remaining average is biased, and filling the blanks with the mean makes your uncertainty look smaller than it is. |
| 28 | Noisy Data Makes Real Effects Look Smaller | Measure someone's blood pressure once and its link to stroke looks weaker than it really is. Random measurement error does not just add noise; it systematically flattens relationships. |
| 29 | When a Measure Becomes a Target | In 1902, colonial Hanoi paid a bounty for every rat tail handed in. Officials soon noticed tailless rats in the streets: people were cutting off tails and letting the rats go on breeding. |

## Machine Learning

| # | Title | Hook |
|---:|---|---|
| 30 | Linear Regression Is Just a Shadow | Fitting a line through 1,000 points looks like a messy optimization. Geometrically it is a single right angle: the fitted values are the shadow of your data vector on a flat plane in 1,000-dimensional space. |
| 31 | Why a Perfect Fit Is a Warning Sign | John von Neumann reportedly quipped that with four parameters he could fit an elephant, and with five make it wiggle its trunk. In 2010, physicists actually did it, a reminder that fitting your data perfectly says nothing about predicting new data. |
| 32 | Why the Lasso Has Sharp Corners | Add a penalty and your model fits its training data worse, on purpose, yet predicts new data better. One kind of penalty also sets many coefficients exactly to zero, for a purely geometric reason: diamonds have corners. |
| 33 | The Cross-Validation Mistake That Fooled Biologists | With 50 samples and 5,000 pure-noise features, you can build a classifier whose cross-validated error looks close to zero while its true error is 50%. All it takes is choosing the features before you cross-validate. |
| 34 | Why Gradient Descent Zigzags | Gradient descent always steps in the steepest downhill direction, and that is exactly why it can take thousands of steps to cross a narrow valley, bouncing from wall to wall instead of heading for the bottom. |
| 35 | Why a Forest of Bad Trees Beats One Good Tree | A single carefully grown decision tree memorizes noise. Grow hundreds of trees deliberately crippled by randomness, each seeing a random sample and random features, and their vote is far more accurate. |
| 36 | Turning Barely-Better-Than-Chance Rules Into an Expert | In the late 1980s, theorists asked whether a pile of rules of thumb, each only slightly better than guessing, could be combined into an arbitrarily accurate classifier. The answer was yes, and the idea later powered the first real-time face detectors. |
| 37 | Separating the Inseparable by Adding a Dimension | Some data cannot be split by any straight line, like a red cluster surrounded by a blue ring. Lift the points into a third dimension and a flat sheet separates them perfectly, and a kernel lets you do this without ever computing the new coordinates. |
| 38 | k-means Will Find Clusters in Pure Noise | Give k-means uniformly random points and ask for five clusters, and it will confidently return five tidy groups. Clustering algorithms always find clusters; whether they are real is a separate question. |
| 39 | Genes That Draw a Map of Europe | Take genetic data from people across Europe and apply a method that knows nothing about geography. The first two directions of variation, plotted against each other, look strikingly like a map of Europe. |
| 40 | What a t-SNE Plot Can't Tell You | In a t-SNE or UMAP plot, the size of a cluster and the distance between clusters can be essentially meaningless, and with the wrong settings pure noise can come out looking like islands. |
| 41 | A Neural Network Is Just a Pile of Bent Lines | A famous 1969 book showed that a single-layer perceptron cannot even compute XOR. Add one hidden layer of simple 'bent lines' and a network can approximate essentially any continuous function. |
| 42 | How a Network Learns: Passing the Blame Backward | A network with a million weights needs a million partial derivatives at every training step. Backpropagation gets all of them for roughly the cost of a couple of extra forward passes, not a million. |
| 43 | Attention: Every Word Asks Every Other Word a Question | Early neural translation systems squeezed a whole sentence into one fixed-size vector before translating, and quality dropped on long sentences. Attention let each word look up every other word directly, and it became the core of modern language models. |
| 44 | 99.8% Accurate and Completely Useless | In a widely used credit-card dataset, only 0.17% of transactions are fraud. A model that flags nothing is 99.8% accurate, and a model with an impressive ROC curve can still bury investigators in false alarms. |
| 45 | When 90% Confident Isn't 90% Right | Modern deep neural networks are far more accurate than those of the 1990s, yet many are worse at knowing when they are wrong: when they say 90%, they can be right much less often. |
| 46 | The Machine Learning Bug Hiding in Hundreds of Papers | Several published papers claimed machine learning predicted civil wars far better than old-fashioned logistic regression. When researchers corrected data leakage and other errors, the advantage disappeared. |
| 47 | Your Image Classifier Might Be Reading the Copyright Notice | A well-performing classifier recognized horses in photos, but an explanation method revealed it was largely keying on a small copyright tag that appeared on many of the horse pictures. |

## Causal Inference & Experiments

| # | Title | Hook |
|---:|---|---|
| 48 | Storks Deliver Babies (p = 0.008) | Across 17 European countries, the number of breeding stork pairs is strongly correlated with the number of human births (r of about 0.62, p = 0.008). The correlation is real; the causation is not. |
| 49 | When Controlling for a Variable Creates the Bias | Among low-birth-weight babies, those born to mothers who smoked had lower infant mortality than those born to non-smokers. Smoking does not protect babies; conditioning on birth weight manufactured the paradox. |
| 50 | When Observational Data Said the Opposite of the Trial | Large observational studies suggested hormone therapy substantially cut heart-disease risk in postmenopausal women. When a big randomized trial tested estrogen plus progestin, it was stopped early, and the treated group had more coronary events, not fewer. |
| 51 | Can Clever Statistics Replace a Randomized Experiment? | In 1986, an economist took a job-training program whose effect was known from a randomized experiment and asked whether standard non-experimental methods could recover it. Most of them missed badly, some even getting the sign wrong. |
| 52 | The Minimum Wage Study That Used New Jersey as a Lab | Standard textbook models predicted that raising the minimum wage would cut fast-food jobs. When New Jersey raised its minimum wage in 1992, economists compared its restaurants with those across the border in Pennsylvania and found no drop in employment. |
| 53 | What Happens the Night You Turn 21 | U.S. death rates jump by about 9% right after people turn 21, the legal drinking age. Because your exact birthday is unrelated to almost everything else about you, that jump is close to a natural experiment. |
| 54 | A Lottery That Measured the Cost of War | Did serving in Vietnam reduce men's later earnings? Comparing veterans with non-veterans is hopelessly confounded, but the draft lottery, which assigned risk of service by birthday, let an economist estimate it: about 15% lower earnings for white veterans in the early 1980s. |
| 55 | Building a Fake California to Measure a Real Law | To measure what California's 1988 tobacco-control law did, you would need a California that never passed it. Researchers built one: a weighted blend of other states that tracked California's cigarette sales closely for nearly two decades before the law. |
| 56 | Why Checking Your A/B Test Early Breaks It | If you check an A/B test repeatedly and stop as soon as p < 0.05, two identical versions of a website will be declared 'significantly different' far more than 5% of the time: with 20 evenly spaced looks, about a quarter of the time. |
| 57 | Stop Wasting Half Your Traffic on the Loser | A classic A/B test keeps sending half its users to the worse option until the experiment ends. Bandit algorithms shift traffic toward the apparent winner as evidence accumulates, an idea first proposed in 1933 for clinical trials. |
| 66 | When Your Control Group Catches the Treatment | Randomly give half of a social network's users a new feature and the 'control' half still feels it, through friends who have it. The experiment's comparison can then be biased in either direction. |

## Networks

| # | Title | Hook |
|---:|---|---|
| 58 | How a Few Shortcuts Shrink the Whole World | Take a network where everyone knows only their nearest neighbors and randomly rewire just a few percent of the links. The typical number of steps between strangers collapses, while every local neighborhood still looks just as cliquey. |
| 59 | Why Acquaintances Find You Jobs | Granovetter found that people often heard about new jobs through acquaintances rather than close friends. Fifty years later, experiments involving about 20 million LinkedIn users tested the idea causally. |
| 60 | Why Your Friends Have More Friends Than You | On average, your friends have more friends than you do. This is a mathematical consequence of how networks are sampled, not a sign that you are unpopular. |
| 61 | Rich-Get-Richer Networks and the Power-Law Trap | If new web pages link to already-popular pages more often, a few hubs end up with an enormous share of links. But a straight line on a log-log plot, the usual 'proof' of such a power law, proves surprisingly little. |
| 62 | How the Medici Won Florence Without Being the Richest | In early 15th-century Florence, the Medici were not the wealthiest family; the Strozzi were richer. Yet the Medici came to dominate the city, and a key part of the story is their position in the network of marriages and business ties. |
| 63 | The Random Surfer Behind Google | Google's original ranking idea can be described as a bored web surfer clicking random links forever. The fraction of time that surfer spends on each page is its PageRank. |
| 64 | The Karate Club That Split in Two | In the 1970s an anthropologist mapped the friendships in a university karate club just before a dispute split it in two. Algorithms given only the friendship links can predict who ended up on which side for all but one member. |
| 65 | Did Your Friends Make You Do It? | Obesity, smoking and happiness appear to 'spread' through social networks. But people also choose friends who resemble them, and in observational network data those two explanations can be impossible to tell apart. |

## Contagion & Collective Behavior

| # | Title | Hook |
|---:|---|---|
| 67 | Why Epidemics Overshoot Herd Immunity | An unchecked epidemic does not stop when it reaches herd immunity; it keeps going. In the simplest model with R0 = 2.5, the number of people currently infected peaks once 60% have caught it, yet about 89% are eventually infected. |
| 68 | Why Behaviors Don't Spread Like Viruses | Random long-range ties make diseases and rumors spread faster. But in an online experiment, a health behavior spread farther and faster through clustered networks, because people needed to hear about it from several contacts. |
| 69 | Two Nearly Identical Crowds: One Riots, One Doesn't | Imagine 100 people whose riot thresholds are 0, 1, 2, ... 99 (each joins once that many others already have): everyone ends up rioting. Change one person's threshold from 1 to 2 and only one person riots. |
| 70 | How Rational People Join the Wrong Crowd | A line of perfectly rational people can all make the same wrong choice, each correctly reasoning that the people before them probably knew something. After just two matching choices, private information can stop mattering. |
| 71 | The Math Behind the Wisdom of Crowds | At a 1906 livestock fair, about 800 people guessed the weight of an ox, and the middle guess (1,207 lb) was within 1% of the true dressed weight (1,198 lb). Let a crowd see each other's guesses, though, and the magic can evaporate. |
| 72 | Rewind the World: Would the Same Song Be a Hit? | In an online experiment with over 14,000 participants, researchers created eight parallel 'worlds' of the same music market. The same song could become a hit in one world and a flop in another. |
| 73 | How Open-Minded People Split Into Camps | Give a population a simple, reasonable rule (average your opinion with everyone who is not too far from you) and instead of reaching consensus it can freeze into permanent, separate camps. |
| 74 | Breaking the Echo Chamber Can Backfire | An intuitive fix for polarization is to expose people to the other side. When researchers paid Twitter users to follow a bot sharing opposing political views for a month, Republicans became more conservative, not less. |

## Agent-Based Models & Inequality

| # | Title | Hook |
|---:|---|---|
| 75 | Mild Preferences, Extreme Segregation | Suppose everyone is content to be in the minority, happy as long as at least a third of their neighbors are like them. A city of such people can still end up sharply segregated. |
| 76 | The Winning Strategy That Never Won a Single Game | In Robert Axelrod's famous tournaments of computer programs playing the repeated prisoner's dilemma, the winner was the simplest entry, and it never outscored any single opponent it played. |
| 77 | The Tragedy of the Commons Isn't Inevitable | The 'tragedy of the commons' says shared resources are doomed to be overused. Yet a Swiss alpine village has governed its shared pastures under community rules for centuries, and the political scientist who documented such cases won a Nobel Prize. |
| 78 | Two Countries, Same Inequality Score, Different Worlds | Two societies can have exactly the same Gini coefficient while one has a struggling bottom and the other a runaway top. When Lorenz curves cross, a single number cannot rank inequality. |
| 79 | Fair Coin Flips, Wildly Unfair Outcomes | Simulate an economy where every trade is a fair coin flip and the stake is a fraction of the poorer trader's wealth. Nobody cheats and nobody has an edge, yet wealth concentrates into fewer and fewer hands. |
| 80 | Why Early Luck Gets Locked In | Start an urn with one red and one blue ball, then repeatedly draw a ball and return it along with another of the same color. The red fraction settles down, but to a random value, and every value between 0 and 1 is equally likely. |

## Text as Data

| # | Title | Hook |
|---:|---|---|
| 81 | Why 'The' Is Twice as Common as 'Of' | In a classic million-word corpus of American English, 'the' makes up about 7% of all words and 'of' about 3.5%, roughly half as much. Frequency keeps falling roughly as 1/rank for thousands of words. |
| 82 | The Boring Words That Unmasked an Author | Twelve of the Federalist Papers were claimed by both Alexander Hamilton and James Madison. Statisticians settled it in the 1960s using not ideas or rhetoric but humble words like 'upon', which Hamilton used far more often than Madison. |
| 83 | The Most Common Words Tell You the Least | Ask a computer which words best describe a speech and raw counts answer 'the', 'and', 'of'. The words that actually distinguish a document are the ones it uses much more than everyone else. |
| 84 | An Algorithm That Finds Topics Without Reading | A topic model knows nothing about what words mean, yet it can sort thousands of documents into coherent themes. Strangely, the version that best predicts held-out text is not necessarily the one humans find most interpretable. |
| 85 | King - Man + Woman = Queen? Not Quite | Word vectors famously solve 'king - man + woman = queen'. Less famously, the standard demo excludes the input words from the answer; without that rule, the nearest vector is often just 'king' again. |
| 86 | Word Vectors as a Telescope on Culture | Word embeddings trained on a century of American text place occupations nearer 'woman' or 'man' in ways that track the actual share of women in those jobs in census data. The 'bias' is also a measurement. |
| 87 | Why Your Sentiment Analyzer Hates Accountants | A widely used general-purpose dictionary labels words like 'tax', 'cost', 'capital' and 'liability' as negative. In corporate annual reports, almost three-quarters of the words it flags as negative are not negative in that context. |
| 88 | Can an AI Replace a Survey of Real People? | Prompt a language model with the demographic backstory of a real survey respondent and it can reproduce many groups' average voting patterns surprisingly well. But using it as a replacement fails in quieter ways: answers are too uniform and shift with prompt wording. |

## Surveys & Digital Traces

| # | Title | Hook |
|---:|---|---|
| 89 | Why 250,000 Survey Responses Were Worth Fewer Than 10 | In 2021, a COVID survey collecting about 250,000 responses a week overestimated U.S. vaccine uptake by 17 percentage points, while a poll of about 1,000 people a wave was far closer. For that estimate, the giant survey was worth less than a random sample of 10 people. |
| 90 | A Poll Can Match the Census and Still Be Wrong | When Pew ran a phone survey with a 9% response rate, it matched government benchmarks on most demographics, yet 55% of respondents said they had volunteered in the past year, versus 27% in a high-response government survey. |
| 91 | How a Poll of Gamers Forecast a Presidential Election | In 2012, a poll run on the Xbox gaming platform drew respondents who were 93% male, versus 47% of voters. After statistical adjustment, its estimates were in line with forecasts from leading poll aggregators. |
| 92 | How Google's Flu Detector Lost to Weeks-Old Data | Google Flu Trends promised real-time flu tracking from search queries. In early 2013 it estimated more than double the CDC's flu levels, and, as critics pointed out, simply projecting forward from CDC data a couple of weeks old would have done better. |
| 93 | The Strange Bump at 20 Friends | Facebook's friend-count distribution, measured in 2011, has a kink near 20 friends and a hard cutoff at 5,000. Neither is a law of human sociality: both were put there by the platform itself. |

## Privacy, Fairness & Ethics

| # | Title | Hook |
|---:|---|---|
| 94 | Three Facts That Can Identify You | Your ZIP code, birth date and sex sound anonymous. Using 1990 census data, that combination was estimated to single out about 87% of Americans, and it was used to find a governor's 'anonymized' medical records. |
| 95 | Hiding in a Crowd Isn't Enough | One fix for re-identification is to make every person in a released table look identical to at least k - 1 others. But if all k people in a group share the same diagnosis, the secret is out anyway. |
| 96 | The Privacy Trick That Starts With a Coin Flip | To learn how many people cheated on their taxes without anyone being able to prove a single person did, have each flip a coin in secret: heads, answer truthfully; tails, flip again and answer 'yes' for heads, 'no' for tails. Every individual answer is deniable, yet the true rate can be recovered. |
| 97 | 'It's Public Data' Isn't an Ethical Argument | In 2008, researchers released a de-identified dataset of Facebook profiles from an unnamed university's students. Others worked out which university it was within days, and some of the profile data had been visible only to members of that campus network. |
| 98 | The Tiny-Effect Experiment That Sparked a Huge Backlash | In 2012, Facebook altered the News Feeds of about 689,000 users for a week to show fewer positive or fewer negative posts. The measured effects on what people later posted were tiny, yet the study set off a global debate about consent. |
| 99 | How a Policing Algorithm Can Confirm Its Own Predictions | Send patrols where past records show more crime and you will record more crime there, because that is where officers are looking. In simulation, a predictive-policing algorithm can keep concentrating on the same neighborhoods even when true crime is spread evenly. |
| 100 | Why No Algorithm Can Be Fair in Every Way at Once | A criminal risk score can be calibrated for two groups, so that 'high risk' means the same reoffense rate in both, and still flag people who never reoffend in one group at nearly twice the rate of the other. When base rates differ, both cannot be fixed at once. |
