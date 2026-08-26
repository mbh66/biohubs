---
title: "Wiki Engagement Pathway Proposal"
tags: ["proposal", "internal", "wiki-architecture"]
status: "draft for review"
created: 2026-08-26
source_project: "VoG as Patron Project Prototype"
audience: "Wiki editor"
epistemic_status: "structural-inference"
---

A working proposal for content that would let a first-time visitor to https://wiki.bioconomy.earth pick up the four-template founding suite and run it in their own bioregion. Written against the current wiki structure (concepts, frameworks, research, essays, sources, people, glossary) and against the Bankable Service Alignment Template v0.1, which currently sits inside the VoG project docs but is not yet exposed on the public wiki.

This proposal is a suggestion layer only. It follows the BioConomy Wiki Extraction Instructions in structure, tagging, and voice. None of the pages below are written to final form here. The intent is that Michael reviews the shape, approves or edits it, and then a subsequent extraction pass writes the pages themselves.

## 1. The gap this proposal addresses

A visitor arriving at the wiki today can read the framework in depth. `essays/what-is-a-biohub.md` orients them. `concepts/retention-logic.md`, `frameworks/time-framework.md`, `concepts/water-retention-landscapes.md` and their neighbours give them the analytical vocabulary. `sources/gladek-metabolic-biohubs.md` places them in the emerging global field.

What is missing is any answer to the question the orientation essay opens up: "This wiki is a guide for establishing your own." The essay says the wiki is a guide. The wiki does not yet contain the guide.

The four templates in the founding suite (Identity, BioRegion Establishment, Value Proposition, Bankable Service Alignment) are that guide. They live in the project docs; they need a wiki-native form so a coordinator in Kerala or Cornwall or the Sonoran Desert can find them, understand what each does, and run them against their own place.

## 2. Proposed new top-level folder: `templates/`

Add a seventh top-level folder to the wiki alongside `concepts`, `frameworks`, `research`, `essays`, `sources`, `people`, `glossary`.

Name candidates, in order of preference:

1. **`templates/`**: matches the vocabulary the templates themselves use (Bankable Service Alignment Template, BioHub Identity Template). Reader knows immediately these are operational instruments, not analytical pieces.
2. **`practice/`**: broader, allows for later inclusion of case studies and worked examples beyond the four templates. Sacrifices the immediate legibility of `templates/`.
3. **`field-kit/`**: warmer, more inviting, less bureaucratic. Signals to a first-time visitor that this is the section where they do something rather than read about something. Sacrifices the direct match to the template vocabulary.

Recommendation: `templates/`. The word is what the source documents use, and reader legibility inside a wiki matters more than warmth. A tagline on the folder's index page can carry the warmth.

Update `index.md`'s wiki-structure table with a new row:

> **Templates**: The four-template founding suite for a BioHub cohort. Each template is a three-prompt sequence that a coordinator runs with a deep research AI platform, with cohort review between prompts, producing documents the BioHub uses to establish itself, its BioRegion, its value proposition, and its alignment to bankable instruments.

## 3. Pages proposed for `templates/`

Nine pages, in the order a visitor would encounter them.

### 3.1 `templates/index.md`

The folder landing page. One-sentence definition, one paragraph on what the suite does, a labelled diagram of the suite (four templates in sequence, nine outputs total, feeding into a tenth stage where alignment to a specific instrument becomes possible). Links to each of the four template pages, in order.

Body sections:

1. Definition: The founding suite for establishing a BioHub, its BioRegion, its value proposition, and its alignment to a bankable financial instrument.
2. What the suite produces: a list of the nine establishment outputs plus the three alignment outputs, tagged by which template produces them.
3. Order and dependencies: run the templates in order, one, two, three, four. Each template's outputs feed the next. Prompts within a template also run in order, with cohort review between them.
4. What the suite is not: not a business plan template, not a fundraising pack, not a substitute for cohort work. The templates coordinate the work; they do not perform it.
5. How to use these pages: read the template page, then follow the link to the source document, then run the prompts with the cohort.

### 3.2 `templates/running-a-template.md`

Practical guidance shared across all four templates. Written once here rather than repeated on each template page.

Body sections:

1. What a template is: a structured three-prompt sequence for use with a deep research AI platform, with cohort review between prompts.
2. Prerequisites: a coordinator, a cohort, a decision-making form, and the source documents each template lists.
3. The between-prompt cohort work: what it is, why it cannot be delegated to the AI, and what the decision-making form does.
4. Cross-platform notes: how to run the prompts on ChatGPT Deep Research, Claude Research, Perplexity, and Gemini, with the same portability notes the source templates carry.
5. Evidentiary discipline: the IC (Independently Corroborated), MS (Mission-Sourced), and TBV (To Be Verified) tagging system. Structural-inference labelling. The refusal to fabricate citations.
6. The three-document output pattern: each template produces a short formal Statement, a long referential Evidence Pack, and a short co-signed Compact. Reader learns the pattern once and recognises it in all four templates.
7. Handoff to operational work: what the outputs of one template become as inputs to the next.

