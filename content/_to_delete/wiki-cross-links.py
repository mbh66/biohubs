#!/usr/bin/env python3
"""
Apply cross-link edits to existing wiki pages after the templates extraction.
Idempotent: each edit checks whether the change has already been applied.
"""

import os
import sys
from pathlib import Path

CONTENT = Path(os.path.expanduser("~/mnt/content"))

EDITS = []


def edit(path: str, marker: str, apply_fn):
    """Register an edit. marker is a string that, if present in the file, means the edit is already applied."""
    EDITS.append((path, marker, apply_fn))


# 1. glossary/commitment-pool.md — add extended paragraph on the three Compacts
def commit_pool(text: str) -> str:
    old = "## Related terms\n\n- [[promise-theory|Promise Theory]]"
    new = (
        "## Usage in the templates\n\n"
        "The commitment pool operates at two scales in the founding-suite templates. "
        "At the cohort scale, the [[founding-compact|Founding Compact]] pools the cohort's founding commitments to each other. "
        "At the tender scale, the [[tender-compact|Tender Compact]] pools the cohort's commitments to counterparties and participants. "
        "Where a BioHub aligns to a specific financial instrument, the [[alignment-compact|Alignment Compact]] pools the cohort's build-out commitments toward instrument readiness. "
        "All three are [[e-form-emergent|+E coordination instruments]] and are co-signed.\n\n"
        "## Related terms\n\n"
        "- [[promise-theory|Promise Theory]]"
    )
    return text.replace(old, new, 1)


edit(
    "glossary/commitment-pool.md",
    "## Usage in the templates",
    commit_pool,
)


# Add three compact links to commitment-pool's related-terms list
def commit_pool_related(text: str) -> str:
    old = "- [[needed|Needed]]\n"
    new = (
        "- [[needed|Needed]]\n"
        "- [[founding-compact|Founding Compact]]\n"
        "- [[tender-compact|Tender Compact]]\n"
        "- [[alignment-compact|Alignment Compact]]\n"
    )
    return text.replace(old, new, 1)


edit(
    "glossary/commitment-pool.md",
    "- [[founding-compact|Founding Compact]]",
    commit_pool_related,
)


# 2. glossary/e-form-emergent.md — add paragraph on Compacts as +E instruments
def eform(text: str) -> str:
    old = "## Related terms\n\n- [[time-framework|TIME Framework]]"
    new = (
        "## Compacts as +E instruments\n\n"
        "The three co-signed Compacts produced by the founding-suite templates ([[founding-compact|Founding Compact]], [[tender-compact|Tender Compact]], and [[alignment-compact|Alignment Compact]]) are +E coordination instruments. "
        "Their authority is voluntary, commitment-based, transparent, and revisable by the cohort through the decision-making forms established at the founding. "
        "They do not derive authority from any state, market, or prior institution. "
        "Where a Compact coexists with a legal entity form or a market contract, the Compact remains the governing document of the coordination work; the entity or contract serves the Compact.\n\n"
        "## Related terms\n\n"
        "- [[time-framework|TIME Framework]]"
    )
    return text.replace(old, new, 1)


edit(
    "glossary/e-form-emergent.md",
    "## Compacts as +E instruments",
    eform,
)


def eform_related(text: str) -> str:
    old = "- [[missing-middle|Missing middle]]\n"
    new = (
        "- [[missing-middle|Missing middle]]\n"
        "- [[founding-compact|Founding Compact]]\n"
        "- [[tender-compact|Tender Compact]]\n"
        "- [[alignment-compact|Alignment Compact]]\n"
    )
    return text.replace(old, new, 1)


edit(
    "glossary/e-form-emergent.md",
    "- [[founding-compact|Founding Compact]]",
    eform_related,
)


# 3. glossary/biohub.md — add related terms
def biohub(text: str) -> str:
    old = "- [[biostack|BioStack]]\n"
    new = (
        "- [[biostack|BioStack]]\n"
        "- [[templates/index|The Templates]]\n"
        "- [[templates/biohub-identity-template|BioHub Identity Template]]\n"
    )
    return text.replace(old, new, 1)


edit(
    "glossary/biohub.md",
    "- [[templates/index|The Templates]]",
    biohub,
)


# 4. glossary/bioregion.md — add related terms
def bioregion(text: str) -> str:
    old = "- [[biostack|BioStack]]\n"
    new = (
        "- [[biostack|BioStack]]\n"
        "- [[templates/index|The Templates]]\n"
        "- [[templates/bioregion-establishment-template|BioRegion Establishment Template]]\n"
    )
    return text.replace(old, new, 1)


edit(
    "glossary/bioregion.md",
    "- [[templates/bioregion-establishment-template|BioRegion Establishment Template]]",
    bioregion,
)


