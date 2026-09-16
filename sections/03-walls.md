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
