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
