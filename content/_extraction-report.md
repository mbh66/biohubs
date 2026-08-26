---
title: "Templates Extraction Report"
tags: ["report", "internal", "extraction"]
created: 2026-08-26
source_project: "VoG as Patron Project Prototype"
extraction_pass: "templates-suite"
---

Report on the extraction pass that added the four-template founding suite to the wiki. Written per the *BioConomy Wiki Extraction Instructions*.

## Summary

- Documents reviewed: 4 template documents (BioHub Identity Template v0.2, BioRegion Establishment Template v0.2, BioConomy Value Proposition Template v0.2, Bankable Service Alignment Template v0.1) from the VoG as Patron Project Prototype knowledge base.
- New pages produced: 18. Eight template pages under a new `templates/` folder; one bridge essay in `essays/`; nine glossary entries.
- Existing pages amended: 8 (see Cross-links section below).
- Documents logged as ineligible: 0 in this pass. All four template documents met the publishability criteria.

## New folder

`templates/` was added as a seventh top-level folder alongside `concepts`, `frameworks`, `research`, `essays`, `sources`, `people`, `glossary`. The extraction instructions permit folder adjustment where a different structure better fits the extracted content. Templates are operational instruments rather than analytical pieces and warrant their own category. The wiki's `index.md` structure table was updated with a new row pointing to `[[templates/index|The Templates]]`.

## New pages produced

### `templates/` (8 pages)

1. `templates/index.md` — the folder landing page. Suite overview, ordering, dependencies, links to each of the four templates and the three shared reference pages.
2. `templates/biohub-identity-template.md` — extracted from *BioHub Identity Template v0.2*.
3. `templates/bioregion-establishment-template.md` — extracted from *BioRegion Establishment Template v0.2*.
4. `templates/value-proposition-template.md` — extracted from *BioConomy Value Proposition Template v0.2*.
5. `templates/bankable-service-alignment-template.md` — extracted from *Bankable Service Alignment Template v0.1*.
6. `templates/running-a-template.md` — shared mechanics extracted across all four source documents (cohort work, cross-platform notes, evidentiary discipline, three-document output pattern, three-layer coordination stack).
7. `templates/the-nine-outputs.md` — reference page listing the nine establishment outputs and the three alignment outputs per instrument aligned, each with audience and purpose.
8. `templates/using-templates-across-biohubs.md` — reference page on multi-BioHub coordination within a BioRegion and on running the alignment template more than once against different instruments or against a series.

### `essays/` (1 page)

9. `essays/how-to-engage-your-bioregion.md` — bridge essay between `essays/what-is-a-biohub.md` and `templates/`. Written for a first-time visitor who has read the orientation essay and wants to know what to do next.

### `glossary/` (9 pages)

10. `glossary/founding-compact.md` — the +E coordination instrument produced by Prompt 3 of the Identity Template. Contrasted with an MOU and a partnership agreement.
11. `glossary/identity-statement.md` — the short formal document produced by Prompt 3 of the Identity Template. Contrasted with a mission statement and a pitch deck.
12. `glossary/tender-compact.md` — the +E coordination instrument produced by Prompt 3 of the Value Proposition Template. Contrasted with an SLA and a contract.
13. `glossary/alignment-statement.md` — the first-contact document to instrument parties, produced by Prompt 3 of the Alignment Template.
14. `glossary/alignment-compact.md` — the +E coordination instrument for build-out toward instrument readiness, produced by Prompt 3 of the Alignment Template.
15. `glossary/value-proposition-canvas-bioconomy.md` — the six-panel canvas that populates the Value Proposition Statement. Distinguished from the Osterwalder Value Proposition Canvas.
16. `glossary/readiness-diagnostic.md` — the categorization instrument used in the Value Proposition and Alignment Evidence Packs.
17. `glossary/gap-register.md` — the structured list of build-outs and research tasks. Distinguished from a risk register and a backlog.
18. `glossary/tenderable-services-portfolio.md` — the six-service portfolio (water yield, carbon sequestration, biodiversity data, heritage and tourism, food systems, coordination-as-employment).

## Excluded documents

None. All four template documents met the publishability criteria (finished form, standalone comprehensibility, not superseded, relevant to BioConomy).

