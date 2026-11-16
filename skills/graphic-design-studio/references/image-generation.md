# Image generation — first-class production route

## Runtime discovery

Use the image-generation tools actually available in the active host. Do not assume a specific provider, API key, model, endpoint or entitlement. If a tool supports image references, pass the user's actual reference and relevant assets through its supported image-reference mechanism. Do not replace image references with text descriptions alone when the actual images are available.

## When to generate

Prefer image-generation-first for expressive posters, illustrated festival artwork, campaign hero graphics, layered scenes, photomontage, cinematic compositions, complex backgrounds and art-directed imagery. Prefer editable-design-first for dense information, tables, schedules, repeated templates and precision typography. Use a hybrid pipeline when both artistic quality and exact content matter.

## How to prompt

Read `prompt-architecture.md`. Identify each image by role, not merely as “image 1”. State the reference's visual grammar and the exact assets' defining characteristics. Describe composition, foreground/middle/background, scale, overlaps, lighting, depth, palette, texture and typography treatment. Include exact copy in a locked block or instruct the model to leave clean typography space when text rendering is unreliable.

## Cohesive scene rule

Generate a complete coherent artwork. Do not generate separate floating subjects and paste them over a background. Do not create a finished background with fake subjects and then cover them with crude cutouts. Build the composition around the supplied reference assets from the start. Use proper compositing only where needed for exactness.

## Exact identity and logo

Image references guide the generator; they do not guarantee pixel-identical reproduction. Inspect faces, saints, architecture, products and other defining features. If the result changes identity, regenerate with stronger reference guidance or use a careful compositing route. For an official logo that must remain unchanged, place the original file as a separate finishing layer. Never recreate or redraw it.

## Text

Generated text may be inaccurate, especially in Malayalam and other complex scripts. If the exact wording is critical, leave a clean area for typography and finish it with an editable text/vector layer using a verified font. If the generated output includes text, proofread every character and correct it before delivery. Never invent text.

## Iteration

Diagnose the actual failure before regenerating. Change the prompt only where needed: wrong composition, incorrect asset identity, weak integration, poor typography, bad lighting, missing detail or incorrect text. Preserve successful aspects. Do not keep rerunning an unchanged prompt and hope for a different outcome.
