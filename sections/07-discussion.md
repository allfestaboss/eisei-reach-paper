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

A second countermeasure was cheaper and caught more: **look at the objects**.
Crop the top-ranked detections, lay them out, and look. Nine of the
twenty-six were caught this way, including a case where five objects identified
as aircraft on an airport apron were all buildings in the town to the east, and
a case where control points supposedly on empty pavement were on car roofs.
No aggregate statistic in the study caught anything these did not, and several
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
