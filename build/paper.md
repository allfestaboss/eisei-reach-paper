# No error was raised: twenty-six broken measurements from a cross-domain audit of free satellite data

Boss Ohkubo (Allfesta Corp.)  
ORCID 0009-0007-8300-0039

## Abstract

Published work on satellite applications is, with few exceptions, a collection
of successes. What free Earth observation cannot do, and where the attempt to
measure whether it can do it breaks down, is largely absent from the record.
We report a cross-domain audit built to close that gap, and the main finding is
about the audit rather than about satellites.

Fifteen advertised industrial applications of satellite data were implemented
in full, fixed to a single region so that results are comparable, and run on
free, unauthenticated data only. All fifteen completed. Nine were then scored
against reference solutions we cannot move: awarded national-government
contracts, each with a title, a contracting body and a contract value,
recovered from thirteen fiscal years of Japanese procurement open data
(312,584 records, of which 332 are satellite analysis or survey work). The
remaining six were not measured because the state does not buy them. Four
industries — insurance, finance, retail and tourism — returned zero analysis
contracts in 312,584 records, and two were artefacts of keyword matching. The
list of fifteen was a demand claim, not a description of demand.

Seven technical walls and four institutional walls are reported. **Only one of
the seven is bought off with money**, and the name we first gave that one —
resolution — turned out to be imprecise, because the commercial sensor that
would solve it changes pixel size and band count together, so what is being
bought cannot be separated. Two walls are properties of the measuring
instrument rather than of the method: a free analysis-ready SAR product that
has already discarded phase, and a thermal sensor whose overpass time has been
drifting since orbit maintenance ended, bending a trend in night-time
land-surface temperature from +0.083 to +0.812 K/yr and contaminating every
year we wished to compare. One is not a technical wall at all: a satellite quantity can
be measured correctly and still add nothing, because the target statistic is
already explained by population at r = 0.85 to 0.95.

The core of the paper is a ledger of **twenty-six occasions on which the
measurement itself was broken**. Every one returned a plausible value without
raising an error, and **ten returned a good result** — the asymmetry that bad
results are doubted while good ones are not is the largest single threat to
self-directed measurement, and it is why the protocol freezes a prediction, a
decision criterion and a counter-hypothesis before each run, so that a
confirmed prediction is also audited. Four recurring shapes are recorded:
repairing one defect introduced the next; four separate defects stacked inside
one measurement; a default value written by the author converted "not
registered" into "no data"; and twice the prediction appeared to be confirmed
precisely because the measurement was wrong.

All code, frozen predictions, verdicts and measurement records are released
under a DOI. We report what we could not establish as carefully as what we
could: the wall taxonomy kept changing as industries were added and we have no
basis for calling it complete; institutional reach rests on a single observed
rejection; the region is fixed and in at least one industry the region
determines the conclusion; and "zero procurement" means zero in
central-government competitive tendering, not zero in existence.

---

## 1. Introduction

Tables of "industrial applications of satellite data" circulate widely in space
business material: agriculture, forestry, fisheries, disaster response,
insurance, finance, infrastructure, real estate, retail, energy, environment,
health, government, tourism, aviation. Each row states that satellites are
useful for something. Almost none of them states what happens when you try.

This is not a complaint about marketing. It reflects a structural property of
the literature. Demonstrations are published when they work; a method that
returns an area estimate 0.13 times the official figure, or an index that
correlates with recorded agricultural damage in the wrong direction, does not
usually become a paper, a case study or a slide. The Japanese government's own
use-case collections are explicitly collections of good practice. The most
useful public buying guide we found — a use-case-to-sensor-specification table
published by a media outlet operated by a satellite platform vendor — is a
guide to what to purchase, and is organised around applications that succeed.

The consequence is that a practitioner asking "can free satellite data do X?"
has a well-populated space of yes and an almost empty space of no. Worse, the
empty space is not uniformly empty: it hides the distinction between *this
cannot be done*, *this can be done but you measured it wrong*, and *this can be
done correctly and is still worthless*. We found all three, and could not tell
them apart until we had built machinery to tell them apart.

### 1.1 What this paper does

We took a fifteen-row application table at face value and implemented every
row. The region was fixed to one prefecture so that results across rows are
comparable rather than incidentally different. Only free, unauthenticated data
was used — no account, no key, no invoice — because that is the boundary whose
position we wanted to locate. All fifteen ran to completion in 108 seconds of
compute after caching, and none was blocked by data availability.

