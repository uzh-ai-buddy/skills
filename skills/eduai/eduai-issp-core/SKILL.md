---
name: eduai-issp-core
description: Use for questions about the Integrierter Supportprozess Studienprogrammentwicklung (ISSP), process routing, glossary terms, quality criteria, governance, and artefacts for UZH study program development.
always-apply: true
---

# EduAI ISSP Core

Use this skill for every Baltibot answer about the Integrierter Supportprozess
Studienprogrammentwicklung (ISSP).

## Required Workflow

1. Route the user question through `references/issp_process_router.md`.
2. Select the relevant process context from `references/issp_process_context.md`.
3. Use `references/issp_glossary_usage.md` and the glossary references for terminology.
4. Use doc-query MCP for detailed source-grounded ISSP content before final answers.
5. Answer with written process names, not internal process codes.

## References

- `references/issp_process_router.md`
- `references/issp_process_context.md`
- `references/issp_process_diagramm.md`
- `references/issp_glossary_usage.md`
- `references/issp-glossary-01.md`
- `references/issp-glossary-02.md`

## Output Rules

- Do not expose internal routing codes such as `K1`, `E4`, `QM`, or `O`, unless the user
  explicitly asks about the internal process notation.
- Use the canonical ISSP terms from the glossary.
- Treat glossary definitions as authoritative when users ask what a term means.
- Use retrieved ISSP document content for operational details, examples, and source-specific
  claims.
