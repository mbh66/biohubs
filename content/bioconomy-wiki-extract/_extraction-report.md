# Extraction report: BioConomy wiki, glossary first pass

Generated 2026-08-24. Source: `BioHub_Glossary_1d3ef26c711e829e84538195cbcc8333.csv`.

## Summary

| Metric | Count |
|---|---|
| CSV rows reviewed | 110 |
| Glossary pages produced | 57 |
| Persons held for `/people/` extraction | 47 |
| Books held for `/sources/` extraction | 3 |
| Organizations held for `/sources/` or dedicated org handling | 3 |
| Instruction-cited terms absent from this CSV | 23 |

Source-tag distribution in the produced glossary pages:

- `Term`: 53
- `Research, Term`: 2
- `(unlabeled)`: 1
- `Resource`: 1

## Scope and method

This pass converts the BioHub Glossary CSV export (Notion) into individual markdown files under `/glossary/`, following the format specified in `bioconomy-wiki-extraction-instructions.md`. Every glossary-eligible row in the CSV became a page. Every non-glossary row (Person, Book, Organization) was held for a subsequent extraction pass targeting the appropriate wiki folder.

Each page carries: YAML frontmatter with title, aliases, tags, term_type, related_terms, source_project, dates, and epistemic_status; a one-sentence definition (the first sentence of the CSV "Short Description"); an optional `## Definition` section carrying any additional sentences from the source cell; a `## Related terms` section linking to other glossary entries; an optional `## Sources and associated figures` section linking to `/people/` and `/sources/` pages that will be created in subsequent passes; and a `## Provenance` block naming the source cell and any editorial actions.

The following spec-required sections are NOT present in first-pass output because the CSV alone does not carry the material: extended-definition beyond what the source cell provides, contrast with adjacent terms, and usage-in-context quotations. Filling these requires the underlying project documents that the CSV was distilled from. Each provenance note flags this.

## Editorial rules applied

**American spelling.** British forms in the CSV descriptions were converted (`organise` -> `organize`, `centre` -> `center`, etc.). Proper-noun terms that carry British spelling in their canonical name (`Bioregional Learning Centre`) were left unchanged; the title is treated as the fixed label the corpus uses. Flagged below for human review if this should change.

**No em dashes.** Em dashes and en dashes in source descriptions were replaced with comma-plus-space. In the handful of cases where the surrounding sentence would have read better with a period or colon, the comma still parses cleanly and preserves the source's rhythm.

**Voice preservation.** Descriptions were not rewritten, only cleaned. Where the CSV cell was one dense sentence, the page carries one dense sentence.

## Term-type inference

The `term_type` frontmatter field was assigned by heuristic:

- `acronym` when the name contains a parenthetical uppercase abbreviation (e.g., `Bioregional Financing Facility (BFF)`, `Strategic Water Source Area (SWSA)`, `P4P (Peer FOR Peer)`).
- `framework` for named frameworks (`TIME Framework`, `TIMN Framework`, `Two Machines`, `Regenerative Capitalism`, `Promise Theory`, `Prosocial`).
- `coined` for BioConomy-family terms (anything Bio*), the coordination-form shorthands (`T form (Tribal)`, etc.), and `Regeneration Economics`.
- `borrowed-technical` as the default for terms adopted from a source thinker with specific technical meaning.

These assignments are best-effort and should be spot-checked against the underlying project documents.

## Promoted entries

Two entries not tagged `Term` in the CSV were promoted into the glossary during extraction:

- **Watershed Mapping** (source tag: `Resource`). The description reads as a set of concepts and techniques rather than a specific tool or organization. It fits the glossary use case (a term referenced by other pages that a reader will need defined) better than a resource listing.
- **Regenerative Capitalism** (source tag: unlabeled). A named framework (John Fullerton, 2015) referenced by other entries in the CSV. Meets the glossary criterion for "named framework or architecture referenced repeatedly."

If a reviewer decides either should sit in `/frameworks/` or `/sources/` instead, the file moves without content change.

## Explicit exclusions from the glossary

Per the extraction instructions ("Proper nouns for people or organizations. These belong in `/people/` or `/sources/`, not the glossary"), the following were NOT written as glossary pages and are held for subsequent passes:

### Persons (47): destined for `/people/`

