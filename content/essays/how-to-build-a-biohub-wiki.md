---
title: "How to Build a BioHub Wiki"
aliases: ["biohub wiki", "building a biohub wiki", "biohub wiki layout"]
tags: ["essay", "orientation", "biohub", "coordination", "wiki"]
created: 2026-08-30
updated: 2026-08-30
source_project: "BioConomy"
source_documents: []
epistemic_status: "documented-framework"
---

A [[glossary/biohub|BioHub]] wiki is a standalone site that publishes a BioHub's local knowledge in a form peer BioHubs can read, both through human coordinators and through AI agents scanning for ways to combine efforts. This essay describes the layout, the conventions that make it interoperable across a [[glossary/bioregion|BioRegion]], and the reading pattern an AI agent follows when it arrives at a peer BioHub's wiki looking for collaboration.

## Overview

The [[frameworks/evolution-of-coordination-nodes|Evolution of Coordination Nodes]] traces the physical structures each coordination form produces as it matures: sacred site, cathedral, skyscraper, bioregional hub. The BioHub is the coordination node of the [[glossary/e-form-emergent|Emergent form]]. Its wiki is the knowledge layer of that node.

A single BioHub holds local knowledge no other BioHub holds: which sub-catchments are being restored, which monitoring methodology is producing usable data, which government frameworks the cohort has chosen to work within, which financial instruments the BioHub is aligning to, which services are contractable now and which are still in build-out. That knowledge is the raw material of inter-BioHub coordination. Without a structured way to publish it, peer BioHubs have to discover it through personal relationships and slow correspondence. With a structured wiki, an AI agent can read a peer BioHub's published knowledge in minutes and surface the specific complementarities a human coordinator would take weeks to identify.

This is [[glossary/mycelial-coordination|mycelial coordination]] made operational. The biological analogy holds: in a mature forest, the mycelial layer connects trees across species boundaries, distributing nutrients and information according to local need, without a central regulator. BioHub wikis connected across a BioRegion do the same thing for coordination knowledge. Each node publishes what it holds. The network reads what each node publishes. Complementary capabilities surface through the reading.

## What the wiki publishes

The wiki publishes the outputs of the [[templates/index|four-template founding suite]], organized for both human navigation and machine parsing. It assumes the founding suite has been completed and the nine establishment outputs exist. The content falls into seven areas.

**Identity.** The three outputs of the [[templates/biohub-identity-template|BioHub Identity Template]]: the [[glossary/identity-statement|Identity Statement]], the Field and Lineage Positioning, and the [[glossary/founding-compact|Founding Compact]]. These tell a peer BioHub who you are, what intellectual lineage you draw on, how your cohort is governed, and what patronage architecture funds the work.

**BioRegion.** The three outputs of the [[templates/bioregion-establishment-template|BioRegion Establishment Template]]: the BioRegion Definition, the BioRegion Atlas (broken into ecological, hydrological, soil carbon, biodiversity, jurisdictional, cultural, institutional, infrastructure, and climate profiles), and the BioRegion Charter. These tell a peer BioHub where you work, what the living system contains, and what governance principles your coordination operates under.

**Services.** The six-service [[glossary/tenderable-services-portfolio|Tenderable Services Portfolio]] from the [[templates/value-proposition-template|BioConomy Value Proposition Template]], with the Value Proposition Statement and the [[glossary/tender-compact|Tender Compact]]. Each service page carries its [[glossary/readiness-diagnostic|readiness status]], its [[glossary/retention-economics|retention]] logic, its monitoring and verification methodology, and its [[glossary/gap-register|gap register]] entries. These are the pages a peer BioHub's AI agent reads most closely, because they are where complementary capabilities surface.

**Alignments.** One subfolder per financial instrument the BioHub has run the [[templates/bankable-service-alignment-template|Bankable Service Alignment Template]] against. Each subfolder holds the [[glossary/alignment-statement|Alignment Statement]], the Alignment Evidence Pack, and the [[glossary/alignment-compact|Alignment Compact]]. Where two BioHubs target subsequent tranches of the same instrument series, their alignment pages are where joint coordination begins.

**Policy frameworks.** A dedicated index of every government framework the BioHub has chosen to embrace, organized by jurisdiction level (international, national, provincial, municipal) and by domain (water, biodiversity, land use, climate, cultural heritage, cooperative governance, finance). Each entry states the framework's name, the BioHub's adoption status, and links to the section of the Atlas, Charter, or Alignment Evidence Pack where the framework is treated in operational depth. Where a framework is substantial enough to warrant its own page (a national water act, a biodiversity offset regulation, a municipal spatial development framework), it gets one. The policy index is a coordination signal: two BioHubs operating under the same national water act have a natural basis for sharing compliance documentation, coordinating engagement with government agencies, and aligning verification methodologies.

**Data.** Monitoring information: what is measured, where, how often, by what methodology. [[glossary/bioscore|BioScore]] sub-scores where the BioHub is enrolled with Guardians of Earth. Baselines from the Atlas. This section carries structured metadata an AI agent can parse to compare monitoring approaches across peer BioHubs.