This page is where the reader learns the mechanics of the suite. Each template page can then stay focused on that template's specific content.

### 3.3 `templates/biohub-identity-template.md`

The first template. Establishes the BioHub itself.

Body sections:

1. Definition: The first of four templates in the founding suite. Produces the BioHub's Identity Statement, its Field and Lineage Positioning, and its Founding Compact.
2. When to run: before any of the other three templates. When a coordinator has convened a cohort and the cohort is prepared to make founding commitments.
3. Prerequisites: the BioStack and BioConomy foundational document, the framework of coordination forms (TIME or equivalent), the commitment-pooling document, and the Metabolic BioHubs Best Practices Research Brief.
4. The three prompts: brief descriptions of what each prompt does. Reference the source document for full prompt text.
5. The three outputs: Identity Statement, Field and Lineage Positioning, Founding Compact. What each is, who reads it, what length to expect.
6. Cohort work between prompts: the coordinator's role, the decision-making form, the fact that these steps cannot be delegated.
7. Handoff: how the three outputs become prerequisite inputs to the BioRegion Establishment Template.
8. Related pages: [[biohub|BioHub]], [[commitment-pooling|Commitment Pooling]], [[frameworks/time-framework|TIME Framework]], [[e-form-emergent|+E Coordination Form]].
9. Sources: the Metabolic BioHubs Best Practices Research Brief once it has its own source page, plus any others referenced in the template.
10. Provenance: extracted from the BioHub Identity Template source document.

Repeat this structure for the next three template pages.

### 3.4 `templates/bioregion-establishment-template.md`

The second template. Establishes the BioRegion within which the BioHub operates.

Outputs to name in the body: BioRegion Definition, BioRegion Atlas, BioRegion Charter.

Cross-links to [[bioregion|BioRegion]], [[bioregional-economics|Bioregional Economics]], [[watershed-mapping|Watershed Mapping]], [[strategic-water-source-area-swsa|Strategic Water Source Area]], and the applicable [[frameworks/timn|TIMN Framework]] page.

### 3.5 `templates/value-proposition-template.md`

The third template. Establishes what the BioHub tenders into markets.

Outputs to name in the body: Value Proposition Statement, Value Proposition Evidence Pack, Tender Compact.

The Value Proposition Canvas is a six-panel structure: Living Substrate, Coordination Layer, Tenderable Services Portfolio, Counterparty Portfolio, Participant Portfolio, Retention Guarantee. Name each panel in the body and link where an existing wiki page carries the deeper concept.

Cross-links to [[retention-logic|Retention Logic]], [[transvestment|Transvestment]], [[payment-for-ecosystem-services-pes|Payment for Ecosystem Services]], [[commitment-pool|Commitment Pool]].

### 3.6 `templates/bankable-service-alignment-template.md`

The fourth template. Maps the BioHub's retention services onto a specific financial instrument.

Outputs to name in the body: Alignment Statement, Alignment Evidence Pack, Alignment Compact.

Body sections track the four-template pattern above, with one addition:

- A short section on the worked reference case in Appendix A of the source document (the Cape Water Performance-Based Bond, JSE ticker FR31PB), with a note that the appendix is illustrative and instrument-agnostic template use is the default.

Cross-links to [[performance-based-bond|Performance-Based Bond]], [[payment-for-ecosystem-services-pes|Payment for Ecosystem Services]], [[bioregional-financing-facility-bff|Bioregional Financing Facility]], and to the sources page for the Cape Water bond once it exists.

### 3.7 `templates/the-nine-outputs.md`

A reference page listing the nine establishment outputs (three per template for the first three templates) and the three alignment outputs. Each output has a one-paragraph description of what it is, what audience reads it, and where it feeds next. This page is what a coordinator hands to a cohort member who is trying to keep track of what document does what.

### 3.8 `templates/glossary-of-template-terms.md`

Alternative to scattering these across the main glossary: a short reference page collecting the terms that only appear inside the templates and their outputs. Examples: Identity Statement, Founding Compact, Value Proposition Canvas (BioConomy), Tender Compact, Alignment Statement, Alignment Evidence Pack, Alignment Compact, Readiness Diagnostic, Gap Register.

