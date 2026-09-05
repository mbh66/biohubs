---
title: "How to Build a BioHub Wiki"
aliases: ["biohub wiki", "building a biohub wiki", "biohub wiki layout"]
tags: ["essay", "orientation", "biohub", "coordination", "wiki"]
created: 2026-08-30
updated: 2026-09-05
source_project: "BioConomy"
source_documents: []
epistemic_status: "documented-framework"
---

A [[glossary/biohub|BioHub]] wiki is a standalone website that publishes a BioHub's local knowledge in a semi-structured form. Other BioHubs can read, both through human coordinators and through AI agents scanning for ways to combine efforts. This essay describes the layout, the conventions that make it interoperable across a [[glossary/bioregion|BioRegion]], and the reading pattern an AI agent follows when it arrives at a peer BioHub's wiki looking for collaboration.

## Overview

The [[frameworks/evolution-of-coordination-nodes|Evolution of Coordination Nodes]] traces the physical structures each coordination form produces as it matures: sacred site, cathedral, skyscraper, bioregional hub. The BioHub is the coordination node of the [[glossary/e-form-emergent|Emergent form]]. Its wiki is the knowledge layer of that node.

A single BioHub holds local knowledge no other BioHub holds: which sub-catchments are being restored, which monitoring methodology is producing usable data, which government frameworks the cohort has chosen to work within, which financial instruments the BioHub is aligning to, which services are contractable now and which are still in build-out. That knowledge is the raw material of inter-BioHub coordination. Without a structured way to publish it, peer BioHubs have to discover it through personal relationships and slow correspondence. With a structured wiki, an AI agent can read a peer BioHub's published knowledge in minutes and surface the specific complementarities a human coordinator would take weeks to identify.

This is [[glossary/mycelial-coordination|mycelial coordination]] made operational. The biological analogy holds: in a mature forest, the mycelial layer connects trees across species boundaries, distributing nutrients and information according to local need, without a central regulator. BioHub wikis connected across a BioRegion do the same thing for coordination knowledge. Each node publishes what it holds. The network reads what each node publishes. Complementary capabilities surface through the reading.

## What the wiki publishes

The wiki publishes the outputs of the [[templates/index|four-template founding suite]], organized for both human navigation and machine parsing. It assumes the founding suite has been completed and the nine establishment outputs exist. The content falls into eight areas.

**Identity.** The three outputs of the [[templates/biohub-identity-template|BioHub Identity Template]]: the [[glossary/identity-statement|Identity Statement]], the Field and Lineage Positioning, and the [[glossary/founding-compact|Founding Compact]]. These tell a peer BioHub who you are, what intellectual lineage you draw on, how your cohort is governed, and what patronage architecture funds the work.

**BioRegion.** The three outputs of the [[templates/bioregion-establishment-template|BioRegion Establishment Template]]: the BioRegion Definition, the BioRegion Atlas (broken into ecological, hydrological, soil carbon, biodiversity, jurisdictional, cultural, institutional, infrastructure, and climate profiles), and the BioRegion Charter. These tell a peer BioHub where you work, what the living system contains, and what governance principles your coordination operates under.

**Services.** The six-service [[glossary/tenderable-services-portfolio|Tenderable Services Portfolio]] from the [[templates/value-proposition-template|BioConomy Value Proposition Template]], with the Value Proposition Statement and the [[glossary/tender-compact|Tender Compact]]. Each service page carries its [[glossary/readiness-diagnostic|readiness status]], its [[glossary/retention-economics|retention]] logic, its monitoring and verification methodology, and its [[glossary/gap-register|gap register]] entries. These are the pages a peer BioHub's AI agent reads most closely, because they are where complementary capabilities surface.

**Alignments.** One subfolder per financial instrument the BioHub has run the [[templates/bankable-service-alignment-template|Bankable Service Alignment Template]] against. Each subfolder holds the [[glossary/alignment-statement|Alignment Statement]], the Alignment Evidence Pack, and the [[glossary/alignment-compact|Alignment Compact]]. Where two BioHubs target subsequent tranches of the same instrument series, their alignment pages are where joint coordination begins.

**Policy frameworks.** A dedicated index of every government framework the BioHub has chosen to embrace, organized by jurisdiction level (international, national, provincial, municipal) and by domain (water, biodiversity, land use, climate, cultural heritage, cooperative governance, finance). Each entry states the framework's name, the BioHub's adoption status, and links to the section of the Atlas, Charter, or Alignment Evidence Pack where the framework is treated in operational depth. Where a framework is substantial enough to warrant its own page (a national water act, a biodiversity offset regulation, a municipal spatial development framework), it gets one. The policy index is a coordination signal: two BioHubs operating under the same national water act have a natural basis for sharing compliance documentation, coordinating engagement with government agencies, and aligning verification methodologies.

