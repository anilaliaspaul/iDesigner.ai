---
name: adobe-design-from-template
description: Find and customize an Adobe Express template for flyers, posters, social posts, invitations and other branded collateral when the Adobe connector is available.
---

# Adobe Design from Template Skill

## Purpose
Use Adobe Express templates as an alternate rendering path alongside Canva. This skill requires the Adobe for Creativity connector and only uses actions exposed by the current host.

## Capability check
1. Discover whether the Adobe for Creativity connector is connected and authorized.
2. Run its mandatory initialization action first if exposed by the connector.
3. Inspect the live available actions. Common workflow actions may include template search, text fill, image replacement, background colour changes, animation and PDF export, but availability varies by host and account.
4. If the connector or required action is unavailable, state that clearly and route to Canva or another actually available renderer. Never pretend Adobe actions succeeded.

## Template workflow
1. Extract the design type from the request and search for templates using the generic type (for example, event poster, invitation or Instagram post).
2. Present the available template choices with preview and editor links when returned. Do not silently choose a template for the user.
3. Wait for explicit template selection. A request describing edits is not itself a template selection.
4. Apply only user-provided or approved copy. If text is missing, ask before filling text fields.
5. Replace imagery only with approved assets or a user-authorized generated visual. Never replace an official logo with generated artwork.
6. Make requested background/animation changes only when supported by the live connector.
7. Export only when the export action is available and the user requests a file. Present the returned editor and download links.

## Studio safeguards
- Brand audit and official-logo hard stop apply equally to Adobe Express templates.
- Never add unrequested copy, slogans, captions, scripture, labels, dates or pseudo-text.
- Preserve Malayalam/English mixed text exactly; verify glyph shaping and line wrapping in the final Adobe export.
- Keep the result minimalist, uncluttered and consistent with the selected brand.
- Do not assume Canva assets, local fonts or brand kits are automatically available inside Adobe Express.

## Connector limitations
Template results, editing actions, animation and exports vary by host, connector permissions and subscription. Report only capabilities confirmed in the current session.