Running an implementation is not measuring reach. To measure reach we need an
external statement of what the work is and what it is worth, and it must be one
we cannot adjust after seeing our own results. We used awarded public
procurement contracts. Japan's procurement portal publishes the successful-bid
record of every central-government competitive tender as annual open data:
title, contracting body, contract value, supplier, corporate number. Thirteen
fiscal years is 312,584 records, of which 332 are satellite analysis or survey
work. Where a contract exists, the state has said "this is the job" and paid a
number for it, and both the description and the number are outside our control.

Two axes are kept separate throughout, because collapsing them produces
statements that cannot be acted on. **Technical reach** counts deliverables
listed in the statement of work that we could actually produce. **Institutional
reach** asks whether the bid could be submitted at all — qualification,
staffing, track record. A result of "technically reachable, institutionally
excluded" is a different fact from "neither", and the remedies have nothing in
common.

### 1.2 What we found

Three findings, in increasing order of how much they surprised us.

**The denominator was wrong.** Only nine of the fifteen industries are procured
by the state at all. Four — insurance, finance, retail, tourism — returned zero
analysis contracts in 312,584 records. Two more dissolved on inspection: real
estate's five hits were four disaster-damaged-building surveys and one survey
of photography practice, and aviation's forty-six were all keyword collisions
with *airborne* laser scanning, which shares a character with *aviation* in
Japanese. The fifteen-row table was a claim about demand, not a description of
it. Where demand is not established, the state is paying for the search: the
largest contracts we could not classify are Cabinet Office demonstration
programmes for finding uses for small SAR constellations, at over one billion
yen a year.

**Seven technical walls, and only one of them is priced.** Section 3 sets these
out. The short version is that the intuitive model — free data is coarse, paid
data is fine, money moves the line — describes exactly one of the seven. Two
walls are properties of the measuring instrument and are not removed by buying
a better one. One is a wall only in a commercial sense: the measurement is
correct and the result is redundant against a statistic that already exists.

**Twenty-six measurements were broken, and none of them raised an error.**
This is the finding we consider most transferable, and Section 4 is the ledger.
Every defect returned a plausible number. Ten of the twenty-six returned a
*good* number — a high AUC, a strong correlation, a value matching the frozen
prediction. Because bad results get re-examined and good results get written
down, a self-directed measurement programme will accumulate exactly the errors
that flatter it. Our protocol freezes a prediction, a decision criterion and a
counter-hypothesis before each run specifically so that a confirmed prediction
still has to be audited; twice, that is the only reason we caught the defect.

### 1.3 Scope and honesty about it

This is a single-operator study over one region with reference solutions from
one country's procurement system. We state limits before findings wherever we
can, and Section 5 collects them. The most important is that the wall taxonomy
was still moving when we stopped: three industries in, we wrote that there was
exactly one technical wall; at six there were five; at nine there are seven,
and the name we gave the first one turned out to be wrong. We have no basis for
claiming that seven is the number.

---

## 2. Design

### 2.1 One region, fifteen implementations

The region is Fukuoka Prefecture, in northern Kyushu, Japan. Fixing it is a
design decision with a cost that we state up front: in at least one industry
the region determines the result. Rice transplanting in Fukuoka falls in the
middle-to-late June, which coincides exactly with the rainy season; clear-sky
probability in the relevant window is 0.0 to 5.5 per cent. **On the days it is
clear the paddies are not yet planted, and after planting it is not clear.**
An optical approach to paddy mapping is not merely difficult here, it is
unavailable, and a study fixed to a different region would have reported a
different wall for the same industry.

We accept that cost because the alternative is worse. If each industry is
measured in whichever region it works best, the cross-industry comparison
measures our choice of regions. Nationwide replication is not "the same thing
1,741 times" but "1,741 differently conditioned measurements", which is not a
cost problem but an unmeasured one. Two industries (pollen and NO2) were
measured nationwide because their reference statistics are prefectural.

Only free, unauthenticated sources were used: Copernicus Sentinel-1 RTC,
Sentinel-2 L2A and Sentinel-5P via Microsoft Planetary Computer and Earth
Search, Landsat Collection 2 Level-2, MODIS, an annual 10 m land cover product,
Copernicus DEM, NOAA blended sea-surface temperature via ERDDAP, and the
Himawari-9 geostationary archive. Planetary Computer issues a short-lived
signed URL to an unauthenticated GET, so no account exists anywhere in the
pipeline. One product resisted: night-time lights, for which we found no free
route, and the two industries whose canonical method is night-time lights were
re-implemented with substitutes and are labelled as such.

### 2.2 Reference solutions from public procurement

