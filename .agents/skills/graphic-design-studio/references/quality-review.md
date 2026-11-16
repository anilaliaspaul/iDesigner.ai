# Independent Quality Assurance — mandatory approval gate

The QA reviewer must inspect the actual generated artwork, final export and (after approval) Canva reconstruction. Do not approve based on the prompt, a designer's self-assessment or a tool's success response. Return PASS / FAIL / UNKNOWN with evidence. UNKNOWN is never PASS.

## 1. Copy, spelling, grammar and sentence quality

- Compare all visible wording against the user-approved copy and verified fact sheet.
- Check spelling, grammar, punctuation, capitalization, sentence structure, completeness, readability and tone.
- Identify awkward phrasing, duplicated meaning, broken sentences, missing words, incorrect names, dates, weekdays, times, venues, URLs, prices, contact information and scripture references.
- Use OCR/text extraction when available to identify rendered text, then manually inspect the image. OCR is not a substitute for visual review.
- Inspect small text, background signs, decorative labels, banners, badges, clothing, buildings, book covers, watermark-like areas and all other visible regions.
- Flag random words, fake language, malformed letters, pseudo-text, gibberish, unintended numerals, duplicated phrases, invented labels, hallucinated dates, fake sponsor names, fake logos and watermarks.
- Any unrequested text or pseudo-text is FAIL, even if the main copy is correct.
- User-provided wording is locked. Do not silently correct or paraphrase it. If it contains an error, report the exact issue and propose a correction for user approval. Re-run QA against the newly approved copy.
- For Malayalam or other complex scripts, inspect shaping, conjuncts, chillu letters, vowel signs, combining marks, punctuation and line wrapping. Never detach marks or split words.

## 2. AI-generated image and visual artifact review

Inspect at full resolution and at the intended viewing size. Look for:
- low-quality, generic or visibly synthetic assets that conflict with the requested style;
- distorted faces, inconsistent identity, strange anatomy, malformed hands, duplicated limbs or objects;
- warped buildings, incorrect church architecture, impossible perspective or inconsistent scale;
- objects, symbols, decorations or people that were never requested;
- inconsistent lighting, shadows, reflections, colour temperature, depth or perspective;
- sticker-like cutouts, floating subjects, visible masks, jagged edges, white halos, smudges, texture seams, blur patches and unnatural glow;
- corrupted lettering, pseudo-words, accidental symbols, AI watermarks, fake logos and text embedded in generated imagery;
- missing details, clipped objects, merged forms, repeated patterns or obvious generation artifacts.

A generated image does not fail merely because it is AI-generated. It fails when its quality, artifacts, style or inaccuracies undermine the brief or the requested finish. The reviewer must distinguish deliberate artistic stylization from accidental generation defects.

## 3. Reference fidelity and design quality

Compare side-by-side with the supplied reference. Check:
- composition zones, focal point, hierarchy and reading path;
- relative placement, scale, overlap and negative space;
- typography style, effects, letterform character and visual weight;
- palette, colour distribution, contrast and background treatment;
- texture, lighting, atmosphere, depth, ornament and visual density;
- whether the result belongs to the same visual design family as the reference.

Do not impose minimalism on a richly layered reference. A design that contains the correct subjects but looks unrelated to the reference is FAIL. Score user-emphasized dimensions from 1–5; below 4 is FAIL.

## 4. Asset, identity and brand integrity

- Verify exact source files for logos and required identity-critical assets.
- Check face, age, facial features, hairstyle, skin tone, expression, clothing and other defining details against supplied people references, as relevant.
- Check exact saint iconography, vestments, halo, objects and defining features.
- Check recognizable building architecture, roof, windows, cross, facade and proportions.
- Verify correct logos, fonts, palette and brand rules.
- Wrong or materially distorted required assets are automatic FAIL.
- A generated approximation is not a substitute for a supplied exact logo or protected identity asset.

## 5. Composite and visual integration

- Every subject should belong naturally to the scene.
- Verify consistent perspective, scale, lighting direction, colour temperature, contrast, depth and occlusion.
- Reject crude cutouts, white rectangles/ovals, sticker edges, arbitrary glow outlines, floating buildings and detached shadows unless explicitly required by the reference.
- Inspect fine edges and details: hair, smoke, robes, white garments, halo details, chains, foliage, rooflines and crosses.

## 6. Layout, typography and technical output

- Verify readability, text contrast, alignment, spacing, margins, clipping, overlaps and safe areas.
- Verify correct output dimensions, aspect ratio, resolution, crop and export integrity.
- Inspect full-size and mobile/target-size preview.
- Verify no unwanted content has entered the background or been lost from the foreground.

## 7. Canva reconstruction QA (mandatory after user approval)

Compare the Canva preview with the user-approved artwork:
- all exact copy is present, spelled correctly and editable as text where practical;
- no text is duplicated, missing, misspelled, reflowed incorrectly or newly hallucinated;
- logos and uploaded assets are separate elements and use the correct source files;
- shapes, panels and decorative elements are layered separately when practical;
- artwork composition, dimensions, spacing, colour, hierarchy and image placement remain faithful;
- no missing fonts, unexpected substitutions, clipping, overflow or element misalignment;
- editability claims accurately distinguish native Canva objects from flattened raster layers.

A Canva design is not complete until this second QA pass succeeds.

## Decision rule

Any incorrect fact, unapproved text, random AI pseudo-text, material spelling/grammar error, wrong logo/subject, identity distortion, serious AI artifact, broken layout or failed reference criterion is FAIL. Fix, regenerate or revise and repeat QA. Only a full PASS can be presented for user approval. User approval is separate and mandatory. Canva delivery is then mandatory, followed by a second QA pass.
