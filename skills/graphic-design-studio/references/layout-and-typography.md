# Layout, typography and multilingual copy integrity

## Professional minimalist visual standard
- Default to restrained editorial/minimalist design, not maximalist AI-generated poster aesthetics.
- Use one primary focal point, one clear reading path, a disciplined grid, consistent spacing and generous negative space.
- Limit the composition to a small number of meaningful elements. Use decoration only when it communicates something in the brief or approved brand language.
- Prefer a strong typographic composition and one purposeful image over many unrelated generated objects.
- Avoid visual noise: random floating words, fake labels, arbitrary icons, stickers, badges, seals, fake stamps, decorative microcopy, excessive gradients, glow, particles, 3D effects, collages and generic AI flourishes.
- Every element must have a reason. If removing it improves clarity, remove it.
- Do not copy generic AI poster tropes. Aim for the quality of a considered editorial designer or experienced event-design studio.

## Typography system
- Use brand-approved display, heading, body and numeral styles. Respect exact font files and licensing notes in `resources/brands/<brand>/typography/`.
- Do not select a font solely because it looks attractive. Confirm it supports every script used in the artwork.
- Use no more than 2 font families by default. A third is allowed only when the brand guide explicitly calls for it.
- Do not fake bold/italic where actual font weights exist. Avoid ultra-thin weights for small or mixed-script copy.
- Keep body copy readable at actual mobile/print size. Do not compress tracking or horizontally scale text to force a fit.
- Use proper line-height and enough space between Malayalam and English runs. Do not mix unrelated typefaces within one sentence unless required by the approved brand system.

## Malayalam + English mixed-language integrity
- Treat every supplied Malayalam or English sentence/phrase as an indivisible copy unit. Preserve the exact characters, spelling, punctuation, word order and language; never translate, transliterate, paraphrase or split a phrase without permission.
- Never insert manual line breaks inside a Malayalam word, English word, URL, name, or a user-supplied phrase. Prefer line breaks between complete phrases or clauses.
- If a sentence cannot fit cleanly, change the text-box width, font size, layout or hierarchy. Do not break words, separate Malayalam vowel signs/diacritics from their base characters, or squeeze the line.
- Preserve Unicode text exactly. Do not normalize by deleting combining marks or punctuation. Check conjuncts, chillu letters, vowel signs, anusvara/visarga and punctuation visually.
- Ensure the chosen Malayalam font has full glyph coverage and correct shaping. A font that merely contains Malayalam-looking glyphs is not sufficient; verify conjunct shaping and rendering in Canva preview/export.
- Keep Malayalam and English together as a coherent typographic system. Use compatible font weights, optical sizes and baseline alignment. A single text box may not render mixed scripts correctly in every font, so separate language runs into adjacent editable text boxes when necessary while preserving sentence order and natural reading flow.
- Do not use transliteration (Manglish) unless explicitly requested. Do not automatically convert Malayalam into English or vice versa.
- If the text is too long for the format, ask whether the user wants a shorter approved version. Never shorten it yourself if exact wording is required.
- Review the actual Canva preview at intended display size and exported file. Check line wraps, ligatures, shaping, spacing, clipping and glyph substitutions.

## Text integrity workflow
1. Store approved copy verbatim in the project brief.
2. Mark each text block with language/script (`ml`, `en`, or `mixed`) and whether wording is locked.
3. Keep each sentence/phrase as an intact text block unless the user approves a line-break plan.
4. Compare rendered text against source copy character-for-character where possible.
5. Manually inspect Malayalam shaping and mixed-language line breaks in Canva preview and export.
6. If rendering is uncertain, stop and ask for an approved font or an alternate layout. Never silently substitute tofu boxes or broken glyphs.