The measurement problem in a self-directed study is that the subject and the
examiner are the same person. Our defence is to put the answer key somewhere we
cannot reach.

Japan's procurement portal distributes successful-bid records for
central-government competitive tenders as per-fiscal-year ZIP archives.
Thirteen fiscal years (FY2014 to FY2026) contain 312,584 records with eight
fields: procurement number, title, contract date, contract value, category,
agency code, supplier and corporate number. Filtering to satellite and remote
sensing work, removing communications and facilities contracts, and keeping
analysis and survey work leaves 332 records. Every one of the nine measured
industries takes its reference from that set.

Four traps are worth recording because each cost us time or a wrong claim.

1. **Encoding.** The CSV is UTF-8 with a byte-order mark and no header row.
   Sniffing the encoding from the first four kilobytes splits a multi-byte
   character and every candidate encoding fails, producing "undetectable".
2. **Coverage.** These are *competitive tenders only*. Sole-source contracts
   are not included, and neither is any municipal procurement. The Geospatial
   Information Authority's four sole-source SAR contracts for FY2025, totalling
   84.35 million yen, are reachable only through separately published
   sole-source disclosure documents.
3. **Keywords.** Searching for "satellite" returns satellite telephones,
   satellite communications and air-conditioning maintenance at a meteorological
   satellite centre. In the other direction, "airborne laser" collides with
   "aviation" and produced forty-six false members of an industry that turned
   out to have none.
4. **Agency codes do not identify a ministry.** The single code 8002010
   contains the Ministry of Justice, the Ministry of Land, Infrastructure and
   Transport, the Ministry of the Environment and the Forestry Agency.

**The contract does not state the requirement.** It states what was paid. The
required accuracy lives in the product specification or the statement of work,
and both have to be read to construct a scoring rule at all. Two examples
determined how we scored: the national land-use product specifies a conformance
level of *zero per cent error against the interpreted base map*, and an
environment-ministry seagrass survey reports achieved overall accuracy of 53.42
to 85.91 per cent using a commercial 50 cm eight-band sensor. The first says
the answer lives inside a human judgement; the second gives a number a free
method can be compared against.

### 2.3 The freeze protocol

Before each measurement runs, a file is written containing four things, and it
is not edited afterwards:

- the **question**, and which cell of the framework in §2.4 it occupies;
- the **reference solution**, with title, agency, supplier and contract value;
- a **numeric prediction** with an interval;
- a **decision criterion** stated as a threshold, and a **counter-hypothesis**
  (an alternative explanation that must be beaten) frozen at the same time.

After the run a verdict file records the outcome against that criterion. The
prediction files exist so that a *correct* prediction can still be audited;
this is not symmetric with the usual reason for pre-registration. Two entries
in the ledger of Section 4 were caught only because the prediction was matched
too neatly.

The counter-hypothesis is the part that changed the most results. For the NO2
industry we froze "the raw correlation will be high and will still lose to
population" as the criterion, rather than freezing a correlation target. The
measured raw correlation was 0.910 — by any conventional reading a success —
and the frozen criterion is the only reason it was recorded as a failure.

### 2.4 Four observables, two samplings

Satellites measure four things: **intensity, wavelength, polarisation and
phase** — in plainer terms, brightness, colour and temperature, how radio waves
bounce back, and gas absorption. Space and time are not quantities but
**samplings** of those quantities. That gives six cells, and four of the seven
technical walls fall into them cleanly: wavelength selection, phase
availability, spatial sampling and temporal sampling.

The framework earned its place by catching something about our own work.
**The first fifteen implementations used two cells.** Three of them read only
the `vv` band of an analysis-ready SAR product, and the `vh` band was inside the
same free asset, unread. The acquisition path had silently determined the
observable: the analysis-ready product retains amplitude and has already
discarded phase, while the single-look complex product retains amplitude,
phase and polarisation but is heavy to process. **Both are free.** Of the six
cells, exactly one — spatial sampling — is moved by money.

We then measured whether polarisation helps, with a frozen ladder of
counter-hypotheses (optical alone, VV alone, VV plus VH). For solar
installations, where optical is strong at AUC 0.951, polarisation adds
-0.003. For buildings, where optical fails (NDBI 0.607, NDVI 0.618), VH alone
is the best single feature at 0.734 and polarisation adds +0.027 over VV alone,
or +0.041 over optical plus VV. The verdict is "it works, and it is not
enough": the ceiling is about 0.78, and the improvement appears only where
optical has already failed. Sentinel-1 IW is dual-polarisation, not fully
polarimetric, so this is a statement about free dual-pol data and not about
polarimetry.