# 5. essays/what-is-a-biohub.md — append a "Running this in your bioregion" section before "## Related pages"
def what_is_biohub(text: str) -> str:
    marker = "## Related pages"
    insertion = (
        "## Running this in your bioregion\n\n"
        "This wiki is a guide for establishing your own. The four-template [[templates/index|founding suite]] is where that guide sits. "
        "Start with [[essays/how-to-engage-your-bioregion|How to Engage Your Bioregion]] for the bridge from the orientation above to the templates themselves.\n\n"
        "## Related pages"
    )
    return text.replace(marker, insertion, 1)


edit(
    "essays/what-is-a-biohub.md",
    "## Running this in your bioregion",
    what_is_biohub,
)


# 6. concepts/retention-logic.md — add related-pages links
def retention_logic(text: str) -> str:
    old = "- [[commitment-pooling|Commitment Pooling]]\n"
    new = (
        "- [[commitment-pooling|Commitment Pooling]]\n"
        "- [[templates/value-proposition-template|BioConomy Value Proposition Template]]\n"
        "- [[templates/bankable-service-alignment-template|Bankable Service Alignment Template]]\n"
    )
    return text.replace(old, new, 1)


edit(
    "concepts/retention-logic.md",
    "- [[templates/value-proposition-template|BioConomy Value Proposition Template]]",
    retention_logic,
)


# 7. concepts/commitment-pooling.md — add related-pages links
def commitment_pooling_concept(text: str) -> str:
    # Find the Related pages section and append template links
    marker = "## Related pages"
    if marker not in text:
        return text  # Skip if section missing
    # Insert after the marker line and before the next section (## Sources or ## Provenance)
    # Simple approach: find "## Sources" and insert links just before it, after Related pages content
    # Better: append to end of Related pages list. Use "\n## Sources" as boundary.
    boundary = "\n## Sources"
    if boundary not in text:
        boundary = "\n## Provenance"
    if boundary not in text:
        return text
    prefix, suffix = text.split(boundary, 1)
    # Append links to the end of Related pages section
    addition = (
        "\n- [[templates/index|The Templates]]"
        "\n- [[templates/value-proposition-template|BioConomy Value Proposition Template]]"
        "\n- [[glossary/founding-compact|Founding Compact]]"
        "\n- [[glossary/tender-compact|Tender Compact]]"
        "\n- [[glossary/alignment-compact|Alignment Compact]]"
    )
    return prefix + addition + boundary + suffix


edit(
    "concepts/commitment-pooling.md",
    "- [[templates/index|The Templates]]",
    commitment_pooling_concept,
)


# 8. frameworks/emancipation-architecture.md — add related-pages link
def ea(text: str) -> str:
    marker = "## Related pages"
    if marker not in text:
        return text
    boundary = "\n## Sources"
    if boundary not in text:
        boundary = "\n## Provenance"
    if boundary not in text:
        return text
    prefix, suffix = text.split(boundary, 1)
    addition = (
        "\n- [[templates/index|The Templates]]"
        " (the practical instruments through which the Emancipation Architecture is instantiated in a specific place)"
    )
    return prefix + addition + boundary + suffix


edit(
    "frameworks/emancipation-architecture.md",
    "- [[templates/index|The Templates]]",
    ea,
)


# 9. content/index.md — add templates row to the wiki-structure table
def index_page(text: str) -> str:
    # Add row for Templates to the markdown table.
    old = "| **People**     | The thinkers, practitioners, and collaborators whose work feeds the BioConomy corpus.                                                |"
    new = (
        "| **People**     | The thinkers, practitioners, and collaborators whose work feeds the BioConomy corpus.                                                |\n"
        "| **Templates**  | The four-template founding suite for a BioHub cohort. Each template is a three-prompt sequence run with a deep research AI platform, with cohort review between prompts. Start at [[templates/index\\|The Templates]]. |"
    )
    return text.replace(old, new, 1)


edit(
    "index.md",
    "| **Templates**",
    index_page,
)


# Apply
applied = []
skipped = []
missing = []
for path, marker, fn in EDITS:
    full = CONTENT / path
    if not full.exists():
        missing.append(path)
        continue
    text = full.read_text()
    if marker in text:
        skipped.append(path)
        continue
    new_text = fn(text)
    if new_text == text:
        # Edit function didn't change anything (marker for edit couldn't be found).
        skipped.append(f"{path} (no change; pattern not found)")
        continue
    full.write_text(new_text)
    applied.append(path)

print("Applied edits:")
for p in applied:
    print(f"  {p}")
print()
print("Skipped (already applied):")
for p in skipped:
    print(f"  {p}")
print()
if missing:
    print("Missing files:")
    for p in missing:
        print(f"  {p}")
