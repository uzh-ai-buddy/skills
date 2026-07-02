---
name: librechat-artifacts-markdown
description: Create clean Markdown artifacts with progressive disclosure for student-facing deliverables.
metadata:
  triggers: [Checkliste, Anleitung, Plan, Zusammenfassung, guide, report]
---

# LibreChat Markdown Artifacts

## When to use
- The user asks for a plan, checklist, guide, template, report, or other document-like output.
- The output should be reusable or shareable outside the chat.

## Inputs to collect
- Goal/outcome and who the artifact is for.
- Required sections or format preferences.
- Constraints (deadline, length, tone, language).
- Key facts, sources, or policies to include.

## Output requirements
- Provide a **2–5 line summary in chat**.
- Provide **exactly one Markdown artifact** with a clear title.
- Use progressive disclosure: short summary up front, details in later sections, and optional appendix.
- Follow wrapper rules in `librechat-artifacts-core`.
- Use `type="text/markdown"` (or `text/md`).

## Structure checklist
- Title
- Summary (bullets)
- Main body (sections with headings)
- Assumptions / Open questions
- Next steps
- Optional appendix (examples, templates, references)

## Steps
1. Confirm the goal, audience, and constraints.
2. Choose a clear artifact title and identifier.
3. Draft a short Summary section first.
4. Add structured sections with headings and bullet points.
5. Add Assumptions/Open Questions and Next steps.
6. Validate completeness and ask for missing info.