---

## 3. Where it stops

### 3.1 The nine measured industries

| Industry | Reference solution (contract value) | Observable | Wall | Verdict |
|---|---|---|---|---|
| Solar energy | MoE PV survey, 211.0 M JPY | intensity, wavelength | priced (resolution) | 4 of 10 deliverables |
| Paddy rice | MAFF rice statistics, 8.96 / 7.33 M JPY | intensity, **polarisation** | observable selection | partial |
| Forest logging | 14.35 / 5.55 M JPY | intensity, wavelength | threshold calibration | **reached** (quantile) |
| Flood extent | MoE, 45.40 M JPY | intensity (SAR) | timeliness | not reached |
| Land use | MLIT, 36.00 M JPY | intensity, wavelength | location of the truth | partial |
| Ground deformation | 68.12 M JPY | **phase** | institutional (track record) | inputs only |
| Seagrass | Port and Airport Research Institute tender no. 101 | intensity, wavelength | priced (unseparable) | not reached |
| Cedar pollen | MoE 17.72 M + airborne lidar 161.23 M JPY | wavelength (thermal) | drift of the instrument | not reached |
| NO2 | NIES, 138.89 M JPY | **gas absorption** | redundancy with existing statistics | not reached |

All four observables are represented: five optical, two SAR amplitude, one
interferometric phase, one atmospheric. Gas absorption was the last cell to be
filled. **Different observables produce different walls**, which is the reason
"what can free satellite data do?" has no cross-industry answer.

### 3.2 Seven technical walls

**Wall 1 — the priced wall, although "resolution" is the wrong name.**
For rooftop photovoltaics it really is resolution: spectrally, a panel on a roof
and the roof itself are the same thing at 10 m. For seagrass the same paid
boundary appears, but the commercial sensor that would cross it changes 50 cm
pixels and eight bands at once, so what money buys cannot be separated into
sharpness or colour. The defensible claim is "only money solves this", not
"resolution solves this". This is the only one of the seven that money solves.

**Wall 2 — choice of observable.** Determined before measurement begins. The
paddy case above: optical succeeded in 3 of 16 municipalities, SAR in 16 of 16,
with correlation rising from 0.239 (VV only) to 0.814 (VV plus VH). The
framework of §2.4 would have said so in advance, and we entered through optical
anyway.

**Wall 3 — threshold calibration, and it is detectable without ground truth.**
For forest loss, pixel-level AUC is 0.906 to 0.974 across all eleven
municipalities: **the ranking works everywhere**. What was broken was the
position of the cut. A fixed absolute threshold of 0.20 lands at a quantile
that varies from the 90.1st to the 99.6th percentile depending on the
municipality, and detection rates therefore varied by a factor of 23.7. Cutting
at the top one per cent per municipality moved the correlation with the official
figure from 0.156 to 0.835. **The diagnostic requires no ground truth at all**
— only the spread of detection rate across windows. A factor of three means an
absolute threshold is safe; a factor of 23.7 means it is not.

**Wall 4 — timeliness, as a ratio between revisit and event duration.**
For the July 2023 Chikugo river floods, **no free satellite observed the day of
inundation.** Sentinel-1 passed on 1 July and 13 July against a 12-day revisit;
Sentinel-2 was 99.3 per cent cloud on the day. What remained three days later
scored AUC 0.574 and best F1 0.111, because the water had gone. This is the
clearest case in the study of what a contract value buys: 45.4 million yen is
not paying for a better algorithm, it is paying for **the right to task an
acquisition**.

**Wall 5 — where the truth lives.** The national land-use product specifies
conformance as zero per cent error, but against the *interpreted base map*, not
against reality. The answer is inside the contractor's human judgement, and
external reach cannot be scored. Our own agreement with the four main land
classes was 0.841 against a naive counter-hypothesis (label everything forest)
at 0.583; forest recall 0.939 and precision 0.933, but farmland 0.440 and
inland water 0.408. The 36 million yen is buying human interpretation itself.

**Wall 6 — drift of the instrument.** Terra ended orbit maintenance in
February 2020 and its overpass time has drifted since. In our pollen panel
(132 samples, four years by 33 prefectures) night-time land-surface temperature
rose 2.1 K over fourteen years while daytime stayed flat, and the trend bends
from +0.083 to +0.812 K/yr at exactly February 2020 — a factor of 9.8. **All
four target years sit inside the contaminated period.** Removing the annual
mean returns the signal to 0.264 against a pre-frozen chance level of 0.265.
A commercial sensor has the same property, so this wall is not priced: it is
the wall of *comparing across years*, where wall 4 is the wall of *arriving in
time*.

