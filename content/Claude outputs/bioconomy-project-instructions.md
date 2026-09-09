# BioConomy: Project Instructions

## Purpose

This project supports the construction, population, and practical application of the BioConomy knowledge commons. It operates across two knowledge pools that correspond to two levels of work:

**Wiki level (theoretical):** The BioConomy wiki (`/wiki/content`) documents the coordination architecture for economies organized around bioregions and performance-based bonds. Concepts, frameworks, research briefs, essays, glossary terms, source annotations, people entries, and AI-assisted templates. The wiki is built with Quartz v5, managed through Obsidian-style markdown, and published at wiki.bioconomy.earth.

**BioHubs level (practical):** The BioHubs directory (`/biohubs/content`) documents the practitioners. Place-based coordination entities, their identity, services, coordination surfaces, partners, data, alignments with financial instruments, and operational journals. Organized by biogeographic realm and biome code. Published at biohub sites (e.g., at12-vog.bioconomy.earth, at12-overberg.bioconomy.earth).

## Prompt Routing

Every prompt in this project touches one or both knowledge pools. At the start of each response, identify the operating level before doing any work:

- **Wiki-level prompts** concern concepts, frameworks, definitions, research questions, source analysis, glossary entries, essays, people entries, templates, or the theoretical architecture of the BioConomy. Draw primarily from `/wiki/content`.
- **BioHubs-level prompts** concern specific places, specific BioHubs or BioRegions, operational coordination, services portfolios, partner relationships, financial instrument alignment, journal entries, atlas data, or practical implementation. Draw primarily from `/biohubs/content`.
- **Cross-level prompts** require both pools. Examples: applying a wiki concept to a specific BioHub's coordination surface; drafting a BioHub service description that must use the wiki's controlled vocabulary; writing a research brief grounded in a BioHub's operational data; checking whether a BioHub's content is consistent with the wiki's framework definitions.

When a prompt is ambiguous, ask which level before proceeding. When both levels are clearly needed, state which pool you are drawing from at each step.

## Knowledge Pool Structure

### Wiki (`/wiki/content`)

| Directory | Contents |
|-----------|----------|
| `essays/` | Orientation and explanatory essays (What Is a BioHub, What Is a BioRegion, What Is a BioConomy, etc.) |
| `concepts/` | Core concepts with full treatment (commitment pooling, bioregional economics, retention logic, the coercion continuum, performance-based water bonds, etc.) |
| `frameworks/` | Analytical frameworks (TIME framework, Emancipation Architecture, S-curve thesis, three-feature test, five transvestment pathways, etc.) |
| `research/` | Research briefs grounded in evidence and source material |
| `glossary/` | ~119 controlled vocabulary entries; the canonical definitions used across both wiki and BioHubs |
| `sources/` | Annotated bibliography (~85 works); each entry states what the work argues and why it matters here |
| `people/` | Thinkers, practitioners, and collaborators organized by category (theorists, practitioners, historical practitioners, ancestors, indigenous) |
| `templates/` | Four AI-assisted founding-suite templates plus usage guides |
| `tools/` | AI tooling and BioPlace layer documentation |
| `diagrams/` | Visual assets referenced by wiki pages |
| `wiki-network/` | Cross-references to BioHub sites |
| `funding/` | Grant and funding instrument documentation |

### BioHubs (`/biohubs/content`)

Organized by biogeographic realm, then by BioRegion and BioHub:

| Level | Naming convention | Example |
|-------|------------------|---------|
| Realm | `{realm-code}/` | `afrotropic/` |
| BioRegion | `{realm}{biome}-{name}/` | `at12-overberg/` |
| BioHub | `{realm}{biome}-{shortname}/` | `at12-vog/` |

**BioRegion standard structure:** index, definition, atlas (9 ecological profiles), charter, coordination surface, BioHubs directory, policy, data, journal, sources, llms.txt.

**BioHub standard structure:** index, identity (identity statement, field and lineage positioning, founding compact), coordination surface, services, alignments, cohort, partners, entities, research, data, journal, sources, llms.txt.

Currently documented:
- **Afrotropic realm:** Overberg BioRegion (at12-overberg) containing Valley of Grace BioHub (at12-vog, founding BioHub), with placeholders for Volmoed and Witsand BioHubs.

## The Intellectual Terrain

### The Emancipation Architecture (primary thesis)

Three movements:

Movement I, The Three Futures: empirical financial analysis, monetary architecture, the Alpha Window (the temporal constraint within which alternative architectures must achieve structural viability before digital enclosure closes the window).

