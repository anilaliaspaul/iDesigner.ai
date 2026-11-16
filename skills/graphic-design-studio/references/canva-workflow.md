# Canva workflow

Canva is the primary editable design surface. Use the connected Canva MCP tools available in the current host. Tool names and schemas can change; discover the current tool list and read descriptions before calling tools.

## New design

1. Search brand kits and brand templates if the user expects brand fidelity and those capabilities are available.
2. Inspect template suitability and fillable fields before choosing autofill.
3. If using local assets, upload them through Canva's supported upload flow and use returned asset IDs. Never fabricate asset IDs or assume local paths are directly visible to Canva.
4. Use design generation for an editable Canva page/layout. Use image generation only for supporting flat image assets.
5. Place exact logos, text and supplied facts as editable elements whenever possible.
6. Wait for asynchronous generation jobs according to the returned polling instructions. Do not claim success before completion.

## Revisions

1. Inspect the design and its pages/content before editing.
2. Start an editing transaction when required by the available tools.
3. Apply targeted changes in batches.
4. Retrieve a new thumbnail/preview and show it to the user.
5. Obtain explicit approval before committing changes when the tool requires it.

## Export

Use Canva's export tools and supported formats. Confirm export job completion and provide the resulting file/link. Keep the Canva edit link in the local project record.

## Local assets vs Canva brand kits

The local `resources/brands` folder is the studio's source of truth, but it does not automatically sync to Canva. Upload assets as needed and use Canva Brand Kits/Templates only when they are actually present and accessible to the authenticated user. Do not claim a local brand profile is a Canva Brand Kit.


## Strict brand, logo and text controls
- Upload the exact approved logo from the selected brand folder. Never create or approximate a logo. If absent, stop and request the official file.
- Use approved local font files only when Canva supports the font upload/use path and the account is authorized. Otherwise ask for an approved Canva font or approved fallback; do not silently substitute.
- Place Malayalam and English copy as editable text. Keep full phrases intact; use separate text elements for script runs if required for shaping, but preserve natural sentence order.
- Do not use AI-generated text inside image assets. All requested wording must be added as editable text from the approved brief.
- Keep the composition restrained and minimalist. Remove any unrequested visual or textual element before preview.