**Wall 7 — redundancy with existing statistics.** Our NO2 retrieval is
physically sound: Osaka highest at 1.01e-4, then Kanagawa, Chiba, Saitama,
Ibaraki, Aichi, with Aomori and Hokkaido at the bottom. That is the correct
distribution for Japan. It still loses. Across all four framings, the raw
correlation with prefectural CO2 emissions is beaten by population (NO2 0.599 /
-0.045 / 0.910 / 0.410 against population 0.851 / 0.884 / 0.948 / 0.930), and in
the log framings the partial correlation is -0.051 and 0.078. The prediction of
*which* prefectures emit more than population explains was sharp — Oita,
Okayama, Yamaguchi, Hiroshima were named at freeze time and came out on top —
but the satellite residual correlates with that excess at -0.051. **Correct and
worthless are compatible**, and this is invisible unless a counter-hypothesis is
part of the decision criterion.

### 3.3 Four institutional walls, one of them observed

| | Wall | Status |
|---|---|---|
| I1 | Staffing | **The only direct observation.** A municipal open call rated the content highly and rejected a sole-operator organisation |
| I2 | Qualification | **Our prediction was wrong.** Neither consultant registration nor a licensed engineer was required; the only qualification was the all-ministry unified vendor registration, obtainable by a sole proprietor |
| I3 | Track record | Hard where money is involved: "experience having *undertaken* such work in the past five years". No award without a record, no record without an award — a bootstrap wall |
| I4 | Paperwork | The only wall crossable by effort alone. Information-security attestation via a free self-assessment benchmark with a self-issued certificate; the pass line is an average of 4.0 over 27 questions. Money and track record are irrelevant; answered honestly, we do not currently clear it |

**One claim here was retracted during the study**, and we record the retraction
rather than the conclusion. We had written that a single verb marks the
boundary: a port tender requires work "undertaken", while an agriculture
ministry call requires having "worked on" prediction — the softer verb being the
way in. Reading the full application guidelines dissolved it. The first page
reads "we are seeking operators willing to cooperate **without compensation**
with statistical research". The two documents were not two procurement
postings; one was an unpaid research collaboration, and the verb difference is
confounded with payment. The same guidelines assign copyright in the outputs to
the ministry without compensation, which would have made participation
incompatible with publishing what we reached.

What survived is narrower and more useful: one paid tender (17.72 million yen)
lists the unified vendor registration as the only qualification and states no
track-record requirement. In a comprehensive-evaluation tender, experience has
presumably moved to the scoring side rather than the gate. That is the case we
had been looking for, and it appeared in the last industry we measured.

### 3.4 Three things visible only across industries

**Ranking transfers, magnitude does not.** Detected over actual is 0.42 for
solar, 0.13 for paddy, 0.79 for forest loss. Forest loss was 1.69 before the
cut was corrected, so the sign of the error flipped. Whether a method
under- or over-estimates is method-specific; that the absolute quantity is
wrong was universal.

**"Accuracy" does not exist until the denominator is fixed.** With the same
method, same scene and same date, changing only the water mask moved seagrass
AUC from 0.387 to 0.897. Seagrass occupies 0.3 to 3 per cent of the water, so
**detecting nothing scores 83.6 to 99.7 per cent overall accuracy**. In the NO2
case, choosing total against per-area and linear against log moves the partial
correlation from -0.05 to 0.61. These are not walls; they are the scoring rule.

**Designing the criterion mattered more than the measurement.** The pollen
industry ended without answering the sharpest question — what does the
satellite add over ground weather stations — so for NO2 that question was
written into the decision criterion before the run. Without it, a raw
correlation of 0.910 would have been recorded as a success.

---

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

---

## 5. What we cannot claim

We state these before the discussion because several of them are load-bearing.

**L1 — The wall taxonomy was still moving when we stopped.** At three
industries we wrote that there was exactly one technical wall. At six there
were five. At nine there are seven, and at nine we also discovered that the
name given to the first one was wrong. There is no basis for treating seven as
the number of walls; it is the number we had reached when we ran out of
industries with reference solutions.

**L2 — Institutional reach rests on one observation.** A single open call in
which a sole-operator organisation was rejected on staffing, with the content
rated highly, is the only direct measurement. We read four tender documents in
full, but we did not bid, and a conclusion assembled from reading tender
documents was retracted the first time we read one of them completely (§3.3).

