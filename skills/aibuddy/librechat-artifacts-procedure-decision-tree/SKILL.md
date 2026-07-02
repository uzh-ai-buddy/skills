---
name: librechat-artifacts-procedure-decision-tree
description: Create Mermaid decision trees for student procedures with branching conditions.
metadata:
  triggers: [Entscheidungsbaum, flowchart, "je nach", "verschiedene Fälle", decision tree, "what do I do if..."]
---

# Procedure Decision Tree (Mermaid)

## Purpose
- Visualize administrative procedures and branching conditions as a decision tree.

## When to use
- The user asks for a procedure with conditional steps (illness on exam day, deadlines,
  exchange application flow, document submission paths).

## Output requirements
- Follow `librechat-artifacts-core` wrapper rules.
- Provide a brief 2–5 line summary in chat and exactly one artifact.
- Use `type="text/markdown"` and include exactly one Mermaid flowchart block.
- Keep node labels short and action-focused.
- **Do not** use Mermaid class syntax with `:::` inside the artifact.
- **Do not** use HTML `<br/>` tags in node labels—use `\n` for line breaks or keep labels single-line.

## Templates

- Generic decision tree skeleton:
  `references/01-decision-tree-skeleton.md`
- Exam illness example (no hardcoded deadlines):
  `references/02-decision-tree-exam-illness.md`
