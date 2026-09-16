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
