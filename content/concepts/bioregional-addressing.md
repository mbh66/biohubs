---
title: "Bioregional Addressing"
aliases: ["bioregional addressing", "biospheric addressing", "address by bioregion"]
tags: ["concept", "coordination", "bioregion", "e-form", "addressing"]
created: 2026-09-04
updated: 2026-09-04
source_project: "BioConomy"
source_documents: []
epistemic_status: "documented-framework"
---

Every coordination architecture chooses a primary addressing unit, and the choice carries the architecture's assumptions about who counts as a coordinating actor. The [[glossary/economy|Economy]] uses the nation-state. Every phone number, tax ID, currency, and legal jurisdiction pins its identifier to a country code first. The BioConomy uses the [[glossary/bioregion|BioRegion]]. Every [[glossary/biohub|BioHub]] wiki address, currency, service catalogue, and coordination surface pins its identifier to a bioregion code first.

## The addressing pattern

A BioHub wiki lives at `{bioregion}-{slug}.bioconomy.earth`, where the bioregion code follows the One Earth Bioregions Framework (a two-letter realm prefix followed by a bioregion number) and the slug is a short name for the BioHub. The Valley of Grace BioHub in the Overberg publishes at `at12-vog.bioconomy.earth`. The Overberg BioRegion's coordinating entity publishes at `at12-overberg.bioconomy.earth`. The bioregion code sits at the front, and the BioHub identifier sits second. There is no country field.

The absence is deliberate. Country codes are the addressing layer of the [[glossary/economy|Economy]] and inherit its assumptions: that a bounded territorial polity is the primary unit of coordination, that a passport determines who can act, that a border decides where a service ends. None of those hold in the [[glossary/e-form-emergent|E form]]. A watershed does not stop at a border. A coordination surface published on a BioHub wiki is read by peers on other continents in the same reading action a same-country peer reads it.

## Why the choice matters

The address a coordination architecture publishes is one of the traces the [[concepts/stigmergy|stigmergic]] pattern reads. When a coordinator arrives at `at12-vog.bioconomy.earth` and finds a bioregion code at the front and no country segment at all, the address itself says what the wiki is doing: coordinating at the scale of the living landscape the bioregion names, above the scale of the political jurisdiction that happens to contain that landscape today. When the same coordinator arrives at `za-at12-vog.bioconomy.earth`, the address says something different: this BioHub coordinates within a national frame, and the national frame is the primary sort. The pattern reproduces the coordination logic of the Economy inside the E form.

The [[substrate-hypothesis|Substrate Hypothesis]] applies here as it applies everywhere. Coordination is a property of the substrate. Address is part of the substrate. An address that leads with a country code invites the coordination behavior countries expect. An address that leads with a bioregion code invites the coordination behavior the biosphere expects.

## What the addressing scheme actually holds

The One Earth Bioregions Framework carries eight biogeographic realms and 185 bioregions grouped from 847 ecoregions in the RESOLVE Ecoregions 2017 dataset. The scheme derives from vegetation type, climate zone, evolutionary history, and biogeographic distribution. Borders play no role in the boundary lines. Where a bioregion crosses a national border (the Great Karoo, the Congo Basin, the Amazon), the addressing scheme treats the bioregion as one unit and lets the geopolitical layer sort itself out at the layer where geopolitical concerns belong.

Where only one BioHub exists in a bioregion, the slug can be omitted: `at12.bioconomy.earth`. Add the slug when a second BioHub registers in the same bioregion. Where a bioregion coordinates multiple BioHubs, the bioregion-level entity itself publishes a wiki at `{bioregion}-{region-name}.bioconomy.earth`, as the Overberg does at `at12-overberg.bioconomy.earth`.

## What the choice rules out and what it enables

Ruled out: any inter-BioHub coordination pattern that requires a country field to route or resolve. A BioHub in the Amazon and a BioHub in the Congo Basin read each other's coordination surfaces on the same terms as two BioHubs in the same watershed. The address itself makes no distinction.

Enabled: coordination that scales from parcel to planet through one continuous addressing convention. A [[concepts/the-bioplace-layer|BioPlace]] belongs to a BioHub which belongs to a BioRegion which belongs to a realm which belongs to the biosphere. Every layer of the [[glossary/biostack|BioStack]] is addressable through the same convention, and every layer is discoverable by any peer without prior geopolitical context.

## Where the habit shows up

Bioregional addressing extends past URLs. Currency codes (ZA-FiCom is a first-generation instance and its successors will drop the country prefix as the pattern matures), service catalogue identifiers, verification credentials, and coordination-surface routing all follow the same convention. Every time the corpus writes an address, it is casting a vote about what unit the coordination sits inside. The habit is instilled by writing it consistently.

## Related pages

- [[concepts/stigmergy|Stigmergy]]
- [[substrate-hypothesis|Substrate Hypothesis]]
- [[concepts/economy-versus-bioconomy|Economy versus BioConomy]]
- [[concepts/the-bioplace-layer|The BioPlace Layer]]
- [[essays/how-to-build-a-biohub-wiki|How to Build a BioHub Wiki]]
- [[essays/how-the-bioconomy-coordinates|How the BioConomy Coordinates]]
- [[glossary/bioregion|BioRegion]]
- [[glossary/biohub|BioHub]]
- [[glossary/biostack|BioStack]]
- [[coordination-surface|Coordination Surface]]
- [[wiki-network/index|Wiki Network]]

## Sources

- Dinerstein, E. et al. (2017). *An Ecoregion-Based Approach to Protecting Half the Terrestrial Realm*. BioScience, 67(6), 534-545. [RESOLVE Ecoregions 2017](https://developers.google.com/earth-engine/datasets/catalog/RESOLVE_ECOREGIONS_2017).
- One Earth (2023). *Bioregions 2023*. [oneearth.org/bioregions-2023](https://www.oneearth.org/bioregions-2023/).
- [[sources/heylighen-stigmergy-universal-mechanism|Heylighen, F. (2016). Stigmergy as a universal coordination mechanism.]]

## Provenance

Written 4 September 2026 as the concept-level treatment of the BioConomy's addressing scheme and its rejection of country-code prefixes. Names the addressing choice as substrate design: the address itself carries the coordination logic the architecture wants to instill. Companion to the naming-convention update in [[essays/how-to-build-a-biohub-wiki|How to Build a BioHub Wiki]] made on the same date. The concept was named to give the habit somewhere to sit in the corpus so subsequent addressing decisions (currencies, credentials, service catalogues) can cite the same rationale.
