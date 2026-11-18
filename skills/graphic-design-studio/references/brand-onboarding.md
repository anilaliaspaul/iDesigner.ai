# Brand onboarding and reusable kits

iDesigner.ai must remain independent of every client identity. Ship only the empty generic template. Do not hard-code or bundle any real organization, church, company, logo or example brand.

## Find before creating
Ask which brand the design is for. Search the active workspace registry under `resources/brands/` by normalized slug and the exact/case-insensitive `brand.json` name. Read and verify the profile, not just the folder name.

- If found, tell the user and ask whether to use or update it. Load the saved kit.
- If not found, state that no saved brand kit exists and ask whether the user wants to create one. Do not create anything until they agree.
- If they decline, offer a one-off design without persisting a brand profile or ask them to select another brand.

## Create after consent
Collect official name, full address/location, recurring branding text, tagline/motto, official logo file(s) and website URL. If there is no website, ask the user to upload recent posters/designs that represent the brand. If no poster exists, use the interview and mark visual identity provisional. Allow optional fields to be skipped. Never fabricate missing details or logos.

## Build the kit
Create a brand folder in the active project workspace (not inside the installed public plugin directory) and populate:
- `brand.json`: name, slug, address, contact, branding text, tagline, website, audience, positioning, language, source provenance, confidence and approval status;
- `design-readme.md`: human-readable brand guide;
- `palette/palette.json`: colours, HEX, roles, source and confidence;
- `typography/font-inventory.json`: display/heading/body fonts and script coverage;
- `01-Logos/`: exact original logos;
- `04-Reference-Design/`: supplied brand posters and references;
- `05-Photography/`: approved photos and inventory;
- `research/`: optional research notes.

A website or poster can provide evidence, not automatic approval. Separate permanent brand identity from campaign-specific wording, dates and venues. Mark each field confirmed/inferred/unknown. Set status to proposed until user approval.

## Save, reload and approve
Save in the active workspace, validate, then re-read the saved files. Show a concise summary and request corrections/approval. Use the re-read files as the source of truth for the design. If persistent storage is unavailable, say so and provide exportable kit files.