- Andrew Millison
- Benjamin Life
- Bill Baue
- Brandon Letsinger
- Carol Willis
- Charles Eisenstein
- Christian Bromberger
- Clare Attwell
- David Bollier
- David Ronfeldt
- Donella Meadows
- E.F. Schumacher
- Elinor Ostrom
- Ethan Roland
- Eva Gladek
- Ferananda Ibarra
- Georges Duby
- Gregory Landua
- Herman Daly
- Isabel Carlisle
- Jan Bergstra
- Jeff Emmett
- Joe Brewer
- John D. Liu
- John Fullerton
- Kate Raworth
- Leanne Ussher
- Leon Seefeld
- Lynne Twist
- Mark Burgess
- Michal Kravčík
- Michel Bauwens
- Mircea Eliade
- P.A. Yeomans
- Penny Heiple
- Peter Andrews
- Rajendra Singh
- Ralph Thurm
- Robert Scott
- Sacha Pignot
- Samantha Power
- Sepp Holzer
- Silke Helfrich
- Walter Jehne
- Wendell Berry
- Will Ruddick
- Zach Weiss

### Books (3): destined for `/sources/`

- Doughnut Economics
- Grassroots Economics
- Sacred Economics

### Organizations (3): destined for `/sources/` or a dedicated org-entity folder

- Guardians of Earth
- Metabolic Institute
- R3.0

## Merged documents

None. This pass runs against a single CSV export, so no cross-document consolidation was necessary. When the underlying project documents are extracted in subsequent passes, some will likely restate content already captured in these glossary stubs; those consolidations belong to the second pass and its report.

## Open decisions for human review

1. **`Regeneration Economics` vs `Regeneration Logic`.** The extraction instructions treat `Regeneration Logic` as the canonical term (with `regeneration economics`, `value retention`, `retention` as aliases). The CSV uses `Regeneration Economics` as the entry name. This first pass keeps `Regeneration Economics` as the page title (matching the CSV) and adds `regeneration logic` to the aliases list. A reviewer needs to decide whether to rename the file to `regeneration-logic.md` and swap the alias, or keep `regeneration-economics.md` as canonical and update the instructions.

2. **`Bioregional Learning Centre` spelling.** The rule is to convert British spellings to American except in proper nouns and direct quotes. This appears to be a proper noun (a specific corpus type-name), so the British `Centre` was preserved in the title. If the corpus treats the term as a generic concept, the file should be renamed to `bioregional-learning-center.md` and the title updated.

