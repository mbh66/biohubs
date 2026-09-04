---
title: "Permacultr"
aliases: ["permacultr.io"]
tags: ["tool", "bioplace", "permaculture", "gis", "site-design"]
url: "https://permacultr.io/"
maintained_by: "Permacultr"
platform: "Web application"
pricing: "Free during public preview"
data_sources: ["OpenStreetMap", "Copernicus ERA5", "OpenTopoData", "SoilGrids", "SRTM"]
created: 2026-09-04
updated: 2026-09-04
source_project: "BioConomy"
source_documents: []
epistemic_status: "documented-fact"
---

Web-based site-planning tool for [[glossary/permaculture|permaculture]] design. The user draws a site boundary on a map, the tool layers open environmental data over the boundary (topographic contours, soil pH and texture and organic carbon, climate normals, water flow, sun aspect, slope), and the user sketches design elements (zones, swales, infrastructure) directly onto the data-informed base map. The result is a site plan grounded in the real terrain, climate, and hydrology of the specific parcel.

## Who it is for

The landing page names three audiences: designers running site surveys and preparing client presentations, smallholders assessing land before committing resources, and educators bringing real geographic data into permaculture coursework. All three sit inside the [[glossary/bioplace|BioPlace]] layer of the [[glossary/biostack|BioStack]].

## Technology and data

Permacultr is built on the open data commons: [OpenStreetMap](https://www.openstreetmap.org) for the base map, Copernicus ERA5 for climate normals, OpenTopoData and SRTM for elevation, and SoilGrids for soil properties. This stack matters. Building on well-maintained public datasets gives the tool consistent global coverage and transparent licensing terms, so a practitioner in any bioregion the open data covers can use it without geographic gating.

## What it does well at BioPlace scale

Permacultr fills a specific gap. Professional GIS software (ArcGIS, QGIS with plugins) can do everything Permacultr does and more, at the cost of a learning curve most BioPlace-scale practitioners cannot justify. Hand-drawn permaculture site plans on paper or in general-purpose drawing software carry no environmental data at all. Permacultr sits in the middle: a lightweight web interface a smallholder or design student can pick up in an afternoon, over the same open environmental data that professional planners work with.

## Notes and caveats

The tool is in public preview at the time of writing. Pricing after the preview period has not been announced. Data resolution varies by region (SoilGrids and SRTM coverage is global but not uniform), so a design decision that depends on fine-grained soil or elevation data should still be ground-truthed with on-site observation.

## Related pages

- [[glossary/bioplace|BioPlace]]
- [[glossary/permaculture|Permaculture]]
- [[concepts/the-bioplace-layer|The BioPlace Layer]]
- [[tools/bioplace/index|BioPlace Tools]]
- [[bill-mollison|Bill Mollison]]
- [[andrew-millison|Andrew Millison]]
- [[richard-perkins|Richard Perkins]]

## Provenance

Entry created 4 September 2026 as the first entry in `tools/bioplace/`. Substantive detail on features, data sources, target audiences, and pricing posture verified against the tool's current landing page on the same date.