Alternative approach: each of these becomes a full entry in the main `glossary/` folder. Recommendation: the main glossary is the right place. See section 5 for the additions.

### 3.9 `templates/using-templates-across-biohubs.md`

A short reference page on multi-BioHub coordination within a BioRegion, and on running the same template again for a second target instrument. Reader learns that the suite is not one-shot: a BioHub aligned to a water bond may later run the fourth template again against a biodiversity credit instrument, and the two alignment compacts coordinate at the BioRegion Charter level.

## 4. Proposed orientation essay: `essays/how-to-engage-your-bioregion.md`

The essay layer currently holds one page. A second essay is proposed as the bridge between the orientation piece (`what-is-a-biohub.md`) and the templates folder. Written for a first-time visitor who has read the orientation essay and wants to know what to do next.

Body sections:

1. Where you are on the wiki: a paragraph placing this essay after the orientation piece and before the templates.
2. What engaging your bioregion means: convening a cohort, establishing the BioHub, mapping the BioRegion, defining the value proposition, and aligning to instruments the market recognises. Each phase has a template.
3. The four questions the templates answer: Who are we, what is our BioRegion, what do we tender, and which instrument does what we tender fit into.
4. What you need before you start: a coordinator, a small cohort willing to make founding commitments, a decision-making form the cohort agrees to work within, and access to a deep research AI platform.
5. What you do not need before you start: perfect information, a legal entity, capital, or permission. The suite is designed to produce what you do not yet have.
6. Where the templates cannot substitute for cohort work: the between-prompt steps, the legitimacy of founding commitments, the local knowledge the AI does not have. The wiki says this explicitly and often.
7. When to reach the wiki's editors: the intent is that BioHubs running the templates in different geographies contribute back into the wiki through case notes, precedent additions, and template revisions. State the contact pathway (email, GitHub issue, or whatever channel is available at the time of writing).
8. Related pages: [[essays/what-is-a-biohub|What Is a BioHub]], [[templates/index|The Templates]], [[templates/running-a-template|Running a Template]].

Voice register: same as `what-is-a-biohub.md`. First-person plural where the wiki as a whole is speaking; second-person singular where the reader is being addressed.

## 5. Glossary additions

Nine or so glossary entries are needed to support the templates section. Each follows the standard format the wiki already uses (frontmatter, one-sentence definition, extended definition, contrast with adjacent terms, usage in context, related terms, sources).

Proposed entries:

- `glossary/founding-compact.md`: term_type coined. The +E coordination instrument produced by Prompt 3 of the BioHub Identity Template. Contrast with a memorandum of understanding.
- `glossary/identity-statement.md`: term_type coined. The short formal document produced by Prompt 3 of the BioHub Identity Template. Contrast with a mission statement.
- `glossary/tender-compact.md`: term_type coined. The +E coordination and commitment document produced by Prompt 3 of the Value Proposition Template. Contrast with a service-level agreement.
- `glossary/alignment-statement.md`: term_type coined. The five-to-ten page document produced by Prompt 3 of the Bankable Service Alignment Template. First-contact document for instrument parties.
- `glossary/alignment-compact.md`: term_type coined. The +E coordination and commitment document produced by Prompt 3 of the Bankable Service Alignment Template. Contrast with the Tender Compact.
- `glossary/value-proposition-canvas-bioconomy.md`: term_type coined. The six-panel canvas produced by Prompt 3 of the Value Proposition Template. Contrast with the Osterwalder Value Proposition Canvas.
- `glossary/readiness-diagnostic.md`: term_type coined. Three-way categorisation (ready now, ready after specified build-out, not ready) applied in the Value Proposition and Alignment Evidence Packs.
- `glossary/gap-register.md`: term_type coined. Structured list of build-outs required for instrument readiness, produced across the third and fourth templates.
- `glossary/tenderable-services-portfolio.md`: term_type coined. The list of retention services the BioHub offers, produced by the Value Proposition Template.

Two existing glossary pages need small extensions:

- `glossary/commitment-pool.md`: add a paragraph on how commitment pooling shows up in the Founding Compact, Tender Compact, and Alignment Compact.
- `glossary/e-form-emergent.md`: add a paragraph on the Compacts as +E coordination instruments (voluntary, commitment-based, transparent, revisable).

## 6. Cross-links needed on existing pages

Existing pages that should gain a link into the new templates section:

- `essays/what-is-a-biohub.md`: append a short section titled "Running this in your bioregion" pointing to [[essays/how-to-engage-your-bioregion|How to Engage Your Bioregion]] and [[templates/index|The Templates]]. This closes the loop the current essay opens.
- `concepts/retention-logic.md`: add a related-pages link to [[templates/value-proposition-template|Value Proposition Template]] and [[templates/bankable-service-alignment-template|Bankable Service Alignment Template]] as the instruments through which retention logic becomes tenderable.
- `concepts/commitment-pooling.md`: add related-pages links to the three Compacts as instantiations at the BioHub scale.
- `frameworks/emancipation-architecture.md`: add a related-pages link to the templates as the practical instruments through which the Emancipation Architecture is instantiated in a specific place.
- `glossary/biohub.md` and `glossary/bioregion.md`: add related-terms entries to the template pages.

## 7. New source pages proposed

The templates cite several works that do not yet have wiki source pages. When the templates are extracted, these need to be created if the extraction pass finds them cited.

- `sources/burgess-bergstra-promise-theory.md`: the joint Burgess and Bergstra basis for commitment pooling as used across the four templates.
- `sources/ruddick-commitment-pooling-2023.md`: exists. Confirm cited from the template pages once extracted.
- `sources/metabolic-biohubs-best-practices.md`: the Metabolic BioHubs Best Practices Research Brief.
- `sources/gctwf-cape-water-bond.md`: RMB, FirstRand Bank, IFC, FSD Africa, Aluwani, TNC-SA, Conservation Alpha public documentation on the FR31PB.

The extraction pass will surface others as the four template documents are read through.

## 8. New people pages proposed

The people folder is already substantial. Two additions are proposed as the templates are extracted:

- `people/jan-burgess.md` (if not already covered under Mark Burgess's page). The joint work with Bergstra on promise theory as it applies to commitment pooling.
- `people/eva-gladek.md`: exists in the people folder. Confirm the Metabolic BioHubs Assessment source is cited from the template pages.

## 9. The visitor pathway

The pages above assemble into a five-step pathway for a first-time visitor:

1. **Land**: `index.md` explains what the wiki is and why now.
2. **Understand**: `essays/what-is-a-biohub.md` orients the reader to the coordination form the framework proposes.
3. **Assess**: `essays/how-to-engage-your-bioregion.md` (new) tells the reader what they need before they start and how the four templates map to the phases of establishment.
4. **Establish**: `templates/index.md` (new) presents the suite. The reader picks the first template and works through the four sequentially, with cohort review between prompts.
5. **Align**: on completion of the first three templates, the reader runs the Bankable Service Alignment Template against a specific instrument, using the reference case in Appendix A as an illustration.

Every page in the pathway carries the frontmatter, epistemic status, and provenance discipline the extraction instructions require. Every page has a clear next step. The reader who wants to skip the pathway and go straight to the templates can do so from the folder navigation; the pathway is available for the reader who wants a route through.

## 10. What this proposal does not include

- Full prompt text for the four templates. That belongs in the wiki pages themselves once extracted, or in a linked reference document if the prompts run long.
- Case-study pages for BioHubs that have already run the templates. When such case studies exist and meet the publishability bar, they belong in a future `case-studies/` folder that this proposal does not open.
- A public GitHub Discussions or issue-tracker workflow for BioHubs running the templates to contribute back into the wiki. That is a governance question for the wiki's editors.
- A translations plan. The wiki is written for an international audience in English; a translation strategy is a separate proposal.

## 11. Sequencing for implementation

If this proposal is approved, one workable sequence is:

1. Create the `templates/` folder and the `templates/index.md` landing page. This unblocks link resolution from other pages.
2. Extract the four template pages into `templates/` from the source documents in the project. The Bankable Service Alignment Template already sits in the project docs; the other three need to be located (Google Drive is a plausible location, given the connected resources).
3. Write `templates/running-a-template.md` and `templates/the-nine-outputs.md` as reference pages that lift shared material out of the individual template pages.
4. Add the nine glossary entries.
5. Write `essays/how-to-engage-your-bioregion.md`.
6. Add the cross-links from existing pages listed in section 6.
7. Update `index.md`'s wiki-structure table with the new row.
8. Do the glossary auto-linking pass across the new pages, per the extraction instructions.

Each of steps two through five can be a separate extraction pass. Step one can be committed today.

## Provenance

Drafted August 26, 2026, against the current published wiki at https://wiki.bioconomy.earth (as read via the live site and the local content folder at `~/Documents/biohubs/content/`) and against the Bankable Service Alignment Template v0.1 in the VoG project docs. The three preceding templates in the founding suite (BioHub Identity, BioRegion Establishment, BioConomy Value Proposition) are referenced but were not read in preparing this proposal; their treatment above rests on how the Bankable Service Alignment Template describes their outputs. A subsequent pass that reads all four template documents in full may adjust the glossary list, the number of pages in the templates folder, or the cross-link recommendations.
