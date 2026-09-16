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
