# Production prompt architecture

Use this structure to turn a brief plus image uploads into a production-ready prompt. The user should not need to author it.

## A. Reference map

For each image, record filename/reference and role:
- Style reference: visual language, type treatment, colour, texture, light, density.
- Composition reference: positions, scale, overlap, visual hierarchy.
- Exact logo: protected identity asset.
- Exact subject: person, saint, building, product, mascot, etc.
- Background/photo: environment or photographic scene.
- Content reference: source facts/copy, only when authorized.

State clearly which attributes transfer from the reference and which subjects/text are replaced.

## B. Mandatory size and output-dimension intake

Poster, flyer, invitation, banner, social graphic and other fixed-canvas work must have an explicit output size before production.

- Check the current conversation and uploaded brief first. If the user already supplied dimensions, use them and do not ask again.
- If dimensions are missing, ask one concise question for the intended width, height and unit (for example, 10 cm × 15 cm, A4, or 1080 × 1350 px). Do not silently assume a size.
- If the user does not know, offer a suitable standard size based on the intended use and ask them to confirm it.
- If the platform or print destination is known but dimensions are not, ask for the required size rather than guessing. If the user explicitly authorizes a recommendation, state the recommended dimensions and proceed.
- Record orientation, aspect ratio, bleed/safe margins where relevant, and intended output medium (print or digital).
- For print, confirm or recommend a print resolution (normally 300 DPI for small-format print) and calculate pixel dimensions from the physical size. Do not confuse aspect ratio with print resolution: a correctly proportioned image is not automatically print-ready.
- For digital artwork, record pixel dimensions and platform. Do not convert physical dimensions to pixels without a stated or agreed DPI.
- Include the agreed dimensions in the generation prompt, finishing/export settings and QA checklist. Verify the final export has the correct aspect ratio and dimensions.

## C. Prompt sections

1. **Deliverable:** purpose, platform, exact dimensions, orientation, print/digital medium and resolution.
2. **Art direction:** genre, emotional tone, style and fidelity to the supplied reference.
3. **Composition:** top/middle/bottom zones, focal point, relative scale, overlaps and reading path.
4. **Reference assets:** identify every image and state its role and defining visual characteristics. Do not say only “use attached images”.
5. **Environment:** background, palette, light direction, texture, depth, atmosphere and decorative elements.
6. **Typography:** reference-led display type; brand font fallback; exact script requirements; dimensional effects.
7. **Exact copy:** quote the user's text verbatim in a dedicated block. Clearly prohibit additions.
8. **Brand constraints:** exact logo handling, colour rules, prohibited substitutions and protected details.
9. **Negative constraints:** common failures specific to the task (generic replacement subjects, crude masks, wrong text, sticker-like assets, unwanted layout changes).
10. **Acceptance criteria:** observable tests, not vague words such as “beautiful” or “professional”.

## D. Reference-driven composition

When the user asks to match a reference, retain its distinctive visual grammar: layout, hierarchy, image scale, visual density, type treatment, colour relationships, lighting, ornament and texture. Replace only the elements the user asks to replace. Do not turn a maximalist illustrated festival poster into a minimalist card layout.

## E. Exact assets and model limits

Reference-guided image generation can create a coherent visual integration, but it may reinterpret details. Never promise pixel-perfect preservation from image generation. If exact logo fidelity is mandatory, place the original logo file in a finishing layer. For identity-critical subjects, inspect the result carefully and regenerate or use high-quality compositing if distorted.

## F. Text handling and reference-text fallback

Copy the exact user text into a locked text block. Do not generate extra captions. If the user has not supplied any text, inspect the reference image for intended wording and use its text when it is clearly part of the requested design. Treat the reference as the copy source only for wording the user has authorized by asking to use that reference; do not infer new facts from decorative or unrelated text. If the reference contains multiple possible text blocks and the intended one is unclear, ask one concise clarification. If the image model is unreliable with the language/script, ask it to leave a clean space for typography and add the text with a verified font in the finishing stage.

## G. Prompt completion test

Before invoking generation, verify that the prompt answers:
- What should the final image look like?
- Which reference controls the style and composition?
- Which uploaded image is which subject?
- What exact physical or pixel dimensions are required, and is the output print or digital?
- What exactly must remain unchanged?
- What exact text must appear?
- What must not appear?
- What visual evidence will make QA pass?