**L3 — The region is fixed, and sometimes the region is the result.** The
paddy case is the clearest: an optical approach is unavailable in Fukuoka
because transplanting coincides with the rainy season, and this is a property
of the prefecture, not of optical remote sensing. Two industries were measured
nationwide; seven were not.

**L4 — In some industries the reference and the measurement are not the same
thing.** The 161 million yen airborne-lidar contract used as a reference for
pollen is for mapping cedar distribution and canopy volume, not for predicting
a prefectural index relative to a normal year. The NO2 reference concerns
greenhouse gases while we measured NO2. We declared the second mismatch at
freeze time and noticed the first only afterwards, which is itself an instance
of the failure mode catalogued as defect 05.

**L5 — Some checks were left unfinished.** The extended summer window for
pollen, and a direct comparison against ground weather stations, were not run.
We can say that the structural ceiling on the truth side (a year effect of
0.358 against a decision line of 0.40) is computable without satellite data and
that no repair reaches the line, but that is an argument, not the missing
measurement.

**L6 — "Free cannot do it" is really "this configuration cannot do it".** For
seagrass we tried free 10 m visible bands and seven simple features. No
supervised classification, no multi-temporal compositing. For NO2 we did not
attempt emission inversion accounting for wind, chemical lifetime or vertical
profile. Our strongest evidence is a ceiling estimate — selecting the best of
seven candidate features *by looking at the ground truth* still tops out at
0.60 — which bounds that configuration and not the problem.

**L7 — "Zero procurement" means zero in central-government competitive
tendering.** Sole-source contracts are absent from the dataset, as is all
municipal procurement. Zero analysis contracts in 312,584 records is a strong
fact about one channel, and it does not establish that the work is not bought.

**L8 — The ledger of Section 4 is a lower bound.** It records defects we
found. A defect that produced a plausible value and was never contradicted by a
counter-hypothesis, an image or a physical ordering is, by construction, still
in the results. Two of the twenty-six were found only after we had already
published a figure derived from them.

---

## 6. Related work

**Use-case collections are collections of successes.** Japanese public-sector
material on satellite data utilisation is explicitly organised as good practice,
and the most useful commercial buying guide we found — a use-case-to-sensor
specification table published by a media outlet operated by a satellite
platform operator, with an accompanying price guide — is organised the same way,
because its purpose is to help a reader choose what to buy. Neither form has a
reason to record that a spectral index carries no information about buildings in
a dense urban area, or that a vegetation-condition index is measuring something
other than the agricultural damage it is used as a proxy for. This is not a
criticism of either: it is the gap they leave.

**Intercomparison exercises do publish failure, within a task.** The most
directly comparable work is the Cloud Mask Intercomparison eXercise conducted
under the CEOS Working Group on Calibration and Validation, which evaluates ten
cloud-masking algorithms over a common reference set and reports where each one
fails (Skakun et al., 2022). CMIX holds the task fixed and varies the
algorithm. We hold the budget fixed — free, unauthenticated data and simple
methods — and vary the task across nine industries. The two are complementary,
and the second appears to be much rarer: we did not find a cross-application
ledger of negative results in Earth observation in Japanese or English, though
we found partial precedents, including a Japanese agricultural-ministry
demonstration report that enumerates cases where interpretation was not
possible, and review articles in machine learning that collect cases where data
augmentation fails.

**Negative results and reproducibility.** The general argument for publishing
negative results is long-standing and we do not restate it. What this study adds
is quantitative: in a programme of this shape, roughly one measurement in four
was broken in a way that produced a plausible number, and **ten of those
twenty-six produced a flattering one**. Any estimate of how much of the positive
literature would survive the same audit has to start from the fact that the
flattering failures are the ones that survive review by their author.

**Ground-truth defects in benchmarks.** The closest methodological sibling is
our own earlier study of professional-practice benchmarks, which reports that a
benchmark's checking machinery — grader, calibration, adversarial suite — is
entirely a function of the reference solution and therefore cannot detect an
error in it (Ohkubo, 2026). The present work inverts the setting: there is no
grader, the reference is a procurement contract we cannot alter, and the thing
that breaks is the measurement rather than the answer key. The shared finding is
that internal consistency is not evidence, in either direction.

**Procurement records as a research instrument.** Awarded-contract open data is
normally used to study procurement itself — competition, pricing, supplier
concentration. Using it as an externally fixed statement of *what a task is and
what it is worth*, in order to score something unrelated to procurement, is the
methodological move we would most like to see reused. It is transferable to any
country with comparable disclosure, and it has the property that matters: the
researcher cannot move it after seeing their own results.