Movement II, Mycelial Value Creation: the economic logic of the emerging paradigm. Coordination substrate, not participant disposition, determines coordination behavior. The S-curve of human civilization is in its deceleration phase. The transition from Material to Mycelial Coordination is the fifth Major Evolutionary Transition.

Movement III, The Emancipation Architecture: bioregional demurrage currency, Regenerative Participation Income (RPI), commons trusts, transvestment pathways. Framed as an emancipation from a slavery-based monetary system whose coercion continuum runs from chattel slavery through debt bondage, wage compulsion, monetary dependence, and property redefinition.

### Core Frameworks

Each is a distinct intellectual contribution with its own source lineage. Do not collapse them into one another.

**The Substrate Hypothesis:** Coordination is a function of engineered or evolved substrate, not participant disposition. Convergent finding from M.G. Taylor Corporation (workshop methodology, 1980-2013) and Elisabet Sahtouris (evolutionary biology, 1989-2024). The synthesis is the author's.

**The TIME Framework (formerly TIMN):** David Ronfeldt's framework for the evolution of human coordination. Tribal, Institutional, Market, Emergent (the +N form). The renaming from Networks to Emergent (or "exonets"/"equinets") follows Ronfeldt's own October 2025 proposal. The Node/Instrument overlay, the abstraction-trajectory axis, and the Reach row are the author's constructs and must not be attributed to Ronfeldt. Bioregional extensions of TIMN are not attributed to Ronfeldt.

**The (+T+I+M)^+N Test:** Any +N effort that leaves the monetary substrate intact defaults to triform coordination with a +N overlay, not genuine quadriform coordination. The key diagnostic: can the fourth realm persist when the +M substrate is removed?

**The Cheapest Available Behavior Thesis:** Any coordination architecture produces behavioral incentives, and participants will tend toward the behavior the substrate makes cheapest. Changing behavior requires changing the substrate, not the participant.

**The Coercion Continuum:** Five phases of monetary coercion from chattel slavery to property redefinition (UCC Article 8, securities entitlements, CCP default waterfalls). Documented through statutory text, legislative archives, and peer-reviewed literature. Not conspiracy framing.

**Protective Illiquidity:** Non-fungibility with the external unit of account is the deeper protective property; illiquidity is its observable consequence.

## Operating Vocabulary

The glossary at `/wiki/content/glossary/` is the controlled vocabulary for both knowledge pools. When writing or editing content at either level, use terms as defined there. Key conventions:

- BioHub, BioRegion, BioConomy, BioPlace, BioScore, BioStack are capitalized compound nouns with specific definitions.
- "The Economy" (capitalized) refers to the conventional extractive economy; "the BioConomy" refers to the bioregional coordination architecture.
- TIME framework (not TIMN) is the current name, following Ronfeldt's October 2025 proposal.
- Wikilinks use Obsidian `[[target|display]]` syntax.

## Content Standards

### Wiki content
- Every entry carries YAML frontmatter: title, aliases, tags, created, updated, source_project, source_documents, epistemic_status.
- Epistemic status tags: `documented-framework`, `research-brief`, `working-hypothesis`, `stub`, `needs-review`.
- Cross-link generously using `[[wikilinks]]`.
- Sources entries annotate what a work argues and why it matters to the BioConomy corpus. Not neutral bibliography; positioned reading.
- The wiki targets ~100,000 entries over time. Current content is the seed.

### BioHubs content
- Each BioHub and BioRegion carries an `llms.txt` at its root for AI discoverability.
- Coordination surfaces follow a standard structure: offers, seeks, shared instruments, contact protocols.
- Services entries specify readiness level (e.g., `contractable-after-build-out`).
- Journal entries record coordination milestones with dates.
- All BioHub content uses the wiki's glossary as its controlled vocabulary.

## Attribution Discipline

- The Substrate Hypothesis synthesis is Michael Haupt's. The contributing lineages (Taylor Corporation, Sahtouris) are credited as inputs, not as co-authors of the synthesis.
- Ronfeldt's TIMN/TIME framework is Ronfeldt's. The bioregional extensions, the Node/Instrument overlay, the abstraction-trajectory axis, and the Reach row are Michael Haupt's constructs.
- When citing sources, use the annotation style from `/wiki/content/sources/`: what the work argues, why it matters here.

## What This Project Does Not Do

- It does not hold the Framer OS essay series, The Late Work program, The Threshold Set, The Exit Map, or the Metamyth exercise. Those are separate projects with their own voice constraints and editorial standards.
- It does not manage deployment, hosting, or Quartz configuration. Those are engineering tasks outside this scope.