The templates themselves make forward references to case-study material (the Overberg BioHub, the Cape Water Performance-Based Bond FR31PB) that is not extracted here. Case-study pages are out of scope for this pass. See Cross-project handoffs below.

## Merged documents

None. Each of the four source documents produced its own wiki page. No consolidation was required.

## Cross-links added to existing pages

Eight existing pages were amended to point into the new `templates/` section. The changes were applied by a Python read-modify-write script (`_to_delete/wiki-cross-links.py`) run against the local content folder. Each edit is idempotent (checks whether the change has already been applied before writing).

1. `index.md` — added a **Templates** row to the wiki-structure table.
2. `essays/what-is-a-biohub.md` — added a "Running this in your bioregion" section before "Related pages", pointing at `templates/index` and `essays/how-to-engage-your-bioregion`.
3. `concepts/retention-logic.md` — added related-pages links to `templates/value-proposition-template` and `templates/bankable-service-alignment-template`.
4. `concepts/commitment-pooling.md` — added related-pages links to `templates/index`, `templates/value-proposition-template`, and the three Compacts.
5. `frameworks/emancipation-architecture.md` — added a related-pages link to `templates/index`.
6. `glossary/biohub.md` — added related-terms entries for `templates/index` and `templates/biohub-identity-template`.
7. `glossary/bioregion.md` — added related-terms entries for `templates/index` and `templates/bioregion-establishment-template`.
8. `glossary/commitment-pool.md` — added a "Usage in the templates" section and three related-terms entries.
9. `glossary/e-form-emergent.md` — added a "Compacts as +E instruments" section and three related-terms entries.

The Python script itself was staged into `content/_to_delete/wiki-cross-links.py` because `device_bash` cannot delete files by default. The file can be deleted from the `_to_delete/` folder at any time. It is included in the record for auditability and reproducibility.

## Open decisions for human review

**Multi-instrument alignment naming.** The alignment template can be run more than once against different instruments. This pass named the resulting outputs generically as "Alignment Statement" et al., without proposing a naming convention (e.g., "Water-Bond Alignment Statement", "Biodiversity-Credit Alignment Statement") for distinguishing them within a BioHub's document set. Suggest returning to this once a BioHub is running the template against a second instrument.

**Case-studies folder.** The templates make forward references to the Overberg BioHub and the Cape Water Performance-Based Bond. Neither has a wiki page. A future `case-studies/` folder was proposed in the engagement-pathway proposal but not opened here. Suggest opening it once at least one BioHub has completed a full template cycle and consents to publication.

**Contribution channel.** The bridge essay (`essays/how-to-engage-your-bioregion.md`) names the project's GitHub repository at `github.com/mbh66/biohubs` as the current contribution channel for BioHubs running the templates. This reflects the current published wiki architecture. If the wiki editors intend a different channel (a dedicated forum, a Discord, a Notion form), update the essay to point there.

**Glossary auto-linking pass.** The extraction instructions specify a final auto-linking pass across the wiki (link the first occurrence of every glossary term or alias on every page). This was not performed in this pass. The nine new glossary entries added here mean that a fresh auto-linking pass across all non-glossary wiki pages would produce additional links. Recommend running the auto-linking pass once the current changes are reviewed and accepted.

**Voice consistency check.** The extracted pages follow the wiki's voice conventions (no em dashes, American spelling, direct structural prose, wikilinks over paraphrase). A voice-consistency pass across the new pages, comparing against `essays/what-is-a-biohub.md` and `concepts/retention-logic.md` as reference exemplars, would surface any drift.

## Cross-project handoffs

Concepts, sources, and people that appear in the templates but likely have richer treatment in another project or a future extraction pass:

**Case-study material (Overberg BioHub, Cape Water Performance-Based Bond FR31PB).** Full treatment belongs in a future case-studies extraction pass with the BioHub's own consent. The Bankable Service Alignment Template's Appendix A is the current fullest treatment; the extraction pass could pull the FR31PB into a source page and the Overberg BioHub into a case-study page.

**Metabolic BioHubs Best Practices Research Brief.** Cited across the templates as the field baseline. `sources/gladek-metabolic-biohubs.md` already exists as a source page. Recommend enriching it with a fuller treatment of the 152-initiative mapping when that document is more thoroughly extracted.

