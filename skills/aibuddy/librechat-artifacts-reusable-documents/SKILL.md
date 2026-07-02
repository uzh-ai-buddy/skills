---
name: librechat-artifacts-reusable-documents
description: Create editable long-form document templates (letters, statements) as Markdown artifacts.
metadata:
  triggers: [Vorlage, Entwurf, Template, Muster, E-Mail, Motivationsschreiben, motivation letter, email draft]
---

# Reusable Document Artifacts (Markdown)

## Purpose
- Provide editable, long-form document drafts that students can copy and customize.

## When to use
- The user asks for a motivation letter, statement of purpose, email draft, or similar long-form
  document meant for editing.

## Output requirements
- Follow `librechat-artifacts-core` wrapper rules.
- Use `type="text/markdown"`.
- Include a 1–2 sentence preface outside the artifact that the draft is editable.
- Minimum length: 15 lines of text inside the artifact.
- Use clear placeholder tokens (e.g., `{{Name}}`, `{{Program}}`).
- Provide 3+ labeled sections (Introduction, Academic Fit, etc.).
- Use a professional tone; keep hints in brackets sparingly.

## Templates

- Motivation letter draft:
  `references/01-motivation-letter.md`
- Formal request email to an office:
  `references/02-formal-email-to-office.md`
