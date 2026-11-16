# Export and Canva handoff

This workflow is orchestrated by `skills/graphic-design-studio/SKILL.md`. Preserve selected brand rules, approved copy, QA evidence and version history.

## Mandatory sequence

1. A complete rendered design must pass the independent Quality Reviewer gate before it is presented for user approval.
2. If QA is FAIL or UNKNOWN, fix defects and rerun QA. Do not export or describe the design as final.
3. After QA PASS, show the actual preview and QA summary and ask for explicit user approval.
4. If the user requests changes, revise and repeat QA.
5. After explicit user approval, ask separately whether the user wants the design opened in Canva.
6. Open Canva only after the user explicitly agrees. Use the exact verified Canva URL returned by the connected tool. Never invent a URL or claim success without confirmation.
7. If the user declines the Canva handoff, do not open Canva.
8. Export the requested formats using the connected export capability. For print, select PDF Print where available and verify dimensions, bleed and resolution requirements.
9. Record the approved version, QA result, user approval, Canva handoff choice, export metadata and verified URLs.

User approval is not consent to open Canva. QA PASS is not user approval. Keep all three decisions separate.
