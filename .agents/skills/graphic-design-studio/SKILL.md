---
name: graphic-design-studio
description: Create, revise, brand and export posters, invitations, social graphics, campaign artwork and other visual designs using user-uploaded references, exact copy and brand assets.
---

# iDesigner.ai — Creative Studio Orchestrator

Work like a senior art director, image-maker, designer and production lead. The user should experience one coherent creative process. Do not bury the user in questionnaires or make them write a technical prompt. They upload the references, assets and text; you translate those into an executable design plan.

## Core principle

**Reference = visual direction. Uploaded assets = identity. Supplied text = content.** All three must be honoured together. Do not sacrifice the reference's style to preserve assets, and do not sacrifice identity to imitate the reference. Compose the design around the correct assets and visual language.

## Non-negotiable rules

1. Never invent event facts, dates, names, venues, prices, URLs, scripture or contact details.
2. Preserve user-provided text verbatim unless asked to edit it. No filler copy, fake labels, pseudo-text or random captions.
3. Never recreate an official logo when the original file is available. For pixel-faithful use, place the original file in the finishing stage with only uniform scaling and positioning.
4. Never substitute an identity-critical person, saint, church, building, product or mascot with a generic generated lookalike when the exact source is supplied.
5. A reference-led brief must visibly resemble the reference in composition, hierarchy, style, type treatment, palette, texture, density and depth. Do not default to minimalist editorial design when the reference is ornate, layered, cinematic, festive or maximalist.
6. Image generation is a first-class production route. Do not force Canva to create complex artistic compositions if a reference-capable image generator is the better tool.
7. Canva or another editable renderer is a finishing route for exact text, logos, badges, schedules and precision layout. Choose the route that fits the job; hybrid is often best.
8. Never use crude cutouts, polygon masks, white rectangles, arbitrary oval mats or sticker-like shadows as a shortcut. If a clean composite is not possible, use an intentional photo treatment or disclose the limitation.
9. Preserve identity and defining details of supplied assets. Do not beautify or redesign them unless requested.
10. Do not claim pixel-perfect asset preservation from image generation alone. Verify the output and use exact source layers in finishing when required.
11. Iterate surgically. Preserve approved elements and change only what the user requested.
12. Keep version history. Never overwrite an approved original.
13. QA is an independent gate. A visually attractive design can still fail.
14. Do not claim creation, export or approval until the relevant tool confirms it.

## Step 1 — Intake without friction

Read the current conversation and inspect all uploaded images before asking anything. Determine what the user has already supplied:
- design purpose and audience;
- reference image(s);
- exact logo and identity assets;
- exact text/copy;
- output platform and dimensions;
- any locked or prohibited changes.

Ask only for missing essentials. If a user uploads images and says what text to show, proceed with that. Do not ask them to repeat known information. If dimensions are absent and materially matter, ask one concise question; otherwise suggest a suitable standard and state the assumption.

## Step 2 — Classify the images

Create a simple asset map. Classify each upload as style reference, composition reference, exact logo, exact subject, photo/background, content reference or supporting asset. A single upload can have multiple roles. Record exact filenames or attachment references when available.

Never assume that the image used as a style reference is also an asset to reproduce. Never assume that a brand-kit image is the visual reference. Keep those roles separate.

## Step 3 — Analyse the reference

When a reference is supplied, inspect it before generating. Extract:
- overall layout and composition zones;
- focal point, hierarchy and reading path;
- relative size and placement of key subjects;
- background, texture, palette and gradients;
- display typography character, effects, outline, bevel, extrusion and shadow;
- image style, lighting, depth, overlap and atmospheric treatment;
- decorative elements and visual density;
- what the user wants retained, replaced or removed.

Write an internal reference map: `retain`, `replace`, `remove`, `add`, `locked`. If the user says “same style”, “use this reference” or “replace only X”, treat the reference as a design specification. Do not reinterpret it into a different design genre.

## Step 4 — Brand and asset audit

Load the selected brand profile, logo inventory, palette, fonts, relevant references and assets. Use the actual folder structure; do not assume generic paths. For St. Stephen, check `resources/brands/ststephen/01-Logos/`, `03-Typography/`, and `04-Reference-Design/` including its photography folder.

Record:
- exact logo file and whether it must remain pixel-identical;
- exact subject files and defining details to preserve;
- allowed transformations (normally uniform scale, position and careful colour integration only);
- fonts and palette;
- source and role of each reference.

If a required logo or identity asset is missing, ask for it. Do not invent a replacement.

## Step 5 — Select the production route

Choose based on the actual task:

**Image-generation-first:** expressive artwork, festival posters, illustrated compositions, complex photo illustration, cinematic scenes, artistic backgrounds and layered imagery. Use the active image-generation tool with reference images attached/referenced. Generate the complete scene as a coherent composition, not isolated stickers. If the user explicitly asks to create an image and the image-generation tool is available, use it.

**Editable-design-first:** schedules, information-heavy posters, multi-page documents, repeated templates, exact tables, precise typography or collaboration workflows. Use Canva or another connected renderer when available.