3. **`BioHub` vs `BioHub (field sense)`.** The CSV distinguishes the coordinating body from the emerging global field of similar initiatives (documented in Metabolic's 2026 assessment). Both got their own pages. A reviewer should confirm this two-page split matches the corpus intent, or fold the field sense into the main entry as a subsection.

4. **Promoted entries.** The two promotions above (`Watershed Mapping`, `Regenerative Capitalism`) should be confirmed or moved.

5. **Term-type assignments.** The heuristic classification may miscategorize borderline cases. `Prosocial`, for instance, was tagged `framework` on the strength of its name; if it's really a general adjective used across the corpus, `borrowed-technical` would be more accurate.

6. **`Sources and associated figures` section naming.** The instruction spec calls for a `Sources` section on glossary pages. Because many entries in this CSV reference both books (which will become `/sources/` pages) and individual thinkers (which will become `/people/` pages), the first pass used the combined heading `Sources and associated figures`. If the reviewer prefers strict adherence to `Sources`, the section can be renamed and the people links moved into a separate `Related people` section.

## Cross-project handoffs

The following will likely have richer treatment in other project extractions and should be revisited when other passes complete:

- **David Ronfeldt and the TIMN framework.** The CSV carries a short definition; the fuller intellectual treatment probably sits in the Emancipation Architecture project (which extends TIMN into the TIME variant).
- **Elinor Ostrom and Commons / Polycentricity.** The CSV entries are single-sentence; the governance-research thread probably holds the substantive treatment.
- **Will Ruddick, Commitment pool, and Mweria.** The Grassroots Economics book and Ruddick's Commitment Pooling Protocol are cross-referenced across at least three CSV entries; the primary treatment likely lives in a research-brief document not represented in this CSV.
- **Bauwens, Cosmo-local production, and Archipelago of Regenerative Projects.** The P2P Foundation lineage probably has fuller treatment elsewhere.

## Sources needing verification

Every glossary entry that cites a work or author currently does so inline in the definition text (`Benjamin Life, 2026`; `Power, Seefeld, et al., 2024`; `Bollier and Hulst`; etc.). None of these have been resolved to `/sources/` pages, because the sources pass has not yet run. When it does, these inline citations should be converted to wikilinks pointing at the appropriate source page.

Specific citations flagged for verification:

- `Benjamin Life, An Introduction to Bioregional Economics (2026)` — cited in `bioregional-economics.md`; full bibliographic details needed.
- `Power, Seefeld, et al. (2024)` — cited in `bioregional-financing-facility-bff.md`; full authorship and title needed.
- `Bollier and Hulst` — cited in `transvestment.md`; full work and year needed.
- `Metabolic (2026), BioHubs: A Pathway to Regional Resilience` — cited across `biohub.md`, `biohub-field-sense.md`; URL and full bibliographic form needed.
- `John Fullerton (2015)` — cited in `regenerative-capitalism.md`; the work is presumably his `Regenerative Capitalism` white paper for the Capital Institute; needs URL.

## Unresolved related-term references

Two related-term references from the source CSV point at entries that were deliberately excluded from the glossary (they belong in `/sources/` or an organization folder). Once those pages exist, the linking pass should resolve these:

- `Metabolic Institute` — referenced by: `BioHub`
- `Guardians of Earth` — referenced by: `BioScore`

## Terms cited in the extraction instructions but absent from this CSV

The instructions name a number of terms as glossary-worthy (both corpus-coined and borrowed-technical). The following are not present in this CSV and will need to be extracted from the underlying project documents in a subsequent pass. Their absence here should not be read as an editorial choice.

- Regeneration Logic
- Alpha Window
- Crisis Codes
- Emancipation Architecture
- Framer
- Threshold Guide
- Substrate Hypothesis
- Demurrage
- Panarchy
- Adaptive cycle
- Alpha phase
- Noosphere
- Threefolding
- Regenerative Participation Income
- Four Irreducible Entities
- Coercion Continuum
- RPI
- EA
- BCU
- TRANCRAA
- NWAP
- UCC Article 8
- TBV

## Glossary linking summary

The instruction spec calls for an auto-linking pass over the wiki after glossary pages exist: for each non-glossary page, link the first occurrence of any glossary term or alias. That pass cannot run until the other categories of pages (concepts, frameworks, research, essays, people, sources) exist. This first pass produces the lookup material the auto-linking pass will use:

- **Total glossary entries created:** 57.
- **Total aliases registered:** approximately 20 (parenthetical acronyms, coordination-form variants, and the Regeneration Economics / Regeneration Logic override).
- **Total intra-glossary wikilinks inserted:** every glossary page carries a `Related terms` section with wikilinks derived from the CSV's `Related Terms` column. This satisfies the intra-category link graph; the cross-category linking waits on the other passes.
- **Terms appearing in the corpus (CSV) but not meeting glossary criteria:** none flagged. Every non-Person, non-Book row was either extracted or explicitly promoted.
- **Ambiguous cases flagged above:** `Regeneration Economics` vs `Regeneration Logic`; `BioHub` vs `BioHub (field sense)`; `Bioregional Learning Centre` spelling; two promoted entries; term-type assignments.

## What was NOT produced in this pass

- `/concepts/`, `/frameworks/`, `/research/`, `/essays/`, `/sources/`, `/people/` folders and their pages.
- `index.md` for the wiki home.
- The auto-linking pass across non-glossary pages.
- Full extended definitions, contrast-with-adjacent-terms sections, and usage-in-context quotations for each glossary entry — these require the underlying project documents.

## Recommended next steps

1. Human review of the six open decisions above.
2. Extract the underlying project documents to produce `/people/`, `/sources/`, and the substantive `/concepts/` and `/frameworks/` pages.
3. Enrich each glossary stub with an extended definition, a contrast section where relevant, and one or two usage-in-context quotations from the source documents.
4. Add pages for the 23 instruction-cited terms currently absent from this CSV.
5. Run the auto-linking pass once the other categories exist.