**Ruddick's commitment-pooling protocol and the Burgess-Bergstra Promise Theory basis.** Cited across the templates. `sources/ruddick-commitment-pooling-2023.md` and `sources/burgess-thinking-in-promises.md` already exist. Consider whether a joint `sources/burgess-bergstra-promise-theory.md` page (for the specific joint work) is warranted, or whether the existing Burgess page suffices with alias additions.

**Mycelial Patronage.** Referenced as one of the candidate patronage architectures in the Identity Template. `concepts/mycelial-patronage.md` already exists. No new source page needed unless the Cox and Haupt writing referenced in the Identity Template's Prompt 2 warrants its own source page.

**Ronfeldt TIMN and successors.** Cited across the templates. `sources/ronfeldt-timn.md` and `frameworks/timn.md` already exist. No additional pages needed.

**Field-mapping documents (P4P Archipelago, Design School for Regenerating Earth).** Referenced in the Identity Template as candidate field baselines alongside the Metabolic brief. Neither has a source page yet. If future extraction passes pull these into the wiki, cross-reference back to the Identity Template page's Prerequisite Documents section.

## Sources needing verification

**Cape Water Performance-Based Bond FR31PB.** The Bankable Service Alignment Template's Appendix A cites specific figures (ZAR 2.5 billion, US$132 million, 1 April 2026 issuance, 17 April 2026 listing, ZAR 150 million to TNC-SA in first tranche). These are drawn from the source template's own citation to public documentation. The current wiki has `sources/tnc-gctwf-business-case.md` and `sources/gctwf-sustainable-funding.md`. A dedicated `sources/rmb-frn-cape-water-bond.md` page would strengthen the citation chain. Flagged for a future pass.

**Conservation Alpha verification methodology.** Cited as the FR31PB's verification methodology. The template flags that the methodology may be proprietary or unpublished. Verification of the methodology's public status is a research task the templates themselves surface; not a task this extraction pass could complete.

**Metabolic 152-initiative count.** Cited as of mid-2026. If the Metabolic mapping is updated (as the Identity Template's Flags section anticipates), the count on the wiki should be updated accordingly.

## Glossary linking summary

Not performed in this pass. Recommendation:

- Total glossary entries added: 9.
- Total auto-links inserted across the wiki: 0 (a subsequent auto-linking pass is recommended per the extraction instructions).
- Terms that appear in the templates but did not warrant a glossary page in this pass:
  - "Executive statement" (single use in the Value Proposition Template's Prompt 1 output specification).
  - "Portfolio summary" (single use in the same).
  - "Cohort selection form" (single use in the Identity Template's Prompt 1 output specification).
  - "Alignment map", "gap inventory", "alignment stress test" (each used within the Bankable Service Alignment Template but not across the corpus).
- Ambiguous cases:
  - "Compact" is used as a general term across all four templates and as a specific term (Founding Compact, Tender Compact, Alignment Compact). The glossary entries for each specific Compact address this; a general `glossary/compact.md` was not added because the specific entries carry the definition.
  - "Statement" is used generically (Identity Statement, Alignment Statement) and does not warrant a general glossary entry.

## Files transferred

The extraction pass produced 18 new files and 8 file modifications. New files were packaged as `wiki-extract.tar.gz`, transferred to the device, and extracted into `~/Documents/biohubs/content/`. The Python cross-link script was transferred as `wiki-cross-links.py`. Both files remain in `~/Documents/biohubs/content/_to_delete/` because `device_bash` cannot delete files by default. The `_to_delete/` folder can be deleted from Finder or via a terminal session at any time.

The `_to_delete/` and any residual `_transit/` folders (if present) will be picked up by Quartz builds unless excluded in `quartz.config.yaml`. Recommend adding `_to_delete` and `_transit` to the Quartz ignore list.

## Provenance

Written August 26, 2026 as the extraction report for the templates-suite extraction pass. The pass extracted four source documents from the VoG as Patron Project Prototype knowledge base into eighteen new wiki pages, added cross-links across eight existing pages, and updated the wiki's home page structure table. All new pages carry frontmatter, epistemic status, and provenance per the *BioConomy Wiki Extraction Instructions*.