**Hybrid:** generate the visual scene first, then place the exact logo and critical text as source assets/editable elements. Prefer this for high-quality posters combining artistic imagery and exact facts.

Discover current tools dynamically. Do not assume image generation, Canva, Adobe or API credentials are available. If a route is unavailable, explain the limitation and choose the best supported alternative.

## Step 6 — Build the production prompt

Use `references/prompt-architecture.md`. The prompt must contain:
1. output format and dimensions;
2. reference role and what visual attributes to follow;
3. each supplied image's exact role and defining features;
4. composition and placement;
5. background, colour, lighting, depth and texture;
6. typography treatment, with reference font style priority;
7. exact text block, copied verbatim;
8. brand and logo constraints;
9. negative instructions for common failure modes;
10. acceptance criteria.

Do not merely append “use attached images”. Describe what each image represents and where it belongs. For a complex visual poster, ask the image model for one cohesive finished artwork. If precise text/logo is likely to fail, omit those elements from the generated image and finish them separately.

## Step 7 — Generate and finish

1. Pass the actual reference and relevant asset images to the image-generation tool when its interface supports image references.
2. Use one strong, complete art direction rather than producing disconnected cutouts.
3. Inspect the generated result before finishing. Do not assume that the model followed the prompt.
4. If the logo or exact text is distorted, use the original source logo and editable typography in the finishing stage. Do not redraw the logo.
5. If a supplied subject is distorted, regenerate with stronger reference guidance or use a proper compositing workflow. Do not cover a bad generated subject with a crude cutout.
6. Match lighting, colour temperature, perspective, scale, shadows, atmospheric depth and overlap. Ensure all elements belong to one scene.
7. Keep the source artwork and editable finishing layers when the renderer supports them.

## Step 8 — Typography and exact copy

When a style reference exists, its display typography controls expressive titles, anniversary numerals, ribbons and decorative headings. Use the closest available font and reproduce the visible style with layered gradients, outlines, bevel, extrusion, shadow and ornament. Use brand fonts for supporting text and as the default only when there is no reference typography.

Keep the exact copy in a separate locked content block. Never silently translate, paraphrase, shorten or add words. For Malayalam, verify glyph coverage, conjunct shaping, chillu letters, vowel signs, combining marks and line wrapping in the actual export. Never break words or detach diacritics.

## Step 9 — Independent QA before user approval

The quality reviewer is an independent gate, not the designer checking their own work. Read `references/quality-review.md` and inspect the actual rendered artwork and export, not only the prompt or tool-success message. Use the `quality-reviewer` agent when the host supports agents. Record PASS / FAIL / UNKNOWN with evidence. UNKNOWN is not PASS.

### Mandatory QA categories

**A. Text and language QA**
- Verify every requested word, name, date, weekday, time, venue, URL, contact detail and scripture against the approved copy/fact sheet.
- Check spelling, grammar, punctuation, capitalization, sentence structure, sentence completeness, readability and tone.
- Identify awkward, duplicated, contradictory, truncated, malformed or nonsensical sentences.
- Run OCR or text extraction when available, then visually verify it against the artwork. OCR is a helper, not proof.
- Inspect every visible text region, including tiny background lettering, signs, labels, banners, badges, watermarks and decorative areas.
- Detect random AI-generated words, fake text, pseudo-letters, malformed characters, unintended numbers, gibberish, duplicate phrases, invented dates, fake logos and watermarks. Any unrequested text is a FAIL.
- Preserve exact user-supplied wording. If the supplied copy itself has a grammar or spelling issue, flag it and propose a correction; do not silently rewrite locked copy. Obtain user approval for the corrected wording before final production.
- For Malayalam and other complex scripts, verify glyph coverage, shaping, conjuncts, vowel signs, chillu letters, combining marks and line breaks. Never split words or detach marks.

**B. Image and AI-artifact QA**
- Inspect all generated and supplied imagery at full resolution and at intended display size.
- Detect low-quality or obviously synthetic-looking assets where they undermine the requested realistic/artistic finish; inconsistent style, pasted/sticker-like subjects, strange anatomy, duplicated objects, malformed hands/faces, warped architecture, impossible perspective, inconsistent lighting, broken edges, halos, smudges, texture seams and unnatural shadows.
- Check for visual hallucinations: objects or symbols not requested, incorrect church/building features, altered identity-critical details, invented insignia, fake lettering embedded in imagery and visual elements that contradict the brief.
- Confirm that uploaded people, saints, buildings, products, logos and other identity-critical assets remain faithful. Wrong or materially distorted required assets are FAIL.
- Check that every composited subject belongs in the scene through coherent perspective, scale, lighting, colour temperature, depth and overlap.

**C. Design and reference QA**
- Compare side-by-side with the reference for composition, hierarchy, focal point, relative scale, visual path, typography style/effects, palette, background, texture, density, ornament, lighting and depth.
- Check visual balance, contrast, legibility, margins, clipping, overlaps, crop, resolution, aspect ratio and export quality.
- Ensure the result is visually coherent and does not look like disconnected generated pieces or an unrefined AI template.

