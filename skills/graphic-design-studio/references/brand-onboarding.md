# Brand onboarding

When the user chooses **Add a new brand**:

1. Ask for brand name and a short description/industry. Ask for logo, official colours, typography and any existing brand guide/reference artwork.
2. Run `python scripts/create_brand.py --slug <slug> --name "<name>"` from the plugin root.
3. Request or help populate `brand.json`, `palette/palette.json` and `design-readme.md` using only user-supplied or explicitly approved information.
4. Copy supplied logo files into `logos/` without modifying originals. Record which file is primary, monochrome, reversed and icon-only.
5. Copy font files only when the user has rights to use them. Otherwise record font family names and licensing/source notes.
6. Add approved references to `reference-designs/`; mark each reference as approved, inspiration-only or deprecated.
7. Run `python scripts/validate_brands.py --brand <slug>` and resolve errors.
8. Set `status` to `active` only after the user confirms the brand profile. Until then use `draft`.

Never infer official brand colours from a logo screenshot and silently declare them official. You may propose sampled colours, but label them `proposed` pending confirmation.