---

## 7. Discussion

### 7.1 What a contract value buys, when it can be read

Contract values are usually treated as opaque. In one case we could read one.
The 45.4 million yen flood-damage contract is not buying a better inundation
algorithm: the free archive contains no observation of the day of inundation,
and three days later the water is gone (AUC 0.574). What the money buys is the
right to task an acquisition. That is a statement about **which cell of §2.4 is
being purchased** — temporal sampling, and specifically the on-demand kind —
rather than about analytical capability.

Generalising across the nine: of six cells, only spatial sampling is priced,
and the on-demand corner of temporal sampling. Spectral degeneracy is solved by
an external register, not by a sensor — a photovoltaic panel and a roof are the
same spectrum, and the thing that separates them is a building footprint
database. Polarisation and phase are free and simply require processing.
Instrument drift is not priced at all. **A buying decision framed as "free
versus paid" is therefore the wrong frame for five of six cells.** This is a
sentence that neither a data vendor nor an agency promoting utilisation has any
reason to write, which is the whole reason we think it is worth publishing.

### 7.2 Correct and worthless

The NO2 result is the one we expect to be least popular and most useful. The
retrieval is right. The spatial pattern is the correct pattern for Japan. The
prefectures we named at freeze time as emitting more than population predicts
came out on top. And the satellite adds nothing, because prefectural CO2
emissions are already explained by population at 0.85 to 0.95, and the
satellite residual correlates with the excess at -0.051.

A technical-reach measurement that does not carry a counter-hypothesis will
score this as a success. Ours did not, only because the criterion had been
written before the run, and it had been written before the run only because the
previous industry had ended without answering the same question. **The
counter-hypothesis is not a robustness check appended to a result; it belongs
in the decision criterion, frozen.**

### 7.3 Good results as the dangerous ones

Ten of twenty-six defects returned a flattering number. We want to be precise
about why this is worse than it sounds.

A bad result triggers investigation automatically, because it is unpleasant and
because there is an obvious next action. A good result triggers writing up.
The defect population is therefore filtered: errors that hurt get fixed, errors
that flatter get published. No amount of care applied *after* seeing the result
corrects for this, because the care is applied selectively by the same
asymmetry.

The only countermeasure that worked was structural: freeze a prediction, and
treat a match as a trigger for audit rather than as a conclusion. It caught two
cases out of twenty-six. That sounds like a low yield until one notices that
those two were, respectively, a sensor artefact we were about to publish as a
physical signal, and a subsample we had no reason to take that happened to land
on the predicted value.

A second countermeasure was cheaper: **look at the objects**. Crop the
top-ranked detections, lay them out, and look. Three of the numbered
twenty-six were caught this way, and three more in the re-measurement of wall 1
before any result was recorded — including five objects identified as aircraft
on an airport apron that were all buildings in the town to the east, and
control points supposedly on empty pavement that were on car roofs. No
aggregate statistic in the study caught anything these did not, and several
aggregates were happily consistent with the defect.

### 7.4 For a reader deciding whether to use free Earth observation

Three practical consequences, in order of how much time they save.

1. **Decide the observable before the method.** Wall 2 was determined before
   any data was touched. If the phenomenon is invisible in the chosen
   observable — because the season is cloudy, because the quantity is phase and
   the free product discards phase — no amount of method work recovers it.
2. **Test threshold calibration with no ground truth.** Compute the detection
   rate in each window and look at its spread. A factor of three permits an
   absolute threshold; a factor of 23.7 requires a quantile. This single check
   moved one industry from "not reached" to "reached" and costs nothing.
3. **Fix the denominator before quoting an accuracy.** The same method, scene
   and date gave AUC from 0.387 to 0.897 under different masks, and a detector
   that finds nothing scores 83.6 to 99.7 per cent overall accuracy on a target
   occupying 0.3 to 3 per cent of the area.

### 7.5 For whoever funds the search for uses

Four of fifteen industries returned zero procurement in thirteen fiscal years,
and the largest contracts we could not classify are demonstration programmes for
finding uses. Public money is flowing towards use discovery precisely where
demand is not established, which is defensible. What we would note is that the
demonstrations are organised by theme, each looking at its own application.
**Nobody has an incentive to compare across themes**, and comparison across
themes is where the six-cell result came from: the observation that the wall in
one industry is the same cell as the wall in another, and that only one of the
cells has a price.

---

## 8. Availability