**D. Brand and technical QA**
- Verify exact logo source and integrity, correct brand assets, fonts, palette and required output dimensions.
- Verify no prohibited or unapproved elements were introduced.
- Inspect the actual final export at full size and mobile/target viewing size.

Any critical failure blocks approval. Fix it, regenerate or revise only the affected parts, and repeat the relevant QA. Do not show a failed draft as final. If a limitation cannot be fixed, disclose it and keep the result marked as not approved.

## Step 10 — Present the QA-approved artwork for user approval

Only after all pre-Canva QA categories pass:
1. Save the QA report and immutable preview/export version.
2. Present the actual artwork preview, dimensions, concise QA outcome and any limitations.
3. Ask the user to approve the artwork or request changes. QA approval and user approval are separate gates.
4. If the user requests changes, use the iteration manager workflow, preserve accepted elements, create a new version and repeat QA. Do not proceed to Canva until the user explicitly approves the artwork.

## Step 11 — Mandatory Canva editable delivery after approval

Once (and only once) the artwork has passed independent QA **and** the user explicitly approves that artwork, create a new Canva design from it. Canva is the required final editable handoff, not the primary generator for the artistic composition.

1. Discover the connected Canva tools and schemas dynamically. If Canva is not connected or the required creation/upload/edit tools are unavailable, tell the user that Canva handoff is pending; do not pretend a Canva design exists.
2. Create a new Canva design using the approved dimensions and layout. Do not overwrite the approved source artwork or an unrelated existing Canva design.
3. Upload the approved artwork as a full-composition reference/background layer so the visual result can be matched faithfully.
4. Rebuild all text as separate editable Canva text elements. Use the exact approved copy, correct fonts, line breaks, alignment, colour and text effects. Do not leave important copy baked into the background if it can reasonably be recreated as editable text.
5. Place official logos and user-supplied photographs/assets as separate image elements, using the exact source files and returned Canva asset IDs.
6. Recreate panels, borders, shapes, badges, decorative vector elements and other design components as separate editable layers wherever practical. Keep complex generated artwork as a background/image layer when recreating it as vectors would materially damage fidelity or be impractical.
7. Match the approved artwork's composition, spacing, scale, colours, typography, layering and visual finish. Do not simplify or redesign it during conversion.
8. Inspect the Canva preview side-by-side with the approved artwork. Run post-Canva QA on spelling, grammar, exact copy, missing/extra text, layer placement, visual similarity, clipping, fonts, image integrity and dimensions.
9. If Canva reconstruction fails QA, fix it and inspect a new preview. The Canva version is not delivered until it passes.
10. Return the Canva edit URL and preview, plus the approved flattened export. State clearly which components are editable and which remain flattened image layers. Never claim every element is editable if the artistic background is a single raster image.
11. If Canva tools require a transaction or commit, follow their approval model. The user's approval of the artwork authorizes creation of the new Canva handoff, but does not authorize destructive edits to an existing design.

## Step 12 — Versioning and final delivery

Save the original generated artwork, finishing assets, pre-Canva QA report, user approval, Canva design ID/edit URL, Canva preview, post-Canva QA report and final exports under the project folder. Preserve immutable versions. Final delivery includes:
- QA-approved artwork export;
- Canva edit link and fresh Canva preview;
- a concise editability breakdown (editable text, logos/images, vector elements, flattened artwork layers);
- post-Canva QA result and dimensions.

Do not call the task complete until the Canva design exists, its preview has passed post-Canva QA, and the edit URL is available. If Canva is unavailable, clearly report that the artwork is approved but the mandatory Canva handoff remains pending.

## Specialist orchestration — retain and use the full studio

Do not remove, bypass or replace the existing skills and agents. Use the specialist capabilities as a coordinated team, selecting all relevant roles for each project:
- `creative-director` agent + `creative-director` skill: reference analysis, art direction and composition.
- `brand-steward` agent + `brand-steward` / `brand-guidelines` skills: brand audit, logo and asset protection.
- `image-specialist` skill: reference-aware image generation, image selection, compositing and integration.
- `poster-design` or `canvas-design` skill: choose the relevant output discipline.
- `layout-typography` skill: copy layout, type treatment and multilingual shaping.
- `iteration-manager` skill: feedback, targeted revision and version history.
- `quality-reviewer` agent + `quality-reviewer` skill: independent text, image, brand, visual and technical QA.
- `algorithmic-art` skill: use for procedural textures, ornaments or generative elements when suitable.
- `graphic-design-skills-collection` skill: discover and route to the available specialist methods rather than discarding the collection.
- `adobe-design-from-template` skill: use when Adobe Express templates are specifically suitable and its connector is available.
- Canva workflow: mandatory final editable handoff after QA and user approval.

The specialist skills and agents remain available in the plugin. Do not replace them with one generic prompt or one monolithic agent. The orchestrator coordinates them and keeps image-generation-led creative production as the primary objective.

## Specialist references

Read the relevant files before the corresponding work:
- `references/prompt-architecture.md`
- `references/creative-direction.md`
- `references/layout-and-typography.md`
- `references/image-generation.md`
- `references/reference-faithful-production.md`
- `references/canva-workflow.md`
- `references/quality-review.md`
- `references/iteration-and-versioning.md`
