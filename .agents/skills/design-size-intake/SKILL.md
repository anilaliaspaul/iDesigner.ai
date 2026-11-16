---
name: design-size-intake
description: Require explicit canvas dimensions for posters, flyers, invitations, banners and other fixed-size designs; ask for size when missing and distinguish print resolution from aspect ratio.
---

# Design size intake

Before producing any fixed-canvas design, inspect the current conversation and uploaded brief for the intended output size.

1. If the user already gave dimensions, use them. Never ask again for information already supplied.
2. If dimensions are missing, ask one concise question for width, height and unit. Examples: 10 cm × 15 cm, A4, or 1080 × 1350 px. Do not silently choose dimensions.
3. If the user does not know, recommend a suitable standard size for the intended use and ask them to confirm it. Do not proceed with an unconfirmed guess unless the user explicitly authorizes you to choose.
4. Record orientation, aspect ratio, intended medium (print or digital), and any relevant bleed/safe margins.
5. For print, normally recommend 300 DPI for small-format print and calculate pixel dimensions from the physical dimensions. Explain that aspect ratio alone does not guarantee print readiness.
6. For digital artwork, record pixel dimensions and platform. Do not convert physical size to pixels without an agreed DPI.
7. Carry the agreed size into the generation prompt, finishing/export settings and independent QA. Verify the exported dimensions and aspect ratio before delivery.

For all design work, also read and follow the main `graphic-design-studio` skill. This skill adds a mandatory intake check; it does not replace reference analysis, brand protection, exact-copy handling or QA.