**Data.** Monitoring information: what is measured, where, how often, by what methodology. [[glossary/bioscore|BioScore]] sub-scores where the BioHub is enrolled with Guardians of Earth. Baselines from the Atlas. This section carries structured metadata an AI agent can parse to compare monitoring approaches across peer BioHubs.

**Entities.** Reference pages for the institutional parties named across the BioHub's historical record and current coordination context: municipalities, government departments, church bodies, consultancies, community organizations, and other institutions the wiki refers to. Each entity page carries the factual record for the party (formation, mandate, actions taken, current position), so a reader arriving without context can situate every acronym and short name the wiki uses. Active partners with ongoing relationships to the BioHub get their fuller relational entry under Partners. A peer BioHub's AI agent uses the entities pages to disambiguate references it encounters in the historical record and to trace institutional continuity across time.

The line between Entities and Partners tracks physical domicile. An entity is any actor domiciled inside the BioRegion the BioHub anchors: the local and district municipalities, the community committees and residents' associations, the churches and their landholdings, the schools and museums, the businesses and cooperatives whose registered address sits within the BioRegion's territory. A partner is any actor whose domicile lies outside the BioRegion: a national government department headquartered in the capital, a consultancy working on a contract, a philanthropic funder, a verification agent, a peer BioHub in another bioregion. A party's page goes in the folder its domicile places it in, regardless of how frequently that party engages with the BioHub. Where a partner opens a local office within the BioRegion, an entity page opens for that office as well, with the two cross-linked and domicile treated as the primary organizing fact.

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
├── entities/                   Institutional parties named across the record
├── journal/                    Chronological coordination milestones
└── sources/                    Local source pages
```

The wiki links back to `wiki.bioconomy.earth` for shared vocabulary rather than duplicating it. Glossary terms, frameworks, concepts, and source pages that exist on the BioConomy wiki are linked there with full URLs. The BioHub wiki maintains local source pages only for works cited in its own documents that do not appear on the BioConomy wiki.

## The dual-layer convention

Every page is written for a human coordinator arriving without context. Every page also carries structured YAML frontmatter that an AI agent can extract without parsing prose.

Service pages carry frontmatter naming the service category, readiness status, counterparties, retention model, monitoring status, verification agent, applicable policy frameworks, gap count, and whether peer coordination is open. The coordination surface carries structured lists of offers, seeks, shared instruments, and contact protocols. The home page carries the BioHub's name, BioRegion, anchor location, founding date, link to the BioConomy wiki, and a list of known peer BioHubs with their wiki URLs.

The structured layer uses a controlled vocabulary consistent across all BioHub wikis. Service categories use the same six slugs everywhere: `water-yield`, `carbon-sequestration`, `biodiversity-data`, `heritage-and-tourism`, `food-systems`, `coordination-as-employment`. Readiness status uses the same three categories: `contractable-now`, `contractable-after-build-out`, `speculative-pending-research`. Page types use a shared set: `biohub-home`, `coordination-surface`, `biohub-service`, `policy-framework`, `biohub-data`, `journal-entry`, `alignment`, `cohort-member`, `partner`, `entity`. An AI agent filtering on type and service slug can match complementary capabilities across BioHubs without parsing a sentence.

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

A coordinator whose founding suite is complete populates the wiki in this order. The instructions below assume no prior experience with GitHub, the terminal, or static site generators.

### Naming your wiki

Every BioHub wiki sits at a subdomain of `bioconomy.earth`. The subdomain convention is:

```
{bioregion}-{slug}.bioconomy.earth
```

The components:

- **Bioregion**: the One Earth Bioregions Framework code, which combines a two-letter realm prefix with a bioregion number. The codes are built on the RESOLVE Ecoregions 2017 dataset. For the South African Cape Shrublands & Mountain Forests, the code is `at12`. The full list is at [oneearth.org/bioregion-list](https://www.oneearth.org/bioregion-list/).
- **Slug**: a short, recognisable name for the BioHub, typically three to five characters. The Overberg BioHub in the Riviersonderend catchment uses `vog` (Valley of Grace).

Examples: `at12-vog.bioconomy.earth`, `at10-laikipia.bioconomy.earth`, `nt1-xingu.bioconomy.earth`.

Where only one BioHub exists in a bioregion, the slug can be omitted: `at12.bioconomy.earth`. Add the slug when a second BioHub registers in the same bioregion.

The absence of a country field is deliberate. Country codes belong to the addressing layer of the [[glossary/economy|Economy]] and inherit its assumptions about who counts as a coordinating actor. The BioConomy anchors its addressing to the biosphere. The choice is treated at concept-level depth in [[concepts/bioregional-addressing|Bioregional Addressing]].

#### Finding your bioregion code

The bioregion code has two parts: a realm prefix and a bioregion number. To find yours:

1. **Identify your realm.** Eight biogeographic realms cover the planet. Find the one that contains your BioHub's location:

| Prefix | Realm | Approximate coverage |
|---|---|---|
| `at` | Afrotropic | Sub-Saharan Africa, Madagascar |
| `au` | Australasia | Australia, New Guinea, New Zealand, eastern Indonesia |
| `im` | Indomalayan | South and Southeast Asia, southern China |
| `na` | Nearctic | North America north of central Mexico |
| `nt` | Neotropic | Central and South America, Caribbean |
| `oc` | Oceania | Pacific islands, Hawai'i |
| `pa` | Palearctic | Europe, North Africa, northern and central Asia |
| `an` | Antarctica | Antarctic continent and subantarctic islands |

2. **Look up your bioregion number.** Go to [oneearth.org/bioregion-list](https://www.oneearth.org/bioregion-list/) and find the bioregion that covers your area. Each bioregion has a name and a number within its realm. The interactive map at [map.oneearth.org](https://map.oneearth.org/) lets you click your location to see the bioregion directly.

3. **Combine them.** The code is the lowercase realm prefix followed by the bioregion number, with no separator. A BioHub in the Laikipia Plateau sits in Afrotropic bioregion 10 (East African Montane Forests & Grasslands), so the code is `at10`. A BioHub in the Xingu basin sits in Neotropic bioregion 1 (Amazonian Forests & Grasslands), so the code is `nt1`.

The [[research/resolve-ecoregions-2017|RESOLVE Ecoregions 2017]] page on this wiki lists all 847 ecoregions that form the spatial foundation for these bioregion groupings.

### What you will need

Three things, all free:

1. A **GitHub account** at [github.com](https://github.com). If you do not have one, create one now.
2. A computer with a **terminal**. On macOS, open the application called Terminal. On Windows, use PowerShell. On Linux, use any terminal emulator.
3. An **AI assistant** (Claude, ChatGPT, or equivalent). The setup process involves terminal commands that an AI assistant can walk you through step by step.

### AI-assisted setup

If you are comfortable with Git and Node.js, skip to the command summary below. If not, paste the following prompt into your AI assistant. It will walk you through each step, wait for your confirmation, and troubleshoot any errors.

> I need to set up a BioHub wiki using Quartz v5, hosted on GitHub Pages. I have no experience with GitHub, Git, or the terminal. Walk me through the entire process one step at a time. Wait for me to confirm each step before moving to the next. If I encounter an error, help me fix it before proceeding.
>
> Here is what needs to happen, in order:
>
> **1. Install prerequisites.**
> I need Node.js v22 or higher and Git installed on my computer. Check whether I have them and install them if not. On macOS, use Homebrew. On Windows, use the official installers. Confirm the versions before proceeding.
>
> **2. Clone and set up Quartz.**
> Run these commands in sequence:
> ```
> git clone https://github.com/jackyzha0/quartz.git
> cd quartz
> npm i
> npx quartz create
> npx quartz plugin install --from-config
> ```
> During `npx quartz create`, I will be prompted for a template and a base URL. For the base URL, I should enter my BioHub's subdomain followed by `.bioconomy.earth` (e.g. `at12-vog.bioconomy.earth`). Do not include `https://` or a trailing slash.
>
> **3. Test the site locally.**
> Run `npx quartz build --serve` and confirm the site loads at `http://localhost:8080`.
>
> **4. Create a GitHub repository.**
> Go to github.com and create a new repository. Name it after my BioHub (e.g. `za-at2-vog-biohub`). Make it public. Do not initialise it with a README. Back in the terminal, set the remote origin to point to my new repository:
> ```
> git remote set-url origin https://github.com/MY-USERNAME/MY-REPO.git
> ```
>
> **5. Set up the GitHub Actions deployment workflow.**
> Create the directory `.github/workflows/` and inside it create a file called `deploy.yml`. The file should contain the standard Quartz GitHub Pages deployment workflow as documented at https://quartz.jzhao.xyz/hosting. The workflow should trigger on pushes to the `v5` branch, use Node.js 24, run `npm ci`, `npx quartz plugin install`, and `npx quartz build`, then upload the `public` directory as a Pages artifact and deploy it.
>
> **6. Push to GitHub and deploy.**
> Run `npx quartz sync` to push the site to GitHub. Then go to the repository's Settings, click Pages, and set the source to "GitHub Actions".
>
> **7. Configure the custom domain.**
> In the repository Settings under Pages, enter my custom domain (my subdomain of `bioconomy.earth`). Then help me understand what DNS record is needed: a CNAME record pointing my subdomain to `MY-USERNAME.github.io`. I will need to coordinate with the BioConomy wiki administrator to have this record added at the domain registrar.
>
> Confirm each step with me. If anything fails, diagnose the error and walk me through the fix.