All code, frozen predictions, verdict files and measurement records are
publicly archived.

- **Implementation and measurement records** — `eisei-bench`: five core modules,
  fifteen industry implementations, and the replication, re-measurement and
  benchmark scripts. 105 result files, including the frozen `*_prediction.json`
  and `*_verdict.json` for every benchmarked industry, and the ledger of
  Section 4 as `docs/LEDGER.md`. MIT licensed.
- **This paper** — sources for the English text and the complete Japanese
  version, CC BY 4.0.
- **Public site** — https://satellite.dx-fukuoka.com/ presents the fifteen
  implementations with maps and figures.

No satellite imagery is redistributed; it is fetched at run time from free,
unauthenticated endpoints, and the acquisition procedures for every dataset,
including the ones we do not bundle, are documented. Bundled third-party data
is limited to OpenStreetMap extracts, which remain under ODbL 1.0 and are not
covered by the repository's MIT licence, and Japanese government statistics
redistributable with attribution.

Reference solutions come from the procurement portal's successful-bid open
data, which is public; the specific contracts used are listed with title,
contracting body, supplier and value in the repository rather than paraphrased
here, so that a reader can retrieve the same records.

**One record was deliberately not tidied.** The frozen result files contain
absolute filesystem paths from the machine that produced them, including a
directory name the project no longer uses. Rewriting them would make the
records look cleaner and would destroy the property that makes them records.
When the repository was renamed we re-ran one industry end to end and confirmed
that all seven reported metrics reproduce exactly; the frozen file was then
restored rather than updated.

---

## References

Hansen, M. C., Potapov, P. V., Moore, R., Hancher, M., Turubanova, S. A.,
Tyukavina, A., Thau, D., Stehman, S. V., Goetz, S. J., Loveland, T. R.,
Kommareddy, A., Egorov, A., Chini, L., Justice, C. O., & Townshend, J. R. G.
(2013). High-resolution global maps of 21st-century forest cover change.
*Science*, 342(6160), 850–853. https://doi.org/10.1126/science.1244693

Lyzenga, D. R. (1978). Passive remote sensing techniques for mapping water
depth and bottom features. *Applied Optics*, 17(3), 379–383.
https://doi.org/10.1364/AO.17.000379

NASA. *Terra's orbit changes*. Terra mission.
https://terra.nasa.gov/about/terras-orbit-changes — the last orbit-maintenance
manoeuvre was performed on 27 February 2020, after which the mean local time of
the equator crossing has drifted from 10:30.

Ohkubo, B. (2026). *Who checks the answer key? Ground-truth defects in eight
professional-practice benchmarks*. Preprint.
https://doi.org/10.5281/zenodo.21862231

Ohkubo, B. (2026). *eisei-bench: where free satellite data stops being enough*.
Software. DOI assigned on release; see the repository's `CITATION.cff`.

Skakun, S., Wevers, J., Brockmann, C., Doxani, G., Aleksandrov, M., Batič, M.,
Frantz, D., Gascon, F., Gómez-Chova, L., Hagolle, O., López-Puigdollers, D.,
Louis, J., Lubej, M., Mateo-García, G., Osman, J., Peressutti, D., Pflug, B.,
Puc, J., Richter, R., Roger, J.-C., Scaramuzza, P., Vermote, E., Vesel, N.,
Zupanc, A., & Žust, L. (2022). Cloud Mask Intercomparison eXercise (CMIX): An
evaluation of cloud masking algorithms for Landsat 8 and Sentinel-2. *Remote
Sensing of Environment*, 274, 112990. https://doi.org/10.1016/j.rse.2022.112990

### Data and primary sources

Procurement Portal (Japan). *Successful bid record open data*, FY2014–FY2026.
https://www.p-portal.go.jp/pps-web-biz/UAB02/OAB0201

Geospatial Information Authority of Japan. *Crustal deformation measurement
results by satellite SAR*. https://sarprod.gsi.go.jp/

Ministry of the Environment, Biodiversity Center of Japan. *National survey on
the natural environment: seagrass and seaweed bed survey (2018–2020)*.
https://www.biodic.go.jp/

Microsoft Planetary Computer. https://planetarycomputer.microsoft.com/ —
Sentinel-1 RTC, Landsat Collection 2 Level-2, Sentinel-5P, MODIS, Esri land
cover. Earth Search (Element 84). https://earth-search.aws.element84.com/v1 —
Sentinel-2 L2A, Copernicus DEM.

Copernicus Sentinel data 2017–2026, processed by ESA. Contains modified
Copernicus Sentinel data.