**Coordination surface.** The page that makes the mycelial pattern operational. It lists what the BioHub offers peer BioHubs (methodology, data, legal templates, cohort secondment, joint tenders), what it seeks from peer BioHubs (verification partnerships, entity-structure precedents, measurement capacity), and which financial instruments it is targeting where joint alignment would be valuable. The coordination surface is the first page a peer BioHub's AI agent reads after `llms.txt`.

## The folder structure

Each BioHub wiki runs its own Quartz instance at its own domain. The top-level folders are consistent across all BioHub wikis so that an AI agent navigating a peer BioHub's wiki can find the coordination surface, services, and policy pages at the same paths every time.

```
content/
├── index.md                    Home page
├── llms.txt                    AI entry point
├── coordination-surface.md     Offers, seeks, shared instruments
├── identity/                   Identity Statement, Field Positioning, Founding Compact
├── bioregion/
│   ├── definition.md           BioRegion Definition
│   ├── atlas/                  Nine profile pages
│   └── charter.md              BioRegion Charter
├── services/                   Six service pages + Value Proposition + Tender Compact
├── alignments/                 One subfolder per instrument
├── policy/                     Government frameworks index + individual pages
├── data/                       Monitoring, BioScore, baselines
├── cohort/                     Founding cohort and current participants
├── partners/                   Implementation partners, verification agents, peer BioHubs
├── journal/                    Chronological coordination milestones
└── sources/                    Local source pages
```

The wiki links back to `wiki.bioconomy.earth` for shared vocabulary rather than duplicating it. Glossary terms, frameworks, concepts, and source pages that exist on the BioConomy wiki are linked there with full URLs. The BioHub wiki maintains local source pages only for works cited in its own documents that do not appear on the BioConomy wiki.

## The dual-layer convention

Every page is written for a human coordinator arriving without context. Every page also carries structured YAML frontmatter that an AI agent can extract without parsing prose.

Service pages carry frontmatter naming the service category, readiness status, counterparties, retention model, monitoring status, verification agent, applicable policy frameworks, gap count, and whether peer coordination is open. The coordination surface carries structured lists of offers, seeks, shared instruments, and contact protocols. The home page carries the BioHub's name, BioRegion, anchor location, founding date, link to the BioConomy wiki, and a list of known peer BioHubs with their wiki URLs.

The structured layer uses a controlled vocabulary consistent across all BioHub wikis. Service categories use the same six slugs everywhere: `water-yield`, `carbon-sequestration`, `biodiversity-data`, `heritage-and-tourism`, `food-systems`, `coordination-as-employment`. Readiness status uses the same three categories: `contractable-now`, `contractable-after-build-out`, `speculative-pending-research`. Page types use a shared set: `biohub-home`, `coordination-surface`, `biohub-service`, `policy-framework`, `biohub-data`, `journal-entry`, `alignment`, `cohort-member`, `partner`. An AI agent filtering on type and service slug can match complementary capabilities across BioHubs without parsing a sentence.

## How an AI agent reads a peer BioHub's wiki

The reading sequence for an AI agent from BioHub A scanning BioHub B's wiki:

Fetch `llms.txt`. It carries a coordination-surface summary in the first 500 tokens: the BioHub's priority services and current seeks. The agent determines whether the profiles overlap before fetching anything else.

If overlap exists, fetch `coordination-surface.md`. Parse the structured YAML for offers, seeks, and shared instruments. Match against BioHub A's own coordination surface.

For each matching service, fetch the relevant service page. Check readiness status, verification methodology, and policy frameworks. Identify complementarities: one BioHub has the methodology, the other has the monitoring sites; one has the legal template, the other has the field experience.

Check the policy index for shared or adjacent government frameworks. Two BioHubs operating under the same national water act surface as natural coordination partners.

Check the alignments index for shared instrument targets. Two BioHubs targeting subsequent tranches of the same bond series should coordinate their alignment runs per the conventions in [[templates/using-templates-across-biohubs|Using Templates Across BioHubs]].

Check the data pages for comparable monitoring approaches. Where monitoring methodologies differ, flag the difference for human coordinators.

Produce a coordination brief: what BioHub B offers that BioHub A needs, what BioHub A offers that BioHub B needs, shared instruments, shared policy frameworks, and recommended next steps. Deliver the brief to BioHub A's coordinator.

This sequence is not prescribed in code. It is the reading pattern the wiki layout is designed to support. The structured metadata makes it tractable for any sufficiently capable AI agent given a link to a peer BioHub's wiki.

## The `llms.txt` file

Each BioHub wiki carries an `llms.txt` at the root, following the convention the BioConomy wiki already uses. It opens with a one-sentence identity statement, then lists the site's sections with one-line descriptions. The coordination surface section sits at the top of the site map so an AI agent can determine in the first read whether collaboration is worth exploring.