Replace the placeholder values with your actual BioHub subdomain, GitHub username, and repository name before pasting.

The DNS record for the custom subdomain must be created by whoever controls the `bioconomy.earth` domain. Coordinate with the BioConomy wiki administrator to have your CNAME record added.

### Command summary (for experienced users)

```bash
# Prerequisites: Node.js >= 22, Git
git clone https://github.com/jackyzha0/quartz.git my-biohub-wiki
cd my-biohub-wiki
npm i
npx quartz create
npx quartz plugin install --from-config

# Test locally
npx quartz build --serve

# Create GitHub repo, then:
git remote set-url origin https://github.com/YOUR-USERNAME/YOUR-REPO.git

# Create .github/workflows/deploy.yml per https://quartz.jzhao.xyz/hosting
# Push and deploy
npx quartz sync

# In GitHub: Settings > Pages > Source: GitHub Actions
# In GitHub: Settings > Pages > Custom domain: your-subdomain.bioconomy.earth
# DNS: CNAME your-subdomain.bioconomy.earth -> YOUR-USERNAME.github.io
```

### Populating the wiki

Write the home page and `llms.txt` from the Identity Statement. Populate the identity folder from the three Identity outputs. Populate the BioRegion folder from the three BioRegion outputs, breaking the Atlas into the nine profile pages. Populate the services folder from the Value Proposition Statement, Evidence Pack, and Tender Compact. Populate the alignments folder from each Alignment run's three outputs.

