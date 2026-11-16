# Canva editable handoff — mandatory after QA and user approval

Canva is not forced as the initial image renderer. It is the required final editable handoff after the artistic design passes independent QA and the user explicitly approves it.

## Gate order

1. Image-generation-led design and precise finishing are complete.
2. Independent pre-Canva QA passes all text, language, artifact, reference, asset, composition and technical checks.
3. User explicitly approves the artwork.
4. Create a new Canva design from the approved artwork.
5. Rebuild editable elements and verify the Canva preview.
6. Run post-Canva QA and deliver the edit URL.

Never create the final Canva handoff before both the pre-Canva QA PASS and user approval. A request to create a design is not approval of a particular final draft.

## Reconstruction requirements

1. Discover the connected Canva tools and schemas at runtime. Do not assume tool names or permissions.
2. Create a new Canva design with the approved dimensions. Keep the approved source artwork unchanged.
3. Upload the approved artwork as a full composition reference and, where needed, a background image layer.
4. Recreate all important text as native editable text elements. Match exact approved copy, font, size, line breaks, colour, alignment, outline/effects and placement.
5. Add exact official logos and user-provided images as separate image elements using the original source files and returned Canva asset IDs.
6. Recreate panels, shapes, borders, frames, ribbons, badges and decorative vectors as independent editable objects wherever practical.
7. Retain complex generated illustration/photo-art as a raster image/background layer if recreating it as editable vectors would be impractical or reduce fidelity. Do not pretend that such pixels are independently editable.
8. Where the design can be layered more fully, separate foreground, background, typography, logos, subject photos, overlays and decorative elements.
9. Do not simplify, redesign or change the approved composition during reconstruction.
10. Retrieve the actual Canva preview and edit URL. Run the full Canva reconstruction QA checklist.
11. If the preview differs materially from the approved artwork or text is not editable as promised, fix and inspect again.
12. Return the Canva edit URL, preview, approved export and an honest editability breakdown.

## Tool and connection limitations

- Canva MCP must be connected and authorized in the active client.
- Local brand files do not automatically sync to Canva. Upload files using the supported tool and use returned asset IDs.
- If Canva is unavailable, report: “Artwork approved; Canva editable handoff pending connection/tool availability.” Do not claim a design exists or provide a fabricated URL.
- Follow Canva's transaction and commit rules. Never overwrite an existing approved design without explicit authorization.

## Editability report

Explicitly list which components are:
- native editable text;
- separate image objects (logos, photographs, uploaded subjects);
- separate editable vector/shape elements;
- flattened generated artwork/background layers.

“Editable Canva design” means the document opens in Canva and its placed elements can be edited according to this breakdown. It does not mean every pixel of a generated raster illustration can be individually edited.
