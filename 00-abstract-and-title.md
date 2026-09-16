# Abstract と表題（作業メモを含む。原稿には Title と投稿版 Abstract だけが入る）

**Title**

> No error was raised: twenty-six broken measurements from a cross-domain
> audit of free satellite data

代案:
- *Where free satellite data stops: seven walls across nine industries, and the
  twenty-six measurements that broke while finding them*（内容は正確だが二頭）
- *Good results are the ones nobody doubts: negative results from nine
  procurement-anchored satellite benchmarks*（重心は合うが説教くさい）

---

## 重心

> **無料の衛星データで「どこまでできるか」を業種横断で測ろうとすると、
> 測定そのものが壊れる。しかも壊れ方は例外を出さない。**
> 26件のうち10件は「良い結果」を返していた。

否定的結果を出すこと自体は主張にならない（負の結果の公開は既に規範として存在する）。
主張になるのは**規模と形**である ── 9業種を1つの物差しで通し、参照解を自分では
動かせない公費調達に置き、走らせる前に予測・判定基準・対抗馬を凍結した。
その設計のもとで、26件の測定不具合が**全部エラーを出さずにそれらしい値を返した**。

第2の主張は壁の分類にある。**技術の壁7種のうち、金で解けるのは1つだけだった。**
2つは手法ではなく測定器の性質（位相を捨てた無料プロダクト／軌道が漂流している
熱赤外センサ）で、1つはそもそも技術の壁ではない（正しく測れているのに、
既存の人口統計に上積みしない）。

---

## Abstract — 投稿版

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
drifting since orbit maintenance ended, bending a night-time land-surface-
temperature trend from +0.083 to +0.812 K/yr and contaminating every year we
wished to compare. One is not a technical wall at all: a satellite quantity can
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

*(Preprint. Not peer reviewed.)*
