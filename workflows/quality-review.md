# Quality Review and Approval Gate

This workflow is mandatory for every newly created design and every material revision. It is orchestrated by `skills/graphic-design-studio/SKILL.md` and executed by the independent `skills/quality-reviewer/SKILL.md`. Read `skills/graphic-design-studio/references/quality-review.md` as the detailed checklist.

## Required lifecycle

```text
Create or revise design
        |
        v
Inspect actual rendered preview/export
        |
        v
Run independent QA
        |
        +---- FAIL or UNKNOWN ----> Correct defects ----> Render again ----> Full QA again
        |
        v
QA PASS
        |
        v
Show preview + QA summary to user
        |
        v
Ask: "Do you approve this design?"
        |
        +---- No / changes requested ----> Revise ----> Render again ----> Full QA again
        |
        v
User explicitly approves
        |
        v
Ask: "Would you like me to open this design in Canva?"
        |
        +---- No ----> Do not open Canva; continue with agreed deliverables
        |
        v
User explicitly agrees
        |
        v
Open the exact verified Canva design URL using the connected Canva/open-URL capability
```

## QA execution rules

1. Invoke the Quality Reviewer skill after the first complete render. Do not ask the user to approve before QA.
2. The reviewer must inspect the actual rendered artifact, not only a design prompt, source code, textual description or tool success message.
3. Run semantic/message review first, exact-copy and fact verification second, brand/assets third, visual/accessibility fourth, and technical/export checks fifth.
4. Require explicit PASS / FAIL / UNKNOWN results with evidence. A critical UNKNOWN blocks approval.
5. If QA returns FAIL or UNKNOWN, do not show the design as approval-ready. Fix defects, create a new version and rerun the full QA process.
6. After QA PASS, show the actual preview and a concise QA report. State any accepted minor limitations. Then ask for explicit user approval.
7. If the user requests changes or declines approval, revise only the requested elements, preserve approved elements, and rerun QA on the revised version.
8. User approval must be explicit. Silence, positive comments about one element, or a request to see a preview do not count as approval.
9. Only after explicit user approval, ask separately whether the user wants the design opened in Canva. Do not combine this with the approval question.
10. If the user agrees, open the exact Canva design URL returned by the connected tool. If no valid Canva URL or open capability exists, explain the limitation and provide the verified edit URL if available. Never invent a link.
11. If the user declines, do not launch Canva or perform an equivalent automatic handoff.
12. Record QA decision, evidence, defects, fixes, version, user approval and Canva handoff choice in the project record.

## Mandatory QA decision

Return PASS / FAIL / UNKNOWN. A visually attractive design must fail if its message is redundant, unclear, misleading, factually wrong, brand-inconsistent or unsuitable for its audience. UNKNOWN is not PASS. Preserve all user-approved wording and factual details; never invent replacement claims.
