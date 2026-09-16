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