The `llms.txt` file names the BioHub's priority services and current seeks in plain text. It links to the coordination surface, the service pages, the policy index, and the alignment pages. It links to `wiki.bioconomy.earth` for the shared vocabulary and frameworks.

## The policy index

Government frameworks the BioHub has chosen to embrace get a dedicated index page organized by jurisdiction and domain. Each entry carries the framework name, jurisdiction, adoption status (`adopted`, `partially-adopted`, `under-review`, `monitoring`), a one-sentence summary, and a link to the Atlas, Charter, or Alignment section where the framework is treated in depth.

A dedicated policy page is warranted where the framework is load-bearing for the BioHub's operations, where the relationship involves specific compliance requirements or reporting obligations, or where the framework is not well-known outside its jurisdiction and a peer BioHub's AI agent would need more than a sentence to understand it.

The policy index serves as a coordination signal. When a peer BioHub's AI agent reads the policy index, it identifies shared regulatory environments. Two BioHubs operating under the same national water act, the same biodiversity offset regulations, or the same municipal spatial development framework have a natural basis for sharing compliance documentation, joint engagement with government agencies, coordinated tender submissions, shared verification methodologies, and policy advocacy.

## Relationship to the BioConomy wiki

The BioHub wiki and the BioConomy wiki serve different purposes. The BioConomy wiki at `wiki.bioconomy.earth` documents the architecture: the concepts, frameworks, templates, glossary, sources, and people that constitute the shared intellectual foundation. The BioHub wiki documents one instance of that architecture: this BioHub's identity, BioRegion, services, alignments, policies, data, and coordination surface.

A BioHub wiki never redefines a term the BioConomy wiki has defined. Where local usage extends a term, the BioHub wiki page states the local specifics and links to the BioConomy wiki for the general definition.

The BioConomy wiki holds the templates. The BioHub wiki publishes their outputs.

## Getting started

A coordinator whose founding suite is complete populates the wiki in this order:

Set up Quartz. Point it at the domain. Confirm the build pipeline works.

Write the home page and `llms.txt` from the Identity Statement. Populate the identity folder from the three Identity outputs. Populate the BioRegion folder from the three BioRegion outputs, breaking the Atlas into the nine profile pages. Populate the services folder from the Value Proposition Statement, Evidence Pack, and Tender Compact. Populate the alignments folder from each Alignment run's three outputs.

Build the policy index by extracting every government framework referenced across the outputs and organizing them by jurisdiction and domain. Populate the data pages from the monitoring and verification sections of the Atlas and Alignment Evidence Packs. Populate the cohort and partners pages from the Founding Compact and Alignment Compact.

Write the coordination surface from the Readiness Diagnostic, Gap Register, and the coordinator's knowledge of what the BioHub seeks from peers. Begin the journal with the founding milestone.

The wiki grows from there. Each new alignment run adds to the alignments folder. Each policy adoption adds to the policy index. Each monitoring cycle updates the data pages. Each coordination milestone adds to the journal. The coordination surface is revised as offers and seeks change. And each revision is legible to every peer BioHub whose AI agent reads the site.

## Related pages

- [[essays/what-is-a-biohub|What Is a BioHub]]
- [[essays/what-is-a-bioregion|What Is a BioRegion]]
- [[essays/how-to-engage-your-bioregion|How to Engage Your Bioregion]]
- [[essays/from-bioregion-to-bioregion|From a Bioregion to a BioRegion]]
- [[templates/index|The Templates]]
- [[templates/using-templates-across-biohubs|Using Templates Across BioHubs]]
- [[templates/the-nine-outputs|The Nine Outputs]]
- [[frameworks/evolution-of-coordination-nodes|The Evolution of Coordination Nodes]]
- [[concepts/mycelial-coordination|Mycelial Coordination]]
- [[concepts/carbon-silicon-partnership|Carbon-Silicon Partnership]]
- [[concepts/cosmo-local-production|Cosmo-Local Production]]
- [[glossary/tenderable-services-portfolio|Tenderable Services Portfolio]]
- [[glossary/readiness-diagnostic|Readiness Diagnostic]]
- [[glossary/coordination-node|Coordination Node]]
- [[glossary/bioscore|BioScore]]

## Sources

- [[sources/gladek-metabolic-biohubs|Gladek, E. et al. (2026). *BioHubs: A Pathway to Regional Resilience*]]
- [[sources/ronfeldt-timn|Ronfeldt, D. (1996). *Tribes, Institutions, Markets, Networks* (RAND P-7967)]]

## Provenance

Written 30 August 2026 as the operational companion to the four-template founding suite. The essay describes how a BioHub publishes its local knowledge for inter-BioHub coordination, drawing on the wiki layout specification produced in conversation with the BioConomy editorial team. The interoperability conventions (consistent folder names, controlled frontmatter vocabulary, dual-layer readability, the coordination surface as handshake page) are proposed standards. The first BioHub to publish a wiki using this layout is invited to feed refinements back through the project's GitHub repository at `github.com/mbh66/biohubs`.
