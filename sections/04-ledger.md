## 4. Twenty-six broken measurements

This is the part of the study we consider most transferable, because nothing in
it is specific to satellites. **All twenty-six defects returned a plausible
value without raising an exception.** None would have been caught by testing
that the code runs, by type checking, or by any check whose failure mode is a
crash.

### 4.1 The ledger

| | What was broken | What caught it |
|---|---|---|
| 01 | Linear discriminant fitted on absolute dB values | It got worse out of sample |
| 02 | "Four scenes" was two dates times two granules | Listed granule dates |
| 03 | Visual-inspection targets chosen by patch area | Recognised the bias |
| 04 | Reported that two measurements agreed | Measured precision directly |
| 05 | Judged two contracts identical because titles matched | Read the Q&A document |
| 06 | Classified a harvest survey as agriculture | Read the contracting body |
| 07 | Used a historically subsiding area as a control | Read the regulation |
| 08 | Read a low-zoom tile as a numeric value | Colour inversion produced midtones |
| 09 | Our own grep was deleting the output | Looked at raw output |
| 10 | Overlaid two rasters in different CRSs, believing them aligned | Drew the overlay |
| 11 | Computed a variable and never used it | Re-read the code |
| 12 | Resampled categorical values with bilinear interpolation | Area quietly shrank |
| 13 | Launched the same job twice | Corrupted PNGs |
| 14 | Failed tile fetches persisted as black rectangles | Looked at the image |
| 15 | Detected encoding from the first 4,000 bytes | Distrusted "undetectable" |
| 16 | The compared samples had been swapped | Listed municipality names |
| 17 | Compared a paid contract with unpaid research cooperation | Read the full guidelines |
| 18 | Measured in a season the ground truth was never captured in | Counted truth capture months |
| 19 | A mask choice put 87 per cent of the truth outside the denominator | Reported truth coverage |
| 20 | Estimated a depth-removal coefficient where depth was not the only variable | Read the method's premise |
| 21 | Did not correct sun glint, producing a season-flipping value | Three areas converged to one value |
| 22 | An unregistered collection silently routed to another provider | Read the default value |
| 23 | The mechanism named two drivers and we measured one | Re-read the mechanism |
| 24 | Nearly reported a sensor drift artefact as a real signal | Looked for a break point |
| 25 | Compared a concentration against a total | Wrote out the units |
| 26 | Subsampled without checking the data volume, and hit the prediction | Counted the available days |

Full descriptions with figures are in the companion repository
(`docs/LEDGER.md`); the eight below are the ones that carry the argument.

**04 — agreement that was not independent.** A detected-to-official ratio of
0.415 and a recall of 0.474 were reported as mutually confirming. The agreement
silently assumed precision near 1. Measuring precision visually gave 40.8 per
cent, and the agreement evaporated. Two numbers that agree are one piece of
evidence unless their derivations are independent.

**12 and 16 — repairing one defect produced the next.** Hansen forest-loss
year is categorical: 0 means no loss, 1 to 24 encode a year. Regridding it with
bilinear interpolation **removed 22 per cent of the loss area silently**, which
made our own over-detection look worse than it was. We had just fixed defect 10
(a CRS mismatch) and passed the data through the same function without noticing.
Then, re-computing after the fix, we drew the municipality list in registry
order while the original measurement had used descending forest cover. The
before-and-after comparison was between different samples. The numbers came out
looking entirely normal.

**18 to 21 — four defects stacked inside one measurement.** The seagrass
industry carried, simultaneously: measuring in November when the ground truth
imagery exists only for March-May and October; masking shallow water with the
red band, which at Kd ≈ 0.4/m retains two per cent of signal over a five-metre
round trip and therefore put 87 per cent of the truth outside the denominator;
estimating a Lyzenga depth-invariant coefficient over mixed bottom types when
the method requires uniform sand, so that the coefficient removed substrate as
well as depth; and no sun-glint correction. **The first of these returned AUC
0.967 in one area** — the best number in the entire study at that point. After
correction, three areas and three dates converge on 0.46, and *the disappearance
of the variance is itself the evidence that the correction was right*.

**09 and 22 — a default we wrote erased what we were looking for.** In one
case a filter that stripped indentation was deleting every result line, and we
concluded the search returned nothing and went looking at the search side. In
the other, `PROVIDER.get(collection, "es")` sent an unregistered collection to
the wrong provider, which returned zero results without error. **"It does not
exist" and "I looked in the wrong place" became indistinguishable.** The fix is
structural: the lookup now raises rather than defaulting.

**24 and 26 — the prediction was confirmed because the measurement was
wrong.** In 24 the night-time temperature trend was positive in all four
framings, exactly as the mechanism predicts, and we nearly wrote it up before
finding the February 2020 break. In 26 we subsampled an orbit archive to every
fourth day "because using all of it is excessive", obtained a partial
correlation of 0.101 — **almost exactly the frozen prediction** — and only later
found the archive held 48 days in total, so there had never been a reason to
subsample. Noisy annual means dilute correlation, which biased the result
*towards* the prediction. Using all 45 days gives 0.165.

### 4.2 Ten of the twenty-six returned a good result

Defects 04, 05, 08, 12, 17, 18, 19, 24, 26 and the inverse of 01 all produced
numbers that looked like success: a high AUC, a clean ratio, a confirmed
prediction, a dramatic before-and-after. The remaining sixteen produced numbers
that looked wrong, and those we investigated immediately.

This asymmetry is, we think, the central methodological hazard of self-directed
measurement, and it is not addressed by any of the usual machinery. Testing
catches crashes. Calibration catches disagreement with a known answer, where
one exists. Pre-registration catches moving the goalposts. **None of them
catches a wrong measurement that lands where you expected it to land.** The
only mechanism that worked for us was making a confirmed prediction trigger an
audit rather than a conclusion, and it worked twice out of twenty-six — not
because the mechanism is weak, but because the population of dangerous cases is
small and every one of them is expensive.

### 4.3 What actually caught them

Grouping the right-hand column of the ledger. Members are listed so the counts
can be checked; every defect appears in exactly one group, and they sum to 26.

| What caught it | Defects | n |
|---|---|---|
| Reading the primary document in full | 05, 06, 07, 17, 20, 23 | 6 |
| Counting a denominator, a unit or a sample size explicitly | 02, 16, 18, 19, 25, 26 | 6 |
| Reading our own code or raw output | 09, 11, 15, 22 | 4 |
| An ordering or sign that violates physics or structure | 01, 08, 21, 24 | 4 |
| Cropping the objects and looking at them | 03, 10, 14 | 3 |
| An independent second measurement of the same thing | 04, 12 | 2 |
| A corrupted artefact | 13 | 1 |

Two things stand out. **Reading and counting dominate**: twelve of twenty-six
were caught by reading a document we had only excerpted, or by writing down a
denominator, a unit or a sample size that we had been carrying implicitly.
Neither requires any satellite data.

**Looking at the cropped objects is under-represented here and should not be.**
It accounts for three of the twenty-six, but the re-measurement of wall 1
produced three further cases that sit outside the numbered ledger because they
were found before a result was recorded: a background annulus that sat entirely
on top of the aircraft it was supposed to provide a background for, five
objects identified as aircraft on an airport apron that were all buildings in
the town to the east, and control points supposedly on empty pavement that were
on car roofs. All three were found by cropping and looking, and none was
visible in any aggregate.

**Aggregate statistics caught almost nothing.** Every defect was already
producing a reasonable aggregate; that is what made it a defect and not a bug.
