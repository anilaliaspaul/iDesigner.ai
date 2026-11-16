---
name: graphic-design-skills-collection
description: Curated catalogue and router for the studio’s graphic-design specialist skills, workflows, tools and upstream references.
---

# Graphic Design Skills Collection

This skill is the index/router for the studio's specialist capabilities. Read only the specialist skill needed for the current task, then return to the main studio orchestration workflow for brand checks, approval and versioning.

## Included capabilities
| Skill | Use it for | Main output |
|---|---|---|
| `canvas-design` | Original visual-first static compositions | Editable vector/HTML source where possible; PNG/PDF |
| `poster-design` | Event, campaign and informational posters | Editable poster + print/digital exports |
| `algorithmic-art` | Procedural patterns, generative illustration and textures | Reproducible source + rendered artwork |
| `brand-guidelines` | Brand onboarding and enforcement | Brand profile, asset/font inventory, usage rules |
| `adobe-design-from-template` | Adobe Express template selection and customization | Express document + supported exports |
| `graphic-design-studio` | End-to-end design orchestration | Brand-aware project, revisions and approved exports |
| `layout-typography` | Grid, hierarchy, multilingual typesetting | Layout and typography specification |
| `image-specialist` | Supporting image creation and image treatment | Approved imagery, never generated logos/text |
| `quality-reviewer` | Final design audit | QA findings and release checklist |

## Routing rules
- Posters: `poster-design` + `brand-guidelines` + `layout-typography`; use `canvas-design` when the piece is visual-first.
- Generative textures or abstract visuals: `algorithmic-art` + `image-specialist` as needed.
- Adobe Express request or template workflow: `adobe-design-from-template`.
- Brand onboarding, refresh or consistency audit: `brand-guidelines`.
- Every production task returns to `graphic-design-studio` for the official-logo gate, exact-copy policy, user approval and version control.

## Upstream skill collection
This is a curated integration, not a promise that every repository under the GitHub topic is installed. The source catalogue is `references/upstream-skill-catalog.md`. Review each upstream project's licence, security, dependencies and tool requirements before importing additional code or assets.
