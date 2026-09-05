---
title: "Wiki Network"
aliases: ["wiki network", "biohub network", "registered biohubs"]
tags: ["landing", "orientation", "wiki-network", "biohub"]
created: 2026-09-04
updated: 2026-09-04
source_project: "BioConomy"
source_documents: []
epistemic_status: "documented-framework"
---

BioHub wikis in the network. Each entry names a peer wiki that publishes a `coordination-surface.md` at the predictable path documented in [[essays/how-to-build-a-biohub-wiki|How to Build a BioHub Wiki]] and is therefore readable by the [[essays/how-the-bioconomy-coordinates|stigmergic coordination pattern]] the corpus describes.

## What listing here means

Listing here means the BioHub's wiki carries the layout convention that the interoperability of the network depends on. A coordinator (or the AI agent working on the coordinator's behalf) arriving at any entry in this folder can then read the peer's coordination surface directly at `{peer-wiki}/coordination-surface`, see what the BioHub offers and seeks, and identify complementarities against their own coordination surface.

Listing is a light-touch verification. The meta-wiki editorial team has read the peer wiki, confirmed it publishes the layout, and merged the pull request that added the entry here. It is not endorsement of the peer BioHub's service claims, financial-instrument alignments, or governance choices. Those the peer BioHub publishes on its own coordination surface and stands behind on its own.

## Distinction from related-wikis

The [[related-wikis/index|related-wikis folder]] holds external knowledge commons whose scope overlaps the BioConomy corpus (P2P Foundation, Omniharmonic, BioHubs.earth, Bioregioning Earth). Those are outside sources the corpus draws on.

This folder holds BioHub wikis inside the network. Each entry is a peer that publishes to the same layout convention, and coordination between the meta-wiki and each entry happens through the same reading-and-revising pattern that operates between any two peers.

## Currently listed

- [[at12-vog|Valley of Grace BioHub]] (`at12-vog.bioconomy.earth`). Overberg region, South African Cape Shrublands & Mountain Forests bioregion. Riviersonderend corridor.
- [[at12-overberg|Overberg BioRegion]] (`at12-overberg.bioconomy.earth`). The regional coordinating entity for the Overberg BioRegion, currently holding the Valley of Grace BioHub with anticipated additions at Volmoed and Witsand.

## Adding a BioHub

A BioHub coordinator who has published a coordination-surface page in the layout convention opens a pull request to `github.com/mbh66/biohubs` that adds a `wiki-network/{bioregion-code}-{slug}.md` file. The file follows the pattern of the entries currently listed and draws its content from the peer wiki's own coordination surface at the time of listing. The editorial team merges after checking that the wiki actually publishes the layout.

The [[concepts/bioregional-addressing|bioregional addressing convention]] specifies the URL format the file name should mirror. Country codes do not enter the address, and they do not enter the file name.

## Related pages

- [[index|Wiki Home]]
- [[coordination-surface|Coordination Surface]]
- [[essays/how-to-build-a-biohub-wiki|How to Build a BioHub Wiki]]
- [[essays/how-the-bioconomy-coordinates|How the BioConomy Coordinates]]
- [[concepts/bioregional-addressing|Bioregional Addressing]]
- [[related-wikis/index|Related Wikis]]

## Provenance

Folder created 4 September 2026 as the registry for peer BioHub wikis that publish the coordination-surface layout convention. Distinct from `related-wikis/`, which holds external knowledge commons whose material the BioConomy corpus draws on. Bootstrapped with the Valley of Grace BioHub and the Overberg BioRegion, the first two published entries. The folder is placed last in the wiki's alphabetical folder order so it sits at the bottom of the sidebar as the outward-facing edge of the network.