Build the policy index by extracting every government framework referenced across the outputs and organising them by jurisdiction and domain. Populate the data pages from the monitoring and verification sections of the Atlas and Alignment Evidence Packs. Populate the cohort and partners pages from the Founding Compact and Alignment Compact. Populate the entities folder by extracting every named institutional party from the identity, alignment, policy, and historical pages, and writing a factual reference page for each.

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
- Dinerstein, E. et al. (2017). *An Ecoregion-Based Approach to Protecting Half the Terrestrial Realm*. BioScience, 67(6), 534-545. [RESOLVE Ecoregions 2017](https://developers.google.com/earth-engine/datasets/catalog/RESOLVE_ECOREGIONS_2017).
- One Earth (2023). *Bioregions 2023*. [oneearth.org/bioregions-2023](https://www.oneearth.org/bioregions-2023/).

## Provenance

Written 30 August 2026 as the operational companion to the four-template founding suite. The essay describes how a BioHub publishes its local knowledge for inter-BioHub coordination, drawing on the wiki layout specification produced in conversation with the BioConomy editorial team. The interoperability conventions (consistent folder names, controlled frontmatter vocabulary, dual-layer readability, the coordination surface as handshake page) are proposed standards. The first BioHub to publish a wiki using this layout is invited to feed refinements back through the project's GitHub repository at `github.com/mbh66/biohubs`.

### Changes from prior version

Revised 3 September 2026. The Getting Started section now includes a subdomain naming convention using ISO country codes, One Earth Bioregions Framework codes (built on the RESOLVE Ecoregions 2017 dataset), and a BioHub slug. Added a complete AI-assisted setup prompt that non-technical coordinators can paste into any AI assistant to be walked through Quartz installation, GitHub repository creation, GitHub Actions deployment, and custom domain configuration. Added a command summary for experienced users. Sources updated to include the RESOLVE Ecoregions dataset and One Earth Bioregions Framework.

Revised 5 September 2026. Added an Entities folder to the wiki layout, described in the What the Wiki Publishes and Populating the Wiki sections and shown in the folder structure. Added `entity` to the shared page-type vocabulary. Rationale: BioHubs operate inside institutional environments where municipalities, government departments, church bodies, consultancies, and community organizations are named repeatedly across the historical record and the current coordination context. A factual reference page for each such party lets a human coordinator and a peer BioHub's AI agent disambiguate acronyms and trace institutional continuity without having to reconstruct context from prose. Added a second Entities paragraph specifying the line between Entities and Partners as physical domicile inside the BioRegion, with the entities folder holding pages for parties domiciled inside and the partners folder holding pages for parties domiciled elsewhere.

Revised 4 September 2026. Removed ISO country codes from the subdomain naming convention. The scheme is now `{bioregion}-{slug}.bioconomy.earth`. Rationale: country codes belong to the addressing layer of the Economy. The BioConomy anchors its addressing to the biosphere. Added a paragraph explaining the choice and linking to the new [[concepts/bioregional-addressing|Bioregional Addressing]] concept page. Updated examples throughout to the country-free form (`at12-vog`, `at10-laikipia`, `nt1-xingu`). The Cape Shrublands bioregion example was updated to `at12` to match the codes in use across the current wiki network.
