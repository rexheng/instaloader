# Facts · episode 82

All counts are recomputed by `data_prep.py` from Project Gutenberg eBook #18 (*The Federalist
Papers*, https://www.gutenberg.org/cache/epub/18/pg18.txt) -> `data.json`. Tokens = `[a-z]+`
after lower-casing, essay body only (after "To the People of the State of New York:", before
"PUBLIUS"). Known authorship: Hamilton 51 (1, 6-9, 11-13, 15-17, 21-36, 59-61, 65-85),
Madison 14 (10, 14, 37-48), disputed 12 (49-58, 62, 63). Gutenberg tags No. 58 "MADISON";
it is treated as disputed, as in the standard list.

| # | Claim (as narrated / shown) | Verification | Source |
|---|---|---|---|
| 1 | Twelve Federalist Papers (49-58, 62, 63) are disputed between Hamilton and Madison | Verified | Adair 1944, WMQ 1(2):97-122; Mosteller & Wallace 1963; Wikipedia "The Federalist Papers" |
| 2 | No. 51 contains "If men were angels, no government would be necessary" | Verified in the Gutenberg text | Federalist No. 51 |
| 3 | Hamilton's list became public after his death in 1804 and claimed No. 51; Madison's list (1818 Gideon edition) claimed it too | Verified. Hamilton's list credited him with 63 essays, incl. 49-53, 55-58, 62, 63 (it gave 54 to Jay, which is why the cold open says "disputed", not "both claimed all twelve"). Madison claimed 29 in the 1818 Gideon edition | Wikipedia "The Federalist Papers"; Adair 1944 |
| 4 | "war": best single dividing line on the 65 known essays still makes 14 errors = calling every essay Hamilton's | Recomputed: best cut for "war" and for "liberty" is the trivial one (14/65 wrong) | data.json `best_cut` |
| 5 | Essay 8 says "war" 11 times; the court essays (78-83) say it at most once | Recomputed: 8 -> 11; 78-83 -> 0, 0, 1, 1, 0, 1 | data.json `war_counts` |
| 6 | Every one of Hamilton's 51 essays uses "upon"; 11 of Madison's 14 never do | Recomputed (Hamilton min 1.01 per 1000; Madison zeros 11/14). Consistent with M&W Table 2.3 (48 Hamilton papers: none at 0; 50 Madison pieces: 41 at 0) | data.json; M&W 1963 Table 2.3 |
| 7 | Line on "upon" makes one mistake (Madison's No. 38) | Recomputed: best cut 0.72-1.01 per 1000, 1/65 wrong | data.json `best_cut` |
| 8 | Disputed: ten at zero "upon"; No. 50 has 1, No. 54 has 2 - both right of the line | Recomputed: 50 -> 1/1101 words (0.91 per 1000), 54 -> 2/1996 (1.00) | data.json `upon_counts_D` |
| 9 | Hamilton's rate 3.3 per 1000; Madison's under 0.2 (on screen 0.18) | Recomputed pooled: 3.34 and 0.181. M&W's own estimates: 3.24 and 0.23 ("about 3 per thousand for Hamilton and about 1/6 per thousand for Madison") | data.json; M&W 1963 p. 276 and Table 5.3 |
| 10 | No. 54 ~ 2,000 words; expected uses: Hamilton ~6.5 (6.68), Madison ~ a third (0.36) | Recomputed: 1996 tokens | data.json `lam54` |
| 11 | Poisson model for counts of a rare word | M&W 1963 use the Poisson and the negative binomial | M&W 1963 §2 |
| 12 | P(2 | Hamilton) = 2.8 %, P(2 | Madison) = 4.5 %, ratio 1.6 | Recomputed: 0.0281, 0.0453, 1.61 | data.json `pmf54` |
| 13 | Five words (upon, by, on, to, there) under independence multiply to > 20 million to one for No. 54 | Recomputed: log10 odds 7.35 (= 22 million). Words chosen from M&W's final list (their groups B3A/B3B) | data.json `odds54_words`; M&W Table 5.3 |
| 14 | Leave-one-out on the 65 known essays: one mistake (No. 25) | Recomputed | data.json `loo_wrong` |
| 15 | All 12 disputed lean Madison; No. 55 weakest (1.5 to 1), No. 56 next | Recomputed (log10 odds 0.17 and 4.0) | data.json `log10_odds` |
| 16 | Mosteller & Wallace 1963: ~30 final words, negative binomial ("lets words clump", damps the odds), all 12 to Madison; No. 55 weakest at ~80 to 1, No. 56 next at ~800 to 1 | Verified from the paper: "Madison is extremely likely ... with the possible exception of No. 55, and there our evidence is weak, suitable deflated odds are 80 to 1 for Madison. No. 56, next weakest, is a strong 800 to 1"; "The net was 30 words in 5 groups"; NB "provides automatic damping" | Mosteller & Wallace 1963, JASA 58(302):275-309, pp. 298-306 |
| 17 | Historians led by Douglass Adair (1944) had already argued for Madison | Verified | Adair 1944, "The Authorship of the Disputed Federalist Papers", WMQ 1(2):97-122 |
| 18 | M&W: contextual words such as "war" are dangerous; filler words have stable rates | Verified (abstract) | M&W 1963 |

**Stated assumptions / limits (narrated or on screen):** independence of words (M&W: correlation
"may either inflate or deflate"; they deflated ~9 %); Poisson is too thin-tailed, the negative
binomial shrinks the odds; my 5-word Poisson odds are therefore overconfident and labelled
"Poisson, 5 words, my counts". Not narrated: Collins et al. (2004) argued some disputed essays
show collaboration; a bag of words cannot rule out joint writing.
